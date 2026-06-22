---
description: Gera post da Câmara Municipal conforme tipo — pergunta detalhes antes de gerar
argument-hint: <tipo>: aniversario | projeto-aprovado | biografia | sessao | rotina-presidente | procuradoria
---

Gere um post para a Câmara Municipal de São Sebastião. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente**

Leia `[F2] memory/agents/camara.md` para carregar tom, linha editorial e restrições.

**PASSO 2 — Identificar o tipo**

Tipos válidos: `aniversario`, `projeto-aprovado`, `biografia`, `sessao`, `rotina-presidente`, `procuradoria`.

Se $ARGUMENTS estiver vazio ou o tipo for inválido, pergunte: "Qual o tipo de post? (aniversario / projeto-aprovado / biografia / sessao / rotina-presidente / procuradoria)"

**PASSO 3 — Perguntar os detalhes específicos**

Antes de gerar, faça as perguntas necessárias conforme o tipo:

- **aniversario** → "Nome do vereador? Quantos anos? Cargo atual?"
- **projeto-aprovado** → "Nome do projeto? O que ele propõe? Quem assinou? Aprovado por unanimidade?"
- **biografia** → "Nome do vereador? Trajetória (resumo)? Bandeiras principais?"
- **sessao** → "Data da sessão? Pautas principais? Votações relevantes?"
- **rotina-presidente** → "Nome do presidente? Ação ou evento específico?"
- **procuradoria** → "Assunto jurídico ou institucional? Qual o comunicado?"

Espere a resposta antes de continuar.

**PASSO 4 — Gerar o post**

Com as informações recebidas, gere o texto seguindo o tom do agente:
- Institucional, claro, respeitoso
- Informação objetiva primeiro
- Linguagem para o cidadão comum
- Comprimento: 100 a 200 palavras
- ❌ Sem linguagem de campanha ou eleição

**PASSO 5 — Gerar slug e salvar**

Slug: tipo + detalhe principal em kebab-case.
Exemplo: `aniversario-vereador-josi`, `projeto-aprovado-pavimentacao`

Caminho: `[F2] memory/outputs/drafts/YYYY-MM-DD-camara-<slug>.md`

Frontmatter:
```
---
tipo: post
frente: camara-municipal
gerado-por: claude
comando: /post-camara
revisado: false
data: YYYY-MM-DD
subtipo: <tipo>
slug: <slug>
---
```

**PASSO 6 — Manchete WhatsApp**

Gere manchete ≤15 palavras estilo jornal. Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-camara-<slug>.md`.

**PASSO 7 — Log e exibição**

Logue em `[F2] memory/logs/comandos/YYYY-MM-DD-post-camara-<slug>.md`.
Exiba post + manchete. Pergunte se quer ajustar.
