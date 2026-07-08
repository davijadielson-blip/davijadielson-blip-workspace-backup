---
tipo: session-log
data: 2026-05-28
agente: claude-sonnet-4-6
---

# Log de Sessão — 2026-05-28

---

## Atualização — 14:30

### O que foi feito
- Diagnosticado problema de recodificação do OneDrive: 3 arquivos com `?` e `"` nos nomes foram convertidos para `&#x3f;` e `&#x22;`
- Renomeados os 3 arquivos para nomes sem caracteres inválidos no Windows:
  - `📌3• COMO CAPTAR MAIS CAPITAL RAPIDAMENTE?.md` → sem `?`
  - `Por que ninguem gosta de vereador?.md` → sem `?`
  - `PODCAST "QUESTÃO DE LÓGICA".md` → sem `"`
- Commit e push realizados com sucesso (`fix: remove caracteres inválidos (? e ") de nomes de arquivo`)
- Verificado: conteúdo dos arquivos intacto, sem wikilinks quebrados

### Decisões
- Caracteres `?`, `"`, `*`, `:`, `<`, `>`, `\`, `|` devem ser evitados em nomes de arquivo (OneDrive recodifica por incompatibilidade com Windows)

### Em aberto
- Arquivos `??` untracked no git ([F0] 0-Inbox, [F1] 5-Frentes, [F2] memory/inbox-externa) — novos arquivos criados fora desta sessão, pendentes de commit
- `.obsidian/(2).json` duplicatas — provavelmente geradas pelo OneDrive em conflito de sync, verificar e remover

---

## Atualização — 15:30

### O que foi feito
- Regra de nomes de arquivo gravada: `? " * : < > \ |` proibidos — substituição silenciosa obrigatória
- Skill `salve` atualizada: log de sessão em `[F2] memory/sessions/YYYY-MM-DD.md` marcado como OBRIGATÓRIO
- Log diário estabelecido como padrão permanente de fechamento

### Decisões
- Sanitização de nomes é ativa e silenciosa — sem perguntar, sempre substituir
- Log de sessão obrigatório a cada salve, para qualquer agente/LLM

### Em aberto
- Links internos do Obsidian quebrados após renomeações ([F1] ESTUDOS/PROJETOS/TAREFAS e [F2] memory) — corrigir manualmente no Obsidian
