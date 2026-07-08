#!/bin/bash
# Envia mensagem pro Telegram do Jadielson
# Uso: ./send-telegram.sh "Sua mensagem aqui" [parse_mode]
# parse_mode: HTML (padrão) | Markdown | "" (texto simples)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/../.secrets/telegram.env"

MESSAGE="$1"
PARSE_MODE="${2:-HTML}"
[ -z "$MESSAGE" ] && exit 1

MAX_LEN=4000
if [ ${#MESSAGE} -gt $MAX_LEN ]; then
  MESSAGE="${MESSAGE:0:$MAX_LEN}...[truncado]"
fi

CURL_ARGS=(
  -s -X POST
  "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage"
  -d "chat_id=${TELEGRAM_CHAT_ID}"
  --data-urlencode "text=${MESSAGE}"
)
[ -n "$PARSE_MODE" ] && CURL_ARGS+=(-d "parse_mode=${PARSE_MODE}")

curl "${CURL_ARGS[@]}" > /dev/null
