# 🗂️ Google Drive — Acesso dos Agentes

**Última atualização:** 2026-07-07
**Status:** ✅ Autenticação direta via `gog` (Zapier descontinuado)

---

## Como funciona

Os agentes agora acessam Drive, Gmail e Calendar via **`gog`** — uma CLI Go que autentica direto no Google OAuth, sem depender do Zapier.

## Contas autenticadas

| Apelido | Email | Escopos | Status |
|---|---|---|---|
| `pessoal` | davijadielson@gmail.com | Drive(readonly), Gmail(modify), Calendar, Docs, Sheets | ✅ |
| `logika` | logikacreative.mkt@gmail.com | Drive(readonly), Gmail(modify), Calendar, Docs, Sheets | ✅ |
| `loh` | loh.open.logika@gmail.com | Drive(readonly), Gmail(modify), Calendar, Docs, Sheets | ✅ |

## Script de autenticação

**Local:** `scripts/gog-auth.sh`

**Uso por agentes:**
```bash
source scripts/gog-auth.sh

# Drive - listar inventário
gog_drive pessoal inventory --max 20

# Drive - buscar arquivos
gog_drive logika search "termo"

# Drive - ler conteúdo de arquivo
gog_drive pessoal cat <file-id>

# Gmail - listar emails recentes
gog_gmail pessoal list 10

# Calendar - ver agenda
gog_calendar pessoal list --days 7
```

## Segurança

- Senha do keyring em: `scripts/.secrets/gog-keyring-password` (modo 600)
- Agentes usam `--gmail-no-send` para bloquear envio acidental
- Escopo Drive é **readonly** por segurança
- Gmail é **modify** (pode ler, arquivar, mas enviar requer permissão explícita)

## Histórico

| Data | Evento |
|---|---|
| 2026-07-07 | 🔴 Zapier esgotou tasks (402 Payment Required) |
| 2026-07-07 | 🟢 Migração para `gog` completa |
| 2026-07-07 | ✅ davijadielson@gmail.com reautenticado |
| 2026-07-07 | ✅ logikacreative.mkt@gmail.com reautenticado |