# Decisão — Revisão de Prompts C-Level + Fallbacks de Modelo

**Data:** 2026-07-20
**Autor:** Lôh (Orquestradora Tier 0)
**Autorizado por:** Jadielson Davi
**Fonte:** Cofre — testes reais de spawn, openclaw.json

---

## 1. Problema

Subagentes C-Level ignoravam comandos literais simples ("Responda APENAS em 1 linha") e entravam em modo operacional completo (leitura profunda do Cofre + diagnóstico), consumindo 2min+ e estourando timeout.

## 2. Diagnóstico

- **Causa raiz:** O Protocolo Global Obrigatório instrui todos os agentes a consultar o Cofre primeiro, sem exceção — mesmo para comandos de teste/ping simples.
- **Agravante:** OpenAI Codex (`gpt-5.5`) estava com rate limit após uso intenso no fim de semana (curadoria 360 de 33 setores), causando timeout nos spawns que caíam no Codex.
- **Padrão comprovado:** Agentes que caíram no OpenRouter/DeepSeek completaram em 24s–2m34s. Agentes no Codex timeout em 100% dos casos.

## 3. Ações Tomadas

### A) Regra de Obediência — 8 C-Levels

Adicionada instrução de obediência a comandos diretos ANTES do Protocolo Global em todos os 8 C-Levels:

```
## ⚡ REGRA DE OBEDIÊNCIA A COMANDOS DIRETOS

Quando receber um comando no formato "Responda APENAS em N linha(s): [formato]"
ou qualquer variação com "APENAS", "SOMENTE" ou "ESTRITAMENTE":
1. NÃO inicie leitura do Cofre
2. NÃO produza diagnóstico, análise ou contexto adicional
3. NÃO adicione formatação extra, rodapé ou fontes
4. Execute o formato solicitado LITERALMENTE
5. Responda com no máximo o número de linhas especificado
```

### B) Fallback de Modelo — Subagentes

`agents.defaults.subagents.model` configurado com fallback em cadeia:

| Ordem | Provider | Finalidade |
|---|---|---|
| 🥇 **Primário** | `openai-codex/gpt-5.5` | Plano A (mais barato 💰) |
| 🥈 **Fallback 1** | `openrouter/deepseek/deepseek-v4-flash` | Plano B (quando Codex cair) |
| 🥉 **Fallback 2** | `openrouter/google/gemini-2.5-flash-lite` | Plano C (último recurso) |

**Timeout aumentado para 300s** para garantir que o Codex tenha tempo de tentar e, se falhar, o fallback rode sem pressa.

### C) Regra de prioridade

O Codex é o plano A porque é **mais barato**. Os fallbacks (B e C) entram **apenas quando o Codex estiver indisponível** (rate limit, timeout, erro). O importante é que **nunca deixe de executar** — mesmo que demore mais.

## 4. Resultado dos Testes (8 C-Levels)

| Agente | Modelo | Status | Tempo | Lição |
|---|---|---|---|---|
| **CAIO** | `deepseek-v4-flash` | ✅ done | 24s | Obediência funcionou |
| **CIO** | `deepseek-v4-flash` | ✅ done | 58s | Obediência funcionou |
| **CFO** | `deepseek-v4-flash` | ✅ done | 1m10s | Obediência funcionou |
| **CTO** | `deepseek-v4-flash` | ✅ done | 1m45s | Obediência funcionou |
| **COO** | `deepseek-v4-flash` | ✅ done | 2m34s | Obediência funcionou |
| CCO | `gpt-5.5` | ⏱️ timeout | 2m11s | Codex ainda limitado |
| CRO | `gpt-5.5` | ⏱️ timeout | 2m12s | Codex ainda limitado |
| CMO | `gpt-5.5` | ⏱️ timeout | 2m12s | Codex ainda limitado |

## 5. Próximos Passos

- Quando o Codex恢复正常 (rate limit reset), reavaliar se volta como primário dos subagentes ou mantém OpenRouter
- Monitorar se algum C-Level ignora a regra de obediência em comandos diretos futuros
- Se o padrão persistir, considerar aumentar timeout padrão de subagentes de 180s para 300s

---

*Fonte: Cofre — openclaw.json, testes de spawn com 8 C-Levels em 20/07/2026.*