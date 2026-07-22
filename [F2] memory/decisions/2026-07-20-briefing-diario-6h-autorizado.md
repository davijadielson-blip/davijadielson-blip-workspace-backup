---
tema: 07 20 briefing diario 6h autorizado
atualizado_em: 2026-07-22
---

# Decisão — Briefing diário automático às 6h

Data: 2026-07-20
Decisor: Jadielson Davi

## Decisão

Jadielson autorizou a opção automática para briefing diário:

> “Opção automática. toda as 6hs da manha.”

## Implementação

Criado cron:

- Nome: `Briefing diário da Lôh — 6h`
- ID: `6c8ab852-c6d5-48b1-8bc5-dcfb77a8a7d1`
- Frequência: todos os dias às 06:00
- Timezone: `America/Maceio`
- Entrega: Telegram direto para Jadielson
- Modo: `isolated agentTurn`

## Regras do briefing

- Consultar Cofre obrigatoriamente antes de responder.
- Gerar briefing curto com até 5 itens:
  1. prioridade principal;
  2. prazo/risco;
  3. pendência parada;
  4. oportunidade;
  5. próximo passo sugerido.
- Se não houver nada relevante, responder brevemente que o dia está tranquilo.
- Não alterar arquivos raiz.
- Não enviar mensagens externas além do briefing.
- Salvar apenas `.md` no Cofre quando houver algo pertinente.

## Observação

Essa ativação não edita `HEARTBEAT.md`; é um cron isolado e reversível.

Fonte: autorização do usuário no chat; Cofre (`CONSTITUICAO.md`, `PROTOCOLO-HEARTBEAT-SEGURO.md`).
