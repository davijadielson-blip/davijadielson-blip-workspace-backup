#!/usr/bin/env bash
# Backup incremental condicional do Cofre → GitHub.
# Só commita/pusha quando houver alterações reais.
# Fonte de verdade: /data/.openclaw/workspace
# Fix: --no-optional-locks / core.preloadindex=false para evitar "unable to create threaded lstat"

set -euo pipefail

cd /data/.openclaw/workspace

REMOTE="${BACKUP_REMOTE:-origin}"
BRANCH="${BACKUP_BRANCH:-main}"
DATA=$(date +%Y-%m-%d-%H%M)

# Evita erro "unable to create threaded lstat" em ambientes com alta contenção de I/O
export GIT_OPTIONAL_LOCKS=0
GIT="git -c core.preloadindex=false"

printf 'Backup condicional Cofre → %s/%s (%s)\n' "$REMOTE" "$BRANCH" "$DATA"

CURRENT_BRANCH=$($GIT branch --show-current)
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  $GIT checkout "$BRANCH"
fi

# Evita sobrescrever remoto. Nunca força push.
$GIT fetch "$REMOTE" "$BRANCH"
$GIT merge --ff-only "$REMOTE/$BRANCH"

# Só segue se houver alteração real no worktree.
if $GIT diff --quiet && $GIT diff --cached --quiet && [ -z "$($GIT ls-files --others --exclude-standard)" ]; then
  echo "Sem alterações; backup incremental ignorado."
  exit 0
fi

$GIT add -A

if $GIT diff --cached --quiet; then
  echo "Sem alterações staged após git add; backup incremental ignorado."
  exit 0
fi

$GIT commit -m "backup: incremental $DATA"
$GIT push "$REMOTE" "$BRANCH"

echo "Backup incremental concluído com sucesso: $DATA"
