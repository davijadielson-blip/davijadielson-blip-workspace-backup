---
tipo: skill
nome: salve
trigger: "usuário digita 'salve' ou 'fechar sessão' ou 'encerrar'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-28
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

### Fase 2 — Atualizar log da sessão ⚠️ OBRIGATÓRIO

4. Abrir ou criar `[F2] memory/sessions/YYYY-MM-DD.md` (data do dia)
5. **Se o arquivo não existir:** criar com o cabeçalho abaixo e depois acrescentar o bloco de atualização
6. **Se já existir:** acrescentar ao final (nunca sobrescrever o que já está lá)

**Cabeçalho do arquivo (apenas na criação):**
```markdown
---
data: YYYY-MM-DD
tipo: sessao
agente: [nome do agente/LLM usado]
---

# Sessão — YYYY-MM-DD
```

**Bloco de atualização (acrescentar sempre):**
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

> Este arquivo é o histórico diário do vault. É padrão permanente — toda sessão, sem exceção.

### Fase 3 — Atualizar pendências

7. Se houve tarefas concluídas: mover de `- [ ]` para `- [x]` + data em `[F2] memory/context/pendencias.md`
8. Se surgiram novas pendências: adicionar na seção correta (🔴/🟡/⚪)

### Fase 4 — Git commit + push

9. Verificar arquivos modificados: `git status`
10. Fazer stage dos arquivos relevantes: `git add "[F2] memory/" CLAUDE.md PROPAGATION.md`
11. Commit com mensagem descritiva:
    ```
    git commit -m "sessão: YYYY-MM-DD — [resumo de 1 linha do que foi feito]"
    ```
12. Push: `git push origin main`
13. Confirmar: `git log --oneline -3`

### Fase 5 — Relatório final

```
## ✅ Sessão salva

- Drafts revisados: [n]
- Log atualizado: [F2] memory/sessions/YYYY-MM-DD.md ✅
- Pendências atualizadas: [sim/não]
- Commit: [hash curto] — [mensagem]
- Push: ✅ GitHub atualizado

Até a próxima. 🤙
```

---

## Output esperado

Sessão commitada e pushada. Log em `[F2] memory/sessions/YYYY-MM-DD.md` atualizado. Pendências refletindo estado real.

---

## Notas

- O log de sessão é **obrigatório** — não encerrar sem ele
- Nunca usar `git add .` sem revisar — preferir `git add "[F2] memory/"` para não incluir arquivos pessoais
- Se o push falhar (sem internet): commitar localmente e sinalizar para Jadielson fazer push depois
- Não encerrar sem confirmar que o push foi OK
- Nomes de arquivo: nunca usar `? " * : < > \ |` — substituir silenciosamente antes de criar