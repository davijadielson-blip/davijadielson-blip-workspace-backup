#!/bin/bash
# daily-brief.sh — Roda todo dia às 7h (via launchd)
# Gera briefing em [F2] memory/sessions/daily-briefs/YYYY-MM-DD.md e envia via Telegram + Email

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
DATE=$(date +%Y-%m-%d)
WEEKDAY=$(date +%u)  # 1=seg ... 7=dom
OUTPUT_DIR="$VAULT/[F2] memory/sessions/daily-briefs"
mkdir -p "$OUTPUT_DIR"

# Tipo do dia
case "$WEEKDAY" in
  1|3|5) TIPO="🎥 Externo" ;;
  2|4|6) TIPO="🏢 Agência" ;;
  7)     TIPO="🗓️ Descanso / Família" ;;
esac

# Dia da semana em português
WEEKDAY_PT=$(python3 -c "
days=['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo']
import datetime; print(days[datetime.date.today().weekday()])
")

cd "$VAULT"
git pull --rebase origin main 2>/dev/null || true

# 1. Sync Notion → Calendar (para que eventos de hoje estejam atualizados)
python3 "$VAULT/scripts/sync/notion-to-calendar.py" >> /tmp/notion-sync.log 2>&1 || true

# 2. Busca eventos do Google Calendar para hoje
EVENTOS_MD=$(python3 "$VAULT/scripts/lib/get-calendar-events.py" --format md 2>/tmp/gcal.err || echo "*(erro ao buscar agenda)*")
EVENTOS_HTML=$(python3 "$VAULT/scripts/lib/get-calendar-events.py" --format html 2>/dev/null || echo "  <i>⚠️ Erro ao buscar agenda</i>")

# 3. Lê pendências do vault
CRITICAS=$(awk '/## 🔴 Críticas/,/## 🟡/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null \
  | grep "^\- \[ \]" | sed 's/^- \[ \] //' | head -5 || true)

IMPORTANTES=$(awk '/## 🟡 Importantes/,/## 🟢/' "$VAULT/[F2] memory/context/pendencias.md" 2>/dev/null \
  | grep "^\- \[ \]" | sed 's/^- \[ \] //' | head -3 || true)

# 4. Deadlines (linhas da tabela markdown)
DEADLINES=$(awk '/## 📅 Próximos/,/## 🗓️/' "$VAULT/[F2] memory/context/deadlines.md" 2>/dev/null \
  | grep "^|" | grep -v "^| Data" | grep -v "^|---|" | head -5 || true)

# 5. Projetos em andamento (PROJETOS/EM ANDAMENTO/)
EM_ANDAMENTO_MD=""
EM_ANDAMENTO_HTML=""
EM_ANDAMENTO_DIR="$VAULT/PROJETOS/EM ANDAMENTO"
if [ -d "$EM_ANDAMENTO_DIR" ]; then
  for f in "$EM_ANDAMENTO_DIR"/*.md; do
    [ -f "$f" ] || continue
    NOME=$(basename "$f" .md)
    FRENTE=$(grep "^frente:" "$f" 2>/dev/null | sed 's/frente:[[:space:]]*//' | head -1)
    FASE=$(grep "^fase-atual:" "$f" 2>/dev/null | sed 's/fase-atual:[[:space:]]*//' | head -1)
    EM_ANDAMENTO_MD+="- 🚀 **${NOME}** · ${FRENTE} · ${FASE}"$'\n'
    EM_ANDAMENTO_HTML+="  🚀 <b>${NOME}</b> · <i>${FRENTE}</i> · ${FASE}\n"
  done
fi
EM_ANDAMENTO_MD="${EM_ANDAMENTO_MD:-*(nenhum em andamento)*}"
EM_ANDAMENTO_HTML="${EM_ANDAMENTO_HTML:-  <i>nenhum em andamento — mova um projeto no COCKPIT</i>}"

# 5b. Estudos em andamento (ESTUDOS/EM ANDAMENTO/)
ESTUDOS_MD=""
ESTUDOS_HTML=""
ESTUDOS_DIR="$VAULT/ESTUDOS/EM ANDAMENTO"
if [ -d "$ESTUDOS_DIR" ]; then
  for f in "$ESTUDOS_DIR"/*.md; do
    [ -f "$f" ] || continue
    NOME=$(basename "$f" .md)
    SUBTIPO=$(grep "^subtipo:" "$f" 2>/dev/null | sed 's/subtipo:[[:space:]]*//' | head -1) || true
    AULAS_C=$(grep "^aulas-concluidas:" "$f" 2>/dev/null | sed 's/aulas-concluidas:[[:space:]]*//' | head -1) || true
    TOTAL_A=$(grep "^total-aulas:" "$f" 2>/dev/null | sed 's/total-aulas:[[:space:]]*//' | head -1) || true
    PROG=""
    if [ -n "$TOTAL_A" ] && [ "$TOTAL_A" -gt 0 ] 2>/dev/null; then
      PROG=" · ${AULAS_C:-0}/${TOTAL_A} aulas"
    fi
    ESTUDOS_MD+="- 📚 **${NOME}**${PROG}"$'\n'
    ESTUDOS_HTML+="  📚 <b>${NOME}</b><i>${PROG}</i>\n"
  done
fi
ESTUDOS_MD="${ESTUDOS_MD:-*(nenhum em andamento)*}"
ESTUDOS_HTML="${ESTUDOS_HTML:-  <i>nenhum em andamento</i>}"

# 6. Datas sazonais (próximos 4 dias)
SAZONAIS=""
for i in 0 1 2 3; do
  CHECK=$(date -v+${i}d +%Y-%m-%d 2>/dev/null || date -d "+${i} days" +%Y-%m-%d 2>/dev/null)
  while IFS= read -r f; do
    [ -z "$f" ] && continue
    DESC=$(grep "^descricao:" "$f" | sed 's/descricao: //')
    FRENTE=$(grep "^frente:" "$f" | sed 's/frente: //')
    SAZONAIS+="- $CHECK — $DESC ($FRENTE)"$'\n'
  done < <(grep -rl "^data: ${CHECK}" "$VAULT/[F2] memory/databases/datas-sazonais/" 2>/dev/null || true)
done

# ── Gera nota no vault ─────────────────────────────────────────────────────────

OUTPUT_FILE="$OUTPUT_DIR/$DATE.md"

{
cat <<HEADER
---
tipo: daily-brief
data: $DATE
gerado-por: cron-daily-brief
revisado: false
---

# Daily Brief — ${WEEKDAY_PT}, $(date '+%d/%m/%Y') — ${TIPO}

## 🚀 Projetos em andamento
$EM_ANDAMENTO_MD

## 📚 Estudos em andamento
$ESTUDOS_MD

## 🗓 Agenda de hoje (Google Calendar)
$EVENTOS_MD

## 🔴 Pendências críticas
${CRITICAS:-*(nenhuma)*}

## 🟡 Pendências importantes
${IMPORTANTES:-*(nenhuma)*}

## 📅 Deadlines próximos
${DEADLINES:-*(nenhum)*}

## 🗓️ Datas sazonais (próximos 4 dias)
${SAZONAIS:-*(nenhuma)*}
## 🎯 Foco do dia
*[a preencher por Jadielson]*

## ✅ Top 3 de hoje
- [ ]
- [ ]
- [ ]

---
*Gerado automaticamente em $(date '+%d/%m/%Y às %H:%M') por cron-daily-brief*
HEADER
} > "$OUTPUT_FILE"

# Gera cockpit.html antes de enviar notificações
bash "$VAULT/scripts/cockpit/generate-cockpit.sh" >> /tmp/cockpit.log 2>&1 || true

git add "$OUTPUT_FILE" "$VAULT/cockpit.html" 2>/dev/null || true
git commit -m "cron: daily-brief $DATE" --allow-empty 2>/dev/null || true
git push origin main 2>/dev/null || true

# ── Monta mensagem Telegram (HTML) ─────────────────────────────────────────────

build_bullets_html() {
  local input="$1" prefix="${2:-  • }" empty_msg="${3:-<i>nenhum</i>}"
  local result=""
  while IFS= read -r line; do
    [[ -z "$line" ]] && continue
    result+="${prefix}${line}\n"
  done <<< "$input"
  echo -e "${result:-  ${empty_msg}}"
}

# Deadlines: converte linhas de tabela markdown → bullets HTML
DEADLINES_BULLETS=""
while IFS='|' read -r _ data evento frente _rest; do
  data=$(echo "$data" | xargs 2>/dev/null)
  evento=$(echo "$evento" | xargs 2>/dev/null)
  frente=$(echo "$frente" | xargs 2>/dev/null)
  [[ -z "$data" ]] && continue
  DEADLINES_BULLETS+="  • ${data} — ${evento} <i>(${frente})</i>\n"
done <<< "$DEADLINES"
DEADLINES_BULLETS="${DEADLINES_BULLETS:-  <i>nenhum nos próximos dias</i>}"

CRITICAS_BULLETS=$(build_bullets_html "$CRITICAS" "  🔴 " "<i>nenhuma</i>")
IMPORTANTES_BULLETS=$(build_bullets_html "$IMPORTANTES" "  • " "<i>nenhuma</i>")
SAZONAIS_BULLETS=$(build_bullets_html "$(echo "$SAZONAIS" | sed 's/^- //')" "  • " "<i>nenhuma nos próximos 4 dias</i>")

# Bloco atual (Inversão Biológica) — determinado pelo horário de execução
HORA_ATUAL=$(date +%H%M)
if   [ "$HORA_ATUAL" -lt 0740 ]; then BLOCO_ATUAL="🌅 Despertar"
elif [ "$HORA_ATUAL" -lt 1130 ]; then BLOCO_ATUAL="🟦 Elite (pensar · criar · decidir)"
elif [ "$HORA_ATUAL" -lt 1300 ]; then BLOCO_ATUAL="🍽️ Almoço"
elif [ "$HORA_ATUAL" -lt 1800 ]; then BLOCO_ATUAL="🟥 Tático (mover · captar · editar)"
elif [ "$HORA_ATUAL" -lt 2100 ]; then BLOCO_ATUAL="🌙 Ancoragem (família · descanso)"
else                                   BLOCO_ATUAL="😴 Sono"; fi

# Semana do plano 30 dias (calculado a partir de 2026-05-16)
INICIO_PLANO="2026-05-16"
DIAS_PLANO=$(python3 -c "
from datetime import date
inicio = date(2026,5,16)
hoje = date.today()
diff = (hoje - inicio).days
if diff < 7: print('1 — Raio-X · despertar 06h')
elif diff < 14: print('2 — Padronização · despertar 05h30')
elif diff < 21: print('3 — Delegação · despertar 05h')
elif diff < 30: print('4 — Consolidar · despertar 04h30')
else: print('Manutenção (pós-30 dias)')
" 2>/dev/null || echo "ver plano-30-dias-diretor")

TG_MSG="📅 <b>${WEEKDAY_PT}, $(date '+%d/%m/%Y')</b> · ${TIPO}

<b>🕐 Bloco atual:</b> ${BLOCO_ATUAL}
<b>📊 Plano 30d — Semana:</b> ${DIAS_PLANO}
<b>💼 Teto SMS esta semana:</b> — / 15h · ver <a href='https://www.notion.so/e6d0b774ebe04761a61b1a30e16db091'>Cockpit Diretor</a>

<b>🚀 Projetos em andamento</b>
$(echo -e "$EM_ANDAMENTO_HTML")
<b>📚 Estudos em andamento</b>
$(echo -e "$ESTUDOS_HTML")
<b>🗓 Agenda de hoje</b>
${EVENTOS_HTML}

<b>🔴 Pendências críticas</b>
${CRITICAS_BULLETS}
<b>🟡 Pendências importantes</b>
${IMPORTANTES_BULLETS}
<b>📌 Deadlines próximos</b>
$(echo -e "$DEADLINES_BULLETS")
<b>🌟 Datas sazonais</b>
${SAZONAIS_BULLETS}
<i>Bom dia, Jadielson! 💪</i>"

"$VAULT/scripts/lib/send-telegram.sh" "$TG_MSG" "HTML" || true

"$VAULT/scripts/lib/send-email.sh" \
  "[Segundo Cérebro] Daily Brief — $(date '+%d/%m/%Y')" \
  "$(cat "$OUTPUT_FILE")" 2>/dev/null || true
