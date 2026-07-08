---
tipo: mapa
pasta: [F2] memory/sessions
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 2-cerebro-ia
camada: 4-geracao-ia
---

# Mapa — [F2] memory/sessions/

## O que mora aqui
Log diário de sessões — o que foi feito, decidido e ficou em aberto em cada dia de trabalho com a IA. Também armazena outputs automáticos dos cron-jobs.

## O que NÃO mora aqui
Daily notes de Jadielson (→ `[F1] 3-Daily/`), decisões arquiteturais (→ `[F2] memory/context/decisoes/`).

## Subpastas
- `daily-briefs/` — briefings diários gerados pelo cron de 7h (`YYYY-MM-DD.md`)
- `weekly/` — planejamentos semanais do cron de domingo (`YYYY-Www.md`)
- `maintenance/` — relatórios de manutenção do cron de sexta (`YYYY-MM-DD.md`)

## Convenções
- **Naming:** `YYYY-MM-DD.md` para sessões manuais; subpastas para outputs de cron
- **Formato:** `## O que foi feito` / `## Decisões` / `## Em aberto`
- **Permissões:** IA cria e atualiza; Jadielson lê e pode anotar

## Mapas relacionados
- `[[[F2] memory/_MAP]]` — mapa-pai
- `[[[F1] 3-Daily/_MAP]]` — daily notes de Jadielson (separado)

---
*Atualizado: 2026-05-10*
