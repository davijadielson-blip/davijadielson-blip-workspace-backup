---
tema: 07 20 tunnel cloudflare v20 2
atualizado_em: 2026-07-22
---

# Mission Control v2.0.2 — Acesso externo via Cloudflare Quick Tunnel

**Data:** 2026-07-20 02:59 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** túnel criado e testado

## Contexto

Jadielson informou que não conseguiu acessar a URL local/rede. Foi necessário expor o Mission Control por um túnel externo temporário.

## Entrega

Foi instalado `cloudflared` localmente em:

`/data/.openclaw/bin/cloudflared`

E criado um Cloudflare Quick Tunnel apontando para:

`http://127.0.0.1:4174`

## URL externa temporária

`https://likewise-threats-its-payroll.trycloudflare.com`

## Acesso

Basic Auth permanece ativo.

- Usuário: `jadielson`
- Senha: não registrada no Cofre; enviada apenas no chat operacional da sessão.

## Testes

Smoke test autenticado na URL externa:

- `/`: OK.
- `/api/logika-crm`: OK.

Saída:

```text
OK / 200
OK /api/logika-crm 200
Smoke test OK
```

## Observação importante

Este é um Quick Tunnel temporário, sem garantia de permanência. Para produção real, usar Cloudflare Tunnel nomeado com conta/domínio, VPS, Vercel, Render ou Railway.

## Próximo passo recomendado

Se Jadielson conseguir acessar, transformar em túnel permanente ou escolher provedor final.
