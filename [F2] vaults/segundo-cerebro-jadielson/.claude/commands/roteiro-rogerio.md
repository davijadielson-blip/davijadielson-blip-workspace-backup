---
description: Gera roteiro de vídeo completo para Rogério Rocha com storytelling e estrutura de takes
argument-hint: <tema, povoado ou ação>
---

Gere um roteiro de vídeo para o vereador Rogério Rocha. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente**

Leia `[F2] memory/agents/rogerio.md` para carregar tom, regras e a restrição crítica sobre eleição.

**PASSO 2 — Gerar slug**

3 a 5 palavras em kebab-case sem acento a partir do argumento.
Exemplo: "visita ao povoado Mata" → `visita-povoado-mata`

**PASSO 3 — Gerar o roteiro**

Estrutura obrigatória em 5 atos, sempre em **1ª pessoa**, tom acolhedor e inspirador:

```
## ATO 1 — GANCHO (0–5 seg)
<Abertura com lugar, situação ou imagem forte. Frase que prende.>

## ATO 2 — CONTEXTO (5–20 seg)
<Quem são as pessoas, qual é a realidade do lugar, o que foi encontrado.>

## ATO 3 — PRESENÇA (20–40 seg)
<O que Rogério fez, está fazendo ou está propondo. Concreto, específico.>

## ATO 4 — REFLEXÃO (40–55 seg)
<O que essa ação significa para a comunidade. Tom esperançoso, não grandioso.>

## ATO 5 — CTA + SLOGAN (55–60 seg)
<Convite a acompanhar o trabalho. Fechar com: "Sempre presente com o Povo!">
```

**Após o roteiro, inclua a seção de takes:**

```
## Sugestão de Takes

| # | Tipo | Descrição |
|---|------|-----------|
| 1 | Cabeça / Talking head | Rogério olha pra câmera — ATO 1 e 5 |
| 2 | B-roll ambiente | Imagens do lugar / comunidade |
| 3 | B-roll ação | Rogério interagindo com moradores |
| 4 | Detalhe | Close em rosto, mãos, objeto relevante |
| 5 | Depoimento | Morador ou servidor (opcional) |
```

**Regras inegociáveis:**
- ❌ Nenhuma menção a eleição, voto, campanha, candidatura, urna
- ✅ Slogan "Sempre presente com o Povo!" sempre no fechamento
- ✅ 1ª pessoa em todo o roteiro

**PASSO 4 — Salvar**

Caminho: `[F2] memory/outputs/roteiros/YYYY-MM-DD-rogerio-<slug>.md`

Frontmatter:
```
---
tipo: roteiro
frente: rogerio-rocha
gerado-por: claude
comando: /roteiro-rogerio
revisado: false
data: YYYY-MM-DD
slug: <slug>
tema: $ARGUMENTS
---
```

**PASSO 5 — Log**

Crie `[F2] memory/logs/comandos/YYYY-MM-DD-roteiro-rogerio-<slug>.md` com referência ao arquivo gerado.

**PASSO 6 — Exibir e perguntar**

Mostre o roteiro completo com os takes. Pergunte: "Quer ajustar tom, algum ato ou os takes antes de salvar como revisado?"
