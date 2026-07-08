---
description: Gera manchete estilo jornal para WhatsApp a partir de uma legenda existente
argument-hint: <caminho da legenda> (vazio = usa a última gerada)
---

Gere um resumo estilo manchete de jornal para compartilhar no WhatsApp.

**Argumento recebido:** $ARGUMENTS

**PASSO 1 — Identificar a legenda de origem**

- Se $ARGUMENTS contiver um caminho de arquivo: leia esse arquivo.
- Se $ARGUMENTS estiver vazio: liste os arquivos em `[F2] memory/outputs/legendas/` ordenados por data de modificação e use o mais recente.
- Se não encontrar nenhuma legenda: informe e pergunte qual usar.

**PASSO 2 — Ler e extrair**

Do arquivo encontrado, extraia:
- `frente` (do frontmatter)
- `slug` (do frontmatter ou nome do arquivo)
- Conteúdo principal da legenda (tema, fato central, benefício)

**PASSO 3 — Gerar a manchete**

Regras:
- Estilo manchete de jornal impresso: objetiva e impactante
- Máximo 15 palavras
- Sem emoji
- Sem aspas desnecessárias
- Verbo de ação preferido: presente do indicativo ("Saúde lança...", "Câmara aprova...", "Lógika entrega...")

**PASSO 4 — Salvar**

Caminho: `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-<frente>-<slug>.md`

(Se o arquivo de destino já existir, sobrescreva.)

Frontmatter:
```
---
tipo: resumo-whatsapp
frente: <frente>
gerado-por: claude
comando: /resumo-whats
revisado: false
data: YYYY-MM-DD
legenda-origem: <caminho-do-arquivo-de-origem>
---
```

**PASSO 5 — Exibir**

Mostre a manchete em destaque e confirme o arquivo salvo em uma linha.
