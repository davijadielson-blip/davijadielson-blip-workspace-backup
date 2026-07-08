"""
telegram-commands.py — Handlers dos 8 comandos interativos do bot Telegram.
Fase 2: /start, /status, /agenda, /buscar
Fase 3: /confirmar, /cancelar, /repetir
Fase 4: /menu
"""
import html
import importlib.util
import json
import os
import subprocess
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

_HERE = Path(__file__).parent
_vault_env = os.environ.get("TG_VAULT_PATH", "")
VAULT = Path(_vault_env) if _vault_env else _HERE.parent.parent
_secrets_env = os.environ.get("TG_SECRETS_PATH", "")
SECRETS = Path(_secrets_env) if _secrets_env else VAULT / "scripts" / ".secrets"

# ── Módulos auxiliares — carregados UMA VEZ para evitar EDEADLK do OneDrive ──
# Cada exec_module relê o .py do disco; se o OneDrive estiver sincronizando = crash.
# Carregando aqui (no startup do módulo, a partir de /tmp/tg-lib) o problema não ocorre.
def _load_once(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

_LIB_TMP = Path("/tmp/tg-lib")

def _lib_path(fname):
    p = _LIB_TMP / fname
    return p if p.exists() else _HERE / fname

_sm_mod  = _load_once("state_manager", _lib_path("state-manager.py"))
_pc_mod  = _load_once("parse_captura", _lib_path("parse-captura.py"))

def _cg():
    """Carregamento lazy do módulo claude-gerar (evita falha no startup sem chave)."""
    return _load_once("claude_gerar", _lib_path("claude-gerar.py"))

# ── Secrets ──────────────────────────────────────────────────────────────────

def _load_env(path):
    env = {}
    try:
        for line in Path(path).read_text().splitlines():
            line = line.strip()
            if "=" in line and not line.startswith("#"):
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"')
    except Exception:
        pass
    return env

_tg = _load_env(SECRETS / "telegram.env")
BOT_TOKEN = _tg.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID   = _tg.get("TELEGRAM_CHAT_ID", "")

# ── Send helpers ──────────────────────────────────────────────────────────────

def _api(method, payload):
    url  = f"https://api.telegram.org/bot{BOT_TOKEN}/{method}"
    body = json.dumps(payload, ensure_ascii=False).encode()
    req  = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        urllib.request.urlopen(req, timeout=10)
    except Exception:
        pass

def send_text(msg, parse_mode="HTML"):
    if len(msg) > 4000:
        msg = msg[:4000] + "…[truncado]"
    _api("sendMessage", {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
    })

def send_keyboard(msg, keyboard, parse_mode="HTML"):
    """keyboard = lista de listas de InlineKeyboardButton."""
    if len(msg) > 4000:
        msg = msg[:4000] + "…[truncado]"
    _api("sendMessage", {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True,
        "reply_markup": {"inline_keyboard": keyboard},
    })

def answer_callback(callback_id, text=""):
    _api("answerCallbackQuery", {"callback_query_id": callback_id, "text": text})

# ── State manager (lazy load) ─────────────────────────────────────────────────

def _sm():
    return _sm_mod

# ── Fase 2: /start ────────────────────────────────────────────────────────────

def cmd_start(chat_id, args):
    _sm().clear_state(chat_id)
    send_text(
        "👋 Olá, Jadielson!\n\n"
        "Sou seu assistente do Segundo Cérebro. Aqui está o que sei fazer:\n\n"
        "<b>📥 CAPTURAR</b>\n"
        "<code>/i &lt;texto&gt;</code>  → ideia rápida no Inbox\n"
        "<code>/t &lt;texto&gt;</code>  → tarefa\n"
        "<code>/c &lt;texto&gt;</code>  → compromisso\n"
        "<code>/r &lt;texto&gt;</code>  → reunião\n"
        "<code>/g &lt;texto&gt;</code>  → gravação/captação\n"
        "<code>/n &lt;texto&gt;</code>  → nota\n"
        "<code>/p &lt;texto&gt;</code>  → pendência\n\n"
        "<b>🎛️ COMANDOS</b>\n"
        "/menu       → menu guiado com botões\n"
        "/status     → status do sistema\n"
        "/agenda     → próximos eventos (48h)\n"
        "/buscar X   → procurar item\n"
        "/projeto X  → criar novo projeto\n"
        "/tpd X      → tarefa Prevenção de Dor\n"
        "/tpg X      → tarefa Produção de Ganho\n\n"
        "<b>🔁 ÚLTIMA CAPTURA</b>\n"
        "/confirmar  → reexibir confirmação\n"
        "/cancelar   → apagar última captura\n"
        "/repetir    → duplicar com nova data\n\n"
        "Tente: /menu pra começar com botões 👇"
    )

# ── Fase 2: /status ───────────────────────────────────────────────────────────

def cmd_status(chat_id, args):
    now     = datetime.now()
    now_str = now.strftime("%d/%m %H:%M")

    # Crons ativos
    try:
        r = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=5)
        jad_lines = [l for l in r.stdout.splitlines() if "jadielson" in l]
        cron_count = len(jad_lines)
    except Exception:
        cron_count = 0

    cron_icon  = "✅" if cron_count >= 5 else "⚠️"
    poll_ok    = any("telegram" in l for l in (jad_lines if "jad_lines" in dir() else []))
    poll_icon  = "✅" if poll_ok else "⚠️"

    # Última captura
    cap = _sm().get_last_capture(chat_id)
    if cap:
        cap_titulo = (cap.get("titulo") or "")[:40]
        ts = cap.get("timestamp", "")
        try:
            cap_hora = datetime.fromisoformat(ts).strftime("%H:%M")
        except Exception:
            cap_hora = ""
        cap_info = f"{cap_hora} — {html.escape(cap_titulo)}"
    else:
        cap_info = "nenhuma ainda"

    # Último sync Notion→Calendar
    sync_log = VAULT / "memory" / "sessions" / "sync" / f"{date.today().isoformat()}.md"
    if sync_log.exists():
        mtime    = datetime.fromtimestamp(sync_log.stat().st_mtime)
        sync_info = f"✅ {mtime.strftime('%H:%M')}"
    else:
        sync_info = "sem sync hoje"

    # Daily-brief
    session_log = VAULT / "memory" / "sessions" / f"{date.today().isoformat()}.md"
    brief_info  = "✅ existe" if session_log.exists() else "sem log hoje"

    # Git
    try:
        gr = subprocess.run(
            ["git", "-C", str(VAULT), "status", "--porcelain"],
            capture_output=True, text=True, timeout=5
        )
        dirty = [l for l in gr.stdout.splitlines() if l.strip()]
        git_info = "✅ working tree clean" if not dirty else f"⚠️ {len(dirty)} arquivo(s) não commitado(s)"
    except Exception:
        git_info = "⚠️ erro ao checar"

    system_ok   = cron_count >= 5
    system_icon = "🟢" if system_ok else "🟡"

    send_text(
        f"📊 <b>Status do Sistema</b>\n\n"
        f"⏰ Agora: {now_str}\n\n"
        f"🕒 <b>CRONS</b>\n"
        f"{cron_icon} {cron_count}/6 ativos\n"
        f"{poll_icon} Telegram polling\n\n"
        f"📥 <b>CAPTURA</b>\n"
        f"• Última: {cap_info}\n\n"
        f"🔄 <b>SYNC</b>\n"
        f"• Notion→Calendar: {sync_info}\n\n"
        f"📋 <b>BRIEFING</b>\n"
        f"• Daily-brief: {brief_info}\n\n"
        f"💾 <b>GIT</b>\n"
        f"{git_info}\n\n"
        f"{system_icon} Sistema {'OK' if system_ok else 'com alertas'}"
    )

# ── Fase 2: /agenda ───────────────────────────────────────────────────────────

_DIAS  = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
_MESES = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

def _cal_service():
    import google.oauth2.credentials
    import googleapiclient.discovery
    from google.auth.transport.requests import Request

    token_file = SECRETS / "google-calendar-token.json"
    td         = json.loads(token_file.read_text())
    creds      = google.oauth2.credentials.Credentials(
        token=td.get("token"), refresh_token=td.get("refresh_token"),
        token_uri=td.get("token_uri"), client_id=td.get("client_id"),
        client_secret=td.get("client_secret"),
    )
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        new_json = creds.to_json()
        token_file.write_text(new_json)
        # sync de volta ao OneDrive quando o token foi atualizado
        _onedrive_token = VAULT / "scripts" / ".secrets" / "google-calendar-token.json"
        try:
            _onedrive_token.write_text(new_json)
        except Exception:
            pass
    return googleapiclient.discovery.build("calendar", "v3", credentials=creds, cache_discovery=False)

def _events_for_day(service, d):
    TZ = "-03:00"
    try:
        r = service.events().list(
            calendarId="primary",
            timeMin=f"{d.isoformat()}T00:00:00{TZ}",
            timeMax=f"{d.isoformat()}T23:59:59{TZ}",
            singleEvents=True, orderBy="startTime", maxResults=20,
        ).execute()
        return r.get("items", [])
    except Exception:
        return []

def _parse_event_time(ev):
    s = ev.get("start", {})
    if "dateTime" in s:
        dt = datetime.fromisoformat(s["dateTime"])
        return dt.hour * 60 + dt.minute, dt.strftime("%H:%M")
    return 9999, "dia todo"

def cmd_agenda(chat_id, args):
    try:
        service = _cal_service()
    except Exception as e:
        send_text(f"⚠️ Erro ao conectar ao Calendar:\n<code>{html.escape(str(e))}</code>")
        return

    today = date.today()
    days  = [today + timedelta(days=i) for i in range(3)]
    lines = ["📅 <b>Próximos eventos</b>\n"]
    has_any = False

    for i, d in enumerate(days):
        events = _events_for_day(service, d)

        seen, unique = set(), []
        for ev in sorted(events, key=lambda e: _parse_event_time(e)[0]):
            _, t = _parse_event_time(ev)
            key  = (t, ev.get("summary", ""))
            if key not in seen:
                seen.add(key)
                unique.append((t, ev.get("summary", "(sem título)")))

        if i == 0:
            hdr = f"🗓️ <b>HOJE {d.day:02d}/{d.month:02d}</b>"
        elif i == 1:
            hdr = f"🗓️ <b>AMANHÃ {d.day:02d}/{d.month:02d}</b>"
        else:
            hdr = f"🗓️ <b>{_DIAS[d.weekday()]} {d.day:02d}/{d.month:02d}</b>"

        lines.append(hdr)
        if unique:
            has_any = True
            for t, s in unique:
                lines.append(f"• {t} — {html.escape(s)}")
        else:
            lines.append("🆓 Sem eventos")
        lines.append("")

    if not has_any:
        lines = [
            "📅 <b>Próximos eventos</b>\n",
            "🆓 Você não tem nada nos próximos 3 dias.",
            "",
            "Aproveita pra descansar ou puxar a fila da Lógika.",
        ]

    send_text("\n".join(lines))

# ── Fase 2: /buscar ───────────────────────────────────────────────────────────

def cmd_buscar(chat_id, args):
    termo = args.strip()[:100]
    if not termo:
        send_text(
            "🔍 <b>Como usar:</b> /buscar &lt;termo&gt;\n\n"
            "Exemplo: /buscar reunião"
        )
        return

    n_env  = _load_env(SECRETS / "notion.env")
    token  = n_env.get("NOTION_TOKEN", "")
    db_id  = n_env.get("NOTION_CAPTURA_DATABASE_ID", "")
    if not token or not db_id:
        send_text("⚠️ Configuração Notion ausente.")
        return

    payload = json.dumps({
        "filter": {
            "or": [
                {"property": "Título", "title":  {"contains": termo}},
                {"property": "Frente", "select": {"equals": termo}},
            ]
        },
        "sorts":     [{"timestamp": "created_time", "direction": "descending"}],
        "page_size": 5,
    }).encode()

    headers = {
        "Authorization":  f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type":   "application/json",
    }
    try:
        req = urllib.request.Request(
            f"https://api.notion.com/v1/databases/{db_id}/query",
            data=payload, headers=headers,
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
    except Exception as e:
        send_text(f"⚠️ Erro ao buscar no Notion:\n<code>{html.escape(str(e))}</code>")
        return

    results = data.get("results", [])
    if not results:
        send_text(
            f"🔍 Nada encontrado pra <b>{html.escape(termo)}</b>\n\n"
            "Tenta:\n• termo mais curto\n• /menu pra capturar algo novo"
        )
        return

    lines = [f'🔍 <b>{len(results)} resultado(s) pra "{html.escape(termo)}"</b>\n']
    for i, page in enumerate(results, 1):
        props = page.get("properties", {})

        title_parts = props.get("Título", {}).get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_parts).strip() or "(sem título)"

        date_obj = (props.get("Data", {}).get("date") or {})
        date_str = date_obj.get("start", "")
        if date_str:
            try:
                date_str = datetime.fromisoformat(date_str).strftime("%d/%m")
            except Exception:
                pass

        frente = (props.get("Frente", {}).get("select") or {}).get("name", "")
        tipo   = (props.get("Tipo",   {}).get("select") or {}).get("name", "")
        meta   = " · ".join(filter(None, [date_str, frente, tipo]))
        url    = f"https://notion.so/{page['id'].replace('-', '')}"

        lines.append(f"{i}. 📌 <b>{html.escape(title)}</b>")
        if meta:
            lines.append(f"   {html.escape(meta)}")
        lines.append(f'   🔗 <a href="{url}">Abrir no Notion</a>')
        lines.append("")

    lines.append("Quer mais? Use termo mais específico.")
    send_text("\n".join(lines))

# ── Fase 3: /confirmar ────────────────────────────────────────────────────────

def cmd_confirmar(chat_id, args):
    cap = _sm().get_last_capture(chat_id)
    if not cap:
        send_text(
            "ℹ️ Nenhuma captura recente\n\n"
            "Capture algo primeiro:\n/menu ou /t &lt;texto&gt;"
        )
        return

    _send_capture_summary(cap, footer=True)

def _send_capture_summary(cap, footer=False):
    if cap.get("inbox_path"):
        fname = cap["inbox_path"].split("/")[-1]
        msg   = (
            f"✓ <b>Última captura</b>\n\n"
            f"📝 <b>Nota:</b> {html.escape(cap.get('titulo',''))}\n"
            f"📁 <b>Arquivo:</b> {html.escape(fname)}"
        )
    else:
        lines = [
            "✓ <b>Última captura</b>", "",
            f"📝 <b>Título:</b> {html.escape(cap.get('titulo',''))}",
            f"🏢 <b>Frente:</b> {html.escape(cap.get('frente',''))}",
            f"📂 <b>Tipo:</b>   {html.escape(cap.get('tipo',''))}",
        ]
        data_val = cap.get("data")
        hora     = cap.get("hora")
        if data_val:
            data_fmt = data_val[8:10] + "/" + data_val[5:7]
            lines.append(f"📅 <b>Data:</b>  {data_fmt}" + (f" às {hora}" if hora else ""))
        url = cap.get("notion_url")
        if url:
            lines.append(f'📲 <a href="{url}">Abrir no Notion</a>')
        if footer:
            lines += ["", "Pra cancelar: /cancelar", "Pra repetir com nova data: /repetir"]
        msg = "\n".join(lines)

    send_text(msg)

# ── Fase 3: /cancelar ─────────────────────────────────────────────────────────

def cmd_cancelar(chat_id, args):
    cap = _sm().get_last_capture(chat_id)
    if not cap:
        send_text(
            "ℹ️ Nenhuma captura recente\n\n"
            "Capture algo primeiro:\n/menu ou /t &lt;texto&gt;"
        )
        return

    titulo   = html.escape((cap.get("titulo") or "")[:60])
    data_val = cap.get("data") or ""
    hora     = cap.get("hora") or ""
    data_fmt = ""
    if data_val:
        data_fmt = data_val[8:10] + "/" + data_val[5:7]
        if hora:
            data_fmt += f" às {hora}"

    msg = (
        f"⚠️ <b>Apagar última captura?</b>\n\n"
        f"📝 {titulo}\n"
        + (f"📅 {data_fmt}\n" if data_fmt else "")
        + "\nIsso vai:\n"
        "• Deletar do Notion\n"
        "• Remover do Calendar (se sincronizado)\n\n"
        "Tem certeza?"
    )
    send_keyboard(msg, [
        [
            {"text": "🗑️ Sim, apagar",  "callback_data": "cancel_yes"},
            {"text": "↩️ Não, manter",  "callback_data": "cancel_no"},
        ]
    ])

def handle_cancel_yes(chat_id):
    sm  = _sm()
    cap = sm.get_last_capture(chat_id)
    if not cap:
        send_text("ℹ️ Nenhuma captura pra apagar.")
        return

    results = []

    # Arquiva no Notion
    notion_id = cap.get("notion_id") or cap.get("notion_page_id")
    if notion_id:
        n_env = _load_env(SECRETS / "notion.env")
        token = n_env.get("NOTION_TOKEN", "")
        if token:
            try:
                body = json.dumps({"archived": True}).encode()
                req  = urllib.request.Request(
                    f"https://api.notion.com/v1/pages/{notion_id}",
                    data=body,
                    headers={
                        "Authorization":  f"Bearer {token}",
                        "Notion-Version": "2022-06-28",
                        "Content-Type":   "application/json",
                    },
                    method="PATCH",
                )
                urllib.request.urlopen(req, timeout=10)
                results.append("Notion: ✅ arquivado")
            except Exception as e:
                results.append(f"Notion: ⚠️ {html.escape(str(e)[:60])}")
        else:
            results.append("Notion: ⚠️ token ausente")
    else:
        results.append("Notion: ℹ️ sem ID (inbox local)")

    # Remove do Calendar
    cal_id = cap.get("calendar_event_id")
    if cal_id:
        try:
            service = _cal_service()
            service.events().delete(calendarId="primary", eventId=cal_id).execute()
            results.append("Calendar: ✅ removido")
        except Exception as e:
            results.append(f"Calendar: ⚠️ {html.escape(str(e)[:60])}")
    else:
        results.append("Calendar: ℹ️ sem evento associado")

    # Remove inbox local
    inbox_path = cap.get("inbox_path")
    if inbox_path:
        try:
            Path(inbox_path).unlink(missing_ok=True)
            results.append("Inbox: ✅ arquivo removido")
        except Exception:
            results.append("Inbox: ⚠️ erro ao remover")

    # Limpa state
    state = sm._load()  # acesso interno para limpar ultima_captura tbm
    cid   = str(chat_id)
    if cid in state:
        state[cid].pop("ultima_captura", None)
    sm._save(state)

    send_text("✅ <b>Captura apagada</b>\n\n" + "\n".join(results))

def handle_cancel_no(chat_id):
    send_text("↩️ Captura mantida.")

# ── Fase 3: /repetir ──────────────────────────────────────────────────────────

def cmd_repetir(chat_id, args):
    cap = _sm().get_last_capture(chat_id)
    if not cap:
        send_text(
            "ℹ️ Nenhuma captura recente\n\n"
            "Capture algo primeiro:\n/menu ou /t &lt;texto&gt;"
        )
        return

    titulo = html.escape((cap.get("titulo") or "")[:60])
    frente = html.escape(cap.get("frente") or "")

    _sm().set_state(chat_id, fluxo="repetir", etapa="aguardando_data", dados=cap)

    send_keyboard(
        f"🔁 <b>Repetir captura</b>\n\n"
        f"📝 {titulo}\n"
        f"🏢 {frente}\n\n"
        "Qual a nova data? (responda em texto)\n\n"
        "Exemplos:\n• amanhã 14h\n• sexta 16h30\n• 25/05 09h",
        [[{"text": "❌ Cancelar", "callback_data": "repetir_cancel"}]]
    )

def handle_repetir_data(chat_id, text):
    """Chamado quando estado é repetir/aguardando_data e chega texto livre."""
    import importlib.util as _iu
    sm     = _sm()
    state  = sm.get_state(chat_id)
    dados  = state.get("dados", {})

    # Reusa parse-captura já carregado no startup do módulo
    pc = _pc_mod

    data_parsed, hora_parsed = None, None
    try:
        data_parsed, hora_parsed = pc.extract_date(text)
    except Exception:
        pass

    if not data_parsed:
        send_text(
            f"❌ Não entendi a data: <b>{html.escape(text[:60])}</b>\n\n"
            "Tenta de novo ou /cancelar pra abortar."
        )
        return

    # Cria nova captura no Notion com a nova data
    frente = dados.get("frente", "")
    tipo   = dados.get("tipo", "")
    titulo = dados.get("titulo", "")

    cmd_text = f"/t {titulo}"
    if frente:
        cmd_text += f" frente:{frente}"

    env = {"CAPTURA_ORIGEM": "Telegram", **{k: v for k, v in __import__("os").environ.items()}}
    r   = subprocess.run(
        ["python3", str(_HERE / "parse-captura.py"), cmd_text],
        capture_output=True, text=True, env=env, timeout=30
    )

    sm.clear_state(chat_id)

    if r.returncode == 0:
        try:
            cap = json.loads(r.stdout)
        except Exception:
            cap = {"titulo": titulo, "frente": frente, "data": data_parsed, "hora": hora_parsed}
        sm.set_last_capture(chat_id, cap)
        data_fmt = data_parsed[8:10] + "/" + data_parsed[5:7] if len(data_parsed) >= 10 else data_parsed
        url = cap.get("notion_url", "")
        url_line = f'\n📲 <a href="{url}">Abrir no Notion</a>' if url else ""
        send_text(
            f"✓ <b>Captura duplicada</b>\n\n"
            f"📝 {html.escape(titulo)}\n"
            f"📅 nova data: {data_fmt}" + (f" às {hora_parsed}" if hora_parsed else "")
            + url_line + "\n🗓️ <i>Calendar: sync em ~7h</i>\n\n"
            "Estado limpo. Manda outro comando."
        )
    else:
        send_text(f"❌ Erro ao duplicar:\n<code>{html.escape(r.stderr[:200])}</code>")

# ── Fase 4: /menu ─────────────────────────────────────────────────────────────

FRENTES = [
    ("💼 Lógika",    "frente_logika"),
    ("🏥 Saúde",     "frente_saude"),
    ("🏛️ Câmara",    "frente_camara"),
    ("🤝 SINDSS",    "frente_sindss"),
    ("🗳️ Rogério",   "frente_rogerio"),
    ("👤 Pessoal",   "frente_pessoal"),
]
TIPOS = [
    ("💡 Ideia",        "tipo_ideia"),
    ("📌 Tarefa",       "tipo_tarefa"),
    ("📅 Compromisso",  "tipo_compromisso"),
    ("🤝 Reunião",      "tipo_reuniao"),
    ("🎬 Gravação",     "tipo_gravacao"),
    ("📝 Nota",         "tipo_nota"),
    ("⚠️ Pendência",    "tipo_pendencia"),
]
FRENTES_IDEIA = [
    ("💼 Lógika",       "ideia_frente_logika"),
    ("👤 Pessoal",      "ideia_frente_pessoal"),
    ("📸 Além da Foto", "ideia_frente_alemfoto"),
    ("🏥 Saúde",        "ideia_frente_saude"),
    ("🏛️ Câmara",       "ideia_frente_camara"),
    ("🤝 SINDSS",       "ideia_frente_sindss"),
    ("❓ Outra",        "ideia_frente_outra"),
]
_IDEIA_FRENTE_MAP = {
    "ideia_frente_logika":   "Lógika",
    "ideia_frente_pessoal":  "Pessoal",
    "ideia_frente_alemfoto": "Além da Foto",
    "ideia_frente_saude":    "Saúde",
    "ideia_frente_camara":   "Câmara",
    "ideia_frente_sindss":   "SINDSS",
    "ideia_frente_outra":    "Outra",
}

def _kb_rows(items, cols=2):
    rows = []
    for i in range(0, len(items), cols):
        rows.append([{"text": t, "callback_data": d} for t, d in items[i:i+cols]])
    return rows

_DRIVE_URL = "https://drive.google.com"

def cmd_menu(chat_id, args):
    _sm().clear_state(chat_id)
    _sm().set_state(chat_id, fluxo="menu", etapa="principal", historico=["principal"])
    send_keyboard(
        "🎛️ <b>Menu</b>",
        [
            [
                {"text": "📋 Notion",    "callback_data": "menu_notion"},
                {"text": "🔵 Google",    "callback_data": "menu_google"},
            ],
            [
                {"text": "✅ Tarefas",   "callback_data": "menu_tarefas"},
                {"text": "🎨 Gerar",     "callback_data": "menu_gerar_cmd"},
            ],
            [
                {"text": "📊 Status",    "callback_data": "menu_status"},
                {"text": "❌ Fechar",    "callback_data": "menu_fechar"},
            ],
        ]
    )

def _menu_notion(chat_id):
    sm = _sm()
    sm.set_state(chat_id, etapa="notion_menu")
    _append_historico(chat_id, "notion_menu")
    send_keyboard(
        "📋 <b>Notion</b>",
        [
            [
                {"text": "📝 Capturar",  "callback_data": "menu_capturar"},
                {"text": "💡 Ideia",     "callback_data": "menu_ideia"},
            ],
            [
                {"text": "🔍 Buscar",    "callback_data": "menu_buscar"},
            ],
            [{"text": "↩️ Voltar",       "callback_data": "menu_voltar"}],
        ]
    )

def _menu_google(chat_id):
    sm = _sm()
    sm.set_state(chat_id, etapa="google_menu")
    _append_historico(chat_id, "google_menu")
    send_keyboard(
        "🔵 <b>Google</b>",
        [
            [
                {"text": "📅 Agendar",   "callback_data": "menu_agendar"},
                {"text": "🗓️ Agenda",    "callback_data": "menu_agenda"},
            ],
            [
                {"text": "📁 Drive ↗",  "url": _DRIVE_URL},
            ],
            [{"text": "↩️ Voltar",       "callback_data": "menu_voltar"}],
        ]
    )

def _menu_tarefas(chat_id):
    sm = _sm()
    sm.set_state(chat_id, etapa="tarefas_menu")
    _append_historico(chat_id, "tarefas_menu")
    send_keyboard(
        "✅ <b>Tarefas</b>",
        [
            [
                {"text": "🔴 TPD — Prevenção de Dor",   "callback_data": "tarefas_tpd"},
            ],
            [
                {"text": "🟢 TPG — Produção de Ganho",  "callback_data": "tarefas_tpg"},
            ],
            [{"text": "↩️ Voltar", "callback_data": "menu_voltar"}],
        ]
    )

def _menu_tarefas_pedir_nome(chat_id, tipo):
    sm = _sm()
    state = sm.get_state(chat_id)
    sm.set_state(chat_id,
        etapa="tarefas_aguardando_nome",
        dados={**state.get("dados", {}), "tipo_tarefa": tipo}
    )
    _append_historico(chat_id, "tarefas_aguardando_nome")
    icon  = "🔴" if tipo == "tpd" else "🟢"
    label = "Prevenção de Dor" if tipo == "tpd" else "Produção de Ganho"
    send_keyboard(
        f"{icon} <b>{label}</b>\n\nQual o nome da tarefa?",
        [[
            {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
            {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
        ]]
    )

def _menu_frentes(chat_id):
    sm = _sm()
    sm.set_state(chat_id, etapa="frente")
    _append_historico(chat_id, "frente")
    rows = _kb_rows(FRENTES, cols=2)
    rows.append([{"text": "📥 Inbox (sem frente)", "callback_data": "frente_inbox"}])
    rows.append([{"text": "↩️ Voltar",             "callback_data": "menu_voltar"}])
    send_keyboard("📝 <b>Nova captura</b> — qual frente?", rows)

def _menu_tipos(chat_id, frente_label):
    sm = _sm()
    sm.set_state(chat_id, etapa="tipo")
    _append_historico(chat_id, "tipo")
    rows = _kb_rows(TIPOS, cols=2)
    rows.append([{"text": "↩️ Voltar", "callback_data": "menu_voltar"}])
    send_keyboard(f"📝 <b>Frente: {html.escape(frente_label)}</b>\n\nTipo de captura?", rows)

def _menu_pedir_texto(chat_id, frente_label, tipo_label):
    sm = _sm()
    sm.set_state(chat_id, etapa="aguardando_titulo")
    _append_historico(chat_id, "aguardando_titulo")
    send_keyboard(
        f"📝 <b>{html.escape(frente_label)} · {html.escape(tipo_label)}</b>\n\n"
        "Descreve a captura:\n\n"
        "<i>(ex: publicar campanha vacinação no IG até sexta)</i>",
        [
            [
                {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
                {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
            ]
        ]
    )

def _menu_pedir_data(chat_id, frente_label, tipo_label, titulo):
    sm = _sm()
    sm.set_state(chat_id, etapa="aguardando_data_menu")
    _append_historico(chat_id, "aguardando_data_menu")
    send_keyboard(
        f"📝 <b>{html.escape(frente_label)} · {html.escape(tipo_label)}</b>\n"
        f"“{html.escape(titulo[:60])}”\n\n"
        "Tem prazo/data?",
        [
            [
                {"text": "📅 Sim, tem data", "callback_data": "menu_data_sim"},
                {"text": "🆓 Não, sem data", "callback_data": "menu_data_nao"},
            ],
            [{"text": "↩️ Voltar", "callback_data": "menu_voltar"}],
        ]
    )

def _menu_confirmacao(chat_id):
    sm     = _sm()
    state  = sm.get_state(chat_id)
    dados  = state.get("dados", {})
    frente = html.escape(dados.get("frente_label", ""))
    tipo   = html.escape(dados.get("tipo_label", ""))
    titulo = html.escape(dados.get("titulo", "")[:80])
    data_v = dados.get("data") or ""
    hora_v = dados.get("hora") or ""
    data_fmt = ""
    if data_v:
        data_fmt = data_v[8:10] + "/" + data_v[5:7]
        if hora_v:
            data_fmt += f" às {hora_v}"
    data_line = f"📅 {data_fmt}" if data_fmt else "📅 sem data"

    sm.set_state(chat_id, etapa="aguardando_confirmacao")
    send_keyboard(
        f"📝 <b>Vou criar:</b>\n\n"
        f"🏢 {frente}\n"
        f"📂 {tipo}\n"
        f"📝 {titulo}\n"
        f"{data_line}\n\n"
        "Confirma?",
        [
            [
                {"text": "✅ Criar",   "callback_data": "confirm_create"},
                {"text": "↩️ Voltar", "callback_data": "menu_voltar"},
            ],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _append_historico(chat_id, tela):
    sm    = _sm()
    state = sm.get_state(chat_id)
    hist  = state.get("historico", [])
    hist.append(tela)
    sm.set_state(chat_id, historico=hist)

def handle_menu_voltar(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    hist  = state.get("historico", [])
    if len(hist) > 1:
        hist.pop()
        tela_anterior = hist[-1]
    else:
        tela_anterior = "principal"
    sm.set_state(chat_id, historico=hist, etapa=tela_anterior)

    dados = state.get("dados", {})
    if tela_anterior == "principal":
        cmd_menu(chat_id, "")
    elif tela_anterior == "notion_menu":
        _menu_notion(chat_id)
    elif tela_anterior == "google_menu":
        _menu_google(chat_id)
    elif tela_anterior == "tarefas_menu":
        _menu_tarefas(chat_id)
    elif tela_anterior == "tarefas_aguardando_nome":
        _menu_tarefas(chat_id)
    elif tela_anterior == "frente":
        _menu_frentes(chat_id)
    elif tela_anterior == "tipo":
        _menu_tipos(chat_id, dados.get("frente_label", ""))
    elif tela_anterior in ("aguardando_titulo",):
        _menu_pedir_texto(chat_id, dados.get("frente_label", ""), dados.get("tipo_label", ""))
    elif tela_anterior == "agendar_titulo":
        _menu_agendar_titulo(chat_id)
    elif tela_anterior == "agendar_datetime":
        _menu_agendar_datetime(chat_id)
    elif tela_anterior == "agendar_duracao":
        _menu_agendar_duracao(chat_id)
    elif tela_anterior == "ideia_titulo":
        _menu_ideia_titulo(chat_id)
    elif tela_anterior == "ideia_frente":
        _menu_ideia_frente(chat_id)
    else:
        cmd_menu(chat_id, "")

_DURACAO_MAP = {
    "dur_15":  ("15 min",  15),
    "dur_30":  ("30 min",  30),
    "dur_60":  ("1 hora",  60),
    "dur_90":  ("1h30",    90),
    "dur_120": ("2 horas", 120),
}

# ── Fluxo Agendar no Calendar ────────────────────────────────────────────────

def _menu_agendar_titulo(chat_id):
    sm = _sm()
    sm.set_state(chat_id, fluxo="agendar_cal", etapa="agendar_titulo",
                 dados={}, historico=["principal", "agendar_titulo"])
    send_keyboard(
        "📅 <b>Agendar no Google Calendar</b>\n\n"
        "Qual o título do evento?",
        [[
            {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
            {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
        ]]
    )

def _menu_agendar_datetime(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    titulo = html.escape(dados.get("titulo", "")[:60])
    sm.set_state(chat_id, etapa="agendar_datetime")
    _append_historico(chat_id, "agendar_datetime")
    send_keyboard(
        f"📅 <b>{titulo}</b>\n\n"
        "Quando? (data + horário obrigatório)\n\n"
        "Ex: <code>amanhã 14h</code> · <code>20/05 09h30</code> · <code>sexta 16h</code>",
        [[
            {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
            {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
        ]]
    )

def _menu_agendar_duracao(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    titulo = html.escape(dados.get("titulo", "")[:60])
    data_v = dados.get("data", "")
    hora_v = dados.get("hora", "")
    data_fmt = f"{data_v[8:10]}/{data_v[5:7]} às {hora_v}" if data_v and len(data_v) >= 10 else hora_v
    sm.set_state(chat_id, etapa="agendar_duracao")
    _append_historico(chat_id, "agendar_duracao")
    send_keyboard(
        f"📅 <b>{titulo}</b>\n"
        f"🕐 {data_fmt}\n\n"
        "⏱️ Qual a duração?",
        [
            [
                {"text": "15 min",  "callback_data": "dur_15"},
                {"text": "30 min",  "callback_data": "dur_30"},
                {"text": "1 hora",  "callback_data": "dur_60"},
            ],
            [
                {"text": "1h30",    "callback_data": "dur_90"},
                {"text": "2 horas", "callback_data": "dur_120"},
                {"text": "✏️ Outro","callback_data": "dur_outro"},
            ],
            [
                {"text": "↩️ Voltar", "callback_data": "menu_voltar"},
                {"text": "❌ Cancelar", "callback_data": "menu_fechar"},
            ],
        ]
    )

def _menu_agendar_confirmacao(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    titulo   = html.escape(dados.get("titulo", "")[:80])
    data_v   = dados.get("data", "")
    hora_v   = dados.get("hora", "09:00")
    dur_min  = dados.get("duracao_min", 60)
    dur_label = dados.get("duracao_label", "1 hora")
    data_fmt = ""
    if data_v and len(data_v) >= 10:
        data_fmt = f"{data_v[8:10]}/{data_v[5:7]} às {hora_v}"

    sm.set_state(chat_id, etapa="agendar_confirmar")
    send_keyboard(
        f"📅 <b>Criar no Google Calendar?</b>\n\n"
        f"📝 {titulo}\n"
        f"🕐 {data_fmt}\n"
        f"⏱️ Duração: {dur_label}\n\n"
        "Confirma?",
        [
            [
                {"text": "✅ Criar no Calendar", "callback_data": "cal_create"},
                {"text": "↩️ Voltar",            "callback_data": "menu_voltar"},
            ],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _do_cal_create(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    titulo   = dados.get("titulo", "Evento")
    data_v   = dados.get("data", "")
    hora_v   = dados.get("hora") or "09:00"
    dur_min  = dados.get("duracao_min", 60)
    dur_label = dados.get("duracao_label", "1 hora")

    sm.clear_state(chat_id)

    if not data_v:
        send_text("❌ Dados insuficientes para criar o evento.")
        return

    try:
        parts = (hora_v + ":00").split(":")
        h, m  = int(parts[0]), int(parts[1])
        start = datetime.fromisoformat(f"{data_v}T{h:02d}:{m:02d}:00")
        end   = start + timedelta(minutes=dur_min)
        TZ    = "America/Maceio"

        service = _cal_service()
        event   = service.events().insert(
            calendarId="primary",
            body={
                "summary": titulo,
                "start":   {"dateTime": start.isoformat(), "timeZone": TZ},
                "end":     {"dateTime": end.isoformat(),   "timeZone": TZ},
            }
        ).execute()

        ev_link  = event.get("htmlLink", "")
        data_fmt = f"{start.day:02d}/{start.month:02d} às {start.strftime('%H:%M')}"
        url_line = f'\n🔗 <a href="{ev_link}">Abrir no Calendar</a>' if ev_link else ""

        send_text(
            f"✅ <b>Evento criado no Calendar!</b>\n\n"
            f"📝 {html.escape(titulo)}\n"
            f"📅 {data_fmt} — {dur_label}"
            + url_line
        )
    except Exception as e:
        send_text(f"❌ Erro ao criar evento:\n<code>{html.escape(str(e)[:200])}</code>")

# ── Fluxo Ideia de Projeto ────────────────────────────────────────────────────

def _menu_ideia_titulo(chat_id):
    sm = _sm()
    sm.set_state(chat_id, fluxo="ideia_projeto", etapa="ideia_titulo",
                 dados={}, historico=["principal", "ideia_titulo"])
    send_keyboard(
        "💡 <b>Nova ideia de projeto</b>\n\n"
        "Qual é a ideia? (título ou 1 frase curta)",
        [[
            {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
            {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
        ]]
    )

def _menu_ideia_frente(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    titulo = html.escape(dados.get("titulo", "")[:60])
    sm.set_state(chat_id, etapa="ideia_frente")
    _append_historico(chat_id, "ideia_frente")
    rows = _kb_rows(FRENTES_IDEIA, cols=2)
    rows.append([
        {"text": "↩️ Voltar",         "callback_data": "menu_voltar"},
        {"text": "❌ Cancelar fluxo", "callback_data": "menu_fechar"},
    ])
    send_keyboard(f"💡 <b>{titulo}</b>\n\nQual frente?", rows)

def _menu_ideia_confirmacao(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    titulo = html.escape(dados.get("titulo", "")[:80])
    frente = html.escape(dados.get("frente_label", ""))
    sm.set_state(chat_id, etapa="ideia_confirmar")
    send_keyboard(
        f"💡 <b>Salvar ideia de projeto?</b>\n\n"
        f"📝 {titulo}\n"
        f"🏷️ Frente: {frente}\n"
        f"📁 Destino: PROJETOS/IDEIAS NOVAS/\n\n"
        "Confirma?",
        [
            [
                {"text": "✅ Salvar ideia", "callback_data": "ideia_salvar"},
                {"text": "↩️ Voltar",       "callback_data": "menu_voltar"},
            ],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _do_ideia_salvar(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    titulo = dados.get("titulo", "Ideia sem título").strip()
    frente = dados.get("frente_label", "Outra")
    agora  = datetime.now()

    sm.clear_state(chat_id)

    safe = titulo.upper()
    for ch in r'/\:*?"<>|':
        safe = safe.replace(ch, "")
    safe = safe.strip()[:80]

    dest_dir = VAULT / "PROJETOS" / "IDEIAS NOVAS"
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest = dest_dir / f"{safe}.md"
    if dest.exists():
        dest = dest_dir / f"{safe} — {agora.strftime('%H%M')}.md"

    frente_slug = {
        "Lógika": "logika", "Pessoal": "pessoal",
        "Além da Foto": "alem-da-foto", "Saúde": "saude",
        "Câmara": "camara", "SINDSS": "sindss", "Outra": "outra",
    }.get(frente, "outra")

    conteudo = (
        f"---\n"
        f"tipo: ideia-projeto\n"
        f"frente: {frente_slug}\n"
        f"capturado-em: {agora.strftime('%Y-%m-%d %H:%M')}\n"
        f"origem: Telegram\n"
        f"---\n\n"
        f"# {titulo}\n\n"
        f"> {titulo}\n\n"
        f"---\n\n"
        f"## 📌 Próximo passo\n"
        f"- [ ] Decidir: vira A INICIAR ou descarta\n"
        f"- [ ] Se virar projeto: pedir card estratégico à IA\n"
    )

    try:
        dest.write_text(conteudo, encoding="utf-8")
        send_text(
            f"✅ <b>Ideia salva!</b>\n\n"
            f"💡 {html.escape(titulo)}\n"
            f"🏷️ {html.escape(frente)}\n"
            f"📁 PROJETOS/IDEIAS NOVAS/{html.escape(dest.name)}\n\n"
            f"Quando quiser expandir: abra o Obsidian e peça à IA o card estratégico completo."
        )
    except Exception as e:
        send_text(f"❌ Erro ao salvar ideia:\n<code>{html.escape(str(e)[:200])}</code>")

# ── /projeto — Cria projeto com estrutura padrão ────────────────────────────

_PROJ_FRENTE_MAP = {
    "proj_frente_logika":   ("logika-creative", "Lógika"),
    "proj_frente_pessoal":  ("pessoal",          "Pessoal"),
    "proj_frente_alemfoto": ("alem-da-foto",     "Além da Foto"),
    "proj_frente_saude":    ("saude",             "Saúde"),
    "proj_frente_camara":   ("camara",            "Câmara"),
    "proj_frente_sindss":   ("sindss",            "SINDSS"),
}

_PROJ_INDEX = {
    "2-pesquisas":        "Pesquisas & Referências\n\nReferências, editais, orçamentos, inspirações.",
    "3-dados":            "Dados & Métricas\n\nTabelas, números, cronogramas.",
    "4-decisoes":         "Decisões\n\nRegistro de decisões importantes do projeto.",
    "5-resumos-semanais": "Resumos Semanais\n\nEvolução semana a semana.",
    "6-entregas":         "Entregas\n\nArquivos finais e entregas do projeto.",
    "7-arquivo":          "Arquivo\n\nMaterial histórico e arquivado.",
}

def cmd_projeto(chat_id, args):
    nome = args.strip()
    if not nome:
        send_text(
            "📁 <b>Como usar:</b>\n"
            "<code>/projeto &lt;nome do projeto&gt;</code>\n\n"
            "Exemplo:\n<code>/projeto PODCAST QUESTÃO DE LÓGICA</code>"
        )
        return

    nome_upper = nome.upper()
    _sm().set_state(chat_id, fluxo="projeto", etapa="proj_frente",
                    dados={"nome": nome_upper})
    send_keyboard(
        f"📁 <b>Novo projeto</b>\n\n"
        f"📝 {html.escape(nome_upper)}\n\n"
        "Qual frente?",
        [
            [
                {"text": "💼 Lógika",       "callback_data": "proj_frente_logika"},
                {"text": "👤 Pessoal",      "callback_data": "proj_frente_pessoal"},
            ],
            [
                {"text": "📸 Além da Foto", "callback_data": "proj_frente_alemfoto"},
                {"text": "🏥 Saúde",        "callback_data": "proj_frente_saude"},
            ],
            [
                {"text": "🏛️ Câmara",      "callback_data": "proj_frente_camara"},
                {"text": "🤝 SINDSS",       "callback_data": "proj_frente_sindss"},
            ],
            [{"text": "💡 Ideia Nova (decidir depois)", "callback_data": "proj_ideia_nova"}],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _do_projeto_criar(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    nome        = dados.get("nome", "PROJETO SEM NOME")
    frente_slug = dados.get("frente_slug", "pessoal")
    frente_label = dados.get("frente_label", "Pessoal")
    sm.clear_state(chat_id)

    # Sanitiza nome para nome de pasta
    safe = nome
    for ch in r'/\:*?"<>|':
        safe = safe.replace(ch, "")
    safe = safe.strip()[:80]

    hoje   = date.today().isoformat()
    review = (date.today() + __import__("datetime").timedelta(weeks=6)).isoformat()

    dest = VAULT / "PROJETOS" / "A INICIAR" / safe
    if dest.exists():
        send_text(
            f"⚠️ Já existe um projeto com esse nome:\n"
            f"<code>PROJETOS/A INICIAR/{html.escape(safe)}/</code>\n\n"
            "Escolha um nome diferente."
        )
        return

    try:
        dest.mkdir(parents=True)

        # Arquivo principal
        (dest / f"{safe}.md").write_text(
            f"---\n"
            f"tipo: projeto\n"
            f"status: a-iniciar\n"
            f"frente: {frente_slug}\n"
            f"fase-atual: pesquisa\n"
            f"criado-em: {hoje}\n"
            f"proximo-review: {review}\n"
            f"destino-matriz: FOCO\n"
            f"ultimo_update: {hoje}\n"
            f"saude: 🟢 ativo\n"
            f"---\n\n"
            f"# {safe}\n\n"
            f"---\n\n"
            f"## 🧭 Por que existe\n\n\n\n"
            f"---\n\n"
            f"## 🎯 Resultado esperado\n\n\n\n"
            f"---\n\n"
            f"## 🔗 Conexões\n\n-\n",
            encoding="utf-8"
        )

        # briefing
        (dest / "1-briefing.md").write_text(
            f"---\ntipo: briefing\nprojeto: {safe}\n---\n\n"
            f"# Briefing — {safe}\n\n"
            f"## Contexto\n*Por que esse projeto existe? Que problema resolve?*\n\n"
            f"## Objetivo claro\n*Qual o resultado mensurável que define \"feito\"?*\n\n"
            f"## Critérios de sucesso\n- [ ]\n- [ ]\n\n"
            f"## Restrições e premissas\n-\n\n"
            f"---\n*Criado em {hoje}.*\n",
            encoding="utf-8"
        )

        # proximas-etapas
        (dest / "proximas-etapas.md").write_text(
            f"---\ntipo: kanban\nprojeto: {safe}\n---\n\n"
            f"# Próximas Etapas — {safe}\n\n"
            f"## 🟡 A FAZER\n- [ ] Definir objetivo e prazo\n\n"
            f"## 🔵 FAZENDO\n- [ ]\n\n"
            f"## 🟢 FEITO\n- [x]\n\n"
            f"---\n## ⚡ Próxima ação\n→ \n\n---\n*Atualizar 1x/semana.*\n",
            encoding="utf-8"
        )

        # subpastas com _index.md
        for sub, titulo in _PROJ_INDEX.items():
            sp = dest / sub
            sp.mkdir()
            (sp / "_index.md").write_text(
                f"---\ntipo: indice\nsecao: {sub}\n---\n\n# {titulo}\n",
                encoding="utf-8"
            )

        # git commit + push
        subprocess.run(
            ["git", "-C", str(VAULT), "add", "-A"],
            capture_output=True, timeout=15
        )
        subprocess.run(
            ["git", "-C", str(VAULT), "commit", "-m", f"novo projeto: {safe}"],
            capture_output=True, timeout=15
        )
        subprocess.run(
            ["git", "-C", str(VAULT), "push", "origin", "main"],
            capture_output=True, timeout=30
        )

        send_text(
            f"✅ <b>Projeto criado!</b>\n\n"
            f"📝 {html.escape(safe)}\n"
            f"🏷️ Frente: {html.escape(frente_label)}\n"
            f"📁 <code>PROJETOS/A INICIAR/{html.escape(safe)}/</code>\n\n"
            f"Abra no Obsidian para preencher objetivo e próximas etapas."
        )

    except Exception as e:
        send_text(f"❌ Erro ao criar projeto:\n<code>{html.escape(str(e)[:200])}</code>")


def _do_ideia_nova(chat_id):
    """Salva ideia em PROJETOS/IDEIAS NOVAS/ sem estrutura de pasta completa."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    nome  = dados.get("nome", "IDEIA SEM NOME")
    sm.clear_state(chat_id)

    safe = nome
    for ch in r'/\:*?"<>|':
        safe = safe.replace(ch, "")
    safe = safe.strip()[:80]

    agora = __import__("datetime").datetime.now()
    dest_dir = VAULT / "PROJETOS" / "IDEIAS NOVAS"
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest = dest_dir / f"{safe}.md"
    if dest.exists():
        dest = dest_dir / f"{safe} — {agora.strftime('%H%M')}.md"

    try:
        dest.write_text(
            f"---\n"
            f"tipo: ideia-projeto\n"
            f"frente: a-definir\n"
            f"capturado-em: {agora.strftime('%Y-%m-%d %H:%M')}\n"
            f"origem: Telegram\n"
            f"---\n\n"
            f"# {safe}\n\n"
            f"> {safe}\n\n"
            f"---\n\n"
            f"## 📌 Próximo passo\n"
            f"- [ ] Decidir: vira A INICIAR ou descarta\n"
            f"- [ ] Se virar projeto: definir frente e pedir card estratégico\n",
            encoding="utf-8"
        )

        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "commit", "-m", f"ideia nova: {safe}"],
                       capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "push", "origin", "main"],
                       capture_output=True, timeout=30)

        send_text(
            f"💡 <b>Ideia capturada!</b>\n\n"
            f"📝 {html.escape(safe)}\n"
            f"📁 <code>PROJETOS/IDEIAS NOVAS/{html.escape(dest.name)}</code>\n\n"
            f"Quando quiser decidir o destino, abra no Obsidian."
        )

    except Exception as e:
        send_text(f"❌ Erro ao salvar ideia:\n<code>{html.escape(str(e)[:200])}</code>")


# ── /tpd — Tarefa Prevenção de Dor ──────────────────────────────────────────

_TPD_FRENTE_MAP = {
    "tpd_f_logika":  ("logika",  "Lógika"),
    "tpd_f_sms":     ("sms",     "SMS"),
    "tpd_f_camara":  ("camara",  "Câmara"),
    "tpd_f_sindss":  ("sindss",  "SINDSS"),
    "tpd_f_pessoal": ("pessoal", "Pessoal"),
    "tpd_f_geral":   ("geral",   "Geral"),
}
_TPG_FRENTE_MAP = {
    "tpg_f_logika":  ("logika",  "Lógika"),
    "tpg_f_sms":     ("sms",     "SMS"),
    "tpg_f_camara":  ("camara",  "Câmara"),
    "tpg_f_sindss":  ("sindss",  "SINDSS"),
    "tpg_f_pessoal": ("pessoal", "Pessoal"),
    "tpg_f_geral":   ("geral",   "Geral"),
}

def _prazo_iso(val):
    from datetime import date, timedelta
    hoje = date.today()
    if val == "hoje":   return hoje.isoformat()
    if val == "amanha": return (hoje + timedelta(days=1)).isoformat()
    if val == "semana": return (hoje + timedelta(days=7)).isoformat()
    return ""

def cmd_tpd(chat_id, args):
    nome = args.strip()
    if not nome:
        send_text(
            "🔴 <b>Tarefa Prevenção de Dor</b>\n\n"
            "<i>Tarefas sem projeto — se não feitas, causam dano.</i>\n\n"
            "<b>Como usar:</b>\n"
            "<code>/tpd &lt;nome da tarefa&gt;</code>\n\n"
            "Exemplo:\n<code>/tpd Pagar fornecedor da gráfica</code>"
        )
        return
    _sm().set_state(chat_id, fluxo="tpd", etapa="tpd_frente", dados={"nome": nome})
    send_keyboard(
        f"🔴 <b>Prevenção de Dor</b>\n\n"
        f"📝 {html.escape(nome)}\n\n"
        "Qual frente?",
        [
            [{"text": "💼 Lógika", "callback_data": "tpd_f_logika"},
             {"text": "🏥 SMS",    "callback_data": "tpd_f_sms"}],
            [{"text": "🏛️ Câmara", "callback_data": "tpd_f_camara"},
             {"text": "🤝 SINDSS", "callback_data": "tpd_f_sindss"}],
            [{"text": "👤 Pessoal","callback_data": "tpd_f_pessoal"},
             {"text": "🌐 Geral",  "callback_data": "tpd_f_geral"}],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _tpd_ask_prazo(chat_id):
    sm = _sm(); state = sm.get_state(chat_id); dados = state.get("dados", {})
    sm.set_state(chat_id, etapa="tpd_prazo")
    send_keyboard(
        f"🔴 <b>Prevenção de Dor</b>\n\n"
        f"📝 {html.escape(dados.get('nome',''))}\n"
        f"🏷️ {html.escape(dados.get('frente_label',''))}\n\n"
        "Prazo?",
        [
            [{"text": "📅 Hoje",        "callback_data": "tpd_prazo_hoje"},
             {"text": "📅 Amanhã",      "callback_data": "tpd_prazo_amanha"}],
            [{"text": "📅 Esta semana", "callback_data": "tpd_prazo_semana"},
             {"text": "🚫 Sem prazo",   "callback_data": "tpd_prazo_sem"}],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _do_tpd_criar(chat_id, prazo_key):
    import re as _re
    sm = _sm(); state = sm.get_state(chat_id); dados = state.get("dados", {})
    nome         = dados.get("nome", "Tarefa")
    frente_slug  = dados.get("frente_slug", "geral")
    frente_label = dados.get("frente_label", "Geral")
    sm.clear_state(chat_id)

    prazo_map = {"tpd_prazo_hoje": "hoje", "tpd_prazo_amanha": "amanha",
                 "tpd_prazo_semana": "semana", "tpd_prazo_sem": ""}
    prazo_str   = _prazo_iso(prazo_map.get(prazo_key, ""))
    prazo_label = {"tpd_prazo_hoje": "Hoje", "tpd_prazo_amanha": "Amanhã",
                   "tpd_prazo_semana": "Esta semana", "tpd_prazo_sem": "Sem prazo"}.get(prazo_key, "")

    safe = nome
    for ch in r'/\:*?"<>|': safe = safe.replace(ch, "")
    safe  = safe.strip()[:80]
    slug  = _re.sub(r'[^a-z0-9]+', '-', safe.lower())[:60].strip('-')
    hoje  = __import__("datetime").date.today().isoformat()

    dest_dir = VAULT / "TAREFAS" / "TPD"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{slug}.md"
    if dest.exists():
        dest = dest_dir / f"{slug}-{__import__('datetime').datetime.now().strftime('%H%M%S')}.md"

    conteudo = (
        f"---\n"
        f"tipo: tarefa-tpd\n"
        f"titulo: {safe}\n"
        f"frente: {frente_slug}\n"
        f"prazo: {prazo_str}\n"
        f"status: pendente\n"
        f"criado-em: {hoje}\n"
        f"origem: Telegram\n"
        f"---\n\n"
        f"# {safe}\n"
    )
    try:
        dest.write_text(conteudo, encoding="utf-8")
        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "commit", "-m", f"tpd: {safe[:50]}"],
                       capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "push", "origin", "main"],
                       capture_output=True, timeout=30)
        send_text(
            f"✅ <b>Tarefa TPD criada!</b>\n\n"
            f"🔴 {html.escape(safe)}\n"
            f"🏷️ {html.escape(frente_label)}\n"
            f"📅 {prazo_label}\n\n"
            f"Visível em localhost:8765 → seção Tarefas"
        )
    except Exception as e:
        send_text(f"❌ Erro:\n<code>{html.escape(str(e)[:200])}</code>")


# ── /tpg — Tarefa Produção de Ganho ──────────────────────────────────────────

def _listar_projetos_tpg():
    """Retorna lista de (nome, frente_slug) de projetos EM ANDAMENTO + A INICIAR (até 8)."""
    import re as _re
    projetos = []
    for status in ["EM ANDAMENTO", "A INICIAR"]:
        pasta = VAULT / "PROJETOS" / status
        if not pasta.exists(): continue
        for item in sorted(pasta.iterdir()):
            if not item.is_dir(): continue
            frente = ""
            main = item / f"{item.name}.md"
            if main.exists():
                try:
                    txt = main.read_text(encoding="utf-8")
                    m = _re.search(r'^frente:\s*(\S+)', txt, _re.MULTILINE)
                    if m: frente = m.group(1)
                except Exception: pass
            projetos.append((item.name, frente, status))
            if len(projetos) >= 8: break
        if len(projetos) >= 8: break
    return projetos[:8]

def cmd_tpg(chat_id, args):
    nome = args.strip()
    if not nome:
        send_text(
            "🟢 <b>Tarefa Produção de Ganho</b>\n\n"
            "<i>Etapas de projetos — cada uma avança um projeto e sua vida.</i>\n\n"
            "<b>Como usar:</b>\n"
            "<code>/tpg &lt;nome da tarefa&gt;</code>\n\n"
            "Exemplo:\n<code>/tpg Gravar intro vídeo institucional</code>"
        )
        return

    projetos = _listar_projetos_tpg()
    if not projetos:
        send_text("⚠️ Nenhum projeto EM ANDAMENTO ou A INICIAR.\n\nCrie um projeto com /projeto")
        return

    _sm().set_state(chat_id, fluxo="tpg", etapa="tpg_projeto",
                    dados={"nome": nome, "_projetos": projetos})

    rows = []
    for i, (proj_nome, _, _status) in enumerate(projetos):
        emoji = "🔵" if _status == "EM ANDAMENTO" else "⚪"
        rows.append([{"text": f"{emoji} {proj_nome[:35]}", "callback_data": f"tpg_proj_{i}"}])
    rows.append([{"text": "❌ Cancelar", "callback_data": "menu_fechar"}])

    send_keyboard(
        f"🟢 <b>Produção de Ganho</b>\n\n"
        f"📝 {html.escape(nome)}\n\n"
        "Qual projeto esta tarefa avança?",
        rows
    )

def _tpg_ask_frente(chat_id):
    sm = _sm(); state = sm.get_state(chat_id); dados = state.get("dados", {})
    sm.set_state(chat_id, etapa="tpg_frente")
    send_keyboard(
        f"🟢 <b>Produção de Ganho</b>\n\n"
        f"📝 {html.escape(dados.get('nome',''))}\n"
        f"📁 {html.escape(dados.get('projeto',''))}\n\n"
        "Qual frente?",
        [
            [{"text": "💼 Lógika", "callback_data": "tpg_f_logika"},
             {"text": "🏥 SMS",    "callback_data": "tpg_f_sms"}],
            [{"text": "🏛️ Câmara", "callback_data": "tpg_f_camara"},
             {"text": "🤝 SINDSS", "callback_data": "tpg_f_sindss"}],
            [{"text": "👤 Pessoal","callback_data": "tpg_f_pessoal"},
             {"text": "🌐 Geral",  "callback_data": "tpg_f_geral"}],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _tpg_ask_prazo(chat_id):
    sm = _sm(); state = sm.get_state(chat_id); dados = state.get("dados", {})
    sm.set_state(chat_id, etapa="tpg_prazo")
    send_keyboard(
        f"🟢 <b>Produção de Ganho</b>\n\n"
        f"📝 {html.escape(dados.get('nome',''))}\n"
        f"📁 {html.escape(dados.get('projeto',''))}\n"
        f"🏷️ {html.escape(dados.get('frente_label',''))}\n\n"
        "Prazo?",
        [
            [{"text": "📅 Hoje",        "callback_data": "tpg_prazo_hoje"},
             {"text": "📅 Amanhã",      "callback_data": "tpg_prazo_amanha"}],
            [{"text": "📅 Esta semana", "callback_data": "tpg_prazo_semana"},
             {"text": "🚫 Sem prazo",   "callback_data": "tpg_prazo_sem"}],
            [{"text": "❌ Cancelar", "callback_data": "menu_fechar"}],
        ]
    )

def _do_tpg_criar(chat_id, prazo_key):
    import re as _re
    sm = _sm(); state = sm.get_state(chat_id); dados = state.get("dados", {})
    nome         = dados.get("nome", "Tarefa")
    projeto      = dados.get("projeto", "")
    frente_slug  = dados.get("frente_slug", "geral")
    frente_label = dados.get("frente_label", "Geral")
    sm.clear_state(chat_id)

    prazo_map = {"tpg_prazo_hoje": "hoje", "tpg_prazo_amanha": "amanha",
                 "tpg_prazo_semana": "semana", "tpg_prazo_sem": ""}
    prazo_str   = _prazo_iso(prazo_map.get(prazo_key, ""))
    prazo_label = {"tpg_prazo_hoje": "Hoje", "tpg_prazo_amanha": "Amanhã",
                   "tpg_prazo_semana": "Esta semana", "tpg_prazo_sem": "Sem prazo"}.get(prazo_key, "")

    safe = nome
    for ch in r'/\:*?"<>|': safe = safe.replace(ch, "")
    safe  = safe.strip()[:80]
    slug  = _re.sub(r'[^a-z0-9]+', '-', safe.lower())[:60].strip('-')
    hoje  = __import__("datetime").date.today().isoformat()

    dest_dir = VAULT / "TAREFAS" / "TPG"
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{slug}.md"
    if dest.exists():
        dest = dest_dir / f"{slug}-{__import__('datetime').datetime.now().strftime('%H%M%S')}.md"

    conteudo = (
        f"---\n"
        f"tipo: tarefa-tpg\n"
        f"titulo: {safe}\n"
        f"projeto: {projeto}\n"
        f"frente: {frente_slug}\n"
        f"prazo: {prazo_str}\n"
        f"status: pendente\n"
        f"criado-em: {hoje}\n"
        f"origem: Telegram\n"
        f"---\n\n"
        f"# {safe}\n"
    )
    try:
        dest.write_text(conteudo, encoding="utf-8")
        subprocess.run(["git", "-C", str(VAULT), "add", "-A"], capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "commit", "-m", f"tpg: {safe[:50]}"],
                       capture_output=True, timeout=15)
        subprocess.run(["git", "-C", str(VAULT), "push", "origin", "main"],
                       capture_output=True, timeout=30)
        send_text(
            f"✅ <b>Tarefa TPG criada!</b>\n\n"
            f"🟢 {html.escape(safe)}\n"
            f"📁 {html.escape(projeto)}\n"
            f"🏷️ {html.escape(frente_label)}\n"
            f"📅 {prazo_label}\n\n"
            f"Visível em localhost:8765 → seção Tarefas"
        )
    except Exception as e:
        send_text(f"❌ Erro:\n<code>{html.escape(str(e)[:200])}</code>")


# ── /gerar — Geração de conteúdo via Claude API ──────────────────────────────

_GERAR_HELP = (
    "🎨 <b>Como usar /gerar:</b>\n\n"
    "<code>/gerar &lt;frente&gt; — &lt;pedido&gt;</code>\n\n"
    "Exemplos:\n"
    "• <code>/gerar Saúde — post sobre campanha de dengue</code>\n"
    "• <code>/gerar SINDSS — legenda para Dia do Trabalhador</code>\n"
    "• <code>/gerar Câmara — headline da sessão de hoje</code>\n"
    "• <code>/gerar Lógika — legenda de repostagem</code>\n"
    "• <code>/gerar Rogério — post de visita à comunidade</code>\n\n"
    "Depois que eu gerar, responda normalmente para ajustar.\n"
    "Quando estiver bom, toque em <b>💾 Salvar</b>."
)

_GERAR_KB = [
    [
        {"text": "💾 Salvar no vault",  "callback_data": "gerar_salvar"},
        {"text": "🔄 Refazer do zero", "callback_data": "gerar_refazer"},
    ],
    [
        {"text": "📋 Texto limpo",      "callback_data": "gerar_limpo"},
        {"text": "❌ Descartar",        "callback_data": "gerar_descartar"},
    ],
]


def cmd_gerar(chat_id, args):
    if not args.strip():
        send_text(_GERAR_HELP)
        return

    cg = _cg()
    frente_slug, frente_label = cg.detectar_frente(args)

    if not frente_slug:
        send_text(
            "⚠️ Não identifiquei a frente no seu pedido.\n\n"
            "Frentes disponíveis: <b>Saúde · SINDSS · Câmara · Lógika · Rogério · "
            "Além da Foto · Vereadores · Lives</b>\n\n"
            "Exemplo: <code>/gerar Saúde — post sobre vacinação</code>"
        )
        return

    _sm().set_state(chat_id,
        fluxo="gerar",
        etapa="aguardando_tipo",
        dados={
            "frente_slug":     frente_slug,
            "frente_label":    frente_label,
            "pedido_original": args,
        }
    )

    pedido_curto = args[:80] + ("…" if len(args) > 80 else "")
    send_keyboard(
        f"🎨 <b>{html.escape(frente_label)}</b>\n"
        f'<i>{html.escape(pedido_curto)}</i>\n\n'
        "Qual tipo de conteúdo?",
        [
            [
                {"text": "📝 Legenda",   "callback_data": "gerar_tipo_legenda"},
                {"text": "📰 Headline",  "callback_data": "gerar_tipo_headline"},
                {"text": "🎬 Roteiro",   "callback_data": "gerar_tipo_roteiro"},
            ],
            [{"text": "❌ Cancelar", "callback_data": "gerar_descartar"}],
        ]
    )


def _do_gerar(chat_id, tipo):
    """Chamado após escolha de tipo — dispara a geração."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    frente_slug  = dados.get("frente_slug", "")
    frente_label = dados.get("frente_label", "")
    pedido       = dados.get("pedido_original", "")

    tipo_label = {"legenda": "Legenda", "headline": "Headline", "roteiro": "Roteiro"}.get(tipo, tipo)
    send_text(f"⏳ Gerando {tipo_label} para <b>{html.escape(frente_label)}</b>…")

    messages = [{"role": "user", "content": pedido}]
    cg = _cg()
    resultado = cg.gerar(messages, frente_slug, tipo)

    sm.set_state(chat_id,
        fluxo="gerar",
        etapa="aguardando_ajuste",
        dados={
            **dados,
            "tipo":     tipo,
            "messages": messages + [{"role": "assistant", "content": resultado}],
        }
    )

    _send_resultado(frente_label, tipo, resultado)


def _send_resultado(frente_label, tipo, resultado):
    tipo_icon = {"legenda": "📝", "headline": "📰", "roteiro": "🎬"}.get(tipo, "🎨")
    cabecalho = f"{tipo_icon} <b>{html.escape(frente_label)}</b>\n\n"
    rodape    = "\n\n─────────────────\n<i>Responda para ajustar · Salvar quando estiver bom</i>"
    corpo     = html.escape(resultado)
    msg       = cabecalho + corpo + rodape
    send_keyboard(msg[:4000], _GERAR_KB)


def handle_gerar_ajuste(chat_id, text):
    """Texto livre enquanto fluxo=gerar — trata como pedido de ajuste."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    frente_slug  = dados.get("frente_slug", "")
    frente_label = dados.get("frente_label", "")
    tipo         = dados.get("tipo", "legenda")
    messages     = dados.get("messages", [])

    messages.append({"role": "user", "content": text})
    send_text("⏳ Aplicando ajuste…")

    cg        = _cg()
    resultado = cg.gerar(messages, frente_slug, tipo)
    messages.append({"role": "assistant", "content": resultado})

    sm.set_state(chat_id, dados={**dados, "messages": messages})
    _send_resultado(frente_label, tipo, resultado)


def handle_gerar_salvar(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    frente_slug  = dados.get("frente_slug", "")
    frente_label = dados.get("frente_label", "")
    messages     = dados.get("messages", [])
    pedido       = dados.get("pedido_original", "draft")

    ultimo = next(
        (m["content"] for m in reversed(messages) if m["role"] == "assistant"),
        None
    )
    if not ultimo:
        send_text("⚠️ Nenhum conteúdo para salvar.")
        return

    sm.clear_state(chat_id)

    try:
        cg      = _cg()
        caminho = cg.salvar_draft(frente_slug, pedido, ultimo)
        send_text(
            f"✅ <b>Salvo no vault!</b>\n\n"
            f"🏢 {html.escape(frente_label)}\n"
            f"📁 <code>{html.escape(caminho)}</code>\n\n"
            "<i>revisado: false — abra no Claude Code para aprovação final.</i>"
        )
    except Exception as e:
        send_text(f"❌ Erro ao salvar:\n<code>{html.escape(str(e)[:200])}</code>")


def handle_gerar_refazer(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    frente_slug  = dados.get("frente_slug", "")
    frente_label = dados.get("frente_label", "")
    tipo         = dados.get("tipo", "legenda")
    messages     = dados.get("messages", [])
    pedido       = dados.get("pedido_original", "")

    send_text(f"🔄 Refazendo com outro ângulo para <b>{html.escape(frente_label)}</b>…")

    cg = _cg()

    if messages:
        novo_messages = messages + [{
            "role": "user",
            "content": (
                "Reescreva com um ângulo completamente diferente. "
                "Mude o gancho, a emoção de entrada e a estrutura. "
                "O resultado não pode se parecer com o anterior — "
                "explore outro aspecto do mesmo fato."
            )
        }]
    else:
        novo_messages = [{"role": "user", "content": pedido}]

    resultado = cg.gerar(novo_messages, frente_slug, tipo)
    novo_messages.append({"role": "assistant", "content": resultado})

    sm.set_state(chat_id, dados={**dados, "messages": novo_messages})
    _send_resultado(frente_label, tipo, resultado)


def handle_gerar_limpo(chat_id):
    """Envia o último resultado em bloco de código para cópia fácil."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    messages = dados.get("messages", [])

    ultimo = next(
        (m["content"] for m in reversed(messages) if m["role"] == "assistant"),
        None
    )
    if not ultimo:
        send_text("⚠️ Nenhum conteúdo para exibir.")
        return

    send_text(f"<code>{html.escape(ultimo)}</code>")


def handle_gerar_descartar(chat_id):
    _sm().clear_state(chat_id)
    send_text("🗑️ Conteúdo descartado. /gerar para criar outro.")


# ── Roteamento de texto livre ─────────────────────────────────────────────────

def _show_destino_selector(chat_id, texto):
    """Exibe seletor de destino completo após texto livre."""
    _sm().set_state(chat_id, fluxo="roteamento", etapa="aguardando_destino",
                   dados={"texto": texto})
    texto_curto = texto[:80] + ("…" if len(texto) > 80 else "")
    send_keyboard(
        f"📥 <i>{html.escape(texto_curto)}</i>\n\nPara onde enviar?",
        [
            [
                {"text": "📋 Notion",    "callback_data": "rota_notion"},
                {"text": "📅 Calendar",  "callback_data": "rota_calendar"},
            ],
            [
                {"text": "📝 Legenda",   "callback_data": "rota_tipo_legenda"},
                {"text": "📰 Headline",  "callback_data": "rota_tipo_headline"},
                {"text": "🎬 Roteiro",   "callback_data": "rota_tipo_roteiro"},
            ],
            [
                {"text": "❌ Descartar", "callback_data": "rota_descartar"},
            ],
        ]
    )

_ROTA_FRENTE_MAP = {
    "rota_frente_saude":   ("saude-sao-sebastiao", "Saúde"),
    "rota_frente_sindss":  ("sindss",              "SINDSS"),
    "rota_frente_camara":  ("camara",              "Câmara"),
    "rota_frente_logika":  ("logika",              "Lógika"),
    "rota_frente_rogerio": ("rogerio",             "Rogério"),
    "rota_frente_alemfoto":("alem-da-foto",        "Além da Foto"),
}

def _show_rota_frente_selector(chat_id):
    send_keyboard(
        "🏢 Qual frente?",
        [
            [
                {"text": "🏥 Saúde",       "callback_data": "rota_frente_saude"},
                {"text": "🤝 SINDSS",      "callback_data": "rota_frente_sindss"},
            ],
            [
                {"text": "🏛️ Câmara",      "callback_data": "rota_frente_camara"},
                {"text": "💼 Lógika",      "callback_data": "rota_frente_logika"},
            ],
            [
                {"text": "🗳️ Rogério",     "callback_data": "rota_frente_rogerio"},
                {"text": "📸 Além da Foto","callback_data": "rota_frente_alemfoto"},
            ],
            [{"text": "❌ Cancelar",        "callback_data": "rota_descartar"}],
        ]
    )

def _do_rota_tipo(chat_id, tipo):
    """Legenda / Headline / Roteiro a partir do texto livre."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    texto = dados.get("texto", "")

    cg = _cg()
    frente_slug, frente_label = cg.detectar_frente(texto)

    if frente_slug:
        _exec_gerar(chat_id, texto, frente_slug, frente_label, tipo)
    else:
        sm.set_state(chat_id, fluxo="roteamento", etapa="rota_aguardando_frente",
                     dados={**dados, "tipo": tipo})
        _show_rota_frente_selector(chat_id)

def _do_rota_frente(chat_id, frente_slug, frente_label):
    """Frente selecionada após seletor — dispara a geração."""
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})
    texto = dados.get("texto", "")
    tipo  = dados.get("tipo", "legenda")
    _exec_gerar(chat_id, texto, frente_slug, frente_label, tipo)

def _exec_gerar(chat_id, texto, frente_slug, frente_label, tipo):
    """Executa a geração e entra no fluxo gerar multi-turno."""
    tipo_label = {"legenda": "Legenda", "headline": "Headline", "roteiro": "Roteiro"}.get(tipo, tipo)
    send_text(f"⏳ Gerando {tipo_label} para <b>{html.escape(frente_label)}</b>…")

    cg = _cg()
    messages  = [{"role": "user", "content": texto}]
    resultado = cg.gerar(messages, frente_slug, tipo)

    _sm().set_state(chat_id,
        fluxo="gerar",
        etapa="aguardando_ajuste",
        dados={
            "frente_slug":     frente_slug,
            "frente_label":    frente_label,
            "tipo":            tipo,
            "pedido_original": texto,
            "messages":        messages + [{"role": "assistant", "content": resultado}],
        }
    )
    _send_resultado(frente_label, tipo, resultado)

def _do_rota_notion(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    texto = state.get("dados", {}).get("texto", "")
    sm.clear_state(chat_id)

    env = {"CAPTURA_ORIGEM": "Telegram", **{k: v for k, v in __import__("os").environ.items()}}
    r   = subprocess.run(
        ["python3", str(_HERE / "parse-captura.py"), texto],
        capture_output=True, text=True, env=env, timeout=30
    )

    if r.returncode == 0:
        try:
            cap = json.loads(r.stdout)
        except Exception:
            cap = {"titulo": texto[:80]}
        sm.set_last_capture(chat_id, cap)
        notion_url = cap.get("notion_url")
        btns = []
        if notion_url:
            btns.append({"text": "📲 Notion ↗", "url": notion_url})
        btns.append({"text": "📁 Drive ↗", "url": _DRIVE_URL})
        send_keyboard(
            f"✓ <b>Capturado no Notion</b>\n\n"
            f"📝 {html.escape(cap.get('titulo', texto[:60]))}",
            [btns]
        )
    else:
        send_text(f"❌ Erro ao capturar:\n<code>{html.escape(r.stderr[:200])}</code>")

def _do_rota_calendar(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    texto = state.get("dados", {}).get("texto", "")
    sm.set_state(chat_id, fluxo="agendar_cal", etapa="agendar_datetime",
                 dados={"titulo": texto},
                 historico=["principal", "agendar_titulo", "agendar_datetime"])
    _menu_agendar_datetime(chat_id)

# ── Dispatcher de callbacks ───────────────────────────────────────────────────

_FRENTE_MAP = {
    "frente_logika":  "Lógika",
    "frente_saude":   "Saúde",
    "frente_camara":  "Câmara",
    "frente_sindss":  "SINDSS",
    "frente_rogerio": "Rogério",
    "frente_pessoal": "Pessoal",
    "frente_inbox":   "Inbox",
}
_TIPO_MAP = {
    "tipo_ideia":       "Ideia",
    "tipo_tarefa":      "Tarefa",
    "tipo_compromisso": "Compromisso",
    "tipo_reuniao":     "Reunião",
    "tipo_gravacao":    "Gravação",
    "tipo_nota":        "Nota",
    "tipo_pendencia":   "Pendência",
}
# Mapeamento tipo → prefixo de captura
_TIPO_PREFIX = {
    "Ideia": "/i", "Tarefa": "/t", "Compromisso": "/c",
    "Reunião": "/r", "Gravação": "/g", "Nota": "/n", "Pendência": "/p",
}

def handle_callback(chat_id, callback_data):
    sm    = _sm()
    state = sm.get_state(chat_id)

    # Estado expirado
    if not state and callback_data not in {"menu_fechar"}:
        if callback_data.startswith("menu_") or callback_data.startswith("frente_") \
                or callback_data.startswith("tipo_") or callback_data.startswith("confirm_") \
                or callback_data.startswith("ideia_") or callback_data.startswith("proj_") \
                or callback_data.startswith("tpd_") or callback_data.startswith("tpg_") \
                or callback_data.startswith("dur_") or callback_data == "cal_create" \
                or callback_data.startswith("gerar_tipo_") \
                or callback_data.startswith("rota_") or callback_data.startswith("rota_frente_") \
                or callback_data.startswith("tarefas_") \
                or callback_data in {"gerar_salvar", "gerar_refazer", "gerar_limpo", "gerar_descartar"}:
            send_text("⏰ Esse menu expirou. Use /menu para recomeçar.")
            return

    # /gerar callbacks
    if callback_data.startswith("gerar_tipo_"):
        tipo = callback_data.replace("gerar_tipo_", "")
        _do_gerar(chat_id, tipo)
        return
    if callback_data == "gerar_limpo":
        handle_gerar_limpo(chat_id)
        return
    if callback_data == "gerar_salvar":
        handle_gerar_salvar(chat_id)
        return
    if callback_data == "gerar_refazer":
        handle_gerar_refazer(chat_id)
        return
    if callback_data == "gerar_descartar":
        handle_gerar_descartar(chat_id)
        return

    # /cancelar callbacks
    if callback_data == "cancel_yes":
        handle_cancel_yes(chat_id)
        return
    if callback_data == "cancel_no":
        handle_cancel_no(chat_id)
        return

    # /repetir callbacks
    if callback_data == "repetir_cancel":
        sm.clear_state(chat_id)
        send_text("↩️ Repetição cancelada.")
        return

    # Roteamento de texto livre
    if callback_data == "rota_notion":
        _do_rota_notion(chat_id)
        return
    if callback_data == "rota_calendar":
        _do_rota_calendar(chat_id)
        return
    if callback_data.startswith("rota_tipo_"):
        tipo = callback_data.replace("rota_tipo_", "")
        _do_rota_tipo(chat_id, tipo)
        return
    if callback_data in _ROTA_FRENTE_MAP:
        frente_slug, frente_label = _ROTA_FRENTE_MAP[callback_data]
        _do_rota_frente(chat_id, frente_slug, frente_label)
        return
    if callback_data == "rota_descartar":
        sm.clear_state(chat_id)
        send_text("🗑️ Descartado.")
        return

    # Tarefas
    if callback_data == "menu_tarefas":
        _menu_tarefas(chat_id)
        return
    if callback_data == "tarefas_tpd":
        _menu_tarefas_pedir_nome(chat_id, "tpd")
        return
    if callback_data == "tarefas_tpg":
        _menu_tarefas_pedir_nome(chat_id, "tpg")
        return

    # Menu principal
    if callback_data == "menu_notion":
        _menu_notion(chat_id)
    elif callback_data == "menu_google":
        _menu_google(chat_id)
    elif callback_data == "menu_gerar_cmd":
        sm.clear_state(chat_id)
        send_text(_GERAR_HELP)
    elif callback_data == "menu_capturar":
        _menu_frentes(chat_id)
    elif callback_data == "menu_ideia":
        _menu_ideia_titulo(chat_id)
    elif callback_data in _IDEIA_FRENTE_MAP:
        frente = _IDEIA_FRENTE_MAP[callback_data]
        sm.set_state(chat_id, dados={**state.get("dados", {}), "frente_label": frente})
        _menu_ideia_confirmacao(chat_id)
    elif callback_data == "ideia_salvar":
        _do_ideia_salvar(chat_id)
    elif callback_data in _DURACAO_MAP:
        label, mins = _DURACAO_MAP[callback_data]
        sm.set_state(chat_id, dados={**state.get("dados", {}), "duracao_min": mins, "duracao_label": label})
        _menu_agendar_confirmacao(chat_id)
    elif callback_data == "dur_outro":
        sm.set_state(chat_id, etapa="agendar_duracao_custom")
        send_text("⏱️ Digite a duração:\n\nEx: <code>45min</code> · <code>1h30</code> · <code>3h</code>")
    elif callback_data == "menu_agendar":
        _menu_agendar_titulo(chat_id)
    elif callback_data == "cal_create":
        _do_cal_create(chat_id)
    elif callback_data == "menu_agenda":
        cmd_agenda(chat_id, "")
    elif callback_data == "menu_buscar":
        sm.set_state(chat_id, fluxo="menu", etapa="aguardando_busca")
        send_text("🔍 Digite o termo a buscar:")
    elif callback_data == "menu_status":
        cmd_status(chat_id, "")
    elif callback_data == "menu_fechar":
        sm.clear_state(chat_id)
        send_text("Menu fechado. /menu pra abrir de novo.")
    elif callback_data == "menu_voltar":
        handle_menu_voltar(chat_id)

    # Escolha de frente
    elif callback_data in _FRENTE_MAP:
        frente = _FRENTE_MAP[callback_data]
        if frente == "Inbox":
            sm.set_state(chat_id, dados={"frente_label": "Inbox", "tipo_label": "Ideia"})
            _menu_pedir_texto(chat_id, "Inbox", "Ideia")
        else:
            sm.set_state(chat_id, dados={**state.get("dados", {}), "frente_label": frente})
            _menu_tipos(chat_id, frente)

    # Escolha de tipo
    elif callback_data in _TIPO_MAP:
        tipo  = _TIPO_MAP[callback_data]
        dados = state.get("dados", {})
        sm.set_state(chat_id, dados={**dados, "tipo_label": tipo})
        _menu_pedir_texto(chat_id, dados.get("frente_label", ""), tipo)

    # Data sim/não
    elif callback_data == "menu_data_sim":
        sm.set_state(chat_id, etapa="aguardando_data_texto")
        send_text("📅 Quando? (ex: amanhã 14h, sexta, 20/05 09h)")
    elif callback_data == "menu_data_nao":
        _menu_confirmacao(chat_id)

    # /projeto — escolha de frente ou ideia nova
    elif callback_data == "proj_ideia_nova":
        _do_ideia_nova(chat_id)
    elif callback_data in _PROJ_FRENTE_MAP:
        slug, label = _PROJ_FRENTE_MAP[callback_data]
        sm.set_state(chat_id, dados={**state.get("dados", {}), "frente_slug": slug, "frente_label": label})
        _do_projeto_criar(chat_id)

    # /tpd — escolha de frente → prazo → criar
    elif callback_data in _TPD_FRENTE_MAP:
        slug, label = _TPD_FRENTE_MAP[callback_data]
        sm.set_state(chat_id, dados={**state.get("dados", {}), "frente_slug": slug, "frente_label": label})
        _tpd_ask_prazo(chat_id)
    elif callback_data in ("tpd_prazo_hoje", "tpd_prazo_amanha", "tpd_prazo_semana", "tpd_prazo_sem"):
        _do_tpd_criar(chat_id, callback_data)

    # /tpg — escolha de projeto → (frente se não detectada) → prazo → criar
    elif callback_data.startswith("tpg_proj_"):
        idx      = int(callback_data.split("_")[-1])
        projetos = state.get("dados", {}).get("_projetos", [])
        if idx < len(projetos):
            proj_nome, proj_frente, _ = projetos[idx]
            new_dados = {**state.get("dados", {}), "projeto": proj_nome}
            if proj_frente:
                new_dados["frente_slug"]  = proj_frente
                new_dados["frente_label"] = proj_frente.replace("-", " ").capitalize()
            sm.set_state(chat_id, dados=new_dados)
            if proj_frente:
                _tpg_ask_prazo(chat_id)
            else:
                _tpg_ask_frente(chat_id)
    elif callback_data in _TPG_FRENTE_MAP:
        slug, label = _TPG_FRENTE_MAP[callback_data]
        sm.set_state(chat_id, dados={**state.get("dados", {}), "frente_slug": slug, "frente_label": label})
        _tpg_ask_prazo(chat_id)
    elif callback_data in ("tpg_prazo_hoje", "tpg_prazo_amanha", "tpg_prazo_semana", "tpg_prazo_sem"):
        _do_tpg_criar(chat_id, callback_data)

    # Confirmação final
    elif callback_data == "confirm_create":
        _do_create(chat_id)

def _do_create(chat_id):
    sm    = _sm()
    state = sm.get_state(chat_id)
    dados = state.get("dados", {})

    frente = dados.get("frente_label", "")
    tipo   = dados.get("tipo_label", "Ideia")
    titulo = dados.get("titulo", "")
    data_v = dados.get("data", "")
    hora_v = dados.get("hora", "")

    prefix  = _TIPO_PREFIX.get(tipo, "/i")
    text_in = f"{prefix} {titulo}"
    if data_v:
        text_in += f" {data_v}"
        if hora_v:
            text_in += f" {hora_v}"

    env = {"CAPTURA_ORIGEM": "Telegram", **{k: v for k, v in __import__("os").environ.items()}}
    r   = subprocess.run(
        ["python3", str(_HERE / "parse-captura.py"), text_in],
        capture_output=True, text=True, env=env, timeout=30
    )

    sm.clear_state(chat_id)

    if r.returncode == 0:
        try:
            cap = json.loads(r.stdout)
        except Exception:
            cap = {"titulo": titulo, "frente": frente, "data": data_v, "hora": hora_v}
        cap["frente"] = cap.get("frente") or frente
        sm.set_last_capture(chat_id, cap)

        lines = [
            "✓ <b>Capturado</b>", "",
            f"📝 <b>Título:</b> {html.escape(cap.get('titulo', titulo))}",
            f"🏢 <b>Frente:</b> {html.escape(cap.get('frente', frente))}",
            f"📂 <b>Tipo:</b>   {html.escape(tipo)}",
        ]
        if cap.get("data"):
            d = cap["data"]
            d_fmt = d[8:10] + "/" + d[5:7]
            lines.append(f"📅 <b>Data:</b>  {d_fmt}" + (f" às {cap['hora']}" if cap.get("hora") else ""))
        lines.append("🗓️ <i>Calendar: sync em ~7h</i>")
        notion_url = cap.get("notion_url")
        btns = []
        if notion_url:
            btns.append({"text": "📲 Notion ↗", "url": notion_url})
        btns.append({"text": "📁 Drive ↗", "url": _DRIVE_URL})
        send_keyboard("\n".join(lines), [btns])
    else:
        send_text(f"❌ Erro ao criar:\n<code>{html.escape(r.stderr[:200])}</code>")

# ── Handler de texto livre com estado ativo ────────────────────────────────────

def handle_free_text(chat_id, text):
    """Retorna True se o texto foi consumido pelo estado ativo."""
    sm    = _sm()
    state = sm.get_state(chat_id)

    # Sem estado ativo — perguntar o destino antes de rotear
    if not state:
        _show_destino_selector(chat_id, text)
        return True

    etapa = state.get("etapa")
    dados = state.get("dados", {})

    if etapa == "aguardando_busca":
        sm.clear_state(chat_id)
        cmd_buscar(chat_id, text)
        return True

    if etapa == "aguardando_titulo":
        pc = _pc_mod
        data_v, hora_v = None, None
        try:
            data_v, hora_v = pc.extract_date(text)
        except Exception:
            pass

        titulo_limpo = text.strip()
        sm.set_state(chat_id, dados={**dados, "titulo": titulo_limpo, "data": data_v, "hora": hora_v})

        if data_v:
            _menu_confirmacao(chat_id)
        else:
            _menu_pedir_data(chat_id, dados.get("frente_label", ""), dados.get("tipo_label", ""), titulo_limpo)
        return True

    if etapa == "aguardando_data_texto":
        pc = _pc_mod
        data_v, hora_v = None, None
        try:
            data_v, hora_v = pc.extract_date(text)
        except Exception:
            pass

        if not data_v:
            send_text(
                f"❌ Não entendi a data: <b>{html.escape(text[:60])}</b>\n\n"
                "Tenta de novo. Ex: amanhã 14h, sexta, 20/05 09h"
            )
            return True

        sm.set_state(chat_id, dados={**dados, "data": data_v, "hora": hora_v})
        _menu_confirmacao(chat_id)
        return True

    if state.get("fluxo") == "gerar" and etapa == "aguardando_tipo":
        send_text("☝️ Use os botões acima para escolher o tipo de conteúdo.")
        return True

    if state.get("fluxo") == "gerar" and etapa == "aguardando_ajuste":
        handle_gerar_ajuste(chat_id, text)
        return True

    if state.get("fluxo") == "repetir" and etapa == "aguardando_data":
        handle_repetir_data(chat_id, text)
        return True

    if etapa == "ideia_titulo":
        sm.set_state(chat_id, dados={**dados, "titulo": text.strip()})
        _menu_ideia_frente(chat_id)
        return True

    if etapa == "agendar_titulo":
        sm.set_state(chat_id, dados={**dados, "titulo": text.strip()})
        _menu_agendar_datetime(chat_id)
        return True

    if etapa in ("agendar_confirmar", "agendar_duracao"):
        send_text("☝️ Clique no botão acima para continuar.")
        return True

    if etapa == "agendar_duracao_custom":
        import re
        mins = None
        label = text.strip()
        t = text.strip().lower()
        m_hmin = re.match(r'^(\d+)h(\d+)', t)
        m_h    = re.match(r'^(\d+)\s*h', t)
        m_min  = re.match(r'^(\d+)\s*min', t)
        if m_hmin:
            mins  = int(m_hmin.group(1)) * 60 + int(m_hmin.group(2))
        elif m_h:
            mins  = int(m_h.group(1)) * 60
        elif m_min:
            mins  = int(m_min.group(1))
        if not mins or mins <= 0 or mins > 480:
            send_text("❌ Não entendi. Tenta: <code>45min</code>, <code>1h30</code>, <code>2h</code>")
            return True
        sm.set_state(chat_id, dados={**dados, "duracao_min": mins, "duracao_label": label})
        _menu_agendar_confirmacao(chat_id)
        return True

    if etapa == "tarefas_aguardando_nome":
        tipo = dados.get("tipo_tarefa", "tpd")
        sm.clear_state(chat_id)
        if tipo == "tpd":
            cmd_tpd(chat_id, text.strip())
        else:
            cmd_tpg(chat_id, text.strip())
        return True

    if etapa == "agendar_datetime":
        pc = _pc_mod
        data_v, hora_v = None, None
        try:
            data_v, hora_v = pc.extract_date(text)
        except Exception:
            pass

        if not data_v or not hora_v:
            send_text(
                "❌ Preciso de data <b>e</b> horário.\n\n"
                "Tenta de novo. Ex: <code>amanhã 14h</code>, <code>20/05 09h30</code>"
            )
            return True

        sm.set_state(chat_id, dados={**dados, "data": data_v, "hora": hora_v})
        _menu_agendar_duracao(chat_id)
        return True

    # Texto não se encaixa em nenhum fluxo ativo — mostrar seletor de destino
    sm.clear_state(chat_id)
    _show_destino_selector(chat_id, text)
    return True
