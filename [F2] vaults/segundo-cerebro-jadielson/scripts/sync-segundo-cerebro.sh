#!/usr/bin/env bash
set -euo pipefail
WORKSPACE="/data/.openclaw/workspace"
VAULT="$WORKSPACE/vaults/segundo-cerebro-jadielson"
REPO_URL="https://github.com/davijadielson-blip/segundo-cerebro-jadielson.git"

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

ASKPASS="$(mktemp /tmp/openclaw-vault-askpass.XXXXXX)"
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

if [ ! -d "$VAULT/.git" ]; then
  mkdir -p "$WORKSPACE/vaults"
  GIT_TERMINAL_PROMPT=0 GIT_ASKPASS="$ASKPASS" git clone "$REPO_URL" "$VAULT"
fi

cd "$VAULT"
git remote set-url origin "$REPO_URL"
git config user.name "Lôh OpenClaw"
git config user.email "openclaw-vault-sync@local"

# Primeiro puxa mudanças manuais do Obsidian/GitHub. Se houver conflito, falha sem tentar resolver sozinho.
GIT_TERMINAL_PROMPT=0 GIT_ASKPASS="$ASKPASS" git pull --ff-only origin main

# Envia mudanças locais feitas pela Lôh no vault, especialmente em [F2] memory/.
git add -A
if git diff --cached --quiet; then
  echo "Sem mudanças locais no Segundo Cérebro."
else
  git commit -m "Auto: sync segundo cerebro $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  GIT_TERMINAL_PROMPT=0 GIT_ASKPASS="$ASKPASS" git push origin main
fi
