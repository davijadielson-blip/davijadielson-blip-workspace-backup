---
tipo: decisao
gerado-por: claude
data: 2026-05-10
---

# Decisão: Subagents Nativos do Claude Code

## Motivação

Os briefings em `[F2] claude/agents/` funcionavam, mas dependiam de invocação manual via slash commands. Subagents nativos em `.claude/agents/` permitem invocação por `@nome` ou automática pelo Claude Code com base na `description`, carregando **só o contexto daquela frente** — foco cirúrgico, menos alucinação, mais qualidade.

## Arquitetura adotada

### Dois sistemas coexistindo

| Pasta | Função | Quem usa |
|-------|--------|---------|
| `[F2] claude/agents/` | Briefings narrativos (fonte de verdade) | Slash commands + subagents como referência |
| `.claude/agents/` | Subagents nativos do Claude Code | Invocados por `@nome` ou auto-delegação |

Os subagents sempre carregam os briefings como fonte de verdade. Briefing muda → subagent reflete.

## Hierarquia de invocação

1. Menção explícita `@nome` → vai esse, sem discussão
2. Frente clara na tarefa → agente da frente
3. Organização/busca/manutenção do vault → `@bibliotecaria`
4. Nada se aplica → Claude principal responde

## Inventário dos 10 subagents

### Tier 1 — Profissionais ativos

| Subagent | Briefing-fonte | Distinção crítica |
|----------|---------------|------------------|
| `@logika` | `agents/logika.md` | Metáfora obrigatória na abertura |
| `@rogerio` | `agents/rogerio.md` | Varredura automática de palavras de campanha |
| `@saude` | `agents/saude.md` | Cruza com databases de campanhas |
| `@camara` | `agents/camara.md` | Câmara como instituição (≠ `@vereadores`) |
| `@sindss` | `agents/sindss.md` | Verifica dia da semana antes de gerar |

### Tier 2 — Secundários

| Subagent | Briefing-fonte | Distinção crítica |
|----------|---------------|------------------|
| `@vereadores` | `agents/vereadores/index.md` + sub-briefings | Pergunta qual dos 3 antes de gerar |
| `@alem-da-foto` | `agents/alem-da-foto.md` | Tom de descoberta; usa "possivelmente" sem dado histórico |
| `@lives-louvor` | `agents/lives.md` | Cobre editais + divulgação + roteiros |

### Tier 3 — Pessoal e estratégico

| Subagent | Briefing-fonte | Distinção crítica |
|----------|---------------|------------------|
| `@pessoal` | `agents/pessoal.md` | Parede-d'água absoluta com frentes profissionais |
| `@bibliotecaria` | vault inteiro (Read only) | Nunca gera conteúdo de frente; só sugere, organiza, conecta |

## Regras herdadas por todos

- Todo output tem `revisado: false`
- Nenhum subagent publica, decide ângulo ou substitui o raciocínio de Jadielson
- Nenhum escreve fora de `[F2] claude/outputs/` (exceto `/ideia` com autorização explícita)
- `@pessoal` e profissionais são paredes-d'água — zero cruzamento sem instrução explícita

## Briefings pendentes de preenchimento (Jadielson)

- `agents/vereadores/josi-curtinhos.md` — slogan, posicionamento, tom específico
- `agents/vereadores/vando-cana-brava.md` — idem
- `agents/vereadores/manoel-gongo.md` — idem
- `agents/pessoal.md` — rotina atual, metas, mentorias em andamento
