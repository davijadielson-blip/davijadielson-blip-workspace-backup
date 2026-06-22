---
tipo: mapa
pasta: raiz
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: misto
camada: mista
---

# Mapa — Raiz do Vault

## O que mora aqui
Ponto de entrada do segundo cérebro de Jadielson. Contém apenas arquivos de configuração global e os acessos às três grandes divisões do vault: Inbox, Fluxo 1 (cérebro de Jadielson) e Fluxo 2 (cérebro da IA).

## O que NÃO mora aqui
Notas autorais, drafts, outputs, briefings de frente — tudo isso mora dentro das subpastas.

## Estrutura
- `[F0] 0-Inbox/` — captura rápida antes de qualquer fluxo
- `[F1] 1-Permanentes/` — notas atômicas e reflexões processadas
- `[F1] 2-Literatura/` — leituras, cursos, mentorias
- `[F1] 3-Daily/` — diário e planejamento diário
- `[F1] 4-Pessoal/` — vida, família, metas, finanças pessoais
- `[F1] 5-Frentes/` — frentes de trabalho (notas autorais)
- `[F2] memory/` — Fluxo 2: casa da IA, autonomia total
- `scripts/` — automações (brain-boot, cron-jobs)
- `skills/` — workflows complexos documentados
- `Anexos/` — imagens e arquivos anexados pelo Obsidian

## Arquivos globais
- `CLAUDE.md` — constituição do vault (regras, fluxos, frentes, preferências)
- `PROPAGATION.md` — protocolo de propagação de mudanças
- `_MAP.md` — este arquivo

## Convenções
- **Naming:** pastas com prefixo `[F0]`, `[F1]`, `[F2]` indicam o fluxo; `[F2] memory/` e `scripts/` sem prefixo são do Fluxo 2
- **Permissões:** CLAUDE.md e PROPAGATION.md → IA pode sugerir edições, Jadielson decide; `[F1]` → intocável pela IA sem aprovação explícita

## Mapas relacionados
- `[[[F2] memory/_MAP]]` — mapa do Fluxo 2
- `[[[F1] 5-Frentes/_MAP]]` — mapa das frentes de trabalho

---
*Atualizado: 2026-05-10*
