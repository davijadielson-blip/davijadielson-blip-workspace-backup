---
tema: mission control blueprint mvp v1 2026 07 20
atualizado_em: 2026-07-22
---

# Backlog Inteligente — Mission Control — Blueprint MVP v1

**Data:** 2026-07-20  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Solicitante:** Jadielson Davi  
**Status:** Blueprint inicial para validação e posterior avaliação técnica por Lôh.

## 1. Ideia central

Criar um **Mission Control pessoal** para Jadielson, inspirado no Backlog Inteligente, no Método TDAH e nas referências visuais enviadas.

O sistema deve funcionar como cockpit único para transformar captura solta em execução real.

```text
Capturar → Clarear → Fatiar → Priorizar → Agendar → Executar → Revisar
```

## 2. Tese do produto

Jadielson não precisa de mais uma lista de tarefas. Precisa de um cockpit que responda rapidamente:

1. O que existe?
2. O que faço hoje?
3. O que está atrasado?
4. O que está travado?
5. O que tem alto impacto?
6. O que devo planejar, delegar, descartar ou executar agora?
7. O que entra na agenda?
8. O que precisa ser salvo no Cofre como decisão/contexto?

## 3. Nome provisório

Opções:

1. **Backlog Inteligente — Mission Control**
2. **Mission Control 70%**
3. **Cockpit Pessoal Jadielson**
4. **Central de Execução 70%**
5. **BI Control — Backlog Inteligente**

Nome recomendado inicial: **Backlog Inteligente — Mission Control**.

## 4. Papéis das camadas

```text
Mission Control = interface operacional
xTiles = protótipo visual / cockpit humano inicial
Google Calendar = compromissos e blocos de tempo
Cofre = fonte de verdade, método, decisões e memória
Central/Agentes = inteligência, triagem, síntese e recomendações
```

## 5. MVP — Telas principais

### 5.1 Inbox

Entrada bruta de tudo:

- tarefas;
- ideias;
- pendências;
- links;
- preocupações;
- demandas externas;
- estudos;
- projetos;
- decisões abertas.

Objetivo: capturar sem pensar demais.

### 5.2 Hoje

Mostra apenas o que cabe no dia.

Blocos:

- Tarefa #1;
- 3 prioridades do dia;
- compromissos fixos;
- bloco de foco;
- tarefas leves;
- travados que precisam de protocolo 10 min.

### 5.3 Amanhã

Preparação do dia seguinte.

Campos:

- 3 prioridades de amanhã;
- PD crítica;
- microvitória PG;
- compromisso importante;
- bloco de energia a proteger.

### 5.4 Esta Semana

Visão semanal:

- entregas;
- prazos;
- projetos ativos;
- estudos ativos;
- compromissos importantes;
- pendências críticas;
- revisão semanal.

### 5.5 Atrasadas

Tudo que venceu ou ficou para trás.

Não serve para culpa. Serve para decisão:

- reagendar;
- cancelar;
- fatiar;
- delegar;
- mover para incubação;
- executar 10 minutos.

### 5.6 Backlog

Área de espera consciente.

Não é cemitério. Cada item precisa ter estado:

- capturado;
- esclarecido;
- fatiado;
- agendado;
- executado/revisado;
- incubado;
- descartado.

### 5.7 Agenda

Camada de tempo.

Deve conversar com Google Calendar.

Tipos:

- compromissos;
- blocos de foco;
- blocos de comunicação;
- blocos de estudo;
- blocos financeiros;
- revisão diária/semanal.

### 5.8 Matriz Eisenhower

Quadrantes:

1. **Fazer agora** — urgente e importante.
2. **Planejar** — importante, mas não urgente.
3. **Delegar** — urgente, mas não exige Jadielson.
4. **Revisar/Eliminar** — baixo valor ou falso compromisso.

### 5.9 Esforço x Impacto

Quadrantes:

1. **Quick Wins** — alto impacto, baixo esforço.
2. **Planejar para fazer** — alto impacto, alto esforço.
3. **Executar quando possível** — baixo impacto, baixo esforço.
4. **Possibilidade de descarte** — baixo impacto, alto esforço.

### 5.10 Projetos

Lista de projetos ativos, com:

- objetivo;
- área;
- status;
- próxima ação;
- prazo;
- energia exigida;
- relação PG/PD;
- links do Cofre/Drive/xTiles.

### 5.11 Templates

Modelos prontos:

- tarefa boa;
- projeto;
- compromisso;
- revisão diária;
- revisão semanal;
- protocolo 10 minutos;
- painel 1 página;
- estudo/curso;
- decisão.

### 5.12 Travados / Protocolo 10 min

Área para tarefas paradas.

Campos:

- tarefa travada;
- padrão de trava;
- menor ação;
- ambiente necessário;
- timer de 10 minutos;
- próxima revisão.

### 5.13 Revisão Semanal

Perguntas:

1. O que avancei?
2. O que ficou parado?
3. O que está me drenando?
4. O que precisa sair do sistema?
5. Qual PG da semana?
6. Qual PD crítica?
7. Qual rotina funcionou 70%?

## 6. Modelo de dados da tarefa

```yaml
id:
titulo:
tipo: tarefa | compromisso | projeto | decisao | ideia | preocupacao
area:
projeto:
subprojeto:
responsavel:
status: capturado | esclarecido | fatiado | agendado | executando | concluido | incubado | descartado
prioridade: P1 | P2 | P3
impacto: alto | medio | baixo
complexidade: facil | media | dificil
energia: leve | media | pesada
pg_pd: PG | PD | essencial | incubacao
prazo_execucao:
prazo_entrega:
proxima_acao:
criterio_concluido:
padrao_trava: perfeicao | hiperfoco | evitacao | tempo | inicio | revisao_infinita | colapso | nenhum
delegavel: sim | nao | talvez
origem: telegram | xtiles | cofre | calendar | manual | drive
links:
  cofre:
  xtiles:
  calendar:
  drive:
criado_em:
atualizado_em:
revisado_em:
```

## 7. Motor de IA — funções desejadas

### 7.1 Organizar com IA

Dado um conjunto de itens, a IA sugere:

- tipo;
- área;
- projeto;
- prioridade;
- impacto;
- complexidade;
- energia;
- próxima ação;
- matriz Eisenhower;
- matriz esforço x impacto;
- se deve ir para agenda.

### 7.2 Fatiar tarefa

Transforma item grande em próximas ações pequenas.

### 7.3 Diagnosticar trava

Identifica padrão dominante:

- perfeição;
- hiperfoco;
- evitação emocional;
- superestimação de tempo;
- sobrecarga de início;
- revisão infinita;
- colapso pós-esforço.

### 7.4 Montar ordem do dia

Com base em energia, compromissos e prioridades, sugere:

- tarefa #1;
- 3 prioridades;
- 1 microvitória PG;
- 1 PD crítica;
- 1 tarefa leve de ativação.

### 7.5 Revisar semana

Gera síntese e recomendações:

- manter;
- cortar;
- reagendar;
- delegar;
- proteger;
- transformar em projeto.

## 8. MVP sem desenvolvimento pesado

### Etapa 1 — xTiles

Criar páginas/blocos no xTiles replicando as telas principais.

### Etapa 2 — Cofre

Criar templates `.md` para tarefa, projeto, revisão e painel 1 página.

### Etapa 3 — Google Calendar

Usar `gog` para compromissos e blocos de tempo.

### Etapa 4 — Rotina manual assistida

Durante 7 dias:

- Jadielson usa xTiles;
- Central recebe prints/exports ou relatos;
- Central salva sínteses no Cofre;
- ajustar o modelo.

## 9. Critérios de sucesso do piloto

O piloto funciona se:

1. Jadielson capturar mais rápido.
2. A ordem do dia ficar mais clara.
3. Tarefas travadas virarem ações de 10 minutos.
4. O sistema não gerar trabalho duplicado.
5. O xTiles for usado naturalmente.
6. O Cofre guardar só o que importa.
7. A revisão semanal gerar decisão real.

## 10. Riscos

1. Virar ferramenta bonita sem execução.
2. Duplicar alimentação xTiles + Cofre.
3. Complexidade excessiva no início.
4. Depender de API inexistente/instável.
5. Misturar vida pessoal com LÓGIKA/clientes sem parede-d'água.
6. Transformar tudo em app antes de validar hábito.

## 11. Decisão recomendada

Não construir app próprio ainda.

Primeiro criar o **Mission Control v0 no xTiles** e validar por 7 dias.

Depois, se funcionar, Lôh avalia arquitetura para:

- integração xTiles ↔ Cofre;
- Google Calendar;
- banco de dados;
- interface própria;
- agentes de triagem;
- segurança/autenticação.

## 12. Próximos passos imediatos

1. Criar template visual do Mission Control para xTiles.
2. Criar `Painel 1 Página do Backlog Inteligente`.
3. Criar 3 templates `.md` no Cofre: tarefa, projeto, revisão semanal.
4. Enviar para Lôh avaliar arquitetura técnica.

---

## 13. Atualização — Arquitetura hierárquica de projetos, subprojetos e tarefas

Após novos prints e correção de Jadielson, fica decidido que o Mission Control não deve ser tratado apenas como um conjunto de matrizes.

As matrizes são **visões de decisão**. O núcleo do sistema é uma hierarquia operacional:

```text
Área / Tema → Projeto → Subprojeto → Tarefa → Subtarefa / Próxima ação
```

### 13.1 Camada estrutural

A camada estrutural organiza o universo de demandas antes de qualquer matriz:

- áreas de vida;
- frentes;
- projetos;
- subprojetos;
- tarefas;
- subtarefas;
- responsáveis;
- prazos;
- vínculos com Cofre, Drive, Calendar e xTiles.

### 13.2 Camada de visualização

Depois que os itens estão estruturados, eles podem aparecer em múltiplas visões:

- Hoje;
- Amanhã;
- Esta semana;
- Atrasadas;
- Backlog;
- Agenda;
- Matriz Eisenhower;
- Esforço x Impacto;
- Delegadas;
- Travados / Protocolo 10 min;
- Revisão semanal.

### 13.3 Regra de modelagem

Todo item deve responder primeiro:

1. A qual área pertence?
2. É projeto, subprojeto ou tarefa?
3. Quem é responsável?
4. Qual é a próxima ação?
5. Qual o prazo de execução?
6. Em quais visões deve aparecer?

Só depois disso ele deve ser distribuído nas matrizes.

### 13.4 Implicação para o MVP

O MVP precisa incluir uma tela/visão de **Projetos** robusta, com navegação por:

- Área;
- Projeto;
- Subprojeto;
- Tarefas vinculadas;
- Progresso;
- Próxima ação;
- Status;
- Prazos.

As telas de matriz continuam importantes, mas deixam de ser o centro do produto. O centro passa a ser a organização hierárquica + execução diária.
