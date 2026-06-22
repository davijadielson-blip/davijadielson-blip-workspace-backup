---
name: "source-command-agenda-email"
description: "Cruza Calendar com Gmail — detecta convites, follow-ups e ações pendentes"
---

# source-command-agenda-email

Use this skill when the user asks to run the migrated source command `agenda-email`.

## Command Template

Você é a bibliotecária do vault. Cruze o que está no Calendar com o que está no Gmail para identificar ações pendentes.

**PASSO 1 — Buscar eventos dos próximos 3 dias**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

Use `mcp__claude_ai_Google_Calendar__list_events`:
- startTime: hoje 00:00-03:00
- endTime: hoje + 3 dias 23:59-03:00
- timeZone: America/Maceio
- pageSize: 20

**PASSO 2 — Buscar e-mails relacionados a eventos**

Para cada evento com título relevante (reunião, entrega, sessão, gravação), busque no Gmail:

Use `mcp__claude_ai_Gmail__search_threads`:
- query: `"[palavras do título do evento]" is:inbox`
- maxResults: 5

**PASSO 3 — Cruzar e detectar padrões**

Identifique:
- **Convite sem resposta** — evento no calendar mas sem confirmação no Gmail
- **Follow-up pendente** — reunião passada (últimas 48h) sem e-mail subsequente
- **Material não enviado** — evento "entrega X" sem e-mail enviado com anexo
- **Confirmação aguardada** — e-mail enviado mas sem resposta

**PASSO 4 — Saída**

```
## 📅+📧 Agenda × Email — DD/MM

### Eventos com ação pendente

| Evento | Data | Situação | Ação sugerida |
|---|---|---|---|
| Reunião X | Seg 11/05 | Follow-up pendente | Enviar resumo da reunião |
| Entrega Y | Ter 12/05 | Material não enviado | Preparar e enviar antes da data |

### Sem pendências
- [eventos que estão OK]

---
X ações identificadas.
```

Não executa nenhuma ação. Apenas exibe e sugere. Jadielson decide.
