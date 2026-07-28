#!/bin/bash
# saturday-planning.sh — Roda todo sábado às 17h (via launchd)
# Gera planejamento semanal em [F2] memory/sessions/weekly/YYYY-Www.md

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
WEEK=$(date +%Y-W%V)
OUTPUT_DIR="$VAULT/[F2] memory/sessions/weekly"
mkdir -p "$OUTPUT_DIR"

cd "$VAULT"
git pull --rebase origin main 2>/dev/null || true

# Pendências
IMPORTANTES=$(awk '/## 🟡 Importantes/,/## ⚪/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null | grep "^\- \[ \]" | head -5 || echo "")
CRITICAS=$(awk '/## 🔴 Críticas/,/## 🟡/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null | grep "^\- \[ \]" | head -3 || echo "")

# Deadlines da semana
DEADLINES=$(awk '/## 📅 Próximos/,/## 🗓️/' "$VAULT/[F2] memory/context/deadlines.md" 2>/dev/null | grep "^|" | grep -v "^| Data" | grep -v "^|---|" | head -7 || echo "")

# Datas sazonais da semana
SAZONAIS=""
for i in 0 1 2 3 4 5 6; do
  CHECK=$(date -v+${i}d +%Y-%m-%d 2>/dev/null || date -d "+${i} days" +%Y-%m-%d 2>/dev/null)
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    DESC=$(grep "^descricao:" "$f" | sed 's/descricao: //')
    FRENTE=$(grep "^frente:" "$f" | sed 's/frente: //')
    SAZONAIS+="- $CHECK — $DESC ($FRENTE)\n"
  done < <(grep -rl "^data: ${CHECK}" "$VAULT/[F2] memory/databases/datas-sazonais/" 2>/dev/null || true)
done

# Aniversariantes da semana
ANIVERSARIANTES=""
for i in 0 1 2 3 4 5 6; do
  CHECK=$(date -v+${i}d +%m-%d 2>/dev/null || date -d "+${i} days" +%m-%d 2>/dev/null)
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    NOME=$(grep "^nome:" "$f" | sed 's/nome: //')
    ANIVERSARIANTES+="- $CHECK — $NOME\n"
  done < <(grep -rl "^data: ${CHECK}" "$VAULT/[F2] memory/databases/aniversariantes/" 2>/dev/null || true)
done

OUTPUT_FILE="$OUTPUT_DIR/$WEEK.md"

cat > "$OUTPUT_FILE" <<EOF
---
tipo: weekly-planning
semana: $WEEK
data: $DATE
gerado-por: cron-saturday-planning
revisado: false
---

# Planejamento Semanal — $WEEK

## 🔴 Pendências críticas em aberto
${CRITICAS:-*(nenhuma)*}

## 🟡 Pendências importantes
${IMPORTANTES:-*(nenhuma)*}

## 📅 Deadlines e datas sazonais da semana
$(echo -e "${SAZONAIS:-*(nenhuma)*}")

${DEADLINES:+**Deadlines:**
$DEADLINES}

## 🎂 Aniversariantes da semana
$(echo -e "${ANIVERSARIANTES:-*(nenhum)*}")

## 🎯 Foco da semana
*[a preencher por Jadielson]*

## 📋 Conteúdo planejado por frente
| Frente | Seg | Ter | Qua | Qui | Sex |
|---|---|---|---|---|---|
| Câmara | ✍️ | — | ✍️ | — | ✍️ |
| SINDSS | ✍️ | — | ✍️ | — | ✍️ |
| Saúde | — | — | ✍️ | — | — |
| Lógika | — | — | — | — | — |

## 💡 Intenção da semana
*[a preencher por Jadielson]*

---

## 📥 Ritual de Fontes Externas (rodar no sábado ou domingo)

> Abra o Claude Code e execute em sequência:

- [ ] \`/inbox\` — e-mails das últimas 24–48h por frente
- [ ] \`/drive-recente\` — arquivos novos ou atualizados no Drive
- [ ] \`/whats-importar\` — exportar e processar grupos do WhatsApp (se houver)
- [ ] \`/prioridades\` — cruzar todas as fontes e montar Top 3 real da semana

> Ver ritual completo: \`[F2] memory/inbox-externa/RITUAL.md\`

---
*Gerado automaticamente em $(date '+%d/%m/%Y às %H:%M') por cron-saturday-planning*
EOF

git add "$OUTPUT_FILE" 2>/dev/null || true
git commit -m "cron: saturday-planning $WEEK" --allow-empty 2>/dev/null || true
git push origin main 2>/dev/null || true

# Notificações — Telegram (primário) + Email (backup)
SUMMARY=$(head -40 "$OUTPUT_FILE")

"$VAULT/scripts/lib/send-telegram.sh" "*Planejamento Semanal* — $WEEK

$SUMMARY

_Relatório completo no vault: [F2] memory/sessions/weekly/${WEEK}.md_" || true

"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Planejamento Semanal — $WEEK" \
  "$(cat "$OUTPUT_FILE")" 2>/dev/null || true
