---
tipo: mapa
pasta: "[F1] 2-Literatura"
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 1-meu-cerebro
camada: 2-literatura
---

# Mapa — [F1] 2-Literatura/

## O que mora aqui
Anotações de livros, cursos, mentorias e referências estudadas por Jadielson. O que foi lido e processado — citações, resumos, aprendizados aplicáveis.

## O que NÃO mora aqui
Reflexões próprias sobre o que foi lido (→ `[F1] 1-Permanentes/`), capturas brutas (→ `[F0] 0-Inbox/`).

## Convenções
- **Naming:** `Autor - Título` ou `Curso - Nome` (kebab-case tolerado)
- **Frontmatter obrigatório (v2):** `tipo: nota-literatura` + `subtipo: curso|livro|mentoria|workshop` + `status: a-iniciar|em-andamento|pausado|concluido`
- **Permissões:** Jadielson escreve; IA lê, nunca edita
- **Templates:** `[F2] memory/templates/template-curso.md` · `template-livro.md` · `template-mentoria.md` · `template-workshop.md`

## Cockpit de estudos
- **Script:** `scripts/cockpit/generate-cockpit-estudos.sh`
- **Output:** `cockpit-estudos.html` na raiz do vault
- O cockpit lê automaticamente todas as notas com `subtipo:` definido no frontmatter.

## Mapas relacionados
- `[[_MAP]]` — mapa-pai (raiz)

---
*Atualizado: 2026-05-19*
