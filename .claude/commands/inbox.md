---
description: Lê Gmail das últimas 24h e resume por frente
---

Você é a bibliotecária do vault. Leia os e-mails das últimas 24h e organize por frente.

**PASSO 1 — Definir intervalo**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

- `after`: hoje menos 1 dia (formato Gmail: `after:YYYY/MM/DD`)
- `before`: hoje (formato Gmail: `before:YYYY/MM/DD`)

**PASSO 2 — Buscar threads**

Use `mcp__claude_ai_Gmail__search_threads`:
- query: `after:YYYY/MM/DD is:inbox`
- maxResults: 30

**PASSO 3 — Classificar por frente**

Para cada thread, identifique a frente pelo remetente ou assunto:

| Palavra-chave | Frente |
|---|---|
| câmara, vereador, sessão, plenário | Câmara Municipal |
| sindss, sindicato, servidor, ceiça | SINDSS |
| saúde, sms, secretaria, sus | SMS / Saúde |
| logika, lógika, produção, audiovisual | Lógika Creative |
| além da foto, fio da memória | Projetos Pessoais |
| rogério, rogerio | Rogério Rocha (inativo) |
| (outros) | Pessoal / Sem frente |

**PASSO 4 — Gerar resumo**

Saída agrupada por frente:

```
## 📧 Inbox — DD/MM (últimas 24h)

### 🎥 Lógika Creative
- [Nome do remetente] — "Assunto" (HH:MM)
  > Uma linha de contexto se relevante

### 🏛️ Câmara Municipal
*(sem e-mails)*

### ⚠️ Ação necessária
- [thread que requer resposta ou follow-up — resumo de 1 linha]

---
Total: X e-mails | Y frentes | Z ações necessárias
```

**PASSO 5 — Salvar em inbox-externa**

Se houver e-mail relevante (não spam), salve resumo em:
`[F2] memory/inbox-externa/email/YYYY-MM-DD.md`

Frontmatter:
```yaml
---
tipo: inbox-externa
fonte: gmail
data: YYYY-MM-DD
frentes: [lista]
revisado: false
---
```

Regra: spam e promoções não entram no vault. Dúvida → não salva.
