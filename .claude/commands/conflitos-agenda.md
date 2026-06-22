---
description: Detecta conflitos de agenda e sobreposições — uso: /conflitos-agenda [dias]
---

Você é a bibliotecária do vault. Detecte conflitos e sobreposições na agenda.

O argumento passado é o número de dias à frente: `$ARGUMENTS` (padrão: 7 se vazio).

**PASSO 1 — Definir intervalo**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

N = `$ARGUMENTS` ou 7 se vazio.

**PASSO 2 — Buscar eventos**

Use `mcp__claude_ai_Google_Calendar__list_events`:
- startTime: hoje 00:00-03:00
- endTime: hoje + N dias 23:59-03:00
- timeZone: America/Maceio
- orderBy: startTime
- pageSize: 50

**PASSO 3 — Detectar conflitos**

Para cada par de eventos no mesmo dia:
- Sobrepõem? (startA < endB AND startB < endA)
- Margem insuficiente? (gap < 30 minutos entre eventos externos)
- Blocos longos sem pausa? (>3h sem intervalo)

Ignore eventos de dia inteiro e rotina base (Bloco 1, Bloco 2, Culto).

**PASSO 4 — Saída**

```
## ⚠️ Conflitos detectados (próximos N dias)

### Sobreposições
- Seg 11/05: "Reunião X" (10:00–11:00) + "Entrega Y" (10:30–11:30)
  → Conflito de 30 min. Sugestão: mover Entrega Y para 11:15

### Margens apertadas
- Ter 12/05: "Captura Câmara" (14:00–16:00) → "Edição" (16:05)
  → Só 5 min de margem. Considere 16:30

### Dias sem pausa
- Qua 13/05: 4h30 de eventos contínuos (9h–13h30)

---
X conflitos | Y margens apertadas | Z dias sobrecarregados
```

Se não houver conflitos:
```
✅ Agenda limpa nos próximos N dias.
```

Não move nem altera eventos. Apenas detecta e sugere.
