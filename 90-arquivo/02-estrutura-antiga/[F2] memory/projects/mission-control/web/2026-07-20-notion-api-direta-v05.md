---
tema: 07 20 notion api direta v05
atualizado_em: 2026-07-22
---

# Mission Control Web MVP v0.5 — Notion API direta

**Data:** 2026-07-20 00:31 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** camada técnica implementada; aguardando variáveis reais de ambiente para carregar dados do CRM.

## Entrega

A integração do CRM da Lógika foi corrigida para usar **Notion API direta**, sem Zapier.

## Arquivos criados/alterados no app

Local do app:

`/data/.openclaw/mission-control-next/`

Arquivos:

- `lib/notionClient.js` — cliente server-side da Notion API.
- `app/api/logika-crm/route.js` — rota server-side para consultar CRM.
- `components/CrmPanel.jsx` — painel agora tenta carregar dados reais da Notion API.
- `app/globals.css` — estado visual de sucesso.

## Segurança

- O token Notion fica apenas no server-side.
- Nenhum token é exposto no frontend.
- A rota retorna apenas dados normalizados/resumidos.

## Variáveis necessárias

- `NOTION_TOKEN`
- `NOTION_LOGIKA_CRM_DATABASE_ID`

## Campos normalizados

O cliente tenta ler campos em português e alguns aliases:

- Nome / Name / Cliente / Lead
- Tipo / Type
- Status / Etapa / Pipeline
- Origem / Source
- Serviço de Interesse / Serviço / Interesse
- Prioridade / Priority
- Valor estimado / Valor / Value
- Próxima ação / Proxima ação / Next Action
- Data próxima ação / Data da próxima ação / Next Action Date
- Último contato / Ultimo contato / Last Contact

## Teste

`npm run build`: OK.

Rotas geradas:

- `/` estática.
- `/api/logika-crm` dinâmica server-side.

## Pendência

No ambiente atual não encontrei `NOTION_TOKEN` nem `NOTION_LOGIKA_CRM_DATABASE_ID` configurados para o app. Assim que forem definidos, o painel passa a puxar os itens reais do CRM.
