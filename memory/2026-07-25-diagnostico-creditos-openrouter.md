---
tema: diagnostico creditos openrouter
atualizado_em: 2026-07-25
---

# 🔴 Diagnóstico Emergencial — Créditos OpenRouter Esgotados e Agentes sem Codex

**Data:** 2026-07-25
**Solicitante:** Jadielson Davi
**Responsável:** Lôh

## 🔍 Constatações Técnicas (evidências do Cofre)

### 1. Agente `main` não tem autenticação Codex

Arquivo: `/data/.openclaw/agents/main/agent/auth-profiles.json`
```json
{
  "profiles": {
    "openrouter:default": {
      "key": "sk-or-v1-...",
      "provider": "openrouter",
      "type": "api_key"
    }
  }
}
```

⚠️ **Só tem OpenRouter — nenhum perfil `openai-codex`.**

Enquanto isso, o `auth-state.json` do mesmo agente registra:
```json
{
  "lastGood": {
    "openrouter": "openrouter:default"
  }
}
```

Ou seja, **nunca houve uma conexão bem-sucedida com o Codex neste agente.**

### 2. O perfil Codex existe APENAS no config global

Em `openclaw.json` existe:
```json
"openai-codex:davijadielson@gmail.com": {
  "mode": "oauth",
  "provider": "openai-codex"
}
```

Mas isso é só a **declaração** do perfil. O agente `main` NÃO o tem no seu auth local, e o runtime busca APENAS no `auth-profiles.json` do agente, **não no global**. Logo: **Codex sempre falha**.

### 3. Cadeia de falha comprovada (Briefing Sábado 25/07)

```
openai-codex/gpt-5.5 → No API key found (auth)
openrouter/deepseek/deepseek-v4-flash → 402 credits: só 16070 tokens sobrando
openrouter/google/gemini-2.5-flash-lite → 402 credits: só 11249 tokens
```

**Tudo falhou. Sistema ficou mudo.**

### 4. O que consumiu os créditos OpenRouter

- 🟢 **LÔH Resumos (06h e 21h):** funcionam com `lightContext: true`, consomem pouco
- 🟡 **CFO, Warren, IA RADAR:** tentam Codex → falham → consomem OpenRouter (mais caro)
- 🔴 **Esta sessão atual (chat comigo):** usa `OPENAI_API_KEY` via env var apontando para OpenRouter
- 🔴 **Briefing Estratégico Semanal:** falhou 3 vezes consecutivas (Codex + 2 fallbacks)
- 🔴 **Limpeza de cache diária:** também falhou por timeout, mas não consome API

### 5. Causa raiz definitiva

> **A correção de 24/07/2026 foi PARCIAL.** O modelo primário foi corrigido para `openai-codex/gpt-5.5` na config, mas a **autenticação** para `openai-codex` nunca foi propagada para o auth local do agente `main`. E todos os outros agentes (21 agentes) herdaram a mesma config de modelo sem auth.

**Todo o ecossistema está rodando em fallback OpenRouter há semanas.**

---

## 🛠 Ações Necessárias

### Imediatas

1. [ ] **Recarregar créditos OpenRouter** — saldo residual insuficiente (≈16K tokens)
2. [ ] **Corrigir auth do Codex no agente `main`** — propagar a chave OAuth ou adicionar API key
3. [ ] **Corrigir auth do Codex para TODOS os outros agentes** — 21 agentes afetados

### Preventivas

4. [ ] Reduzir `max_tokens` dos fallbacks OpenRouter para funcionar com saldo baixo
5. [ ] Criar alerta de créditos OpenRouter baixos (<$1)
6. [ ] Auditoria de fallbacks: evitar chamadas desnecessárias quando primário falha

---

**Fonte:** Cofre — `agents_list`, `auth-profiles.json`, `auth-state.json`, `openclaw.json`, log de erros do cron `briefing-estrategico-semanal`