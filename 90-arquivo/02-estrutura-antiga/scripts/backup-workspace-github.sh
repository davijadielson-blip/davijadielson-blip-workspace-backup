#!/usr/bin/env bash
set -euo pipefail
WORKSPACE="/data/.openclaw/workspace"
REPO_URL="https://github.com/davijadielson-blip/davijadielson-blip-workspace-backup.git"
cd "$WORKSPACE"

if [ -f "$WORKSPACE/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "$WORKSPACE/.env"
  set +a
fi

if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "GITHUB_TOKEN ausente em $WORKSPACE/.env" >&2
  exit 2
fi

ASKPASS="$(mktemp /tmp/openclaw-git-askpass.XXXXXX)"
cat > "$ASKPASS" <<'EOF'
#!/usr/bin/env bash
case "$1" in
  *Username*) printf '%s\n' 'x-access-token' ;;
  *Password*) printf '%s\n' "$GITHUB_TOKEN" ;;
  *) printf '%s\n' "$GITHUB_TOKEN" ;;
esac
EOF
chmod 700 "$ASKPASS"
cleanup() { rm -f "$ASKPASS"; }
trap cleanup EXIT

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init
fi
if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "$REPO_URL"
else
  git remote set-url origin "$REPO_URL"
fi

git config user.name "Lôh OpenClaw"
git config user.email "openclaw-backup@local"

git add -A
if git diff --cached --quiet; then
  echo "Sem mudanças para backup."
else
  git commit -m "Auto: workspace backup $(date -u +%Y-%m-%dT%H:%M:%SZ)"
fi

GIT_TERMINAL_PROMPT=0 GIT_ASKPASS="$ASKPASS" git push origin main
