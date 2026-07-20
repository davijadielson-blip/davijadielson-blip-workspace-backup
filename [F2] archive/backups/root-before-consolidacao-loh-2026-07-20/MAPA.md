# MAPA — Workspace Lôh / Jadielson

> **Fonte de verdade única. GitHub é backup.**
> **Última reorganização:** 2026-06-22 — Mapeamento aos 3 Fluxos

---

## Os 3 Fluxos (e o Fluxo 0)

| Tag | Nome | Quem mexe | Sistema? |
|---|---|---|---|
| **`[F0]`** | CAPTURA | Só você | Consulta, não edita |
| **`[F1]`** | CRIATIVO (você) | Só você | Consulta, nunca escreve |
| **`[F2]`** | SISTEMA (máquina) | Agentes | Gerencia livre |
| **`[F3]`** | INTEGRAÇÃO | Você + Sistema | Você cria, sistema gerencia metadados |

---

## Estrutura Completa

```
workspace/                            ← FONTE DE VERDADE ÚNICA
│
├── [F0] 0-Inbox/          22 arq    ← CAPTURA BRUTA (pré-fluxo)
│                                     Suas notas rápidas, ideias soltas
│
├── [F1] 1-Permanentes/    7 subp.   ← REFERÊNCIAS (notas evergreen)
├── [F1] 2-Literatura/     6 subp.   ← LEITURAS (livros, cursos concluídos)
├── [F1] 3-Daily/          8 notas   ← DIÁRIO (notas do dia, reflexões)
├── [F1] 4-Pessoal/        12 subp.  ← PESSOAL (parede d'água)
├── [F1] 5-Frentes/        8 subp.   ← TRABALHO (clientes, frentes ativas/standby)
├── [F1] ESTUDOS/          4 subp.   ← CURSOS (A INICIAR / EM ANDAMENTO / CONCLUÍDO / PAUSADO)
├── [F1] TAREFAS/                    ← LISTAS PESSOAIS (deprecated)
│
├── [F2] memory/           1671 arq  ← ❤️ CORAÇÃO DO SISTEMA
│   ├── agents/                      Definições de agentes e prompts
│   ├── context/                     Contextos estratégicos, decisões, calendários
│   ├── databases/                   Dados estruturados, mapeamentos
│   ├── decisions/                   Registro de decisões
│   ├── inbox-externa/               Capturas de fontes externas (áudio, etc)
│   ├── outputs/                     Entregáveis, relatórios, drafts
│   ├── projects/                    Memória de projetos (planos, pesquisas)
│   ├── sessions/                    Logs de sessões
│   ├── templates/                   Templates canônicos
│   └── visualizations/              Diagramas, mapas, dashboards
│
├── [F2] agentes/          155 arq   ← DEFINIÇÕES DE AGENTES (prompts, personalidades)
├── [F2] archive/          74 arq    ← HISTÓRICO (backups, exemplos, materiais legados)
├── [F2] vaults/           4410 arq  ← CLONE DO GITHUB (sincronização automática)
│
├── [F3] PROJETOS/         7 subp.   ← PROJETOS (você cria, sistema gerencia)
│
├── scripts/                         ← AUTOMAÇÃO (não mexer)
├── skills/                          ← HABILIDADES (não mexer)
│
├── SOUL.md                          Minha identidade
├── AGENTS.md                        Manual de conduta
├── IDENTITY.md                      Ficha formal
├── USER.md                          Quem é Jadielson
├── MEMORY.md                        Memória de longo prazo
├── MAPA.md                          Este arquivo
├── TOOLS.md                         Anotações de ferramentas
├── HEARTBEAT.md                     Tarefas periódicas
├── [F1] _README.md                  Regras do Fluxo 1
├── [F2] _README.md                  Regras do Fluxo 2
└── [F3] PROJETOS/_README.md         Regras do Fluxo 3
```

---

## 🧠 REGRA ABSOLUTA — Workspace é o Cérebro Central

> **"Varra todo o banco. O workspace é a fonte. Tavily é complemento."**

### Para TODO agente, em TODA resposta:

**1. CONSULTE O WORKSPACE PRIMEIRO**
   - Antes de qualquer resposta, vasculhe o workspace inteiro
   - Não se limite a `[F2] memory/` — contexto relevante pode estar em `[F1]`, `[F3]`, qualquer pasta
   - Use `memory_search` e ferramentas de leitura para encontrar informações

**2. WEB SÓ DEPOIS**
   - Tavily (web_search) é complementar, não substituto
   - Só busque na web quando o workspace não tiver a resposta

**3. REGISTRE TUDO QUE FOR PERTINENTE**
   - Informação nova encontrada → salve em `[F2] memory/`
   - Decisão tomada → registre em `[F2] memory/decisions/`
   - Aprendizado relevante → salve no arquivo de diário (`[F2] memory/YYYY-MM-DD.md`)
   - Se não foi salvo, não existiu para a próxima sessão

**4. APRENDA ENTRE SESSÕES**
   - Memória não sobrevive a restart de sessão
   - Use `[F2] memory/` como ponte entre sessões
   - Registre descobertas, ajustes de comportamento, regras para o futuro

**5. NÃO INVENTE**
   - Se o workspace não tem a resposta E a web não ajudou: **"não consegui acessar essa informação"**
   - Nunca alucine dados, contextos ou integrações

---

## Consolidated Paths (de onde vieram)

| Saiu de | Foi para |
|---|---|
| `entregaveis/` | `[F2] memory/outputs/` |
| `reports/` | `[F2] memory/outputs/reports/` |
| `templates/` (raiz) | `[F2] memory/templates/` |
| `contextos/` | `[F2] memory/context/` |
| `calendarios/` | `[F2] memory/context/calendarios/` |
| `content/` | `[F2] memory/outputs/` |
| `pesquisa/` | `[F2] memory/projects/pesquisa/` |
| `projetos/` (raiz) | `[F3] PROJETOS/` |
| `producao/` | `[F2] memory/outputs/` |
| `Anexos/` | `[F2] memory/Anexos/` |
| `_curso/` | `[F2] archive/_curso/` |
| `backups/` | `[F2] archive/backups/` |
| `exemplos/` | `[F2] archive/exemplos/` |
| `memory/` (raiz) | `[F2] memory/` (fundido) |
| `notion-configs/` | `scripts/notion/configs/` |
| `config-patches/` | `scripts/patches/` |

---

## Diretórios que NÃO se move (não mexer)

- `scripts/` — automação
- `skills/` — habilidades dos agentes
- `vaults/` — clone do repositório (sincronizado por cron, não editar diretamente)