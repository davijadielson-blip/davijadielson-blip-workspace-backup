---
tema: quarentena de client secrets em media inbound
conteudo: registro da movimentacao segura de arquivos client_secret temporarios para quarentena fora do Cofre
setor: governanca agentiva
cliente: Jadielson Davi
tipo: relatorio de seguranca
prioridade: alta
atualizado_em: 2026-08-09
usar_quando: auditar onde foram preservados os client secrets removidos de media/inbound
nao_usar_quando: recuperar credenciais para uso operacional sem revalidacao humana
---

# Quarentena de client secrets - 2026-08-09

## Contexto

Jadielson autorizou mover anexos temporarios sensiveis para quarentena por seguranca, desde que isso nao atrapalhasse o contexto dos agentes nem aumentasse risco de alucinacao.

## Acao executada

Foram movidos para area tecnica de quarentena, fora do Cofre versionado, dois arquivos `client_secret` encontrados em `media/inbound/`.

## Origem

- `media/inbound/openclaw-staged-057d2968-7281-483e-9642-dd25be13158d/client_secret_814986081043_8gjtlblvle38loa4sapdkrqkhkq9l5ef_---8ca5ec38-ba79-4ccf-91c8-b814fab6dd80.json`
- `media/inbound/openclaw-staged-437feb7a-ef85-4905-baa5-7fddb06f9672/client_secret_814986081043_8gjtlblvle38loa4sapdkrqkhkq9l5ef_---a47bb4de-eff4-4b3c-89cb-49ddc21bc207.json`

## Destino

- `/data/.openclaw/quarantine/cofre-media-inbound-client-secrets-2026-08-09/`

## Garantias

- Nenhum arquivo foi excluido definitivamente.
- A movimentacao ficou limitada aos arquivos `client_secret` temporarios.
- Demais anexos em `media/inbound/` permaneceram no lugar para nao quebrar referencias operacionais ainda nao revisadas.
- O Cofre preserva este registro textual para continuidade dos agentes.

## Proximo passo recomendado

Rotacionar ou revogar esses client secrets no Google Cloud quando houver janela segura, e manter o acesso Google oficial pelo `gog` com segredos fora do Git.
