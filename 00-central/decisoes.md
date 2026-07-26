---
tema: decisões estruturais do Cofre
conteudo: registro oficial de decisões finais sobre organização, governança, agentes e segurança do Cofre
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: registro de decisões
prioridade: máxima
atualizado_em: 2026-07-26
usar_quando: verificar decisões finais aprovadas sobre estrutura e operação do Cofre
nao_usar_quando: registrar ideias, hipóteses ou propostas ainda não aprovadas
---

# Decisões estruturais do Cofre

## 2026-07-26 — Diagnóstico e proposta de reorganização iniciados
- **Status:** em proposta, aguardando aprovação de Jadielson para mover arquivos.
- **Decisão operacional já executada:** criar camada central mínima (`00-central/`, `70-agentes/`, `80-handoffs/`) sem mover arquivos existentes, para registrar regras, mapa de agentes e template de handoff.
- **Motivo:** atender ao pedido de reorganização segura, reforçar LOCAL-FIRST e reduzir alucinação/vazamento de contexto.
- **Arquivos-base consultados:** `CONSTITUICAO.md`, `AGENTS.md`, `MAPA.md`, `MEMORY.md`, `memory_search`.
- **Próxima decisão pendente:** aprovar ou ajustar a estrutura proposta antes de qualquer movimentação.
## 2026-07-26 — Aprovação da reorganização e revisão da lógica dos fluxos
- **Status:** aprovado por Jadielson.
- **Decisão:** abandonar a regra estrutural de limitação rígida de escrita por fluxos `[F0]`–`[F3]`, porque o Cofre hoje é alimentado primariamente por agentes.
- **Nova diretriz:** a estrutura deve ser firme, colaborativa e favorável ao time; agentes podem escrever onde a função exigir, desde que haja escopo, rastreabilidade, frontmatter, citação de fontes, segurança e registro de decisões/pendências.
- **Execução autorizada:** iniciar reorganização em etapas pequenas, sem apagar arquivos, movendo duplicidades/legados apenas para áreas de arquivo/revisão quando apropriado.
- **Arquivos criados/atualizados nesta etapa:** `00-central/mapa-do-cofre.md`, `00-central/glossario.md`, `00-central/regras-de-uso.md`, `00-central/decisoes.md`.
- **Como desfazer:** manter os arquivos criados como proposta histórica ou mover para `90-arquivo/_revisar/` mediante nova aprovação; nenhum arquivo antigo foi movido nesta etapa.
## 2026-07-26 — Lote 1 executado: frontmatter e mapas centrais
- **Status:** concluído.
- **O que mudou:** corrigidos cabeçalhos YAML dos 12 arquivos `.md` identificados sem frontmatter; criados mapa central, glossário e inventários de revisão.
- **Onde foi salvo:** arquivos originais corrigidos; inventários em `00-central/inventario-md-sem-frontmatter.md` e `00-central/inventario-arquivos-nao-md.md`.
- **Como desfazer:** remover manualmente os blocos YAML adicionados aos 12 arquivos listados no snapshot textual, se Jadielson solicitar.
- **Pendentes:** classificar e decidir destino dos arquivos não-`.md`; mover duplicidades apenas em lote aprovado.
## 2026-07-26 — Lote 2 executado: estrutura-base e classificação não-.md
- **Status:** concluído.
- **O que mudou:** criadas subpastas-base nas áreas `10-pessoal/` a `90-arquivo/`; adicionados `README.md` com finalidade e regra de uso em cada área; regras centrais reorganizadas com texto mais estratégico; arquivos não-.md classificados por risco/destino provável.
- **Onde foi salvo:** `00-central/classificacao-arquivos-nao-md.md`, `00-central/mapa-do-cofre.md`, `00-central/regras-de-uso.md` e `README.md` das áreas.
- **Como desfazer:** remover as subpastas-base vazias/índices criados e restaurar versões anteriores pelo snapshot textual; nenhum arquivo antigo foi apagado.
- **Pendentes:** decidir política para arquivos sensíveis/técnicos e migrar conteúdos legados por lotes.
## 2026-07-26 — Lote 3 executado: consolidação segura das memórias
- **Status:** concluído.
- **O que mudou:** criado plano de consolidação em `00-central/plano-consolidacao-memorias.md`; criados índices em `memory/README.md` e `[F2] memory/README.md`; pastas duplicadas/vazias com nomes problemáticos foram movidas para `90-arquivo/20-duplicidades/`.
- **Decisão:** `memory/` permanece como memória ativa diária/sessão; `[F2] memory/` permanece como memória operacional legada em transição, sem migração em massa.
- **Como desfazer:** usar o log `90-arquivo/20-duplicidades/log-lote3-memorias-20260726T032315Z.md` e mover as pastas arquivadas de volta à raiz.
- **Pendentes:** migrar conteúdos de `[F2] memory/` por tema para áreas numeradas.
## 2026-07-26 — Lote 4 executado: estrutura canônica de clientes/frentes
- **Status:** concluído.
- **O que mudou:** criada estrutura canônica por cliente/frente em `50-clientes/`, com `README.md`, `contexto.md`, `fontes.md`, `pendencias.md` e `handoffs.md` para cada frente principal.
- **Onde foi salvo:** `50-clientes/` e `00-central/plano-migracao-clientes-frentes.md`.
- **Como desfazer:** remover os arquivos/índices criados em `50-clientes/`; nenhum conteúdo legado foi movido.
- **Pendentes:** migrar conteúdos legados por frente, começando por Saúde São Sebastião.
## 2026-07-26 — Lote 5 executado: migração real Saúde São Sebastião
- **Status:** concluído.
- **O que mudou:** fontes legadas de Saúde São Sebastião foram movidas para `50-clientes/10-saude-sao-sebastiao/`, centralizando F1, F2 outputs/memória e F3 projetos da frente.
- **Movimentações:** 4 origens migradas, total de 545 arquivos.
- **Onde foi salvo:** `50-clientes/10-saude-sao-sebastiao/`; log em `50-clientes/10-saude-sao-sebastiao/90-arquivo/log-lote5-migracao-saude-20260726T032915Z.md`; snapshot em `90-arquivo/50-backups-snapshots/lote5-saude-before-20260726T032915Z.md`.
- **Como desfazer:** seguir o log do lote 5 e mover cada destino de volta à origem.
- **Pendentes:** revisar duplicidades internas, separar aprovados/rascunhos e consolidar índices temáticos.
## 2026-07-26 — Lote 6 executado: organização interna Saúde São Sebastião
- **Status:** concluído.
- **O que mudou:** criados índices internos de unidades/setores, editorial, aprovados/rascunhos e padrão de nomes; duplicidades de `Projetos de Conteudo`/`Projetos de Conteúdo` foram consolidadas em `30-entregas/10-producao-conteudo-legado/`.
- **Critério de renomeação:** renomear/consolidar apenas quando melhorar compreensão sem quebrar rastreabilidade; nomes legados internos foram preservados quando úteis.
- **Onde foi salvo:** `50-clientes/10-saude-sao-sebastiao/00-indice/` e log `50-clientes/10-saude-sao-sebastiao/90-arquivo/renomeacoes/log-lote6-organizacao-interna-20260726T033434Z.md`.
- **Como desfazer:** seguir o log do lote 6 e snapshot `90-arquivo/50-backups-snapshots/lote6-saude-interno-before-20260726T033434Z.md`.
- **Pendentes:** revisão qualitativa dos materiais classificados automaticamente como aprovados/rascunhos.
## 2026-07-26 — Lote 7 executado: migração Câmara Municipal e SINDSS
- **Status:** concluído.
- **O que mudou:** migradas as bases legadas de Câmara Municipal e SINDSS para `50-clientes/`, com índices gerais/editoriais, classificação inicial de aprovados/rascunhos e padrão de nomes.
- **Movimentações:** 2 origens migradas, total de 30 arquivos.
- **Como desfazer:** usar logs em `50-clientes/20-camara-municipal/90-arquivo/renomeacoes/` e `50-clientes/30-sindss/90-arquivo/renomeacoes/`.
- **Pendentes:** revisão qualitativa dos índices e migração de outras frentes/clientes.
## 2026-07-26 — Lote 8 executado: outros vereadores e outros clientes
- **Status:** concluído.
- **O que mudou:** migradas frentes menores/legadas para `50-clientes/40-outros-vereadores/` e `50-clientes/50-outros-clientes/`, com índices e logs reversíveis.
- **Movimentações:** 4 origens migradas, total de 9 arquivos.
- **Onde foi salvo:** `50-clientes/40-outros-vereadores/`, `50-clientes/50-outros-clientes/`, snapshots em `90-arquivo/50-backups-snapshots/` e inventário `00-central/inventario-frentes-f1-restantes.md`.
- **Como desfazer:** seguir logs em `90-arquivo/renomeacoes/` de cada frente.
- **Pendentes:** avaliar `Logika-Creative` e `Projetos` restantes em `[F1] 5-Frentes/`.
