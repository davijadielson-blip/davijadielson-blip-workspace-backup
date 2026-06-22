---
description: Gera comunicação institucional da Secretaria de Saúde de São Sebastião
argument-hint: <campanha ou serviço>: ex: outubro-rosa, entrega-exames, saude-em-movimento
---

Gere comunicação institucional para a Secretaria de Saúde de São Sebastião/AL. Siga cada passo.

**Argumento recebido:** $ARGUMENTS

---

**PASSO 1 — Carregar agente**

Leia `[F2] memory/agents/saude.md` para carregar tom, estrutura preferida e restrições.

**PASSO 2 — Identificar o tema**

Se $ARGUMENTS contiver o tema, use-o. Se for vago ou ausente, pergunte:
"Qual o tema ou serviço? (ex.: campanha do mês, unidade em destaque, entrega de exames, ação preventiva...)"

Verifique também se o tema corresponde a alguma campanha mensal de saúde nos arquivos de `[F2] memory/databases/datas-sazonais/campanhas-saude/` — se sim, leia o arquivo para contexto adicional.

**PASSO 3 — Perguntar detalhes específicos**

Antes de gerar, pergunte:
- "Há dados ou números concretos? (ex.: X vacinas aplicadas, Y atendimentos...)"
- "Qual unidade ou setor é o foco? (PSF, EMULTI, CAPS, Farmácia...)"
- "Há orientação de acesso para a população? (endereço, horário, telefone...)"

Se não houver dados, avise que gerará sem eles e que devem ser preenchidos antes de publicar.

**PASSO 4 — Gerar o conteúdo**

Estrutura obrigatória:
1. **Informação objetiva** — o quê, onde, quando (primeira frase sempre)
2. **Benefício ou contexto** — por que isso importa para a população
3. **Orientação de acesso** — como a população chega ao serviço (se aplicável)

Tom: institucional, claro, acessível. Sem jargões técnicos excessivos.
Comprimento: 80 a 160 palavras.

**Atenção:** Se o conteúdo envolver dados de saúde pública ou falas de autoridades, adicione ao final do arquivo: `⚠️ Validar dados com Jadielson antes de publicar.`

**PASSO 5 — Gerar slug e salvar**

Slug: tema em kebab-case.

Caminho: `[F2] memory/outputs/drafts/YYYY-MM-DD-saude-<slug>.md`

Frontmatter:
```
---
tipo: post
frente: saude-sao-sebastiao
gerado-por: claude
comando: /post-saude
revisado: false
data: YYYY-MM-DD
slug: <slug>
---
```

**PASSO 6 — Manchete WhatsApp**

Gere manchete ≤15 palavras. Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-saude-<slug>.md`.

**PASSO 7 — Log e exibição**

Logue. Exiba o post + manchete. Se houver aviso de validação, destaque-o em negrito.
