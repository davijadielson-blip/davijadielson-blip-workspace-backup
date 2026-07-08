---
description: Ritual de sexta — logs da semana, drafts velhos, notas órfãs, relatório
---

Execute o ritual de manutenção semanal do vault. Estimativa: 15 minutos. Siga cada passo.

**PASSO 1 — Logs da semana**

Liste os arquivos criados em `[F2] memory/logs/comandos/` nos últimos 7 dias:
```bash
find "[F2] memory/logs/comandos" -name "*.md" -newer $(date -v-7d +"%Y-%m-%d") 2>/dev/null | sort
```

Exiba a lista. Resumo: quantos comandos foram executados e quais frentes foram atendidas.

**PASSO 2 — Drafts velhos sem revisão**

Encontre todos os arquivos em `[F2] memory/outputs/` com `revisado: false` criados há mais de 7 dias:
```bash
find "[F2] memory/outputs" -name "*.md" -not -newer $(date -v-7d +"%Y-%m-%d") 2>/dev/null | sort
```

Para cada arquivo encontrado, mostre:
```
- YYYY-MM-DD | frente | tipo | nome-do-arquivo
  → Proposta: [ ] manter  [ ] deletar  [ ] revisar agora
```

**Aguarde a decisão de Jadielson para cada arquivo antes de deletar qualquer coisa.**
Nunca delete sem confirmação explícita.

**PASSO 3 — Verificações de saúde do vault**

Execute cada verificação e exiba o resultado:

3a. **Notas órfãs em [F2] memory/outputs/** — arquivos sem nenhum link de entrada:
```bash
# (verificação manual — listar arquivos e cruzar com referências)
```
Informe quais arquivos em `outputs/` não são referenciados por nenhuma outra nota.

3b. **Pasta Inbox** — verifique se há itens em `[F0] 0-Inbox/` há mais de 3 dias:
```bash
find "[F0] 0-Inbox" -name "*.md" -not -newer $(date -v-3d +"%Y-%m-%d") 2>/dev/null
```
Se encontrar, liste e sugira destino baseado no conteúdo.

3c. **Agentes desatualizados** — liste os arquivos em `[F2] memory/agents/` com data de criação (não checagem de atualização automática — apenas informe a data do campo `data-criacao` de cada um para Jadielson avaliar se precisam de revisão).

**PASSO 4 — Gerar relatório**

Crie `[F2] memory/logs/manutencao/YYYY-MM-DD.md`:

```
---
tipo: log-manutencao
data: YYYY-MM-DD
gerado-por: claude
comando: /manutencao
---

# Manutenção — YYYY-MM-DD

## Atividade da semana
<resumo do Passo 1>

## Drafts velhos
<lista com decisões pendentes ou tomadas>

## Saúde do vault
- Notas órfãs em outputs: <lista ou "nenhuma">
- Inbox com itens antigos: <lista ou "limpo">
- Agentes — última criação: <lista>

## Ações tomadas
<o que foi deletado, arquivado ou processado — somente com confirmação>

## Pendências para Jadielson
<itens que precisam de decisão manual>
```

**PASSO 5 — Exibir resumo**

Mostre o relatório completo no chat. Finalize com: "Manutenção concluída. X itens precisam da sua decisão."
