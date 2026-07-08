#!/usr/bin/env python3
"""
Autenticação inicial com Google Calendar API.
Roda UMA VEZ para gerar o token de acesso offline.
Resultado salvo em scripts/.secrets/google-calendar-token.json
"""

import os
import json
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
SECRETS_DIR = SCRIPT_DIR.parent / ".secrets"
CREDENTIALS_FILE = SECRETS_DIR / "google-calendar-credentials.json"
TOKEN_FILE = SECRETS_DIR / "google-calendar-token.json"

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def main():
    from google_auth_oauthlib.flow import InstalledAppFlow

    if not CREDENTIALS_FILE.exists():
        print(f"❌ Credenciais não encontradas em: {CREDENTIALS_FILE}")
        return

    print("Abrindo navegador para autenticação com o Google...")
    print("(Faça login com davijadielson@gmail.com)\n")

    flow = InstalledAppFlow.from_client_secrets_file(
        str(CREDENTIALS_FILE), SCOPES
    )
    creds = flow.run_local_server(port=0, open_browser=True)

    TOKEN_FILE.write_text(creds.to_json())
    print(f"\n✅ Token salvo em: {TOKEN_FILE}")
    print("Autenticação concluída. Pode fechar esta janela.")

if __name__ == "__main__":
    main()
