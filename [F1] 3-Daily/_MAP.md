---
tipo: mapa
pasta: "[F1] 3-Daily"
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 1-meu-cerebro
camada: 3-gerenciamento-ia
---

# Mapa — [F1] 3-Daily/

## O que mora aqui
Daily notes e planejamentos semanais de Jadielson. O registro diário do que foi feito, pensado e planejado. Criadas pelo comando `/hoje` com eventos reais do Google Calendar.

## O que NÃO mora aqui
Logs de sessão da IA (→ `[F2] memory/sessions/`), planejamento de frentes (→ `[F1] 5-Frentes/`).

## Subpastas
- `Semanais/` — notas de planejamento semanal (criadas pelo `/planejar-semana`)
- `Pendentes/` — itens que precisam ser processados ou movidos

## Convenções
- **Naming:** `YYYY-MM-DD.md` (novas) ou formato livre (antigas)
- **Frontmatter:** `tipo: daily`, `data:`, `dia-tipo:` (Externo/Agência/Planejamento)
- **Permissões:** Jadielson escreve; IA pode criar a estrutura via `/hoje`, nunca edita o conteúdo autoral

## Mapas relacionados
- `[[_MAP]]` — mapa-pai (raiz)
- `[[[F2] memory/sessions/_MAP]]` — log de sessões da IA (separado)

---
*Atualizado: 2026-05-10*
