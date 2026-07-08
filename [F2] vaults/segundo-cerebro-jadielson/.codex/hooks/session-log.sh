#!/usr/bin/env bash
# Hook: Stop — Mantém log de atividade incremental em /tmp/
# Arquivo permanente só é criado pelo session-start.sh na próxima abertura

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('session_id','unknown'))" \
  2>/dev/null || echo "unknown")

ACTIVITY_LOG="/tmp/vault-session-${SESSION_ID}-activity.log"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M")

if [ -f "$ACTIVITY_LOG" ]; then
  # Atualiza marcador de última resposta
  TMP=$(grep -v "^Ultima resposta:" "$ACTIVITY_LOG" 2>/dev/null)
  printf "%s\nUltima resposta: %s\n" "$TMP" "$TIMESTAMP" > "$ACTIVITY_LOG"
else
  # Cria log inicial (sessão sem session-start — caso raro)
  printf "## Inicio: %s\n\n### Arquivos criados/modificados\n\nUltima resposta: %s\n" \
    "$TIMESTAMP" "$TIMESTAMP" > "$ACTIVITY_LOG"
fi

exit 0
