---
tipo: diagrama
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Timeline de Projetos

> Projetos organizados por status. Atualizar quando houver mudança de fase.

```mermaid
gantt
    title Projetos — Visão Geral
    dateFormat  YYYY-MM-DD
    axisFormat  %b/%y

    section Em Andamento
    [a preencher]           :active, p1, 2026-05-01, 30d

    section Pronto para Iniciar
    [a preencher]           :p2, 2026-06-01, 20d

    section Pensando
    [a preencher]           :crit, p3, 2026-05-10, 45d

    section Aguardando
    [a preencher — bloqueado por fator externo] :p4, 2026-05-10, 30d
```

---

## Sistema de Status

```mermaid
stateDiagram-v2
    [*] --> Pensando : nova ideia
    Pensando --> Pronto_para_Iniciar : decisão tomada
    Pronto_para_Iniciar --> Em_Andamento : início efetivo
    Em_Andamento --> Aguardando : bloqueio externo
    Aguardando --> Em_Andamento : desbloqueado
    Em_Andamento --> Finalizado : entrega concluída
    Em_Andamento --> Abortado : cancelado
    Finalizado --> Arquivado : após 30 dias
```

---

## Projetos por Status

### Em Andamento

```dataview
LIST
FROM "[F1] 5-Frentes/Projetos/Em-Andamento"
SORT file.name ASC
```

### Pronto para Iniciar

```dataview
LIST
FROM "[F1] 5-Frentes/Projetos/Pronto-para-Iniciar"
SORT file.name ASC
```

### Aguardando

```dataview
LIST
FROM "[F1] 5-Frentes/Projetos/Aguardando"
SORT file.name ASC
```

### Pensando

```dataview
LIST
FROM "[F1] 5-Frentes/Projetos/Pensando"
SORT file.name ASC
```
