---
tema: configurações locais de ferramentas e dispositivos
conteudo: câmeras, logins locais, chaves SSH, preferências de voz, comandos específicos do setup
nicho: ecossistema agêntico Lôh/Jadielson
setor: operações técnicas
cliente: Jadielson Davi
tipo: configuração/tools
prioridade: alta
atualizado_em: 2026-09-05
usar_quando: consultar detalhes de dispositivos, câmeras, chaves SSH ou preferências de ferramentas
nao_usar_quando: regras operacionais (AGENTS.md) ou mapa do workspace (MAPA.md)
---

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
## Integrações — `gog` oficial; Zapier removido

Decisão de Jadielson/Lôh: **Zapier não deve mais ser usado no ecossistema operacional**.

Para Google, use `gog` e scripts diretos:

- Google Drive: `gog_drive`
- Gmail: `gog_gmail`
- Google Calendar: `gog_calendar` ou scripts do Cofre
- Google Sheets: `gog`/scripts diretos com OAuth

Antes de qualquer operação Google, carregar ambiente quando necessário:

```bash
cd /data/.openclaw/workspace
source scripts/gog-auth.sh
```

Proibido reabilitar, reprovisionar ou sugerir Zapier sem autorização explícita posterior de Jadielson.

Decisão: `[F2] memory/decisions/2026-07-20-remocao-total-zapier-gog-oficial.md`

## Integrações — Notion com escopos separados

O ambiente tem duas integrações Notion oficiais, com escopos separados:

- `MAPA 360`: painel pessoal/estratégico e camada visual do Cofre.
- `Loh-bot`: produção/editorial da LÓGIKA no workspace `LÓGIKA CREATIVE`.

Arquivos locais de segredo:

- `scripts/.secrets/notion.env` — token do `MAPA 360`.
- `scripts/.secrets/notion-logika-producao.env` — token do `Loh-bot`, base `Produção & Agenda - LÓGIKA`.

Antes de qualquer operação Notion por script, carregar:

```bash
cd /data/.openclaw/workspace
source scripts/notion-env.sh
```

Base oficial de produção/editorial:

- Nome: `Produção & Agenda - LÓGIKA`
- ID: `375207e6-f145-8111-bba0-e132fd820542`
- Integração: `Loh-bot`
- Variáveis disponíveis aos agentes: `NOTION_LOGIKA_TOKEN`, `NOTION_PRODUCAO_DATABASE_ID`, `NOTION_API_VERSION`

Segurança:

- Nunca registrar tokens em Markdown, respostas, relatórios ou logs.
- Registrar apenas status, caminho seguro, bot/workspace, database e resultado dos testes.
- Para sync com Calendar, usar a skill `source-command-sync-notion-calendar` e validar leitura antes de criar/atualizar eventos.

## Integrações — xTiles conectado

Validado em 2026-09-05: a sessão da Lôh consegue acessar o xTiles via conector `mcp__codex_apps__xtiles`.

Workspace disponível:

- `personal` — `My workspace`

Projetos vistos no teste:

- `MATRIZ`
- `Estudos e Projetos - Minha Rotina Organizada -`
- `Casa - Minha Rotina Organizada`
- `Dia a Dia-JADIELSON - Minha Rotina Organizada --copy`
- `Lógika Finanças - Minha Rotina Organizada`
- `Saúde - Minha Rotina Organizada`
- `Finanças - Minha Rotina Organizada`
- `ARCO+ Framework`

Operações disponíveis:

- listar workspaces e projetos;
- ler conteúdo de projeto, página/view e planner;
- criar projeto ou página/view a partir de Markdown;
- criar tiles em uma view existente a partir de Markdown;
- criar, listar, ler e atualizar tarefas;
- montar um projeto visual virtual a partir de informação solta.

Governança:

- Não excluir tarefas ou conteúdo sem confirmação explícita de Jadielson.
- Para arquitetura do Backlog Inteligente, manter a regra registrada no Cofre: xTiles como cockpit visual/operacional humano; Cofre como fonte de verdade; Google Calendar como camada de tempo.
