---
tipo: skill
nome: salve
trigger: "usuário digita 'salve' ou 'fechar sessão' ou 'encerrar'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-10
---

# SKILL — salve (Fechamento de Sessão)

> Fecha a sessão com git add + commit + push, atualiza o log da sessão e marca pendências.
> Rodar sempre ao fim de cada sessão de trabalho.

---

## Trigger

O usuário digita: `salve`, `fechar sessão`, `encerrar`, `fim de sessão`.

---

## Procedimento

### Fase 1 — Checagem de drafts revisados

1. Verificar se algum draft em `[F2] memory/outputs/` foi marcado como `revisado: true` durante a sessão
2. Se sim: listar e perguntar se deve mover/arquivar
3. Atualizar Hub se houve novos drafts: `[F2] memory/visualizations/Hub.md`

### Fase 2 — Atualizar log da sessão

4. Abrir ou criar `[F2] memory/sessions/YYYY-MM-DD.md`
5. Acrescentar ao final (sem sobrescrever):

```markdown
---

## Atualização — HH:MM

### O que foi feito
- [resumo das ações desta sessão]

### Decisões
- [decisões tomadas, se houver]

### Em aberto
- [tarefas que ficaram pendentes]
```

### Fase 3 — Atualizar pendências

6. Se houve tarefas concluídas: mover de `- [ ]` para `- [x]` + data em `[F2] memory/context/pendencias.md`
7. Se surgiram novas pendências: adicionar na seção correta (🔴/🟡/⚪)

### Fase 4 — Git commit + push

8. Verificar arquivos modificados: `git status`
9. Fazer stage de tudo em `[F2] memory/`: `git add [F2] memory/ CLAUDE.md PROPAGATION.md`
10. Commit com mensagem descritiva:
    ```
    git commit -m "sessão: YYYY-MM-DD — [resumo de 1 linha do que foi feito]"
    ```
11. Push: `git push origin main`
12. Confirmar: `git log --oneline -3`

### Fase 5 — Relatório final

```
## ✅ Sessão salva

- Drafts revisados: [n]
- Log atualizado: [F2] memory/sessions/YYYY-MM-DD.md
- Pendências atualizadas: [sim/não]
- Commit: [hash curto] — [mensagem]
- Push: ✅ GitHub atualizado

Até a próxima. 🤙
```

---

## Output esperado

Sessão commitada e pushada. Log atualizado. Pendências refletindo estado real.

---

## Notas

- Nunca usar `git add .` sem revisar — preferir `git add [F2] memory/` para não incluir arquivos pessoais acidentalmente
- Se o push falhar (sem internet): commitar localmente e sinalizar para Jadielson fazer push depois
- Não encerrar sem confirmar que o push foi OK
