---
tema: limpeza tecnica de disco do OpenClaw
conteudo: registro da limpeza de caches, venv, midia inbound e backup bundle com preservacao no Drive quando aplicavel
setor: operacoes tecnicas e governanca
cliente: Jadielson Davi
tipo: relatorio operacional
prioridade: alta
atualizado_em: 2026-08-08
usar_quando: auditar liberacao de espaco em disco, localizar manifestos de Drive ou entender o que foi removido localmente
nao_usar_quando: substituir backup GitHub, Drive ou auditoria de seguranca de credenciais
---

# Limpeza tecnica de disco do OpenClaw - 2026-08-08

## Resumo

Limpeza autorizada por Jadielson em conversa direta apos diagnostico de baixo ganho de espaco na limpeza apenas do Cofre.

Resultado observado:

- Antes da limpeza tecnica: cerca de 3,0 GB livres em `/data`.
- Apos remocao de caches, venv, midia inbound e bundle antigo: cerca de 4,3 GB livres em `/data`.
- Ganho aproximado: cerca de 1,3 GB.

## Itens removidos localmente

- Caches temporarios regeneraveis em `/data/.openclaw/agents/*/agent/codex-home/.tmp`.
- Ambiente virtual regeneravel em `/data/.openclaw/workspace/scripts/.venv`.
- Cache temporario do workspace em `/data/.openclaw/workspace/.tmp`.
- `__pycache__` em `scripts/sync/__pycache__`.
- Copia local recuperavel ja enviada ao Drive em `/data/.openclaw/non-md-review/runtime-media-uploaded-20260808/`.
- Midia inbound global em `/data/.openclaw/media/inbound/`, apos upload para Drive.
- Bundle antigo `cofre-main-ahead-2-2026-07-31.bundle`, apos upload para Drive.

## Preservacao no Drive

Midia inbound global:

- Manifesto no Cofre: `memory/inbox-externa/drive/2026-08-08-limpeza-media-inbound-global.md`.
- Pasta Drive: https://drive.google.com/drive/folders/1Gq2si_EZaqsUsuouedA27bF1X_oL8YnP

Backup Git bundle antigo:

- Arquivo Drive: [1fd6oyGMvo_GLenTrHSFAAp5xjTxwtasT](https://drive.google.com/file/d/1fd6oyGMvo_GLenTrHSFAAp5xjTxwtasT/view?usp=drivesdk)
- Nome: `cofre-main-ahead-2-2026-07-31.bundle`
- Tamanho: `64066026` bytes

## Nao removido

- Memoria canonica Markdown do Cofre.
- Repositorio Git ativo do Cofre.
- Bancos SQLite ativos dos agentes.
- `node_modules`/NPM ativo do OpenClaw.
- Sessoes e logs de trajetoria.

## Observacoes

- A remocao de `scripts/.venv` pode exigir recriacao de ambiente Python se algum script antigo depender dele.
- Os caches `.tmp` dos agentes e plugins podem ser regenerados automaticamente pelo sistema.
- O ganho principal veio dos caches temporarios dos agentes, nao da limpeza de anexos do Cofre.
