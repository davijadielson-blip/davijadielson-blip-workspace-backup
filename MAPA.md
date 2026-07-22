---
tema: mapa geral do workspace
conteudo: estrutura completa de pastas, arquivos e rotas de cada tipo de informação no Cofre
nicho: ecossistema agêntico Lôh/Jadielson
setor: audiovisual, comunicação, marketing digital, gestão pessoal
cliente: Jadielson Davi
tipo: mapa
prioridade: máxima
atualizado_em: 2026-07-22
usar_quando: antes de qualquer consulta, decisão de salvamento, roteamento ou busca no Cofre
nao_usar_quando: informação urgente que exige fonte externa atualizada (Tavily primeiro)
---

# MAPA — Cofre de Jadielson Davi

> **Cofre** = `/data/.openclaw/workspace/`  
> Fonte de verdade primária do ecossistema.  
> Backup no GitHub (`davijadielson-blip/segundo-cerebro-jadielson`) — consultar só emergencial.

---

## 📍 Regra LOCAL-FIRST (obrigatória para todo agente)

Antes de qualquer resposta contextual, operacional, estratégica ou informacional:

1. **Consulte o Cofre primeiro** — leia os arquivos relevantes.
2. **Fallback direto obrigatório** — se `memory_search` falhar, use `read`, `find`, `grep`, este MAPA.md, `AGENTS.md`, `MEMORY.md`, `memory/*.md`, `[F1]`/`[F2]`/`[F3]` relevantes.
3. **Tavily/Pesquisador** — só depois, se precisar de dado externo/atualizado.
4. **Outras fontes** — só se Cofre + Tavily não resolverem.
5. **Rodapé de fonte** em toda resposta analítica/operacional.
6. **Salve no Cofre** tudo que for pertinente para continuidade.

> Falha em consultar o Cofre é falha operacional. Registre em `memory/lessons.md`.

---

## 🏗️ Estrutura do Cofre

```
/data/.openclaw/workspace/
│
├── CONSTITUICAO.md          ← Lei maior do ecossistema (ler antes de qualquer ação estratégica)
├── SOUL.md                  ← Quem sou (Lôh) — identidade, tom, poderes, método
├── IDENTITY.md              ← Ficha técnica da Lôh (modelo, agente ID, reporte)
├── USER.md                  ← Quem é Jadielson — perfil, preferências, contexto pessoal
├── AGENTS.md                ← Regras de operação para todos os agentes (ler toda sessão)
├── MEMORY.md                ← Memória de longo prazo — decisões, protocolos, histórico
├── HEARTBEAT.md             ← Proatividade segura, briefing diário
├── MAPA.md                  ← ESTE ARQUIVO — mapa de navegação
├── README.md                ← Starter Kit OpenClaw (material do curso, não operacional)
│
├── [F0] 0-Inbox/            ← Captura bruta — só Jadielson mexe, IA só lê
├── [F1] 1-Permanentes/      ← Notas autorais de Jadielson (IA só lê, nunca edita)
├── [F2] memory/             ← Cérebro da IA (autonomia total: cria, edita, deleta)
├── [F3] PROJETOS/           ← Projetos ativos com estrutura central
│
├── checklists/              ← Checklists operacionais (veja checklists/local-first.md)
├── skills/                  ← Workflows complexos portáveis
├── scripts/                 ← Scripts bash de automação
└── templates/               ← Moldes canônicos de arquivos
```

---

## 🧭 Onde encontrar cada tipo de informação

| Tipo de informação | Onde buscar | Onde salvar |
|---|---|---|
| **Lei maior do ecossistema** | `CONSTITUICAO.md` | — |
| **Identidade do agente (Lôh)** | `SOUL.md`, `IDENTITY.md` | `SOUL.md` |
| **Perfil de Jadielson** | `USER.md` | `USER.md` |
| **Regras de operação** | `AGENTS.md` | `AGENTS.md` |
| **Decisões arquiteturais** | `MEMORY.md`, `memory/context/decisoes/` | `memory/context/decisoes/` |
| **Memória diária** | `memory/YYYY-MM-DD.md` | `memory/YYYY-MM-DD.md` |
| **Briefing diário** | `HEARTBEAT.md`, `memory/daily-briefs/` | `memory/daily-briefs/` |
| **Projetos em andamento** | `[F3] PROJETOS/`, `memory/projects/` | `[F3] PROJETOS/[status]/` |
| **Frentes de trabalho ativas** | `[F1] 5-Frentes/[frente]/` | `[F1] 5-Frentes/[frente]/` |
| **Contexto operacional de frente** | `memory/agents/[frente].md` | `memory/agents/[frente].md` |
| **Legendas, roteiros, briefings** | `memory/outputs/` | `memory/outputs/` |
| **Log de sessão** | `memory/sessions/YYYY-MM-DD.md` | `memory/sessions/YYYY-MM-DD.md` |
| **Checklists operacionais** | `checklists/` | `checklists/` |
| **Captura bruta (inbox)** | `[F0] 0-Inbox/` | `[F0] 0-Inbox/` |
| **Notas autorais de Jadielson** | `[F1] 1-Permanentes/` | Só Jadielson escreve |
| **Skills (workflows)** | `skills/` | `skills/` |
| **Scripts de automação** | `scripts/` | `scripts/` |
| **Templates** | `templates/` | `templates/` |
| **Dados do Google Drive** | `gog drive` (CLI, não Zapier) | Google Drive |
| **Leads/CRM** | Notion (link em MEMORY.md) | Notion |
| **Calendário Google** | `gog calendar` (CLI, não Zapier) | Google Calendar |
| **E-mails (Gmail)** | `gog gmail` (CLI, só leitura) | Gmail |

---

## 📂 Detalhamento das pastas

### `[F0] 0-Inbox/` — Captura bruta
- Tudo que chega sem filtro: notas rápidas, ideias soltas, links, prints
- Só Jadielson mexe. Sistema não edita.
- Quando processado, vai para o fluxo correto.

### `[F1] 1-Permanentes/` — Notas autorais de Jadielson
- Notas atômicas, reflexões processadas, conceitos que resistem ao tempo
- **IA só lê. Nunca edita.**
- Subpastas: `2-Literatura/`, `3-Daily/`, `4-Pessoal/`, `5-Frentes/`, `PROJETOS/`, `TAREFAS/`, `ESTUDOS/`

### `[F1] 5-Frentes/` — Frentes de trabalho ativas
| Pasta | Frente | Status |
|---|---|---|
| `Logika-Creative/` | Lógika Creative (agência audiovisual) | 🟢 Ativa |
| `Camara-Municipal/` | Câmara Municipal de São Sebastião | 🟢 Ativa |
| `SINDSS/` | Sindicato dos Servidores | 🟢 Ativa |
| `Alem-da-Foto/` | Canal documental | 🟡 Standby |
| `Lives-Louvor-Reflexao/` | Lives gospel | 🟡 Standby |
| `Outros-Vereadores/` | Josi, Vando, Manoel | 🟡 Standby |
| `Projetos/` | Projetos diversos | 🟢 Ativa |

### `[F2] memory/` — Cérebro da IA (autonomia total)
```
memory/
├── YYYY-MM-DD.md           ← Diários (criar se não existir)
├── context/                ← Estado atual: pendências, deadlines, negócio
│   └── decisoes/           ← Decisões arquiteturais registradas
├── sessions/               ← Log diário de sessões + outputs de crons
├── outputs/                ← Legendas, roteiros, briefings, drafts
├── agents/                 ← Briefings operacionais por frente
│   └── central-pessoal/    ← Prompts dos agentes pessoais
├── databases/              ← Calendários, aniversariantes, regras
├── templates/              ← Modelos reutilizáveis
├── visualizations/         ← Hub, Canvas, dashboards, diagramas
├── projects/               ← Pesquisas, projetos rastreados, planos
├── daily-briefs/           ← Briefings diários
├── inbox-externa/          ← E-mail, Drive, WhatsApp, áudio importados
├── backup-log.md           ← Log de backups
└── lessons.md              ← Lições aprendidas (falhas operacionais)
```

### `[F3] PROJETOS/` — Projetos ativos (estrutura central)
- `EM ANDAMENTO/` — projetos em execução
- `EM PAUSA/` — projetos parados
- `CONCLUÍDOS/` — projetos finalizados

### `checklists/` — Checklists operacionais
- `local-first.md` — Protocolo LOCAL-FIRST (consulte antes de responder)

---

## 🔗 Arquivos de referência rápida

| Para saber | Leia |
|---|---|
| Quem sou como agente | `SOUL.md` + `IDENTITY.md` |
| Quem é Jadielson | `USER.md` |
| Como operar | `AGENTS.md` (sessão completa) |
| Regras imutáveis | `CONSTITUICAO.md` |
| Decisões e memória consolidada | `MEMORY.md` |
| Briefing diário e proatividade | `HEARTBEAT.md` |
| Localização de cada info | `MAPA.md` (este arquivo) |
| Lições de falhas passadas | `memory/lessons.md` |

---

*Criado em: 2026-07-22 · Protocolo LOCAL-FIRST ativado.*