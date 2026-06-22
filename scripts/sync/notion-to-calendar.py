#!/usr/bin/env python3
"""
Sync unidirecional: Notion → Google Calendar
  1. Calendário Editorial (Saúde, Câmara, SINDSS…) → eventos de publicação
  2. Captura Geral (Compromissos, Reuniões, Gravações) → eventos de agenda pessoal
Roda via cron (daily-brief 7h) ou manualmente.
Log em memory/sessions/sync/YYYY-MM-DD.md
"""

import os
import json
import sys
import warnings
from datetime import datetime, date, timedelta
from pathlib import Path

warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
VAULT         = Path(__file__).parent.parent.parent
SECRETS_DIR   = Path(__file__).parent.parent / ".secrets"
TOKEN_FILE    = SECRETS_DIR / "google-calendar-token.json"
CREDS_FILE    = SECRETS_DIR / "google-calendar-credentials.json"
LOG_DIR       = VAULT / "memory/sessions/sync"
MAPPING_FILE  = VAULT / "memory/databases/notion-calendar-mapping.json"

LOG_DIR.mkdir(parents=True, exist_ok=True)

TODAY = date.today().isoformat()
LOG_FILE = LOG_DIR / f"{TODAY}.md"

# ── Notion config ──────────────────────────────────────────────────────────────
def _load_notion_env():
    env = {}
    for line in (SECRETS_DIR / "notion.env").read_text().splitlines():
        line = line.strip()
        if "=" in line and not line.startswith("#"):
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"')
    return env

_notion_env   = _load_notion_env()
NOTION_TOKEN   = _notion_env["NOTION_TOKEN"]
NOTION_VERSION = "2022-06-28"
CALENDAR_ID    = "primary"

# Status que NÃO devem ser sincronizados
SKIP_STATUS = {"CANCELADO", "ABORTADO", "REPROVADO", "PUBLICADO"}

# ── Espaços de equipe — um dict por frente/cliente ─────────────────────────────
# Para novo cliente: adicionar {"id": "...", "frente": "Nome", "color_id": "X"}
# colorId Google Calendar: 9=Mirtilo · 5=Banana · 6=Tangerina · 11=Tomate
DATABASES = [
    {"id": "1d8207e6-f145-8153-99c1-f5ae2b4e4e23", "frente": "Saúde",  "color_id": "9"},   # Mirtilo
    {"id": "52a83dbb-9d10-40b6-87c3-687013d92138", "frente": "Câmara", "color_id": "5"},   # Banana
    {"id": "5ca1a34c-342b-406a-8c71-4b8b63e0a1f5", "frente": "SINDSS", "color_id": "6"},   # Tangerina
    # {"id": "...", "frente": "...",    "color_id": "11"},  # Tomate   — outros clientes
]


# ── Helpers ────────────────────────────────────────────────────────────────────

def log(msg):
    print(msg)

def notion_headers():
    return {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }

def get_google_service():
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


# ── Notion: buscar itens elegíveis ─────────────────────────────────────────────

def _fetch_from_database(db):
    import urllib.request
    url = f"https://api.notion.com/v1/databases/{db['id']}/query"
    payload = json.dumps({
        "filter": {
            "property": "Data da Publicacao ",
            "date": {"is_not_empty": True}
        },
        "page_size": 100
    }).encode()

    req = urllib.request.Request(url, data=payload, headers=notion_headers(), method="POST")
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read())

    items = []
    for page in data.get("results", []):
        props = page.get("properties", {})

        status = (props.get("Status", {}).get("status") or {}).get("name", "")
        if status in SKIP_STATUS:
            continue

        # Título: CRIATIVO (principal) → Linhas Editoriais → "(sem título)"
        criativo = (props.get("CRIATIVO", {}).get("rich_text") or [])
        criativo_text = "".join(t.get("plain_text", "") for t in criativo).strip()

        title_parts = props.get("Linhas Editoriais ", {}).get("title", [])
        linha_text = "".join(t.get("plain_text", "") for t in title_parts).strip()

        title = criativo_text or linha_text or "(sem título)"

        # Data de publicação
        pub_date = (props.get("Data da Publicacao ", {}).get("date") or {}).get("start")
        if not pub_date:
            continue

        # Data do evento (com horário, opcional)
        event_date_obj = props.get("Data do Evento", {}).get("date") or {}
        event_date = event_date_obj.get("start")

        # Extras para descrição
        plataformas  = [o.get("name","") for o in props.get("Plataforma ", {}).get("multi_select", [])]
        formatos     = [o.get("name","") for o in props.get("Formato de Post", {}).get("multi_select", [])]
        obs          = props.get("Observações", {}).get("rich_text", [])
        obs_text     = "".join(o.get("plain_text","") for o in obs)
        setor        = (props.get("SETOR", {}).get("rich_text") or [])
        setor_text   = "".join(t.get("plain_text","") for t in setor).strip()
        roteiro      = (props.get("ROTEIROS/BRIEFENG", {}).get("rich_text") or [])
        roteiro_text = "".join(t.get("plain_text","") for t in roteiro).strip()

        description_parts = []
        description_parts.append(f"Frente: {db['frente']}")
        if setor_text:
            description_parts.append(f"Setor: {setor_text}")
        if plataformas:
            description_parts.append(f"Plataforma: {', '.join(plataformas)}")
        if formatos:
            description_parts.append(f"Formato: {', '.join(formatos)}")
        if status:
            description_parts.append(f"Status: {status}")
        if obs_text:
            description_parts.append(f"Obs: {obs_text}")
        if roteiro_text:
            description_parts.append(f"\nRoteiro/Briefing:\n{roteiro_text}")
        description_parts.append(f"\nNotion: https://notion.so/{page['id'].replace('-','')}")

        items.append({
            "notion_id": page["id"],
            "title": title,
            "pub_date": pub_date,
            "event_date": event_date,
            "description": "\n".join(description_parts),
            "status": status,
            "color_id": db["color_id"],
            "frente": db["frente"],
        })

    return items

def fetch_notion_items():
    all_items = []
    for db in DATABASES:
        try:
            items = _fetch_from_database(db)
            log(f"  ✅ {db['frente']}: {len(items)} itens")
            all_items.extend(items)
        except Exception as e:
            log(f"  ⚠️  Erro ao buscar {db['frente']}: {e}")
    return all_items


# ── Google Calendar: buscar eventos existentes do script ──────────────────────

def fetch_existing_events(service):
    """Retorna dict notion_id → event_id para eventos já criados por este script."""
    mapping = {}
    if MAPPING_FILE.exists():
        try:
            mapping = json.loads(MAPPING_FILE.read_text())
        except Exception:
            mapping = {}
    return mapping

def save_mapping(mapping):
    MAPPING_FILE.parent.mkdir(parents=True, exist_ok=True)
    MAPPING_FILE.write_text(json.dumps(mapping, indent=2, ensure_ascii=False))


# ── Criar / atualizar evento ───────────────────────────────────────────────────

def build_event(item):
    title    = item['title'].upper()
    color_id = item["color_id"]

    # Usa event_date (com hora) se disponível; senão pub_date (all-day)
    date_str = item["event_date"] or item["pub_date"]
    has_time = "T" in date_str

    if has_time:
        start = {"dateTime": date_str, "timeZone": "America/Maceio"}
        end   = {"dateTime": date_str, "timeZone": "America/Maceio"}
    else:
        next_day = (datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        start = {"date": date_str}
        end   = {"date": next_day}

    return {
        "summary": title,
        "description": item["description"],
        "start": start,
        "end": end,
        "colorId": color_id,
        "extendedProperties": {
            "private": {"notion_id": item["notion_id"]}
        }
    }

def sync(service, items, mapping):
    created = updated = skipped = errors = 0

    for item in items:
        nid = item["notion_id"]
        event_body = build_event(item)

        try:
            if nid in mapping:
                # Atualizar evento existente
                service.events().update(
                    calendarId=CALENDAR_ID,
                    eventId=mapping[nid],
                    body=event_body
                ).execute()
                updated += 1
            else:
                # Criar novo evento
                result = service.events().insert(
                    calendarId=CALENDAR_ID,
                    body=event_body
                ).execute()
                mapping[nid] = result["id"]
                created += 1
        except Exception as e:
            log(f"  ⚠️  Erro em '{item['title']}': {e}")
            errors += 1

    save_mapping(mapping)
    return created, updated, skipped, errors


# ── Captura Geral → Google Calendar ───────────────────────────────────────────
# Sincroniza Compromissos, Reuniões e Gravações com Data preenchida.
# gcal_event_id e sincronizado são atualizados diretamente na página Notion.

_CAPTURA_DB_ID = None  # carregado lazy de notion.env
_CAPTURA_TIPOS_SYNC = {"Compromisso", "Reunião", "Gravação"}
_CAPTURA_COLOR = {"Compromisso": "11", "Reunião": "9", "Gravação": "5"}  # Tomate, Mirtilo, Banana


def _load_captura_db_id():
    global _CAPTURA_DB_ID
    if _CAPTURA_DB_ID:
        return _CAPTURA_DB_ID
    secrets = Path(__file__).parent.parent / ".secrets" / "notion.env"
    for line in secrets.read_text().splitlines():
        if line.startswith("NOTION_CAPTURA_DATABASE_ID"):
            _CAPTURA_DB_ID = line.split("=", 1)[1].strip().strip('"')
            return _CAPTURA_DB_ID
    raise RuntimeError("NOTION_CAPTURA_DATABASE_ID não encontrado em notion.env")


def _fetch_captura_items():
    import urllib.request as ur
    db_id = _load_captura_db_id()
    url   = f"https://api.notion.com/v1/databases/{db_id}/query"
    payload = json.dumps({
        "filter": {
            "and": [
                {"property": "Data",   "date": {"is_not_empty": True}},
                {"property": "Status", "select": {"does_not_equal": "Cancelado"}},
            ]
        },
        "page_size": 100,
    }).encode()

    req = ur.Request(url, data=payload, headers=notion_headers(), method="POST")
    with ur.urlopen(req) as resp:
        data = json.loads(resp.read())

    items = []
    for page in data.get("results", []):
        props  = page.get("properties", {})
        tipo   = (props.get("Tipo", {}).get("select") or {}).get("name", "")
        if tipo not in _CAPTURA_TIPOS_SYNC:
            continue

        # Título
        title_parts = props.get("Título", {}).get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_parts).strip() or "(sem título)"

        # Data
        date_obj = (props.get("Data", {}).get("date") or {})
        start    = date_obj.get("start")
        if not start:
            continue

        # gcal_event_id já existente
        gcal_parts = props.get("gcal_event_id", {}).get("rich_text", [])
        gcal_id    = "".join(t.get("plain_text", "") for t in gcal_parts).strip()

        # Frente
        frente = (props.get("Frente", {}).get("select") or {}).get("name", "Geral")

        items.append({
            "notion_id": page["id"],
            "title":     title,
            "tipo":      tipo,
            "frente":    frente,
            "date_str":  start,
            "gcal_id":   gcal_id,
            "color_id":  _CAPTURA_COLOR.get(tipo, "11"),
        })
    return items


def _update_notion_gcal(notion_id, gcal_event_id):
    import urllib.request as ur
    url  = f"https://api.notion.com/v1/pages/{notion_id}"
    body = json.dumps({
        "properties": {
            "gcal_event_id": {"rich_text": [{"text": {"content": gcal_event_id}}]},
            "sincronizado":  {"checkbox": True},
        }
    }).encode()
    req = ur.Request(url, data=body, headers=notion_headers(), method="PATCH")
    with ur.urlopen(req) as resp:
        return json.loads(resp.read())


def _build_captura_event(item):
    has_time = "T" in item["date_str"]
    if has_time:
        start = end = {"dateTime": item["date_str"], "timeZone": "America/Maceio"}
    else:
        next_day = (datetime.strptime(item["date_str"], "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        start = {"date": item["date_str"]}
        end   = {"date": next_day}
    return {
        "summary":     f"{item['tipo'].upper()}: {item['title']}",
        "description": f"Frente: {item['frente']}\nTipo: {item['tipo']}\nNotion: https://notion.so/{item['notion_id'].replace('-','')}",
        "start":       start,
        "end":         end,
        "colorId":     item["color_id"],
        "extendedProperties": {"private": {"captura_notion_id": item["notion_id"]}},
    }


def sync_captura(service):
    log("\n📥 Sincronizando Captura Geral → Calendar...")
    try:
        items = _fetch_captura_items()
    except Exception as e:
        log(f"  ⚠️  Erro ao buscar Captura Geral: {e}")
        return 0, 0

    created = updated = 0
    for item in items:
        event_body = _build_captura_event(item)
        try:
            if item["gcal_id"]:
                service.events().update(
                    calendarId=CALENDAR_ID, eventId=item["gcal_id"], body=event_body
                ).execute()
                updated += 1
            else:
                result = service.events().insert(
                    calendarId=CALENDAR_ID, body=event_body
                ).execute()
                _update_notion_gcal(item["notion_id"], result["id"])
                created += 1
        except Exception as e:
            log(f"  ⚠️  Erro em '{item['title']}': {e}")

    log(f"  ✅ Captura: {created} criados | {updated} atualizados")
    return created, updated


def main():
    start_time = datetime.now()
    log(f"Sync Notion → Calendar iniciado: {start_time.strftime('%d/%m/%Y %H:%M')}")

    try:
        service = get_google_service()
        log("✅ Google Calendar autenticado")
    except Exception as e:
        log(f"❌ Falha na autenticação Google: {e}")
        sys.exit(1)

    try:
        items = fetch_notion_items()
        log(f"✅ {len(items)} itens elegíveis no Notion (Editorial)")
    except Exception as e:
        log(f"❌ Falha ao buscar Notion: {e}")
        sys.exit(1)

    mapping = fetch_existing_events(service)
    created, updated, skipped, errors = sync(service, items, mapping)

    # Captura Geral
    cap_created, cap_updated = sync_captura(service)

    duration = (datetime.now() - start_time).seconds

    report = f"""---
tipo: sync-log
data: {TODAY}
gerado-por: notion-to-calendar
revisado: false
---

# Sync Notion → Calendar — {TODAY}

**Horário:** {start_time.strftime('%H:%M')}
**Duração:** {duration}s

## Calendário Editorial
- ✅ Criados: {created}
- 🔄 Atualizados: {updated}
- ⚠️ Erros: {errors}
- Total: {len(items)}

## Captura Geral
- ✅ Criados: {cap_created}
- 🔄 Atualizados: {cap_updated}

## Itens do Editorial sincronizados
"""
    for item in items:
        report += f"- {item['pub_date']} — {item['title']} [{item['status']}]\n"

    if errors:
        report += f"\n## ⚠️ Atenção\n{errors} item(ns) com erro — verifique o log do terminal.\n"

    LOG_FILE.write_text(report)
    log(f"\n📋 Log: {LOG_FILE}")
    log(f"✅ Editorial: {created} criados, {updated} atualizados | Captura: {cap_created} criados, {cap_updated} atualizados")


if __name__ == "__main__":
    main()
