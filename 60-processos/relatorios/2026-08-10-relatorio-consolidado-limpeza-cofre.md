---
tema: relatorio consolidado da limpeza do Cofre em 2026-08-10
conteudo: consolidado das mudancas feitas na revisao canonica, etapa 2, etapa 3 e passada final de pendencias seguras
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: relatorio consolidado
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: auditar o que foi alterado na limpeza e consolidacao do Cofre em 2026-08-09/10
nao_usar_quando: substituir AGENTS.md, MAPA.md, 00-central/decisoes.md ou 00-central/pendencias.md
---

# Relatorio consolidado - limpeza do Cofre

## Escopo

Este relatorio consolida as mudancas feitas na sequencia de revisao do Cofre iniciada em 2026-08-09 e concluida em 2026-08-10, com foco em deixar a rota ativa mais clara, menos contraditoria e mais operacional.

O trabalho seguiu as diretrizes de Jadielson:

- nao apagar nada definitivamente;
- nao usar `rm`;
- mover legados para `90-arquivo/`;
- preservar rastreabilidade;
- verificar dependencias antes de mover;
- resolver no mesmo dia tudo que pudesse ser resolvido com seguranca;
- manter como pendencia apenas risco real, dependencia ativa nao confirmada ou necessidade de decisao humana.

## Commits

- `e418027 governanca: alinhar cofre a estrutura numerada`
- `6705f6d governanca: limpar rota ativa do cofre`
- `a036447 governanca: fechar rota ativa do cofre`
- `78098f3 governanca: resolver pendencias seguras da rota ativa`

Commit final remoto confirmado:

`78098f35d4bc0b4cd9b4a419afcb1ba9d0963b5e`

## Mudancas estruturais principais

### Estrutura numerada consolidada

Foram alinhados os arquivos centrais para a estrutura oficial atual:

- `00-central/` - governanca, regras, decisoes, mapas, pendencias e notas centrais.
- `10-pessoal/` - vida pessoal, rotina, saude, familia, inbox e tarefas.
- `20-profissional/` - LÓGIKA, carreira e referencias profissionais.
- `30-estudos/` - cursos, livros, metodos, planos e recursos de estudo.
- `40-projetos/` - projetos pessoais, profissionais, autorais, produtos e ideias.
- `50-clientes/` - Saude, Camara, SINDSS, vereadores e outros clientes.
- `60-processos/` - checklists, rotinas, relatorios, templates e processos.
- `70-agentes/` - agentes, runtime, squads, escopos e protocolos.
- `80-handoffs/` - passagens formais de contexto.
- `90-arquivo/` - legado, backups, duplicidades, quarentena e estrutura antiga.
- `memory/` - memoria operacional ativa, sessoes, outputs e inbox externa.
- `media/` - midias recebidas/referenciadas.
- `scripts/` - automacoes executaveis.
- `skills/` - skills ativas do workspace.

### Autonomia operacional alinhada

Foram revogadas como regra operacional ativa as ideias antigas de:

- IA apenas como "bibliotecaria";
- IA apenas leitora;
- proibicao geral de editar F1;
- salvamento orientado por F0/F1/F2/F3;
- rotas antigas como destino operacional atual.

A regra atual registrada e reforcada e:

- IA autorizada pode ler, criar, editar, reorganizar, consolidar, mover e manter arquivos do Cofre quando houver escopo claro, seguranca e rastreabilidade.
- Jadielson continua autoridade final sobre sentido, prioridade, publicacao, envio externo, decisoes sensiveis e exclusao definitiva.
- F0/F1/F2/F3 sao legado tecnico/historico, nao rota operacional.

## Arquivos e pastas movidos para `90-arquivo/`

### Planos e inventarios superados

Destino:

`90-arquivo/30-regras-obsoletas/2026-08-10-planos-e-inventarios-superados/`

Movidos:

- `00-central/03-cockpit-projetos.md`
- `00-central/classificacao-arquivos-nao-md.md`
- `00-central/diagnostico-e-proposta-reorganizacao-cofre.md`
- `00-central/inventario-arquivos-nao-md.md`
- `00-central/inventario-frentes-f1-restantes.md`
- `00-central/inventario-md-sem-frontmatter.md`
- `00-central/plano-consolidacao-memorias.md`
- `00-central/plano-migracao-clientes-frentes.md`

Motivo: documentos de diagnostico, plano e inventario que duplicavam ou competiam com `MAPA.md`, `00-central/mapa-do-cofre.md`, `00-central/decisoes.md` e `00-central/pendencias.md`.

### Itens fora da rota ativa com revisao humana

Destino:

`90-arquivo/40-revisao-humana/2026-08-10-itens-fora-da-rota-ativa/`

Movidos:

- `00-central/manifesto.md`
- `40-projetos/README-legado.md`

Motivo: material preservado fora da rota ativa, sem exclusao definitiva.

### Starter Kit/OpenClaw retirado da raiz

Destino:

`90-arquivo/30-regras-obsoletas/2026-08-10-starter-kit-raiz/`

Movidos:

- `README.md`
- `CHANGELOG.md`
- `FAQ.md`

Motivo: material didatico antigo do Starter Kit/OpenClaw confundia a raiz ativa do Cofre.

### Dashboard antigo retirado da raiz

Destino:

`90-arquivo/30-regras-obsoletas/2026-08-10-dashboards-raiz-obsoletos/`

Movido:

- `COCKPIT.md`

Motivo: painel antigo com rotas e consultas superadas.

### Agente bibliotecaria legado

Destino:

`90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/`

Movidos:

- `.claude/agents/bibliotecaria.md` para `bibliotecaria.claude.md`
- `.codex/agents/bibliotecaria.toml` para `bibliotecaria.codex.toml`

Motivo: os perfis ativos antigos mantinham instrucoes diretamente conflitantes com a autonomia operacional atual. A busca por dependencias ativas nao encontrou chamada obrigatoria fora de contexto historico, relatorio ou memoria.

## Arquivos atualizados

### Governanca central

- `AGENTS.md`
- `CONSTITUICAO.md`
- `MAPA.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `00-central/decisoes.md`
- `00-central/mapa-do-cofre.md`
- `00-central/pendencias.md`
- `00-central/regras-de-uso.md`
- `00-central/notas-permanentes/_MAP.md`
- `70-agentes/_MANDATORY.md`

Principais ajustes:

- estrutura numerada registrada como rota oficial;
- F0/F1/F2/F3 tratados como legado;
- autonomia operacional da IA alinhada;
- regra de nao exclusao definitiva reforcada;
- fontes do heartbeat atualizadas;
- pendencias antigas removidas ou reclassificadas.

### Mapas, comandos e agentes

- `.claude/agents/*.md`
- `.claude/commands/*.md`
- `.codex/agents/*.toml`

Principais ajustes:

- removida a persona "bibliotecaria" como identidade operacional ativa;
- removidas rotas antigas F0/F1/F2/F3 como destino de busca ou salvamento;
- referencias antigas de MCP Google trocadas para `gog`;
- comandos de Gmail, Drive e Calendar alinhados com o caminho oficial atual.

### Saude Sao Sebastiao

- `50-clientes/10-saude-sao-sebastiao/README.md`
- `50-clientes/10-saude-sao-sebastiao/contexto.md`
- `50-clientes/10-saude-sao-sebastiao/fontes.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/README.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/01-matrizes/matriz-unificacao-frente-saude.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/README.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/README.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/_ORIGEM_MIGRACAO.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/00-moc/00-mapa-operacional-saude.md`

Principais ajustes:

- rota ativa separada de fontes historicas;
- bases antigas mantidas como rastreabilidade, nao como rota operacional;
- fichas de setor ganharam indice explicando camadas:
  - `fichas-operacionais/` e `servicos-e-competencias/` como rota ativa;
  - `ideias-de-conteudo/` e `lacunas-a-confirmar/` como apoio editorial;
  - `fontes-f1-incorporadas/` e `conteudo-f1-incorporado/` como rastreabilidade.

### Bases legadas de clientes

Foram criados ou atualizados READMEs/avisos de fonte historica em:

- `50-clientes/10-saude-sao-sebastiao/20-fontes/base-legada-f1-frente/`
- `50-clientes/20-camara-municipal/20-fontes/base-legada-f1-frente/`
- `50-clientes/30-sindss/20-fontes/base-legada-f1-frente/`
- `50-clientes/40-outros-vereadores/20-fontes/base-legada-f1-frente/`

Regra registrada:

- usar para auditar origem, recuperar detalhe historico ou comparar com material consolidado;
- nao usar como rota operacional atual nem destino de salvamento novo.

### Estudos, projetos e referencias

- `30-estudos/ia-radar/_README.md`
- `30-estudos/ia-radar/00-cockpit.md`
- `30-estudos/cursos/em-andamento/COMUNIDADE 1P/_MAPA.md`
- `40-projetos/00-mapa.md`
- `40-projetos/30-projetos-autorais/01_Autorais_Culturais/Editais Culturais/README.md`
- `20-profissional/90-referencias/caio-architect.md`

Principais ajustes:

- rotas antigas removidas como destino operacional;
- Google/Drive alinhado para `gog`, browser ou API direta aprovada;
- referencia operacional a Zapier corrigida.

## Arquivos criados

- `60-processos/relatorios/2026-08-10-revisao-cofre-etapa-2-limpeza-rota-ativa.md`
- `60-processos/relatorios/2026-08-10-revisao-cofre-etapa-3-fechamento-rota-ativa.md`
- `60-processos/relatorios/2026-08-10-relatorio-consolidado-limpeza-cofre.md`
- `50-clientes/10-saude-sao-sebastiao/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/20-camara-municipal/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/30-sindss/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/40-outros-vereadores/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/README.md`
- READMEs de rastreabilidade nos lotes de arquivamento em `90-arquivo/`.

## Conteudos uteis nao rastreados que entraram no Cofre

Foram auditados e versionados por serem Markdown util para continuidade:

- `50-clientes/30-sindss/30-entregas/2026-08-09-dia-dos-pais-whatsapp.md`
- `memory/outputs/2026-08-09-prompt-alfred-inbox-captura-geral.md`
- `memory/sessions/2026/2026-08-09-dia-dos-pais-retomada-noite.md`
- `memory/sessions/2026/2026-08-10-contexto-inicial-revisao-cofre.md`

## Contradicoes resolvidas

- Raiz do Cofre deixou de conter README/FAQ/CHANGELOG do Starter Kit como se fossem rota atual.
- `COCKPIT.md` antigo saiu da raiz ativa.
- `memory/2026-08-10.md` deixou de existir como daily note nova criada automaticamente e virou log de sessao.
- Bases legadas de clientes passaram a avisar que sao historicas.
- Comandos e agentes ativos deixaram de apontar para rotas antigas F0/F1/F2/F3.
- Persona "bibliotecaria" saiu da rota ativa.
- Ferramentas Google antigas em comandos foram substituidas por `gog`.
- Zapier deixou de aparecer como caminho operacional em material ativo revisado.

## Pendencias atuais mantidas por motivo real

As pendencias remanescentes estao centralizadas em `00-central/pendencias.md` e foram mantidas por risco real ou necessidade de decisao humana:

- revisar `70-agentes/runtime/*/openclaw-workspace-state.json` antes de versionar;
- decidir se `openclaw-workspace-state.json` da raiz continua versionado ou vira estado tecnico regeneravel;
- decidir destino de midias/anexos locais em `media/inbound/`, por possivel sensibilidade e politica de Drive por frente;
- fazer curadoria final de aprovados/rascunhos quando houver demanda real, porque pode exigir validacao editorial;
- revisar duplicidades internas da Saude somente se houver divergencia factual entre fichas ativas e lacunas;
- manter F0/F1/F2/F3 apenas em contexto historico, logs, relatorios e rastreabilidade;
- verificar dependencias antes de mover scripts, skills, agentes, crons ou runtimes.

## Itens mantidos por seguranca

- `BOOT.md`: mantido na raiz por poder ser lido pelo runtime de startup.
- `UPGRADE-POSTURA.md`: mantido na raiz por ser contrato ativo de postura.
- `openclaw-workspace-state.json`: mantido porque ja estava versionado e pode ter relacao com setup.
- `70-agentes/runtime/central-pessoal/memory/`: mantido fora do commit por exigir revisao de sensibilidade.
- `70-agentes/runtime/*/openclaw-workspace-state.json`: mantidos fora do commit por serem estado tecnico/runtime sensivel ou regeneravel.
- `media/inbound/`: mantido fora do Git por `.gitignore`; no Cofre versionado devem entrar apenas sinteses Markdown, links, IDs, status ou proximos passos.

## Validacoes realizadas

- `git status`
- `git diff --check`
- `git diff --cached --check`
- verificacao de `.md` sem YAML frontmatter
- `python3 -m py_compile scripts/sync/*.py`
- busca por referencias operacionais antigas em `.claude/` e `.codex/`
- confirmacao do remoto `origin/main`

Resultado final das validacoes:

- diff check: OK;
- Markdown sem YAML: sem pendencias;
- scripts Python em `scripts/sync/`: OK;
- `.claude/` e `.codex/` sem referencias operacionais antigas a F0/F1/F2/F3, bibliotecaria, MCP Google antigo ou Zapier;
- push confirmado em `origin/main`.

## Estado final

O Cofre ficou com a rota ativa mais limpa e integrada:

- governanca central aponta para a estrutura numerada;
- mapas e pendencias estao coerentes;
- legados foram preservados fora da rota ativa;
- agentes e comandos ativos foram alinhados;
- Saude Sao Sebastiao ficou mais navegavel;
- pendencias remanescentes agora tem justificativa real;
- nada foi excluido definitivamente.

