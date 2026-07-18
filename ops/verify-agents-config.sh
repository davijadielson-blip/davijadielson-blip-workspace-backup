#!/usr/bin/env bash
set -euo pipefail
CONFIG=${1:-/data/.openclaw/openclaw.json}
jq -e '
  (.agents.list | length == 21) and
  (.agents.defaults.model.primary == "openai-codex/gpt-5.5") and
  ((.agents.defaults.model.fallbacks | join(",")) == "openrouter/deepseek/deepseek-v4-flash,openrouter/google/gemini-2.5-flash-lite") and
  ([.agents.list[] | select((.model|type)!="object" or .model.primary!="openai-codex/gpt-5.5" or ((.model.fallbacks|join(","))!="openrouter/deepseek/deepseek-v4-flash,openrouter/google/gemini-2.5-flash-lite"))] | length == 0)
' "$CONFIG" >/dev/null
printf 'OK: agents config canonical (21 agents, GPT-5.5 Codex primary, OpenRouter only fallback B/C).\n'
