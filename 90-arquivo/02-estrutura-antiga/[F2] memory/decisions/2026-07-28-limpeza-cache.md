---
tipo: registro operacional
tema: limpeza diária de caches
executado_em: 2026-07-28 11:12 UTC
origem: cron eac72b16-9b61-4d5c-bd3c-d02e488fab2e limpeza-diaria-cache
---

# Limpeza diária de caches — 2026-07-28

## Ações executadas
- Homebrew: removidos arquivos em `/data/.cache/Homebrew/downloads/` com mais de 30 dias.
- NPM: executado `npm cache clean --force` quando disponível e removido `/data/.npm/_cacache/`.
- Browser OpenClaw: removidos diretórios de Cache, Code Cache, GPUCache, Dawn/WebGPU/Graphite caches, Shader/GrShader/GraphiteDawn/GPUPersistent e caches de CRX.
- Pip: removido `/data/.cache/pip/`.
- Temporários: removidos `*.tmp`, `*.pyc` e diretórios `__pycache__` em `/data/.openclaw/`.
- Git: executado `git -C /data/.openclaw/workspace gc --auto --prune=now`.

## Espaço liberado estimado
- Antes: 299MB
- Depois: 53MB
- Liberado: 247MB (258035630 bytes)

## Observações
- Cálculo considera os caminhos-alvo de cache e temporários solicitados; limpeza de git gc pode liberar espaço fora dessa estimativa direta dependendo do estado do repositório.
- Log do npm cache clean: npm warn using --force Recommended protections disabled. 
