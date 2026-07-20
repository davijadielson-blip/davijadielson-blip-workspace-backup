# Diagnóstico Técnico — Falha de Subagentes CMO e CCO (Rate Limit)

**Data:** 2026-07-20
**Autor:** Lôh (Orquestradora Tier 0)
**Fonte:** Cofre — config do Gateway (`openclaw.json`), tentativas reais de sessions_spawn

---

## 1. Problema

Subagentes CMO (`agent:cmo:subagent:8963a439...`) e CCO (`agent:cco:subagent:3c77e739...`) falharam com erro:

```
⚠️ API rate limit reached. Please try again later.
```

### Histórico de tentativas

| Tentativa | Alvo | Modo | Resultado |
|---|---|---|---|
| 1 | CMO + CCO | Paralelo | Ambos falharam |
| 2 | CMO | Sequencial (isolado) | Falhou |
| 3 | CCO | Sequencial (isolado) | Falhou |

---

## 2. Evidência da Configuração

### Modelo dos agentes (Cofre: `openclaw.json`)

- **CMO:** `agents.list[].id=cmo` → model primary: `openai-codex/gpt-5.5`, fallbacks: `openrouter/deepseek/deepseek-v4-flash`, `openrouter/google/gemini-2.5-flash-lite`
- **CCO:** `agents.list[].id=cco` → model primary: `openai-codex/gpt-5.5`, fallbacks: `openrouter/deepseek/deepseek-v4-flash`, `openrouter/google/gemini-2.5-flash-lite`
- **Subagent defaults:** `agents.defaults.subagents.model` não está configurado explicitamente. Subagentes herdam de `agents.defaults.model`, que é `openai-codex/gpt-5.5`.

### Perfil de autenticação

- **`openai-codex:davijadielson@gmail.com`** — modo OAuth, único perfil OpenAI Codex
- **`openrouter:default`** — modo API key
- **`anthropic:default`** — modo API key

### Conclusão da configuração

**CMO e CCO compartilham o mesmo provider e API key/OAuth da sessão principal (Lôh).** Não há separação de chaves ou provedor distinto para subagentes.

---

## 3. Hipótese Confirmada

A falha **não é arquitetural**. O roteamento de subagentes funciona, a invocação chega ao Gateway, o modelo é atribuído. O gargalo é downstream:

1. **Uso intenso anterior:** horas de operação contínua na curadoria 360 (33 setores, scripts Python, leitura de centenas de arquivos, geração de 206+ arquivos .md) consumiu cota do mesmo provider (`openai-codex/gpt-5.5`).
2. **Mesma chave:** sessão principal (Lôh) e subagentes (CMO, CCO) usam o mesmo `openai-codex:davijadielson@gmail.com` OAuth. Não há chave separada.
3. **0 tokens nas tentativas:** o rate limit é pré-gravação — a API rejeita antes de qualquer consumo.
4. **Prova de concorrência descartada:** mesmo disparando um subagente de cada vez, com intervalo, ambos caíram. O rate limit é por provedor/API key, não por concorrência entre subagentes.

---

## 4. Caminhos de Resolução

### Imediato (curto prazo)

1. **Aguardar refrigeração:** ~15-30 minutos para reset do rate limit do OpenAI Codex, dependendo do tier de cota da conta.
2. **Testar com fallback:** ao disparar subagentes, forçar o uso do fallback `openrouter/deepseek/deepseek-v4-flash` que tem chave API separada.
3. **Reduzir carga:** espaçar spawns de subagentes com intervalos maiores.

### Estrutural (médio prazo)

1. **Separar chave/provedor para subagentes:**
   - Opção A: Configurar `agents.defaults.subagents.model` com primary diferente (ex: `openrouter/deepseek/deepseek-v4-flash`) e fallbacks, liberando o OpenAI Codex apenas para a sessão principal.
   - Opção B: Obter uma segunda chave OpenAI Codex/OAuth e configurar perfil de auth separado para subagentes.
2. **Avaliar tier do plano OpenAI:** verificar se o plano atual tem cota adequada para o volume de operações (sessão principal + subagentes C-Level).
3. **Configurar `agents.defaults.subagents.model`** no Gateway com fallback explícito para OpenRouter, garantindo que subagentes não dependam exclusivamente do OpenAI Codex.

### Operacional

- Registrar este diagnóstico no Cofre para referência futura.
- Se o problema persistir após refrigeração, acionar CAIO para avaliar arquitetura de rate limit e modelo de subagentes.

---

## 5. Próximos Passos

1. ✅ Diagnóstico registrado neste arquivo
2. ⏳ Aguardar refrigeração (~15-30 min a partir das 15:10 UTC)
3. 🔄 Testar spawn de CMO ou CCO isolado com fallback OpenRouter
4. 📝 Se resolver, avaliar configuração permanente de subagent model/provider separado
5. 🚨 Se não resolver, escalar para Jadielson com recomendação de upgrade de plano ou chave separada

---

*Fonte: Cofre — `openclaw.json` (config do Gateway), tentativas reais de sessions_spawn com CMO e CCO.*