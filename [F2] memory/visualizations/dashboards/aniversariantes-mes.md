---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Aniversariantes do Mês

> Aniversários do mês atual — útil para conteúdo de homenagem e relacionamento.

```dataview
TABLE nome AS "Nome", cargo AS "Cargo", dateformat(date(aniversario), "dd/MM") AS "Data"
FROM "[F2] claude/databases"
WHERE tipo = "aniversario" AND month(date(aniversario)) = month(date(today))
SORT date(aniversario).day ASC
```

---

## Todos os aniversários do ano

```dataview
TABLE nome AS "Nome", cargo AS "Cargo", dateformat(date(aniversario), "dd/MM") AS "Data"
FROM "[F2] claude/databases"
WHERE tipo = "aniversario"
SORT date(aniversario).month ASC, date(aniversario).day ASC
```

---

## Como adicionar aniversariantes

Crie arquivos em `[F2] claude/databases/aniversariantes/` com frontmatter:

```yaml
---
nome: [nome da pessoa]
aniversario: 1990-07-15
frente: camara-municipal
cargo: Vereador
tipo: aniversario
---
```
