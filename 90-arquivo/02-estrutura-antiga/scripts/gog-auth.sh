#!/usr/bin/env bash
# 🧬 gog-auth.sh — Autenticação Google direta para agentes
# Substitui completamente a dependência do Zapier MCP
# Uso: source scripts/gog-auth.sh && gog_drive <email> <comando>
#
# Contas disponíveis:
#   pessoal    → davijadielson@gmail.com
#   logika     → logikacreative.mkt@gmail.com
#   loh        → loh.open.logika@gmail.com
#
# Escopos autorizados:
#   📧 Gmail (modify)  🗂️ Drive (full - pessoal, readonly - logika/loh)
#   📅 Calendar         📄 Docs  📊 Sheets
#
# 2026-07-07: Drive pessoal (davijadielson) atualizado de readonly → full
#             Motivo: Warren precisava de escrita para comprovantes

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd 2>/dev/null || echo "/data/.openclaw/workspace/scripts")"
KEYRING_PW_FILE="/data/.openclaw/workspace/scripts/.secrets/gog-keyring-password"

# Carrega a senha do keyring
if [[ -f "$KEYRING_PW_FILE" ]]; then
  export GOG_KEYRING_PASSWORD="$(cat "$KEYRING_PW_FILE")"
else
  echo "❌ ERRO: Arquivo de senha do keyring não encontrado em $KEYRING_PW_FILE" >&2
  exit 1
fi

# Mapeia apelido → email completo
resolve_account() {
  case "$1" in
    pessoal|jadielson|davi|davijadielson) echo "davijadielson@gmail.com" ;;
    logika|logikacreative|lógika)          echo "logikacreative.mkt@gmail.com" ;;
    loh|open|agentes)                      echo "loh.open.logika@gmail.com" ;;
    *)                                     echo "$1" ;;  # já é email
  esac
}

# ── Comandos helpers ───────────────────────────────────────────────────────────

gog_drive() {
  local account=$(resolve_account "${1:-pessoal}")
  shift
  gog --account "$account" drive "$@"
}

gog_gmail() {
  local account=$(resolve_account "${1:-pessoal}")
  shift
  gog --account "$account" gmail "$@"
}

gog_calendar() {
  local account=$(resolve_account "${1:-pessoal}")
  shift
  gog --account "$account" calendar "$@"
}

gog_docs() {
  local account=$(resolve_account "${1:-pessoal}")
  shift
  gog --account "$account" docs "$@"
}

gog_sheets() {
  local account=$(resolve_account "${1:-pessoal}")
  shift
  gog --account "$account" sheets "$@"
}

gog_list_accounts() {
  gog auth list 2>&1 | grep -v WARN | grep -v hint
}

# Se executado diretamente (não sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "🔐 gog-auth — Autenticação Google unificada"
  echo ""
  echo "Use como library: source scripts/gog-auth.sh"
  echo ""
  echo "Comandos disponíveis:"
  echo "  gog_drive pessoal inventory --max 10"
  echo "  gog_gmail logika list 5"
  echo "  gog_calendar pessoal list --days 7"
  echo "  gog_list_accounts"
  echo ""
  echo "Contas: pessoal | logika | loh"
fi