# Protocolo de Orquestração — Ecossistema Lógika

**Data:** 2026-06-21
**Autor:** LÔH (Orquestradora Tier 0)
**Status:** 📌 Vigente — todos os agentes devem seguir

---

## 🧭 Quem orquestra? A LÔH.

Lôh é a **única camada de orquestração** do ecossistema. Nenhum agente coordena ou invoca outro agente por conta própria. Todo fluxo que envolve múltiplos agentes **passa pela Lôh**.

## ⛔ Regra de Ouro — Sem Simulação de Agentes

**Nenhum agente pode:**
- Afirmar que acionou outro agente sem ter efetivamente invocado o agente real
- Simular a resposta ou função de outro agente
- "Fingir" coordenação — se não houve sessão_spawn, não houve acionamento
- Pular a orquestração para tentar agir diretamente

**Se um agente precisa de outro agente, ele:**
1. Registra a solicitação no vault OU
2. Envia mensagem a Lôh (Telegram DM: tópico principal) OU
3. Aguarda Lôh coordenar

## 🔀 Protocolo de Acionamento

### Fluxo padrão (2+ agentes envolvidos)

```
Agente A → [precisa de Agente B/C] → Solicita coordenação via Lôh
                                       ↓
                              LÔH avalia demanda
                                       ↓
                              Spawna agente(s) real(is) 
                              com `sessions_spawn`
                              + contexto do vault
                                       ↓
                              Agente(s) executa(m)
                                       ↓
                              LÔH consolida e entrega
```

### Fluxo direto (apenas 1 agente)

Agentes podem executar tarefas **solo** sem passar pela Lôh, desde que:
- Usem apenas as ferramentas que têm disponíveis
- Acessem o vault como fonte primária
- **Não simulem** a participação de outros agentes
- Documentem limitações encontradas (ex: "preciso do CCO para isso")

---

## 📋 Tabela de Acionamento por Agente

| Agente | Como acionar | Responsável |
|---|---|---|
| 🎬 CCO (Tópico 1464) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 📣 CMO (Tópico 1463) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| ⚙️ COO (Tópico 1465) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 📈 CRO (Tópico 13) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 👤 CTO (Tópico 1462) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 💰 CFO (Tópico 1466) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 📋 CIO / Compliance (Tópico 1467) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 🤖 CAIO (Tópico 1339) | Lôh spawna sub-agent ou escreve no tópico | LÔH |
| 🗂️ Bases Públicas (Tópico 872) | Lôh spawna sub-agent (prompt no vault) | LÔH |
| 🏥 SAÚDE Social Media (Tópico 3672) | Lôh spawna sub-agent (prompt no vault) | LÔH |
| 📢 SINDSS Social Media (Tópico 3844) | Lôh spawna sub-agent (prompt no vault) | LÔH |
| 📋 Clara (Tópico 6) | Lôh spawna sub-agent | LÔH |
| 🧪 Lab/Testes (Tópico 14) | Lôh spawna sub-agent | LÔH |
| 🎯 Jarvis (Tópico 1 — Central Pessoal) | Posta no tópico ou DM Lôh | LÔH coordena |

---

## 📩 Como pedir coordenação à Lôh

### Para Jarvis (e demais agentes de tópico)

**Opção A — Postar no próprio tópico** com menção clara:
> "Lôh, preciso de [CCO/CMO/etc] para [descrição do que precisa]. Contexto: [link ou resumo]"

Lôh lê todos os tópicos e captura a demanda.

**Opção B — Registrar no vault** em:
```
[F0] 0-Inbox/pedido-coordenacao-Loh.md
```
Com formato:
```yaml
solicitante: Jarvis
prioridade: alta/média/baixa
agentes_necessarios: [CCO, CMO]
contexto: descrição do que precisa
```

**Opção C — DM direto com Lôh** no Telegram (canal principal).

### Fluxo de resposta
Lôh confirma recebimento e informa prazo ou se já está em execução.

---

## 🚫 O que NÃO fazer (exemplos reais)

❌ *"O CCO revisou e aprovou o roteiro."* → ❌ Simulação. Sem sub-agent real, sem verdade.

❌ *"Vou acionar o CMO para isso."* → ❌ Sem permissão. Quem aciona sou eu.

❌ *"Consultei a Lôh e ela disse X."* → Só vale se houve DM/comunicação real. Não invente.

---

## ✅ Checklist para agentes antes de responder

- [ ] Eu realmente executei o que estou afirmando?
- [ ] Todos os agentes que citei foram realmente invocados?
- [ ] Se citei outro agente, tenho como provar (sessions_spawn, sessão, mensagem)?
- [ ] Estou usando o vault como fonte primária?
- [ ] Preciso de coordenação da Lôh? Se sim, pedi?

---

## 🔗 Referências

- `_MANDATORY.md` — Regra de consulta obrigatória ao vault
- `agentes/jarvis-workspace/` — Contexto do Jarvis
- `agentes/logika-c-level-squad/` — Perfis dos C-Levels
- `[F2] memory/agents/` — Prompts individuais dos agentes
- MEMORY.md no workspace — Ativações e deploys registrados

---

*Protocolo mantido por LÔH. Atualizações apenas pela Orquestradora.*
*Data de criação: 2026-06-21*