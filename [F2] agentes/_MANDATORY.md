# 📖 FONTE DE VERDADE — WORKSPACE NATURAL

**Regra para todo agente do ecossistema Lógika:**

---

## ANTES DE RESPONDER

**Passo único — Leia do workspace natural**
Busque os arquivos relevantes em `/data/.openclaw/workspace/`

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
| ✅ **Leia do workspace** | `/data/.openclaw/workspace/` é a ÚNICA fonte de verdade |
| ✅ **Cite a fonte real** | Sempre mencione qual arquivo/ferramenta você usou |
| 🚫 **NÃO invente** | Se não leu ou não conseguiu, diga "NÃO CONSEGUI" |
| 🚫 **NÃO finja consulta** | Não diga que consultou algo que não consultou |
| 📦 **GitHub** | É backup automático (03:00 BRT). Nunca é fonte primária |
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

