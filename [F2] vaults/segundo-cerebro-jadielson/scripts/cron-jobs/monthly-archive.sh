#!/bin/bash
# monthly-archive.sh — Roda todo dia 1º às 8h (via launchd)
# Arquiva outputs do mês anterior para <frente>/_arquivo/YYYY-MM/

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)

# Mês anterior
PREV_YEAR=$(date -v-1m +%Y 2>/dev/null || date --date="1 month ago" +%Y)
PREV_MONTH=$(date -v-1m +%m 2>/dev/null || date --date="1 month ago" +%m)
PREV_LABEL="${PREV_YEAR}-${PREV_MONTH}"

OUTPUTS="$VAULT/[F2] memory/outputs"
TIPOS="roteiros legendas headlines drafts resumos-whatsapp briefings"
FRENTES="saude-sao-sebastiao camara sindss logika rogerio alem-da-foto vereadores lives-louvor"

cd "$VAULT"
git pull --rebase origin main 2>/dev/null || true

TOTAL=0
RELATORIO=""

for FRENTE in $FRENTES; do
  FRENTE_DIR="$OUTPUTS/$FRENTE"
  [ -d "$FRENTE_DIR" ] || continue

  FRENTE_COUNT=0

  for TIPO in $TIPOS; do
    TIPO_DIR="$FRENTE_DIR/$TIPO"
    [ -d "$TIPO_DIR" ] || continue

    # Arquivos do mês anterior
    while IFS= read -r ARQUIVO; do
      [ -z "$ARQUIVO" ] && continue

      DESTINO="$FRENTE_DIR/_arquivo/$PREV_LABEL/$TIPO"
      mkdir -p "$DESTINO"
      mv "$ARQUIVO" "$DESTINO/"

      NOME=$(basename "$ARQUIVO")
      RELATORIO+="  [$FRENTE/$TIPO] $NOME\n"
      FRENTE_COUNT=$((FRENTE_COUNT + 1))
      TOTAL=$((TOTAL + 1))
    done < <(find "$TIPO_DIR" -maxdepth 1 -name "${PREV_LABEL}-*" -type f 2>/dev/null || true)
  done

  [ "$FRENTE_COUNT" -gt 0 ] && RELATORIO="$FRENTE ($FRENTE_COUNT arquivo(s)):\n$RELATORIO"
done

# Relatório em sessions
OUTPUT_DIR="$VAULT/[F2] memory/sessions"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/archive-$DATE.md"

cat > "$OUTPUT_FILE" <<EOF
---
tipo: archive-report
data: $DATE
mes-arquivado: $PREV_LABEL
total-arquivos: $TOTAL
gerado-por: cron-monthly-archive
---

# Arquivamento Mensal — $PREV_LABEL

**Data de execução:** $DATE
**Total arquivado:** $TOTAL arquivo(s)

## Arquivos movidos

$([ "$TOTAL" -gt 0 ] && echo -e "$RELATORIO" || echo "*(nenhum arquivo encontrado para $PREV_LABEL)*")

## Destino
\`[F2] memory/outputs/<frente>/_arquivo/$PREV_LABEL/<tipo>/\`

---
*Gerado automaticamente às $(date '+%H:%M') por cron-monthly-archive*
EOF

git add "$OUTPUT_FILE" 2>/dev/null || true
git commit -m "cron: monthly-archive $PREV_LABEL ($TOTAL arquivos)" --allow-empty 2>/dev/null || true
git push origin main 2>/dev/null || true

# Notificações
if [ "$TOTAL" -gt 0 ]; then
  MSG="*Arquivamento Mensal Concluído* — $PREV_LABEL

$TOTAL arquivo(s) movidos para \`_arquivo/$PREV_LABEL/\`

$(echo -e "$RELATORIO" | head -20)

_Relatório: [F2] memory/sessions/archive-${DATE}.md_"
else
  MSG="*Arquivamento Mensal* — $PREV_LABEL

Nenhum arquivo encontrado para arquivar."
fi

"$VAULT/scripts/lib/send-telegram.sh" "$MSG" || true
"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Arquivamento Mensal — $PREV_LABEL" \
  "$(cat "$OUTPUT_FILE")" 2>/dev/null || true
