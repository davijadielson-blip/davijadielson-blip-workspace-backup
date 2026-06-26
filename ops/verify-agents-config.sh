#!/usr/bin/env bash
set -euo pipefail
CONFIG=${1:-/data/.openclaw/openclaw.json}
jq -e '
  (.agents.list | length == 20) and
  (.agents.defaults.model.primary == "openai-codex/gpt-5.5") and
  ((.agents.defaults.model.fallbacks | join(",")) == "openrouter/deepseek/deepseek-v4-flash,openrouter/google/gemini-2.5-flash-lite") and
  ([.agents.list[] | select((.model|type)!="object" or .model.primary!="openai-codex/gpt-5.5" or ((.model.fallbacks|join(","))!="openrouter/deepseek/deepseek-v4-flash,openrouter/google/gemini-2.5-flash-lite") or ((.systemPromptOverride//"")|test("COMANDO OPERACIONAL DA LÔH TEM PRECEDÊNCIA SOBRE PERSONA")|not))] | length == 0)
' "$CONFIG" >/dev/null
printf 'OK: agents config canonical (20 agents, official model priority, operational precedence).\n'
