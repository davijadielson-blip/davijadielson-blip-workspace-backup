---
tema: 07 20 notion tarefas integradas v08
atualizado_em: 2026-07-22
---

# Mission Control Web MVP v0.8 — Tarefas Notion integradas ao CRM

**Data:** 2026-07-20 01:22 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Pedido

Jadielson autorizou seguir após a v0.7 do CRM operacional.

## Entrega

O Mission Control agora integra o database **Tarefas** do CRMaster ao painel CRM da Lógika.

## Database integrado

- Nome: `Tarefas`
- ID: `1a4207e6f14583ec951881e4faf11a56`

## Campos mapeados

- `Name` — título da tarefa.
- `Status` — fórmula/status textual.
- `Data Final` — prazo.
- `Feito?` — checkbox de conclusão.
- `Contato` — relação com o item do pipeline.

## Resultado do teste

Consulta via Notion API direta:

- Pipeline: 7 itens.
- Tarefas: 8 itens.
- Tarefas abertas associadas: 6.

### Leads com tarefas abertas

- Guilherme:
  - Nova Tarefa — Dentro do Prazo
  - Follow Up — Atrasado — 2024-03-15
  - Follow Up — Dentro do Prazo
- Kim Wayn:
  - Follow Up — Dentro do Prazo
  - Follow Up — Dentro do Prazo
- Gustavo:
  - Enviar Proposta — Atrasado — 2024-03-29

## Alterações no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos alterados:

- `lib/notionClient.js`
- `components/CrmPanel.jsx`
- `app/globals.css`

## O que mudou no dashboard

- Cards de lead agora mostram próximas tarefas reais quando houver.
- O KPI mudou de “tarefas pendentes” para “tarefas abertas”.
- Tarefas são associadas ao lead por relação Notion.
- Tarefas concluídas não entram como abertas.

## Testes

- Consulta direta ao cliente Notion: OK.
- `npm run build`: OK.

## Próximos passos recomendados

1. Criar alerta visual forte para tarefas atrasadas.
2. Criar seção “Ações comerciais de hoje”.
3. Criar ordenação por urgência: atrasadas > sem data > próximas.
4. Registrar rotina semanal comercial da Lógika no Mission Control.
