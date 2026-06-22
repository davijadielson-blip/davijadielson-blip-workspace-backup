---
tipo: referencia-operacional
subtipo: bot-telegram
ultimo-update: 2026-05-18
agente-compatibilidade: [claude, openclaw, gpt, hermes]
---

# Bot Telegram — Manual de Uso

## Comandos de captura rápida (prefixos)

| Prefixo | Tipo |
|---|---|
| `/i <texto>` | Inbox / ideia rápida |
| `/t <texto>` | Tarefa |
| `/c <texto>` | Compromisso |
| `/r <texto>` | Reunião |
| `/g <texto>` | Gravação / captação |
| `/n <texto>` | Nota |
| `/p <texto>` | Pendência |

Data opcional no texto: `amanhã 14h`, `sexta 16h30`, `20/05 09h`, `2026-05-20`.

---

## Comandos interativos

| Comando | Função |
|---|---|
| `/menu` | Menu guiado com botões inline |
| `/status` | Status do sistema (crons, sync, git, última captura) |
| `/agenda` | Próximos eventos — hoje + amanhã + depois (Google Calendar) |
| `/buscar <termo>` | Top 5 itens da Captura Geral com link Notion |

---

## Ações sobre última captura

| Comando | Função |
|---|---|
| `/confirmar` | Reexibe confirmação da última captura |
| `/cancelar` | Apaga (Notion + Calendar + inbox) — exige clique no botão |
| `/repetir` | Duplica no Notion com nova data |

---

## Fluxo do /menu

```
Menu → Frente → Tipo → Texto → Data? → Confirmação → Criar
```

- Botão ↩️ Voltar em cada tela (histórico preservado no estado)
- Botão ❌ Fechar → limpa estado

---

## Estado conversacional

- Arquivo: `scripts/state/telegram-state.json`
- Expira em **1 hora** — fluxos travados são limpos automaticamente
- Preserva `ultima_captura` mesmo após expiração de fluxo

---

## Arquitetura

| Arquivo | Função |
|---|---|
| `scripts/cron-jobs/telegram-polling.sh` | Daemon principal (loop + long polling) |
| `scripts/lib/telegram-commands.py` | Todos os 8 handlers de comando |
| `scripts/lib/telegram-router.py` | Roteador: texto → handler correto |
| `scripts/lib/state-manager.py` | CRUD do estado em JSON |
| `scripts/state/telegram-state.json` | Estado persistente por chat_id |

**Daemon:** launchd com `KeepAlive=true` + `timeout=25` no getUpdates → latência <1s.

---

## Troubleshooting

| Problema | Diagnóstico | Solução |
|---|---|---|
| Bot não responde | `launchctl list \| grep telegram` | Se PID=-, reload do plist |
| Responde lento (>5s) | `tail /tmp/telegram-polling.error.log` | Ver erro; reiniciar daemon |
| Estado travado | Deletar entrada do chat_id em `telegram-state.json` | — |
| mktemp conflict | `ls /tmp/tg-*.json` | `rm /tmp/tg-*.json` + reiniciar |
| Captura falha | `tail /tmp/telegram-polling.log` | Ver traceback Python |

**Reiniciar daemon:**
```bash
launchctl unload ~/Library/LaunchAgents/br.segundo-cerebro.telegram-polling.plist
launchctl load  ~/Library/LaunchAgents/br.segundo-cerebro.telegram-polling.plist
```
