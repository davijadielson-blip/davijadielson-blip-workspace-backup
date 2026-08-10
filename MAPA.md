---
tema: mapa geral do workspace
conteudo: estrutura completa de pastas, arquivos, salvamento pertinente e rotas de cada tipo de informação no Cofre
nicho: ecossistema agêntico Lôh/Jadielson
setor: audiovisual, comunicação, marketing digital, gestão pessoal
cliente: Jadielson Davi
tipo: mapa
prioridade: máxima
atualizado_em: 2026-08-10
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
2. **Fallback direto obrigatório** — se `memory_search` falhar, use `read`, `find`, `grep`, este MAPA.md, `AGENTS.md`, `MEMORY.md`, `memory/*.md`, `00-central/` a `90-arquivo/`, `scripts/`, `skills/` e demais áreas relevantes.
3. **Tavily/Pesquisador** — só depois, se precisar de dado externo/atualizado.
4. **Outras fontes** — só se Cofre + Tavily não resolverem.
5. **Rodapé de fonte** em toda resposta analítica/operacional.
6. **Registre com governança**: proponha o registro do que for pertinente para continuidade e grave com autorização explícita, rotina canônica aprovada ou aprovação leve de Jadielson.

> Falha em consultar o Cofre é falha operacional. Proponha registro da lição em arquivo canônico e só grave com autorização explícita.

### 💾 Salvamento pertinente

Reação **👍** ou **❤️**, figurinha coerente de aprovação/uso, ou respostas como **"obrigado"**, **"obg"**, **"muito bom"**, **"vou usar"** e equivalentes autorizam salvar no Cofre o que for pertinente para continuidade, sem pedir nova confirmação.

Somente Markdown (`.md`) vai para o Cofre. Demais arquivos vão para o Drive ou armazenamento externo aprovado, com referência em `.md` quando necessário.

---

## 🏗️ Estrutura oficial do Cofre

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
├── 00-central/              ← Governança, regras, decisões, mapas, pendências, notas centrais
├── 10-pessoal/              ← Vida pessoal, rotina, saúde, família, inbox e tarefas pessoais
├── 20-profissional/         ← LÓGIKA, carreira, operação profissional e referências internas
├── 30-estudos/              ← Cursos, livros, métodos, planos de estudo e materiais de aprendizagem
├── 40-projetos/             ← Projetos pessoais, profissionais, autorais, produtos e ideias
├── 50-clientes/             ← Clientes e frentes institucionais: Saúde, Câmara, SINDSS, vereadores etc.
├── 60-processos/            ← Checklists, rotinas, relatórios, templates e processos operacionais
├── 70-agentes/              ← Agentes, runtime, squads, escopos e protocolos
├── 80-handoffs/             ← Passagens formais de contexto entre sessões/agentes
├── 90-arquivo/              ← Legado, backups, duplicidades, quarentena e estrutura antiga
├── memory/                  ← Memória operacional ativa da IA, sessões, outputs e inbox externa
├── media/                   ← Mídias recebidas ou referenciadas
├── scripts/                 ← Automações executáveis
└── skills/                  ← Skills ativas do workspace
```

### Compatibilidade com F0/F1/F2/F3

Os termos `[F0]`, `[F1]`, `[F2]` e `[F3]` são **legado técnico e histórico**. Eles podem aparecer em memórias antigas, scripts, relatórios, registros de migração e referências de auditoria, mas **não orientam mais o roteamento atual do Cofre**.

Regra prática:
- Para salvar ou procurar conteúdo novo, use a estrutura numerada de `00-central/` a `90-arquivo/`, mais `memory/`, `media/`, `scripts/` e `skills/`.
- Caminhos antigos só devem ser mantidos quando forem referência histórica ou compatibilidade temporária.
- Nada deve ser movido, renomeado ou consolidado sem antes checar dependências em agentes, skills, scripts, crons, runtimes e handoffs.
- A inbox física atual é `10-pessoal/inbox/`.
- A inbox operacional de fontes externas continua em `memory/inbox-externa/`.

### Autonomia Operacional da IA

A IA autorizada pode ler, criar, editar, reorganizar, consolidar, mover e manter arquivos do Cofre quando estiver executando pedidos, preservando contexto, melhorando organização ou garantindo continuidade.

Jadielson permanece como autoridade final sobre sentido, prioridade, publicação, envio externo, decisões sensíveis e exclusão definitiva. A autonomia da IA é operacional; a autoridade final é humana.

---

## 🧭 Onde encontrar cada tipo de informação

| Tipo de informação | Onde buscar | Onde salvar |
|---|---|---|
| **Lei maior do ecossistema** | `CONSTITUICAO.md` | — |
| **Identidade do agente (Lôh)** | `SOUL.md`, `IDENTITY.md` | `SOUL.md` |
| **Perfil de Jadielson** | `USER.md` | `USER.md` |
| **Regras de operação** | `AGENTS.md` | `AGENTS.md` |
| **Decisões estruturais do Cofre** | `00-central/decisoes.md`, `MEMORY.md`, `memory/context/decisoes/` | `00-central/decisoes.md` ou `memory/context/decisoes/` |
| **Memória diária legada** | `memory/YYYY-MM-DD.md` | Consultar se existir; não criar automaticamente |
| **Briefing diário** | `HEARTBEAT.md`, `memory/daily-briefs/` | `memory/daily-briefs/` |
| **Projetos em andamento** | `40-projetos/`, `memory/projects/` | `40-projetos/` |
| **Frentes de trabalho ativas** | `20-profissional/`, `50-clientes/`, `40-projetos/` | área correspondente |
| **Contexto operacional de frente** | `memory/agents/[frente].md` | `memory/agents/[frente].md` |
| **Legendas, roteiros, briefings** | `memory/outputs/` | `memory/outputs/` |
| **Log de sessão** | `memory/sessions/YYYY-MM-DD.md` | `memory/sessions/YYYY-MM-DD.md` |
| **Checklists operacionais** | `60-processos/checklists/` | `60-processos/checklists/` |
| **Captura bruta pessoal (inbox)** | `10-pessoal/inbox/` | `10-pessoal/inbox/` |
| **Notas centrais/permanentes** | `00-central/` | `00-central/` |
| **Skills (workflows)** | `skills/` | `skills/` |
| **Scripts de automação** | `scripts/` | `scripts/` |
| **Templates** | `60-processos/templates/` | `60-processos/templates/` |
| **Dados do Google Drive** | `gog drive` (CLI, não Zapier) | Google Drive |
| **Arquivos não Markdown** | Drive/origem externa + referência `.md` | Google Drive |
| **Leads/CRM** | Notion (link em MEMORY.md) | Notion |
| **Calendário Google** | `gog calendar` (CLI, não Zapier) | Google Calendar |
| **E-mails (Gmail)** | `gog gmail` (CLI, só leitura) | Gmail |

---

## 📂 Detalhamento das pastas

### `00-central/` — Governança e notas centrais
- Regras, decisões, mapa, glossário, pendências transversais, diagnósticos estruturais e notas centrais.
- É a primeira área para entender decisões oficiais sobre o Cofre.

### `10-pessoal/` — Vida pessoal e inbox
- Rotina, saúde, família, finanças pessoais, tarefas e captura pessoal.
- Inbox física atual: `10-pessoal/inbox/`.
- Respeitar parede d'água: contexto pessoal só entra quando a demanda exigir.

### `20-profissional/` — LÓGIKA e operação profissional
- Referências profissionais, LÓGIKA, estratégia, produção e operação interna.

### `30-estudos/` — Estudos
- Cursos, livros, fichamentos, métodos, planos de estudo e recursos educacionais.

### `40-projetos/` — Projetos
- Projetos pessoais, profissionais, autorais, produtos, trabalho e ideias com começo, meio e fim.

### `50-clientes/` — Clientes e frentes institucionais
- Saúde São Sebastião, Câmara Municipal, SINDSS, vereadores e outros clientes.
- Conteúdo sensível institucional exige validação humana antes de publicar.

### `60-processos/` — Processos
- Checklists, rotinas, relatórios, templates, playbooks e documentação operacional.

### `70-agentes/` — Agentes
- Arquitetura, prompts, runtime, squads, protocolos e mapas de agentes.

### `80-handoffs/` — Handoffs
- Passagens formais de contexto para continuidade entre sessões e agentes.

### `90-arquivo/` — Legado e quarentena
- Legado, backups, duplicidades, estrutura antiga, quarentena e revisão.
- Usar para preservação e reversibilidade; nunca como lixeira definitiva.
- Subpastas de revisão usadas na etapa 2:
  - `90-arquivo/10-legado-f0-f1-f2-f3/` — reservado para legado explícito dos fluxos antigos quando necessário.
  - `90-arquivo/20-duplicidades/` — duplicidades e reaparecimentos já identificados.
  - `90-arquivo/30-regras-obsoletas/` — planos, inventários e regras superadas que não devem orientar agentes.
  - `90-arquivo/40-revisao-humana/` — itens preservados fora da rota ativa que precisam de decisão humana.

### `memory/` — Memória operacional ativa
```
memory/
├── YYYY-MM-DD.md           ← Diários legados (consultar se existirem; não criar automaticamente)
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
