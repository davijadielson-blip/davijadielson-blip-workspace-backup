---
description: Registra ideia diretamente na frente correta em [F1] 5-Frentes/<frente>/Ideias/
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
- `logika` → `[F1] 5-Frentes/Logika-Creative/Ideias/`
- `saude` → `[F1] 5-Frentes/Saude-Sao-Sebastiao/Ideias/`
- `camara` → `[F1] 5-Frentes/Camara-Municipal/Ideias/`
- `sindss` → `[F1] 5-Frentes/SINDSS/Ideias/`
- `rogerio` → `[F1] 5-Frentes/Inativos/Rogerio-Rocha/Ideias/`
- `alem-da-foto` → `[F1] 5-Frentes/Alem-da-Foto/Ideias/`
- `lives` → `[F1] 5-Frentes/Lives-Louvor-Reflexao/Ideias/`
- `outros` → `[F1] 5-Frentes/Outros-Vereadores/Ideias/`
- `pessoal` → `[F1] 4-Pessoal/`

Se a frente não for reconhecida, pergunte antes de continuar.

**PASSO 2 — Gerar slug e obter data**

```bash
date +"%Y-%m-%d"
```

Slug: 3 a 5 palavras da ideia em kebab-case, sem acento, minúsculas.

**PASSO 3 — Criar o arquivo**

Caminho: `[F1] 5-Frentes/<pasta-da-frente>/YYYY-MM-DD-<slug>.md`

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
