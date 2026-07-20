# Revisão semanal comercial Lógika — 2026-07-20

**Data/hora:** 2026-07-20 11:30 UTC  
**Origem:** cron Mission Control — revisão semanal comercial Lógika  
**Snapshot base:** `2026-07-20-snapshot-crm-logika.md`

## Resumo executivo

- Pipeline com 7 itens.
- Valor pretendido total: R$ 203.000.
- Valor fechado registrado: R$ 35.000.
- Tarefas comerciais abertas: 6.
- Leads com aging crítico: 7.
- Leads com tarefas atrasadas: 2.
- Itens de higiene CRM: 16.

## Top 3 ações comerciais da semana

1. **Guilherme — Em Negociação — R$ 32.000**
   - Resolver imediatamente a tarefa atrasada de follow-up, registrada para 2024-03-15.
   - Consolidar as 3 tarefas abertas em uma única próxima ação com prazo real.
   - Atualizar `Último Contato` após qualquer interação.

2. **Gustavo — Lead — R$ 35.000**
   - Tratar a tarefa atrasada `Enviar Proposta`, registrada para 2024-03-29.
   - Decidir se ainda é lead ativo; se sim, enviar proposta/follow-up e criar próximo passo com data.
   - Se não houver fit ou prioridade, pausar/arquivar para reduzir ruído.

3. **Kim Wayn — Proposta Enviada — R$ 37.000**
   - Enviar follow-up consultivo sobre a proposta.
   - Remover duplicidade: existem 2 tarefas `Follow Up` sem data.
   - Definir uma única próxima ação com prazo de até 2 dias úteis.

## Tarefas atrasadas

1. **Guilherme — Follow Up — 2024-03-15**
   - 857 dias de atraso.
   - Criticidade: alta por estar em negociação e com 3 tarefas abertas.

2. **Gustavo — Enviar Proposta — 2024-03-29**
   - 843 dias de atraso.
   - Criticidade: alta por valor pretendido de R$ 35.000 e ausência de cadência recente.

## Higiene CRM

Principais problemas identificados:

- 16 itens de higiene no total.
- 7 leads com aging crítico.
- 6 tarefas abertas; 4 estão sem data.
- Registro `test` aparenta ser teste e está sem telefone/e-mail.
- Gilberto está sem telefone/e-mail.
- Contatos antigos: test, Jonathan, Guilherme, Kim Wayn, Gilberto, João e Gustavo.
- João está fechado, mas aparece com contato antigo; recomenda-se validar se precisa permanecer no aging comercial ou ser tratado separadamente como cliente/fechado.

## Recomendação da semana

Priorizar receita e reduzir ruído em paralelo:

1. Fazer follow-up/reagendamento de **Guilherme**, **Gustavo** e **Kim Wayn** nesta ordem.
2. Corrigir tarefas sem data e duplicidades, especialmente em Guilherme e Kim Wayn.
3. Limpar ou arquivar `test` e completar/reclassificar Gilberto.
4. Atualizar `Último Contato` somente após interação real.
5. Meta mínima até sexta: 3 follow-ups enviados, 4 tarefas sem data corrigidas, 2 atrasadas resolvidas/reagendadas e novo snapshot salvo.

## Fontes

- Cofre: `CONSTITUICAO.md`.
- Cofre: `[F2] memory/projects/mission-control/logika-crm/2026-07-20-rotina-semanal-comercial-v16.md`.
- Cofre: `[F2] memory/outputs/logika/crm/2026-07-20-snapshot-crm-logika.md`.
- Ferramenta específica: `npm run snapshot:crm` em `/data/.openclaw/mission-control-next`.
