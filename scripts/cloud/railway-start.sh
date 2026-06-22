#!/usr/bin/env bash
# railway-start.sh — Startup do bot Telegram no Railway.
# Reconstrói secrets a partir de variáveis de ambiente, sincroniza vault e inicia o daemon.
set -eo pipefail

VAULT="/app"
SECRETS_DIR="$VAULT/scripts/.secrets"
mkdir -p "$SECRETS_DIR"

echo "[startup] === DEBUG VARIAVEIS ==="
echo "TOKEN_LEN=${#TELEGRAM_BOT_TOKEN}"
echo "CHAT_LEN=${#TELEGRAM_CHAT_ID}"
echo "ANTHROPIC_LEN=${#ANTHROPIC_API_KEY}"
echo "GITHUB_LEN=${#GITHUB_TOKEN}"
echo "[startup] === FIM DEBUG ==="

if [ "${#TELEGRAM_BOT_TOKEN}" -eq 0 ]; then echo "[ERRO] TELEGRAM_BOT_TOKEN vazia"; exit 1; fi
if [ "${#TELEGRAM_CHAT_ID}" -eq 0 ];   then echo "[ERRO] TELEGRAM_CHAT_ID vazia";   exit 1; fi
if [ "${#ANTHROPIC_API_KEY}" -eq 0 ];  then echo "[ERRO] ANTHROPIC_API_KEY vazia";  exit 1; fi
if [ "${#GITHUB_TOKEN}" -eq 0 ];       then echo "[ERRO] GITHUB_TOKEN vazia";       exit 1; fi
echo "[startup] Todas as variaveis OK."

echo "[startup] Reconstruindo secrets..."
cat > "$SECRETS_DIR/telegram.env" << EOF
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
TELEGRAM_CHAT_ID=${TELEGRAM_CHAT_ID}
EOF

cat > "$SECRETS_DIR/anthropic.env" << EOF
ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
EOF

echo "[startup] Configurando git..."
git config --global user.email "bot@segundo-cerebro"
git config --global user.name "Segundo Cérebro Bot"
git remote set-url origin "https://${GITHUB_TOKEN}@github.com/davijadielson-blip/segundo-cerebro-jadielson.git"

echo "[startup] Sincronizando vault com GitHub..."
git pull origin main --rebase 2>/dev/null || echo "[aviso] git pull falhou — continuando com versão atual"

echo "[startup] Iniciando daemon de polling..."
export TG_VAULT_PATH="$VAULT"
exec bash "$VAULT/scripts/cron-jobs/telegram-polling.sh"
