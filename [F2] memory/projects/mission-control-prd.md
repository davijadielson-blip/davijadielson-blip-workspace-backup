# 🧠 PRD — Mission Control

> **Produto:** Painel Central de Comando (Mission Control)
> **Dono:** Jadielson Davi
> **Orquestradora:** Lôh (Tier 0)
> **Versão do Documento:** 1.0
> **Data:** 20/07/2026
> **Status:** ✅ Mockup aprovado — Pronto para Fase 2

---

## 1. Visão Geral

### 1.1 Propósito

Centralizar em um único painel visual todas as áreas da vida profissional de Jadielson: tarefas, projetos, agentes, conteúdos, métricas, pendências e relatórios — eliminando a necessidade de abrir múltiplos arquivos, abas ou ferramentas para ter visão do todo.

### 1.2 Público

- **Único usuário:** Jadielson Davi
- **Acesso:** Local (arquivo HTML no Cofre) — futuramente podendo ser servido via HTTP

### 1.3 Stack

| Camada | Tecnologia |
|---|---|
| Front-end | HTML5 + CSS3 + JavaScript puro (zero dependências) |
| Dados (Fase 1) | Mockados inline |
| Dados (Fase 2) | Arquivos `.md` do Cofre via leitura de arquivo |
| Dados (Fase 3) | APIs externas (Google Calendar, Trello, etc.) |

---

## 2. Arquitetura do Painel

### 2.1 Camadas

```
┌─────────────────────────────────────────────────┐
│                 HEADER                           │
│  Título + Subtítulo | Filtro | Data + Status     │
├─────────────────────────────────────────────────┤
│               NAVEGAÇÃO (6 Abas)                 │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌───────────────┬─────────────────────────┐     │
│  │  ESTRATÉGICO  │      TÁTICO             │     │
│  │  · Métricas   │  · Kanban de Tarefas    │     │
│  │  · Relatórios │  · Projetos Ativos      │     │
│  │               │  · Agentes              │     │
│  ├───────────────┼─────────────────────────┤     │
│  │  OPERACIONAL                             │     │
│  │  · Pendências  · Alertas  · Conteúdos    │     │
│  └───────────────┴─────────────────────────┘     │
│                                                  │
└─────────────────────────────────────────────────┘
```

### 2.2 Temas de Design
- **Fundo:** Black piano (`#000000`)
- **Cards:** `#080808` com borda sutil `#181818`
- **Header/Abas:** `#050505`
- **Tipografia:** Sistema nativa (SF/Inter/Segoe UI), limpa e legível
- **Cores de destaque:** Azul (`#3b82f6`), Verde (`#22c55e`), Laranja (`#fb923c`), Vermelho (`#ef4444`)

---

## 3. Funcionalidades por Aba

### 3.1 📊 Visão Geral (Dashboard Principal)

| Componente | Descrição | Fonte de Dados (Fase 2) |
|---|---|---|
| Blocos do Dia | Lista de blocos de horário com status (verde=feito, azul=agora, cinza=próximo) | `[F1] 3-Daily/` ou configuração manual |
| Agenda de Hoje | Eventos do dia com horários | Google Calendar API (Fase 3) ou manual |
| Horas Trabalhadas | Progresso semanal com meta | Cálculo sobre blocos do dia |
| Widget Eficiência | Percentual com indicador de tendência | Cálculo interno |
| Widget Tarefas | Contagem concluídas/total + barra | `[F2] memory/` tasks |
| Widget Carga | Horas trabalhadas vs meta | Blocos do dia |
| Widget NPS | Score + badge qualitativo | Input manual |
| Task Board (Resumo) | Mini kanban 4 colunas | `[F2] memory/tasks/` |
| Alertas Ativos | Lista de alertas por severidade | `[F2] memory/decisions/` + jobs |
| Agentes Rodando | Quem está ativo agora | Leitura de estado dos agentes |

### 3.2 📋 Tarefas (Kanban Completo)

| Componente | Descrição |
|---|---|
| 4 Colunas | Backlog → A Fazer → Fazendo → Concluído |
| Cards | Título, tags, responsável, barra de progresso |
| Filtros | Por projeto, agente, prioridade (Fase 3) |
| Drag & Drop | Mover cards entre colunas (Fase 3) |

### 3.3 📁 Projetos

| Componente | Descrição |
|---|---|
| Projetos Ativos (máx 3) | Nome, fase, %, próximo marco, bloqueios |
| Próximos a Iniciar | Fila de projetos standby |
| Atalhos | Links para pastas do Cofre |

### 3.4 🤖 Agentes

| Componente | Descrição |
|---|---|
| Tabela de Agentes | Nome, Tier, Função, Status, Ocupação |
| Indicador de Ocupação | % de agentes ativos vs total |
| Acesso Rápido | Botões para acionar agente (Fase 3) |

### 3.5 ⚠️ Alertas

| Componente | Descrição |
|---|---|
| Críticos (🔴) | Jobs falhando, prazos estourados |
| Atenção (🟡) | Prazos próximos, tarefas paradas |
| Rotina (🔵) | Lembretes diários |
| Resolvidas | Histórico do dia |

### 3.6 📈 Relatório Semanal

| Componente | Descrição |
|---|---|
| Consolidado | Tarefas, projetos, conteúdos, horas |
| Receita | Gerada (semana) e Potencial (mês) |
| O que não foi feito | Itens que escorregaram |
| Prioridades | Top 5 da próxima semana |
| Métricas | Taxa de conclusão, produtividade, conteúdos |

---

## 4. Roadmap de Implementação

```
FASE 1 — Mockup ✅
├── HTML estático com dados fictícios
├── Todas as 6 abas navegáveis
├── Tema black piano aprovado
└── Arquivo: mission-control.html

FASE 2 — Dados Reais do Cofre 🔜 (PRÓXIMA)
├── Conectar arquivos .md como fonte de dados
├── Kanban lendo de [F2] memory/tasks/
├── Projetos lendo de [F3] PROJETOS/
├── Alertas lendo de jobs e decisões
├── Métricas calculadas do Cofre
└── Geração automática do HTML via script

FASE 3 — Interatividade + APIs (⏳ Futuro)
├── Botões para mover cards (drag & drop)
├── Conexão Google Calendar (agenda real)
├── Conexão GitHub (commits e atividades)
├── Auto-refresh periódico
└── (Requer autorização explícita de Jadielson)
```

---

## 5. Regras de Negócio

### 5.1 Limites
- Máx. 3 projetos em andamento simultâneos
- Máx. 3 estudos em andamento simultâneos
- Meta de horas semanais: 20h
- NPS: 0-30 = Poor, 31-50 = Good, 51-70 = Excellent, 71-100 = Outstanding

### 5.2 Atualização
- Fase 2: O HTML é estático — para atualizar, reexecutar o script gerador
- Fase 3: Auto-refresh a cada 5 minutos

### 5.3 Segurança
- Nenhuma credencial ou API key armazenada no HTML
- Dados sensíveis permanecem no Cofre (nunca expostos em rede)

---

## 6. Critérios de Aceite

- [x] Mockup aprovado visualmente por Jadielson
- [ ] Fase 2: Dados reais refletindo o estado atual do Cofre
- [ ] Fase 2: Todas as 6 abas populadas com dados verdadeiros
- [ ] Fase 3: Interatividade funcional (mover cards, filtrar)
- [ ] Fase 3: Integração com Google Calendar e GitHub

---

## 7. Limitações Conhecidas

- Fase 1/2: HTML estático — não atualiza automaticamente
- Fase 1/2: Sem drag & drop — cards são visuais apenas
- Fase 1/2: Dados do Cofre precisam ser parseados em formato adequado
- Navegador sandbox indisponível para previews ao vivo

---

*Documento mantido em [F2] memory/projects/mission-control-prd.md*
*PRD aprovado junto com mockup em 20/07/2026*
