---
tema: 07 20 rotina semanal comercial v16
atualizado_em: 2026-07-22
---

# Mission Control v1.6 — Rotina semanal comercial Lógika

**Data:** 2026-07-20 02:36 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado no Cofre e agendado

## Entrega

Foi criada a rotina semanal comercial da Lógika e agendado lembrete/revisão automática.

## Arquivo operacional

`[F2] memory/projects/mission-control/logika-crm/2026-07-20-rotina-semanal-comercial-v16.md`

## Estrutura da rotina

- Segunda: revisão e priorização.
- Terça: follow-ups de valor alto.
- Quarta: propostas e negociação.
- Quinta: higiene e reativação.
- Sexta: fechamento comercial e snapshot.

## Métricas semanais mínimas

- 3 follow-ups enviados.
- 4 tarefas sem data corrigidas.
- 2 tarefas atrasadas críticas resolvidas/reagendadas.
- 3 leads com último contato atualizado.
- 1 snapshot semanal salvo.

## Cron semanal criado

- Nome: `Mission Control — revisão semanal comercial Lógika`
- Job ID: `0b237eb2-fbaf-4c03-838e-ea56867f2472`
- Frequência: toda segunda-feira às 08:30
- Timezone: `America/Bahia`
- Entrega: Telegram do Jadielson

## Relação com snapshot diário

A rotina semanal usa o snapshot diário já agendado às 08:00 como base e roda uma revisão às 08:30 de segunda.

## Próximo avanço recomendado

Criar v1.7 — preparação de deploy/acesso estável do Mission Control, com revisão de segurança, variáveis e vulnerabilidades Next.
