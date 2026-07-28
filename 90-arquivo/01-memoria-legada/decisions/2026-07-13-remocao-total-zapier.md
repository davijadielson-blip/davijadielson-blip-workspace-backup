---
tipo: decisao
data: 2026-07-13
status: implementado
fonte: Lôh + Jadielson
assunto: Remoção total do Zapier MCP do ecossistema
---

# Decisão — Remoção total do Zapier MCP

## Motivo

Agentes continuavam tentando usar Zapier para acessar Google (Drive, Gmail, Calendar, Sheets) mesmo após a desativação parcial em 07/07. Jadielson determinou: **remover Zapier completamente do ecossistema**.

## O que foi feito

### 1. Remoção dos MCP Servers
Todos os 5 servidores Zapier foram removidos do `openclaw.json`:

| Server | Ação |
|--------|------|
| 🔴 canva-zapier | Removido |
| 🔴 zapier-1 | Removido |
| 🔴 zapier-2 | Removido |
| 🔴 zapier-3 | Removido |
| 🔴 zapier-youtube | Removido |

### 2. Acesso ao Google agora
- **Google Drive** → `gog_drive` (autenticação direta)
- **Gmail** → `gog_gmail` (autenticação direta)
- **Google Calendar** → Acesso nativo do sistema / gog
- **YouTube** → Acesso direto via web/browser
- **Facebook/Instagram** → Acesso direto via web/browser

### 3. Regras propagadas para o ecossistema

> **🚫 ZAPIER ESTÁ OFICIALMENTE DESATIVADO. NENHUM AGENTE DEVE TENTAR USÁ-LO.**
> - Ferramentas do Zapier (zapier-1__*, zapier-3__*, zapier-youtube__*, canva-zapier__*) não estão mais disponíveis
> - Se um agente tentar chamar uma ferramenta Zapier, vai receber erro — e deve imediatamente buscar alternativa direta
> - Para Google: use `gog` (gog_drive, gog_gmail, etc.)
> - Para web: use web_search / tavily / browser

### 4. Arquivos atualizados
- [x] `openclaw.json` — servidores MCP Zapier removidos
- [x] `MEMORY.md` — regra propagada
- [x] `AGENTS.md` — regra propagada (se necessário)
- [x] `[F2] memory/context/integracoes/` — sinalizado
- [x] Gateway reload (secrets reload) aplicado

Fonte: Decisão Jadielson, 2026-07-13.