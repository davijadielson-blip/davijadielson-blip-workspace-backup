---
tema: consolidacao dos pilares editoriais da Saude Sao Sebastiao na skill v1.3.1
conteudo: resumo do fechamento operacional sobre mapa de pilares, alternancia do quinto e sexto pilar, stories mesclados e aplicacao da skill no runtime Logika
setor: comunicacao institucional
cliente: Saude Sao Sebastiao
tipo: registro operacional
prioridade: alta
atualizado_em: 2026-08-08
usar_quando: consultar o que foi consolidado na skill de comunicacao da Saude apos validacao de Jadielson
nao_usar_quando: substituir a leitura da skill ativa ou das regras detalhadas de rotacao e mesclagem
---

# Consolidacao — pilares editoriais e skill v1.3.1

## Origem

Conversa no Telegram, topico **SAUDE - SAO SEBASTIAO**, em 2026-08-08.

Jadielson validou o mapa geral de pilares da Secretaria e pediu para salvar e consolidar dentro da skill do agente de comunicacao da Saude.

## Decisoes consolidadas

1. Os pilares gerais da Secretaria para comunicacao editorial sao:
   - Atencao Basica / Territorio;
   - Servicos Especializados / Diagnostico;
   - Vigilancia / Prevencao;
   - Rede de Apoio / Humanizacao;
   - Urgencia / Servico;
   - Bastidores / Prestacao de Contas;
   - Campanhas Mensais / Datas de Saude como eixo transversal.
2. Como a proposta operacional e produzir de segunda a sexta, o quinto e o sexto pilar devem se alternar para manter equilibrio editorial:
   - Urgencia / Servico;
   - Bastidores / Prestacao de Contas.
3. Mesmo quando houver protagonista claro no feed ou Reels, os stories devem alternar entre setores, servicos, rotinas ou angulos do mesmo pilar, evitando monotonia diaria.
4. A pauta diaria deve puxar primeiro o pilar do dia, depois definir protagonista do feed, depois abrir os stories com mesclagem interna do pilar.

## Aplicacao realizada

- Regra operacional atualizada no Cofre:
  `50-clientes/10-saude-sao-sebastiao/30-entregas/outputs-f2/sistema-producao/2026-07-13-regra-rotacao-mesclagem-pilares.md`
- Skill aplicada no runtime Logika:
  `70-agentes/runtime/logika/skills/saude-sao-sebastiao-comunicacao-v1-3-1-pilares/SKILL.md`
- Nome da skill ativa no runtime:
  `saude-sao-sebastiao-comunicacao-v1-3-1-pilares`

## Status

Consolidado e aplicado no runtime do agente Logika em 2026-08-08.

Observacao: a skill global legada em `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao` continua existindo como fonte historica; a versao aplicada pelo Skill Workshop ficou ativa no runtime do agente com sufixo `v1-3-1-pilares`.
