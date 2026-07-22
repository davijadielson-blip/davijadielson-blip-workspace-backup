# Decisão: Desativar lembretes automáticos no tópico Jack Lemley (PROJETOS)

**Data:** 22/07/2026
**Decidido por:** Jadielson Davi
**Executado por:** Central Pessoal (agente do tópico)

## O que foi decidido

- **❌ Desativado:** Lembretes/paautas automáticas postadas pelo `central-topic-agent` no tópico **Jack Lemley** (PROJETOS, topic_id: 1, chat_id: -1004292150901)
- **✅ Apenas Lôh** deve lembrar Jadielson sobre compromissos, pautas e tarefas
- **Regra:** Nenhum agente na Central Pessoal deve enviar lembretes proativos neste tópico

## Contexto

- O `central-topic-agent` estava postando pautas do calendário da Saúde São Sebastião neste tópico (ex: pauta do dia 22/07)
- A sessão do agente para este tópico rodou por ~3 dias e falhou (status: failed)
- Após falha da sessão, Jadielson respondeu: "desative o lembrete aqui. apenas a loh deve me lembrar"
- Não há cron jobs configurados para entregar neste tópico — os lembretes eram gerados pelo próprio agente durante a sessão contínua

## Ação tomada

1. ✅ Sessão do `central-topic-agent` para este tópico já está encerrada (failed/ended)
2. ✅ Nenhum cron job entrega neste tópico
3. ✅ Decisão registrada no Cofre
4. ✅ Jadielson notificado

## Próximos passos

- Lôh (via crons 06h e 21h) continua enviando resumos diretamente no privado de Jadielson
- **Lôh deve manter visibilidade ativa sobre PROJETOS** — Jadielson pediu para não pararem nem esquecerem de trabalhar consistentemente nos projetos
- Este tópico (Jack Lemley) permanece operacional para demandas manuais de projeto

## Complemento (22/07)

Jadielson reforçou: "se possível, só vai nos avisando, também via Lôh, quanto a este grupo de PROJETOS. para não pararmos e nem esquecermos de trabalhar consistentemente."

- ✅ Lôh já cobre PROJETOS nos resumos diários (06h e 21h) — fonte consultada: `[F3] PROJETOS/COCKPIT.md`
- ✅ Continuidade mantida via Lôh, sem necessidade de reativar lembretes automáticos no tópico

Fonte: Cofre (CONSTITUICAO.md, openclaw.json, sessão central-topic-agent)
