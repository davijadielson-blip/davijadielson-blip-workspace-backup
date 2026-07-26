---
tema: auditoria de gasto OpenRouter
conteudo: diagnóstico de consumo, riscos e ações sobre gasto OpenRouter
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança, operações e conteúdo
cliente: Jadielson Davi
tipo: auditoria
prioridade: média
atualizado_em: 2026-07-26
usar_quando: consultar histórico ou contexto relacionado a auditoria de gasto OpenRouter
nao_usar_quando: substituir decisões finais em 00-central/decisoes.md
---

# Auditoria — novo gasto de créditos OpenRouter (~US$ 5)

**Data:** 2026-07-26  
**Solicitante:** Jadielson Davi  
**Tema:** Por que novos créditos OpenRouter foram consumidos após correções de modelo/auth.

## Resumo executivo

A nova drenagem de créditos OpenRouter ocorreu por combinação de três fatores:

1. **Crons explícitos continuaram ativos** e executaram tarefas pesadas com `sessionTarget: isolated`.
2. **Algumas execuções ainda estavam com cadeia antiga/misturada**, especialmente `openai/gpt-5.1-codex` como primário em cron/sessão antiga, o que falhava por parâmetro de pensamento (`low` não suportado), caindo em OpenRouter.
3. **A configuração observada no runtime/arquivo estava diferente da ordem aprovada por Jadielson** em um momento da auditoria: `openrouter/google/gemini-3.5-flash` aparecia antes de `openrouter/deepseek/deepseek-v4-flash`, enquanto a decisão aprovada era DeepSeek primeiro e Gemini 2.5 Flash Lite depois.

## Evidências principais

### 1. Cron das 21h tentou OpenRouter em 2026-07-26

Job:
- ID: `4cf67e57-3648-46fe-890c-be88abeab892`
- Nome: `LÔH — Resumo geral de AMANHÃ (21h)`
- Horário: diário às 21h America/Maceio

Execução problemática:
- `runAtMs`: `1785024004806`
- Status: `error`
- Erro:
  - `openai/gpt-5.1-codex`: falhou por `Unsupported value: 'low'` — o modelo exigia `medium`.
  - `openrouter/google/gemini-3.5-flash`: tentou rodar e retornou 402 por créditos insuficientes.
  - `openrouter/deepseek/deepseek-v4-flash`: tentou rodar e retornou 402 por créditos insuficientes.

Mensagem exata observada no cron:

```text
FallbackSummaryError: All models failed (3): openai/gpt-5.1-codex: 400 Unsupported value: 'low' is not supported with the 'gpt-5.1-codex' model. Supported values are: 'medium'. (format) | openrouter/google/gemini-3.5-flash: 402 This request requires more credits, or fewer max_tokens. You requested up to 32000 tokens, but can only afford 479. | openrouter/deepseek/deepseek-v4-flash: 402 This request requires more credits, or fewer max_tokens. You requested up to 32000 tokens, but can only afford 15421.
```

Interpretação: esse cron não necessariamente conseguiu gastar toda a tentativa — porque retornou 402 — mas confirma que o sistema ainda estava tentando OpenRouter por fallback com max_tokens alto.

### 2. Crons diários anteriores consumiram OpenRouter de forma recorrente

O mesmo cron das 21h (`4cf67e57...`) tem histórico de execuções bem-sucedidas via OpenRouter/DeepSeek, com grandes contextos:

- 2026-07-25/26: `deepseek/deepseek-v4-flash`, provider `openrouter`, uso registrado: `input_tokens` 269509, `output_tokens` 2873.
- 2026-07-24/25: `deepseek/deepseek-v4-flash`, provider `openrouter`, uso registrado: `input_tokens` 121780, `output_tokens` 4248.
- Várias execuções anteriores do mesmo cron também rodaram em `openrouter/deepseek/deepseek-v4-flash`.

Também o cron das 06h (`888d851b-658e-48b1-9acd-45f5d248292e`) rodou várias vezes em OpenRouter/DeepSeek, incluindo:

- 2026-07-25 06h: provider `openrouter`, modelo `deepseek/deepseek-v4-flash`, `input_tokens` 71637, `output_tokens` 4398.
- 2026-07-24 06h: provider `openrouter`, modelo `deepseek/deepseek-v4-flash`, `input_tokens` 129709, `output_tokens` 2868.

Interpretação: esses crons são explícitos, mas são pesados. Quando caem em OpenRouter, consomem saldo de forma previsível.

### 3. Heartbeats também apareceram como sessões que tentaram modelos antigos

Sessões recentes listadas:

- `agent:main:telegram:default:direct:7654417048:heartbeat`
- `agent:main:main:heartbeat`

Ambas apareceram como falhas rápidas em `gpt-5.1-codex`. Em rastros antigos também há heartbeat com `provider: openrouter`, modelo `deepseek/deepseek-v4-flash`.

Interpretação: heartbeats podem ter contribuído, mas a maior evidência de gasto está nos crons de resumo/briefing com contexto grande.

## Achado crítico durante a auditoria

A leitura direta de `/data/.openclaw/openclaw.json` durante a auditoria mostrou:

```json
{
  "primary": "openai-codex/gpt-5.5",
  "fallbacks": [
    "openrouter/google/gemini-3.5-flash",
    "openrouter/deepseek/deepseek-v4-flash"
  ]
}
```

Isso divergia da decisão confirmada por Jadielson:

```json
{
  "primary": "openai-codex/gpt-5.5",
  "fallbacks": [
    "openrouter/deepseek/deepseek-v4-flash",
    "openrouter/google/gemini-2.5-flash-lite"
  ]
}
```

## Correção emergencial aplicada

Após identificar a regressão, a cadeia foi regravada em `/data/.openclaw/openclaw.json` para:

1. `openai-codex/gpt-5.5`
2. `openrouter/deepseek/deepseek-v4-flash`
3. `openrouter/google/gemini-2.5-flash-lite`

Aplicado em:

- `agents.defaults.model`
- `agents.defaults.subagents.model`
- todos os `agents.list[].model`

Validação adicional:

- `openai:default` permanece ausente dos auth-profiles dos agentes.
- Gateway recarregado via `gateway.restart`.

## Diagnóstico final

O gasto adicional de aproximadamente US$ 5 em OpenRouter provavelmente veio principalmente de **crons explícitos diários pesados** (06h e 21h), que continuaram autorizados e caíram/rodaram em OpenRouter quando o primário falhou ou quando sessões antigas ainda tinham cadeia antiga.

A causa não parece ser “agentes acordando sozinhos em cadeia”, mas sim:

- crons explícitos ativos;
- fallback OpenRouter autorizado;
- contexto muito grande/max_tokens alto;
- sessões/crons antigos ainda usando configuração anterior;
- regressão/estado divergente da cadeia de modelos durante a auditoria.

## Recomendação para impedir novo gasto alto

Opções de segurança, da mais conservadora para a mais flexível:

1. **Desativar temporariamente os crons de resumo/briefing** até confirmar saldo e modelo.
2. **Manter crons, mas sem fallback OpenRouter** — Codex-only nos crons; OpenRouter só para chat manual.
3. **Manter fallback OpenRouter, mas reduzir escopo dos crons**: contexto menor, arquivos específicos, sem varredura ampla, timeout menor e saída mais curta.
4. **Criar regra por job:** tarefas diárias simples usam Codex-only; só tarefas urgentes/autorizadas usam OpenRouter fallback.

## Fonte

Fonte: Cofre (`CONSTITUICAO.md`, `memory/2026-07-26.md`), `cron list`, `cron runs` dos jobs `4cf67e57...` e `888d851b...`, leitura direta de `/data/.openclaw/openclaw.json`, rastros de sessões em `/data/.openclaw/agents/main/sessions/`, `session_status`, `sessions_list`.
