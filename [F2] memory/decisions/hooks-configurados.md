---
tipo: decisao
gerado-por: claude
data: 2026-05-10
---

# Decisão: Hooks do Claude Code

## Motivação

Hooks são scripts que rodam automaticamente em eventos do ciclo de vida do Claude Code, sem invocação manual. Permitem briefings automáticos, proteções de fluxo e automações pós-escrita — mantendo a regra de ouro: **a IA nunca publica, nunca decide por Jadielson**.

## Arquitetura adotada

### Eventos nativos vs. solicitados

| Solicitado | Suporte nativo | Solução adotada |
|---|---|---|
| `SessionStart` | ❌ não existe | `UserPromptSubmit` + lock file `/tmp/vault-session-{ID}.lock` |
| `SessionEnd` | ❌ não existe | `Stop` com log incremental em `/tmp/` |
| `PostToolUse` | ✅ | direto |
| `UserPromptSubmit` | ✅ | direto |
| `Stop` | ✅ | direto |

### Limitação de hooks e Calendar

Hooks são scripts bash — sem acesso ao MCP. O `session-start.sh` resolve isso emitindo no stdout uma instrução que Claude lê e executa como chamada MCP, integrando o resultado na primeira resposta.

## Inventário dos 4 hooks

### `session-start.sh` — UserPromptSubmit (primeiro prompt da sessão)

**Arquivo:** `.claude/hooks/session-start.sh`
**Trigger:** todo `UserPromptSubmit`, mas silencia após o primeiro (lock file por session_id)
**O que faz:**
1. Finaliza o log da sessão anterior (se houver arquivo `/tmp/vault-session-*-activity.log` de sessão diferente)
2. Exibe briefing: tipo do dia, drafts pendentes, aniversariantes de hoje/amanhã, datas sazonais dos próximos 7 dias
3. Lembretes específicos: sexta → `/manutencao`; domingo → `/planejar-semana`
4. Emite instrução para Claude buscar eventos do Google Calendar
5. Cria lock file `/tmp/vault-session-{ID}.lock`

**Output:** silencioso se tudo limpo ("✅ Tudo limpo — bora trabalhar.") ou briefing seccional se houver dados

### `prompt-guard.sh` — UserPromptSubmit (todo prompt)

**Arquivo:** `.claude/hooks/prompt-guard.sh`
**O que faz:** verifica frases de publicação e combinação Rogério+eleição
**Gatilhos de publicação:** frases completas ("publicar agora", "postar agora", "envia esse", "manda esse", "posta esse", "sobe esse")
**Gatilho Rogério:** `@rogerio` + palavras de eleição/campanha
**Comportamento:** aviso não-bloqueante (exit 0 sempre) — nunca interrompe o fluxo

### `post-write.sh` — PostToolUse(Write)

**Arquivo:** `.claude/hooks/post-write.sh`
**Trigger:** toda chamada Write bem-sucedida
**Lógica por path:**

| Path | Ação |
|------|------|
| `outputs/legendas/` | Instrui Claude a gerar resumo-whats automaticamente |
| `outputs/roteiros/` | Appende entrada em `databases/pipeline.md` |
| `[F2] claude/agents/` | Appende linha em `logs/agents-changes.md` |
| Qualquer outro | Sai silenciosamente |

**Também:** registra arquivo criado em `/tmp/vault-session-{ID}-activity.log`

### `session-log.sh` — Stop (após cada resposta)

**Arquivo:** `.claude/hooks/session-log.sh`
**O que faz:** atualiza timestamp de "última resposta" em `/tmp/vault-session-{ID}-activity.log`
**Por que incremental:** não há como detectar "fim de sessão" nativamente — o log permanente é criado pelo `session-start.sh` na próxima abertura

## Arquivos de estado (temporários)

| Arquivo | Criado por | Deletado por |
|---------|-----------|-------------|
| `/tmp/vault-session-{ID}.lock` | `session-start.sh` | `session-start.sh` (próxima sessão) |
| `/tmp/vault-session-{ID}-activity.log` | `session-start.sh` / `session-log.sh` | `session-start.sh` (ao finalizar como log permanente) |

## Arquivos permanentes criados pelos hooks

| Arquivo | Criado por |
|---------|-----------|
| `[F2] claude/logs/sessoes/YYYY-MM-DD-HHMM.md` | `session-start.sh` (finalizando sessão anterior) |
| `[F2] claude/logs/agents-changes.md` | `post-write.sh` |
| `[F2] claude/databases/pipeline.md` | `post-write.sh` |

## Regras herdadas

- Nenhum hook publica, envia ou decide por Jadielson
- Todos os avisos são não-bloqueantes (exit 0)
- Hooks silenciosos quando não há dados relevantes (zero output = zero ruído)
