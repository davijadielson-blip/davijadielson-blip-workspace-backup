---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Notas Tocadas esta Semana

> Notas modificadas nos últimos 7 dias — mostra o que está ativo no momento.

```dataview
TABLE file.folder AS "Pasta", file.mtime AS "Modificado"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 40
```

---

## Modificado hoje

```dataview
TABLE file.folder AS "Pasta", file.mtime AS "Horário"
FROM ""
WHERE file.mtime >= date(today)
SORT file.mtime DESC
```
