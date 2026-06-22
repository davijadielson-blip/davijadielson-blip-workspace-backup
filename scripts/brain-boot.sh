#!/bin/bash
# brain-boot.sh — Inicialização do segundo cérebro
# Chamado pelo hook SessionStart (.claude/settings.json)
# Faz git pull + exibe estado atual: drafts, frentes, datas sazonais

set -euo pipefail

VAULT="$(cd "$(dirname "$0")/.." && pwd)"
DATE=$(date +%Y-%m-%d)
WEEK=$(date +%V)

# ── 1. Git pull (sync com GitHub) ──────────────────────────────────────────
cd "$VAULT"
if git remote get-url origin &>/dev/null; then
  echo "✅ Workspace é fonte de verdade. Nada a puxar do GitHub."
fi

# ── 2. Drafts pendentes ────────────────────────────────────────────────────
DRAFTS=$(grep -rl "^revisado: false" "$VAULT/[F2] memory/outputs/" 2>/dev/null | grep "\.md$" | wc -l | tr -d ' ')
if [ "$DRAFTS" -gt 0 ]; then
  echo ""
  echo "📋 Drafts aguardando revisão: $DRAFTS"
  grep -rl "^revisado: false" "$VAULT/[F2] memory/outputs/" 2>/dev/null | grep "\.md$" | while read -r f; do
    echo "  • $(basename "$f")"
  done
fi

# ── 3. Contagem de notas por frente ───────────────────────────────────────
echo ""
echo "📁 Notas por frente:"
for frente in Logika-Creative Saude-Sao-Sebastiao Camara-Municipal SINDSS Alem-da-Foto Lives-Louvor-Reflexao Outros-Vereadores; do
  COUNT=$(find "$VAULT/[F1] 5-Frentes/$frente" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
  echo "  • $frente: $COUNT notas"
done

# ── 4. Datas sazonais próximas (7 dias) ───────────────────────────────────
echo ""
echo "📅 Datas sazonais nos próximos 7 dias:"
FOUND=0
for i in 0 1 2 3 4 5 6 7; do
  CHECK=$(date -v+${i}d +%Y-%m-%d 2>/dev/null || date -d "+${i} days" +%Y-%m-%d 2>/dev/null)
  MATCHES=$(grep -rl "^data: ${CHECK}" "$VAULT/[F2] memory/databases/datas-sazonais/" 2>/dev/null)
  if [ -n "$MATCHES" ]; then
    while IFS= read -r f; do
      DESC=$(grep "^descricao:" "$f" | sed 's/descricao: //')
      FRENTE=$(grep "^frente:" "$f" | sed 's/frente: //')
      echo "  • $CHECK — $DESC ($FRENTE)"
      FOUND=1
    done <<< "$MATCHES"
  fi
done
[ "$FOUND" -eq 0 ] && echo "  (nenhuma)"

# ── 5. Pendências críticas ─────────────────────────────────────────────────
PENDENCIAS="$VAULT/[F2] memory/context/pendencias.md"
if [ -f "$PENDENCIAS" ]; then
  CRITICAS=$(awk '/## 🔴 Críticas/,/## 🟡/' "$PENDENCIAS" | grep "^\- \[ \]" | head -5)
  if [ -n "$CRITICAS" ]; then
    echo ""
    echo "🔴 Pendências críticas:"
    echo "$CRITICAS" | while IFS= read -r line; do
      echo "  $line"
    done
  fi
fi

echo ""
echo "─────────────────────────────────────────"
echo "Vault pronto. Bom trabalho, Jadielson."
echo "─────────────────────────────────────────"
