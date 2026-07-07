---
tipo: correcao-cron
frente: saude-sao-sebastiao-social-media
criado_em: 2026-07-06
solicitante: Jadielson Davi
chat_origem: telegram:-1003645702069
topic_id: 3672
topic_name: SAÚDE - SOCIAL MEDIA
---

# Correção dos crons — fuso Maceió, próximo dia correto e Lôh no privado

Jadielson apontou erro no lembrete das 21h: em 06/07 segunda-feira, o lembrete deveria trazer a pauta de terça 07/07, não quarta 08/07. A causa provável foi cálculo de “amanhã” pela data UTC em vez da data local de Maceió.

## Correções aplicadas

### 1) Regra de data local
Os prompts dos crons agora mandam calcular a data usando `America/Maceio`, não UTC.

Exemplo explícito incluído no cron das 21h:
- Se em UTC já for madrugada do dia seguinte, mas em Maceió ainda for segunda 06/07 às 21h, então amanhã é terça 07/07.

### 2) Entrega no chat individual de Jadielson
Os crons foram recriados/ajustados para entregar no privado Telegram de Jadielson (`7654417048`) em vez do tópico Saúde.

### 3) Lôh como agente responsável
Os novos jobs foram configurados com `agentId: loh`.

## Jobs atuais

### 06h — pauta do dia
- Job ID: `888d851b-658e-48b1-9acd-45f5d248292e`
- Nome: `LÔH — SAÚDE Social Media — pauta completa do dia às 06h`
- Agenda: `0 6 * * *`, timezone `America/Maceio`
- Entrega: Telegram privado de Jadielson (`7654417048`)
- Formato: textos finais de publicação em blocos copiáveis; informações operacionais em texto normal.

### 21h — pauta do próximo dia
- Job ID: `4cf67e57-3648-46fe-890c-be88abeab892`
- Nome: `LÔH — SAÚDE Social Media — pauta do próximo dia às 21h`
- Agenda: `0 21 * * *`, timezone `America/Maceio`
- Entrega: Telegram privado de Jadielson (`7654417048`)
- Formato: texto normal, sem blocos copiáveis, para ciência e preparação.

## Jobs antigos removidos
- `01cfd4e8-072e-422e-bd06-79472c3060f2`
- `35477be2-2d51-45a9-8c42-1fd30d62722c`
