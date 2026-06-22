---
tipo: dashboard
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Pipeline de Produção

> Visão completa de todos os conteúdos em cada fase do pipeline.

## Ideias

```dataview
TABLE frente AS "Frente"
FROM #producao/ideia
SORT frente ASC
```

## Roteiro

```dataview
TABLE frente AS "Frente"
FROM #producao/roteiro
SORT frente ASC
```

## Captação

```dataview
TABLE frente AS "Frente"
FROM #producao/captura
SORT frente ASC
```

## Edição

```dataview
TABLE frente AS "Frente"
FROM #producao/edicao
SORT frente ASC
```

## Revisão

```dataview
TABLE frente AS "Frente"
FROM #producao/revisao
SORT frente ASC
```

## Publicados

```dataview
TABLE frente AS "Frente", data-publicacao AS "Publicado"
FROM #producao/publicado
SORT data-publicacao DESC
LIMIT 20
```
