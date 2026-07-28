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
    {"id": "375207e6-f145-8111-bba0-e132fd820542", "frente": "Saúde",  "color_id": "9"},   # Mirtilo — Produção & Agenda LÓGIKA
    # {"id": "...", "frente": "Câmara", "color_id": "5"},   # Banana
    # {"id": "...", "frente": "SINDSS", "color_id": "6"},   # Tangerina
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

def _extract_item(page, frente, color_id):
    props = page.get("properties", {})

    status = (props.get("Status", {}).get("select") or {}).get("name", "")
    if status in SKIP_STATUS:
        return None

    # Título: Nome (title field)
    title_parts = props.get("Nome", {}).get("title", [])
    title = "".join(t.get("plain_text", "") for t in title_parts).strip() or "(sem título)"

    # Data de publicação
    pub_date = (props.get("Data de publicação", {}).get("date") or {}).get("start")
    if not pub_date:
        return None

    # Data do evento (com horário, opcional)
    event_date_obj = props.get("Data do evento", {}).get("date") or {}
    event_date = event_date_obj.get("start")

    # Extras para descrição
    plataformas  = [o.get("name","") for o in props.get("Plataforma", {}).get("multi_select", [])]
    tipo_conteudo = [o.get("name","") for o in props.get("Tipo de conteúdo", {}).get("multi_select", [])]
    entrega      = [o.get("name","") for o in props.get("Entregas previstas", {}).get("multi_select", [])]
    obs          = props.get("Observações", {}).get("rich_text", [])
    obs_text     = "".join(o.get("plain_text","") for o in obs)
    cliente      = (props.get("Frente/Cliente", {}).get("select") or {}).get("name", "")
    roteiro      = (props.get("Briefing/Roteiro", {}).get("rich_text") or [])
    roteiro_text = "".join(t.get("plain_text","") for t in roteiro).strip()
    tipo         = (props.get("Tipo", {}).get("select") or {}).get("name", "")
    origem       = (props.get("Origem", {}).get("select") or {}).get("name", "")

    description_parts = []
    description_parts.append(f"Frente: {frente}")
    if cliente and cliente != frente:
        description_parts.append(f"Cliente: {cliente}")
    if tipo:
        description_parts.append(f"Tipo: {tipo}")
    if origem:
        description_parts.append(f"Origem: {origem}")
    if plataformas:
        description_parts.append(f"Plataforma: {', '.join(plataformas)}")
    if tipo_conteudo:
        description_parts.append(f"Tipo de conteúdo: {', '.join(tipo_conteudo)}")
    if entrega:
        description_parts.append(f"Entregas: {', '.join(entrega)}")
    if status:
        description_parts.append(f"Status: {status}")
    if obs_text:
        description_parts.append(f"Obs: {obs_text}")
    if roteiro_text:
        description_parts.append(f"\nRoteiro/Briefing:\n{roteiro_text}")
    description_parts.append(f"\nNotion: https://notion.so/{page['id'].replace('-','')}")

    return {
        "notion_id": page["id"],
        "title": title,
        "pub_date": pub_date,
        "event_date": event_date,
        "description": "\n".join(description_parts),
        "status": status,
        "color_id": color_id,
        "frente": frente,
        "cliente": cliente,
    }


def _fetch_from_producao():
    """Busca todos os itens com Data de publicação na Produção & Agenda."""
    import urllib.request as ur
    url = f"https://api.notion.com/v1/databases/{DATABASES[0]['id']}/query"
    payload = json.dumps({
        "filter": {
            "property": "Data de publicação",
            "date": {"is_not_empty": True}
        },
        "page_size": 100
    }).encode()

    req = ur.Request(url, data=payload, headers=notion_headers(), method="POST")
    with ur.urlopen(req) as resp:
        data = json.loads(resp.read())

    # Mapeia nomes de clientes → cor/frente
    CLIENTE_MAP = {
        "Secretaria de Saúde": {"frente": "Saúde", "color_id": "9"},
        "Câmara":             {"frente": "Câmara", "color_id": "5"},
        "SINDSS":             {"frente": "SINDSS", "color_id": "6"},
    }
    DEFAULT = {"frente": "LÓGIKA", "color_id": "7"}

    items = []
    by_frente = {}
    for page in data.get("results", []):
        props = page.get("properties", {})
        cliente = (props.get("Frente/Cliente", {}).get("select") or {}).get("name", "")
        cfg = CLIENTE_MAP.get(cliente, DEFAULT)
        item = _extract_item(page, cfg["frente"], cfg["color_id"])
        if item:
            items.append(item)
            by_frente[cfg["frente"]] = by_frente.get(cfg["frente"], 0) + 1

    for f, count in sorted(by_frente.items()):
        log(f"  ✅ {f}: {count} itens")
    return items


def fetch_notion_items():
    log("📥 Buscando Produção & Agenda — LÓGIKA...")
    try:
        items = _fetch_from_producao()
        log(f"✅ Total: {len(items)} itens elegíveis no Notion (Produção & Agenda)")
        return items
    except Exception as e:
        log(f"  ⚠️  Erro ao buscar Produção & Agenda: {e}")
        return []


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
_CAPTURA_TIPOS_SYNC = {"Captura", "Compromisso"}
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
                {"property": "Status de triagem", "select": {"does_not_equal": "Descartado"}},
                {"property": "Status de triagem", "select": {"does_not_equal": "Arquivado"}},
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
        tipo   = (props.get("Tipo de entrada", {}).get("select") or {}).get("name", "")
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

        # gcal_event_id — não existe no schema atual, sempre recria
        gcal_id = ""

        # Frente
        frente = (props.get("Frente/Cliente", {}).get("select") or {}).get("name", "Geral")

        # Status
        status_triagem = (props.get("Status de triagem", {}).get("select") or {}).get("name", "")

        items.append({
            "notion_id": page["id"],
            "title":     title,
            "tipo":      tipo,
            "frente":    frente,
            "date_str":  start,
            "gcal_id":   gcal_id,
            "color_id":  _CAPTURA_COLOR.get(tipo, "11"),
            "status":    status_triagem,
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

    created = updated = errors = 0
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
                # Notion não tem campos gcal_event_id/sincronizado — pula atualização
                # Se precisar no futuro, adicionar propriedades no banco Inbox.
                created += 1
        except Exception as e:
            log(f"  ⚠️  Erro em '{item['title']}': {e}")
            errors += 1

    log(f"  ✅ Captura: {created} criados | {updated} atualizados | {errors} erros")
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
