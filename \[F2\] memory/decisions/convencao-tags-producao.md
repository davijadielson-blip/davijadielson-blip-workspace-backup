---
tipo: decisao
gerado-por: claude
data: 2026-05-10
---

# Decisão: Convenção de Tags de Produção

## Sistema de tags

```
#producao/ideia       — conceito ainda não desenvolvido
#producao/roteiro     — texto escrito, aguardando captação
#producao/captura     — gravação/foto realizada, aguardando edição
#producao/edicao      — em edição (Premiere, CapCut etc.)
#producao/revisao     — editado, aguardando aprovação do cliente/Jadielson
#producao/publicado   — publicado em plataforma
```

## Frontmatter complementar recomendado

```yaml
frente: [nome-da-frente]
data-publicacao: YYYY-MM-DD   # apenas em #producao/publicado
```

## Justificativa

Pipeline linear de 6 etapas cobre todo o ciclo de vida de um conteúdo audiovisual. Tags em hierarquia (`#producao/`) permitem consultas granulares ou agregadas via Dataview.

## Regras de uso

- Uma nota = um conteúdo (não misturar dois vídeos na mesma nota)
- Atualizar a tag conforme o conteúdo avança de fase (remover a antiga, adicionar a nova)
- Tag `#producao/publicado` + `data-publicacao` permite histórico de entregas
- Dataview consulta padrão: `FROM #producao/ideia` (sem JS necessário)
