#!/usr/bin/env python3
"""
Time Blocking semanal — cria blocos automáticos no Google Calendar para a próxima semana.
Roda via saturday-planning.sh (sábado 17h).

Lógica:
  Seg/Qua/Sex → Externo (campo, gravações, clientes)
  Ter/Qui     → Agência (foco profundo, edição, legendas)
  Dom         → Livre — nenhum bloco criado
  Buffer de 2h por dia reservado (16h-18h)
  Compromissos/Reuniões: +30 min de prep antes, +30 min de follow-up depois
"""

import json
import warnings
from datetime import date, datetime, timedelta
from pathlib import Path

warnings.filterwarnings("ignore")

SECRETS_DIR = Path(__file__).parent.parent / ".secrets"
TOKEN_FILE  = SECRETS_DIR / "google-calendar-token.json"
CALENDAR_ID = "primary"
TZ          = "America/Maceio"
TZ_OFFSET   = "-03:00"

# Marca todos os eventos criados por este script — usado para limpar antes de recriar
AUTO_MARKER = "sc_auto_block"

# Cores Google Calendar
COLOR_BLOCK  = "8"   # Grafite  — blocos de trabalho
COLOR_BUFFER = "2"   # Sage     — buffer livre
COLOR_PREP   = "6"   # Tangerina — prep/follow-up

# 0=Seg 1=Ter 2=Qua 3=Qui 4=Sex 5=Sab 6=Dom
DAY_TYPE = {0: "externo", 1: "agencia", 2: "externo", 3: "agencia", 4: "externo"}
# Sab (5) e Dom (6) ficam de fora → sem blocos automáticos

# Blocos fixos por tipo de dia: (h_ini, m_ini, h_fim, m_fim, nome, cor)
BLOCKS = {
    "externo": [
        (8, 30, 11, 30, "🎬 Campo / Gravações",       COLOR_BLOCK),
        (13, 0, 16, 0,  "🤝 Atendimentos / Clientes", COLOR_BLOCK),
        (16, 0, 18, 0,  "🔲 Buffer Livre",             COLOR_BUFFER),
    ],
    "agencia": [
        (8, 30, 12, 0,  "🖥️ Agência — Foco Profundo", COLOR_BLOCK),
        (13, 0, 16, 0,  "✂️ Edição & Legendas",        COLOR_BLOCK),
        (16, 0, 18, 0,  "🔲 Buffer Livre",             COLOR_BUFFER),
    ],
}


# ── Google Calendar ─────────────────────────────────────────────────────────────

def get_service():
    import google.oauth2.credentials
    import googleapiclient.discovery
    from google.auth.transport.requests import Request

    token_data = json.loads(TOKEN_FILE.read_text())
    creds = google.oauth2.credentials.Credentials(
        token=token_data.get("token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=token_data.get("token_uri"),
        client_id=token_data.get("client_id"),
        client_secret=token_data.get("client_secret"),
    )
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
        TOKEN_FILE.write_text(creds.to_json())
    return googleapiclient.discovery.build("calendar", "v3", credentials=creds, cache_discovery=False)


def _dt(day: date, h: int, m: int) -> str:
    return f"{day.isoformat()}T{h:02d}:{m:02d}:00{TZ_OFFSET}"


def _event_body(summary, start_dt, end_dt, color, description=""):
    return {
        "summary": summary,
        "description": description,
        "start": {"dateTime": start_dt, "timeZone": TZ},
        "end":   {"dateTime": end_dt,   "timeZone": TZ},
        "colorId": color,
        "extendedProperties": {"private": {AUTO_MARKER: "true"}},
    }


# ── Limpar blocos antigos da semana ─────────────────────────────────────────────

def delete_old_auto_blocks(service, week_start: date, week_end: date):
    deleted = 0
    page_token = None
    while True:
        result = service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=f"{week_start.isoformat()}T00:00:00{TZ_OFFSET}",
            timeMax=f"{week_end.isoformat()}T23:59:59{TZ_OFFSET}",
            privateExtendedProperty=f"{AUTO_MARKER}=true",
            singleEvents=True,
            pageToken=page_token,
            maxResults=100,
        ).execute()
        for ev in result.get("items", []):
            service.events().delete(calendarId=CALENDAR_ID, eventId=ev["id"]).execute()
            deleted += 1
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    return deleted


# ── Buscar compromissos/reuniões do Calendar na semana ─────────────────────────

def fetch_commitments(service, week_start: date, week_end: date):
    """Retorna eventos com prefixo COMPROMISSO: ou REUNIÃO: (criados pelo sync Captura)."""
    result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=f"{week_start.isoformat()}T00:00:00{TZ_OFFSET}",
        timeMax=f"{week_end.isoformat()}T23:59:59{TZ_OFFSET}",
        singleEvents=True,
        orderBy="startTime",
        maxResults=100,
    ).execute()

    commits = []
    for ev in result.get("items", []):
        summary = ev.get("summary", "")
        start   = ev.get("start", {})
        if not start.get("dateTime"):
            continue
        if any(summary.upper().startswith(p) for p in ("COMPROMISSO:", "REUNIÃO:", "REUNIAO:", "GRAVAÇÃO:", "GRAVACAO:")):
            commits.append({
                "summary": summary,
                "start":   datetime.fromisoformat(start["dateTime"]),
                "end":     datetime.fromisoformat(ev.get("end", {}).get("dateTime", start["dateTime"])),
            })
    return commits


# ── Criar blocos fixos ─────────────────────────────────────────────────────────

def create_fixed_blocks(service, week_start: date):
    created = 0
    for offset in range(5):  # Seg a Sex
        day      = week_start + timedelta(days=offset)
        weekday  = day.weekday()
        day_type = DAY_TYPE.get(weekday)
        if not day_type:
            continue

        for (h_ini, m_ini, h_fim, m_fim, name, color) in BLOCKS[day_type]:
            body = _event_body(
                summary    = name,
                start_dt   = _dt(day, h_ini, m_ini),
                end_dt     = _dt(day, h_fim, m_fim),
                color      = color,
                description= f"Bloco automático — {day_type.capitalize()}",
            )
            service.events().insert(calendarId=CALENDAR_ID, body=body).execute()
            created += 1
    return created


# ── Criar blocos de proteção (prep + follow-up) ────────────────────────────────

def create_protection_blocks(service, commitments):
    created = 0
    for ev in commitments:
        name  = ev["summary"]
        start = ev["start"]
        end   = ev["end"]

        # Prep: 30 min antes
        prep_end   = start
        prep_start = start - timedelta(minutes=30)
        service.events().insert(calendarId=CALENDAR_ID, body=_event_body(
            summary    = f"📋 Prep: {name}",
            start_dt   = prep_start.isoformat(),
            end_dt     = prep_end.isoformat(),
            color      = COLOR_PREP,
            description= "Preparação automática — 30 min antes do compromisso",
        )).execute()
        created += 1

        # Follow-up: 30 min depois
        follow_start = end
        follow_end   = end + timedelta(minutes=30)
        service.events().insert(calendarId=CALENDAR_ID, body=_event_body(
            summary    = f"✅ Follow-up: {name}",
            start_dt   = follow_start.isoformat(),
            end_dt     = follow_end.isoformat(),
            color      = COLOR_PREP,
            description= "Follow-up automático — 30 min após o compromisso",
        )).execute()
        created += 1

    return created


# ── Main ───────────────────────────────────────────────────────────────────────

def run():
    today      = date.today()
    days_ahead = (7 - today.weekday()) % 7 or 7   # próxima segunda
    week_start = today + timedelta(days=days_ahead)
    week_end   = week_start + timedelta(days=4)    # sexta

    print(f"Time Blocking: {week_start} → {week_end}")

    service = get_service()

    deleted = delete_old_auto_blocks(service, week_start, week_end)
    print(f"  🗑️  Blocos antigos removidos: {deleted}")

    fixed = create_fixed_blocks(service, week_start)
    print(f"  📦 Blocos fixos criados: {fixed}")

    commitments = fetch_commitments(service, week_start, week_end)
    print(f"  🔎 Compromissos/Reuniões encontrados: {len(commitments)}")

    protection = create_protection_blocks(service, commitments)
    print(f"  🛡️  Blocos de proteção criados: {protection}")

    total = fixed + protection
    print(f"  ✅ Total criado: {total} blocos para a semana de {week_start.strftime('%d/%m')}")

    # Resumo para o Telegram/Email
    day_names = ["Seg", "Ter", "Qua", "Qui", "Sex"]
    lines = []
    for i in range(5):
        d = week_start + timedelta(days=i)
        dtype = DAY_TYPE.get(d.weekday(), "")
        icon = "🎬" if dtype == "externo" else "🖥️"
        lines.append(f"  {day_names[i]} {d.strftime('%d/%m')} — {icon} {dtype.capitalize() if dtype else '—'}")

    return "\n".join(lines), total


if __name__ == "__main__":
    summary, total = run()
    print(f"\nResumo da semana:\n{summary}")
