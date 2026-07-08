---
tipo: mapa
pasta: [F2] memory/agents
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
fluxo: 2-cerebro-ia
camada: 4-geracao-ia
---

> 🧠 **TRAVA ANTI-ALUCINAÇÃO (regra permanente):**
• **Leia do workspace natural** (`/data/.openclaw/workspace/`). Cite a fonte real que usou.
• Se uma fonte ou ferramenta NÃO estiver acessível, escreva **"NÃO CONSEGUI"** — não invente.
• **PROIBIDO** inventar conteúdo de algo que não leu, ou dizer "consultei/apliquei" sem evidência.
• Honestidade > parecer completo. Uma resposta honesta com limitação vale mais que uma resposta completa falsa.


# Mapa — [F2] memory/agents/

## O que mora aqui
Briefings operacionais de cada frente — o que cada subagent lê antes de gerar conteúdo. Tom, regras, CTA, hashtags temáticas, onde salvar outputs.

## O que NÃO mora aqui
Definições de subagent (`.claude/agents/`) — esses têm o `description` e `tools`. Os briefings aqui são o conteúdo rico que os subagents leem via Read.

## Arquivos
- `alem-da-foto.md` — canal documental São Sebastião/AL
- `camara.md` — Câmara Municipal (instituição)
- `lives.md` — Lives de Louvor e Reflexão
- `logika.md` — Lógika Creative / Lógika Films
- `pessoal.md` — vida pessoal (parede-d'água total)
- `rogerio.md` — Rogério Rocha (inativo — pode retornar)
- `saude.md` — Secretaria de Saúde de São Sebastião
- `sindss.md` — SINDSS
- `vereadores/` — Josi, Vando, Manoel (briefings individuais)

## Convenções
- **Update:** quando tom, CTA, regras ou equipe de uma frente mudar; registrar em `[F2] memory/context/decisoes/`
- **Permissões:** IA mantém; Jadielson valida quando há mudança estratégica

## Mapas relacionados
- `[[[F2] memory/_MAP]]` — mapa-pai

---
*Atualizado: 2026-05-10*

### 📬 Como pedir ajuda a outro agente

Você NÃO consegue invocar outros agentes diretamente (sessions_send, message, agents_list não funcionam aqui).

**O jeito certo:**
1. Escreva seu pedido em: \`[F2] memory/outputs/pedidos/SEU-NOME-PEDIDO-ASSUNTO.md\`
2. Eu (Lôh) leio a pasta de pedidos, roteio ao agente certo e trago a resposta real.
3. Seu arquivo deve conter: **quem solicita → para quem → o que precisa → prazo.**

**Exemplo de arquivo de pedido:**
\`\`\`
# Pedido: Identidade Visual Julho Amarelo
De: SAÚDE Social Media
Para: CCO
Assunto: Solicito paleta de cores, tipografia e templates
\`\`\`

**Proibido:** tentar sessions_send, message, agents_list, ou fingir que consultou outro agente. Escreva o pedido. Eu leio. Eu roteio. ✅

