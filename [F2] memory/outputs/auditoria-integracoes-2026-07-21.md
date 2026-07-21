# Auditoria de Integrações — 2026-07-21

> Realizada por: Lôh (Orquestradora Tier 0)
> Fontes: Cofre (CONSTITUICAO.md, MAPA.md, AGENTS.md, .env, scripts/, cron jobs do Gateway, testes diretos de API)

---

## 🔵 INTEGRAÇÕES FUNCIONAIS

### 1. ✅ Telegram — OK
- Onipresença em todos os grupos e tópicos
- 39 cron jobs ativos com delivery via Telegram
- Entrega de briefings diários, lembretes, pautas e alertas
- Último commit de backup do workspace: 2026-07-21 01:49

### 2. ✅ Miro — OK
- Token funcional (Status 200)
- 3 boards detectadas: FLUXOGRAMAS, PROJETOS E ESTUDOS, MAPA 360
- Script `scripts/miro.py` operacional
- **Uso restrito** ao Jack Lemley e tópicos do GRUPO PROJETOS

### 3. ✅ Notion — OK
- Token funcional (Status 200, autenticado como "Loh-bot")
- Sync Notion → Google Calendar rodando via cron diário às 10h
- Scripts Python em `scripts/notion/` para calendário da Saúde

### 4. ✅ GitHub (workspace) — OK
- Backup incremental a cada 30min via Gateway cron
- Último commit: `2de93e5 backup: incremental 2026-07-21-0149`
- Remote: `davijadielson-blip-workspace-backup.git`

### 5. ✅ GitHub (segundo-cérebro) — OK
- Repositório clonado em `/data/.openclaw/segundo-cerebro-jadielson/`
- Remote: `segundo-cerebro-jadielson.git`
- Último commit: `d44d56d docs: reforça fallback de consulta ao Cofre`

### 6. ✅ Mission Control — OK
- Snapshot diário do CRM Lógika rodando às 08h
- Revisão semanal comercial às segundas 08:30
- HTMLs gerados: mission-control.html, mc-agents.html, mc-projects.html, etc.

### 7. ✅ Cron Jobs do Gateway — OK
- 39 jobs registrados, todos com status "ok"
- Destaques: Briefing diário 6h, Pauta Saúde 6h/21h, Backup 30min, Save Deltas 1h, Extração de Decisões, PG/PD 20h30, Lembretes de aniversário, Manutenção semanal

---

## 🟡 INTEGRAÇÕES COM RESSALVAS

### 8. ⚠️ gog (Google) — Parcial
- **gog instalado:** ✅ `/home/linuxbrew/.linuxbrew/bin/gog`
- **Conta pessoal (davijadielson@gmail.com):** ✅ Autenticada, escopos calendar + drive
- **Conta Lógika (logikacreative.mkt@gmail.com):** ✅ Autenticada, escopos docs + drive + forms + sheets
- **Conta Lôh (loh.open.logika@gmail.com):** ❌ **NÃO aparece** no auth list — não autenticada ou não registrada
- **GOG_KEYRING_PASSWORD:** ⚠️ Não está setada como variável de ambiente global. O script `gog-auth.sh` lê de um arquivo `.secrets/gog-keyring-password`, mas o CLI `gog` direto não funciona sem a env var em modo não-interativo.
- **Shell compatível:** ⚠️ `source scripts/gog-auth.sh` falha porque o shell padrão é `sh`, não `bash`

### 9. ⚠️ Segundo-cérebro desatualizado — Parcial
- Vault sincronizado, mas arquivos raiz divergem do workspace
- `AGENTS.md`, `HEARTBEAT.md`, `IDENTITY.md`, `MAPA.md`, `MEMORY.md`, `SOUL.md`, `TOOLS.md` — todos diferentes
- `CONSTITUICAO.md` — não existe no vault (criada após última sincronização)
- Symlinks `F0-Inbox`, `F2-agentes`, `F2-archive`, `F2-memory`, `F3-Projetos` — só existem no workspace

### 10. ⚠️ TOOLS.md — Vazio
- Arquivo é template, sem configurações preenchidas (câmeras, SSH, preferências)

### 11. ⚠️ Telegram state — Vazio
- `scripts/state/telegram-state.json` = `{}` — sem estado registrado

---

## 🔴 INTEGRAÇÕES QUEBRADAS / REMOVIDAS

### 12. ❌ memory_search (OpenAI Embeddings) — Quebrado
- Chave API OpenAI retorna **401 — Invalid API Key**
- `memory_search` completamente offline
- Fallback manual por `read`/`find`/`grep` funciona, mas embeddings não indexam
- **Impacto:** busca semântica em todo o Cofre indisponível

### 13. ❌ Zapier — Removido (mas resíduo técnico)
- **Decisão de Jadielson/Lôh:** removido do ecossistema operacional
- 6 decisões registradas entre 07/07 e 20/07/2026
- **Mas:** 3 MCPs Zapier ainda estão disponíveis como ferramentas na sessão: `zapier-1`, `zapier-3`, `zapier-youtube`
- Arquivo de decisão `2026-07-20-remocao-total-zapier-gog-oficial.md` está **vazio (0 bytes)**
- Crontab do sistema também vazio

### 14. ❌ Scripts shell com `source` — Incompatível
- `gog-auth.sh` usa `source` que não funciona em `sh` (só em `bash`)
- Necessário usar `. scripts/gog-auth.sh` (ponto) em vez de `source`

---

## 📋 RECOMENDAÇÕES

### Prioridade Alta
1. **Corrigir chave OpenAI** — renovar API key para restaurar `memory_search`
2. **Autenticar conta Lôh no gog** — `loh.open.logika@gmail.com` precisa ser adicionada
3. **Configurar GOG_KEYRING_PASSWORD** como env var global no container
4. **Remover ou desabilitar MCPs Zapier** — já que a decisão foi removê-los

### Prioridade Média
5. **Sincronizar segundo-cérebro** — copiar nova estrutura do workspace para o vault
6. **Corrigir arquivo de decisão vazio** — preencher `2026-07-20-remocao-total-zapier-gog-oficial.md`
7. **Preencher TOOLS.md** com configurações reais do ambiente
8. **Migrar scripts `source` para `.`** nos shells ou garantir bash

### Prioridade Baixa
9. **Preencher telegram-state.json** com estado real
10. **Revisar cron jobs duplicados** — há briefings tanto no `daily-brief.sh` (script) quanto no Gateway (cron); verificar se não há conflito

---

*Fonte: Cofre — CONSTITUICAO.md, MAPA.md, AGENTS.md, .env, scripts/, cron jobs Gateway, testes diretos de API (Miro, Notion, gog, OpenAI)*