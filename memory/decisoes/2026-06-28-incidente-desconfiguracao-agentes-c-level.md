# Incidente — Desconfiguração recorrente dos agentes C-Level

**Data:** 2026-06-28
**Solicitante:** Jadielson Davi
**Responsável:** Lôh

## Problema
Jadielson reportou recorrência de agentes C-Level aparecendo como não configurados/invocáveis, afetando produção e exigindo retrabalho.

## Diagnóstico
A causa não é mais confusão de diretórios do Cofre. O Cofre padrão está consolidado em `/data/.openclaw/workspace/`.

A falha está na camada de configuração viva do OpenClaw, fora do Cofre:

- Arquivo crítico: `/data/.openclaw/openclaw.json`
- Sintoma: IDs dos agentes existem/ficam allowlisted, mas entradas completas em `agents.list` somem ou ficam incompletas, então aparecem como `configured:false`.
- Registro anterior em `memory/2026-06-26.md` indicava que o arquivo tinha sido blindado com `chmod 400`.
- Em 2026-06-28, a blindagem não estava mais ativa: o arquivo estava `rw-------`, permitindo sobrescrita posterior.

## Correção aplicada
- Recriadas/configuradas entradas completas para CMO, COO, CCO, CTO, CFO e CIO em `/data/.openclaw/openclaw.json`.
- Gateway reiniciado para carregar as entradas.
- Validação por `agents_list`: agentes aparecem como `configured:true`.
- Criado verificador: `/data/.openclaw/workspace/ops/verify-c-level-agents.sh`.
- Reaplicada blindagem no arquivo crítico: `chmod 400 /data/.openclaw/openclaw.json`.

## Prevenção recomendada
1. Nunca editar `/data/.openclaw/openclaw.json` diretamente sem antes destravar e registrar motivo.
2. Antes de qualquer mudança de config, rodar `ops/verify-c-level-agents.sh`.
3. Após qualquer restart/update/config.patch, rodar `agents_list` e verificar C-Levels.
4. Criar monitor recorrente/cron para validar C-Levels e alertar Lôh/Jadielson se algum voltar a `configured:false`.
5. Manter este incidente como referência operacional até estabilização definitiva.

## Estado após contenção
C-Level prioritários para o projeto Entre Tempos:

- CMO: configurado
- COO: configurado
- CCO: configurado

Demais C-Levels também restaurados:

- CTO: configurado
- CFO: configurado
- CIO: configurado


---

## Fechamento operacional — 2026-06-28 03:39 UTC

Jadielson solicitou: "ok. salve tudo."

Foi registrado no diário `memory/2026-06-28.md` o resumo completo do incidente, diagnóstico, correção, prevenção e estado final.

### Evidências finais
- Verificador criado: `/data/.openclaw/workspace/ops/verify-c-level-agents.sh`
- Configuração crítica travada: `/data/.openclaw/openclaw.json` em modo `400`
- Monitor recorrente criado: `guard-c-level-agents-config` a cada 30 minutos
- Pareceres salvos:
  - `[F3] PROJETOS/PAUSADO/ENTRE TEMPOS/6-entregas/parecer-cmo-lancamento-entre-tempos.md`
  - `[F3] PROJETOS/PAUSADO/ENTRE TEMPOS/6-entregas/parecer-coo-lancamento-entre-tempos.md`
  - `[F3] PROJETOS/PAUSADO/ENTRE TEMPOS/6-entregas/parecer-cco-lancamento-entre-tempos.md`

