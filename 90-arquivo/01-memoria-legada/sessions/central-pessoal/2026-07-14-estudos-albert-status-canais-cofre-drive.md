---
tema: 07 14 estudos albert status canais cofre drive
atualizado_em: 2026-07-22
---

# ESTUDOS / Albert — status de canais de armazenamento no Cofre e Drive

**Data:** 2026-07-14
**Pedido:** Jadielson perguntou se já existem canais criados no Cofre e no Drive para armazenar o que for pertinente ao aprendizado.

## Verificação realizada
- Cofre consultado: `AGENTS.md`, `MAPA.md`, `SOUL.md`, `USER.md`, `[F1] ESTUDOS/COCKPIT.md`, `[F2] memory/agents/central-pessoal/albert-estudos.md`, `[F2] memory/context/estudos/backlog-cursos-ativos.md`.
- Busca semântica indisponível por erro de embeddings/API key; foi usado fallback por leitura direta, `find` e `grep`.
- Drive pessoal verificado via `gog` OAuth direto/readonly.

## Resultado
Sim, já existem estruturas principais:

### Cofre
- `[F1] ESTUDOS/` com status: `A INICIAR`, `EM ANDAMENTO`, `CONCLUÍDO`, `PAUSADO` e `DESCARTADO`, além de `COCKPIT.md`.
- `[F1] 2-Literatura/` para leituras, cursos concluídos/anotações e planos de estudos.
- `[F2] memory/context/estudos/` para contexto operacional de estudos.
- `[F2] memory/projects/estudos/` para memória de projetos de aprendizagem.
- `[F2] memory/agents/central-pessoal/albert-estudos.md` define Albert como tutor/organizador de estudos.

### Google Drive pessoal
- Pasta raiz `ESTUDOS` confirmada em `davijadielson@gmail.com` via inventário live (`gog_drive pessoal inventory`).
- Inventário anterior registrou pelo menos 2.086 itens relacionados a estudos/cursos, com pasta `ESTUDOS` e subpastas/itens como `CURSOS` e `EBOOKs`.

## Observação operacional
O Drive está configurado principalmente como repositório de arquivos/material bruto. O Cofre deve ser a fonte de verdade para sínteses, planos, notas, checklists, decisões e progresso de aprendizagem.

## Atualização — autorização de protocolo para cursos sem pasta no Drive
Jadielson autorizou/solicitou que cursos que ainda não tiverem pasta no Drive recebam pasta própria e que os brutos sejam salvos lá. Regra registrada em `[F2] memory/context/estudos/protocolo-drive-brutos-cursos.md`.

Bloqueio/atenção: contexto atual do Drive pessoal está registrado como `Drive(readonly)`. Para criação/upload real no Drive, pode ser necessária reautorização com escopo de escrita ou encaminhamento para Alfred/Lôh.

## Confirmação — pasta macro no Drive
Jadielson confirmou que a pasta macro para armazenar brutos de cursos/aprendizados no Drive deve ser exatamente `ESTUDOS`. Regra atualizada no protocolo de estudos.

## Encerramento da decisão
Jadielson confirmou: “OK. SALVE TUDO. OBG”.

### Decisão consolidada
- A pasta macro oficial no Google Drive pessoal para brutos de aprendizado é `ESTUDOS`.
- Cursos sem pasta devem receber uma pasta própria dentro de `ESTUDOS`.
- Arquivos brutos ficam no Drive.
- Sínteses, planos, checklists, progresso e revisões ficam no Cofre.
- Essa regra deve orientar o Albert e demais agentes que atuarem em estudos/aprendizagem.
