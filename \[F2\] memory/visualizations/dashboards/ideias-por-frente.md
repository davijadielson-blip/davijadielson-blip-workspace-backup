---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Ideias por Frente

> Notas marcadas com `#producao/ideia` — banco de ideias para produção de conteúdo.

```dataview
TABLE frente AS "Frente", file.folder AS "Pasta"
FROM #producao/ideia
SORT frente ASC, file.name ASC
```

---

## Contagem por Frente

```dataview
TABLE length(rows) AS "Total de Ideias"
FROM #producao/ideia
GROUP BY frente
SORT length(rows) DESC
```
