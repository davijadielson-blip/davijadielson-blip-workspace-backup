# Mission Control Web MVP v0.3 — Dados espelhados do Cofre

**Data:** 2026-07-20 00:16 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** Implementado e testado

## Pedido

Jadielson autorizou avançar após a versão Next.js modular v0.2.

## Entrega

Foi criada a primeira camada de **espelhamento de dados do Cofre para o app Next.js**.

## Implementação

No app:

`/data/.openclaw/mission-control-next/`

foram adicionados/alterados:

- `scripts/sync-cofre-data.mjs` — lê arquivos `.md` do Cofre e gera dados para o app.
- `lib/missionData.generated.js` — arquivo gerado automaticamente com dados espelhados.
- `app/page.jsx` — passou a consumir `missionData.generated`.
- `package.json` — ganhou script `npm run sync`.

## Fontes espelhadas

- `[F2] memory/projects/mission-control/placar-semanal-execucao.md`
- `[F2] memory/visualizations/dashboards/mission-control.md`
- `[F2] memory/projects/mission-control/backlog-mission-control.md`
- `[F2] memory/projects/mission-control/web/wireframe-dashboard-web-v01.md`
- artefatos operacionais do Mission Control

## Resultado do sync

`npm run sync` gerou dados com **15 cards** extraídos/espelhados do placar semanal.

## Testes realizados

- `npm run sync`: OK.
- `npm run build`: OK.
- servidor dev local: OK.
- teste HTTP em `http://127.0.0.1:4174`: OK.

Validações no HTML:

- Mission Control;
- Operacional v0.3;
- LOG-002;
- backlog-mission-control.md.

## Segurança / dependências

Foi executado `npm audit --json`.

Resultado:

- 2 vulnerabilidades moderadas;
- origem: `postcss` via `next`;
- correção sugerida pelo npm envolve downgrade/mudança major para `next@9.3.3`, inadequado para este app.

Decisão técnica: **não aplicar correção automática/forçada**. Registrar para revisão antes do deploy.

## Próximos passos recomendados

1. Modelar e integrar CRM Notion.
2. Melhorar parser dos Markdown do Cofre para cobrir mais seções.
3. Transformar links de fontes em navegação útil/segura.
4. Preparar deploy privado/público controlado.
