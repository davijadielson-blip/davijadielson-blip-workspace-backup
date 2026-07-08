---
tipo: mapa
pasta: scripts
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 2-cerebro-ia
camada: 4-geracao-ia
---

# Mapa — scripts/

## O que mora aqui
Automações bash do segundo cérebro — brain-boot (executa no SessionStart) e cron-jobs que rodam em horários definidos via launchd (Mac).

## O que NÃO mora aqui
Skills/workflows documentados (→ `skills/`). Hooks do Claude Code (→ `.claude/hooks/`).

## Estrutura
- `brain-boot.sh` — inicialização do vault: git pull + briefing de estado
- `cron-jobs/daily-brief.sh` — roda todo dia 7h
- `cron-jobs/sunday-planning.sh` — roda domingo 8h
- `cron-jobs/friday-maintenance.sh` — roda sexta 16h45
- `cron-jobs/_README.md` — como pausar, editar horários, adicionar novos crons
- `cron-jobs/.logs/` — logs de execução (no .gitignore)

## Convenções
- **Permissões de execução:** `chmod +x` obrigatório em todos os .sh
- **Logs:** `.logs/` excluído do git — apenas local
- **Segurança:** nunca colocar tokens ou senhas nos scripts

## Mapas relacionados
- `[[_MAP]]` — raiz do vault
- `[[skills/_MAP]]` — workflows documentados

---
*Atualizado: 2026-05-10*
