---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Drafts Pendentes de Revisão

> Todos os outputs gerados pela IA que ainda não foram revisados por Jadielson.

```dataview
TABLE frente AS "Frente", data-criacao AS "Criado em", file.folder AS "Pasta"
FROM "[F2] claude/outputs"
WHERE revisado = false
SORT data-criacao DESC
```

---

## Por Frente

```dataview
TABLE rows.file.link AS "Arquivo", rows.data-criacao AS "Data"
FROM "[F2] claude/outputs"
WHERE revisado = false
GROUP BY frente
SORT rows.data-criacao DESC
```
