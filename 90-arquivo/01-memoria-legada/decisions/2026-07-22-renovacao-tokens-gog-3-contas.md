---
tema: 07 22 renovacao tokens gog 3 contas
atualizado_em: 2026-07-22
---

# Renovação de Tokens OAuth — gog (3 contas)

**Data:** 2026-07-22
**Status:** ✅ Concluído
**Responsável:** Lôh + Jadielson

## Problema

Todos os tokens OAuth do `gog` estavam expirados/revogados nas 3 contas:
- `invalid_grant: Token has been expired or revoked`

## O que foi feito

1. **Conta Lógika** (`logikacreative.mkt@gmail.com`) — reautorizada via OAuth
2. **Conta Pessoal** (`davijadielson@gmail.com`) — reautorizada via OAuth
3. **Conta Lôh** (`loh.open.logika@gmail.com`) — reautorizada via OAuth

## Método usado

Em vez do callback local do `gog` (que estava expirando antes do usuário colar a URL), foi usado:
1. Jadielson autorizou no navegador via link OAuth
2. Colou a URL de callback com o `code` de autorização
3. Lôh trocou o `code` por `refresh_token` + `access_token` via API direta do Google (`POST oauth2.googleapis.com/token`)
4. Refresh token importado no `gog` via `gog auth import --refresh-token-stdin --force`

## Tokens renovados

| Conta | Refresh Token | Expiração |
|---|---|---|
| davijadielson@gmail.com | ✅ Novo | ~1h access + refresh permanente |
| logikacreative.mkt@gmail.com | ✅ Novo | ~1h access + refresh permanente |
| loh.open.logika@gmail.com | ✅ Novo | ~1h access + refresh permanente |

## Testes realizados

- ✅ `gog drive ls` em todas as 3 contas
- ✅ `gog auth list` — 3 contas ativas sem warnings
- ✅ Drive da Lógika com conteúdo visível
- ✅ Drive pessoal com conteúdo visível
- ✅ Drive da Lôh vazio (esperado — conta nova)

## Observações

- Token da Lôh (`loh.open.logika@gmail.com`) foi renovado com escopos extras (Chat, Classroom, YouTube, etc.) por ser a conta admin dos agentes
- O BOOTSTRAP.md foi removido — identidade já consolidada desde 2026-05-30
- Jadielson autorizou via `authuser=0` (pessoal) e `authuser=1/4` (Lógika/Lôh) — contas diferentes no mesmo navegador