#!/usr/bin/env bash
# Backup automático do workspace → GitHub.
# Fonte de verdade: /data/.openclaw/workspace
# Remoto operacional do backup do workspace: origin

set -euo pipefail

cd /data/.openclaw/workspace

REMOTE="${BACKUP_REMOTE:-origin}"
BRANCH="${BACKUP_BRANCH:-main}"
DATA=$(date +%Y-%m-%d-%H%M)

printf 'Backup workspace → %s/%s (%s)\n' "$REMOTE" "$BRANCH" "$DATA"

# Garante que estamos na branch esperada.
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  git checkout "$BRANCH"
fi

# Integra apenas se for fast-forward. Nunca força push.
git fetch "$REMOTE" "$BRANCH"
git merge --ff-only "$REMOTE/$BRANCH"

git add -A
if git diff --cached --quiet; then
  git commit --allow-empty -m "backup: $DATA"
else
  git commit -m "backup: $DATA"
fi

git push "$REMOTE" "$BRANCH"

echo "Backup concluído com sucesso: $DATA"
