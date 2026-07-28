---
tipo: resumo_sessao_financeira
data: 2026-07-15
agente: Warren
escopo: finanças pessoais
origem: Telegram Central Pessoal / My Finance
---

# Resumo salvo — ajustes de contas, cartão, mercado e cron mensal

## Contexto

Sessão no tópico My Finance com Jadielson para revisar pendências de julho/2026, atualizar cartão, mercado e configurar lembrete/relatório mensal de contas para a esposa pagar/confirmar.

## Atualizações principais realizadas

1. **Água mineral**
   - Despesa de R$ 36,00 marcada como paga.

2. **Escola Eloah**
   - Jadielson decidiu deixar para pagar/regularizar no próximo mês.
   - Na planilha, marcada como `ADIADO PARA PRÓXIMO MÊS`.

3. **Prestação da moto**
   - Retirada da lista de pendências pessoais do mês porque a esposa está pagando diretamente.

4. **Cartão/Nubank julho**
   - Fatura inicialmente identificada por imagem com referência de R$ 612,31.
   - Jadielson corrigiu: foi pago R$ 413,71.
   - Na planilha, julho ficou como `PAGO`, valor R$ 413,71, vencimento fixo dia 09, pago em 10/07/2026.

5. **Vencimento fixo do cartão**
   - Regra registrada: fatura do cartão/Nubank vence sempre no dia 09 de cada mês.

6. **Fatura parcial de agosto**
   - Imagem registrada como fatura parcial do próximo mês.
   - Parcial visível considerada para agosto/2026: R$ 244,55.
   - Vencimento: 09/08/2026.
   - Status: `PARCIAL / PRÓXIMO MÊS`.

7. **Mercado / Hopernatacha**
   - Jadielson esclareceu que `Quiteria de Almeida Santos LTDA` é razão social de um mercado — Hopernatacha.
   - Item de R$ 126,10 reclassificado como `MERCADO / Alimentação`, status pago.

8. **Compra de mercado no crédito**
   - Cupom enviado por Jadielson.
   - Data: 10/07/2026.
   - Valor no cartão: R$ 435,14.
   - Forma: cartão TEF/crédito, SafraPay Master parcialmente visível.
   - Status na planilha: `NO CARTÃO / A CONCILIAR` para evitar duplicidade ao pagar fatura.
   - Controle de mercado/alimentação de julho ajustado para realizado aproximado de R$ 1.232,81, cerca de R$ 232,81 acima do teto de referência de R$ 1.000,00.

9. **Combustível**
   - Mantido como `A LEVANTAR`, pois Jadielson verá depois.

10. **Cron mensal de relatório de contas para esposa pagar**
   - Criado job: `55801eae-7ea5-4628-9382-d7c1a0055aaf`.
   - Nome: `WARREN — Relatório mensal de contas para esposa pagar`.
   - Horário: 08h America/Maceio.
   - Agenda: `0 8 28-31 * *` com checagem interna para só gerar relatório no último dia real do mês.
   - Destino: Telegram Central Pessoal / tópico My Finance.
   - Foco: mensagem copiável para Jadielson enviar à esposa, com contas a pagar/confirmar.

## Arquivos/locais relacionados

- Status financeiro atualizado: `[F2] memory/context/integracoes/financeiro_status_a_quitar_2026-07-07.md`
- Cron mensal: `[F2] memory/context/central-pessoal/2026-07-15-warren-cron-relatorio-contas-mensal.md`
- Planilha: `Warren — Controle Financeiro Pessoal 2026`
- Spreadsheet ID: `1HS9w4c04l2tUlggaztNPQuk-2BYIDmaTHTI7Df0QCGs`

## Observações de segurança

- Tudo mantido no escopo de finanças pessoais.
- Não misturar com LÓGIKA/empresa.
- Nenhuma transação foi executada; apenas organização, registro, classificação e cron de relatório.
