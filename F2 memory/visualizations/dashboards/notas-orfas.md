---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Notas Órfãs

> Notas que não têm nenhum link de entrada (não são referenciadas por nenhuma outra nota). Candidatas a integrar, arquivar ou deletar.

```dataview
TABLE file.folder AS "Pasta", file.ctime AS "Criado"
FROM ""
WHERE length(file.inlinks) = 0
AND file.folder != "[F2] claude/visualizations/dashboards"
AND file.name != "Hub"
SORT file.folder ASC, file.name ASC
LIMIT 50
```

> **Nota:** O Obsidian também tem a opção nativa em *Arquivo → Localizar notas órfãs*. Use os dois para cruzar resultados.
