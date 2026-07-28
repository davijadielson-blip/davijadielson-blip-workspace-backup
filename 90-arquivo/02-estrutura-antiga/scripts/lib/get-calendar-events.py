#!/usr/bin/env python3
"""
Busca eventos de TODOS os calendários Google para hoje.
Uso: python3 get-calendar-events.py [--format md|html]
"""
import sys
import json
import argparse
import warnings
from datetime import datetime, date
from pathlib import Path

warnings.filterwarnings("ignore")

SCRIPT_DIR = Path(__file__).parent
TOKEN_FILE = SCRIPT_DIR.parent / ".secrets" / "google-calendar-token.json"
TZ_OFFSET  = "-03:00"  # America/Maceio (UTC-3)

# Calendários a ignorar (só leitura, não relevantes para o briefing)
SKIP_CALENDARS = set()


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


def list_all_calendars(service):
    result = service.calendarList().list().execute()
    calendars = []
    for cal in result.get("items", []):
        cal_id   = cal["id"]
        cal_name = cal.get("summary", cal_id)
        if cal_id in SKIP_CALENDARS:
            continue
        calendars.append({"id": cal_id, "name": cal_name})
    return calendars


def fetch_events_for_calendar(service, cal_id):
    today = date.today().isoformat()
    try:
        result = service.events().list(
            calendarId=cal_id,
            timeMin=f"{today}T00:00:00{TZ_OFFSET}",
            timeMax=f"{today}T23:59:59{TZ_OFFSET}",
            singleEvents=True,
            orderBy="startTime",
            maxResults=20,
        ).execute()
        return result.get("items", [])
    except Exception:
        return []


def parse_start(event):
    """Retorna (sort_key, display_time)."""
    start = event.get("start", {})
    if "dateTime" in start:
        dt = datetime.fromisoformat(start["dateTime"])
        return (dt.hour * 60 + dt.minute, dt.strftime("%H:%M"))
    return (9999, "dia todo")  # all-day events ficam no final


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--format", choices=["md", "html"], default="md")
    args = parser.parse_args()
    fmt = args.format

    try:
        service    = get_service()
        calendars  = list_all_calendars(service)
        all_events = []

        for cal in calendars:
            events = fetch_events_for_calendar(service, cal["id"])
            for ev in events:
                sort_key, time_str = parse_start(ev)
                all_events.append({
                    "sort_key" : sort_key,
                    "time"     : time_str,
                    "summary"  : ev.get("summary", "(sem título)"),
                    "calendar" : cal["name"],
                })

        # Ordena por horário; remove duplicatas pelo título+hora (eventos que aparecem em vários calendários)
        seen = set()
        unique = []
        for ev in sorted(all_events, key=lambda x: x["sort_key"]):
            key = (ev["time"], ev["summary"])
            if key not in seen:
                seen.add(key)
                unique.append(ev)

        if not unique:
            print("  <i>Nenhum evento hoje</i>" if fmt == "html" else "*(nenhum evento)*")
            return

        for ev in unique:
            if fmt == "html":
                print(f"  {ev['time']} · <b>{ev['summary']}</b> <i>· {ev['calendar']}</i>")
            else:
                print(f"- {ev['time']} — {ev['summary']} [{ev['calendar']}]")

    except Exception as e:
        print("  <i>⚠️ Erro ao buscar agenda</i>" if fmt == "html" else "*(erro ao buscar agenda)*")
        print(f"ERRO: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
