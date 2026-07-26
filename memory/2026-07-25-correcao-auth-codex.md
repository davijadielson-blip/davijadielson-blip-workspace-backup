---
tema: correcao autenticacao codex
atualizado_em: 2026-07-25
---

# ✅ Correção Aplicada — Auth Codex em 21 Agentes + Gateway Restart

**Data:** 2026-07-25
**Solicitante:** Jadielson Davi
**Executor:** Lôh

## O que foi feito

### 1. Diagnóstico completo (já salvo)
- `memory/2026-07-25-diagnostico-creditos-openrouter.md`

### 2. Correção do auth Codex no agente `main`
- **Antes:** só `openrouter:default` no auth-profiles.json
- **Depois:** adicionado `openai-codex:davijadielson@gmail.com` em modo OAuth

### 3. Propagação para TODOS os 20 agentes restantes
- Alfred, Arca, Autoconhecimento, CAIO, CCO, Central-Topic-Agent, CFO, CIO, CMO, COO, CRO, CTO, Espiritualidade, Família, Fio-da-Memória, Identidade, Jarvis, Liberdade, Saúde, Warren
- Todos agora têm `openai-codex:davijadielson@gmail.com` (oauth) no auth local

### 4. Gateway restart (SIGUSR1)
- Config recarregada
- Agentes listados com primário `openai-codex/gpt-5.5` e auth Codex disponível

## Pendências

### 🟡 OAuth precisa de autorização humana
O Codex usa OAuth com a conta Google (davijadielson@gmail.com). Na primeira tentativa de uso, o gateway vai gerar um link de autenticação. Jadielson precisa abrir esse link no navegador e autorizar.

### 🔴 OpenRouter com saldo residual
Ainda há saldo baixo no OpenRouter (~16K tokens). Enquanto o Codex não estiver autenticado, os crons vão continuar falhando para fallback.

### 🟢 Política de agentes dormentes
Já está vigente desde 24/07. Agentes só acordam quando Jadielson, Lôh ou cron explícito requisitar. Proibição de despertar em cadeia mantida.

## Próximo passo
Quando um cron (ex: LÔH resumo, CFO, Warren) tentar rodar com Codex e o OAuth não estiver autenticado, o gateway deve gerar um link. Jadielson precisa acessar esse link para completar a autenticação.

---

**Fonte:** Cofre — `agents_list`, `auth-profiles.json` (todos os 21 agentes)