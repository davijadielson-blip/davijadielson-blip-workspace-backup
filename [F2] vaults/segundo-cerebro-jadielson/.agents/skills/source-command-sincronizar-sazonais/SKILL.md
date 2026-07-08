---
name: "source-command-sincronizar-sazonais"
description: "Sincroniza datas sazonais do vault com o Google Calendar — 3 lembretes por data"
---

# source-command-sincronizar-sazonais

Use this skill when the user asks to run the migrated source command `sincronizar-sazonais`.

## Command Template

Sincronize as datas sazonais do vault com o Google Calendar. Nada é criado sem confirmação.

**PASSO 1 — Leia todas as datas sazonais futuras**

```bash
TODAY=$(date +"%Y-%m-%d")
grep -rh "^data: " "[F2] memory/databases/datas-sazonais/" | sort | uniq
```

Para cada data encontrada que seja >= hoje, leia o arquivo correspondente e extraia:
- `data` (YYYY-MM-DD)
- `descricao`
- `frente`

**PASSO 2 — Monte o plano de eventos**

Para cada data sazonal futura, calcule até 3 eventos (omita os que já passaram):

| Tipo | Quando | Título gerado |
|------|--------|--------------|
| Planejamento | 7 dias antes | `📌 [descricao] — planejar conteúdo` |
| Produção | 3 dias antes | `🎬 [descricao] — produzir agora` |
| Publicação | No dia | `📤 [descricao] — publicar hoje` |

Todos como eventos **all-day** (sem horário específico, sem notificação invasiva).

**PASSO 3 — Confirme antes de criar**

Exiba o plano completo e aguarde aprovação:

```
📅 **Plano de sincronização — N datas sazonais → M eventos**

| Criar em | Evento | Frente |
|----------|--------|--------|
| 03/05 | 📌 Dia das Mães — planejar conteúdo | comerciais |
| 07/05 | 🎬 Dia das Mães — produzir agora | comerciais |
| 10/05 | 📤 Dia das Mães — publicar hoje | comerciais |
...

Posso criar todos os M eventos no Google Calendar?
```

Se já existirem eventos com o mesmo título no Calendar (verifique com list_events antes de criar), sinalize e pergunte se quer substituir ou ignorar.

**PASSO 4 — Crie após confirmação**

Para cada evento, use `mcp__claude_ai_Google_Calendar__create_event`:
- `summary`: título conforme tabela
- `allDay`: true
- `startTime`: YYYY-MM-DDT00:00:00Z (meia-noite UTC)
- `endTime`: YYYY-MM-DDT00:00:00Z (mesmo dia — all-day)
- `colorId`: conforme frente (tabela no `/agendar`)
- `description`: "Data sazonal: [descricao] | Frente: [frente] | Criado via /sincronizar-sazonais"
- `overrideReminders`: [] (sem popup — evento visual apenas)
- `timeZone`: "America/Maceio"

**PASSO 5 — Log**

Crie `[F2] memory/logs/comandos/YYYY-MM-DD-sincronizar-sazonais.md`:
```
---
comando: /sincronizar-sazonais
data: YYYY-MM-DD
datas-processadas: N
eventos-criados: M
---
M eventos criados para N datas sazonais.
```

Confirme: "✅ Sincronização concluída — [M] eventos criados para [N] datas sazonais."
