#!/bin/bash
# friday-maintenance.sh — Roda toda sexta às 18h (via launchd)
# Lista drafts velhos, gera relatório em [F2] memory/sessions/maintenance/

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="$VAULT/[F2] memory/sessions/maintenance"
mkdir -p "$OUTPUT_DIR"

cd "$VAULT"
git pull --rebase origin main 2>/dev/null || true

# Drafts com revisado: false há mais de 7 dias
VELHOS=""
VELHOS_COUNT=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  MTIME=$(stat -f "%m" "$f" 2>/dev/null || stat -c "%Y" "$f" 2>/dev/null)
  NOW=$(date +%s)
  DIFF=$(( (NOW - MTIME) / 86400 ))
  if [ "$DIFF" -ge 7 ]; then
    VELHOS+="- $(basename "$f") (${DIFF}d sem revisão)\n"
    VELHOS_COUNT=$((VELHOS_COUNT + 1))
  fi
done < <(grep -rl "^revisado: false" "$VAULT/[F2] memory/outputs/" 2>/dev/null | grep "\.md$" || true)

# Notas no Inbox
INBOX_COUNT=$(find "$VAULT/[F0] 0-Inbox" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')

# Sessões da semana
SESSOES=$(ls "$VAULT/[F2] memory/sessions/"*.md 2>/dev/null | xargs -I{} basename {} | sort -r | head -5 | tr '\n' ', ' | sed 's/,$//')

OUTPUT_FILE="$OUTPUT_DIR/$DATE.md"

cat > "$OUTPUT_FILE" <<EOF
---
tipo: maintenance-report
data: $DATE
gerado-por: cron-friday-maintenance
revisado: false
---

# Relatório de Manutenção — $DATE

## 📋 Drafts aguardando revisão há +7 dias ($VELHOS_COUNT)
$(echo -e "${VELHOS:-*(nenhum)*}")

## 📥 Inbox pendente
$INBOX_COUNT nota(s) em \`[F0] 0-Inbox/\` aguardando processamento.

## 📓 Sessões desta semana
$SESSOES

## ✅ Checklist de manutenção
- [ ] Revisar ou arquivar drafts velhos acima
- [ ] Processar inbox (mover para destino correto)
- [ ] Atualizar \`[F2] memory/context/pendencias.md\` — marcar o que foi resolvido
- [ ] Atualizar \`[F2] memory/context/deadlines.md\` — remover datas passadas
- [ ] Commitar e fazer push: \`git add . && git commit -m "chore: manutenção $DATE" && git push\`

---
*Gerado automaticamente em $(date '+%d/%m/%Y às %H:%M') por cron-friday-maintenance*
EOF

git add "$OUTPUT_FILE" 2>/dev/null || true
git commit -m "cron: friday-maintenance $DATE" --allow-empty 2>/dev/null || true
git push origin main 2>/dev/null || true

# Notificações — Telegram (primário) + Email (backup)
SUMMARY=$(head -35 "$OUTPUT_FILE")

"$VAULT/scripts/lib/send-telegram.sh" "*Manutenção do Vault* — $DATE

$SUMMARY

_Relatório completo no vault: [F2] memory/sessions/maintenance/${DATE}.md_" || true

"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Manutenção do Vault — $DATE" \
  "$(cat "$OUTPUT_FILE")" 2>/dev/null || true
