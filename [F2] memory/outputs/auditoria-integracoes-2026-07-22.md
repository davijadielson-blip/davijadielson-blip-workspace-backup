---
tema: auditoria integracoes 2026 07 22
atualizado_em: 2026-07-22
---

# Auditoria de Integrações — 2026-07-22 (Atualizado)

> Atualização pós-configuração do gog conta Lôh

## 🔵 INTEGRAÇÕES FUNCIONAIS

### 1. ✅ Telegram — OK
### 2. ✅ Miro — OK
### 3. ✅ Notion — OK
### 4. ✅ GitHub (workspace) — OK (backup 3h)
### 5. ✅ GitHub (segundo-cérebro) — OK
### 6. ✅ Mission Control — OK
### 7. ✅ Cron Jobs do Gateway — OK (39+ ativos)
### 8. ✅ Gog (Google) — 3 contas ativas ✅
- `davijadielson@gmail.com` — calendar, drive
- `logikacreative.mkt@gmail.com` — docs, drive, forms, sheets
- `loh.open.logika@gmail.com` — drive, calendar ✅ NOVA

### 9. ✅ memory_search (OpenAI Embeddings) — Restaurado
- Chave API validada (respondeu 200)
- Busca semântica operacional

## 🟡 INTEGRAÇÕES COM RESSALVAS

### 10. ⚠️ Segundo-cérebro desatualizado — Parcial
### 11. ⚠️ TOOLS.md — Vazio
### 12. ⚠️ Telegram state — Vazio

## 🔴 INTEGRAÇÕES QUEBRADAS / REMOVIDAS

### 13. ❌ Cron jobs isolados — Falha de autenticação
- Crons que usam `sessionTarget: "isolated"` falham porque:
  - Modelo principal (openai-codex/gpt-5.5) não tem chave API no perfil do agente isolado
  - Fallbacks OpenRouter (DeepSeek, Gemini) sem créditos (402)
- **Impacto:** Resumo diário (06h) e outros crons isolados não entregam
- **Necessário:** configurar chave API no auth-profiles.json ou mudar modelo dos crons

### 14. ❌ Zapier MCPs — Resíduo técnico
- 3 MCPs Zapier ainda disponíveis como ferramentas (zapier-1, zapier-3, zapier-youtube)
- Decisão de remoção registrada mas MCPs ainda ativos no gateway

## 📋 RESUMO

| Integração | Status |
|---|---|
| Telegram | ✅ |
| Miro | ✅ |
| Notion | ✅ |
| GitHub (workspace) | ✅ |
| GitHub (segundo-cérebro) | ✅ |
| Mission Control | ✅ |
| Cron jobs | 🟡 (isolados falham) |
| Gog (3 contas) | ✅ **CONCLUÍDO** |
| memory_search | ✅ restaurado |
| Zapier | 🟡 residual (decidido remover) |
| TOOLS.md | ⚠️ vazio |
| Telegram state | ⚠️ vazio |

Fonte: Cofre — MEMORY.md, decisões 2026-07-22, testes diretos