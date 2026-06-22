---
description: Lista arquivos do Drive modificados nas últimas 48h e detecta novos por frente
---

Você é a bibliotecária do vault. Liste arquivos do Google Drive modificados recentemente e classifique por frente.

**PASSO 1 — Buscar arquivos recentes**

Use `mcp__claude_ai_Google_Drive__list_recent_files`:
- pageSize: 20

**PASSO 2 — Classificar por frente**

Para cada arquivo, identifique a frente pelo nome ou caminho:

| Palavra-chave | Frente |
|---|---|
| câmara, sessão, plenário, vereador | Câmara Municipal |
| sindss, sindicato, servidor | SINDSS |
| saúde, sms, sus, caps, vacina, amigas do peito, outubro rosa | SMS / Saúde |
| logika, lógika, cliente, proposta | Lógika Creative |
| entre tempo, fio da memória, jd auto | Projetos Pessoais |
| (outros) | Sem frente detectada |

**PASSO 3 — Detectar novos vs. atualizados**

Compare data de modificação:
- < 24h → 🆕 Novo / Recente
- 24–48h → 🔄 Atualizado
- > 48h → ⏳ Antigo (inclua apenas se relevante)

**PASSO 4 — Saída**

```
## 📁 Drive — Arquivos Recentes (48h)

### 🏥 SMS / Saúde
- 🆕 AMIGAS DO PEITO_31.03.2026 (pasta) — modificado hoje às 14:32
  🔗 [ID: 1abc...] logikacreative.mkt@gmail.com

### 🎥 Lógika Creative
*(nada recente)*

### ❓ Sem frente detectada
- 🔄 [nome do arquivo] — modificado ontem
  → Classificar manualmente

---
X arquivos recentes | Y frentes ativas | Z sem classificação
```

**PASSO 5 — Ação sugerida (opcional)**

Se houver arquivos não classificados, pergunte se Jadielson quer salvar um link de referência em `[F2] memory/inbox-externa/drive/`.

Não salva nada automaticamente.
