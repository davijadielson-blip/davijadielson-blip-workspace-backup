# Mission Control — Briefing inicial para Jadielson

**Data:** 2026-07-19  
**Solicitante:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** Briefing inicial criado; aguardando definição de escopo e autorização para execução técnica.

## Pedido original

Jadielson pediu: “LOH, CONSEGUE CRIAR PRA MIM UM MISSION CONTROL?”

## Interpretação operacional

Criar um **Mission Control** como cockpit visual do ecossistema Jadielson/Lôh: uma central para acompanhar projetos, frentes, tarefas, agentes, conteúdos, decisões e próximos passos em uma única visão.

## Direção recomendada para MVP

### Objetivo do MVP

Construir uma primeira versão simples, útil e evolutiva, sem tentar integrar tudo de uma vez.

### Módulos prioritários

1. **Visão geral do dia/semana**
   - prioridades atuais
   - próximas entregas
   - alertas
   - pendências críticas

2. **Projetos e frentes**
   - clientes/frentes ativas
   - status por projeto
   - próximos passos
   - links para arquivos do Cofre

3. **Agentes / ecossistema**
   - quem faz o quê
   - agentes principais
   - demandas atribuídas
   - status de execução

4. **Kanban operacional**
   - Backlog
   - Em andamento
   - Aguardando Jadielson
   - Concluído

5. **Conteúdo / agência**
   - ideias de conteúdo
   - roteiros em produção
   - gravações
   - edições
   - publicações

6. **Memória e decisões**
   - últimas decisões registradas
   - arquivos recentes importantes
   - links internos do Cofre

## Caminho técnico recomendado

### Fase 1 — Produto no papel
Criar PRD completo: escopo, telas, módulos, dados, integrações e fases.

### Fase 2 — Protótipo local
Criar um dashboard simples, inicialmente com dados em Markdown/JSON gerado a partir do Cofre, sem integrações externas complexas.

### Fase 3 — Integrações
Adicionar, conforme prioridade:
- Trello/Notion/Google Sheets, se Jadielson quiser
- calendário
- métricas de redes sociais
- comandos para acionar agentes

### Fase 4 — Deploy
Publicar em ambiente acessível, preferencialmente Vercel/Cloudflare Pages + backend simples, se necessário.

## Perguntas pendentes

1. Você quer que o Mission Control seja:
   - dashboard visual web;
   - página simples em Markdown/HTML;
   - painel dentro do Telegram;
   - ou os três em fases?

2. Prioridade principal:
   - agência/clientes;
   - vida pessoal/produtividade;
   - agentes/ecossistema;
   - conteúdo/redes sociais;
   - tudo integrado?

3. Você quer começar com uma versão rápida e funcional ou uma versão mais bonita/ambiciosa?

## Próximo passo recomendado

Lôh deve apresentar ao Jadielson uma proposta curta de MVP e pedir autorização para criar o PRD + estrutura inicial do projeto no Cofre.

## Fontes internas consultadas

- `/data/.openclaw/workspace/CONSTITUICAO.md`
- `/data/.openclaw/workspace/MAPA.md`
- `/data/.openclaw/workspace/AGENTS.md`
- `/data/.openclaw/workspace/SOUL.md`
- `/data/.openclaw/workspace/USER.md`
- `/data/.openclaw/workspace/[F2] archive/cheatsheets-legacy-v1.0/mission-control.md`
