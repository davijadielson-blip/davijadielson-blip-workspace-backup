---
description: Gera post do Rogério Rocha em 1ª pessoa com storytelling, sem menção à eleição
argument-hint: <tipo>: proposta | execucao | presenca | depoimento-apoiador
---

Gere um post para o vereador Rogério Rocha. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente**

Leia `[F2] memory/agents/rogerio.md`. Internalize a regra crítica: **zero menção a eleição, voto, campanha**.

**PASSO 2 — Identificar o tipo**

Tipos válidos: `proposta`, `execucao`, `presenca`, `depoimento-apoiador`.
Se ausente ou inválido, pergunte antes de continuar.

**PASSO 3 — Perguntar os detalhes**

Conforme o tipo:
- **proposta** → "Qual a proposta? O que ela resolve? Quem se beneficia?"
- **execucao** → "O que foi feito ou entregue? Onde? Para quem?"
- **presenca** → "Onde foi? Qual comunidade ou evento? O que encontrou lá?"
- **depoimento-apoiador** → "Quem é o apoiador (perfil geral, sem nome se preferir)? O que disse?"

Espere a resposta.

**PASSO 4 — Gerar o post**

Regras absolutas:
- ✅ 1ª pessoa: "Hoje estive...", "Quando cheguei...", "Vi de perto..."
- ✅ Storytelling: situação → presença → impacto → reflexão
- ✅ Slogan "Sempre presente com o Povo!" no fechamento
- ❌ Nenhuma menção a eleição, voto, campanha, candidatura, urna, próximas eleições

Comprimento: 120 a 220 palavras.

**PASSO 5 — Gerar slug e salvar**

Slug: tipo + detalhe em kebab-case.

Caminho: `[F2] memory/outputs/drafts/YYYY-MM-DD-rogerio-<slug>.md`

Frontmatter:
```
---
tipo: post
frente: rogerio-rocha
gerado-por: claude
comando: /post-rogerio
revisado: false
data: YYYY-MM-DD
subtipo: <tipo>
slug: <slug>
---
```

**PASSO 6 — Manchete WhatsApp**

Gere manchete ≤15 palavras. Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-rogerio-<slug>.md`.

**PASSO 7 — Log e exibição**

Logue. Exiba post + manchete. Pergunte: "Quer ajustar tom, algum trecho ou o CTA?"
