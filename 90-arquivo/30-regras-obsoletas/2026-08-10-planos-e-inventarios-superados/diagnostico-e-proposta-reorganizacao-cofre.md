---
tema: diagnóstico e proposta de reorganização do Cofre
conteudo: relatório curto da fase 1, proposta estrutural da fase 2 e pedido de aprovação antes de mover arquivos
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: diagnóstico/proposta
prioridade: máxima
atualizado_em: 2026-07-26
usar_quando: revisar o plano de reorganização segura do Cofre e aprovar próximas etapas
nao_usar_quando: como decisão final de movimentação sem aprovação explícita de Jadielson
---

# Diagnóstico e proposta de reorganização do Cofre — 2026-07-26

## Snapshot realizado
- Snapshot textual salvo em `[F2] archive/snapshots/snapshot-20260726T025413Z.md`.
- Não foi mantido `.tar.gz` no Cofre para respeitar a regra constitucional de somente `.md` no Cofre.

## Fase 1 — Diagnóstico curto

### Principais pastas existentes
- Raiz governamental: `CONSTITUICAO.md`, `AGENTS.md`, `MAPA.md`, `MEMORY.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `PIN.md`.
- Fluxos oficiais atuais: `[F0] 0-Inbox/`, `[F1] ...`, `[F2] memory/`, `[F2] agentes/`, `[F2] archive/`, `[F3] PROJETOS/`.
- Pastas técnicas/operacionais: `.agents/`, `.claude/`, `.codex/`, `scripts/`, `skills/`, `ops/`, `.obsidian/`.
- Pastas paralelas/legadas: `memory/`, `archive/`, `areas/`, `\[F0\] 0-Inbox/`, `\[F2\] memory/`, `[F2]memory/`.
- Nova camada criada sem mover arquivos: `00-central/`, `70-agentes/`, `80-handoffs/`.

### Arquivos importantes
- Lei maior: `CONSTITUICAO.md`.
- Operação: `AGENTS.md`.
- Mapa atual: `MAPA.md` e `_MAP.md`.
- Memória longa: `MEMORY.md`.
- Identidade: `SOUL.md`, `IDENTITY.md`, `PIN.md`.
- Perfil do usuário: `USER.md`.
- Novos arquivos criados: `00-central/regras-de-uso.md`, `00-central/decisoes.md`, `00-central/pendencias.md`, `70-agentes/mapa-dos-agentes.md`, `80-handoffs/template-handoff.md`.

### Duplicidades e sinais de legado
- `memory/` e `[F2] memory/` coexistem; ambos têm dados operacionais.
- `archive/` e `[F2] archive/` coexistem.
- `[F2] agentes/`, `[F2] memory/agents/`, `.agents/`, `.claude/agents/`, `.codex/agents/` coexistem com funções diferentes, mas podem confundir agentes.
- Existem pastas com colchetes escapados literalmente: `\[F0\] 0-Inbox/`, `\[F2\] memory/`.
- Existem arquivos soltos de cockpit/mission-control na raiz, incluindo `.html` e `.png`.
- Foram identificados 12 `.md` sem frontmatter YAML e 236 arquivos não-`.md` fora de `.git`.

### Informações misturadas
- Conteúdo pessoal, profissional, clientes, estudos, scripts, artefatos técnicos e outputs convivem na raiz e em pastas legadas.
- `[F1] 5-Frentes/` mistura clientes/frentes com ideias, referências e produção.
- `[F2] memory/outputs/`, `[F2] memory/projects/` e `[F3] PROJETOS/` se sobrepõem em alguns projetos.

### Riscos de alucinação
- Agentes podem consultar `memory/` legado em vez de `[F2] memory/` ou vice-versa.
- Arquivos sem cabeçalho reduzem precisão semântica.
- Rascunhos, outputs e decisões estão parcialmente misturados; risco de tratar proposta como decisão.
- Materiais externos e capturas importadas sem normalização podem parecer contexto oficial.

### Riscos de vazamento de contexto
- `MEMORY.md`, `USER.md`, finanças, saúde e dados pessoais estão no mesmo Cofre compartilhado por todos os agentes.
- Arquivos sensíveis existem em `scripts/.secrets/` e `.env`; não devem ser expostos nem enviados a agentes sem necessidade.
- Conteúdos de clientes/frentes podem cruzar contexto se agentes receberem pastas amplas demais.

### Deve virar memória central
- Constituição, regras de uso, mapa do Cofre, decisões finais, pendências, glossário e mapa de agentes.
- Protocolos de LOCAL-FIRST, frontmatter obrigatório, handoff e separação fato/hipótese/sugestão.
- Política de acesso mínimo por agente.

### Deve ser separado por área
- Pessoal: saúde, finanças, rotina, família, propósito.
- Profissional: Lógika, carreira, posicionamento, processos de trabalho.
- Estudos: cursos, leituras, fichamentos, planos.
- Projetos: projetos autorais/pessoais/profissionais com status.
- Clientes: Câmara, SINDSS, Saúde São Sebastião, vereadores, etc.
- Processos: checklists, templates, scripts documentados, SOPs.
- Agentes: mapas, prompts, escopos, permissões.
- Handoffs: passagens e logs entre agentes.
- Arquivo: legado, duplicados, backups, itens não classificados.

## Fase 2 — Proposta de estrutura

### `00-central/`
- Serve para: fonte central de governança, mapa, regras, decisões, pendências, glossário.
- Acesso: LÔH e agentes que precisem operar no Cofre.
- Entra: regras, decisões finais, mapa, pendências, glossário.
- Não entra: rascunhos, arquivos pessoais profundos, segredos, outputs de cliente.

### `10-pessoal/`
- Serve para: vida pessoal de Jadielson.
- Acesso: LÔH, Alfred e agentes pessoais quando necessário.
- Entra: saúde, rotina, finanças pessoais, família, propósito.
- Não entra: dados de clientes, estratégia Lógika, scripts técnicos.

### `20-profissional/`
- Serve para: carreira, Lógika, posicionamento e operação profissional interna.
- Acesso: LÔH, C-Levels e agentes profissionais por necessidade.
- Entra: planejamento profissional, Lógika, processos internos.
- Não entra: cliente específico com dados sensíveis; isso vai em `50-clientes/`.

### `30-estudos/`
- Serve para: aprendizagem, cursos, leituras e sínteses.
- Acesso: LÔH, Alfred, agentes de estudos.
- Entra: planos de estudo, fichamentos, materiais processados em `.md`.
- Não entra: downloads binários; devem ir ao Drive.

### `40-projetos/`
- Serve para: projetos autorais e iniciativas com começo/fim.
- Acesso: agentes envolvidos no projeto.
- Entra: briefing, plano, status, próximos passos, decisões do projeto.
- Não entra: memória central do ecossistema nem dados de outros projetos.

### `50-clientes/`
- Serve para: contexto e entregáveis por cliente/frente externa.
- Acesso: apenas agentes alocados ao cliente/frente.
- Entra: briefing, tom de voz, calendário, entregas, referências permitidas.
- Não entra: dados de outros clientes, segredos, financeiro pessoal.

### `60-processos/`
- Serve para: SOPs, checklists, templates, automações documentadas.
- Acesso: agentes operacionais conforme função.
- Entra: processos recorrentes, modelos, guias.
- Não entra: execução avulsa, rascunhos de cliente, credenciais.

### `70-agentes/`
- Serve para: mapa, papéis, permissões e handbooks de agentes.
- Acesso: LÔH e agentes conforme escopo.
- Entra: mapa de agentes, escopo, prompts sem segredos, políticas de contexto.
- Não entra: memória íntima/pessoal nem credenciais.

### `80-handoffs/`
- Serve para: passagens entre agentes.
- Acesso: agente origem, agente destino e LÔH.
- Entra: template e handoffs datados.
- Não entra: decisões finais isoladas; estas vão em `00-central/decisoes.md`.

### `90-arquivo/`
- Serve para: legado, duplicados, antigos, quarentena de revisão.
- Acesso: LÔH e manutenção.
- Entra: itens antigos movidos com aprovação, backups textuais, duplicados para revisão.
- Não entra: arquivo ativo, segredo, binário novo.

## Recomendação de execução segura
1. Aprovar a estrutura-alvo.
2. Corrigir primeiro apenas cabeçalhos YAML dos 12 `.md` sem frontmatter.
3. Criar `00-central/mapa-do-cofre.md` e `00-central/glossario.md`.
4. Mapear arquivos não-`.md` por categoria e propor destino antes de mover.
5. Consolidar duplicidades em lotes: memória, arquivos, agentes, projetos/clientes.
6. Registrar cada lote em `00-central/decisoes.md` e `00-central/pendencias.md`.

## Aguardando aprovação
Nenhum arquivo existente foi movido. Próximo passo depende de aprovação explícita de Jadielson.
