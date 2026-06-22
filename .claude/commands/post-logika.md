---
description: Gera legenda da Lógika Creative com abertura metafórica, mini-case e CTA
argument-hint: <descrição do vídeo ou cliente>
---

Gere um post para o Instagram da Lógika Creative. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente**

Leia `[F2] memory/agents/logika.md` para carregar regras de tom, CTA e hashtags base.

**PASSO 2 — Extrair contexto**

Do argumento, extraia:
- O tipo de vídeo (institucional, clipe, cobertura, documentário...)
- O cliente ou segmento (saúde, câmara, empresa privada...)
- Qualquer detalhe de bastidor mencionado

Se o argumento for vago demais, pergunte: "Tem algum detalhe de bastidor ou elemento visual marcante do vídeo que eu possa usar na abertura?"

**PASSO 3 — Gerar o post**

Estrutura obrigatória:

1. **Abertura metafórica** — conectada ao conteúdo do vídeo. Uma imagem, uma ideia, uma sensação. Não pode ser genérica. (2–3 frases)
2. **Mini-case de bastidor** — o que tinha por trás desse vídeo: o desafio, a escolha criativa, o detalhe que fez diferença. (2–3 frases)
3. **Conexão com o cliente** — o resultado entregue, a história contada. (1–2 frases)
4. **CTA** — variação criativa de: "Transforme suas ideias em impacto visual! Fale com a Lógika Films e leve seu projeto ao próximo nível."

Comprimento total: 120 a 220 palavras.

**PASSO 4 — Gerar 25 hashtags**

Minúsculas, sem acento. Combine as hashtags base do agente com tags específicas do tipo de vídeo e cliente.

**PASSO 5 — Gerar slug e salvar**

Slug: 3–5 palavras sobre o conteúdo em kebab-case.

Caminho: `[F2] memory/outputs/legendas/YYYY-MM-DD-logika-<slug>.md`

Frontmatter:
```
---
tipo: legenda
frente: logika-creative
gerado-por: claude
comando: /post-logika
revisado: false
data: YYYY-MM-DD
slug: <slug>
---
```

**PASSO 6 — Manchete WhatsApp**

Gere manchete ≤15 palavras. Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-logika-<slug>.md`.

**PASSO 7 — Log e exibição**

Logue. Exiba legenda + hashtags + manchete. Pergunte se quer ajustar a metáfora ou o CTA.
