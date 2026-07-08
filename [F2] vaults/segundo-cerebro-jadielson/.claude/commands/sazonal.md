---
description: Lista datas sazonais próximas por frente com sugestões de ângulo de conteúdo
argument-hint: <dias> (padrão: 30)
---

Liste as datas sazonais que se aproximam e sugira ângulos de conteúdo. Siga cada passo.

**Argumento recebido:** $ARGUMENTS
(Se vazio ou não for um número, use 30 dias como padrão)

---

**PASSO 1 — Calcular o intervalo**

```bash
date +"%Y-%m-%d"   # hoje
```

Intervalo: de hoje até hoje + N dias (N = argumento ou 30).

**PASSO 2 — Varrer o banco de datas**

Leia todos os arquivos `.md` em `[F2] memory/databases/datas-sazonais/` (recursivo, incluindo subpastas).

Para cada arquivo, extraia do frontmatter: `data`, `descricao`, `frente`, `tipo`, `observacao`.

Filtre apenas as datas que caem dentro do intervalo calculado.

**PASSO 3 — Organizar por frente**

Agrupe as datas filtradas por `frente`. Ordene por data crescente dentro de cada grupo.

**PASSO 4 — Sugerir ângulos de conteúdo**

Para cada data, sugira **2 a 3 ângulos** de conteúdo concretos e específicos — não genéricos.

Exemplos de ângulos bons:
- "Entrevista com enfermeira sobre prevenção de hepatite B na UBS do Cruzeiro"
- "Reels do Rogério visitando um ACS rural durante o Julho Amarelo"
- "Post do SINDSS com estatística de servidores de saúde no município"

Ângulos ruins (evitar):
- "Post sobre a data"
- "Conteúdo relevante para o público"

**PASSO 5 — Exibir**

Formato de saída:

```
## Datas Sazonais — próximos N dias

### [Frente]

**DD/MM — Descrição da data**
*Tipo: campanha-saude / data-civica / data-comercial / data-religiosa*
> Observação: <se houver>

Ângulos sugeridos:
1. <ângulo específico>
2. <ângulo específico>
3. <ângulo específico>

---
```

Ao final, mostre o total de datas encontradas e pergunte: "Quer que eu gere algum desses conteúdos agora?"
