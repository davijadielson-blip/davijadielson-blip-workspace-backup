---
tipo: skill
nome: reindex
trigger: "usuário digita 'reindex' ou 'reindexar' ou 'atualizar memória'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-10
---

# SKILL — reindex (Reindexação Forçada)

> Procedimento para rodar ao trocar de LLM (Claude → OpenClaw, GPT, Hermes etc.)
> ou quando quiser "atualizar a memória" do agente atual após um período sem uso.
> Garante que qualquer IA entenda o vault antes de operar.

---

## Trigger

O usuário digita: `reindex`, `reindexar`, `atualizar memória`, `novo agente`, `trocar de IA`.

---

## Procedimento

### Fase 1 — Varredura completa (ordem obrigatória)

Ler nesta sequência exata:

1. `CLAUDE.md` — constituição: regras, fluxos, frentes, preferências de escrita
2. `PROPAGATION.md` — protocolo de propagação e gatilhos
3. `_MAP.md` (raiz) — visão geral da estrutura
4. `[F2] memory/_MAP.md` → `[F2] memory/context/_MAP.md` → `[F2] memory/agents/_MAP.md` → `[F2] memory/outputs/_MAP.md` → `[F2] memory/sessions/_MAP.md`
5. `[F1] 5-Frentes/_MAP.md` → mapas de cada frente ativa
6. `[F2] memory/context/business-context.md` — situação atual do negócio
7. `[F2] memory/context/people.md` — pessoas-chave
8. `[F2] memory/context/pendencias.md` — o que está em aberto
9. `[F2] memory/context/deadlines.md` — o que está chegando
10. `[F2] memory/agents/*.md` — briefings de todas as frentes ativas
11. Últimas 7 entradas de `[F2] memory/sessions/` (arquivos mais recentes)
12. Última entrada de `[F2] memory/context/decisoes/` (mês mais recente)

### Fase 2 — Auto-relatório

Devolver ao usuário um relatório estruturado provando que entendeu:

```
## Reindexação completa — [data]

### Quem é Jadielson
[3 linhas: empreendedor audiovisual, servidor, músico gospel, família]

### Regra de ouro
[1 linha: bibliotecária nunca autora; o que a IA pode e não pode]

### Frentes ativas e seus subagents
| Frente | Subagent | Tom resumido |
|---|---|---|
[uma linha por frente]

### Pendências críticas agora
[lista ou "nenhuma"]

### Próximos deadlines
[lista ou "nenhum nos próximos 7 dias"]

### Última sessão
[data + resumo de 1 linha]

### Decisão arquitetural mais recente
[data + resumo de 1 linha]

### O que NÃO fazer
- Tocar em [F1] sem aprovação explícita
- Pedir voto em conteúdo do Rogério Rocha
- Inventar dados (números, valores, datas)
- Escrever como observador externo em conteúdo de cliente
```

### Fase 3 — Validação

Aguardar resposta de Jadielson:
- **"100% mapeado"** → encerrar reindex, vault operacional
- **Aponta lacuna** → voltar à Fase 1 para os arquivos específicos indicados, re-relatar apenas a seção corrigida

### Fase 4 — Registrar reindexação

Acrescentar em `[F2] memory/context/decisoes/YYYY-MM.md`:

```markdown
## [DD/MM] Reindexação — [LLM usado]
**Resultado:** [100% mapeado / lacunas identificadas e corrigidas]
**LLM:** [Claude Code Sonnet / OpenClaw / GPT-4o / etc.]
**Observação:** [se houver algo a notar]
```

---

## Output esperado

Auto-relatório entregue + validação de Jadielson + entrada registrada em `decisoes/`.

---

## Notas

- Duração estimada: 2–5 minutos de leitura, dependendo do volume de sessões
- Não pular arquivos mesmo que pareçam redundantes — a sequência tem intenção
- Se um arquivo listado não existir: mencionar e continuar
- Esta skill é o "contrato de onboarding" para qualquer IA nova no vault
