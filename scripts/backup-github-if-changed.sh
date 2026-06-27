#!/usr/bin/env bash
# Backup incremental condicional do Cofre → GitHub.
# Só commita/pusha quando houver alterações reais.
# Fonte de verdade: /data/.openclaw/workspace

set -euo pipefail

cd /data/.openclaw/workspace

REMOTE="${BACKUP_REMOTE:-origin}"
BRANCH="${BACKUP_BRANCH:-main}"
DATA=$(date +%Y-%m-%d-%H%M)

printf 'Backup condicional Cofre → %s/%s (%s)\n' "$REMOTE" "$BRANCH" "$DATA"

CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  git checkout "$BRANCH"
fi

# Evita sobrescrever remoto. Nunca força push.
git fetch "$REMOTE" "$BRANCH"
git merge --ff-only "$REMOTE/$BRANCH"

# Só segue se houver alteração real no worktree.
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
  echo "Sem alterações; backup incremental ignorado."
  exit 0
fi

git add -A

if git diff --cached --quiet; then
  echo "Sem alterações staged após git add; backup incremental ignorado."
  exit 0
fi

git commit -m "backup: incremental $DATA"
git push "$REMOTE" "$BRANCH"

echo "Backup incremental concluído com sucesso: $DATA"
