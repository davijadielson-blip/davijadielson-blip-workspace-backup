#!/usr/bin/env bash
set -euo pipefail
CFG="/data/.openclaw/openclaw.json"
required=(cmo coo cco cto cfo cio cro caio main)
missing=()
for id in "${required[@]}"; do
  if ! jq -e --arg id "$id" '.agents.list[]? | select(.id == $id and (.systemPromptOverride // "" | length > 100))' "$CFG" >/dev/null; then
    missing+=("$id")
  fi
done
if [ "${#missing[@]}" -gt 0 ]; then
  echo "AGENTS_CONFIG_BROKEN missing_or_incomplete=${missing[*]}"
  exit 2
fi
mode=$(stat -c '%a' "$CFG")
echo "AGENTS_CONFIG_OK required=${required[*]} mode=$mode"
