---
tipo: cockpit
subtipo: estudos
---

# 📚 COCKPIT DE ESTUDOS

> Abra este arquivo para escolher **1 estudo** para avançar hoje. Arraste o arquivo para a pasta correta para mudar o status — as tabelas atualizam sozinhas.
> **Regra de ouro: máximo 3 estudos em EM ANDAMENTO ao mesmo tempo.**

---

## Como mover um estudo de status

Arraste o arquivo (ou pasta) para a pasta correta no Obsidian:

`A INICIAR` → `EM ANDAMENTO` → `PAUSADO` ou `CONCLUÍDO` ou `DESCARTADO`

---

## 🟢 EM ANDAMENTO

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

---

## 🟡 A INICIAR

```dataview
TABLE WITHOUT ID
  file.link AS "Estudo",
  subtipo AS "Tipo",
  instrutor AS "Instrutor/Autor",
  categoria AS "Área"
FROM "ESTUDOS/A INICIAR"
WHERE file.name != ".DS_Store" AND file.folder = "ESTUDOS/A INICIAR"
SORT file.name ASC
```

---

## 🔵 PAUSADO

```dataview
TABLE WITHOUT ID
  file.link AS "Estudo",
  subtipo AS "Tipo",
  instrutor AS "Instrutor/Autor"
FROM "ESTUDOS/PAUSADO"
WHERE file.name != ".DS_Store" AND file.folder = "ESTUDOS/PAUSADO"
SORT file.name ASC
```

---

## ✅ CONCLUÍDO

```dataview
TABLE WITHOUT ID
  file.link AS "Estudo",
  subtipo AS "Tipo",
  instrutor AS "Instrutor/Autor"
FROM "ESTUDOS/CONCLUÍDO"
WHERE file.name != ".DS_Store"
SORT file.mtime DESC
```

---

## ❌ DESCARTADO

```dataview
TABLE WITHOUT ID
  file.link AS "Estudo",
  subtipo AS "Tipo"
FROM "ESTUDOS/DESCARTADO"
WHERE file.name != ".DS_Store"
SORT file.mtime DESC
```
