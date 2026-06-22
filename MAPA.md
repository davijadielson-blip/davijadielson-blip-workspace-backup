# MAPA — Workspace Lôh / Jadielson

> Fonte de verdade única. GitHub é backup.  
> Última reorganização: 2026-06-22

---

## Raiz

| Caminho | Função |
|---|---|
| `SOUL.md` | Minha identidade — sou Lôh, orquestradora Tier 0 |
| `AGENTS.md` | Manual de conduta e operação |
| `IDENTITY.md` | Ficha formal |
| `USER.md` | Quem é Jadielson Davi |
| `MEMORY.md` | Memória de longo prazo |
| `MAPA.md` | **Este arquivo** — mapa do workspace |
| `TOOLS.md` | Anotações de ferramentas |
| `HEARTBEAT.md` | Tarefas periódicas |
| `BOOTSTRAP.md` | Ritual de primeiro boot (se existir) |
| `scripts/reorganizar-workspace.sh` | Script de reorganização |

---

## Núcleo de Conteúdo (PARA)

| Caminho | O que é |
|---|---|
| `[F0] 0-Inbox/` | Captura bruta — o que chega sem filtro |
| `[F1] 1-Permanentes/` | Referências, templates, arquivos fixos |
| `[F1] 2-Literatura/` | Livros, cursos, materiais de estudo |
| `[F1] 3-Daily/` | Notas diárias, pendências rápidas |
| `[F1] 4-Pessoal/` | Vida pessoal de Jadielson (parede d'água) |
| `[F1] 5-Frentes/` | Clientes e frentes ativas/standby |
| `[F1] ESTUDOS/` | Cursos, aprendizados |
| `[F1] PROJETOS/` | Projetos ativos e passados |
| `[F1] TAREFAS/` | Tarefas avulsas |

---

## Segundo Cérebro (Inteligência dos Agentes)

| Caminho | O que é |
|---|---|
| `F2 memory/agents/` | Definições de agentes, prompts, personalidades |
| `F2 memory/context/` | Contextos estratégicos, calendários, decisões |
| `F2 memory/databases/` | Dados estruturados (JSON, mapeamentos) |
| `F2 memory/decisions/` | Decisões registradas |
| `F2 memory/inbox-externa/` | Capturas de fontes externas (áudio, transcrições) |
| `F2 memory/outputs/` | **Entregáveis, relatórios, drafts.** Saída de agentes |
| `F2 memory/projects/` | Memória de projetos (planos, pesquisas) |
| `F2 memory/sessions/` | Logs de sessões |
| `F2 memory/templates/` | **Templates canônicos** (arquivos raiz) |
| `F2 memory/visualizations/` | Diagramas, mapas visuais |
| `F2 memory/` (raiz) | Diários diários, MAPA, etc. |

---

## Motor (Scripts)

| Caminho | O que é |
|---|---|
| `scripts/` | Automacao geral |
| `scripts/cockpit/` | Painéis HTML (cockpit, estudos) |
| `scripts/cron-jobs/` | Configuração de crons |
| `scripts/health/` | Health checks e guards (Tavily, integrações) |
| `scripts/notion/` | Scripts Notion (incl. `configs/` com payloads JSON) |
| `scripts/patches/` | Patches de config |
| `scripts/setup/` | Scripts de setup |
| `scripts/state/` | Estado operacional |
| `scripts/sync/` | Sincronizadores (Notion → Calendar) |
| `scripts/cloud/` | Cloud scripts |
| `scripts/lib/` | Bibliotecas compartilhadas |

---

## Habilidades (Skills)

| Caminho | O que é |
|---|---|
| `skills/` | Módulos de habilidade dos agentes |
| `skills/planejamento/` | Planejamento, execução, verificação |
| `skills/operacional/` | Backup, commit, segurança, crons |
| `skills/starter/` | Onboarding, bootstrap, wizards |
| `skills/canais/` | Canais de comunicação |
| `skills/cerebro/` | Gestão do segundo cérebro |
| `skills/colheita/` | Colheita de outputs |
| ... | Demais módulos |

---

## Arquivo Morto e Backup

| Caminho | O que é |
|---|---|
| `archive/` | Legado histórico, zips, exemplos |
| `archive/_curso/` | Material didático do curso starter |
| `archive/backups/` | Snapshots manuais antigos |
| `archive/exemplos/` | Exemplos de configs de agentes |
| `archive/cheatsheets-legacy-v1.0/` | Cheatsheets do starter v1.0 |
| `archive/starter-kit-zips/` | Zips do starter kit |

---

## Outros

| Caminho | O que é |
|---|---|
| `vaults/segundo-cerebro-jadielson/` | Clone do vault GitHub (segundo cérebro) |
| `agentes/` | Prompts e definições de agentes (mirrors) |
| `Anexos/` | **consolidado em `F2 memory/Anexos/`** |
| `entregaveis/` → `F2 memory/outputs/` | **Consolidado** |
| `reports/` → `F2 memory/outputs/reports/` | **Consolidado** |
| `templates/` → `F2 memory/templates/` | **Consolidado** |
| `contextos/` → `F2 memory/context/` | **Consolidado** |
| `calendarios/` → `F2 memory/context/calendarios/` | **Consolidado** |
| `content/` → `F2 memory/outputs/` | **Consolidado** |
| `pesquisa/` → `F2 memory/projects/pesquisa/` | **Consolidado** |
| `projetos/` → `[F1] PROJETOS/` | **Consolidado** |
| `producao/` → `F2 memory/outputs/` | **Consolidado** |
| `notion-configs/` → `scripts/notion/configs/` | **Consolidado** |
| `config-patches/` → `scripts/patches/` | **Consolidado** |
| `_curso/` → `archive/_curso/` | **Consolidado** |
| `backups/` → `archive/backups/` | **Consolidado** |
| `exemplos/` → `archive/exemplos/` | **Consolidado** |
| `memory/` → `F2 memory/` | **Consolidado** |

---

## Regra para agentes

> Se você não encontrar o que procura, **não invente**.  
> Consulte `MAPA.md`, busque no `F2 memory/` ou diga "não consegui acessar".