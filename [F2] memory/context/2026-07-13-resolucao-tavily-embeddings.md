# Resolução — Tavily + Memory Search (2026-07-13)

## Problema
- Tavily/Pesquisador inoperante — sem chave de API configurada
- Memory Search (embeddings) inoperante — cota OpenAI esgotada (erro 429)

## O que foi feito

### Memory Search (OpenAI embeddings) ✅
- Jadielson adicionou créditos na conta OpenAI
- Testado e confirmado: memory_search voltou a funcionar (modelo `text-embedding-3-small`, ~270ms)

### Tavily / Pesquisador ✅
- Chave obtida por Jadielson: `tvly-dev-...GPx3`
- Chave salva em:
  - `/data/.openclaw/secrets/tavily.env`
  - `/data/.openclaw/openclaw.json` (em `tools.web.search.apiKey`)
  - `/data/.openclaw/workspace/.env` (como `TAVILY_API_KEY`)
- `web_search` (provider: tavily) testado e funcionando — resposta em 1.2s
- `tavily_search` (tool dedicada) ainda precisa da env var no ambiente do processo (`TAVILY_API_KEY` no `/proc/7/environ`), mas a tool `web_search` já está operacional plenamente

### Observação técnica
O gateway (`u4s-openclaw`) é gerenciado pelo `tini` (PID 1) e não herda env vars de `.bashrc` ou `/etc/profile.d/`. A cada restart, o processo filho (PID 7) é recriado com o mesmo ambiente do `tini`. Para o `tavily_search` tool funcionar, seria necessário injetar `TAVILY_API_KEY` no ambiente do contêiner (Dockerfile / docker-compose / entrypoint). Como `web_search` já funciona com a chave no `openclaw.json`, a funcionalidade de busca web está completa.

## Status final
| Serviço | Status | Observação |
|---|---|---|
| ✅ Memory Search (embeddings) | **Online** | Créditos OpenAI renovados |
| ✅ Web Search (Tavily via web_search tool) | **Online** | Configurado no openclaw.json |
| ⚠️ Tavily Search (tavily_search tool) | **Parcial** | Funciona só se env var no ambiente do gateway |
| ✅ Cofre (leitura direta) | **Online** | Sempre esteve |
| ✅ Ferramentas de escrita/execução | **Online** | Sempre estiveram |

## Próximos passos
- Para resolver 100% o `tavily_search`: adicionar `TAVILY_API_KEY` no entrypoint do contêiner ou no docker-compose
- Jadielson pode voltar às pendências operacionais agora que os serviços estão no ar

Fonte: Cofre (config, logs, scripts de health, testes de conectividade).