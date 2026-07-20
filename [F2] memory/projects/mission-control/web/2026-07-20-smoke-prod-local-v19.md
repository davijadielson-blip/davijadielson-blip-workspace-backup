# Mission Control v1.9 — Smoke test de produção local

**Data:** 2026-07-20 02:49 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Contexto

Após a v1.8 com proteção de acesso para deploy privado, a próxima etapa foi preparar e validar um smoke test de produção para reduzir risco antes de publicar.

## Entrega

Foi criado um script de smoke test para validar o Mission Control rodando como produção.

## Arquivos alterados no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos:

- `scripts/smoke-test.mjs`
- `package.json`
- `DEPLOY.md`

## Scripts adicionados

```bash
npm run start:prod
npm run smoke
```

## Como testar

Servidor produção local:

```bash
PORT=4180 npm run start:prod
```

Smoke test:

```bash
MISSION_CONTROL_SMOKE_URL=http://127.0.0.1:4180 npm run smoke
```

## Validações feitas

O smoke test valida:

- `/` responde 200 e contém `Mission Control` e `CRM`.
- `/api/logika-crm` responde 200 e contém `connected` e `summary`.

## Resultado

- `npm run build`: OK.
- `PORT=4180 npm run start:prod`: OK.
- `MISSION_CONTROL_SMOKE_URL=http://127.0.0.1:4180 npm run smoke`: OK.

Saída:

```text
OK / 200
OK /api/logika-crm 200
Smoke test OK
```

## Próximo passo recomendado

Escolher provedor/ambiente de publicação e executar o mesmo smoke test na URL final.
