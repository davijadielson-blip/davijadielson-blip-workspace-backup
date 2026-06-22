---
tipo: mapa
pasta: [F2] memory/inbox-externa
camada: 4
subtipo: geração-ia-fonte-externa
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-10
---

# _MAP — inbox-externa

> **Camada 4 — Geração de IA com Fonte Externa**
> Esta pasta é a zona de quarentena de tudo que entra via MCP (Gmail, Drive, Calendar) ou importação manual (WhatsApp, áudio, financeiro). Nada aqui entra em `[F1]` sem revisão explícita de Jadielson.

---

## Regra de Ouro

A IA **sugere** — nunca **decide**.
Sugestões ficam aqui como `revisado: false`.
Jadielson move para `[F1]` quando e como quiser.

---

## Subpastas

| Pasta | Fonte | Método de entrada |
|---|---|---|
| `email/` | Gmail | MCP `mcp__claude_ai_Gmail__*` via `/inbox` |
| `drive/` | Google Drive | MCP `mcp__claude_ai_Google_Drive__*` via `/drive-recente` |
| `whatsapp/whatsapp-raw/` | WhatsApp | Exportação manual (.txt) |
| `whatsapp/processados/` | WhatsApp | IA processa raw → resumo estruturado |
| `audio/audio-raw/` | Reuniões, voicenotes | Arquivo de áudio manual |
| `audio/audio-transcricoes/` | Áudio | Transcrição via Whisper |
| `cruzados/` | Múltiplas fontes | `/prioridades` — hub de cruzamento |

---

## Comandos que alimentam esta pasta

| Comando | O que faz |
|---|---|
| `/inbox` | Lê Gmail (últimas 24h) → resumo por frente |
| `/inbox-cliente` | Filtra Gmail por cliente específico |
| `/agenda-email` | Cruza Calendar com Gmail (convites, follow-ups) |
| `/drive-recente` | Lista Drive (últimas 48h) → detecta novos arquivos por frente |
| `/drive-buscar` | Busca Drive por termo |
| `/drive-arquivo` | Arquiva link de referência de um arquivo do Drive |
| `/whats-importar` | Processa exportação .txt do WhatsApp |
| `/audio-importar` | Transcreve áudio e estrutura em nota |
| `/financeiro` | Importa planilha financeira e atualiza contexto |
| `/prioridades` | Cruza todas as fontes → Top 3 do dia enriquecido |

---

## Ritual de Importação

Ver `RITUAL.md` nesta pasta para o fluxo semanal recomendado.

---

## Fluxo resumido

```
Fonte externa
    ↓ (MCP ou importação manual)
[F2] memory/inbox-externa/[subpasta]/
    ↓ (IA processa + sugere)
[F2] memory/outputs/ (draft revisado: false)
    ↓ (Jadielson aprova)
[F1] (nota definitiva)
```
