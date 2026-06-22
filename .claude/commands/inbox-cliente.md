---
description: Filtra Gmail por cliente específico — uso: /inbox-cliente <nome>
---

Você é a bibliotecária do vault. Filtre e-mails de um cliente específico.

O argumento passado pelo usuário é o nome do cliente: `$ARGUMENTS`

**PASSO 1 — Montar query**

Baseie a query no nome recebido:
- Se contiver "câmara" ou "camara" → query: `câmara OR vereador OR plenário is:inbox`
- Se contiver "sindss" ou "sindicato" → query: `sindss OR sindicato OR ceiça is:inbox`
- Se contiver "saúde" ou "sms" → query: `saúde OR secretaria OR sus is:inbox`
- Se contiver "logika" ou "lógika" → query: `logika OR lógika OR produção is:inbox`
- Outros → use o nome literal como query

**PASSO 2 — Buscar**

Use `mcp__claude_ai_Gmail__search_threads`:
- query: conforme acima
- maxResults: 20

**PASSO 3 — Listar threads**

Para cada thread relevante:
- Remetente
- Assunto
- Data/hora
- Resumo de 1 linha do conteúdo (se disponível via `get_thread`)
- Tag: `[RESPONDER]`, `[INFO]`, `[SPAM]` ou `[AGUARDANDO]`

**PASSO 4 — Saída**

```
## 📧 Threads — [Cliente] (últimas semanas)

- [Remetente] — "Assunto" (DD/MM) [TAG]
  > Resumo

---
X threads encontradas. Y requerem ação.
```

Não salva no vault automaticamente — apenas exibe. Jadielson decide o que fazer.
