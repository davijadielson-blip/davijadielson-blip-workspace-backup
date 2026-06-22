---
description: Hub de cruzamento — Gmail + Drive + Calendar + pendencias → Top 3 enriquecido do dia
---

Você é a bibliotecária do vault. Cruze todas as fontes disponíveis e entregue o Top 3 real do dia.

**PASSO 1 — Carregar contexto base**

Leia em paralelo:
- `[F2] memory/context/pendencias.md` — pendências críticas e importantes
- `[F2] memory/context/deadlines.md` — prazos próximos

**PASSO 2 — Puxar fontes externas**

Execute sequencialmente:

**2a. Gmail (últimas 24h):**
Use `mcp__claude_ai_Gmail__search_threads`:
- query: `after:YYYY/MM/DD is:inbox`
- maxResults: 20

Extraia apenas itens que requerem ação (ignore spam, promoções).

**2b. Google Calendar (próximas 48h):**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

Use `mcp__claude_ai_Google_Calendar__list_events`:
- startTime: hoje 00:00-03:00
- endTime: hoje + 2 dias 23:59-03:00
- timeZone: America/Maceio
- pageSize: 20

Filtre eventos não-rotina.

**2c. Drive (recente):**
Use `mcp__claude_ai_Google_Drive__list_recent_files`:
- pageSize: 10

Identifique arquivos que requerem ação (ex: novos materiais de clientes).

**2d. Inbox processada:**
Liste arquivos em `[F2] memory/inbox-externa/` com `revisado: false` e data recente (≤3 dias).

**PASSO 3 — Montar matriz de prioridade**

Para cada item das fontes, atribua pontuação:

| Critério | Pontos |
|---|---|
| Prazo ≤ 1 dia | +10 |
| Prazo ≤ 3 dias | +7 |
| Prazo ≤ 7 dias | +4 |
| Requer resposta de cliente | +5 |
| Bloqueando outra entrega | +5 |
| E-mail não respondido há >24h | +3 |
| Arquivo novo de cliente | +2 |

**PASSO 4 — Entregar Top 3 + contexto**

```
## 🎯 Prioridades do Dia — DD/MM/YYYY

### #1 — [Item mais urgente]
**Fonte:** [pendencias / gmail / calendar / drive]
**Prazo:** DD/MM ou "hoje" ou "sem prazo fixo"
**Frente:** [frente]
**Ação:** [o que fazer em 1 linha]

### #2 — [Segundo item]
...

### #3 — [Terceiro item]
...

---

### 📧 E-mails que aguardam resposta
- [remetente] — "[assunto]" (há Xh)

### 📅 Compromissos hoje
- HH:MM — [evento] (frente: X)

### 📁 Materiais novos no Drive
- [arquivo] — [frente] (modificado: DD/MM)

### 📥 Inbox pendente de revisão
- [arquivo] — [tipo] (há X dias)

---
Fontes consultadas: Gmail ✅ | Calendar ✅ | Drive ✅ | Pendências ✅
```

**PASSO 5 — Alerta opcional**

Se houver e-mail de cliente sem resposta há >48h:
```
⚠️ ATENÇÃO: [cliente] aguarda resposta há X horas.
```

Se houver prazo crítico não listado nas pendências:
```
⚠️ NOVO PRAZO: [item] detectado no Gmail/Calendar — não está em pendencias.md.
Quer adicionar?
```
