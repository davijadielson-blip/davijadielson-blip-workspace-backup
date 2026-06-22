#!/bin/bash
# end-of-day-reminder.sh — Roda todo dia às 17h (via launchd)
# Fechamento do dia: pendências abertas + agenda de amanhã. Telegram + Email.

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
TOMORROW=$(date -v+1d +%Y-%m-%d 2>/dev/null || date -d "+1 day" +%Y-%m-%d)
WEEKDAY=$(date +%u)

# Domingo: silencioso
[ "$WEEKDAY" -eq 7 ] && exit 0

source "$VAULT/scripts/.secrets/notion.env"
source "$VAULT/scripts/.secrets/telegram.env"

# ── Captura Geral: itens de hoje ainda abertos ────────────────────────────────
HOJE_ABERTOS=$(python3 << PYEOF
import json, urllib.request
from datetime import date

token  = "$NOTION_TOKEN"
db_id  = "$NOTION_CAPTURA_DATABASE_ID"
today  = date.today().isoformat()
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
payload = json.dumps({
    "filter": {
        "and": [
            {"property": "Data",   "date":   {"equals": today}},
            {"property": "Status", "select": {"does_not_equal": "Concluído"}},
            {"property": "Status", "select": {"does_not_equal": "Cancelado"}},
        ]
    },
    "page_size": 8,
}).encode()

try:
    req = urllib.request.Request(
        f"https://api.notion.com/v1/databases/{db_id}/query",
        data=payload, headers=headers, method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    for page in data.get("results", []):
        props = page.get("properties", {})
        title_parts = props.get("Título", {}).get("title", [])
        titulo = "".join(t.get("plain_text","") for t in title_parts).strip() or "(sem título)"
        frente = (props.get("Frente",{}).get("select") or {}).get("name", "")
        label  = f" [{frente}]" if frente else ""
        print(f"• {titulo}{label}")
except Exception as e:
    print(f"(erro ao buscar Notion: {e})")
PYEOF
)

# ── Captura Geral: agenda de amanhã ───────────────────────────────────────────
AMANHA_ITEMS=$(python3 << PYEOF
import json, urllib.request

token  = "$NOTION_TOKEN"
db_id  = "$NOTION_CAPTURA_DATABASE_ID"
tomorrow = "$TOMORROW"
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
payload = json.dumps({
    "filter": {
        "and": [
            {"property": "Data",   "date":   {"equals": tomorrow}},
            {"property": "Status", "select": {"does_not_equal": "Cancelado"}},
        ]
    },
    "sorts": [{"property": "Data", "direction": "ascending"}],
    "page_size": 8,
}).encode()

try:
    req = urllib.request.Request(
        f"https://api.notion.com/v1/databases/{db_id}/query",
        data=payload, headers=headers, method="POST"
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())
    for page in data.get("results", []):
        props = page.get("properties", {})
        title_parts = props.get("Título", {}).get("title", [])
        titulo = "".join(t.get("plain_text","") for t in title_parts).strip() or "(sem título)"
        frente = (props.get("Frente",{}).get("select") or {}).get("name", "")
        hora_raw = (props.get("Data",{}).get("date") or {}).get("start","")
        hora = hora_raw.split("T")[1][:5] if "T" in hora_raw else ""
        prefix = f"• {hora} — " if hora else "• "
        label  = f" [{frente}]" if frente else ""
        print(f"{prefix}{titulo}{label}")
except Exception as e:
    print(f"(erro ao buscar Notion: {e})")
PYEOF
)

# ── Pendências importantes ─────────────────────────────────────────────────────
IMPORTANTES=$(awk '/## 🟡 Importantes/,/## ⚪/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null \
  | grep "^\- \[ \]" | sed 's/^- \[ \] //' | head -3 || true)

# ── Monta mensagem ─────────────────────────────────────────────────────────────
build_bullets() {
  local input="$1" prefix="${2:-  • }" empty="${3:-<i>nenhum</i>}"
  local out=""
  while IFS= read -r line; do [[ -z "$line" ]] && continue; out+="${prefix}${line}\n"; done <<< "$input"
  echo -e "${out:-  ${empty}}"
}

ABERTOS_BULLETS=$(build_bullets "$HOJE_ABERTOS" "  ⚠️ " "<i>nenhum — ótimo dia!</i>")
AMANHA_BULLETS=$(build_bullets "$AMANHA_ITEMS"  "  "    "<i>nada agendado</i>")
IMP_BULLETS=$(build_bullets "$IMPORTANTES"      "  • "  "<i>nenhuma</i>")

TG_MSG="🌙 <b>Fechamento do dia — 17h</b>
<i>30 minutos para Ancoragem (família 18h+)</i>

<b>⚠️ Ficou em aberto hoje</b>
${ABERTOS_BULLETS}
<b>📅 Amanhã — $(date -v+1d '+%d/%m' 2>/dev/null || date -d '+1 day' '+%d/%m')</b>
${AMANHA_BULLETS}
<b>🟡 Em andamento (semana)</b>
${IMP_BULLETS}
<b>✅ Antes de fechar</b>
  • Rode <code>/salve</code> no terminal
  • Empurre pendências pra amanhã se necessário

<i>Bom descanso, Jadielson. 🙏</i>"

"$VAULT/scripts/lib/send-telegram.sh" "$TG_MSG" "HTML" || true

"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Fechamento 17h — $(date '+%d/%m/%Y')" \
  "$TG_MSG" 2>/dev/null || true
