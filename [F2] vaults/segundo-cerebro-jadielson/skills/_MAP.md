---
tipo: mapa
pasta: skills
ultimo-update: 2026-05-28
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 2-cerebro-ia
camada: 4-geracao-ia
---

# Mapa — skills/

## O que mora aqui
Workflows complexos documentados em Markdown — procedimentos que qualquer IA executa do mesmo jeito, tornando o sistema portável entre ferramentas (Claude Code, OpenClaw, GPT, Hermes).

## O que NÃO mora aqui
Slash commands simples (→ `.claude/commands/`). Automações em bash (→ `scripts/`).

## Skills disponíveis
- `cerebro/SKILL.md` — modo briefing: carrega contexto completo do vault antes de operar
- `rotina/SKILL.md` — planejamento do dia: Top 3, tracker de conteúdo por frente
- `salve/SKILL.md` — fechamento de sessão: git add + commit + push + atualiza sessão
- `reindex/SKILL.md` — reindexação forçada ao trocar de LLM ou "atualizar memória"
- `arquivar-outputs/SKILL.md` — move outputs do mês anterior para `_arquivo/YYYY-MM/` mantendo estrutura por frente
- `colheita/SKILL.md` — fecha o Fluxo 3: registra que Jadielson sintetizou um output em nota autoral

## Convenções
- **Naming:** `<skill>/SKILL.md` — uma pasta por skill
- **Formato:** frontmatter + ## Trigger + ## Procedimento + ## Output esperado
- **Portabilidade:** escrito em Markdown puro, sem dependência de ferramenta específica

## Mapas relacionados
- `[[_MAP]]` — raiz do vault
- `[[scripts/_MAP]]` — automações bash

---
*Atualizado: 2026-05-28*