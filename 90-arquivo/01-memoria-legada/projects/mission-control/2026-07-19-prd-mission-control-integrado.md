---
tema: 07 19 prd mission control integrado
atualizado_em: 2026-07-22
---

# PRD — Mission Control Integrado Jadielson/Lôh

**Data:** 2026-07-19  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** PRD v0.1 aprovado em direção macro: opção 5 — tudo integrado.  
**Escopo:** Cockpit central para agência, vida pessoal/produtividade, produção de conteúdo, projetos, agentes e decisões.

---

## 1. Resumo executivo

O **Mission Control Integrado** será a central visual e operacional do ecossistema Jadielson/Lôh. A proposta é começar simples, mas com arquitetura preparada para crescer.

Ele deve funcionar como uma tela de comando para responder rapidamente:

- O que é prioridade agora?
- Quais projetos/frentes estão ativos?
- Que tarefas estão pendentes, em andamento ou travadas?
- Que conteúdos precisam ser roteirizados, gravados, editados ou publicados?
- Quais agentes existem e quem deve executar cada tipo de demanda?
- Quais decisões recentes foram tomadas?
- Onde está cada informação importante dentro do Cofre?

---

## 2. Princípio do produto

**Tudo integrado, começando simples.**

O MVP não deve tentar resolver todas as integrações externas de uma vez. Primeiro ele deve organizar o cockpit com dados vindos do Cofre e de arquivos Markdown estruturados. Depois, evolui para integrações com Google Sheets, Trello/Notion, calendário, redes sociais e comandos para agentes.

---

## 3. Usuário principal

**Jadielson Davi** — filmmaker/videomaker, servidor público municipal, dono de agência em início de estruturação e criador do ecossistema Lôh/agentes.

Necessidade central: reduzir dispersão, enxergar prioridades e transformar o ecossistema de arquivos/agentes em uma operação visível, simples e acionável.

---

## 4. Módulos do Mission Control

### 4.1 Cockpit Hoje / Semana

Mostra:

- prioridade do dia
- prioridade da semana
- próximos prazos
- alertas
- demandas aguardando Jadielson
- últimas decisões importantes

### 4.2 Projetos e Frentes

Mostra:

- projetos ativos
- clientes/frentes em andamento
- status: ativo, pausado, aguardando, concluído
- próximo passo de cada frente
- link para pasta/arquivo no Cofre

Fontes iniciais:

- `[F1] 5-Frentes/`
- `[F3] PROJETOS/`
- `[F2] memory/projects/`

### 4.3 Kanban Operacional

Colunas iniciais:

- Backlog
- Próximas
- Em andamento
- Aguardando Jadielson
- Aguardando terceiro/cliente
- Concluído

Cada card deve conter:

- título
- frente/projeto
- responsável/agente sugerido
- prioridade
- prazo, se houver
- link de contexto

### 4.4 Produção de Conteúdo

Pipeline:

- Ideias
- Roteiro
- Gravação
- Edição
- Aprovação
- Publicação
- Reaproveitamento

Campos recomendados:

- plataforma
- objetivo do conteúdo
- status
- responsável
- prazo
- arquivos relacionados

### 4.5 Agentes e Ecossistema

Mostra:

- agentes principais
- função de cada agente
- quando acionar
- status/observações
- links para definições em `[F2] agentes/` e `[F2] memory/agents/`

### 4.6 Vida / Produtividade Pessoal

Mostra de forma leve, sem invadir a parede d'água pessoal:

- lembretes pessoais operacionais
- estudos em andamento
- hábitos/rotina se Jadielson quiser
- finanças apenas como atalho/resumo, nunca exposição completa sem decisão posterior

Fontes:

- `[F1] ESTUDOS/`
- `[F1] 4-Pessoal/` apenas como consulta cuidadosa
- arquivos específicos autorizados depois

### 4.7 Memória, Decisões e Próximos Passos

Mostra:

- decisões recentes
- registros de briefing
- próximos passos salvos
- arquivos importantes recentes

Fontes:

- `[F2] memory/decisions/`
- `[F2] memory/sessions/`
- `[F2] memory/context/`
- `[F2] memory/projects/`

---

## 5. MVP recomendado

### MVP 1 — Painel em Markdown estruturado

Criar primeiro um arquivo central `.md` com visão operacional atual, fácil de manter pelo ecossistema.

Arquivo sugerido:

`/data/.openclaw/workspace/[F2] memory/visualizations/dashboards/mission-control.md`

Vantagens:

- rápido
- seguro
- compatível com regra do Cofre: somente `.md`
- pode ser atualizado por agentes
- vira base para dashboard web depois

### MVP 2 — Dashboard web local/online

Depois do painel Markdown, criar aplicação visual com:

- cards
- kanban
- filtros por frente
- visão semanal
- links para arquivos do Cofre

Stack candidata:

- Next.js
- Tailwind
- Supabase ou arquivo estruturado como fonte inicial
- deploy Vercel/Cloudflare Pages

---

## 6. Requisitos funcionais

1. Exibir prioridades atuais.
2. Listar frentes/projetos ativos.
3. Exibir Kanban operacional.
4. Exibir pipeline de conteúdo.
5. Exibir mapa de agentes.
6. Exibir decisões recentes.
7. Conectar cada item a uma fonte no Cofre.
8. Permitir atualização incremental por agentes.
9. Separar o que é público/operacional do que é pessoal/sensível.
10. Preparar estrutura para integrações futuras.

---

## 7. Requisitos não funcionais

- Simplicidade antes de complexidade.
- Nenhuma informação sensível deve ser exposta sem revisão.
- O Cofre permanece fonte de verdade.
- O dashboard não substitui o Cofre; apenas visualiza e organiza.
- Toda decisão importante deve continuar sendo salva em `.md`.
- Nada de salvar arquivos não-Markdown dentro do Cofre.

---

## 8. Fases de implementação

### Fase 1 — Estrutura documental

- Criar PRD.
- Criar arquivo central `mission-control.md`.
- Criar templates de cards e status.
- Mapear fontes do Cofre.

### Fase 2 — População manual assistida

- Preencher primeiras frentes.
- Preencher primeiros cards do Kanban.
- Mapear agentes principais.
- Definir prioridades da semana.

### Fase 3 — Prototipagem visual

- Escolher stack/template.
- Criar dashboard web inicial.
- Consumir dados do Markdown/estrutura intermediária.

### Fase 4 — Integrações

- Google Sheets/Calendário.
- Trello/Notion, se desejado.
- Métricas de redes sociais.
- Comandos/links para acionar agentes.

### Fase 5 — Operação contínua

- Rotina diária/semana de atualização.
- Relatórios semanais.
- Revisão de projetos parados.
- Evolução do cockpit.

---

## 9. Decisão registrada

Jadielson escolheu: **Opção 5 — tudo integrado.**

Interpretação da Lôh: criar uma central única, mas com MVP progressivo para não travar por excesso de escopo.

---

## 10. Próximo passo imediato

Criar o arquivo operacional:

`[F2] memory/visualizations/dashboards/mission-control.md`

com a primeira visão integrada em formato Markdown.

