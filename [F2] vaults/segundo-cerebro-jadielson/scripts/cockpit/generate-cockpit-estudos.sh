#!/bin/bash
# generate-cockpit-estudos.sh — Gera cockpit-estudos.html na raiz do vault
# Pode ser chamado manualmente ou pelo daily-brief.sh
# Output: $VAULT/cockpit-estudos.html

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"

echo "[cockpit-estudos] Varrendo [F1] 2-Literatura/..."
python3 "$VAULT/scripts/cockpit/estudos-generator.py"

if [ -t 1 ]; then
  if command -v open &>/dev/null; then
    open "$VAULT/cockpit-estudos.html"
  elif command -v xdg-open &>/dev/null; then
    xdg-open "$VAULT/cockpit-estudos.html"
  fi
fi
