---
description: Busca um tema no vault inteiro e retorna resultados agrupados por camada
argument-hint: <tema ou palavra-chave>
---

Faça uma busca completa no vault pelo tema indicado. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

Se $ARGUMENTS estiver vazio, pergunte: "O que quer buscar?"

---

**PASSO 1 — Executar a busca**

Busque o termo em todo o vault usando grep recursivo:

```bash
grep -ril "$ARGUMENTS" \
  "[F1] 1-Permanentes/" \
  "[F1] 2-Literatura/" \
  "[F1] 3-Daily/" \
  "[F1] 4-Pessoal/" \
  "[F1] 5-Frentes/" \
  "[F2] memory/outputs/" \
  "[F2] memory/agents/" \
  "[F2] memory/databases/" \
  2>/dev/null | sort
```

**PASSO 2 — Classificar por camada**

Para cada arquivo encontrado, classifique:

- **Camada 1 — Notas permanentes:** arquivos em `1-Permanentes/`
- **Camada 2 — Literatura:** arquivos em `2-Literatura/`
- **Camada 3 — Daily/Pessoal/Frentes:** arquivos em `3-Daily/`, `4-Pessoal/`, `5-Frentes/`
- **Camada 4 — Outputs da IA:** arquivos em `[F2] memory/outputs/`
- **Contexto operacional:** arquivos em `[F2] memory/agents/` ou `databases/`

**PASSO 3 — Ler contexto de cada resultado**

Para cada arquivo encontrado (máximo 15 resultados no total), leia as linhas que contêm o termo e as 2 linhas ao redor para dar contexto.

**PASSO 4 — Exibir agrupado**

```
## Busca: "<tema>" — X resultados

### 📘 Notas permanentes (Camada 1)
- [[nome-da-nota]] — "<trecho com o termo>"

### 📗 Literatura (Camada 2)
- [[nome-da-nota]] — "<trecho>"

### 📋 Frentes / Daily / Pessoal (Camada 3)
- [[nome-da-nota]] — "<trecho>"

### 🤖 Outputs da IA (Camada 4)
- [[nome-do-draft]] — "<trecho>"

### ⚙️ Contexto operacional
- [[nome-do-agente]] — "<trecho>"
```

**PASSO 5 — Conexões observadas**

Após listar, escreva em 2 a 4 linhas: "Conexões observadas:" — o que há em comum entre os resultados, padrões, sobreposições ou lacunas relevantes.

**PASSO 6 — Perguntar**

"Quer que eu aprofunde algum dos resultados ou busque por outro termo relacionado?"
