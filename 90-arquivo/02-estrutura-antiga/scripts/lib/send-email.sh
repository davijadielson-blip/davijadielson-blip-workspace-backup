#!/bin/bash
# Envia email via Gmail SMTP
# Uso: ./send-email.sh "Assunto" "Corpo da mensagem"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/../.secrets/email.env"

SUBJECT="$1"
BODY="$2"

[ -z "$SUBJECT" ] || [ -z "$BODY" ] && { echo "Uso: $0 'assunto' 'corpo'"; exit 1; }

python3 - <<PYEOF
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

gmail_user = "${GMAIL_USER}"
gmail_pass = "${GMAIL_APP_PASSWORD}"
email_to   = "${EMAIL_TO}"
subject    = """${SUBJECT}"""
body       = """${BODY}"""

msg = MIMEMultipart()
msg['From']    = gmail_user
msg['To']      = email_to
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain', 'utf-8'))

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_pass)
    server.send_message(msg)
    server.quit()
    print("✓ Email enviado")
except Exception as e:
    print(f"✗ Erro: {e}", file=sys.stderr)
    sys.exit(1)
PYEOF
