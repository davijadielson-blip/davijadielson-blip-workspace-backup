---
description: Gera legenda Instagram + 25 hashtags + manchete WhatsApp para a frente indicada
argument-hint: <frente> <descrição do vídeo>
---

Gere uma legenda completa para Instagram. Execute cada passo na ordem.

**Argumentos recebidos:** $ARGUMENTS
(Primeiro elemento = frente; o restante = descrição do vídeo ou contexto)

---

**PASSO 1 — Identificar frente e descrição**

Separe:
- `<frente>` = primeira palavra dos argumentos
- `<descricao>` = tudo que veio depois

Frentes válidas: `logika`, `saude`, `camara`, `sindss`, `rogerio`, `alem-da-foto`, `lives`.
Se a frente não for reconhecida ou estiver ausente, **pergunte antes de continuar**.

**PASSO 2 — Carregar briefing da frente**

Leia o arquivo `[F2] memory/agents/<frente>.md` para carregar tom, regras, CTA e hashtags temáticas da frente. Se o arquivo não existir, informe e pergunte como proceder.

**PASSO 3 — Gerar slug**

Crie um slug de 3 a 5 palavras em kebab-case, sem acento, minúsculas, a partir da descrição.
Exemplo: "vídeo institucional da prefeitura" → `video-institucional-prefeitura`

**PASSO 4 — Gerar a legenda**

Aplique as regras carregadas do agente. Regras globais obrigatórias:
- Português brasileiro
- Conteúdo de cliente em 1ª pessoa (exceto Lógika, que pode usar 3ª)
- Comprimento: 150 a 300 palavras

Regras específicas por frente:
- **logika** → abrir com metáfora conectada ao vídeo + mini-case de bastidor + CTA ao direct
- **rogerio** → storytelling (gancho → contexto → presença → reflexão → CTA) + 1ª pessoa + slogan "Sempre presente com o Povo!" no fechamento + ❌ zero menção a eleição, voto, campanha
- **saude / camara / sindss** → institucional, informação primeiro, sucinto, claro
- **alem-da-foto** → narrativa histórica, contemplativo, convite à memória
- **lives** → espiritual, edificante, convite à live ou à reflexão

**PASSO 5 — Gerar 25 hashtags**

Minúsculas, sem acento, sem espaço entre palavras compostas. Combine as hashtags temáticas do agente com tags específicas do conteúdo. Total exato: **25 hashtags**.

**PASSO 6 — Salvar a legenda**

Caminho: `[F2] memory/outputs/legendas/YYYY-MM-DD-<frente>-<slug>.md`

Frontmatter:
```
---
tipo: legenda
frente: <frente>
gerado-por: claude
comando: /legenda
revisado: false
data: YYYY-MM-DD
slug: <slug>
---
```

Estrutura do corpo:
```
# Legenda — <descrição resumida>

<legenda gerada>

---

#tag1 #tag2 ... (25 no total, numa única linha)
```

**PASSO 7 — Gerar manchete WhatsApp**

Crie uma manchete estilo manchete de jornal:
- Objetiva, impactante
- Máximo 15 palavras
- Sem emoji, sem aspas desnecessárias
- Foco no fato ou benefício principal

Salve em `[F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-<frente>-<slug>.md` com frontmatter equivalente (tipo: resumo-whatsapp).

**PASSO 8 — Log**

Crie `[F2] memory/logs/comandos/YYYY-MM-DD-legenda-<slug>.md`:
```
---
comando: /legenda
frente: <frente>
slug: <slug>
data: YYYY-MM-DD
arquivos:
  - [F2] memory/outputs/legendas/YYYY-MM-DD-<frente>-<slug>.md
  - [F2] memory/outputs/resumos-whatsapp/YYYY-MM-DD-<frente>-<slug>.md
---
```

**PASSO 9 — Mostrar e perguntar**

Exiba no chat:
1. A legenda completa com hashtags
2. A manchete WhatsApp

Pergunte: "Quer ajustar algo antes de marcar como pronto para revisão?"
Se sim → faça os ajustes e salve novamente.
Se não → confirme: "Arquivos salvos em outputs/legendas/ e outputs/resumos-whatsapp/."
