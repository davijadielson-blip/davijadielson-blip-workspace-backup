---
tipo: decisao
gerado-por: claude
data: 2026-05-10
---

# Decisão: Integração Google Calendar

## Motivação

O Google Calendar já é usado por Jadielson para rotina e compromissos. Integrá-lo ao vault evita duplicação de contexto: a daily note passa a refletir compromissos reais e os comandos de agenda funcionam como uma visão unificada de produção + compromissos.

## Conector usado

MCP nativo disponível no Claude Code: `mcp__claude_ai_Google_Calendar__*`
Calendário primário: `davijadielson@gmail.com`
Timezone padrão: `America/Maceio` (UTC-3)

## Comandos que usam o Calendar

| Comando | Operação MCP | Cria eventos? |
|---------|-------------|--------------|
| `/hoje` | `list_events` (só hoje) | ❌ |
| `/agenda` | `list_events` (N dias) | ❌ |
| `/agendar` | `create_event` (1 evento) | ✅ com confirmação |
| `/sincronizar-sazonais` | `create_event` (múltiplos) | ✅ com confirmação |
| `/bloquear-rotina` | `create_event` (recorrentes) | ✅ com confirmação |

## Campos usados na criação de eventos

| Campo | Uso |
|-------|-----|
| `summary` | Título com ícone de frente (ex: "🎬 Reunião cliente X") |
| `startTime` / `endTime` | ISO 8601 com `-03:00` |
| `timeZone` | `America/Maceio` (sempre) |
| `colorId` | 1–11 conforme frente (ver tabela abaixo) |
| `description` | Frente + origem do comando |
| `allDay` | `true` apenas para `/sincronizar-sazonais` |
| `recurrenceData` | Array de RRULE para `/bloquear-rotina` |
| `overrideReminders` | `[]` para sazonais (só visual, sem popup) |

## Mapa de cores por frente

| Frente | Ícone | colorId | Nome |
|--------|-------|---------|------|
| Lógika Creative | 🎬 | 7 | Peacock |
| Câmara Municipal | 🏛️ | 9 | Blueberry |
| Saúde | 🏥 | 10 | Basil |
| SINDSS | 🔴 | 6 | Tangerine |
| Rogério Rocha | 🗳️ | 3 | Grape |
| Outros Vereadores | 📢 | 4 | Flamingo |
| Além da Foto | 🎙️ | 1 | Lavender |
| Lives de Louvor | 🎵 | 5 | Banana |
| Pessoal / Família | 👨‍👧 | 2 | Sage |
| Rotina / Vault | 🧹 | 8 | Graphite |

## Regras de classificação

Arquivo de referência: `[F2] claude/databases/regras-classificacao-agenda.md`
Editável por Jadielson — adicionar palavras-chave sem alterar os comandos.

## Regras de segurança

- **Nunca criar ou modificar eventos sem confirmação explícita** de Jadielson
- **Nunca deletar eventos existentes** (nenhum comando implementa `delete_event`)
- **`/bloquear-rotina` simula primeiro** — lista o que criaria antes de criar
- **`/sincronizar-sazonais` lista o plano completo** antes de qualquer criação
- Calendar é leitura por padrão; escrita é exceção que sempre requer aprovação

## Log de eventos criados

`[F2] claude/logs/eventos-criados.md` — linha por evento criado, com data, hora, título e frente.
