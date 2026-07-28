#!/bin/bash
# weekly-projects-summary.sh — Resumo semanal de projetos
# Roda toda sexta 18h (antes da ancoragem noturna)
# Saída: Telegram (primário) + Email (backup)

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="$VAULT/[F2] memory/sessions/weekly-projects"
mkdir -p "$OUTPUT_DIR"

cd "$VAULT"
git pull --rebase origin main 2>/dev/null || true

# Gera o resumo via Python
OUTPUT_FILE="$OUTPUT_DIR/$DATE.md"
python3 "$VAULT/scripts/lib/weekly-projects-summary.py" \
    --vault "$VAULT" \
    --output "$OUTPUT_FILE"

# Commit do arquivo gerado
git add "$OUTPUT_FILE" 2>/dev/null || true
git commit -m "cron: weekly-projects-summary $DATE" --allow-empty 2>/dev/null || true
git push origin main 2>/dev/null || true

# Envia via Telegram + Email
MENSAGEM=$(cat "$OUTPUT_FILE" | grep -v "^---" | grep -v "^tipo:" | grep -v "^data:" | grep -v "^gerado-por:")

"$VAULT/scripts/lib/send-telegram.sh" "$MENSAGEM" "HTML" || true

"$VAULT/scripts/lib/send-email.sh" \
    "[Segundo Cérebro] Resumo Semanal de Projetos — $DATE" \
    "$(cat "$OUTPUT_FILE")" 2>/dev/null || true
