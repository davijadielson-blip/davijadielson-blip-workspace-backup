---
tema: 07 22 proibicao zapier reforco jarvis
atualizado_em: 2026-07-22
---

# Decisão: Proibição Total de Zapier — Reforço via Jarvis

**Data:** 22/07/2026  
**Solicitante:** Jadielson Davi  
**Executor:** Jarvis (General LÓGIKA)  
**Status:** 🔴 Decisão final — nenhum agente, subagente ou tópico pode usar Zapier

---

## Contexto

Jadielson reportou que subagentes e tópicos continuam tentando usar Zapier mesmo após remoções anteriores. Diagnóstico:

- `mcp.servers` no gateway está vazio (`{}`) — Zapier MCP não está mais habilitado.
- Porém, as ferramentas Zapier (`zapier-1__*`, `zapier-3__*`) **ainda aparecem no toolset global** dos agentis.
- Os system prompts dos tópicos sob Jarvis (tópicos 1,5,6,8,9,10,11,12,14,96,474,550,551,552) **NÃO têm a proibição explícita de Zapier** — apenas o PROTOCOLO GLOBAL genérico.
- Sem proibição explícita no prompt, o agente vê as ferramentas Zapier disponíveis e pode tentar usá-las.

## Ações executadas

1. ✅ Decisão registrada no Cofre: `[F2] memory/decisions/2026-07-22-proibicao-zapier-reforco-jarvis.md`
2. ✅ AGENTS.md atualizado com regra mais forte e explícita (seção "🚫 REGRA ABSOLUTA — ZAPIER PROIBIDO NO ECOSSISTEMA").
3. ✅ TOOLS.md atualizado com nota sobre Zapier removido e caminho `gog` oficial.
4. 🔄 **Precisa de Lôh**: atualizar o gateway config para:
   a) Desabilitar/remover completamente os tool entries `zapier-1__*` e `zapier-3__*` do toolset ativo.
   b) Adicionar a proibição de Zapier nos system prompts de TODOS os tópicos/agentes que ainda não têm.

## Regra absoluta (vigente)

> **ZAPIER ESTÁ COMPLETAMENTE PROIBIDO EM TODO O ECOSSISTEMA.**  
> NENHUM agente, subagente, tópico, skill, cron, automação ou fluxo tem permissão para usar, mencionar, habilitar, reprovisionar, descobrir ações ou sugerir Zapier como alternativa.  
> TODO acesso a Google Drive, Gmail, Calendar, Docs e Sheets é feito EXCLUSIVAMENTE via `gog` (CLI via terminal).  
> Se uma instrução, skill, briefing, roteiro, demanda ou arquivo citar Zapier, considere FALHA DE PROCEDIMENTO e corrija para o caminho `gog`/fonte direta.  
> Esta regra substitui QUALQUER instrução anterior em QUALQUER documento e vale para agentes ATUAIS E FUTUROS.

## Próximo passo necessário

Jadielson precisa que **Lôh** aplique no gateway config:
- Remova `zapier-1` e `zapier-3` do toolset ativo (skills ou tools).
- Atualize os system prompts de tópicos 1,5,6,8,9,10,11,12,14,96,474,550,551,552 com a proibição Zapier + caminho `gog`.
- Garanta que novos tópicos/agentes herdem a regra automaticamente.

Fonte: Cofre (CONSTITUICAO.md, AGENTS.md, TOOLS.md, gateway config)