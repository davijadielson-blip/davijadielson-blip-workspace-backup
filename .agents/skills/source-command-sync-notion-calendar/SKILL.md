---
name: "source-command-sync-notion-calendar"
description: "Sincroniza Notion (Calendário Editorial Saúde) → Google Calendar manualmente"
---

# source-command-sync-notion-calendar

Use this skill when the user asks to run the migrated source command `sync-notion-calendar`.

## Command Template

Rode o script de sync e mostre o relatório.

```bash
python3 scripts/sync/notion-to-calendar.py
```

Depois leia o log gerado em `[F2] memory/sessions/sync/YYYY-MM-DD.md` e mostre:
- Quantos eventos criados
- Quantos atualizados
- Erros (se houver)
- Lista dos itens sincronizados

O sync é **unidirecional**: Notion → Calendar. Mudanças feitas diretamente no Google Calendar não voltam para o Notion.
