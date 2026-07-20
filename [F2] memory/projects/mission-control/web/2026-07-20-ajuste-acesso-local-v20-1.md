# Mission Control v2.0.1 — Ajuste de acesso local

**Data:** 2026-07-20 02:55 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** servidor local reativado e testado

## Contexto

Jadielson informou que não conseguiu acessar o Mission Control.

## Diagnóstico

A URL `http://127.0.0.1:4174` é local do servidor/host onde o app está rodando. Em outro dispositivo, ela aponta para o próprio aparelho do usuário, não para o servidor OpenClaw.

## Ação realizada

O servidor de produção local foi reativado em:

`http://127.0.0.1:4174`

O Next também reportou URL de rede local:

`http://10.0.0.66:4174`

## Testes

Smoke test autenticado:

- `/`: OK.
- `/api/logika-crm`: OK.

## Observação

Para acesso fora do host/rede local, será necessário expor por túnel seguro, VPS, domínio, Cloudflare Tunnel, Vercel/Render/Railway ou outra forma de deploy externo.
