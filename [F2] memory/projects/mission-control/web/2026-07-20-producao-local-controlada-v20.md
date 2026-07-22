---
tema: 07 20 producao local controlada v20
atualizado_em: 2026-07-22
---

# Mission Control v2.0 — Produção local controlada

**Data:** 2026-07-20 02:52 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** rodando em produção local controlada

## Entrega

O Mission Control foi colocado para rodar em modo produção local com proteção por senha ativada.

## URL local

`http://127.0.0.1:4174`

## Segurança

- Basic Auth ativado.
- Usuário configurado: `jadielson`.
- A senha real não foi salva no Cofre.
- Token Notion permanece fora do Cofre.
- Acesso sem autenticação retorna `401`.

## Processo

Servidor iniciado a partir de:

`/data/.openclaw/mission-control-next/`

Comando:

`PORT=4174 npm run start:prod`

## Testes

- `npm run build`: OK.
- Smoke test autenticado: OK.
- Teste sem autenticação: `401` OK.
- Rotas validadas:
  - `/`
  - `/api/logika-crm`

## Observação

Esta etapa deixa o app pronto e rodando localmente/controlado. Para acesso público/externo ainda é necessário expor via provedor, túnel seguro, VPS, domínio ou plataforma de deploy.

## Próximo passo recomendado

Definir forma de exposição externa:

1. VPS/domínio próprio.
2. Cloudflare Tunnel.
3. Vercel/Render/Railway com variáveis protegidas.
4. Acesso apenas local/host, se for suficiente.
