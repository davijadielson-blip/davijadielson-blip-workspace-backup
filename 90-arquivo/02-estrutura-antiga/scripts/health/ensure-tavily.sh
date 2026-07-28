#!/usr/bin/env bash
# Garante Tavily como buscador principal do OpenClaw.
# Token fica fora do workspace: /data/.openclaw/secrets/tavily.env
set -euo pipefail
CONFIG="/data/.openclaw/openclaw.json"
SECRET="/data/.openclaw/secrets/tavily.env"

if [ ! -f "$SECRET" ]; then
  echo "ERRO: segredo Tavily ausente: $SECRET" >&2
  exit 1
fi
# shellcheck disable=SC1090
source "$SECRET"
if [ -z "${TAVILY_API_KEY:-}" ]; then
  echo "ERRO: TAVILY_API_KEY vazio" >&2
  exit 1
fi

NEEDS_FIX=$(node - <<'NODE'
const fs=require('fs');
const c=JSON.parse(fs.readFileSync('/data/.openclaw/openclaw.json','utf8'));
const ok = c.plugins?.allow?.includes('tavily') && c.plugins?.entries?.tavily?.enabled === true && c.tools?.web?.search?.enabled === true && c.tools?.web?.search?.provider === 'tavily' && !!(c.tools?.web?.search?.apiKey || c.plugins?.entries?.tavily?.config?.webSearch?.apiKey);
console.log(ok ? 'no' : 'yes');
NODE
)

if [ "$NEEDS_FIX" = "no" ]; then
  echo "OK: Tavily já está como provider principal."
  exit 0
fi

TS=$(date +%Y%m%dT%H%M%SZ)
cp "$CONFIG" "$CONFIG.bak-ensure-tavily-$TS"
TAVILY_API_KEY="$TAVILY_API_KEY" node - <<'NODE'
const fs=require('fs');
const path='/data/.openclaw/openclaw.json';
const token=process.env.TAVILY_API_KEY;
const c=JSON.parse(fs.readFileSync(path,'utf8'));
c.plugins=c.plugins||{};
c.plugins.enabled=true;
c.plugins.allow=Array.isArray(c.plugins.allow)?c.plugins.allow:[];
for (const p of ['tavily','whatsapp','telegram','discord','slack','openrouter','openai','browser']) {
  if(!c.plugins.allow.includes(p)) c.plugins.allow.push(p);
}
c.plugins.entries=c.plugins.entries||{};
c.plugins.entries.tavily={enabled:true,config:{webSearch:{apiKey:token,baseUrl:'https://api.tavily.com'}}};
c.tools=c.tools||{};
c.tools.web=c.tools.web||{};
c.tools.web.search={...(c.tools.web.search||{}),enabled:true,provider:'tavily',maxResults:10,apiKey:token};
fs.writeFileSync(path, JSON.stringify(c,null,2)+'\n');
NODE
openclaw config validate
# Hot reload/restart signal via CLI if available; failure should not hide config repair.
openclaw gateway restart || true
echo "FIXED: Tavily reaplicado como provider principal."
