#!/usr/bin/env bash
# Garante integrações críticas no config ativo: Tavily, Notion e Whisper.
set -euo pipefail
CONFIG="/data/.openclaw/openclaw.json"
TAVILY_SECRET="/data/.openclaw/secrets/tavily.env"
WORKSPACE_ENV="/data/.openclaw/workspace/.env"

[ -f "$CONFIG" ] || { echo "ERRO: config ausente" >&2; exit 1; }
[ -f "$TAVILY_SECRET" ] || { echo "ERRO: Tavily secret ausente" >&2; exit 1; }
[ -f "$WORKSPACE_ENV" ] || { echo "ERRO: workspace .env ausente" >&2; exit 1; }
# shellcheck disable=SC1090
source "$TAVILY_SECRET"
NOTION_TOKEN=$(grep -E '^NOTION_TOKEN=' "$WORKSPACE_ENV" | tail -1 | sed 's/^NOTION_TOKEN=//')
[ -n "${TAVILY_API_KEY:-}" ] || { echo "ERRO: TAVILY_API_KEY vazio" >&2; exit 1; }
[ -n "${NOTION_TOKEN:-}" ] || { echo "ERRO: NOTION_TOKEN vazio" >&2; exit 1; }

TAVILY_API_KEY="$TAVILY_API_KEY" NOTION_TOKEN="$NOTION_TOKEN" node - <<'NODE'
const fs=require('fs');
const path='/data/.openclaw/openclaw.json';
const c=JSON.parse(fs.readFileSync(path,'utf8'));
const before=JSON.stringify(c);
const tavily=process.env.TAVILY_API_KEY;
const notion=process.env.NOTION_TOKEN;

c.plugins=c.plugins||{};
c.plugins.enabled=true;
c.plugins.allow=Array.isArray(c.plugins.allow)?c.plugins.allow:[];
for (const p of ['tavily','whatsapp','telegram','discord','slack','openrouter','openai','browser']) {
  if(!c.plugins.allow.includes(p)) c.plugins.allow.push(p);
}
c.plugins.entries=c.plugins.entries||{};
c.plugins.entries.tavily={enabled:true,config:{webSearch:{apiKey:tavily,baseUrl:'https://api.tavily.com'}}};

c.tools=c.tools||{};
c.tools.web=c.tools.web||{};
c.tools.web.search={...(c.tools.web.search||{}),enabled:true,provider:'tavily',maxResults:10,apiKey:tavily};

c.skills=c.skills||{};
c.skills.entries=c.skills.entries||{};
c.skills.entries.notion={...(c.skills.entries.notion||{}),enabled:true,config:{...(c.skills.entries.notion?.config||{}),token:notion}};
c.skills.entries['openai-whisper']={...(c.skills.entries['openai-whisper']||{}),enabled:true};

if(JSON.stringify(c)!==before){
  fs.copyFileSync(path, `${path}.bak-ensure-integrations-${new Date().toISOString().replace(/[-:.]/g,'').slice(0,15)}Z`);
  fs.writeFileSync(path, JSON.stringify(c,null,2)+'\n');
  console.log('FIXED: integrações reaplicadas');
}else{
  console.log('OK: integrações já estavam aplicadas');
}
console.log(JSON.stringify({tavily:c.tools?.web?.search?.provider,notion:!!c.skills?.entries?.notion?.enabled,whisper:!!c.skills?.entries?.['openai-whisper']?.enabled},null,2));
NODE
openclaw config validate
