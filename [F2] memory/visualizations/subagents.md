---
tipo: visualizacao
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Cheat Sheet — Subagents

> Invoque com `@nome` no chat do Claude Code. Para ver o prompt completo de cada agente, abra `.claude/agents/<nome>.md`.

---

## Quando usar cada um

| Subagent | Use quando... | Nunca use para... |
|----------|--------------|------------------|
| `@logika` | Legenda da Lógika, mini-case, proposta comercial | Conteúdo de clientes políticos |
| `@rogerio` | Legenda ou roteiro do mandato do Rogério | Qualquer menção a eleição ou campanha |
| `@saude` | Post da SMS, campanha mensal, homenagem à equipe | Conteúdo político |
| `@camara` | Post institucional da Câmara (sessão, projeto, linha seg/qua/sex) | Post individual de Josi/Vando/Manoel como figura própria |
| `@sindss` | Feed SINDSS, reel educativo, depoimento de sexta | Conteúdo fora do calendário editorial |
| `@vereadores` | Post individual da Josi, Vando ou Manoel | Câmara como instituição |
| `@alem-da-foto` | Roteiro do canal, post de divulgação, briefing de captação | Conteúdo comercial ou político |
| `@lives-louvor` | Divulgação de live, reflexão bíblica, edital, roteiro gospel | Polêmica doutrinária ou política |
| `@pessoal` | Rotina, família, hábitos, propósito, finanças pessoais | Qualquer frente profissional |
| `@bibliotecaria` | Busca no vault, conexões entre notas, manutenção, orphan check | Geração de conteúdo de frente |

---

## Hierarquia de invocação

```
1. @nome explícito          → vai esse, sem discussão
2. Frente clara na tarefa   → agente da frente
3. Vault / organização      → @bibliotecaria
4. Nada se aplica           → Claude principal (sem subagent)
```

---

## Exemplos de invocação

**Explícita:**
```
@rogerio escreve uma legenda sobre a visita ao Povoado Mata
@saude post sobre o Outubro Rosa no CEO
@bibliotecaria quais notas falam sobre comunicação e saúde?
@pessoal me ajuda a organizar minha rotina semanal
```

**Automática** (Claude Code decide com base no contexto):
```
"preciso de uma legenda para repostagem do clipe do SINDSS"
→ dispara @sindss

"quero um roteiro para o canal sobre a foto da feira antiga"
→ dispara @alem-da-foto

"tem alguma nota duplicada sobre Outubro Rosa?"
→ dispara @bibliotecaria
```

---

## Onde cada agente escreve

| Agente | Destino dos outputs |
|--------|-------------------|
| `@logika` | `outputs/legendas/`, `outputs/drafts/` |
| `@rogerio` | `outputs/legendas/`, `outputs/roteiros/` |
| `@saude` | `outputs/drafts/`, `outputs/legendas/` |
| `@camara` | `outputs/drafts/`, `outputs/legendas/` |
| `@sindss` | `outputs/drafts/` |
| `@vereadores` | `outputs/legendas/`, `outputs/drafts/`, `outputs/roteiros/` |
| `@alem-da-foto` | `outputs/roteiros/alem-da-foto/`, `outputs/drafts/` |
| `@lives-louvor` | `outputs/roteiros/lives-louvor/`, `outputs/drafts/`, `outputs/legendas/` |
| `@pessoal` | `outputs/pessoal/` |
| `@bibliotecaria` | `outputs/sugestoes-bibliotecaria/` |

---

## Regra de ouro que todos herdam

Bibliotecária, nunca autora. Subagents geram drafts com `revisado: false`. Jadielson revisa e publica.
