---
tema: 07 20 cron snapshot diario crm v11
atualizado_em: 2026-07-22
---

# Mission Control Web v1.1 — Cron diário do Snapshot CRM Lógika

**Data:** 2026-07-20 01:31 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** agendado

## Contexto

Jadielson autorizou continuidade sem necessidade de aprovação a cada etapa. A próxima etapa natural após o snapshot manual era automatizar a geração diária.

## Entrega

Foi criado um cron diário para executar o snapshot comercial da Lógika automaticamente.

## Job

- Nome: `Mission Control — snapshot diário CRM Lógika`
- Job ID: `a07badd8-d064-4fd8-963d-00f2a9dcbab4`
- Frequência: todos os dias às 08:00
- Timezone: `America/Bahia`
- Execução: sessão isolada
- Entrega: anúncio no Telegram do Jadielson

## O que o job faz

1. Consulta a Constituição do Cofre.
2. Acessa o app em `/data/.openclaw/mission-control-next`.
3. Executa `npm run snapshot:crm`.
4. Lê o snapshot gerado no Cofre.
5. Resume:
   - pipeline;
   - valor pretendido;
   - valor fechado;
   - tarefas abertas;
   - ações atrasadas.
6. Não expõe token.

## Arquivo de saída esperado

`[F2] memory/outputs/logika/crm/YYYY-MM-DD-snapshot-crm-logika.md`

## Observação de segurança

O token Notion permanece fora do Cofre, em `.env.local` do app. O cron apenas aciona a rotina já implementada.

## Próximo avanço recomendado

Criar uma visão de **aging comercial**: leads sem contato recente e tarefas atrasadas por dias de atraso.
