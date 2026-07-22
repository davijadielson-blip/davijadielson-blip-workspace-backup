---
tema: proatividade segura e briefing diário
conteudo: estado atual do heartbeat, regras de proatividade, formato do briefing diário, crons, itens de verificação
nicho: ecossistema agêntico Lôh/Jadielson
setor: operações agentivas
cliente: Jadielson Davi
tipo: heartbeat/proatividade
prioridade: alta
atualizado_em: 2026-07-22
usar_quando: verificar o que fazer em heartbeats, formato do briefing diário, regras de proatividade
nao_usar_quando: consulta de contexto ou decisões (MEMORY.md) ou mapa do workspace (MAPA.md)
---

# HEARTBEAT.md — Proatividade segura da Lôh

Atualizado em: 2026-07-20
Autorizado por: Jadielson Davi

## Estado atual

O briefing automático diário está ativo via cron externo, não por heartbeat direto deste arquivo.

- Cron: `Briefing diário da Lôh — 6h`
- ID: `6c8ab852-c6d5-48b1-8bc5-dcfb77a8a7d1`
- Horário: todos os dias às 06:00
- Timezone: `America/Maceio`
- Entrega: Telegram direto para Jadielson

## Regra de proatividade

Proatividade deve ser útil, curta e baseada em evidência. Não virar spam.

## Briefing diário — formato

Até 5 itens:

1. Prioridade principal.
2. Prazo ou risco.
3. Pendência parada.
4. Oportunidade percebida.
5. Próximo passo sugerido.

Se não houver nada relevante: dizer brevemente que o dia está tranquilo.

## Fontes obrigatórias do briefing

Antes de gerar briefing, consultar:

- `CONSTITUICAO.md`
- `MAPA.md`
- `USER.md`
- `MEMORY.md` quando apropriado
- `[F2] memory/context/HOT-Loh-operacional.md`
- decisões recentes em `[F2] memory/decisions/`
- outputs recentes em `[F2] memory/outputs/`
- projetos/frentes relevantes em `[F1] 5-Frentes/` e `[F3] PROJETOS/`

## Anti-spam

Não interromper se:

- não houver novidade relevante;
- a informação não foi verificada;
- for apenas confirmação vazia;
- puder esperar o briefing seguinte;
- envolver ação externa não autorizada.

## Limites

- Não alterar arquivos raiz durante briefing automático.
- Não enviar mensagens externas em nome de Jadielson.
- Salvar apenas `.md` no Cofre quando houver algo realmente pertinente.
- Em caso de dúvida, registrar pendência e pedir confirmação no próximo contato.
