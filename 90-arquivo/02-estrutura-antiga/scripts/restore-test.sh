#!/bin/bash
# RESTORE TESTADO — procedimento manual seguro
# Traz 1 arquivo do backup GitHub para pasta TEMPORÁRIA
# NÃO sobrescreve produção

TEMP_DIR="/tmp/restore-test-$(date +%Y%m%d-%H%M)"
VAULT="/data/.openclaw/segundo-cerebro-jadielson"
LOG_DIR="/data/.openclaw/workspace/[F2] memory/outputs/logs"
ARQUIVO_TESTE="entregaveis/briefing-identidade-visual-julho-amarelo-2026.md"

mkdir -p "$TEMP_DIR/entregaveis"
mkdir -p "$LOG_DIR"

echo "🧪 RESTORE TEST — $(date '+%Y-%m-%d %H:%M')"
echo ""

cd "$VAULT" || { echo "❌ FALHOU: vault clone inacessivel"; exit 1; }
git fetch origin main 2>&1 | tail -1

git show origin/main:"$ARQUIVO_TESTE" > "$TEMP_DIR/$ARQUIVO_TESTE" 2>&1

if [ -s "$TEMP_DIR/$ARQUIVO_TESTE" ]; then
  SIZE=$(wc -c < "$TEMP_DIR/$ARQUIVO_TESTE")
  LINES=$(wc -l < "$TEMP_DIR/$ARQUIVO_TESTE")
  echo "✅ RESTORE FUNCIONOU"
  echo "   Arquivo: $ARQUIVO_TESTE"
  echo "   Tamanho: $SIZE bytes / $LINES linhas"
  echo "   Local temporario: $TEMP_DIR"
  echo "   Producao intacta: /data/.openclaw/workspace/$ARQUIVO_TESTE"
  echo ""
  echo "📋 Verificando integridade..."
  diff "$TEMP_DIR/$ARQUIVO_TESTE" "/data/.openclaw/workspace/$ARQUIVO_TESTE" && \
    echo "   ✅ Backup IDENTICO ao workspace" || \
    echo "   ⚠️ Backup DIFERE do workspace"
  
  echo "[$(date '+%Y-%m-%d %H:%M')] RESTORE TEST OK - arquivo=$ARQUIVO_TESTE - tamanho=$SIZE" >> "$LOG_DIR/restore-test.log"
  echo ""
  echo "🧪 Teste concluido. Pasta segura para deletar:"
  echo "   rm -rf $TEMP_DIR"
else
  echo "❌ RESTORE FALHOU"
  echo "[$(date '+%Y-%m-%d %H:%M')] RESTORE TEST FALHOU - arquivo=$ARQUIVO_TESTE" >> "$LOG_DIR/restore-test.log"
fi