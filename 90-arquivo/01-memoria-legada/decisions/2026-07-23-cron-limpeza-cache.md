---
tema: configuração de cron de limpeza diária de cache
data: 2026-07-23
decisao: cron diário às 00:00 (America/Maceio) para limpar caches do sistema
autor: Lôh
aprovado_por: Jadielson Davi
status: ativo
---

# Cron — Limpeza Diária de Cache

## Job

- **Nome:** `limpeza-diaria-cache`
- **ID:** `eac72b16-9b61-4d5c-bd3c-d02e488fab2e`
- **Schedule:** `0 0 * * *` (todos os dias à meia-noite, fuso America/Maceio)
- **Session:** Isolada (não interfere na Lôh)
- **Delivery:** Nenhuma (silenciosa)

## O que limpa

1. **Homebrew cache** — arquivos com +30 dias em `/data/.cache/Homebrew/downloads/`
2. **NPM cache** — `/data/.npm/_cacache/`
3. **Browser cache** — Chromium caches em `/data/.openclaw/browser/`
4. **Pip cache** — `/data/.cache/pip/`
5. **Temp files** — `*.tmp`, `*.pyc`, `__pycache__`
6. **Git GC** — `git gc --auto --prune=now` no workspace

## Registro

Após cada execução, salva relatório em:
`[F2] memory/decisions/YYYY-MM-DD-limpeza-cache.md`

---

*Fonte: Cofre (cron add)*