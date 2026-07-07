---
tipo: consolidado-operacional
frente: saude-sao-sebastiao-social-media
criado_em: 2026-07-07T02:49:00Z
solicitante: Jadielson Davi
chat_origem: telegram:-1003645702069
topic_id: 3672
topic_name: SAÚDE - SOCIAL MEDIA
status: salvo
---

# Consolidado — Lembretes automáticos e ajustes da pauta Saúde Social Media

## Contexto
Jadielson solicitou configurar lembretes automáticos para receber diariamente a pauta da Saúde São Sebastião, com base no calendário editorial já debatido e salvo no Cofre.

## Decisão final de operação

### Responsável pelo envio
- Os lembretes devem ser enviados pela **Lôh**.
- Entrega preferencial: **chat individual de Jadielson**, não o tópico coletivo.

### Fuso correto
- Todos os lembretes devem considerar o fuso **America/Maceio**.
- O lembrete das 21h deve calcular o “amanhã” pela data local de Maceió, não pela data UTC.
- Exemplo corrigido: segunda-feira 06/07 às 21h em Maceió → pauta de terça-feira 07/07, nunca quarta 08/07.

## Crons finais configurados

### 1) LÔH — pauta completa do dia às 06h
- Job ID: `888d851b-658e-48b1-9acd-45f5d248292e`
- Agenda: todos os dias às 06h
- Timezone: `America/Maceio`
- Expressão cron: `0 6 * * *`
- Agente: `loh`
- Entrega: Telegram privado de Jadielson (`7654417048`)
- Objetivo: enviar a pauta do dia.
- Formato:
  - informações operacionais em texto normal;
  - apenas textos finais/headlines/legendas para publicação em blocos copiáveis;
  - cenas, checklist e cuidados fora dos blocos copiáveis.

### 2) LÔH — pauta do próximo dia às 21h
- Job ID: `4cf67e57-3648-46fe-890c-be88abeab892`
- Agenda: todos os dias às 21h
- Timezone: `America/Maceio`
- Expressão cron: `0 21 * * *`
- Agente: `loh`
- Entrega: Telegram privado de Jadielson (`7654417048`)
- Objetivo: enviar a pauta do dia seguinte para ciência/preparação.
- Formato:
  - texto normal;
  - sem necessidade de blocos copiáveis.

## Jobs antigos removidos
- `01cfd4e8-072e-422e-bd06-79472c3060f2`
- `35477be2-2d51-45a9-8c42-1fd30d62722c`

## Pauta de 06/07 — ajuste real de produção
Jadielson informou que, no dia 06/07, só conseguiu produzir 3 stories:

1. Story 1 permanece conforme combinado inicialmente.
2. Story 2 será um mini vídeo da recepção da **UBS Cruzeiro**, destacando que atende até as 21h.
3. Story 3 será do **ACS em campo**.

### Headline adaptada para o Story 2
```text
UBS Cruzeiro: atendimento até as 21h para cuidar melhor da população.
```

Versão alternativa mais completa:
```text
Na UBS Cruzeiro, o cuidado segue até mais tarde: atendimento disponível até as 21h para acolher melhor a população.
```

## Pauta correta do lembrete de 21h em 06/07
Como 06/07 é segunda-feira, a pauta correta para o lembrete das 21h é terça-feira, 07/07.

### 07/07 — Terça-feira — Serviços Especializados
- Tema: quando o exame ajuda a cuidar melhor.
- Serviços: Laboratório, CEO, Oftalmologia, Saúde Bucal, Odontomóvel.

### Stories previstos
1. Laboratório Municipal — quando o exame entra no cuidado, a equipe consegue orientar o próximo passo com mais segurança.
2. Coleta / Exames — exame não é só procedimento: é parte do caminho para entender o que seu corpo precisa.
3. CEO — na saúde bucal, material seguro e cuidado especializado também ajudam a proteger você.
4. Oftalmologia — quando a visão pede atenção, o cuidado especializado ajuda a enxergar melhor o caminho.
5. Odontomóvel — cuidado especializado também pode se aproximar do território para orientar e atender melhor.

### Post/feed previsto
Headline:
```text
Exames e especialidades ajudam a transformar dúvida em caminho de cuidado.
```

Legenda:
```text
Laboratório, saúde bucal especializada, oftalmologia e outros atendimentos fortalecem a rede quando ajudam a investigar e orientar cada caso. No Julho Amarelo, a mensagem continua: procure orientação antes de tirar conclusões sozinho.
```

## Fontes operacionais principais
- `[F2] memory/outputs/sms-sao-sebastiao-calendario-editorial-julho-2026-completo-f1-ancorado.md`
- `[F2] memory/outputs/saude-sao-sebastiao/2026-07-06-resumo-operacional-semana-06-a-10-julho.md`
- `[F2] memory/outputs/saude-sao-sebastiao/2026-07-06-crons-lembretes-saude-social-media.md`
- `[F2] memory/outputs/saude-sao-sebastiao/2026-07-06-ajuste-final-crons-textos-publicacao.md`
- `[F2] memory/outputs/saude-sao-sebastiao/2026-07-06-correcao-crons-loh-fuso-maceio.md`

## Cuidados permanentes
- Não expor nome, cartão, prontuário, tela, endereço, residência ou rosto de paciente sem autorização.
- Validar dados, números, fluxos, testes, vacinas e agendas antes de publicar.
- Usar linguagem institucional, humana, simples e segura.
