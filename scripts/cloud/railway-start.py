#!/usr/bin/env python3
"""Startup do bot Telegram no Railway — lê env vars via os.environ (mais confiável que bash)."""
import os
import sys
import subprocess
import pathlib

VAULT = pathlib.Path("/app")
SECRETS = VAULT / "scripts" / ".secrets"
SECRETS.mkdir(parents=True, exist_ok=True)

def require(name):
    val = os.environ.get(name, "").strip()
    print(f"[startup] {name}: len={len(val)}", flush=True)
    if not val:
        print(f"[ERRO] {name} não definida. Abortando.", flush=True)
        sys.exit(1)
    return val

import base64

print("[startup] Lendo variáveis de ambiente...", flush=True)
TG_TOKEN   = require("TELEGRAM_BOT_TOKEN")
TG_CHAT    = require("TELEGRAM_CHAT_ID")
ANTHROPIC  = require("ANTHROPIC_API_KEY")
GH_TOKEN   = require("GITHUB_TOKEN")
print("[startup] Todas as variáveis OK.", flush=True)

(SECRETS / "telegram.env").write_text(
    f'TELEGRAM_BOT_TOKEN={TG_TOKEN}\nTELEGRAM_CHAT_ID={TG_CHAT}\n'
)
(SECRETS / "anthropic.env").write_text(f'ANTHROPIC_API_KEY={ANTHROPIC}\n')

NOTION_TOKEN = os.environ.get("NOTION_TOKEN", "").strip()
(SECRETS / "notion.env").write_text(
    f'NOTION_TOKEN={NOTION_TOKEN}\n'
    f'NOTION_CAPTURA_DATABASE_ID=242f2506a972451d80209bd593bdb006\n'
    f'NOTION_HUB_PAGE_ID=35d207e6-f145-81b0-817b-c7d0d3475743\n'
    f'NOTION_EDITORIAL_SAUDE_ID=1d8207e6-f145-8153-99c1-f5ae2b4e4e23\n'
    f'NOTION_EDITORIAL_CAMARA_ID=52a83dbb-9d10-40b6-87c3-687013d92138\n'
    f'NOTION_EDITORIAL_SINDSS_ID=5ca1a34c-342b-406a-8c71-4b8b63e0a1f5\n'
)

GCT_B64 = os.environ.get("GOOGLE_CALENDAR_TOKEN_B64", "").strip()
if GCT_B64:
    try:
        (SECRETS / "google-calendar-token.json").write_bytes(base64.b64decode(GCT_B64))
        print("[startup] google-calendar-token.json reconstruído.", flush=True)
    except Exception as e:
        print(f"[aviso] Falha ao reconstruir token Calendar: {e}", flush=True)
else:
    print("[aviso] GOOGLE_CALENDAR_TOKEN_B64 não definida — /agendar indisponível no Railway.", flush=True)

print("[startup] Secrets reconstruídos.", flush=True)

subprocess.run(["git", "config", "--global", "user.email", "bot@segundo-cerebro"], check=False)
subprocess.run(["git", "config", "--global", "user.name", "Segundo Cérebro Bot"], check=False)
subprocess.run(["git", "remote", "set-url", "origin",
                f"https://{GH_TOKEN}@github.com/davijadielson-blip/segundo-cerebro-jadielson.git"],
               check=False)

print("[startup] Sincronizando vault...", flush=True)
subprocess.run(["git", "pull", "origin", "main", "--rebase"], capture_output=True)

print("[startup] Iniciando daemon de polling...", flush=True)
os.environ["TG_VAULT_PATH"] = str(VAULT)
os.execv("/bin/bash", ["bash", str(VAULT / "scripts/cron-jobs/telegram-polling.sh")])
