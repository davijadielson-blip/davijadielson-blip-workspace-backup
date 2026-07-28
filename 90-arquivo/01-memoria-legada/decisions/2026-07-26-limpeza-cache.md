---
tema: limpeza diária de caches do sistema
conteudo: registro de execução cron e espaço liberado
setor: manutenção operacional
cliente: Jadielson Davi
tipo: decisão/registro operacional
prioridade: média
criado_em: 2026-07-26
---

# Limpeza diária de caches — 2026-07-26

Execução solicitada por cron `eac72b16-9b61-4d5c-bd3c-d02e488fab2e` às 03:00 UTC.

## Ações executadas

- Homebrew: remoção de arquivos em `/data/.cache/Homebrew/downloads/` com mais de 30 dias.
- NPM: `npm cache clean --force` quando disponível + remoção de `/data/.npm/_cacache/`.
- Browser OpenClaw: remoção dos diretórios de cache indicados.
- Pip: remoção de `/data/.cache/pip/`.
- Temporários: remoção de `*.tmp`, `*.pyc` e diretórios `__pycache__` em `/data/.openclaw/`.
- Git: `git -C /data/.openclaw/workspace gc --auto --prune=now` (executado).

## Espaço apurado

- Antes: 301MB (314590634 bytes)
- Depois: 78MB (81547511 bytes)
- Espaço liberado estimado: **223MB (233043123 bytes)**

## Observações

- Status NPM: `npm warn using --force Recommended protections disabled.`
- A apuração considera os diretórios/arquivos-alvo da limpeza; efeitos indiretos do `git gc --auto` podem variar conforme necessidade do Git.
