---
tema: 07 22 gog auth loh concluido
atualizado_em: 2026-07-22
---

# Conclusão — Gog auth da conta Lôh (loh.open.logika@gmail.com)

**Data:** 2026-07-22
**Status:** ✅ Concluído

## O que foi feito
1. Jadielson abriu o link de autorização OAuth e autorizou a conta
2. Callback URL capturada e token de refresh obtido via Google OAuth API
3. Token importado no gog via `gog auth import --refresh-token-stdin`
4. GOG_KEYRING_PASSWORD persistida permanentemente em `/data/.profile`

## Status atual do gog
| Conta | Escopos | Última atualização |
|---|---|---|
| davijadielson@gmail.com | calendar, drive | 2026-07-15 |
| logikacreative.mkt@gmail.com | docs, drive, forms, sheets | 2026-07-15 |
| loh.open.logika@gmail.com | drive (funcionando) | 2026-07-22 ✅ |

## Testes realizados
- ✅ `gog auth list` — 3 contas ativas sem warnings
- ✅ `gog drive ls` — autenticação funcionando
- ✅ `gog calendar list` — calendário da Lôh acessível
- ✅ GOG_KEYRING_PASSWORD — persistida no .profile

## Observações
- A conta Lôh foi criada recentemente e tem poucos dados (Drive vazio, calendário com eventos de pautas da Saúde)
- As 3 contas agora estão autenticadas e funcionais para os agentes