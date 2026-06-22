---
name: "source-command-hoje"
description: "Cria ou abre a daily note de hoje com eventos reais do Google Calendar"
---

# source-command-hoje

Use this skill when the user asks to run the migrated source command `hoje`.

## Command Template

Execute o ritual de abertura do dia. Siga os passos na ordem.

**PASSO 1 — Data e tipo de dia**

Execute via bash:
```bash
date +"%Y-%m-%d|%u|%H:%M"
```

Com o resultado:
- `YYYY-MM-DD` → nome do arquivo e datas de navegação
- Número do dia (1=Seg ... 7=Dom) → tipo:
  - 1, 3, 5 (Seg/Qua/Sex) → **EXTERNO** (gravações, atendimentos, clientes)
  - 2, 4, 6 (Ter/Qui/Sáb) → **AGÊNCIA** (edição, planejamento, produção)
  - 7 (Dom) → **PLANEJAMENTO**
- Calcule ONTEM: `date -v-1d +"%Y-%m-%d"`
- Calcule AMANHÃ: `date -v+1d +"%Y-%m-%d"`

**PASSO 2 — Eventos do Google Calendar de hoje**

Leia primeiro `[F2] memory/databases/regras-classificacao-agenda.md` para ter os ícones de cada frente.

Use `mcp__claude_ai_Google_Calendar__list_events`:
- `startTime`: YYYY-MM-DDT00:00:00-03:00 (data de hoje)
- `endTime`: YYYY-MM-DDT23:59:59-03:00
- `orderBy`: startTime
- `timeZone`: America/Maceio

Para cada evento retornado, extraia e formate:
- Ícone de frente (conforme regras)
- Horário início–fim
- Título
- Local (se houver, prefixe com 📍)
- Link de reunião (se houver na descrição ou htmlLink, prefixe com 🔗 e encurte ao domínio)

Eventos recorrentes da rotina base (Bloco 1: Fundação Pessoal, Ir ao Culto) → exiba compacto (só hora + nome, sem detalhes).

Se não houver nada além da rotina: escreva `*(agenda livre — apenas rotina fixa)*`

**PASSO 3 — Cruzamentos contextuais**

Execute via bash para buscar aniversariantes de hoje:
```bash
TODAY_MMDD=$(date +"%m-%d")
grep -rl "${TODAY_MMDD}$" "[F2] memory/databases/aniversariantes/" 2>/dev/null
```
Para cada arquivo encontrado, leia `nome` e `cargo`.

Para datas sazonais dos próximos 3 dias:
```bash
for i in 0 1 2 3; do date -v+${i}d +"%Y-%m-%d"; done
```
Grep cada data em `[F2] memory/databases/datas-sazonais/` e extraia `descricao` e `frente`.

**PASSO 4 — Verifique se a daily já existe**

Caminho: `[F1] 3-Daily/YYYY-MM-DD.md`

**PASSO 5a — Se NÃO existir, crie com este conteúdo:**

(Substitua todos os placeholders com valores reais antes de escrever)

```
---
tipo: daily
data: YYYY-MM-DD
gerado-por: Codex
comando: /hoje
---

# [Dia-da-Semana], [DD/MM/YYYY]

← [[YYYY-MM-DD_ONTEM]] | [[YYYY-MM-DD_AMANHA]] →

---

## 🎯 Foco do dia — [TIPO]

1. [ ] 
2. [ ] 
3. [ ] 

---

## 📅 Agenda

[LISTA DE EVENTOS — uma por linha, com ícone e horário]
[🎂 Aniversário: Nome (cargo) — se houver]
[📌 Data sazonal: Nome — X dias para produção — se houver nos próximos 3 dias]

---

## ✅ Tarefas pendentes

```dataview
TASK
FROM ""
WHERE !completed AND contains(tags, "tarefa")
SORT file.mtime DESC
```

---

## 📝 Captura



---

## 🌙 Revisão (17h–18h)

**O que funcionou:**

**O que não avancei e por quê:**

**Para amanhã:**
```

**PASSO 5b — Se JÁ existir:**
Leia e exiba o conteúdo atual. Informe: "Daily de hoje já existe." Pergunte se quer editar algum bloco específico.

**PASSO 6 — Registre o log**

Crie `[F2] memory/logs/comandos/YYYY-MM-DD-hoje.md`:
```
---
comando: /hoje
data: YYYY-MM-DD
resultado: criada | existia
eventos-calendar: N
---
Daily de [TIPO]. N eventos na agenda.
```

Confirme com uma linha: "Daily de **[Dia-da-Semana]** pronta — [N] evento(s) na agenda."
