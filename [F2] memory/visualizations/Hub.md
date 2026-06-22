---
tipo: visualizacao
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
ultimo-update: 2026-05-16
---

# Hub Central — MAPA OBSIDIAN

> `=dateformat(date(today), "EEEE, dd 'de' MMMM 'de' yyyy")`

---

## ⚡ Sistema Operacional Pessoal

> [[../context/rotina|Rotina-Diretor]] · [[../databases/matriz-tarefas|Matriz dos 5 Destinos]] · [[../projects/plano-30-dias-diretor|Plano 30 dias]] · [[../_MAP-skills|Mapa de Skills]]

| Princípio | Detalhe |
|---|---|
| Bloco Elite | 07:40–11:30 — pensar, criar, decidir |
| Bloco Tático | 13:00–18:00 — mover, captar, editar |
| Ancoragem | 18:00+ — família, descanso (inegociável) |
| Teto total | 20h/sem (SMS 15h · SINDSS 1h30 · Câmara 3h30) |
| Valor da hora | R$ 96 — toda hora institucional extra = R$ 96 perdidos |

---

## 🕐 Agora

> Bloco atual baseado no horário local. Para visão em tempo real → `/cockpit`

| Hora | Bloco | O que fazer |
|---|---|---|
| 06:00–07:40 | 🌅 Despertar | Oração, família, transição |
| 07:40–11:30 | 🟦 **Elite** | Pensar, criar, decidir — Lógika em primeiro |
| 10:00–11:30 (terça) | 🔵 SINDSS | Dentro do Elite — teto 1h30 |
| 11:30–13:00 | 🍽️ Almoço | Pausa sem pressa |
| 13:00–18:00 | 🟥 **Tático** | Mover, captar, editar, campo |
| 16:00–19:30 (sexta) | 🏛️ Câmara | Invade ancoragem — aplicar Zero-Sum |
| 18:00–21:00 | 🌙 **Ancoragem** | Família, descanso — celular virado |
| 21:00–06:00 | 😴 Sono | 7h mínimas — não negociável |

---

## 🎯 Top 3 hoje

> Preencher na daily de hoje via `/hoje` ou `/prioridades`

- [ ] *(via Notion Cockpit Diretor ou daily note)*
- [ ]
- [ ]

---

## 🚀 Cockpit completo

> Visão detalhada do dia: blocos, agenda, pendências, horas institucionais.

- **Abrir:** `/cockpit` — gera e abre `cockpit.html` no browser
- **Notion:** [🚀 Cockpit Diretor](https://www.notion.so/e6d0b774ebe04761a61b1a30e16db091)
- **Semana atual do plano:** Semana 1 (16–22/05) — Raio-X da rotina real

---

## 📥 Inbox

> Captura recente aguardando processamento.

```dataview
TABLE fonte AS "Fonte", frente AS "Frente", data AS "Data"
FROM "[F2] memory/inbox-externa"
WHERE revisado = false
SORT data DESC
LIMIT 5
```

> Processar inbox: `/inbox` (Gmail) · `/drive-recente` (Drive) · `[F0] 0-Inbox/` (vault)

---

## 💼 Esta semana — Horas Institucionais

> Meta: máximo 20h/sem. Toda hora excedente = R$ 96 perdidos da Lógika.

| Cliente | Teto | Horas esta semana | Status |
|---|---|---|---|
| SMS | 15h | — | — |
| SINDSS | 1h30 | — | — |
| Câmara | 3h30 | — | — |
| **Total** | **20h** | **—** | — |

> Registrar no [🚀 Cockpit Diretor](https://www.notion.so/e6d0b774ebe04761a61b1a30e16db091) após cada bloco.

---

## 📊 Status dos Sistemas

### Matriz dos 5 Destinos
- **Total:** 37 tarefas categorizadas — [[../databases/matriz-tarefas|ver matriz]]
- **Implementado:** 3/37 (8%)
- **Próxima alavanca:** Semana 2 (23/05) — criar os 9 SISTEMAS

### Plano 30 dias
- **Semana atual:** 1 — Raio-X (16–22/05 · despertar 06h)
- **Próxima:** Semana 2 (23/05 · despertar 05h30 · criar sistemas)
- **Encerramento:** 2026-06-15 · auto-avaliação KPI

### Projetos ativos
- [[../projects/plano-30-dias-diretor|Plano 30d]] — 🔨 Semana 1 em andamento
- [[../projects/regra-1-3-patrimonio|Regra 1/3]] — 🔨 Sessão 1 (diagnóstico) pendente

---

## 🔴 Pendências Críticas

> Ver completo: [[../context/pendencias|Pendências]]

```dataview
LIST
FROM "[F2] memory/context/pendencias.md"
WHERE contains(file.content, "🔴")
LIMIT 5
```

---

## 📅 Próximos Deadlines (14 dias)

> Ver completo: [[../context/deadlines|Deadlines]]

```dataview
TABLE data AS "Data", descricao AS "Descrição", frente AS "Frente"
FROM "[F2] memory/databases/datas-sazonais"
WHERE data >= date(today) AND data <= date(today) + dur(14 days)
SORT data ASC
LIMIT 8
```

---

## ⚙️ Skills disponíveis

> Mapa completo: [[../_MAP-skills|_MAP-skills]] — quando usar cada skill

| Situação rápida | O que usar |
|---|---|
| Iniciar sessão | `cerebro` |
| Planejar dia | `rotina` ou `/prioridades` |
| Fechar sessão | `salve` |
| Gerar cockpit | `/cockpit` |
| Post por frente | `/post-saude` · `/post-camara` · `/post-sindss` · `/post-logika` |
| Captura rápida | `/captura` ou `/ideia` |
| Ver agenda | `/agenda` |

---

## 🧠 Skills do Vault

| Skill | Como invocar | O que faz |
|---|---|---|
| `cerebro` | Digite "cerebro" | Carrega contexto completo antes de operar |
| `rotina` | Digite "rotina" | Top 3 do dia + tracker por frente |
| `salve` | Digite "salve" | git commit + push + log + pendências |
| `reindex` | Digite "reindex" | Reindexação ao trocar de LLM |

---

## Frentes Ativas

> [!info]+ Lógika Creative
> **Empresa / Audiovisual — Prioridade máxima no bloco Elite**
> - Pasta: `[F1] 5-Frentes/Logika-Creative/`
> - Canvas: [[logika-creative.canvas]]
> - Briefing: [[../agents/logika|Briefing Lógika]]

> [!success]+ Saúde São Sebastião
> **Secretaria Municipal de Saúde — Teto: 15h/sem**
> - Pasta: `[F1] 5-Frentes/Saude-Sao-Sebastiao/`
> - Briefing: [[../agents/saude|Briefing Saúde]]

> [!warning]+ Câmara Municipal
> **Vereadores e plenário — Teto: 3h30/sem (sexta 16–19h30)**
> - Pasta: `[F1] 5-Frentes/Camara-Municipal/`
> - Canvas: [[camara-municipal.canvas]]
> - Briefing: [[../agents/camara|Briefing Câmara]]

> [!danger]+ SINDSS
> **Sindicato dos Servidores — Teto: 1h30/sem (terça 10–11h30)**
> - Pasta: `[F1] 5-Frentes/SINDSS/`
> - Briefing: [[../agents/sindss|Briefing SINDSS]]

> [!tip]+ Outros Vereadores
> **Josi · Vando · Manoel**
> - Pasta: `[F1] 5-Frentes/Outros-Vereadores/`
> - Briefings: [[../agents/vereadores/index|Vereadores]]

> [!tip]+ ALÉM DA FOTO
> **Canal documental — em construção**
> - Pasta: `[F1] 5-Frentes/Alem-da-Foto/`
> - Briefing: [[../agents/alem-da-foto|Briefing Além da Foto]]

> [!example]+ Lives de Louvor e Reflexão
> **Projeto gospel — em planejamento**
> - Pasta: `[F1] 5-Frentes/Lives-Louvor-Reflexao/`
> - Briefing: [[../agents/lives|Briefing Lives]]

> [!abstract]- Rogério Rocha *(inativo)*
> Cliente inativo — pode retornar.
> - Pasta: `[F1] 5-Frentes/Inativos/Rogerio-Rocha/`
> - Canvas: [[rogerio-rocha.canvas]]

---

## 📅 Agenda

> [!tip] Eventos do Google Calendar
> - `/hoje` → daily com eventos do dia
> - `/agenda 7` → semana completa com frente
> - `/agenda 14` → quinzena

```dataview
TABLE data AS "Data", tipo AS "Tipo"
FROM "[F1] 3-Daily"
WHERE data = date(today)
LIMIT 1
```

---

## Pipeline de Produção

```dataview
TABLE frente, status AS "Status"
FROM #producao/ideia OR #producao/roteiro OR #producao/captura OR #producao/edicao OR #producao/revisao
SORT frente ASC
```

### Publicados recentemente

```dataview
TABLE frente, data-publicacao AS "Publicado em"
FROM #producao/publicado
SORT data-publicacao DESC
LIMIT 10
```

---

## Drafts Aguardando Revisão

```dataview
TABLE frente, data-criacao AS "Criado em"
FROM "[F2] memory/outputs"
WHERE revisado = false
SORT data-criacao DESC
```

---

## Próximas Datas Sazonais (30 dias)

```dataview
TABLE data AS "Data", descricao AS "Descrição", frente AS "Frente"
FROM "[F2] memory/databases/datas-sazonais"
WHERE data >= date(today)
SORT data ASC
LIMIT 15
```

---

## Comandos Disponíveis

> Ver cheat sheet completo: [[comandos]]

| Uso diário | Por frente | Estratégicos | Calendário |
|---|---|---|---|
| `/hoje` | `/legenda` | `/planejar-semana` | `/agenda` |
| `/captura` | `/post-saude` | `/manutencao` | `/agendar` |
| `/cockpit` | `/post-camara` | `/sazonal` | `/bloquear-rotina` |
| `/revisar` | `/post-sindss` | `/aniversariante` | `/sincronizar-sazonais` |
| `/ideia` | `/post-logika` | `/busca` | `/conflitos-agenda` |
| `/prioridades` | `/post-rogerio` | `/conecta` | `/agenda-frente` |
| | `/roteiro-rogerio` | `/financeiro` | |

**📥 Fontes Externas**

| Gmail | Drive | Importação manual |
|---|---|---|
| `/inbox` | `/drive-recente` | `/whats-importar` |
| `/inbox-cliente` | `/drive-buscar` | `/audio-importar` |
| `/agenda-email` | `/drive-arquivo` | |

---

## Acesso Rápido

| Tipo | Arquivo |
|---|---|
| **Rotina-Diretor** | [[../context/rotina\|Rotina-Diretor]] |
| **Matriz 5 Destinos** | [[../databases/matriz-tarefas\|Matriz de Tarefas]] |
| **Plano 30 dias** | [[../projects/plano-30-dias-diretor\|Plano 30 dias]] |
| **Regra 1/3** | [[../projects/regra-1-3-patrimonio\|Patrimônio]] |
| **Mapa de Skills** | [[../_MAP-skills\|_MAP-skills]] |
| **Cockpit Notion** | [🚀 Cockpit Diretor](https://www.notion.so/e6d0b774ebe04761a61b1a30e16db091) |
| **Contexto de Negócio** | [[../context/business-context\|Business Context]] |
| **Pendências** | [[../context/pendencias\|Pendências]] |
| **Deadlines** | [[../context/deadlines\|Deadlines]] |
| **Pessoas** | [[../context/people\|People]] |
| **Decisões (maio 2026)** | [[../context/decisoes/2026-05\|Decisões 05/2026]] |
| **Canvas Geral** | [[Vault-Map.canvas]] |
| **Canvas Lógika** | [[logika-creative.canvas]] |
| **Canvas Câmara** | [[camara-municipal.canvas]] |
| **Comandos disponíveis** | [[comandos]] |
| **Subagents disponíveis** | [[subagents]] |
| **PROPAGATION.md** | [[../../PROPAGATION\|Protocolo de Propagação]] |
