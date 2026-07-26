---
tipo: configuracao-cron
frente: saude-sao-sebastiao-social-media
criado_em: 2026-07-06
solicitante: Jadielson Davi
chat: telegram:-1003645702069
topic_id: 3672
topic_name: SAÚDE - SOCIAL MEDIA
---

# Crons configurados — lembretes Saúde Social Media

Foram configurados dois lembretes automáticos para a frente Saúde São Sebastião / Social Media, entregues no tópico do Telegram **SAÚDE - SOCIAL MEDIA**.

## 1) Pauta completa do dia — 06h
- Job ID: `01cfd4e8-072e-422e-bd06-79472c3060f2`
- Nome: `SAÚDE Social Media — pauta completa do dia às 06h`
- Agenda: todos os dias às 06h, timezone `America/Maceio`
- Expressão cron: `0 6 * * *`
- Entrega: Telegram `-1003645702069`, tópico `3672`
- Conteúdo solicitado: pauta de hoje com data, tema, serviços, Story 1 a 5 com cenas e headline/legenda, Reel, Post/feed, checklist prático e cuidados de LGPD/validação.

## 2) Pauta completa do próximo dia — 21h
- Job ID: `35477be2-2d51-45a9-8c42-1fd30d62722c`
- Nome: `SAÚDE Social Media — pauta do próximo dia às 21h`
- Agenda: todos os dias às 21h, timezone `America/Maceio`
- Expressão cron: `0 21 * * *`
- Entrega: Telegram `-1003645702069`, tópico `3672`
- Conteúdo solicitado: pauta de amanhã com data, tema, serviços, Story 1 a 5 com cenas e headline/legenda, Reel, Post/feed, checklist de preparação, materiais necessários e cuidados de LGPD/validação.

## Fonte operacional principal
- `[F2] memory/outputs/sms-sao-sebastiao-calendario-editorial-julho-2026-completo-f1-ancorado.md`
- Diretórios auxiliares: `[F2] memory/context/calendarios` e `[F2] memory/outputs/saude-sao-sebastiao`

## Observações
- O pedido de Jadielson também considerou concentrar estes lembretes via Lôh e/ou visualizar a grade completa no Notion.
- A configuração atual já concentra a entrega no tópico da Saúde; para mover a governança para Lôh ou sincronizar/visualizar no Notion, é recomendável uma etapa separada de arquitetura/integração.

## Execução registrada — 2026-07-20 11:00 UTC
- Job: `3a62a8d4-bfe0-49ac-a5d6-16dd04b6782b` — Saúde Social Media — aniversário Alanderson D-2.
- Mensagem prevista ao tópico **SAÚDE - SOCIAL MEDIA**: lembrar Jadielson de preparar/confirmar arte e legenda de aniversário de Alanderson, Coordenador eMULTI, para 22/07.
