#!/usr/bin/env python3
"""Re-authenticate Google Calendar OAuth v2 - with local server."""
import json, sys, urllib.request, urllib.parse, socketserver, http.server, threading, time
from pathlib import Path
from urllib.parse import urlparse, parse_qs

SECRETS_DIR = Path(__file__).parent.parent / ".secrets"
TOKEN_FILE = SECRETS_DIR / "google-calendar-token.json"
CREDS_FILE = SECRETS_DIR / "google-calendar-credentials.json"

creds = json.loads(CREDS_FILE.read_text())
client_id = creds["installed"]["client_id"]
client_secret = creds["installed"]["client_secret"]

auth_code = None
server = None

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urlparse(self.path)
        qs = parse_qs(parsed.query)
        auth_code = qs.get("code", [None])[0]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if auth_code:
            self.wfile.write(b"<html><body><h1>Auth OK</h1></body></html>")
        else:
            self.wfile.write(b"<html><body><h1>No code</h1></body></html>")
        threading.Thread(target=server.shutdown).start()
    def log_message(self, format, *args):
        pass

def get_free_port():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    port = s.getsockname()[1]
    s.close()
    return port

port = get_free_port()
redirect_uri = f"http://localhost:{port}"

params = {
    "client_id": client_id,
    "redirect_uri": redirect_uri,
    "response_type": "code",
    "scope": "https://www.googleapis.com/auth/calendar",
    "access_type": "offline",
    "prompt": "consent",
}
auth_url = "https://accounts.google.com/o/oauth2/auth?" + urllib.parse.urlencode(params)

print("REAUTH GOOGLE CALENDAR")
print("=" * 50)
print()
print(f"Port: {port}")
print(f"Redirect: {redirect_uri}")
print()
print("OPEN THIS URL IN THE BROWSER:")
print(auth_url)
print()

server = http.server.HTTPServer(("localhost", port), Handler)
print(f"Listening on http://localhost:{port} ...")

server_thread = threading.Thread(target=server.serve_forever)
server_thread.daemon = True
server_thread.start()

timeout = 120
start = time.time()
while auth_code is None and time.time() - start < timeout:
    time.sleep(0.5)

if not auth_code:
    print("Timeout - no code received")
    sys.exit(1)

print("Code received, exchanging for token...")

try:
    token_data = urllib.parse.urlencode({
        "code": auth_code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }).encode()

    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=token_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    resp = urllib.request.urlopen(req)
    token_response = json.loads(resp.read())

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
    print(f"Token saved to {TOKEN_FILE}")
    print("Reauthentication complete!")

except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.read().decode()}")
except Exception as e:
    print(f"Error: {e}")