---
data: 2026-07-14
status: vigente
decisor: Jadielson Davi
assunto: Remoção dos MCPs Google via Zapier e padronização do gog
---

# Decisão — Google via Zapier removido; `gog` é o caminho oficial

## Decisão

Jadielson determinou que os acessos Google não devem mais ser feitos por Zapier/MCP. O caminho oficial para Google é o **`gog`**.

## Ações executadas

Foram desabilitadas as ações Google nos servidores Zapier disponíveis:

- Google Drive removido do Zapier principal.
- Google Drive removido do Zapier secundário.
- Google Sheets removido do Zapier secundário.
- Google Calendar removido do Zapier secundário.
- Google Drive removido do Zapier YouTube.

Estado após verificação:

- Zapier principal: permanece apenas Notion habilitado.
- Zapier secundário: nenhum app habilitado.
- Zapier YouTube: nenhum app habilitado.

## Regra operacional para todos os agentes

1. Para Google Drive, Google Calendar, Gmail e Google Sheets, usar **`gog`** ou scripts diretos já existentes no Cofre.
2. Não habilitar Google novamente no Zapier sem autorização explícita de Jadielson/Lôh.
3. Não sugerir Zapier como primeira alternativa para Google.
4. Se `gog` falhar, diagnosticar `gog`, OAuth, escopos ou scripts locais antes de cogitar outra integração.
5. Zapier pode permanecer para apps não-Google quando não houver alternativa melhor e quando estiver explicitamente habilitado.

## Referências

- Contexto técnico: `[F2] memory/context/integracoes/google_drive_jadielson.md`
- Migração original: `[F2] memory/context/decisoes/2026-07-07-migracao-zapier-para-gog.md`
- Política long-term: `MEMORY.md`
