---
description: Cria um evento no Google Calendar com confirmação obrigatória antes de criar
---

Crie um evento no Google Calendar a partir da descrição: $ARGUMENTS

**PASSO 1 — Extraia as informações**

Da descrição em $ARGUMENTS, extraia:
- **Título** (obrigatório)
- **Data** — converta expressões como "amanhã", "sexta-feira", "dia 15", "próxima terça" para YYYY-MM-DD usando a data atual
- **Hora de início** — formato HH:MM
- **Duração** — se não informada, sugira baseado no tipo:

| Tipo detectado | Duração padrão |
|----------------|---------------|
| Reunião / call / alinhamento | 30 min |
| Captura / gravação / filmagem | 1h |
| Cobertura / evento externo | 2h |
| Edição / produção / montagem | 2h |
| Live / apresentação / culto | 1h30 |

- **Local** (opcional)
- **Frente** → para ícone e cor

**Se data ou hora não estiverem claras, pergunte antes de continuar. Não avance sem essas informações.**

**PASSO 2 — Determine ícone e cor pela frente**

| Frente | Ícone | colorId |
|--------|-------|---------|
| Lógika Creative | 🎬 | 7 (Peacock) |
| Câmara Municipal | 🏛️ | 9 (Blueberry) |
| Saúde | 🏥 | 10 (Basil) |
| SINDSS | 🔴 | 6 (Tangerine) |
| Rogério Rocha | 🗳️ | 3 (Grape) |
| Outros vereadores | 📢 | 4 (Flamingo) |
| Pessoal / família | 👨‍👧 | 2 (Sage) |
| Sem classificação | 📅 | 8 (Graphite) |

**PASSO 3 — Confirme antes de criar**

Exiba o resumo e aguarde confirmação explícita ("sim", "pode criar", "confirma"):

```
📅 **Evento a criar:**
- Título: [ícone] [título]
- Data: [DD/MM/YYYY] ([dia da semana])
- Horário: [HH:MM] – [HH:MM] ([duração])
- Local: [se informado / "não informado"]
- Cor: [nome da cor] — [frente]

Posso criar no Google Calendar?
```

**Não crie sem confirmação.**

**PASSO 4 — Crie o evento**

Após confirmação, use `mcp__claude_ai_Google_Calendar__create_event` com os parâmetros abaixo.

> ⚠️ Formato obrigatório dos horários: `YYYY-MM-DDTHH:MM:00` **sem offset** (ex: `2026-05-26T14:00:00`). O fuso é definido pelo campo `timeZone`, não pelo timestamp.

- `summary`: "[ícone] [título]"
- `startTime`: YYYY-MM-DDTHH:MM:00 (sem -03:00)
- `endTime`: YYYY-MM-DDTHH:MM:00 (início + duração, sem -03:00)
- `timeZone`: "America/Maceio"
- `colorId`: número como string — ex: `"7"` (não número inteiro)
- `location`: se informado
- `description`: "Frente: [frente] | Criado via /agendar"

**PASSO 5 — Registre**

Appende em `[F2] memory/logs/eventos-criados.md`.
Se o arquivo não existir, crie com cabeçalho:
```
---
tipo: log-eventos
gerado-por: claude
---

# Log de Eventos Criados

| Data criação | Data evento | Hora | Título | Frente |
|---|---|---|---|---|
```

Adicione a linha: `| HOJE | DD/MM/YYYY | HH:MM | título | frente |`

Confirme: "✅ Evento criado: **[ícone] [título]** — [DD/MM] às [HH:MM]."
