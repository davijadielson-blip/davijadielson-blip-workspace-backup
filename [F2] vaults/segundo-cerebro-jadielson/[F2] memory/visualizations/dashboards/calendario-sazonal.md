---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Calendário Sazonal

> Datas importantes para produção de conteúdo — todas as frentes.

## Próximas datas (60 dias)

```dataview
TABLE data AS "Data", descricao AS "Descrição", frente AS "Frente", tipo AS "Tipo"
FROM "[F2] claude/databases"
WHERE data >= date(today) AND data <= date(today) + dur(60 days)
SORT data ASC
```

## Todas as datas do ano

```dataview
TABLE data AS "Data", descricao AS "Descrição", frente AS "Frente"
FROM "[F2] claude/databases"
WHERE data >= date(today)
SORT data ASC
```

---

## Como adicionar datas

Crie ou edite arquivos em `[F2] claude/databases/` com frontmatter:

```yaml
---
data: 2026-06-12
descricao: Dia dos Namorados
frente: logika-creative
tipo: data-comercial
---
```
