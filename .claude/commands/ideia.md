---
description: Registra ideia diretamente na frente correta em 50-clientes/<frente>/Ideias/
argument-hint: <frente> <texto da ideia>
---

Registre a ideia na frente correta. Sem ritual — rápido e direto.

**Argumento recebido:** $ARGUMENTS
(Primeiro elemento = frente; o restante = texto da ideia)

---

**PASSO 1 — Identificar frente e texto**

Separe:
- `<frente>` = primeira palavra
- `<ideia>` = tudo que veio depois

Mapeamento de frente para pasta:
- `logika` → `20-profissional/10-logika/Ideias/`
- `saude` → `50-clientes/10-saude-sao-sebastiao/Ideias/`
- `camara` → `50-clientes/20-camara-municipal/Ideias/`
- `sindss` → `50-clientes/30-sindss/Ideias/`
- `rogerio` → `50-clientes/40-outros-vereadores/rogerio-rocha/Ideias/`
- `alem-da-foto` → `50-clientes/50-outros-clientes/20-fontes/alem-da-foto/Ideias/`
- `lives` → `40-projetos/30-projetos-autorais/lives-louvor-reflexao/Ideias/`
- `outros` → `50-clientes/40-outros-vereadores/Ideias/`
- `pessoal` → `10-pessoal/`

Se a frente não for reconhecida, pergunte antes de continuar.

**PASSO 2 — Gerar slug e obter data**

```bash
date +"%Y-%m-%d"
```

Slug: 3 a 5 palavras da ideia em kebab-case, sem acento, minúsculas.

**PASSO 3 — Criar o arquivo**

Caminho: `50-clientes/<pasta-da-frente>/YYYY-MM-DD-<slug>.md`

Conteúdo:
```
---
tipo: ideia
frente: <frente>
tags: [ideia, <frente>]
producao: "#producao/ideia"
data: YYYY-MM-DD
---

# <primeiras palavras da ideia como título>

<texto completo da ideia, exatamente como foi passado no argumento>

---
*Registrado via /ideia em YYYY-MM-DD*
```

**PASSO 4 — Responder em uma linha**

"✓ Ideia salva em `<caminho-do-arquivo>`."

Nada mais. Não expanda, não reformule a ideia, não pergunte.
