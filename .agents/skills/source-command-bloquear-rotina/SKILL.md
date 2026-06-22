---
name: "source-command-bloquear-rotina"
description: "Cria blocos recorrentes de rotina no Google Calendar com confirmação obrigatória"
---

# source-command-bloquear-rotina

Use this skill when the user asks to run the migrated source command `bloquear-rotina`.

## Command Template

Crie os blocos recorrentes de rotina no Google Calendar. Nada é criado sem confirmação explícita.

**PASSO 1 — Data de início**

```bash
date +"%Y-%m-%d|%u"
```

Calcule a próxima segunda-feira a partir de hoje como data de início dos eventos recorrentes.

**PASSO 2 — Verifique conflitos**

Antes de criar, busque eventos da próxima semana com `mcp__claude_ai_Google_Calendar__list_events` (startTime: próxima segunda, endTime: próximo domingo). Identifique sobreposições de horário e informe.

**PASSO 3 — Lista dos blocos**

| # | Título | Dias | Horário (BRT) | RRULE | colorId |
|---|--------|------|--------------|-------|---------|
| 1 | 🎥 Externo — capturas/reuniões/clientes | Seg, Qua, Sex | 08:00–17:00 | RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR | 7 |
| 2 | 🏢 Agência — produção/planejamento | Ter, Qui, Sáb | 08:00–17:00 | RRULE:FREQ=WEEKLY;BYDAY=TU,TH,SA | 2 |
| 3 | 📋 Revisão do próximo dia | Diário | 17:00–18:00 | RRULE:FREQ=DAILY | 8 |
| 4 | 📱 Alimentação de redes profissionais | Diário | 18:00–19:00 | RRULE:FREQ=DAILY | 6 |
| 5 | 🗓️ Planejamento semanal | Domingo | 08:00–10:00 | RRULE:FREQ=WEEKLY;BYDAY=SU | 5 |
| 6 | 🧹 Manutenção do vault (15min) | Sexta | 16:45–17:00 | RRULE:FREQ=WEEKLY;BYDAY=FR | 8 |

**PASSO 4 — Confirme antes de criar**

Exiba a lista e pergunte quais criar:

```
🗓️ **Blocos de rotina a criar (recorrentes semanais/diários):**

1. 🎥 Externo — Seg/Qua/Sex 08:00–17:00
2. 🏢 Agência — Ter/Qui/Sáb 08:00–17:00
3. 📋 Revisão do próximo dia — diário 17:00–18:00
4. 📱 Alimentação de redes — diário 18:00–19:00
5. 🗓️ Planejamento semanal — domingo 08:00–10:00
6. 🧹 Manutenção do vault — sexta 16:45–17:00

[Sobreposições detectadas: X / Nenhuma sobreposição detectada]

Posso criar todos? Ou informe os números dos que quer criar (ex: "1 2 5 6").
```

**PASSO 5 — Crie os aprovados**

Para cada bloco selecionado, use `mcp__claude_ai_Google_Calendar__create_event`:
- `summary`: título conforme tabela
- `startTime`: próxima ocorrência correta do dia/horário em formato `YYYY-MM-DDTHH:MM:00` (sem offset -03:00)
- `endTime`: mesmo dia, horário de fim — mesmo formato sem offset
- `timeZone`: "America/Maceio"
- `recurrenceData`: [RRULE conforme tabela]
- `colorId`: conforme tabela
- `description`: "Bloco de rotina | Criado via /bloquear-rotina"

**Nota técnica:** para blocos all-day ou com sobreposição detectada, pergunte antes de sobrescrever.

**PASSO 6 — Confirme**

"✅ [N] bloco(s) criado(s). Início: semana de [DD/MM]."
