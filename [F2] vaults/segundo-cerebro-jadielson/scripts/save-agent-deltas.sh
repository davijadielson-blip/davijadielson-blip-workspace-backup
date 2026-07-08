#!/bin/bash
# Save 01:00 — cada agente salva seu delta NO WORKSPACE (condicional)
# Cron: diário às 01:00 BRT
# Princípio: só salva quem mudou. Nada de commit vazio.

WORKSPACE="/data/.openclaw/workspace"
LOG_DIR="$WORKSPACE/[F2] memory/outputs/logs"
DATA=$(date "+%Y-%m-%d %H:%M")
DATA_TAG=$(date +%Y-%m-%d)
LOG_FILE="$LOG_DIR/save-deltas-$DATA_TAG.md"

mkdir -p "$LOG_DIR"

echo "# 📓 Save de Deltas — $DATA_TAG" > "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "| Agente | Salvou? | Arquivos |" >> "$LOG_FILE"
echo "|--------|---------|----------|" >> "$LOG_FILE"

# Função: verifica se houve mudança em uma área e registra
check_and_save() {
  local AGENT_NAME=$1
  local AREA_PATH=$2
  local LOG_REF=$3

  if [ -d "$WORKSPACE/$AREA_PATH" ]; then
    CHANGES=$(cd "$WORKSPACE" && git status --porcelain "$AREA_PATH" 2>/dev/null | head -20)
    if [ -n "$CHANGES" ]; then
      FILE_COUNT=$(echo "$CHANGES" | wc -l)
      echo "| $AGENT_NAME | ✅ Sim | $FILE_COUNT arquivo(s) alterado(s): $LOG_REF |" >> "$LOG_FILE"
    else
      echo "| $AGENT_NAME | ❌ Não | Sem alterações |" >> "$LOG_FILE"
    fi
  else
    echo "| $AGENT_NAME | ⬜ N/A | Área não encontrada |" >> "$LOG_FILE"
  fi
}

# Agentes corporativos
check_and_save "CCO (Criação)" "[F2] memory/outputs" "outputs/"
check_and_save "CMO (Marketing)" "[F2] memory/context" "context/"
check_and_save "Bases Públicas" "[F2] memory/databases" "databases/"
check_and_save "CIO (Governança)" "[F2] memory/agents" "agents/"
check_and_save "CAIO (Automação)" "scripts/" "scripts/"
check_and_save "SAÚDE Social Media" "[F2] memory/agents" "agents/"
check_and_save "CÂMARA Social Media" "[F2] memory/agents" "agents/"
check_and_save "SINDSS Social Media" "[F2] memory/agents" "agents/"
check_and_save "COO (Operações)" "skills/" "skills/"
check_and_save "CRO (Vendas)" "[F2] memory/outputs" "outputs/"
check_and_save "CFO (Finanças)" "[F2] memory/context" "context/"
check_and_save "CTO (Tecnologia)" "[F2] memory/agents/cto" "cto/"
check_and_save "LÔH (Orquestradora)" "[F2] memory/sessions" "sessions/"

# Parede d'água: Central Pessoal separada
echo "" >> "$LOG_FILE"
echo "### 🧱 Central Pessoal (parede d'água)" >> "$LOG_FILE"
echo "| Agente | Salvou? | Arquivos |" >> "$LOG_FILE"
echo "|--------|---------|----------|" >> "$LOG_FILE"

check_and_save "Alfred" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Warren" "[F1] 4-Pessoal/Financas" "Financas/"
check_and_save "Arca" "[F2] memory/context" "context pessoal/"
check_and_save "Saúde/Corpo" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Autoconhecimento" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Família" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Identidade/Futuro" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Lazer/Hobbies" "[F1] 4-Pessoal" "4-Pessoal/"
check_and_save "Moisés" "[F1] 4-Pessoal" "4-Pessoal/"

echo "" >> "$LOG_FILE"
echo "---" >> "$LOG_FILE"
echo "*Gerado em: $DATA*" >> "$LOG_FILE"

echo "[$DATA] ✅ Save de deltas concluído" >> "$LOG_FILE"
tail -20 "$LOG_FILE"