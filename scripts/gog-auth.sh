#!/usr/bin/env bash
# Google Workspace environment for OpenClaw agents.
# Usage: source scripts/gog-auth.sh && gog_drive pessoal search "trashed=false" --max 10

set -euo pipefail

export PATH="/home/linuxbrew/.linuxbrew/bin:/data/.local/bin:$PATH"
export GOG_KEYRING_BACKEND="${GOG_KEYRING_BACKEND:-file}"

KEYRING_PW_FILE="/data/.openclaw/workspace/scripts/.secrets/gog-keyring-password"
if [[ -f "$KEYRING_PW_FILE" ]]; then
  export GOG_KEYRING_PASSWORD="$(cat "$KEYRING_PW_FILE")"
fi

resolve_account() {
  case "${1:-pessoal}" in
    pessoal|jadielson|davi|davijadielson) echo "davijadielson@gmail.com" ;;
    logika|logikacreative|logikacreative.mkt) echo "logikacreative.mkt@gmail.com" ;;
    loh|open|agentes) echo "loh.open.logika@gmail.com" ;;
    *) echo "$1" ;;
  esac
}

gog_drive() {
  local account
  account="$(resolve_account "${1:-pessoal}")"
  shift || true
  gog --account "$account" drive "$@"
}

gog_gmail() {
  local account
  account="$(resolve_account "${1:-pessoal}")"
  shift || true
  gog --account "$account" gmail "$@"
}

gog_calendar() {
  local account
  account="$(resolve_account "${1:-pessoal}")"
  shift || true
  gog --account "$account" calendar "$@"
}

gog_docs() {
  local account
  account="$(resolve_account "${1:-pessoal}")"
  shift || true
  gog --account "$account" docs "$@"
}

gog_sheets() {
  local account
  account="$(resolve_account "${1:-pessoal}")"
  shift || true
  gog --account "$account" sheets "$@"
}

gog_list_accounts() {
  gog auth list 2>&1 | sed '/WARN/d;/hint/d'
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "gog-auth loaded for direct Google Workspace access."
  echo "Use: source scripts/gog-auth.sh"
  echo "Accounts: pessoal | logika | loh"
fi
