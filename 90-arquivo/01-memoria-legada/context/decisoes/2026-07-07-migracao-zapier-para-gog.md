---
tipo: decisao
data: 2026-07-07
status: implementado
fonte: Lôh + Jadielson
assunto: Migração de Zapier para autenticação direta (gog)
---

# Decisão — Migração Zapier → gog (Google OAuth direto)

## Motivo

Zapier MCP esgotou todas as tasks das 3 instâncias (erro 402 Payment Required), bloqueando acesso dos agentes a Google Drive, Gmail e YouTube.

Jadielson decidiu: **"NÃO. NÃO VAMOS DEPENDER DO ZAPIER."**

## Decisão

✅ Cancelar dependência do Zapier para acesso a Google APIs
✅ Migrar para autenticação OAuth direta via `gog` (Google CLI)
✅ Manter Zapier apenas se for estritamente necessário no futuro

## Implementação

1. **Ferramenta:** `gog` v0.21.0 (já instalado via brew)
2. **Script central:** `scripts/gog-auth.sh`
3. **Contas autenticadas:**
   - davijadielson@gmail.com (pessoal) — ✅ Drive + Gmail + Calendar
   - logikacreative.mkt@gmail.com (Lógika) — ✅ Drive + Gmail + Calendar
   - loh.open.logika@gmail.com (Lôh) — ✅ pendente de reautenticação
4. **Escopos:** Drive readonly, Gmail modify, Calendar, Docs, Sheets
5. **Reauth flow:** OAuth2 via Google — Jadielson autorizou pessoalmente

## Resultados dos testes

- ✅ `gog_drive pessoal inventory` — 10 pastas raiz visíveis
- ✅ `gog_drive logika inventory` — 5 pastas visíveis
- ✅ `gog_gmail pessoal list 10` — emails recentes OK
- ✅ `gog_gmail logika list 5` — emails recentes OK

## Próximos passos

- [ ] Reautenticar conta loh.open.logika@gmail.com
- [ ] Atualizar comandos `/drive-recente`, `/drive-buscar`, `/drive-arquivo` para usar gog
- [ ] Remover ou desabilitar Zapier MCP das skills
- [ ] Documentar para todos os agentes como usar gog