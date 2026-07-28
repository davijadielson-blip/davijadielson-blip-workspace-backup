---
tema: backlog inteligente prints dashboard requisitos ui 2026 0...
atualizado_em: 2026-07-22
---

# Backlog Inteligente — Prints de dashboard — requisitos de UI

**Data:** 2026-07-20  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Material:** 3 prints de referência de dashboard/app enviados por Jadielson.

## Observação técnica

A análise visual automática desta rodada teve instabilidade/time-out, mas os prints já tinham sido visualizados/analisados anteriormente no tópico. Esta nota consolida os requisitos extraídos dos prints.

## Prints identificados

### 1. Matriz Eisenhower

Elementos principais:

- Sidebar com: Todas, Hoje, Amanhã, Esta Semana, Atrasadas, Backlog, Agenda, Matriz Eisenhower, Esforço x Impacto, Projetos, Templates, Integrações, Time, Delegadas.
- Busca: `Buscar tarefas...`
- Filtros: Todas, Hoje, Amanhã, 7 dias.
- Opções: `Inteligente`, `Mostrar sem data`.
- Quadrantes:
  - Fazer agora;
  - Possibilidade de delegar;
  - Planejar;
  - Revisar e ver se é realmente necessário.
- Botão flutuante `+`.

### 2. Criar tarefa

Campos principais:

- Projeto/subprojeto;
- Responsável;
- Complexidade: Fácil, Médio, Difícil;
- Impacto: Alto, Baixo;
- Prioridade: P1, P2, P3;
- Prazo ou entrega: Hoje, Amanhã, Semana, Próx. Semana, selecionar data;
- Descrição;
- Opções avançadas;
- Criar tarefa.

### 3. Esforço x Impacto

Quadrantes:

- Quick Wins — fazer primeiro;
- Planejar para fazer — planejar bem;
- Executar quando possível — quando sobrar;
- Possibilidade de descarte — delegar/eliminar.

Também apresenta busca, filtros, botão `Organizar com I.A`, opção `Mostrar sem data` e botão flutuante `+`.

## Requisitos de interface extraídos

1. Sidebar fixa com visões temporais, backlog, agenda, matrizes, projetos, templates, integrações e delegadas.
2. Busca global/contextual no topo.
3. Filtros rápidos por período.
4. Alternância `Mostrar sem data`.
5. Modo/botão `Inteligente` ou `Organizar com I.A`.
6. Matrizes com 4 quadrantes, cores semânticas e contadores.
7. Cadastro de tarefa com campos suficientes para a IA classificar.
8. Botão de captura rápida sempre visível.
9. Separação clara entre execução, planejamento, delegação e descarte.
10. Suporte a tarefas delegadas/time, mesmo que isso fique para versão futura.

## Como isso altera o blueprint

O Mission Control deve priorizar 3 experiências centrais:

1. **Captura rápida:** criar item sem fricção.
2. **Classificação inteligente:** impacto, esforço, prioridade, prazo, responsável e padrão de trava.
3. **Visão decisória:** matrizes para decidir fazer, planejar, delegar, descartar ou destravar.

## Decisão de design

O MVP deve começar com as telas:

1. Hoje;
2. Inbox;
3. Matriz Eisenhower;
4. Esforço x Impacto;
5. Criar Tarefa;
6. Travados / Protocolo 10 min;
7. Revisão Semanal.

As telas Projetos, Delegadas, Integrações e Time podem entrar como v1/v2 após o piloto.
