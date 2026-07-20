# Mission Control Web MVP v0.7 — CRM operacional com KPIs

**Data:** 2026-07-20 01:18 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Pedido

Jadielson autorizou avançar após conexão do Notion API.

## O que faltava

Após a v0.6, ainda faltava transformar a conexão bruta em leitura operacional útil:

1. Mapear campos reais do template CRMaster.
2. Ler `Status` do tipo Notion `status`.
3. Exibir valor de pipeline, valor fechado, tarefas pendentes e último contato.
4. Gerar resumo comercial para o Mission Control.

## Entrega v0.7

O painel CRM agora mostra:

- total de itens no pipeline;
- valor total pretendido do pipeline;
- valor fechado;
- total de tarefas pendentes;
- contagem por status agrupado;
- cards reais com status, valor, último contato, telefone/e-mail quando disponíveis;
- link para abrir o item no Notion.

## Resultado lido da Notion API

`Conectado via Notion API — 7 itens`

Resumo calculado:

- Total: 7 itens
- Pipeline: R$ 203.000
- Fechado: R$ 35.000
- Tarefas pendentes: 6

Status agrupados:

- Lead: 2
- Contato: 2
- Negociação: 1
- Proposta: 1
- Fechado: 1

Exemplos:

- test — Lead
- Jonathan — Contactado — R$ 22.000
- Guilherme — Em Negociação — R$ 32.000 — 3 tarefas pendentes
- Kim Wayn — Proposta Enviada — R$ 37.000 — 2 tarefas pendentes
- Gilberto — Contactado — R$ 35.000

## Arquivos alterados

No app fora do Cofre:

- `lib/notionClient.js`
- `components/CrmPanel.jsx`
- `app/globals.css`

## Testes

- Consulta direta ao cliente Notion: OK.
- `npm run build`: OK.

## Observações de segurança

- Token Notion permanece fora do Cofre.
- O Cofre registra apenas IDs operacionais e status, não segredos.
- O frontend recebe apenas dados comerciais normalizados.

## Próximos passos recomendados

1. Criar visão de alerta: leads com tarefa pendente e último contato antigo.
2. Integrar tarefas do database `Tarefas` para detalhar próximas ações reais.
3. Definir rotina semanal de revisão comercial da Lógika no Mission Control.
