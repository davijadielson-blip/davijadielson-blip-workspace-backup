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

// Trava antirreversão: garante que rotinas de saúde/integração não consolidem
// padrões antigos de agentes/modelos. Política definida por Jadielson em 2026-06-26.
const officialModel={primary:'openai-codex/gpt-5.5',fallbacks:['openrouter/deepseek/deepseek-v4-flash','openrouter/google/gemini-2.5-flash-lite']};
const ids=['main','my-finance','alfred','arca','central-topic-agent','jarvis','identidade-visao-futuro','liberdade-lazer-ocio','autoconhecimento','saude-corpo-energia','familia-relacionamentos','espiritualidade-propositos','caio','cro','cco','cmo','coo','cto','cfo','cio'];
const roles={main:'agente principal','my-finance':'Warren',alfred:'Alfred',arca:'Arca','central-topic-agent':'Agente Temático',jarvis:'Jarvis','identidade-visao-futuro':'Identidade','liberdade-lazer-ocio':'Liberdade',autoconhecimento:'Autoconhecimento','saude-corpo-energia':'Saúde','familia-relacionamentos':'Família','espiritualidade-propositos':'Espiritualidade',caio:'CAIO',cro:'CRO',cco:'CCO',cmo:'CMO',coo:'COO',cto:'CTO',cfo:'CFO',cio:'CIO'};
c.agents=c.agents||{};
c.agents.defaults=c.agents.defaults||{};
c.agents.defaults.model=officialModel;
c.agents.defaults.subagents={...(c.agents.defaults.subagents||{}),allowAgents:ids,maxConcurrent:8};
const byId=new Map((Array.isArray(c.agents.list)?c.agents.list:[]).map(a=>[a.id,a]));
c.agents.list=ids.map(id=>{
  const a={...(byId.get(id)||{}),id};
  a.model=officialModel;
  a.systemPromptOverride=`COMANDO OPERACIONAL DA LÔH TEM PRECEDÊNCIA SOBRE PERSONA. Responda exatamente no formato pedido, curto e objetivo. Você é ${roles[id]}. Prioridade oficial de modelos: 1 openai-codex/gpt-5.5; 2 openrouter/deepseek/deepseek-v4-flash; 3 openrouter/google/gemini-2.5-flash-lite. Troca automática nessa ordem em falha/indisponibilidade. Consulte o Cofre (/data/.openclaw/workspace/) antes de demandas com contexto; se memory_search falhar, use leitura direta. Não publique/aprove/assuma compromisso externo sem OK de Jadielson via Lôh.`;
  if(id==='main') { a.thinkingDefault='low'; a.fastModeDefault=true; }
  return a;
});

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
echo 'Sincronizando exec-policy sem sobrescrever agents...'
openclaw exec-policy set --security=full --ask=off 2>/dev/null || true
