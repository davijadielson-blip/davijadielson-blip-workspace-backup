#!/usr/bin/env bash
set -euo pipefail

export PATH="/data/.npm-global/bin:$PATH"
export PATH="/data/.openclaw/workspace/scripts/.venv/bin:/home/linuxbrew/.linuxbrew/bin:/data/.local/bin:$PATH"

if [[ -f "/data/.openclaw/workspace/scripts/.secrets/notion.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  . "/data/.openclaw/workspace/scripts/.secrets/notion.env"
  set +a
fi
