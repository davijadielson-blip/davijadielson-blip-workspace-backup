---
tema: memoria operacional de 2026-08-10
conteudo: registros de continuidade sobre revisao do Cofre, estrutura canonica e briefing imediato
nicho: ecossistema agentico Loh/Jadielson
setor: memoria operacional
cliente: Jadielson Davi
tipo: memoria diaria
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: recuperar contexto operacional do dia 2026-08-10
nao_usar_quando: substituir MEMORY.md ou decisoes estruturais em 00-central/decisoes.md
---

# Memoria operacional - 2026-08-10

## Revisao canonica do Cofre concluida em 2026-08-09

- Jadielson pediu para executar a otimizacao conforme `80-handoffs/prompt-loh-revisao-cofre-2026-08-09.md`.
- A revisao foi concluida e comunicada a Jadielson.
- Commit criado e enviado: `e418027 governanca: alinhar cofre a estrutura numerada`.
- Remoto confirmado em `origin/main`: `e418027bfbc922b08812c93e09451fd43dff3a87`.
- Relatorio gerado: `60-processos/relatorios/2026-08-09-revisao-canonica-cofre-estrutura-numerada.md`.
- Validacoes realizadas: `git diff --check` OK, `python3 -m py_compile` nos scripts alterados OK, 3 crons OpenClaw ativos verificados com ultimo status OK.

## Estrutura oficial atual do Cofre

Arvore canonica comunicada a Jadielson:

- `00-central/` - governanca, decisoes, regras, mapas, pendencias
- `10-pessoal/` - vida pessoal, rotina, saude, familia, inbox, tarefas
- `20-profissional/` - LOGIKA, carreira, operacao profissional
- `30-estudos/` - cursos, livros, metodos, planos, recursos
- `40-projetos/` - projetos pessoais, profissionais, autorais, produtos, ideias
- `50-clientes/` - Saude, Camara, SINDSS, vereadores e outros clientes
- `60-processos/` - checklists, rotinas, relatorios, templates, processos
- `70-agentes/` - agentes, runtime, squads, escopos, protocolos
- `80-handoffs/` - passagens formais de contexto
- `90-arquivo/` - legado, backups, duplicidades, quarentena, estrutura antiga
- `memory/` - memoria operacional ativa, sessoes, outputs, inbox externa
- `media/` - midias recebidas/referenciadas
- `scripts/` - automacoes executaveis
- `skills/` - skills ativas do workspace

Subpastas principais destacadas:

- `10-pessoal/`: `inbox`, `tarefas`, `diario`, `20-rotina-agenda`, `30-saude`, `40-financas`, `50-familia-casa`
- `40-projetos/`: `10-pessoais`, `20-profissionais`, `30-projetos-autorais`, `40-trabalho`, `50-produtos`, `ideias`
- `50-clientes/`: `10-saude-sao-sebastiao`, `20-camara-municipal`, `30-sindss`, `40-outros-vereadores`, `50-outros-clientes`
- `60-processos/`: `checklists`, `relatorios`, `rotinas`, `skills`, `templates`
- `70-agentes/`: `central-pessoal`, `logika-c-level-squad`, `runtime`
- `90-arquivo/`: `01-memoria-legada`, `02-estrutura-antiga`, `20-duplicidades`, `50-backups-snapshots`, `99-quarentena-nao-md`, `backups/`

## Pontos de atencao da revisao

- Nao houve movimentacao fisica ampla de pastas nesta etapa; a mudanca foi de governanca, mapa, agentes e scripts para nao quebrar automacoes.
- `MEMORY.md` ainda contem referencias historicas a `[F2]`, `[F3]` etc.; devem ser lidas como historico, nao como roteamento vigente.
- O papel antigo `@bibliotecaria` ainda precisa de decisao humana: renomear, arquivar ou manter como historico. Ja foi removido do `AGENTS.md` como fallback operacional.
- Havia arquivos nao rastreados fora do commit, preservados por nao pertencerem diretamente a revisao.

## Briefing imediato para 2026-08-10

- Saude Sao Sebastiao: pauta ativa de 10/08 e `Postinho em Foco / PSF` - "Equipe da familia: o medico que conhece sua historia", em formato Reels.
- LOGIKA: retomar a decisao de qual proposta comercial vem primeiro e proteger as 4 horas nobres da semana: estrategia, criacao premium, comercial e sistema/processo.
- Rotina/Nexus: comecar a semana pelo Backlog Inteligente: capturar, clarear e escolher a "Unica Coisa" do dia.
- Google Calendar nao trouxe eventos para 10/08.
- Gmail tinha e-mail importante nao lido da Acerto, de 08/08, assunto "proposta liberada para voce"; revisar sem assumir urgencia.
- Nao foram puxadas execucoes de Camara, SINDSS, vereadores, outros clientes ou projetos autorais para 10/08 porque nao havia acao prevista confirmada encontrada.
