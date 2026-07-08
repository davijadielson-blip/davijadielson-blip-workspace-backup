---
tipo: mapa
pasta: memory
ultimo-update: 2026-06-04
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 2-cerebro-ia
camada: 4-geracao-ia
---

# Mapa — [F2] memory/

## O que mora aqui
Fluxo 2 completo — tudo que a IA cria, edita e mantém. Autonomia total dentro desta pasta. Nada aqui vai direto para publicação sem revisão de Jadielson.

## O que NÃO mora aqui
Notas autorais de Jadielson. Qualquer nota que exige a voz, o pensamento ou a decisão dele mora em `[F1]`.

## Subpastas
- `agents/` — briefings operacionais de cada frente (lidos pelos subagents)
- `context/` — estado atual: pendências, deadlines, pessoas, negócio, decisões
- `databases/` — bancos de dados permanentes (aniversariantes, datas sazonais, regras)
- `decisions/` — decisões arquiteturais antigas (migradas para `context/decisoes/`)
- `outputs/` — todos os drafts gerados: legendas, roteiros, briefings
- `research/` — pesquisas e referências coletadas pela IA
- `sessions/` — log diário de sessões (substitui `logs/`)
- `templates/` — modelos reutilizáveis para outputs
- `visualizations/` — Hub, Canvas, dashboards Dataview, diagramas Mermaid

## Convenções
- **Frontmatter obrigatório:** `tipo`, `gerado-por: claude`, `revisado: false/true`
- **Naming outputs:** `YYYY-MM-DD-frente-slug.md`
- **Permissões:** IA escreve livremente aqui; Jadielson valida e marca `revisado: true`

## Agentes operacionais em configuração
- `agents/arca.md` — Arca, especialista do Segundo Cérebro/sistema de conhecimento da Central Pessoal, supervisionada por Alfred e integrada à Lôh.

## Mapas relacionados
- `[[_MAP]]` — mapa-pai (raiz)
- `[[[F2] memory/context/_MAP]]` — estado operacional
- `[[[F2] memory/outputs/_MAP]]` — drafts e pipeline
- `[[[F2] memory/sessions/_MAP]]` — log de sessões

---
*Atualizado: 2026-06-04*
