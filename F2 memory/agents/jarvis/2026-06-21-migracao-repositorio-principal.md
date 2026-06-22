# Jarvis — migração para repositório principal consolidado

Data: 2026-06-21T20:30:52Z

Jadielson definiu que o repositório principal/consolidado dos agentes deve ser:

- [workspace] /data/.openclaw/workspace/ (GitHub segundo-cerebro é backup apenas)

Ação executada pelo Jarvis:

- Criado espelho seguro do workspace Jarvis em `agentes/jarvis-workspace/`.
- Origem `/data/.openclaw/workspace-jarvis` preservada sem deleção.
- Segredos e artefatos ruidosos excluídos: `.env*`, `.git/`, `node_modules/`, `media/`, `.audit/`, logs.
- Contexto consolidado inclui identidade, memória, mapa, skills, templates, exemplos e material do Starter Kit.

Aviso à Lôh:

- Tentativa de aviso via Telegram `@loh_aluno` e `@loh_analytics` falhou por chat não resolvido.
- Este registro serve como aviso persistente para governança da Lôh.
- Integrações/configurações sensíveis continuam sob governança da Lôh; valores de tokens não devem ser salvos em memória ou repositório.

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

