# Mission Control v1.7 — Preparação de deploy/acesso seguro

**Data:** 2026-07-20 02:40 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** preparado e testado localmente

## Entrega

Foi preparada a base de deploy/acesso estável do Mission Control Web.

## Arquivos criados/alterados no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos:

- `.env.example` — modelo de variáveis sem segredos reais.
- `next.config.js` — headers básicos de segurança.
- `DEPLOY.md` — instruções de deploy seguro.

## Segurança aplicada

Headers configurados:

- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`

## Variáveis necessárias

- `NOTION_TOKEN`
- `NOTION_LOGIKA_CRM_DATABASE_ID`
- `NOTION_LOGIKA_TASKS_DATABASE_ID`

## Auditoria

`npm audit` segue reportando 2 vulnerabilidades moderadas ligadas a `postcss` via `next`.

A correção automática sugerida pelo npm aponta para `next@9.3.3`, o que seria downgrade/mudança inadequada. Decisão técnica mantida: **não aplicar `npm audit fix --force`**.

## Testes

- `npm run build`: OK.

## Estratégia recomendada de deploy

1. Deploy privado/controlado primeiro.
2. Proteger variáveis no provedor.
3. Validar rota `/api/logika-crm` no ambiente final.
4. Validar snapshot diário após deploy.
5. Atualizar Next/PostCSS quando houver correção segura sem downgrade.

## Próximos passos

1. Escolher ambiente de deploy.
2. Criar autenticação simples ou limitar acesso.
3. Publicar versão privada.
4. Monitorar cron e Notion API.
