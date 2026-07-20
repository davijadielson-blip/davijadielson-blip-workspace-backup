# Relatório simples do sistema — 2026-07-20

## Pedido
Jadielson pediu um relatório simples e detalhado sobre o sistema: o que faz e do que é capaz.

## Síntese
O sistema é um ecossistema de IA orquestrado pela Lôh, com Cofre como fonte de verdade, agentes/subagentes para execução paralela, integrações com canais e apps, automações agendadas, pesquisa externa via Tavily, geração/análise de mídia e capacidade de registrar continuidade em Markdown.

## Pontos principais
- Lôh é a orquestradora Tier 0: filtra, roteia, comanda, coordena, sintetiza e antecipa demandas.
- Cofre oficial: `/data/.openclaw/workspace/`.
- Estrutura por fluxos: F0 captura, F1 criativo/humano, F2 sistema/memória, F3 projetos/integração.
- Pode consultar, organizar e produzir relatórios, planos, checklists, roteiros, diagnósticos e memórias.
- Pode acionar subagentes reais para tarefas complexas.
- Pode pesquisar na web com Tavily depois de consultar o Cofre.
- Pode operar canais/mensagens, navegador, arquivos, PDFs, imagens, áudio, vídeo, cron jobs e integrações Zapier conectadas.
- Integrações Zapier vistas: Miro, Gmail, Google Calendar, Google Drive e Notion. Observação: TOOLS.md registra decisão de usar Google preferencialmente via `gog`/scripts diretos, não Zapier, salvo autorização.

## Observações
- Memory search estava indisponível por erro de chave de embeddings; foi feito fallback por leitura direta, find e grep conforme Constituição.
- Relatório salvo para continuidade.

## Fontes
CONSTITUICAO.md, MAPA.md, AGENTS.md, SOUL.md, USER.md, TOOLS.md, HEARTBEAT.md e listagem Zapier habilitada.

---

## Complemento — Árvore dos agentes do sistema

### Raiz
- Jadielson Davi — dono absoluto e decisor final
- Lôh — Orquestradora Tier 0 / gerente geral do ecossistema

### Camada 1 — Grupos principais
1. LÓGIKA / Empresa
   - General local: Jarvis
   - C-Level Squad: COO, CRO, CMO, CCO, CFO, CAIO, CTO, CIO
   - Operacionais por área: comercial, marketing, criação, operações, financeiro, tecnologia, governança e IA
2. Central Pessoal
   - General local: Alfred
   - Especialistas principais: Arca, Warren, Projetos Pessoais, Estudos
   - Especialistas pessoais por tópico: Identidade e Visão de Futuro, Liberdade/Lazer/Ócio Criativo, Autoconhecimento, Saúde/Corpo/Energia, Família/Relacionamentos, Espiritualidade/Propósitos
3. Frentes/clientes e tópicos especializados
   - Saúde São Sebastião, Câmara Municipal, SINDSS, Bases Públicas, Clara, Lab/Testes e outros tópicos operacionais conforme protocolo.

### Regra de orquestração
Demandas com múltiplos agentes passam pela Lôh. Generais coordenam seus grupos localmente. Nenhum agente simula outro agente.

