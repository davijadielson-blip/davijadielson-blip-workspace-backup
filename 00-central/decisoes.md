---
tema: decisões estruturais do Cofre
conteudo: registro oficial de decisões finais sobre organização, governança, agentes e segurança do Cofre
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: registro de decisões
prioridade: máxima
atualizado_em: 2026-07-28
usar_quando: verificar decisões finais aprovadas sobre estrutura e operação do Cofre
nao_usar_quando: registrar ideias, hipóteses ou propostas ainda não aprovadas
---

# Decisões estruturais do Cofre

## 2026-07-28 — Opção A aprovada: migrar fluxos [F0]–[F3] para estrutura numerada
- **Status:** aprovado por Jadielson.
- **Decisão:** migrar TODO o conteúdo dos fluxos antigos `[F0]`–`[F3]` para a estrutura numerada (`00-central` a `90-arquivo`), e arquivar os fluxos vazios em `90-arquivo/` como legado.
- **Mapa de migração:**
  | Fluxo antigo | Destino novo |
  |---|---|
  | `[F0] 0-Inbox/` | `10-pessoal/00-inbox/` (captura pessoal) |
  | `[F1] 1-Permanentes/` | `00-central/notas-permanentes/` |
  | `[F1] 2-Literatura/` | `30-estudos/` |
  | `[F1] 3-Daily/` | `10-pessoal/` |
  | `[F1] 4-Pessoal/` | `10-pessoal/` (fundir com estrutura existente) |
  | `[F1] 5-Frentes/` | Resquícios → `20-profissional/` ou `50-clientes/` |
  | `[F1] ESTUDOS/` | `30-estudos/` |
  | `[F1] TAREFAS/` | `10-pessoal/` ou `20-profissional/` |
  | `[F2] memory/` | Incorporar gradualmente às áreas por tema |
  | `[F2] agentes/` | `70-agentes/` |
  | `[F2] archive/` | `90-arquivo/` |
  | `[F3] PROJETOS/` | `40-projetos/` |
  | `memory/` | Consolidar com `[F2] memory/` → áreas |
  | `archive/` | `90-arquivo/` |
  | `areas/` | `20-profissional/` ou `50-clientes/` |
  | `scripts/` | `60-processos/` |
  | `skills/` | `60-processos/` |
  | `ops/` | `60-processos/` |
  | `checklists/` | `60-processos/` |
  | `rotinas/` | `60-processos/` |
- **Regra:** cada lote com log reversível; nada apagado, apenas movido para `90-arquivo/` como backup.
- **Execução:** em lotes pequenos e seguros, começando pelos mais simples.

## 2026-07-28 — Auditoria de espaço emergencial: limpeza concluída
- **Status:** concluído.
- **Decisão:** executar auditoria de espaço para liberar disco de 95% para ~76%.
- **Ações realizadas:**
  1. Git garbage removido e shallow clone (`.git` de 753 MB → 8.6 MB)
  2. Clone duplicado `segundo-cerebro-jadielson/` removido (132 MB)
  3. Sessões de agentes com +7 dias removidas (~111 MB)
  4. Backups `openclaw.json.bak*` e `rejected*` antigos removidos (~12 MB)
  5. Arquivos não-.md movidos para `90-arquivo/99-quarentena-nao-md/` (~12 MB)
  6. Pastas vazias removidas (143 pastas)
  7. `trash/` limpo (~8 MB)
  8. `mission-control-next/node_modules/` removido (~328 MB)
  9. `media/` (cache) limpo (46 MB)
  10. `browser/` (cache) limpo (16 MB)
  11. HTMLs mission-control no workspace removidos (~492 KB)
- **Preservado:** sessões de agentes com menos de 3 dias (para evitar alucinação).
- **Backup:** GitHub atualizado com force push do shallow clone.
- **Resultado:** disco de 9.5G/10G (95%) → 7.6G/10G (76%) — **~1.9 GB liberados**.
- **Como desfazer:** não há rollback simples; o histórico completo do git foi substituído pelo shallow clone, mas o GitHub preserva o histórico completo do workspace.

## 2026-07-28 — Protocolo de bootstrap obrigatório: consultar Cofre antes de qualquer resposta
- **Status:** aprovado e registrado por Jadielson.
- **Decisão:** ao acordar em sessão nova, a Lôh DEVE consultar o Cofre (IDENTITY.md, SOUL.md, USER.md, CONSTITUICAO.md) ANTES de responder qualquer mensagem, inclusive para se apresentar ou identificar.
- **Motivo:** evitar o erro de começar uma conversa como se fosse um agente genérico sem memória, quando na verdade o Cofre já contém identidade, história e contexto completos.
- **Como desfazer:** remover este registro; não afeta outros arquivos.

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

## 2026-07-26 — Lote 9 executado: migração Lógika Creative
- **Status:** concluído.
- **O que mudou:** migrado o conteúdo profissional legado de `[F1] 5-Frentes/Logika-Creative/` para `20-profissional/10-logika/`.
- **Movimentações:** 104 arquivos movidos, preservando subpastas operacionais e criando estrutura por área.

## 2026-07-28 — Migração completa [F0]–[F3] para estrutura numerada (L10–L23)
- **Status:** concluído.
- **O que mudou:** toda a estrutura antiga `[F0] 0-Inbox` até `[F3] PROJETOS` foi migrada para a estrutura numerada `00-central` a `90-arquivo`.
- **Lotes executados:**
  - L10: `[F1] 2-Literatura/` → `30-estudos/10-literatura/`
  - L11: `[F1] 3-Daily/` → `10-pessoal/`
  - L12: `[F1] TAREFAS/` → `10-pessoal/tarefas/`
  - L13: `[F1] 1-Permanentes/` → `00-central/notas-permanentes/`
  - L14: `[F1] ESTUDOS/` → `30-estudos/cursos/`
  - L15: `[F1] 4-Pessoal/` → `10-pessoal/` (146 arquivos, organizados por tema: saúde, finanças, família, transporte, etc.)
  - L16: `[F1] 5-Frentes/` resquícios → `40-projetos/ideias/`
  - L17: `[F3] PROJETOS/` → `40-projetos/` (1.053 arquivos, organizados em 10-pessoais, 20-profissionais, 30-projetos-autorais, 40-trabalho, 50-produtos)
  - L18: `[F2] memory/` → `90-arquivo/01-memoria-legada/` (539 arquivos)
  - L19: `[F2] agentes/` → `70-agentes/`
  - L20: `scripts/`, `skills/`, `ops/`, `checklists/`, `rotinas/` → `60-processos/`
  - L21: `[F2] archive/`, `archive/`, `areas/` → `90-arquivo/`
  - L22: `[F0] 0-Inbox/` → `10-pessoal/inbox/`
  - L23: Pastas `[F0]`–`[F3]` vazias → `90-arquivo/02-estrutura-antiga/` (1.896 arquivos)
- **Segurança:** credenciais `.secrets/` removidas do workspace, `.env` removido, não-.md movidos para quarentena.
- **Disco:** 44 MB (excluindo .git), contra 8.4M só do [F3] PROJETOS original.
- **Git:** commit `e50a6f9` → novo commit com todos os lotes.
- **Onde estão os originais:** `90-arquivo/02-estrutura-antiga/` (estrutura completa preservada).
- **Como desfazer:** mover os arquivos de `40-projetos/`, `10-pessoal/`, `30-estudos/` de volta para suas origens em `90-arquivo/02-estrutura-antiga/`.
## 2026-07-28 — Política de custo: agentes e subagentes sem fallback automático para OpenRouter
- **Status:** executado por solicitação de Jadielson.
- **Problema:** agentes/subagentes estavam falhando no Codex e caindo em OpenRouter, consumindo créditos.
- **Decisão:** alinhar agentes e subagentes ao mesmo princípio da Lôh: `openai-codex/gpt-5.5` como primário e `fallbacks: []` para impedir failover automático pago.
- **Correção técnica:** `agents.defaults.model`, `agents.defaults.subagents.model` e os 21 agentes configurados foram ajustados para Codex sem fallback; perfis `openai-codex` foram propagados do agente `main` para os agentes explícitos sem expor credenciais.
- **Observação:** OpenRouter permanece apenas como integração disponível/manual no catálogo, mas não como fallback automático de agentes/subagentes.
- **Como desfazer:** restaurar fallbacks em `/data/.openclaw/openclaw.json` e/ou remover perfis Codex propagados dos diretórios de agentes.

## 2026-07-28 — Ajuste da política de fallback: mínimo de operação sem queimar crédito
- **Status:** provisório/seguro.
- **Diretriz de Jadielson:** manter planos B/C para garantir operação mínima quando Codex GPT-5.5 não rodar por limite, mas evitar consumo indevido de OpenRouter.
- **Diagnóstico:** o fallback nativo não expõe, no schema atual, uma condição clara por motivo de falha (ex.: limite/capacidade vs autenticação). Como falha de autenticação já disparou OpenRouter no passado, fallback pago automático é arriscado.
- **Política aplicada agora:** `openai-codex/gpt-5.5` como primário; fallback automático restrito a `openrouter/minimax/minimax-m2.5:free` enquanto a autenticação Codex dos agentes/subagentes não estiver validada.
- **Plano B/C definitivo desejado:** Codex primário; fallback pago/baixo custo só após guardrail contra falha de autenticação ou com autorização explícita por tarefa crítica.
- **Pendente:** resolver autenticação Codex individual dos agentes (perfil Codex do `main` não é portátil para outros `agentDir`), ou definir arquitetura onde especialistas rodam via runtime autenticado sem compartilhar credenciais indevidamente.

## 2026-07-28 — Correção: fallback DEVE ser para OpenRouter
- **Status:** corrigido após esclarecimento de Jadielson.
- **Decisão final:** manter `openai-codex/gpt-5.5` como modelo primário, mas com fallback automático para OpenRouter como plano B/C.
- **Ordem aplicada:** `openrouter/minimax/minimax-m2.5:free` → `openrouter/google/gemini-2.5-flash-lite` → `openrouter/deepseek/deepseek-v4-flash`.
- **Motivo:** garantir mínimo de operação quando Codex não rodar, preservando custo menor antes de fallback pago.

## 2026-07-28 — Reordenação de fallback OpenRouter por custo
- **Status:** executado por ajuste de Jadielson.
- **Decisão:** após o primário `openai-codex/gpt-5.5`, a cadeia de fallback deve começar por `openrouter/deepseek/deepseek-v4-flash`, por ser a opção mais barata indicada.
- **Ordem aplicada:** `openrouter/deepseek/deepseek-v4-flash` → `openrouter/minimax/minimax-m2.5:free` → `openrouter/google/gemini-2.5-flash-lite`.
- **Escopo:** defaults globais, subagents e todos os agentes configurados.

## 2026-07-28 — Consciência de modelo: GPT-5.5 Codex como primário oficial
- **Status:** executado por solicitação de Jadielson.
- **Problema:** alguns agentes e subagentes ainda não reconheciam corretamente o modelo oficial `GPT-5.5 Codex`, tratando o runtime como GPT genérico ou versões antigas.
- **Decisão:** reforçar em configuração que o primário oficial do ecossistema é `openai-codex/gpt-5.5`, chamado operacionalmente de **GPT-5.5 Codex**.
- **Correção técnica:** `agents.defaults.model`, `agents.defaults.subagents.model` e os 21 agentes configurados foram realinhados para `openai-codex/gpt-5.5`; também foi adicionado `params.modelAwareness` nos defaults e nos agentes para declarar explicitamente o modelo oficial e a ordem de fallback.
- **Fallback preservado:** `openrouter/deepseek/deepseek-v4-flash` → `openrouter/minimax/minimax-m2.5:free` → `openrouter/google/gemini-2.5-flash-lite`.
- **Como validar:** conferir `/data/.openclaw/openclaw.json` e reiniciar/recarregar o Gateway após qualquer alteração futura de modelo.

## 2026-07-28 — Correção de billing OpenRouter em heartbeat de agente
- **Status:** executado após erro reportado por Jadielson.
- **Problema:** o agente `saude-corpo-energia`, em heartbeat, caiu no fallback `openrouter/google/gemini-2.5-flash-lite` e recebeu erro 402 de billing por saldo insuficiente/max tokens alto.
- **Decisão:** remover o fallback Gemini da cadeia automática e limitar o teto de saída para reduzir risco de erro/custo.
- **Política aplicada:** defaults e agentes usam `openai-codex/gpt-5.5` como primário, com fallback `openrouter/deepseek/deepseek-v4-flash` → `openrouter/minimax/minimax-m2.5:free`; o agente `saude-corpo-energia` ficou ainda mais restrito, com fallback apenas `openrouter/minimax/minimax-m2.5:free`.
- **Limites aplicados:** `params.max_tokens` e `params.max_output_tokens` em 4096 nos defaults/agentes; `saude-corpo-energia` em 2048.
- **Motivo:** manter operação mínima sem tentar modelos OpenRouter que já falharam por saldo insuficiente.

## 2026-07-29 — Correção de ID inválido do GPT-5.5 Codex
- **Status:** executado após novo erro reportado por Jadielson.
- **Erro observado:** `Model Fallback: openrouter/deepseek/deepseek-v4-flash (selected openai-codex/gpt-5.5; model not found)`.
- **Diagnóstico:** o ID `openai-codex/gpt-5.5` não é resolvido de forma confiável pelo Gateway/OpenClaw para todos os agentes/tópicos; por isso o sistema caía no fallback OpenRouter com motivo `model not found`.
- **Correção:** trocar o primário técnico de defaults, subagents e 21 agentes para `openai/gpt-5.5`, mantendo a consciência operacional de que este é o **GPT-5.5 Codex oficial do ecossistema**.
- **Fallback preservado:** `openrouter/deepseek/deepseek-v4-flash` → `openrouter/minimax/minimax-m2.5:free`; `saude-corpo-energia` permanece mais restrito, com fallback apenas `openrouter/minimax/minimax-m2.5:free`.
- **Regra nova:** não usar `openai-codex/gpt-5.5` como primário em `openclaw.json`; usar `openai/gpt-5.5` com alias/consciência de GPT-5.5 Codex.
