---
tipo: verificacao-sync
data: 2026-07-20
gerado-por: loh
frente: SMS São Sebastião
cron: notion-sync-diario
---

# Verificação — Sync Notion → Google Calendar — SMS São Sebastião

Execução solicitada pelo cron `notion-sync-diario` em 2026-07-20 13:00 UTC.

## Comando executado

```bash
python3 /data/.openclaw/workspace/scripts/sync/notion-to-calendar.py
```

## Resultado do script

- Google Calendar autenticado com sucesso.
- Produção & Agenda — LÓGIKA consultada no Notion com sucesso.
- Total editorial elegível: 28 itens.
- Recorte por frente no script: Saúde 27 itens; LÓGIKA 1 item.
- Calendário Editorial: 0 criados, 28 atualizados, 0 erros.
- Captura Geral: 1 criado, 0 atualizados, 0 erros.
- Log oficial gerado em: `/data/.openclaw/workspace/memory/sessions/sync/2026-07-20.md`.

## Verificação direta no Google Calendar

Consulta feita no Google Calendar primário para julho/2026 com busca `SMS São Sebastião`.

Eventos encontrados: 18.

Datas confirmadas:

- 2026-07-08 — SMS SÃO SEBASTIÃO — 08/07/2026 — QUARTA — atualizado em 2026-07-20T13:01:35Z
- 2026-07-09 — SMS SÃO SEBASTIÃO — 09/07/2026 — QUINTA — atualizado em 2026-07-20T13:01:34Z
- 2026-07-10 — SMS SÃO SEBASTIÃO — 10/07/2026 — SEXTA — atualizado em 2026-07-20T13:01:34Z
- 2026-07-13 — SMS SÃO SEBASTIÃO — 13/07/2026 — SEGUNDA — atualizado em 2026-07-20T13:01:33Z
- 2026-07-14 — SMS SÃO SEBASTIÃO — 14/07/2026 — TERÇA — atualizado em 2026-07-20T13:01:33Z
- 2026-07-15 — SMS SÃO SEBASTIÃO — 15/07/2026 — QUARTA — atualizado em 2026-07-20T13:01:32Z
- 2026-07-16 — SMS SÃO SEBASTIÃO — 16/07/2026 — QUINTA — atualizado em 2026-07-20T13:01:32Z
- 2026-07-17 — SMS SÃO SEBASTIÃO — 17/07/2026 — SEXTA — atualizado em 2026-07-20T13:01:32Z
- 2026-07-20 — SMS SÃO SEBASTIÃO — 20/07/2026 — SEGUNDA — atualizado em 2026-07-20T13:01:31Z
- 2026-07-21 — SMS SÃO SEBASTIÃO — 21/07/2026 — TERÇA — atualizado em 2026-07-20T13:01:31Z
- 2026-07-22 — SMS SÃO SEBASTIÃO — 22/07/2026 — QUARTA — atualizado em 2026-07-20T13:01:30Z
- 2026-07-23 — SMS SÃO SEBASTIÃO — 23/07/2026 — QUINTA — atualizado em 2026-07-20T13:01:30Z
- 2026-07-24 — SMS SÃO SEBASTIÃO — 24/07/2026 — SEXTA — atualizado em 2026-07-20T13:01:29Z
- 2026-07-27 — SMS SÃO SEBASTIÃO — 27/07/2026 — SEGUNDA — atualizado em 2026-07-20T13:01:29Z
- 2026-07-28 — SMS SÃO SEBASTIÃO — 28/07/2026 — TERÇA — atualizado em 2026-07-20T13:01:28Z
- 2026-07-29 — SMS SÃO SEBASTIÃO — 29/07/2026 — QUARTA — atualizado em 2026-07-20T13:01:27Z
- 2026-07-30 — SMS SÃO SEBASTIÃO — 30/07/2026 — QUINTA — atualizado em 2026-07-20T13:01:27Z
- 2026-07-31 — SMS SÃO SEBASTIÃO — 31/07/2026 — SEXTA — atualizado em 2026-07-20T13:01:26Z

## Status

Sincronização verificada como OK: o calendário editorial da SMS São Sebastião está refletido no Google Calendar para as 18 entradas SMS encontradas em julho/2026, todas confirmadas e atualizadas na execução de 2026-07-20 13:01 UTC.

Observação técnica: `memory_search` estava indisponível por erro de API key de embeddings; foi feito fallback obrigatório com leitura direta, `find`/`grep`, execução do script e consulta direta à API do Google Calendar.
