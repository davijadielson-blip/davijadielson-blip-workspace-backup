#!/bin/bash
# generate-cockpit.sh — Gera cockpit.html na raiz do vault
# Pode ser chamado manualmente ou pelo daily-brief.sh (7h)
# Output: $VAULT/cockpit.html

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"

echo "[cockpit] Gerando cockpit.html..."
python3 "$VAULT/scripts/cockpit/cockpit-generator.py"

# Abre no browser se rodado interativamente (não em cron)
if [ -t 1 ]; then
  if command -v open &>/dev/null; then
    open "$VAULT/cockpit.html"
  elif command -v xdg-open &>/dev/null; then
    xdg-open "$VAULT/cockpit.html"
  fi
fi
