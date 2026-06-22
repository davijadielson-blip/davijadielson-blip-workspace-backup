---
description: Lista eventos do Google Calendar dos próximos N dias classificados por frente
---

Liste os eventos do Google Calendar. $ARGUMENTS = número de dias à frente (padrão: 7 se vazio).

**PASSO 1 — Defina o intervalo**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

- N = valor numérico em $ARGUMENTS; se vazio ou não-numérico, use 7.
- `startTime`: hoje às 00:00:00-03:00
- `endTime`: data de hoje + N dias às 23:59:59-03:00

**PASSO 2 — Busque os eventos**

Use `mcp__claude_ai_Google_Calendar__list_events`:
- startTime / endTime conforme acima
- orderBy: startTime
- timeZone: America/Maceio
- pageSize: 50

**PASSO 3 — Classifique cada evento**

Leia `[F2] memory/databases/regras-classificacao-agenda.md` e aplique o ícone correto a cada evento baseado em palavras-chave do título e descrição.

**PASSO 4 — Determine o tipo de cada dia**

Para cada dia do intervalo:
- Seg/Qua/Sex → 🎥 Externo
- Ter/Qui/Sáb → 🏢 Agência
- Dom → 🗓️ Planejamento

**PASSO 5 — Exiba agrupado por dia**

Formato de saída:
```
## 📅 Próximos N dias (DD/MM – DD/MM)

### Seg, 10/05 — 🎥 Externo
- 04:00–07:00 👨‍👧 Bloco 1: Fundação Pessoal
- 09:30–10:00 🎬 Reunião cliente X
  📍 São Sebastião

### Ter, 11/05 — 🏢 Agência
*(agenda livre)*
```

Regras de exibição:
- Eventos recorrentes da rotina base (Bloco 1, Culto): omitir se N > 3 e forem os únicos do dia; manter se houver outros eventos no mesmo dia.
- Local: exibir só se presente e relevante (não genérico).
- Link de reunião: exibir domínio encurtado (meet.google.com/..., zoom.us/...).
- Dias sem eventos (além da rotina): exibir `*(agenda livre)*`.
- Ao final: total de eventos não-rotina encontrados.
