
## 🗄️ Vault Central (Segundo Cérebro)

**Workspace (fonte de verdade):** `/data/.openclaw/workspace/`

**Regra:** Todo conhecimento, contexto, decisão, aprendizado ou anotação que eu ou qualquer sub-agente meu gerar DEVE ser salvo neste vault. Nada fica solto. Nada em repositórios separados. Isso evita esquecimentos e alucinações entre sessões e agentes.

**Orientações para sub-agentes:**
- Sempre clonar/usar este vault como destino de escrita
- Qualquer arquivo novo de conhecimento vai pra cá
- Qualquer atualização de contexto vai pra cá
- Se não souber onde salvar, salva aqui

**Data de registro:** 2026-06-18
**GitHub:** backup apenas (cron 03:00 BRT)
**Último clone:** 2026-06-18 (autenticado com GITHUB_TOKEN do .env)

---

## Destaque de Comunicação - Headline "Arraiá da Saúde"

*   **Headline:** "No clima dos festejos juninos, a Academia da Saúde Polo também virou espaço de alegria, convivência e cuidado."
*   **Contexto:** Refere-se à adaptação da Academia da Saúde Polo para eventos juninos, destacando a transformação em um local de alegria, convivência e cuidado, sob o guarda-chuva da Secretaria de Saúde.
*   **Data de Registro:** 2026-06-17

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

