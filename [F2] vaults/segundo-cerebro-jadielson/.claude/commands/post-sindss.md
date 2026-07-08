---
description: Gera conteúdo do SINDSS respeitando calendário editorial seg-sex
argument-hint: <tipo>: feed | reel-viral | reel-educativo | depoimento-sexta
---

Gere conteúdo para o SINDSS. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente e calendário**

Leia em paralelo:
- `[F2] memory/agents/sindss.md` → tom, regras editoriais, tipos de conteúdo
- `[F2] memory/databases/calendario-sazonal-sindss.md` → datas próximas relevantes

**PASSO 2 — Verificar o dia da semana**

```bash
date +"%A"
```

- Segunda a Quinta → tipos válidos: `feed`, `reel-viral`, `reel-educativo`
- Sexta → tipo preferencial: `depoimento-sexta` (mas aceita outros se explicitamente pedido)
- Se o tipo passado conflitar com o dia, informe e confirme antes de continuar

**PASSO 3 — Identificar o tipo**

Se $ARGUMENTS estiver vazio, pergunte: "Qual formato? (feed / reel-viral / reel-educativo / depoimento-sexta)"
Se o tipo for inválido, corrija e confirme.

**PASSO 4 — Perguntar o tema**

Pergunte: "Qual o tema ou assunto do conteúdo?" (a menos que o argumento já contenha o tema).

Verifique no calendário se há alguma data sazonal relevante nos próximos 7 dias — se houver, sugira como ângulo antes de gerar.

**PASSO 5 — Gerar o conteúdo**

Conforme o tipo:

- **feed** → post informativo, claro, defesa de direito ou informação útil ao servidor. 100–180 palavras.
- **reel-viral** → gancho nos 3 primeiros segundos + desenvolvimento rápido + CTA. Máx. 60 palavras de roteiro. Tom combativo mas positivo.
- **reel-educativo** → explica um direito trabalhista, lei ou benefício em linguagem simples. Estrutura: problema → explicação → solução. 80–150 palavras.
- **depoimento-sexta** → 1ª pessoa do servidor. Estrutura: quem sou → dificuldade vivida → como o SINDSS ajudou ou o que sinto pelo serviço público → mensagem final. 150–250 palavras.

**PASSO 6 — Gerar slug e salvar**

Slug: tipo + tema em kebab-case.

Caminho: `[F2] memory/outputs/drafts/YYYY-MM-DD-sindss-<slug>.md`

Frontmatter:
```
---
tipo: post
frente: sindss
gerado-por: claude
comando: /post-sindss
revisado: false
data: YYYY-MM-DD
subtipo: <tipo>
slug: <slug>
---
```

**PASSO 7 — Manchete WhatsApp** (para feed e depoimento)

Gere manchete ≤15 palavras. Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-sindss-<slug>.md`.

**PASSO 8 — Log e exibição**

Logue. Exiba o conteúdo gerado. Pergunte se quer ajustar.
