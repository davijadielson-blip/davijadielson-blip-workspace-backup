#!/usr/bin/env python3
"""
Organiza o Gmail de Jadielson:
  1. Cria / atualiza labels por categoria
  2. Classifica TODOS os emails sem label (histórico completo, paginado)
  3. Cria filtros automáticos no Gmail para novos emails

Uso: python3 organize-gmail.py [--filters-only | --history-only]
"""
import json
import sys
import time
import warnings
import argparse
from pathlib import Path

warnings.filterwarnings("ignore")

VAULT      = Path(__file__).parent.parent.parent
SECRETS    = VAULT / "scripts/.secrets"
CREDS_FILE = SECRETS / "google-calendar-credentials.json"
TOKEN_FILE = SECRETS / "gmail-token.json"
SCOPES     = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.settings.basic",
]


# ── Autenticação ───────────────────────────────────────────────────────────────

def get_service():
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    import googleapiclient.discovery

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("🌐 Abrindo navegador para autorizar o Gmail...")
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return googleapiclient.discovery.build("gmail", "v1", credentials=creds, cache_discovery=False)


# ── Definição de labels ────────────────────────────────────────────────────────

LABELS_CONFIG = [
    ("Segundo Cérebro",      "#16a766", "#ffffff"),
    ("Dev & Ferramentas",    "#4986e7", "#ffffff"),
    ("Google",               "#4986e7", "#ffffff"),
    ("Eventos",              "#f691b2", "#000000"),
    ("Newsletters",          "#ffad46", "#000000"),
    ("Financeiro",           "#cc3a21", "#ffffff"),
    ("Financeiro/Cartões",   "#cc3a21", "#ffffff"),
    ("Financeiro/Cobranças", "#cc3a21", "#ffffff"),
    ("Financeiro/Recibos",   "#cc3a21", "#ffffff"),
    ("Compras & Lojas",      "#a479e2", "#ffffff"),
    ("Redes Sociais",        "#b3efd3", "#000000"),
    ("Marketing",            "#e3d7ff", "#000000"),
]


# ── Regras de classificação ────────────────────────────────────────────────────

def classify(sender, subject):
    s   = sender.lower()
    sub = subject.lower()

    if "segundo cérebro" in sub or "segundo cerebro" in sub:
        return "Segundo Cérebro"

    if any(x in s for x in ["github.com", "anthropic.com", "openai.com", "n8n.io",
                              "email.claude.com"]):
        return "Dev & Ferramentas"
    if any(x in sub for x in ["[github]", "[task update]"]):
        return "Dev & Ferramentas"

    if any(x in s for x in ["google.com", "onedrive.com", "calendar-notification"]):
        return "Google"

    if "mail.anthropic.com" in s or "invoice+statements" in s:
        return "Financeiro/Recibos"
    if "receipt" in sub or "recibo" in sub or "fatura" in sub and "nubank" in s:
        return "Financeiro/Recibos"

    if "nubank.com.br" in s:
        return "Financeiro/Cartões"
    if any(x in s for x in ["bradesco", "itau", "santander", "caixa.gov", "bb.com.br",
                              "banco", "c6bank", "inter.co", "picpay"]):
        return "Financeiro/Cartões"

    if any(x in s for x in ["acordocerto", "queroquitar", "scpc", "cobranca",
                              "serasa", "boa vista", "negativado", "acerto.com",
                              "tmbeducacao", "evoluawp"]):
        return "Financeiro/Cobranças"
    if any(x in sub for x in ["débito", "debito", "pendência", "pendencia",
                                "quitação", "quitacao", "negativado", "cpf",
                                "renegoci", "acordo", "boleto em aberto"]):
        return "Financeiro/Cobranças"

    if any(x in s for x in ["shein.com", "temuemail.com", "magazineluiza",
                              "americanas", "submarino", "shopee", "aliexpress",
                              "mercadolivre", "amazon"]):
        return "Compras & Lojas"

    if "denderson2013@gmail.com" in s or "convite de remetente" in sub:
        return "Eventos"
    if any(x in sub for x in ["você foi convidado", "convite para", "imersão"]):
        return "Eventos"

    if any(x in s for x in ["instagram.com", "facebookmail.com", "twitter.com",
                              "linkedin.com", "tiktok.com", "youtube.com"]):
        return "Redes Sociais"

    if any(x in s for x in ["ted.com", "empiricus.com.br", "comunicacao-exame.com",
                              "exame.com", "infomoney", "moneytimes"]):
        return "Newsletters"
    if any(x in sub for x in ["newsletter", "daily digest", "weekly digest"]):
        return "Newsletters"

    if any(x in sub for x in ["acesso", "senha", "login", "bem-vindo à plataforma",
                                "confirme seu cadastro", "verify your email",
                                "ative sua conta", "seu acesso", "credenciais"]):
        return "CURSOS"

    marketing_senders = [
        "gestoraia", "caroliasmim", "elainneourives", "danilohgomes",
        "sofisadireto", "evoluawp", "mkt.", "marketing@", "email@market",
        "contato@", "emailmarket", "relacionamento@",
    ]
    if any(x in s for x in marketing_senders):
        return "Marketing"

    return None


# ── Helpers ────────────────────────────────────────────────────────────────────

def load_labels(service):
    result = service.users().labels().list(userId="me").execute()
    return {l["name"]: l["id"] for l in result.get("labels", [])}

def ensure_labels(service):
    existing = load_labels(service)
    label_map = dict(existing)
    for name, bg, fg in LABELS_CONFIG:
        if name not in existing:
            body = {
                "name": name,
                "labelListVisibility": "labelShow",
                "messageListVisibility": "show",
                "color": {"backgroundColor": bg, "textColor": fg},
            }
            result = service.users().labels().create(userId="me", body=body).execute()
            label_map[name] = result["id"]
            print(f"  ✅ Criado: {name}")
        else:
            print(f"  ⏭  Existe: {name}")
    return label_map

def apply_label(service, thread_id, label_id):
    try:
        service.users().threads().modify(
            userId="me", id=thread_id,
            body={"addLabelIds": [label_id]}
        ).execute()
        return True
    except Exception as e:
        print(f"  ⚠️  Erro ao aplicar label em {thread_id}: {e}")
        return False


# ── Scan histórico (todos os emails sem label) ─────────────────────────────────

def scan_history(service, label_map):
    print("\n📬 Escaneando histórico completo (emails sem marcador)...")
    total_applied = 0
    total_skipped = 0
    page_token    = None
    page_num      = 0

    while True:
        page_num += 1
        kwargs = dict(userId="me", q="has:nouserlabels -in:spam -in:trash",
                      maxResults=100)
        if page_token:
            kwargs["pageToken"] = page_token

        result   = service.users().threads().list(**kwargs).execute()
        threads  = result.get("threads", [])
        page_token = result.get("nextPageToken")

        if not threads:
            break

        print(f"  Página {page_num}: {len(threads)} threads...", end=" ", flush=True)
        batch_applied = 0

        for t in threads:
            try:
                detail  = service.users().threads().get(
                    userId="me", id=t["id"], format="metadata",
                    metadataHeaders=["From", "Subject"]
                ).execute()
                msg     = detail["messages"][0]
                headers = {h["name"]: h["value"]
                           for h in msg.get("payload", {}).get("headers", [])}
                sender  = headers.get("From", "")
                subject = headers.get("Subject", "")

                category = classify(sender, subject)
                if category and category in label_map:
                    if apply_label(service, t["id"], label_map[category]):
                        batch_applied += 1
                        total_applied += 1
                else:
                    total_skipped += 1

                time.sleep(0.05)  # respeita rate limit da API

            except Exception as e:
                total_skipped += 1

        print(f"{batch_applied} classificados.")

        if not page_token:
            break

        time.sleep(0.5)

    print(f"\n  ✅ Histórico: {total_applied} classificados | {total_skipped} sem categoria")
    return total_applied


# ── Filtros automáticos para novos emails ─────────────────────────────────────

FILTER_RULES = [
    ("Segundo Cérebro",      {"subject": "Segundo Cérebro"}),
    ("Dev & Ferramentas",    {"from": "(github.com OR anthropic.com OR openai.com OR n8n.io OR email.claude.com)"}),
    ("Google",               {"from": "(google.com OR onedrive.com)"}),
    ("Financeiro/Recibos",   {"from": "mail.anthropic.com"}),
    ("Financeiro/Cartões",   {"from": "(nubank.com.br OR bradesco OR itau.com.br OR santander OR c6bank OR inter.co OR picpay)"}),
    ("Financeiro/Cobranças", {"from": "(acordocerto OR queroquitar OR serasa OR scpc OR cobranca)"}),
    ("Financeiro/Cobranças", {"subject": "(débito OR pendência OR quitação OR negativado)"}),
    ("Compras & Lojas",      {"from": "(shein.com OR temuemail.com OR shopee OR mercadolivre OR americanas OR amazon)"}),
    ("Eventos",              {"subject": "Convite de remetente"}),
    ("Redes Sociais",        {"from": "(instagram.com OR facebookmail.com OR linkedin.com OR twitter.com OR tiktok.com)"}),
    ("Newsletters",          {"from": "(ted.com OR empiricus.com.br OR comunicacao-exame.com)"}),
]

def create_filters(service, label_map):
    print("\n⚙️  Criando filtros automáticos para novos emails...")

    # Lista filtros existentes para não duplicar
    existing = service.users().settings().filters().list(userId="me").execute()
    existing_criteria = [
        (f.get("criteria", {}).get("from", "") + f.get("criteria", {}).get("subject", ""))
        for f in existing.get("filter", [])
    ]

    created = 0
    for label_name, criteria in FILTER_RULES:
        if label_name not in label_map:
            continue

        # Verifica duplicata simples
        key = criteria.get("from", "") + criteria.get("subject", "")
        if key in existing_criteria:
            print(f"  ⏭  Já existe: {label_name} ({key[:40]})")
            continue

        body = {
            "criteria": criteria,
            "action":   {"addLabelIds": [label_map[label_name]]},
        }
        try:
            service.users().settings().filters().create(userId="me", body=body).execute()
            print(f"  ✅ Filtro: {label_name} ← {key[:50]}")
            created += 1
        except Exception as e:
            print(f"  ⚠️  Erro ao criar filtro {label_name}: {e}")

    print(f"\n  ✅ {created} filtros criados — novos emails serão classificados automaticamente.")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--filters-only",  action="store_true")
    parser.add_argument("--history-only",  action="store_true")
    args = parser.parse_args()

    service = get_service()

    print("\n🏷  Verificando marcadores...")
    label_map = ensure_labels(service)
    label_map.update(load_labels(service))  # inclui CURSOS, TELEFONE, Notes etc.

    if not args.filters_only:
        scan_history(service, label_map)

    if not args.history_only:
        create_filters(service, label_map)

    print("\n✅ Tudo pronto.")

if __name__ == "__main__":
    main()
