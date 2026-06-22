#!/usr/bin/env bash
# telegram-polling.sh — Daemon de long polling persistente.
# Gerenciado pelo launchd com KeepAlive=true. Reinicia automaticamente se morrer.
# Long polling: getUpdates com timeout=25 → resposta em ~1-2s após envio.
set -uo pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SECRETS="$VAULT/scripts/.secrets"
SEND_SCRIPT="$VAULT/scripts/lib/send-telegram.sh"
OFFSET_FILE="/tmp/telegram-polling-offset.txt"

# Copia lib e secrets para /tmp ao iniciar — evita deadlock do OneDrive no importlib/leitura
LIB_DIR="/tmp/tg-lib"
SECRETS_TMP="/tmp/tg-secrets"
mkdir -p "$LIB_DIR" "$SECRETS_TMP"
cp -f "$VAULT/scripts/lib/"*.py "$LIB_DIR/" 2>/dev/null || true
cp -f "$SECRETS/"* "$SECRETS_TMP/" 2>/dev/null || true
PARSE_SCRIPT="$LIB_DIR/parse-captura.py"
export TG_VAULT_PATH="$VAULT"
export TG_SECRETS_PATH="$SECRETS_TMP"

# No Railway, as variáveis já estão no ambiente (herdadas do startup Python).
# Localmente, carrega do arquivo de secrets.
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
    source "$SECRETS/telegram.env"
fi
echo "[startup] TOKEN_PREVIEW=${TELEGRAM_BOT_TOKEN:0:10}... len=${#TELEGRAM_BOT_TOKEN}"

# Arquivo temporário fixo por PID — sem mktemp no loop
TMP="/tmp/tg-polling-$$.json"
trap 'rm -f "$TMP"' EXIT TERM INT

echo "[$(date '+%H:%M:%S')] Telegram polling daemon iniciado (long-poll mode, PID=$$)"

# ── Loop principal ────────────────────────────────────────────────────────────
while true; do
    OFFSET=0
    [ -f "$OFFSET_FILE" ] && OFFSET=$(cat "$OFFSET_FILE")

    # Long polling: bloqueia até 25s esperando mensagem nova no Telegram.
    # Quando chega mensagem, retorna imediatamente — daí a latência baixa.
    if ! curl -sf \
        "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/getUpdates?offset=${OFFSET}&timeout=25" \
        -o "$TMP" 2>/dev/null; then
        echo '{"result":[]}' > "$TMP"
        sleep 3  # Back-off em caso de falha de rede
    fi

    export TMP PARSE_SCRIPT SEND_SCRIPT OFFSET_FILE TELEGRAM_CHAT_ID TELEGRAM_BOT_TOKEN LIB_DIR TG_VAULT_PATH TG_SECRETS_PATH

    python3 << 'PYEOF'
import json, os, subprocess, sys, importlib.util, urllib.request

tmp         = os.environ["TMP"]
script      = os.environ["PARSE_SCRIPT"]
send_script = os.environ["SEND_SCRIPT"]
offset_f    = os.environ["OFFSET_FILE"]
expected    = os.environ["TELEGRAM_CHAT_ID"]
bot_token   = os.environ["TELEGRAM_BOT_TOKEN"]
lib_dir     = os.environ["LIB_DIR"]


def _load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


state_mgr = _load_mod("state_manager",   f"{lib_dir}/state-manager.py")
router    = _load_mod("telegram_router",  f"{lib_dir}/telegram-router.py")


try:
    data = json.loads(open(tmp).read())
except Exception:
    sys.exit(0)


def _send(msg):
    try:
        subprocess.run(["bash", send_script, msg, "HTML"],
                       capture_output=True, timeout=10)
    except Exception:
        pass


def _answer_callback(callback_id):
    try:
        url  = f"https://api.telegram.org/bot{bot_token}/answerCallbackQuery"
        body = json.dumps({"callback_query_id": callback_id}).encode()
        req  = urllib.request.Request(url, data=body,
                                      headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass


def _build_confirmation(cap):
    if cap.get("inbox_path"):
        fname = cap["inbox_path"].split("/")[-1]
        return (
            f"✓ <b>Salvo no inbox</b>\n\n"
            f"📝 <b>Nota:</b> {cap.get('titulo','')}\n"
            f"📁 <b>Arquivo:</b> {fname}"
        )
    lines = [
        "✓ <b>Capturado</b>", "",
        f"📝 <b>Título:</b> {cap.get('titulo','')}",
        f"🏢 <b>Frente:</b> {cap.get('frente','')}",
        f"📂 <b>Tipo:</b>   {cap.get('tipo','')}",
    ]
    data_val = cap.get("data")
    hora     = cap.get("hora")
    if data_val:
        data_fmt = data_val[8:10] + "/" + data_val[5:7]
        lines.append(f"📅 <b>Data:</b>  {data_fmt}" + (f" às {hora}" if hora else ""))
    url = cap.get("notion_url")
    if url:
        lines.append(f'📲 <a href="{url}">Abrir no Notion</a>')
    lines.append("🗓️ <i>Calendar: sync em ~7h (daily-brief)</i>")
    return "\n".join(lines)


results = data.get("result", [])
max_id   = 0

for u in results:
    uid    = u.get("update_id", 0)
    max_id = max(max_id, uid + 1)

    # ── Mensagem de texto ──────────────────────────────────────────────────
    if "message" in u:
        msg     = u["message"]
        chat_id = str(msg.get("chat", {}).get("id", ""))
        text    = msg.get("text", "").strip()

        if not text or chat_id != expected:
            continue

        if router.route_message(chat_id, text, _send):
            continue

        # Captura (lógica original)
        env = os.environ.copy()
        env["CAPTURA_ORIGEM"] = "Telegram"

        r = subprocess.run(
            ["python3", script, text],
            capture_output=True, text=True, env=env, timeout=30
        )

        if r.returncode == 0:
            try:
                cap = json.loads(r.stdout)
            except Exception:
                cap = {"status": "ok", "notion_url": r.stdout.strip()}
            _send(_build_confirmation(cap))
            state_mgr.set_last_capture(chat_id, cap)
            print(f"[{__import__('datetime').datetime.now().strftime('%H:%M:%S')}] captura ok: {text[:50]!r}")
        else:
            err = r.stderr.strip()[:200]
            _send(f"❌ <b>Captura falhou</b>\n\n<code>{err}</code>")
            print(f"[ERRO captura] {err}", file=sys.stderr)

    # ── Callback de botão inline ───────────────────────────────────────────
    elif "callback_query" in u:
        cq      = u["callback_query"]
        cq_id   = str(cq.get("id", ""))
        chat_id = str(cq.get("message", {}).get("chat", {}).get("id", ""))
        cb_data = cq.get("data", "")

        if chat_id != expected:
            continue

        router.route_callback(chat_id, cb_data, lambda cid=cq_id: _answer_callback(cid))

if max_id > 0:
    open(offset_f, "w").write(str(max_id))
PYEOF

    # Sem sleep: curl já bloqueia 25s quando não há mensagens
done
