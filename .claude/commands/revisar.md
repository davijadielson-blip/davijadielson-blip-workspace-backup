---
description: Lista todos os drafts com revisado: false, agrupados por frente e ordenados por data
---

Faça a varredura completa da fila de revisão. Siga cada passo.

**PASSO 1 — Varredura**

Procure recursivamente em `[F2] memory/outputs/` todos os arquivos `.md` que contenham `revisado: false` no frontmatter.

Use bash para listar:
```bash
grep -rl "revisado: false" "[F2] memory/outputs/" 2>/dev/null | sort
```

**PASSO 2 — Ler e catalogar**

Para cada arquivo encontrado, leia o frontmatter e extraia: `tipo`, `frente`, `data`, `comando`.
Também leia as primeiras 3 linhas de conteúdo após o frontmatter para a prévia.

**PASSO 3 — Exibir a fila agrupada**

Agrupe por `frente`, ordene cada grupo por `data` (mais antigo primeiro). Formato:

```
## Fila de revisão — X drafts pendentes

### [frente]
- YYYY-MM-DD | tipo | `nome-do-arquivo.md`
  > "prévia das primeiras linhas..."

### [frente]
...
```

**PASSO 4 — Resumo final**

Ao final, exiba em negrito:
- Total de drafts pendentes
- Frente com mais pendências
- Draft mais antigo sem revisão (nome + data)

**Importante:** Não marque nada como `revisado: true` sem que Jadielson peça explicitamente. Apenas liste.
