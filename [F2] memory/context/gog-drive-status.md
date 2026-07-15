---
tipo: contexto-operacional
gerado-por: loh
revisado: true
valido-ate: 2027-01-15
---

# Estado Atual — Google/gog Drive

## Status: ✅ OPERACIONAL

**Autorizações renovadas em:** 2026-07-15  
**Projeto Google Cloud:** `logika-openclaw-gog` — **Em produção** ✅  
**Validade dos tokens:** Indeterminada (refresh tokens não expiram mais em 7 dias)

## Contas Ativas

| Conta | Serviços | Última autenticação |
|-------|----------|---------------------|
| `logikacreative.mkt@gmail.com` | drive (full), docs, sheets, forms | 2026-07-15T15:31Z |
| `davijadielson@gmail.com` | drive (full), calendar | 2026-07-15T15:32Z |

## Pré-requisito para agentes

Sempre definir antes de usar gog (senha canônica):
```bash
export GOG_KEYRING_PASSWORD="$(cat /data/.openclaw/credentials/gog/keyring-password)"
```

⚠️ Não usar senha ad-hoc. A senha está nos arquivos:
- `/data/.openclaw/credentials/gog/keyring-password`
- `/data/.openclaw/workspace/scripts/.secrets/gog-keyring-password`

## Documentação

- Briefing completo: `briefings/gog-drive-auth-briefing.md`
- Decisão detalhada: `decisions/2026-07-15-gog-auth-drive-fix.md`
- Diário: `2026-07-15.md`

## Próxima ação

- **Janeiro/2027:** Revisão periódica dos tokens
- Se `invalid_grant` aparecer: seguir procedimento no briefing