#!/usr/bin/env python3
"""Re-authenticate Google Calendar OAuth for sync script."""
import json
import sys
from pathlib import Path
from urllib.parse import urlencode, parse_qs, urlparse

SECRETS_DIR = Path(__file__).parent.parent / ".secrets"
TOKEN_FILE = SECRETS_DIR / "google-calendar-token.json"
CREDS_FILE = SECRETS_DIR / "google-calendar-credentials.json"

creds = json.loads(CREDS_FILE.read_text())
client_id = creds["installed"]["client_id"]
client_secret = creds["installed"]["client_secret"]
redirect_uri = creds["installed"]["redirect_uris"][0]

params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": "https://www.googleapis.com/auth/calendar",
    "access_type": "offline",
    "prompt": "consent",
}
auth_url = "https://accounts.google.com/o/oauth2/auth?" + urlencode(params)

print("=" * 70)
print("🔑 REAUTH GOOGLE CALENDAR — SYNC NOTION→CALENDAR")
print("=" * 70)
print()
print("1️⃣  Abra este link no seu navegador:")
print()
print(auth_url)
print()
print("2️⃣  Faça login com: loh.open.logika@gmail.com")
print()
print("3️⃣  Autorize o acesso")
print("    (Se aparecer 'App not verified', clique em Advanced → Go to project)")
print()
print("4️⃣  O navegador vai tentar abrir http://localhost/?code=...")
print("    Como não tem servidor local, a página vai dar erro.")
print("    Copie a URL COMPLETA da barra de endereço (começa com http://localhost/?code=...)")
print("    e cole aqui.")
print()
print("5️⃣  Digite a URL completa ou apenas o code:")
print("    (ou 'q' para sair)")
print()

# Read from stdin or argument
if len(sys.argv) > 1:
    input_url = sys.argv[1]
else:
    try:
        input_url = input("➡️  ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nSaindo...")
        sys.exit(1)

if input_url.lower() in ("q", "quit", "exit", ""):
    print("Cancelado.")
    sys.exit(0)

# Extract code from URL or direct code
parsed = urlparse(input_url)
code = parse_qs(parsed.query).get("code", [None])[0]
if not code:
    code = input_url  # assume it's the code itself

if not code:
    print("❌ Não foi possível extrair o code. Verifique a URL.")
    sys.exit(1)

print(f"\n✅ Code extraído: {code[:30]}...")
print("\n🔄 Trocando code por token...")

# Exchange code for token
import urllib.request
import urllib.error

token_data = urllib.parse.urlencode({
    "code": code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
}).encode()

try:
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=token_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    resp = urllib.request.urlopen(req)
    token_response = json.loads(resp.read())

    # Save full token
    token_json = {
        "token": token_response["access_token"],
        "refresh_token": token_response.get("refresh_token", ""),
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": client_id,
        "client_secret": client_secret,
        "scopes": ["https://www.googleapis.com/auth/calendar"],
        "expiry": token_response.get("expires_in", 3600),
    }
    TOKEN_FILE.write_text(json.dumps(token_json, indent=2))
    print("✅ Token salvo em:", TOKEN_FILE)
    print()
    print("🎉 Reautenticação concluída! Agora o sync deve funcionar.")
    print("Execute: python3 scripts/sync/notion-to-calendar.py")

except urllib.error.HTTPError as e:
    print(f"❌ Erro HTTP {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"❌ Erro: {e}")
