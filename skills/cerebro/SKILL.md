---
tipo: skill
nome: cerebro
trigger: "usuário digita 'cerebro' ou 'modo briefing'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-10
---

# SKILL — cerebro (Modo Briefing)

> Carrega o contexto completo do vault antes de qualquer operação.
> Use no início de uma sessão nova ou ao trocar de frente.

---

## Trigger

O usuário digita: `cerebro`, `modo briefing`, `me atualiza` ou `contexto completo`.

---

## Procedimento

### Fase 1 — Carregar constituição

1. Ler `CLAUDE.md` (raiz) — regras, fluxos, frentes, preferências
2. Ler `PROPAGATION.md` — protocolo de propagação

### Fase 2 — Carregar estado atual

3. Ler `[F2] memory/context/pendencias.md` — o que está em aberto
4. Ler `[F2] memory/context/deadlines.md` — o que está chegando
5. Ler `[F2] memory/context/business-context.md` — situação do negócio
6. Ler `[F2] memory/context/people.md` — equipe, clientes, família

### Fase 3 — Carregar contexto operacional

7. Ler todos os `_MAP.md` relevantes para a tarefa do dia (começar pela raiz)
8. Listar subagents disponíveis: `ls .claude/agents/`
9. Buscar datas sazonais próximas (7 dias): `[F2] memory/databases/datas-sazonais/`
10. Listar drafts pendentes: `grep -rl "revisado: false" [F2] memory/outputs/`
11. Ler última sessão: `[F2] memory/sessions/` — arquivo mais recente

### Fase 4 — Auto-relatório

Devolver ao usuário um resumo estruturado:

```
## Estou a par de:
- **Frentes ativas:** [lista]
- **Subagents disponíveis:** [lista]
- **Pendências críticas:** [lista ou "nenhuma"]
- **Próximos deadlines:** [lista ou "nenhum"]
- **Datas sazonais próximas:** [lista]
- **Drafts aguardando revisão:** [contagem e nomes]
- **Última sessão:** [data e resumo de 1 linha]
- **Regra de ouro:** bibliotecária, nunca autora. Fluxo 1 intocável.

Pronto. O que fazemos hoje?
```

---

## Output esperado

Relatório de briefing entregue ao usuário. Nenhum arquivo criado nesta skill — apenas leitura e síntese.

---

## Notas

- Se algum arquivo de contexto não existir, mencionar mas não interromper
- Não inventar dados — se não encontrar, dizer "não encontrado"
- Duração estimada: 30–60 segundos de leitura
