---
tema: 07 20 superpowers obra captura instalacao
atualizado_em: 2026-07-22
---

# Superpowers (obra/superpowers) — captura e instalação

Data: 2026-07-20
Pedido: “o que dar para usar dos super poderes? capte e instale tudo.”
Origem externa: https://github.com/obra/superpowers

## O que foi feito

1. Consultei o Cofre primeiro, conforme Constituição.
2. Como `memory_search` estava indisponível por erro de chave de embeddings, fiz fallback por leitura direta (`CONSTITUICAO.md`, `MAPA.md`) e `grep` no Cofre.
3. Consultei Tavily/GitHub para obter informações atuais do repositório.
4. Clonei o repositório temporariamente em `/tmp/superpowers` para inspeção.
5. Instalei no Cofre uma biblioteca Markdown de Superpowers em:

`/data/.openclaw/workspace/skills/superpowers/`

Somente arquivos `.md` foram persistidos no Cofre, respeitando a regra de não salvar binários/JSON/JS/TS/etc. no Cofre.

## Status de instalação

- ✅ Captura concluída.
- ✅ Skills/documentação Markdown instaladas no Cofre.
- ⚠️ Plugin nativo por marketplace/CLI não instalado neste ambiente porque não foram detectados comandos compatíveis: `codex`, `claude`, `agy`, `droid`, `copilot`, `pi`, `cursor`.
- ✅ O conteúdo já pode ser usado operacionalmente por consulta às skills em Markdown.

## Superpoderes úteis disponíveis

### Fluxo de criação e engenharia
- `brainstorming` — lapidar ideia antes de sair executando.
- `writing-plans` — transformar decisão em plano executável detalhado.
- `executing-plans` — executar plano em lotes com checkpoints.
- `subagent-driven-development` — dividir execução entre subagentes com revisão.
- `dispatching-parallel-agents` — paralelizar frentes de trabalho.

### Qualidade de código/processo
- `test-driven-development` — ciclo RED/GREEN/REFACTOR.
- `systematic-debugging` — depuração por causa raiz, sem chute.
- `verification-before-completion` — não declarar pronto sem verificar.
- `requesting-code-review` — pedir revisão estruturada.
- `receiving-code-review` — responder/incorporar feedback.

### Git e finalização
- `using-git-worktrees` — branches/worktrees isoladas para trabalho seguro.
- `finishing-a-development-branch` — finalizar branch, testar, decidir merge/PR/descarte.

### Meta
- `using-superpowers` — guia de uso do sistema.
- `writing-skills` — criar novas skills com padrão bom.

## Como usar daqui pra frente

Antes de tarefas complexas de código, produto, automação ou análise técnica, consultar:

`skills/superpowers/skills/using-superpowers/SKILL.md`

Depois aplicar a skill adequada, por exemplo:

- Ideia vaga → `brainstorming`
- Implementação grande → `writing-plans` + `executing-plans`/`subagent-driven-development`
- Bug → `systematic-debugging`
- Correção concluída → `verification-before-completion`
- Desenvolvimento com testes → `test-driven-development`

## Observação importante

O repositório tem instaladores/plugins para Claude Code, Antigravity, Codex App/CLI, Cursor, Factory Droid, GitHub Copilot CLI, Kimi Code, OpenCode e Pi. A instalação nativa depende do harness usado. Neste ambiente atual, usei a rota segura: importar as skills Markdown para o Cofre.

## Fontes

- Cofre: `CONSTITUICAO.md`, `MAPA.md`, busca direta por `grep`.
- Tavily/GitHub: `https://github.com/obra/superpowers`.
- Ferramenta local: clone temporário em `/tmp/superpowers` e instalação Markdown em `skills/superpowers/`.
