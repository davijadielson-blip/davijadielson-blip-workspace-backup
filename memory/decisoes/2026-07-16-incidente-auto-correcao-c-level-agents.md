---
tema: 07 16 incidente auto correcao c level agents
atualizado_em: 2026-07-22
---

# Incidente — Auto-correção da configuração dos agentes C-Level

**Data/hora:** 2026-07-16 02:25 UTC  
**Origem:** cron `guard-c-level-agents-config`  
**Verificador:** `/data/.openclaw/workspace/ops/verify-c-level-agents.sh`

## Sintoma

O verificador retornou falha:

```text
AGENTS_CONFIG_BROKEN missing_or_incomplete=cmo coo cco cto cfo cio cro caio main
```

## Causa observada

Os agentes obrigatórios existiam em `/data/.openclaw/openclaw.json`, mas estavam sem `systemPromptOverride` suficiente para aprovação do guard.

## Correção aplicada

- Restaurados os prompts oficiais dos agentes C-Level a partir de `/data/.openclaw/workspace/memory/agents/prompts/`:
  - `caio-prompt.md`
  - `cro-prompt.md`
  - `cco-prompt.md`
  - `cmo-prompt.md`
  - `coo-prompt.md`
  - `cto-prompt.md`
  - `cfo-prompt.md`
  - `cio-prompt.md`
- Restaurado prompt operacional mínimo do agente `main` para cumprir o guard.
- Não houve exclusão de arquivos.

## Validação pós-correção

```text
AGENTS_CONFIG_OK required=cmo coo cco cto cfo cio cro caio main mode=600
```

## Status

✅ Auto-correção concluída e validada.

Fonte: Cofre (`ops/verify-c-level-agents.sh`, `memory/agents/prompts/`, `/data/.openclaw/openclaw.json`).
