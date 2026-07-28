#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Uso: $0 <email> <redirect-url>" >&2
  echo "Emails esperados: logikacreative.mkt@gmail.com ou davijadielson@gmail.com" >&2
  exit 2
fi
acct="$1"
redirect_url="$2"
export GOG_KEYRING_BACKEND=file
export GOG_KEYRING_PASSWORD="$(cat /data/.openclaw/credentials/gog/keyring-password)"
gog auth add "$acct" \
  --services gmail,calendar,drive,docs,sheets,contacts \
  --drive-scope readonly \
  --gmail-scope readonly \
  --force-consent \
  --remote --step 2 \
  --auth-url "$redirect_url"
gog auth list --check
gog --account "$acct" --gmail-no-send --json drive inventory --max 10 > "/tmp/gog-drive-readonly-${acct//@/_}.json"
echo "OK: $acct reautorizada com Drive readonly amplo; smoke em /tmp/gog-drive-readonly-${acct//@/_}.json"
