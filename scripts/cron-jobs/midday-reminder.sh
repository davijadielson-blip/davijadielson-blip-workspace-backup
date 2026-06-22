#!/bin/bash
# midday-reminder.sh — Roda todo dia às 13h (via launchd)
# Lembrete de reentrada no bloco Tático. Telegram + Email.

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
WEEKDAY=$(date +%u)

# Domingo: silencioso
[ "$WEEKDAY" -eq 7 ] && exit 0

source "$VAULT/scripts/.secrets/notion.env"
source "$VAULT/scripts/.secrets/telegram.env"

# ── Captura Geral: itens de hoje ainda pendentes ───────────────────────────────
HOJE_ITEMS=$(python3 << PYEOF
import json, urllib.request, sys
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
    "sorts": [{"property": "Data", "direction": "ascending"}],
    "page_size": 10,
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
        tipo   = (props.get("Tipo",  {}).get("select") or {}).get("name", "")
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

# ── Capturas feitas hoje de manhã (inbox) ─────────────────────────────────────
CAPTURAS_MANHA=$(find "$VAULT/[F0] 0-Inbox" -name "${DATE}-0[0-9]*-*.md" -o -name "${DATE}-1[01]*-*.md" 2>/dev/null \
  | while read f; do basename "$f" .md | sed 's/^[0-9-]*-//; s/-/ /g'; done \
  | head -5 || true)

# ── Pendências críticas ────────────────────────────────────────────────────────
CRITICAS=$(awk '/## 🔴 Críticas/,/## 🟡/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null \
  | grep "^\- \[ \]" | sed 's/^- \[ \] //' | head -3 || true)

# ── Monta mensagem Telegram ────────────────────────────────────────────────────
build_bullets() {
  local input="$1" prefix="${2:-  • }" empty="${3:-<i>nenhum</i>}"
  local out=""
  while IFS= read -r line; do [[ -z "$line" ]] && continue; out+="${prefix}${line}\n"; done <<< "$input"
  echo -e "${out:-  ${empty}}"
}

HOJE_BULLETS=$(build_bullets "$HOJE_ITEMS" "  " "<i>nenhum agendado</i>")
MANHA_BULLETS=$(build_bullets "$CAPTURAS_MANHA" "  • " "<i>nenhuma</i>")
CRITICAS_BULLETS=$(build_bullets "$CRITICAS" "  🔴 " "<i>nenhuma</i>")

TG_MSG="🌞 <b>Reentrada na tarde — 13h</b>

<b>🟥 Bloco atual:</b> Tático (mover · captar · editar · reunir)

<b>📅 Agenda de hoje</b>
${HOJE_BULLETS}
<b>📥 Capturas da manhã pra revisar</b>
${MANHA_BULLETS}
<b>🔴 Pendências críticas</b>
${CRITICAS_BULLETS}
<i>Foco, ritmo e entrega. 🎯</i>"

"$VAULT/scripts/lib/send-telegram.sh" "$TG_MSG" "HTML" || true

"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Lembrete 13h — $(date '+%d/%m/%Y')" \
  "$TG_MSG" 2>/dev/null || true
