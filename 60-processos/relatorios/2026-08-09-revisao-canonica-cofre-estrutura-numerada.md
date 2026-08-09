---
tema: relatorio da revisao canonica do Cofre para estrutura numerada
conteudo: auditoria, arquivos alterados, regras revogadas, dependencias verificadas, riscos restantes e resultado da otimizacao estrutural de 2026-08-09
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: relatorio de auditoria
prioridade: maxima
atualizado_em: 2026-08-09
usar_quando: verificar o que foi otimizado na revisao estrutural do Cofre em 2026-08-09
nao_usar_quando: substituir MAPA.md, AGENTS.md ou CONSTITUICAO.md
---

# Revisao canonica do Cofre - estrutura numerada

## Origem

- Pedido de Jadielson em 2026-08-09.
- Prompt-base: `80-handoffs/prompt-loh-revisao-cofre-2026-08-09.md`.
- Objetivo: alinhar governanca, mapa e agentes com a arvore real atual, sem quebrar dependencias.

## Resultado

Revisao aplicada sem mover, renomear ou apagar pastas. A mudanca foi feita como camada canonica de governanca e compatibilidade:

- estrutura oficial atual: `00-central/`, `10-pessoal/`, `20-profissional/`, `30-estudos/`, `40-projetos/`, `50-clientes/`, `60-processos/`, `70-agentes/`, `80-handoffs/`, `90-arquivo/`, `memory/`, `media/`, `scripts/`, `skills/`;
- `[F0]`, `[F1]`, `[F2]` e `[F3]` marcados como legado tecnico/historico;
- revogada a logica operacional de "IA bibliotecaria", "IA so le", "nao editar F1" e "so Jadielson escreve determinada pasta";
- consolidada a diretriz: autonomia operacional da IA autorizada, autoridade final humana.

## Arquivos alterados

- `MAPA.md`
- `AGENTS.md`
- `CONSTITUICAO.md`
- `MEMORY.md`
- `00-central/decisoes.md`
- `00-central/regras-de-uso.md`
- `00-central/mapa-do-cofre.md`
- `70-agentes/_MANDATORY.md`
- `70-agentes/ARQUITETURA-AGENTES.md`
- `70-agentes/protocolo-de-orquestracao.md`
- `70-agentes/mapa-dos-agentes.md`
- prompts do squad em `70-agentes/logika-c-level-squad/`
- `60-processos/templates/approval_workflow.md`
- `60-processos/skills/metodo-pode.md`
- `60-processos/skills/SKILL-SERVICE’s MacBook Pro.md`
- `scripts/sync/notion-cofre-index-import.py`
- `scripts/sync/notion-cofre-sync.py`

## Regras revogadas

- IA como "bibliotecaria" no sentido de so organizar sem escrever.
- "IA so le" como regra geral.
- "Nao editar F1" como regra estrutural.
- "F1 humano / F2 IA" como roteamento vigente.
- "Camada 4 nunca migra" como limitacao geral.
- Salvamento novo guiado por `[F0]` a `[F3]`.

## Regras consolidadas

- O Cofre e fonte de verdade unica.
- A IA autorizada pode manter o Cofre inteiro operacionalmente quando houver escopo, fonte, rastreabilidade e utilidade real.
- Jadielson permanece autoridade final sobre sentido, prioridade, publicacao, envio externo, decisoes sensiveis e exclusao definitiva.
- Antes de mover, renomear ou consolidar, auditar dependencias em agentes, subagentes, skills, crons, scripts, runtimes, handoffs, configuracoes e referencias internas.
- Nada de exclusao definitiva sem autorizacao humana explicita.
- Todo Markdown criado ou editado deve ter YAML frontmatter.

## Inventario verificado

- Agentes e documentos em `70-agentes/`: 95 arquivos.
- Skills ativas em `skills/`: 12 arquivos.
- Scripts em `scripts/`: 18 arquivos.
- Handoffs em `80-handoffs/`: 3 arquivos.
- Runtimes em `70-agentes/runtime/`: 27 arquivos ate profundidade 2.
- Crons OpenClaw ativos: 3 jobs, todos habilitados e com ultimo status `ok`.

## Crons verificados

- `sinal-proximo-dia-2100`
- `governanca-cofre-sessoes-diaria-0000`
- `pauta-completa-dia-0700`

Os payloads consultados nao dependem diretamente de caminhos `[F0]`, `[F1]`, `[F2]` ou `[F3]`. Dois crons tinham avisos de execucoes anteriores relacionados a comandos internos, mas nao ligados a esta revisao estrutural.

## Scripts verificados

- `scripts/sync/notion-cofre-index-import.py`: atualizado para priorizar e classificar a estrutura numerada, mantendo compatibilidade com caminhos legados.
- `scripts/sync/notion-cofre-sync.py`: atualizado para tratar `10-pessoal/` como sensivel/protegido, mantendo protecao para caminhos legados.
- Validacao executada: `python3 -m py_compile scripts/sync/notion-cofre-index-import.py scripts/sync/notion-cofre-sync.py`.

## Referencias legadas mantidas

Referencias `[F0]` a `[F3]` permanecem em:

- registros historicos de `00-central/decisoes.md`;
- trechos historicos de `MEMORY.md`;
- mencoes explicitas de compatibilidade/legado em `MAPA.md`, `AGENTS.md`, `CONSTITUICAO.md`, `00-central/regras-de-uso.md` e `00-central/mapa-do-cofre.md`.

Essas referencias foram mantidas porque fazem parte da rastreabilidade da migracao e nao devem ser apagadas sem revisao humana.

## Riscos restantes

- `MEMORY.md` ainda contem muitos registros historicos com caminhos `[F2]` e `[F3]`; eles devem ser lidos como historico, nao como roteamento atual.
- Alguns documentos arquivados em `90-arquivo/` e memorias antigas ainda podem conter instrucoes legadas; nao foram reescritos para preservar historico.
- Nao foi feita movimentacao fisica de pastas nesta etapa.
- Ha arquivos nao rastreados no worktree que nao pertencem a esta otimizacao e foram preservados sem alteracao.

## Pontos para decisao humana

- Decidir se o antigo papel/subagente `@bibliotecaria` deve ser renomeado formalmente, arquivado ou mantido apenas como historico.
- Decidir se `MEMORY.md` deve receber uma limpeza editorial mais profunda para separar historico antigo de instrucoes vigentes.
- Decidir se scripts de sync com Notion devem rodar apos esta revisao para atualizar o indice externo.

## Conclusao

O Cofre agora esta alinhado nos documentos centrais com a estrutura numerada real e com autonomia operacional responsavel. A revisao preservou compatibilidade, nao apagou nada e reduziu o risco de agentes seguirem regras antigas de F0/F1/F2/F3 como se ainda fossem vigentes.
