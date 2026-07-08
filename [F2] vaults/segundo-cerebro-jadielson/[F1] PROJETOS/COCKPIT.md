---
tipo: cockpit
subtipo: projetos
---

# 🎯 COCKPIT DE PROJETOS

> Abra este arquivo todo dia. Escolha **1 projeto** para avançar. Execute a ⚡ próxima ação. Feche.
> As tabelas atualizam sozinhas — mover o arquivo de pasta = status refletido aqui na hora.

---

## ✅ Tarefas do Dia

> Capture pelo Telegram: `/tpd <tarefa>` (sem projeto) · `/tpg <tarefa>` (avança projeto)

### 🔴 Prevenção de Dor — evitam dano, não fazem parte de projetos

```dataview
TABLE WITHOUT ID
  file.link AS "Tarefa",
  frente AS "Frente",
  prazo AS "Prazo"
FROM "TAREFAS/TPD"
WHERE tipo = "tarefa-tpd" AND status = "pendente"
SORT prazo ASC
```

### 🟢 Produção de Ganho — etapas de projetos, avançam a vida

```dataview
TABLE WITHOUT ID
  file.link AS "Tarefa",
  projeto AS "Projeto",
  prazo AS "Prazo"
FROM "TAREFAS/TPG"
WHERE tipo = "tarefa-tpg" AND status = "pendente"
SORT prazo ASC
```

---

## Como mover um projeto de status

Arraste o arquivo para a pasta correta no Obsidian:

`IDEIAS NOVAS` → `A INICIAR` → `EM ANDAMENTO` → `PAUSADO` ou `CONCLUÍDO` ou `DESCARTADO`

> **Regra de ouro: máximo 3 projetos em EM ANDAMENTO ao mesmo tempo.**
> Antes de mover para EM ANDAMENTO, confirme que tem bloco de tempo na agenda para ele esta semana.

---

## 🟢 EM ANDAMENTO

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

---

## 🟡 A INICIAR

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente",
  fase-atual AS "Fase"
FROM "PROJETOS/A INICIAR"
WHERE tipo = "projeto"
SORT frente ASC
```

---

## 🗂️ Por Destino da Matriz

> Use para decidir **o que priorizar esta semana**. Referência: [[[F2] memory/databases/matriz-tarefas|Matriz dos 5 Destinos]].

### 🎯 FOCO — Só você, bloco Elite

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/A INICIAR" OR "PROJETOS/EM ANDAMENTO"
WHERE tipo = "projeto" AND destino-matriz = "FOCO"
SORT frente ASC
```

### 📦 BLOCO — Janela fixa, agrupa e despacha

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/A INICIAR" OR "PROJETOS/EM ANDAMENTO"
WHERE tipo = "projeto" AND destino-matriz = "BLOCO"
SORT frente ASC
```

### ⚙️ SISTEMA — Vira processo antes de executar

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/A INICIAR" OR "PROJETOS/EM ANDAMENTO"
WHERE tipo = "projeto" AND destino-matriz = "SISTEMA"
SORT frente ASC
```

### 🤝 DELEGAR — Sai da sua mão

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/A INICIAR" OR "PROJETOS/EM ANDAMENTO"
WHERE tipo = "projeto" AND destino-matriz = "DELEGAR"
SORT frente ASC
```

---

## 🔵 PAUSADO

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente",
  proximo-review AS "Revisar em"
FROM "PROJETOS/PAUSADO"
WHERE tipo = "projeto"
SORT file.name ASC
```

---

## ✅ CONCLUÍDO

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/CONCLUÍDO"
WHERE tipo = "projeto"
SORT file.mtime DESC
```

---

## ❌ DESCARTADO

```dataview
TABLE WITHOUT ID
  file.link AS "Projeto",
  frente AS "Frente"
FROM "PROJETOS/DESCARTADO"
WHERE tipo = "projeto"
SORT file.mtime DESC
```

---

## 💡 IDEIAS NOVAS — triagem pendente

> Capturadas pelo Telegram. Decida: arrasta para **A INICIAR** (com card estratégico) ou para **DESCARTADO**.

```dataview
TABLE WITHOUT ID
  file.link AS "Ideia",
  frente AS "Frente",
  capturado-em AS "Capturado"
FROM "PROJETOS/IDEIAS NOVAS"
WHERE tipo = "ideia-projeto"
SORT capturado-em DESC
```

---

## 📌 Frentes permanentes

> Não são projetos — são **frentes com conteúdo recorrente**. Acesse pelo vault quando precisar.

| Frente | Pasta |
|---|---|
| Lógika Creative | `[F1] 5-Frentes/Logika-Creative/` |
| Secretaria de Saúde | `[F1] 5-Frentes/Saude-Sao-Sebastiao/` |
| Câmara Municipal | `[F1] 5-Frentes/Camara-Municipal/` |
| SINDSS | `[F1] 5-Frentes/SINDSS/` |
| ALÉM DA FOTO | `[F1] 5-Frentes/Alem-da-Foto/` |
| Lives de Louvor | `[F1] 5-Frentes/Lives-Louvor-Reflexao/` |
