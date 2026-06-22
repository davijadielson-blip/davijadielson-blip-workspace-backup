---
tipo: cockpit
subtipo: geral
---

# 🧠 COCKPIT GERAL — Jadielson Davi

> Visão unificada de projetos e estudos. Escolha **1 projeto + 1 estudo** para avançar hoje.
> Para detalhes: [[PROJETOS/COCKPIT]] · [[ESTUDOS/COCKPIT]]

---

## PROJETOS

### 🟢 Projetos em andamento

```dataview
TABLE WITHOUT ID
  file.link AS "🚀 Projeto",
  frente AS "Frente",
  fase-atual AS "Fase",
  destino-matriz AS "Matriz"
FROM "PROJETOS/EM ANDAMENTO"
WHERE tipo = "projeto"
SORT frente ASC
```

### 🟡 Próximos a iniciar

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente",
  fase-atual AS "Fase"
FROM "PROJETOS/A INICIAR"
WHERE tipo = "projeto"
SORT frente ASC
LIMIT 5
```

---

## ESTUDOS

### 🟢 Estudos em andamento

```dataview
TABLE WITHOUT ID
  file.link AS "📚 Estudo",
  subtipo AS "Tipo",
  instrutor AS "Instrutor/Autor",
  aulas-concluidas + "/" + total-aulas AS "Progresso"
FROM "ESTUDOS/EM ANDAMENTO"
WHERE file.name != ".DS_Store"
SORT file.name ASC
```

### 🟡 Próximos a iniciar

```dataview
TABLE WITHOUT ID
  file.link AS "Estudo",
  subtipo AS "Tipo",
  instrutor AS "Instrutor/Autor",
  categoria AS "Área"
FROM "ESTUDOS/A INICIAR"
WHERE file.name != ".DS_Store" AND file.folder = "ESTUDOS/A INICIAR"
SORT file.name ASC
LIMIT 5
```

---

## 📌 Regras de ouro

| Sistema | Limite | Critério para mover |
|---|---|---|
| Projetos EM ANDAMENTO | máx. 3 | Tem bloco de tempo esta semana? |
| Estudos EM ANDAMENTO | máx. 3 | Tem horário fixo na rotina? |
