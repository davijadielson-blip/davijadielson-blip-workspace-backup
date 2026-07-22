---
tema: backlog inteligente prints projetos subprojetos tarefas 2...
atualizado_em: 2026-07-22
---

# Backlog Inteligente — Prints de projetos, subprojetos e tarefas

**Data:** 2026-07-20  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Material:** prints adicionais enviados por Jadielson sobre o sistema de organização.  
**Correção de Jadielson:** não se trata apenas de matrizes; trata-se de um sistema de organização de projetos, subprojetos e tarefas.

## Leitura corrigida

Jadielson está correto: os prints não devem ser interpretados apenas como referências de Matriz Eisenhower ou Esforço x Impacto. Eles apontam para um sistema operacional completo com hierarquia de organização.

A matriz é apenas uma das visões. O núcleo real é a relação:

```text
Área / Tema → Projeto → Subprojeto → Tarefa → Subtarefa / Próxima ação
```

## Implicação para o Mission Control

O Mission Control precisa ter duas camadas:

### 1. Camada estrutural

Responsável por organizar o universo de demandas:

- áreas de vida;
- projetos;
- subprojetos;
- tarefas;
- responsáveis;
- prazos;
- status;
- vínculos com Drive, Cofre, Calendar e xTiles.

### 2. Camada de visualização/decisão

Responsável por mostrar recortes úteis:

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

## Correção no blueprint

O blueprint deve deixar claro que:

- Matriz Eisenhower não é o sistema inteiro.
- Esforço x Impacto não é o sistema inteiro.
- Essas matrizes são apenas formas de enxergar tarefas já estruturadas.
- O banco/estrutura principal deve ser hierárquico: projeto/subprojeto/tarefa.

## Modelo de entidade recomendado

### Área / Tema

Exemplos:

- Saúde;
- Família;
- Estudos;
- Finanças;
- Trabalho;
- Projetos pessoais;
- LÓGIKA/clientes, com parede-d'água.

### Projeto

Possui objetivo e resultado desejado.

Campos:

- nome;
- área;
- status;
- prioridade;
- prazo macro;
- descrição;
- links;
- subprojetos;
- tarefas.

### Subprojeto

Parte de um projeto maior.

Campos:

- nome;
- projeto pai;
- objetivo;
- status;
- próxima ação;
- tarefas vinculadas.

### Tarefa

Unidade de execução.

Campos:

- verbo + objeto;
- projeto/subprojeto;
- responsável;
- complexidade;
- impacto;
- prioridade;
- prazo de execução;
- prazo de entrega;
- padrão de trava;
- status;
- próxima ação.

## Decisão

Atualizar o Mission Control para ser primeiro um **sistema hierárquico de organização** e só depois um painel de matrizes.

A pergunta central deixa de ser apenas “em qual quadrante está essa tarefa?” e passa a ser:

1. A qual área isso pertence?
2. Isso é projeto, subprojeto ou tarefa?
3. Qual é a próxima ação?
4. Onde isso aparece hoje/semana/matriz/agenda?
5. Isso está travado, delegável ou incubado?

## Próximo passo

Atualizar o blueprint do Mission Control com a seção `Arquitetura hierárquica: Áreas → Projetos → Subprojetos → Tarefas`.
