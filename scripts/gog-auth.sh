#!/usr/bin/env bash
# Google Workspace environment for OpenClaw agents.
# Usage: source scripts/gog-auth.sh && gog_drive pessoal search "trashed=false" --max 10

set -euo pipefail

export PATH="/home/linuxbrew/.linuxbrew/bin:/data/.local/bin:$PATH"
export GOG_KEYRING_BACKEND="${GOG_KEYRING_BACKEND:-file}"
export GOG_ACCOUNT="${GOG_ACCOUNT:-davijadielson@gmail.com}"
export GOG_CLIENT="${GOG_CLIENT:-openclaw}"

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

resolve_client() {
  case "$1" in
    davijadielson@gmail.com) echo "${GOG_CLIENT:-openclaw}" ;;
    *) echo "default" ;;
  esac
}

gog_drive() {
  local account
  local client
  account="$(resolve_account "${1:-pessoal}")"
  client="$(resolve_client "$account")"
  shift || true
  gog --account "$account" --client "$client" drive "$@"
}

gog_gmail() {
  local account
  local client
  account="$(resolve_account "${1:-pessoal}")"
  client="$(resolve_client "$account")"
  shift || true
  gog --account "$account" --client "$client" gmail "$@"
}

gog_calendar() {
  local account
  local client
  account="$(resolve_account "${1:-pessoal}")"
  client="$(resolve_client "$account")"
  shift || true
  gog --account "$account" --client "$client" calendar "$@"
}

gog_docs() {
  local account
  local client
  account="$(resolve_account "${1:-pessoal}")"
  client="$(resolve_client "$account")"
  shift || true
  gog --account "$account" --client "$client" docs "$@"
}

gog_sheets() {
  local account
  local client
  account="$(resolve_account "${1:-pessoal}")"
  client="$(resolve_client "$account")"
  shift || true
  gog --account "$account" --client "$client" sheets "$@"
}

gog_list_accounts() {
  gog auth list 2>&1 | sed '/WARN/d;/hint/d'
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "gog-auth loaded for direct Google Workspace access."
  echo "Use: source scripts/gog-auth.sh"
  echo "Accounts: pessoal | logika | loh"
fi
