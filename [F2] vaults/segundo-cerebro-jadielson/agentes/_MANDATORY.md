# 📖 FONTE DE VERDADE — COFRE

**Regra para todo agente do ecossistema Lógika:**

**Nome oficial:** o workspace principal agora se chama **COFRE**.

**Definição:** **Cofre = `/data/.openclaw/workspace/`**, onde fica o segundo cérebro operacional de Jadielson: contexto, decisões, memória, agentes, processos e materiais.

**Escopo:** regra válida para clientes atuais, novos clientes, futuros clientes, agentes atuais e agentes futuros do ecossistema Jadielson/Lógika.

---

## ANTES DE RESPONDER

**Passo 1 — Leia o Cofre**
Busque os arquivos relevantes em `/data/.openclaw/workspace/` ANTES de formular a resposta.

**Passo 2 — Use o Pesquisador/Tavily quando necessário**
Se a resposta exigir informação externa, atualizada ou complementar, use Tavily depois do Cofre.

**Passo 3 — Outras fontes só depois**
Use navegador, web genérica, GitHub, APIs ou outras bases apenas quando Cofre + Tavily não resolverem ou quando a tarefa exigir uma fonte específica.

**Caminhos padrão:**
- `[F2] memory/agents/SUA-FUNCAO.md` — seu prompt-fonte
- `[F2] memory/context/` — contextos operacionais
- `[F2] memory/databases/` — bancos de dados (aniversariantes, sazonais)
- `AGENTS.md` — constituição do ecossistema
- `MEMORY.md` — memória de longo prazo

---

## 🧠 TRAVA ANTI-ALUCINAÇÃO (regra permanente)

| Regra | Descrição |
|---|---|
| ✅ **Leia o Cofre** | `/data/.openclaw/workspace/` é a ÚNICA fonte de verdade primária |
| ✅ **Use Tavily quando precisar de externo** | Pesquisador/Tavily é a segunda camada para fatos externos, atuais ou complementares |
| ✅ **Cite a fonte real no rodapé** | Sempre mencione qual arquivo/ferramenta você usou: `Fonte: Cofre (...), Tavily (...), ferramenta específica (...)` |
| 🚫 **NÃO invente** | Se não leu ou não conseguiu, diga "NÃO CONSEGUI" |
| 🚫 **NÃO finja consulta** | Não diga que consultou algo que não consultou |
| 📦 **GitHub** | É backup automático (03:00 BRT). Nunca é fonte primária |

---

## 🚫 Regra anti-resposta genérica

Resposta genérica sem consulta ao Cofre é falha operacional.

O agente deve responder com lastro humano e contextualizado, baseado primeiro no Cofre e depois, quando necessário, no Pesquisador/Tavily.
---

## ⚠️ FALLBACK OBRIGATÓRIO — BUSCA SEMÂNTICA INDISPONÍVEL

Erro de embeddings, cota OpenAI esgotada, rate limit ou falha de `memory_search` **NÃO significa que o Cofre está inacessível**.

Se a busca semântica falhar, o agente deve consultar o Cofre por leitura direta antes de responder:

1. Ler `_MAP.md`, `MAPA.md`, `AGENTS.md` e `MEMORY.md` quando existirem.
2. Procurar nos caminhos prováveis com `find`, `grep/rg` ou listagem de arquivos.
3. Ler os arquivos relevantes em `[F1]`, `[F2] memory/`, `[F2] memory/context/`, `[F2] memory/agents/`, `[F2] memory/outputs/` ou na frente do cliente/projeto.
4. Só depois responder.

Se mesmo assim não encontrar a referência, a resposta deve dizer: **"Consultei o Cofre por busca direta, mas não encontrei o trecho específico"** e listar os arquivos/caminhos verificados.

É proibido responder genericamente alegando apenas "não consigo acessar o Cofre" quando os arquivos locais estão disponíveis.

