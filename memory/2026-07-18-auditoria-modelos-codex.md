# Auditoria e correção — prioridade GPT-5.5 Codex

Data: 2026-07-18 18:29 UTC
Solicitante: Jadielson Davi
Responsável: Lôh

## Intenção operacional confirmada
Usar sempre `openai-codex/gpt-5.5` como modelo primário. OpenRouter deve atuar apenas como fallback B/C para não interromper execução.

## Diagnóstico
- A memória oficial já registrava a política desde 2026-06-26: `openai-codex/gpt-5.5` primário; fallbacks `openrouter/deepseek/deepseek-v4-flash` e `openrouter/google/gemini-2.5-flash-lite`.
- A auditoria runtime mostrou divergência no agente `main`: estava publicado em `agents_list` como `openrouter/deepseek/deepseek-v4-flash`.
- O arquivo `/data/.openclaw/openclaw.json` também tinha fallbacks extras em defaults e agentes, além de `main` com primário OpenRouter.

## Correção aplicada
- Backup criado: `/data/.openclaw/openclaw.json.bak-model-audit-20260718T182944Z`.
- Corrigido `/data/.openclaw/openclaw.json` para:
  - `agents.defaults.model.primary = openai-codex/gpt-5.5`
  - `agents.defaults.model.fallbacks = [openrouter/deepseek/deepseek-v4-flash, openrouter/google/gemini-2.5-flash-lite]`
  - todos os 21 agentes em `agents.list` com o mesmo bloco de modelo oficial.
- Gateway recebeu reload/restart via ferramenta `gateway.restart`.

## Validação pós-correção
- `agents_list` validou 21 agentes, todos `configured: true`, todos com modelo publicado `openai-codex/gpt-5.5`.
- A sessão atual foi recolocada explicitamente em `openai-codex/gpt-5.5` após o teste de reset.
- Observação: sessões já abertas podem manter fallbacks herdados até renovação da sessão; novas sessões/agentes devem herdar a política corrigida no arquivo oficial.

## Regra de continuidade
Se reaparecer OpenRouter como primário em qualquer agente, tratar como regressão de configuração e rodar:
- `agents_list` para validar runtime;
- `ops/verify-agents-config.sh` para validar arquivo;
- comparar `/data/.openclaw/openclaw.json` contra a política oficial acima.
