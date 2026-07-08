---
summary: "Workspace template for HEARTBEAT.md"
read_when:
  - Bootstrapping a workspace manually
---

# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.
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

