#!/usr/bin/env python3
import json, os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.metadata.readonly']
TOKEN_FILE = '/data/.openclaw/workspace/scripts/.secrets/google-sheets-token.json'
SPREADSHEET_ID = '1HS9w4c04l2tUlggaztNPQuk-2BYIDmaTHTI7Df0QCGs'

def get_creds():
    with open(TOKEN_FILE) as f:
        data = json.load(f)
    # O arquivo local foi salvo com expiry em formato com espaço; construir diretamente evita erro de parse.
    creds = Credentials(
        token=data.get('token'),
        refresh_token=data.get('refresh_token'),
        token_uri=data.get('token_uri'),
        client_id=data.get('client_id'),
        client_secret=data.get('client_secret'),
        scopes=SCOPES,
    )
    # Força refresh para garantir token válido.
    if creds and creds.refresh_token:
        creds.refresh(Request())
        data.update({
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'token_uri': creds.token_uri,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret,
            'scopes': list(creds.scopes) if creds.scopes else [],
            'expiry': str(creds.expiry),
        })
        with open(TOKEN_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    return creds

creds = get_creds()
service = build('sheets', 'v4', credentials=creds)
row = [[
    '2026-07-18',
    'TRANSPORTE',
    'Manutenção veículo / pneu',
    'Conserto de pneu do carro',
    30.00,
    'DESPESA VARIÁVEL',
    'Pessoal',
    'Não informado',
    'PAGO',
    '2026-07',
    'Informado por Jadielson no Telegram/My Finance em 2026-07-18: "gastei mais R$ 30,00 com conserto de pneu do carro". Manter separado de LÓGIKA/empresa.'
]]
res = service.spreadsheets().values().append(
    spreadsheetId=SPREADSHEET_ID,
    range="'Lançamentos'!A:K",
    valueInputOption='USER_ENTERED',
    insertDataOption='INSERT_ROWS',
    body={'values': row}
).execute()
print(res.get('updates', {}))
