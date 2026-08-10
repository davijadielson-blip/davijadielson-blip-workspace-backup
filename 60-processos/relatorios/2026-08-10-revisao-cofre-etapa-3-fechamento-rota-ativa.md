---
tema: revisao do Cofre etapa 3 - fechamento da rota ativa
conteudo: relatorio de limpeza final da rota ativa, bases legadas, raiz, memory e arquivos nao rastreados
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: relatorio
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: auditar o fechamento da limpeza e consolidacao do Cofre em 2026-08-10
nao_usar_quando: substituir MAPA.md, AGENTS.md ou 00-central/mapa-do-cofre.md
---

# Revisao do Cofre - Etapa 3

## Objetivo

Concluir a limpeza da rota ativa do Cofre, reduzindo contradicoes fortes sem deletar nada definitivamente e sem quebrar automacoes.

## Arquivos movidos para `90-arquivo/`

### Starter Kit/OpenClaw retirado da raiz ativa

Destino: `90-arquivo/30-regras-obsoletas/2026-08-10-starter-kit-raiz/`

- `README.md`
- `CHANGELOG.md`
- `FAQ.md`
- `90-arquivo/30-regras-obsoletas/2026-08-10-starter-kit-raiz/README.md` criado como rastreabilidade.

Motivo: materiais didaticos do Starter Kit/OpenClaw, nao rota operacional atual do Cofre.

### Dashboard antigo retirado da raiz ativa

Destino: `90-arquivo/30-regras-obsoletas/2026-08-10-dashboards-raiz-obsoletos/`

- `COCKPIT.md`
- `90-arquivo/30-regras-obsoletas/2026-08-10-dashboards-raiz-obsoletos/README.md` criado como rastreabilidade.

Motivo: painel antigo com rotas e consultas Dataview superadas.

## Arquivo movido em `memory/`

- Origem: `memory/2026-08-10.md`
- Destino: `memory/sessions/2026/2026-08-10-contexto-inicial-revisao-cofre.md`

Motivo: evitar manter nova daily note automatica na raiz de `memory/`. O conteudo era log/contexto de sessao e foi preservado no local adequado.

## Arquivos atualizados

- `MAPA.md`: removida referencia ao README do Starter Kit na raiz, ajustada rota de logs de sessao e registrado arquivamento do Starter Kit.
- `00-central/mapa-do-cofre.md`: reforcada a regra de raiz limpa e rota ativa.
- `00-central/decisoes.md`: registrada a decisao da etapa 3.
- `00-central/pendencias.md`: removidas pendencias ja resolvidas e mantidas pendencias reais.
- `50-clientes/10-saude-sao-sebastiao/README.md`: rota atual da frente explicitada.
- `50-clientes/10-saude-sao-sebastiao/contexto.md`: estrutura atual separada de fonte historica.
- `50-clientes/10-saude-sao-sebastiao/fontes.md`: fontes ativas e legadas separadas.
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/01-matrizes/matriz-unificacao-frente-saude.md`: removida linguagem de destino antigo e ajustada para rota atual.
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/README.md`: marcada como memoria historica consultiva.
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/_ORIGEM_MIGRACAO.md`: removida instrucao de retorno para rota antiga.
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/00-moc/00-mapa-operacional-saude.md`: marcado como mapa historico.
- `_MAP.md` e `_ORIGEM_MIGRACAO.md` das bases legadas de Saúde, Câmara, SINDSS e Outros Vereadores: avisos de fonte historica e regra de nao usar como rota ativa.
- `30-estudos/ia-radar/_README.md`, `30-estudos/ia-radar/00-cockpit.md` e `30-estudos/cursos/em-andamento/COMUNIDADE 1P/_MAPA.md`: removidas rotas antigas como orientação operacional.

## Arquivos criados

- `50-clientes/10-saude-sao-sebastiao/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/20-camara-municipal/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/30-sindss/20-fontes/base-legada-f1-frente/README.md`
- `50-clientes/40-outros-vereadores/20-fontes/base-legada-f1-frente/README.md`

Motivo: impedir que bases legadas sejam lidas como rota operacional atual.

## Arquivos nao rastreados auditados

- `50-clientes/30-sindss/30-entregas/2026-08-09-dia-dos-pais-whatsapp.md`: conteudo Markdown aprovado, deve entrar no Cofre e no commit.
- `memory/outputs/2026-08-09-prompt-alfred-inbox-captura-geral.md`: prompt operacional aprovado, deve entrar no Cofre e no commit.
- `memory/sessions/2026/2026-08-09-dia-dos-pais-retomada-noite.md`: log de continuidade, deve entrar no Cofre e no commit.
- `memory/sessions/2026/2026-08-10-contexto-inicial-revisao-cofre.md`: conteudo preservado de `memory/2026-08-10.md`, deve entrar no Cofre e no commit.
- `70-agentes/runtime/central-pessoal/memory/2026-08-08.md`: memoria interna de runtime; mantida fora do commit por exigir revisao de sensibilidade.
- `70-agentes/runtime/*/openclaw-workspace-state.json`: estado tecnico/regeneravel de runtime; mantido fora do commit por risco de versionar estado operacional.

## Duplicidades consolidadas

- Na raiz, `README.md`, `CHANGELOG.md` e `FAQ.md` do Starter Kit deixaram de competir com `MAPA.md`, `AGENTS.md` e `00-central/mapa-do-cofre.md`.
- Em Saúde, a leitura operacional foi centralizada em `README.md`, `fontes.md` e `10-contexto/operacional/README.md`; bases antigas receberam avisos de legado.

## Contradicoes resolvidas

- Starter Kit removido da raiz ativa.
- `COCKPIT.md` antigo removido da raiz ativa.
- `memory/2026-08-10.md` removido da raiz de `memory/`.
- Bases legadas deixaram claro que preservam origem, mas nao orientam salvamento novo.
- Referencias ativas em IA Radar e Comunidade 1P deixaram de usar rotas antigas como destino operacional.

## Itens mantidos por decisao ou risco

- `BOOT.md`: mantido na raiz por poder ser lido pelo runtime de startup.
- `UPGRADE-POSTURA.md`: mantido na raiz por ser contrato ativo de postura e possuir referencias historicas em briefing.
- `openclaw-workspace-state.json` da raiz: mantido porque ja estava versionado e pode ter relacao com setup do workspace; precisa de decisao tecnica futura.
- Estados runtime nao rastreados: mantidos fora do commit.
- Referencias antigas em logs, relatorios, scripts de compatibilidade, `00_ORIGENS_LEGADAS/` e fichas que citam fontes historicas: mantidas como contexto historico.

## Dependencias verificadas

- `rg` por arquivos raiz movidos antes da movimentacao.
- `rg` por `memory/2026-08-10.md`.
- `rg` por referencias antigas fora de `90-arquivo/`, `memory/` e bases legadas.
- `git status` antes e depois da limpeza.

## Riscos restantes

- Ha grande volume de referencias antigas em areas historicas, fichas incorporadas e relatorios. Elas nao devem orientar rota ativa, mas ainda podem aparecer em busca textual.
- Alguns arquivos de estudos/cursos antigos mencionam rotas ou ferramentas antigas em contexto historico; revisar por frente quando voltarem a ser usados.
- Estados runtime ainda aparecem como nao rastreados e precisam de politica definitiva: versionar, ignorar ou mover para revisao.

## Recomendacao de proxima etapa

Fazer uma etapa pequena, por frente, para limpar apenas arquivos ativos de estudos/projetos que ainda tenham rotas antigas fora de contexto historico. Nao fazer migracao em massa sem prioridade de uso.

## Complemento apos revisao de pendencias

Pedido posterior de Jadielson: nao deixar como pendencia aquilo que pudesse ser resolvido com seguranca em 2026-08-10.

Resolvido no complemento:

- Arquivados os perfis antigos `bibliotecaria` de `.claude/agents/` e `.codex/agents/` em `90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/`.
- Criado `90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/README.md` com origem, destino, motivo e dependencias verificadas.
- Criado `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/README.md`, separando `fichas-operacionais/` e `servicos-e-competencias/` como rota ativa, `ideias-de-conteudo/` e `lacunas-a-confirmar/` como apoio editorial, e `fontes-f1-incorporadas/`/`conteudo-f1-incorporado/` como rastreabilidade.
- Normalizados comandos e perfis ativos em `.claude/commands/`, `.claude/agents/` e `.codex/agents/`: removida persona "bibliotecaria", substituidas rotas `[F2] memory/` por `memory/`, trocadas referencias antigas de MCP Google por `gog` e corrigidas rotas `[F1]`/`[F0]` que ainda orientavam salvamento ou busca.
- Atualizado `00-central/pendencias.md` para manter somente pendencias com risco real, dependencia ativa nao confirmada ou necessidade de decisao humana.

Pendencias removidas por resolucao segura:

- Destino formal do agente `bibliotecaria` legado.
- Separacao navegacional das duplicidades internas de fichas da Saude.
- Politica generica de arquivos nao Markdown dentro do Cofre.
- Referencias operacionais antigas em comandos e perfis ativos `.claude/` e `.codex/`.

Pendencias mantidas por risco real:

- Estados runtime nao rastreados em `70-agentes/runtime/*/openclaw-workspace-state.json`.
- `openclaw-workspace-state.json` da raiz, por ja estar versionado e poder ter relacao com setup.
- Midias/anexos locais em `media/inbound/`, por envolverem material sensivel e politica de Drive por frente.
- Curadoria final de rascunhos/aprovados, por exigir validacao editorial ou leitura caso a caso.

## Validacao

- `git status`: executado.
- `git diff --check`: OK.
- Verificacao de `.md` sem YAML frontmatter: OK, sem pendencias retornadas.
- `python3 -m py_compile` nos scripts Python de `scripts/sync/`: OK.
- Busca por referencias antigas: executada; sobras foram classificadas como historicas, compatibilidade tecnica, ou pendencia futura.
