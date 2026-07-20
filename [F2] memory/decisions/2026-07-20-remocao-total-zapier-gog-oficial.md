# Decisão — remoção total do Zapier; `gog` oficial

**Data:** 2026-07-20  
**Decisor:** Jadielson Davi  
**Status:** vigente

## Decisão

Jadielson determinou: **remover de vez o Zapier do ecossistema operacional**, porque voltou a atrapalhar os briefings/integrações. A integração Google roda bem via **`gog`**, que permanece como caminho oficial.

## Ação executada

Foram desativadas as ações habilitadas nos servidores Zapier disponíveis:

- Gmail;
- Google Calendar;
- Google Drive;
- Notion;
- Miro.

Verificação posterior indicou que os servidores Zapier consultados ficaram sem apps/actions habilitados.

## Regra operacional

- Não usar Zapier MCP para Google, Notion, Miro, YouTube ou qualquer integração operacional.
- Não habilitar, reprovisionar, descobrir ações ou sugerir Zapier sem autorização explícita posterior de Jadielson.
- Se algum briefing ou rotina citar “Zapier” como fonte, considerar falha de procedimento e corrigir para fonte direta.

## Caminhos oficiais/alternativos

- Google Drive → `gog_drive` ou scripts diretos.
- Gmail → `gog_gmail` ou scripts diretos.
- Google Calendar → `gog_calendar` ou scripts diretos do Cofre.
- Google Sheets → `gog`/scripts diretos com OAuth Google.
- Notion/outros sistemas → API direta, MCP específico, CLI ou scripts locais.
- Busca externa → Tavily/Pesquisador primeiro após Cofre.

## Arquivos atualizados

- `MEMORY.md`
- `AGENTS.md`
- `TOOLS.md`
- Este registro em `[F2] memory/decisions/2026-07-20-remocao-total-zapier-gog-oficial.md`
