#!/usr/bin/env bash
# Hook: PostToolUse(Write) — Automações pós-escrita
# Age em 3 paths: outputs/legendas/ | outputs/roteiros/ | memory/agents/

VAULT="/Users/servicepro/Library/CloudStorage/OneDrive-Pessoal/Documentos/Obsidian Vault 4/MAPA OBSIDIAN"

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" \
  2>/dev/null || echo "")
SESSION_ID=$(echo "$INPUT" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('session_id','unknown'))" \
  2>/dev/null || echo "unknown")

[ -z "$FILE_PATH" ] && exit 0

TIMESTAMP=$(date +"%H:%M")
ACTIVITY_LOG="/tmp/vault-session-${SESSION_ID}-activity.log"

# Registra no log de atividade da sessão
echo "- ${TIMESTAMP} → $(basename "$FILE_PATH")" >> "$ACTIVITY_LOG" 2>/dev/null

# -------------------------------------------------------
# 1. outputs/legendas/ → instrui Claude a gerar resumo-whats
# -------------------------------------------------------
if echo "$FILE_PATH" | grep -q "outputs/legendas/"; then
  FILENAME=$(basename "$FILE_PATH")
  printf "📲 *[auto] Legenda salva: \`%s\`.*\n*Gere também o resumo para WhatsApp (manchete curta estilo jornal + texto de apoio, sem hashtags) e salve em \`memory/outputs/resumos-whatsapp/\` com o mesmo slug.*\n\n" "$FILENAME"
  exit 0
fi

# -------------------------------------------------------
# 2. outputs/roteiros/ → adiciona ao pipeline.md
# -------------------------------------------------------
if echo "$FILE_PATH" | grep -q "outputs/roteiros/"; then
  FILENAME=$(basename "$FILE_PATH" .md)
  TODAY=$(date +"%Y-%m-%d")
  PIPELINE="${VAULT}/memory/databases/pipeline.md"

  if [ ! -f "$PIPELINE" ]; then
    {
      printf "---\ntipo: pipeline\ngerado-por: hook-post-write\n---\n\n"
      printf "# Pipeline de Produção\n\n"
      printf "| Data | Arquivo | Status |\n"
      printf "|------|---------|--------|\n"
    } > "$PIPELINE"
  fi

  printf "| %s | %s | ideia |\n" "$TODAY" "$FILENAME" >> "$PIPELINE"
  exit 0
fi

# -------------------------------------------------------
# 3. memory/agents/ (briefings) → loga mudança
# -------------------------------------------------------
if echo "$FILE_PATH" | grep -q "\[F2\] claude/agents/"; then
  FILENAME=$(basename "$FILE_PATH")
  TODAY=$(date +"%Y-%m-%d")
  TIME=$(date +"%H:%M")
  CHANGES_LOG="${VAULT}/memory/logs/agents-changes.md"

  mkdir -p "${VAULT}/memory/logs/" 2>/dev/null

  if [ ! -f "$CHANGES_LOG" ]; then
    {
      printf "---\ntipo: log-agents\ngerado-por: hook-post-write\n---\n\n"
      printf "# Log de Mudanças em Briefings\n\n"
      printf "| Data | Hora | Arquivo |\n"
      printf "|------|------|---------|\n"
    } > "$CHANGES_LOG"
  fi

  printf "| %s | %s | %s |\n" "$TODAY" "$TIME" "$FILENAME" >> "$CHANGES_LOG"
  exit 0
fi

exit 0
