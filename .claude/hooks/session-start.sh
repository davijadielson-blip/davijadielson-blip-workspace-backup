#!/usr/bin/env bash
# Hook: UserPromptSubmit — Simula SessionStart
# Roda em todo prompt, mas emite briefing só na primeira mensagem da sessão

VAULT="/Users/servicepro/Library/CloudStorage/OneDrive-Pessoal/Documentos/Obsidian Vault 4/MAPA OBSIDIAN"

INPUT=$(cat)
SESSION_ID=$(echo "$INPUT" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('session_id','unknown'))" \
  2>/dev/null || echo "unknown")

LOCK="/tmp/vault-session-${SESSION_ID}.lock"
ACTIVITY_LOG="/tmp/vault-session-${SESSION_ID}-activity.log"

# Não é primeiro prompt desta sessão — silêncio total
[ -f "$LOCK" ] && exit 0

# Marca como iniciada
touch "$LOCK"

# -------------------------------------------------------
# Finaliza log da sessão anterior (se houver)
# -------------------------------------------------------
while IFS= read -r prev_log; do
  PREV_ID=$(basename "$prev_log" | sed 's/vault-session-//' | sed 's/-activity.log//')
  [ "$PREV_ID" = "$SESSION_ID" ] && continue

  LOG_DATE=$(stat -f "%Sm" -t "%Y-%m-%d" "$prev_log" 2>/dev/null || date +"%Y-%m-%d")
  LOG_TIME=$(stat -f "%Sm" -t "%H%M" "$prev_log" 2>/dev/null || date +"%H%M")
  DEST="${VAULT}/memory/logs/sessoes/${LOG_DATE}-${LOG_TIME}.md"

  mkdir -p "${VAULT}/memory/logs/sessoes/" 2>/dev/null
  {
    printf "---\ntipo: log-sessao\ngerado-por: hook-session-log\ndata: %s\nsession_id: %s\n---\n\n" \
      "$LOG_DATE" "$PREV_ID"
    printf "# Log de Sessão — %s\n\n" "$LOG_DATE"
    cat "$prev_log"
  } > "$DEST" 2>/dev/null

  rm -f "$prev_log"
  rm -f "/tmp/vault-session-${PREV_ID}.lock" 2>/dev/null
done < <(find /tmp -maxdepth 1 -name "vault-session-*-activity.log" 2>/dev/null)

# Inicia log desta sessão
{
  printf "## Inicio: %s\n\n### Arquivos criados/modificados\n\n" "$(date '+%Y-%m-%d %H:%M')"
} > "$ACTIVITY_LOG"

# -------------------------------------------------------
# Data e tipo de dia
# -------------------------------------------------------
TODAY=$(date +"%Y-%m-%d")
TODAY_BR=$(date +"%d/%m/%Y")
DOW=$(date +"%u")  # 1=Seg ... 7=Dom

case $DOW in
  1) DAY_PT="Segunda-feira" ; TIPO="🎥 Externo — gravações / atendimentos / clientes" ;;
  2) DAY_PT="Terça-feira"   ; TIPO="🏢 Agência — edição / planejamento / produção" ;;
  3) DAY_PT="Quarta-feira"  ; TIPO="🎥 Externo — gravações / atendimentos / clientes" ;;
  4) DAY_PT="Quinta-feira"  ; TIPO="🏢 Agência — edição / planejamento / produção" ;;
  5) DAY_PT="Sexta-feira"   ; TIPO="🎥 Externo — gravações / atendimentos / clientes" ;;
  6) DAY_PT="Sábado"        ; TIPO="🏢 Agência — edição / planejamento / produção" ;;
  7) DAY_PT="Domingo"       ; TIPO="🗓️ Planejamento / Descanso" ;;
esac

# -------------------------------------------------------
# Coleta de dados do vault
# -------------------------------------------------------
HAS_CONTENT=0
BODY=""

# Drafts com revisado: false
DRAFTS=$(grep -rl "^revisado: false" "${VAULT}/memory/outputs/" 2>/dev/null | grep "\.md$" | head -8)
if [ -n "$DRAFTS" ]; then
  HAS_CONTENT=1
  BODY+="📋 **Drafts aguardando revisão:**\n"
  while IFS= read -r f; do
    BODY+="  - $(basename "$f" .md)\n"
  done <<< "$DRAFTS"
  BODY+="\n"
fi

# Aniversariantes hoje e amanhã
TODAY_MMDD=$(date +"%m-%d")
TOMORROW_MMDD=$(date -v+1d +"%m-%d" 2>/dev/null || date -d "tomorrow" +"%m-%d" 2>/dev/null)

ANIV_SECTION=""
while IFS= read -r f; do
  ANIV_LINE=$(grep "^aniversario:" "$f" 2>/dev/null | head -1)
  MMDD=$(echo "$ANIV_LINE" | grep -o "[0-9][0-9]-[0-9][0-9]$")
  NAME=$(grep "^nome:" "$f" 2>/dev/null | head -1 | sed 's/nome:[[:space:]]*//' | tr -d '"')
  [ -z "$NAME" ] || [ -z "$MMDD" ] && continue

  if [ "$MMDD" = "$TODAY_MMDD" ]; then
    ANIV_SECTION+="  - ${NAME} 🎉 (hoje)\n"
    HAS_CONTENT=1
  elif [ "$MMDD" = "$TOMORROW_MMDD" ]; then
    ANIV_SECTION+="  - ${NAME} (amanhã)\n"
    HAS_CONTENT=1
  fi
done < <(find "${VAULT}/memory/databases/aniversariantes/" -name "*.md" 2>/dev/null)

if [ -n "$ANIV_SECTION" ]; then
  BODY+="🎂 **Aniversariantes:**\n${ANIV_SECTION}\n"
fi

# Datas sazonais próximas (7 dias)
SAZONAIS=""
for i in 0 1 2 3 4 5 6 7; do
  CHECK=$(date -v+${i}d +"%Y-%m-%d" 2>/dev/null || date -d "+${i} days" +"%Y-%m-%d" 2>/dev/null)
  while IFS= read -r f; do
    DESC=$(grep "^descricao:" "$f" 2>/dev/null | head -1 | sed 's/descricao:[[:space:]]*//' | tr -d '"')
    FRENTE=$(grep "^frente:" "$f" 2>/dev/null | head -1 | sed 's/frente:[[:space:]]*//' | tr -d '"')
    [ -z "$DESC" ] && continue
    [ $i -eq 0 ] && LBL="hoje" || LBL="em ${i}d"
    SAZONAIS+="  - [${LBL}] ${DESC} — ${FRENTE}\n"
    HAS_CONTENT=1
  done < <(grep -rl "^data: ${CHECK}" "${VAULT}/memory/databases/datas-sazonais/" 2>/dev/null)
done

if [ -n "$SAZONAIS" ]; then
  BODY+="📅 **Datas sazonais (próximos 7 dias):**\n${SAZONAIS}\n"
fi

# Lembretes específicos do dia
[ "$DOW" -eq 5 ] && BODY+="🧹 Sexta-feira — quer rodar \`/manutencao\` hoje? (15 min)\n\n" && HAS_CONTENT=1
[ "$DOW" -eq 7 ] && BODY+="🗓️ Domingo — quer rodar \`/planejar-semana\` agora?\n\n" && HAS_CONTENT=1

# -------------------------------------------------------
# Monta output final
# -------------------------------------------------------
printf -- "---\n"
printf "⚙️ **%s, %s** — %s\n" "$DAY_PT" "$TODAY_BR" "$TIPO"

if [ $HAS_CONTENT -eq 0 ]; then
  printf "\n✅ Tudo limpo — bora trabalhar.\n"
else
  printf "\n"
  printf "%b" "$BODY"
fi

# Instrução Calendar (sempre — Claude cuida da chamada MCP)
printf "📆 *[auto] Busque os eventos do Google Calendar de hoje (%s) e inclua na sua primeira resposta se houver algo além da rotina fixa. Se não houver nada novo além dos blocos recorrentes, omita esta seção.*\n" "$TODAY"
printf -- "---\n"

exit 0
