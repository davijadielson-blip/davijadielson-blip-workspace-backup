---
tema: 07 20 acoes comerciais hoje v09
atualizado_em: 2026-07-22
---

# Mission Control Web MVP v0.9 — Ações comerciais de hoje

**Data:** 2026-07-20 01:26 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Pedido

Jadielson aprovou avançar após a integração das tarefas Notion ao CRM.

## Entrega

Foi criada a seção **Ações comerciais de hoje** no painel CRM do Mission Control.

## Lógica de prioridade

As tarefas abertas são ordenadas automaticamente por urgência:

1. **Atrasada** — status contém `Atrasado` e não está concluída.
2. **Sem data** — tarefa aberta sem prazo definido.
3. **Próxima** — tarefa aberta com data futura/definida.

A ordenação secundária usa data e nome do lead.

## Resultado atual

Consulta via Notion API direta:

`Conectado via Notion API — 7 itens`

Ações comerciais abertas: 6.

### Prioridade atual

1. Atrasada — Guilherme — Follow Up — 2024-03-15 — Em Negociação
2. Atrasada — Gustavo — Enviar Proposta — 2024-03-29 — Lead
3. Sem data — Guilherme — Nova Tarefa — Em Negociação
4. Sem data — Guilherme — Follow Up — Em Negociação
5. Sem data — Kim Wayn — Follow Up — Proposta Enviada
6. Sem data — Kim Wayn — Follow Up — Proposta Enviada

## Alterações no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos alterados:

- `lib/notionClient.js`
- `components/CrmPanel.jsx`
- `app/globals.css`

## Testes

- Consulta direta ao cliente Notion: OK.
- `npm run build`: OK.

## Valor operacional

Agora Jadielson consegue abrir o Mission Control e ver não apenas o pipeline, mas também **o que atacar primeiro comercialmente**.

## Próximos passos recomendados

1. Criar comando/rotina diária: “me diga as ações comerciais de hoje”.
2. Criar destaque visual por atraso e aging de último contato.
3. Criar sincronização/registro semanal no Cofre com resumo comercial.
