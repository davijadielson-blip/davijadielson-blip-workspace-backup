# Mission Control Web v1.2 — Aging comercial

**Data:** 2026-07-20 01:37 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Pedido

Jadielson pediu para avançar após o agendamento do snapshot diário.

## Entrega

Foi criada a visão de **aging comercial** no CRM da Lógika dentro do Mission Control.

## O que o aging mede

1. Dias desde o último contato registrado no pipeline.
2. Tarefas abertas atrasadas e quantidade de dias de atraso.
3. Nível de risco comercial por lead.

## Regras de risco por contato

- `Crítico`: 120 dias ou mais sem contato.
- `Alto`: 60 a 119 dias sem contato.
- `Atenção`: 30 a 59 dias sem contato.
- `OK`: menos de 30 dias.
- `Sem contato`: sem data registrada.

## Resultado atual

Resumo via Notion API direta:

- Pipeline: 7 itens.
- Valor pretendido: R$ 203.000.
- Valor fechado: R$ 35.000.
- Tarefas abertas: 6.
- Leads com aging crítico: 7.
- Leads com tarefas atrasadas: 2.

## Principais alertas

1. Guilherme — Crítico — 683 dias sem contato — tarefa 857 dias atrasada — Em Negociação.
2. Gustavo — Crítico — 683 dias sem contato — tarefa 843 dias atrasada — Lead.
3. test — Crítico — 850 dias sem contato — Lead.
4. Jonathan — Crítico — 683 dias sem contato — Contactado.
5. Kim Wayn — Crítico — 683 dias sem contato — Proposta Enviada.
6. Gilberto — Crítico — 683 dias sem contato — Contactado.
7. João — Crítico — 683 dias sem contato — Fechado.

## Alterações no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos alterados:

- `lib/notionClient.js`
- `components/CrmPanel.jsx`
- `app/globals.css`
- `scripts/snapshot-logika-crm.mjs`

## Testes

- `npm run build`: OK.
- Consulta direta Notion API: OK.
- `npm run snapshot:crm`: OK.

## Impacto operacional

O Mission Control agora aponta leads em risco, não apenas tarefas. Isso permite priorizar recuperação comercial e higiene do CRM.

## Próximos passos recomendados

1. Criar seção “Higiene CRM” para tarefas sem data e contatos muito antigos.
2. Criar rotina de atualização de datas no Notion.
3. Criar botão/ação futura para gerar mensagem de follow-up por lead.
