---
tipo: configuracao_cron_financeiro
data: 2026-07-15
agente: Warren
escopo: finanças pessoais
origem: Telegram Central Pessoal / My Finance
---

# Cron — relatório mensal de contas para esposa pagar

Jadielson perguntou se existia cron para rodar o relatório das contas que devem ser pagas do mês corrente. Também reforçou que o mais importante é o envio/uso para a esposa pagar/organizar as contas.

## Verificação

- Lista de cron jobs ativos/inativos consultada via ferramenta `cron list`.
- Busca no Cofre por registros de cron/relatório/contas a pagar.
- Resultado: não havia cron específico do Warren/My Finance para relatório mensal de contas a pagar no último dia do mês.

## Configuração criada

- **Nome:** WARREN — Relatório mensal de contas para esposa pagar
- **Job ID:** `55801eae-7ea5-4628-9382-d7c1a0055aaf`
- **Agente:** `my-finance`
- **Destino:** Telegram grupo `Central Pessoal`, tópico `My Finance` (`threadId: 12`)
- **Horário:** 08h, fuso `America/Maceio`
- **Agenda:** `0 8 28-31 * *`
- **Regra de último dia:** o job roda entre os dias 28 e 31, mas o prompt manda calcular a data local e só gerar relatório se for o último dia real do mês. Assim cobre fevereiro 28/29, meses de 30 e 31.
- **Próxima execução prevista pelo scheduler:** `2026-07-28 08:00 America/Maceio` aproximadamente, mas só deve gerar relatório de fato no último dia do mês.

## Conteúdo do relatório

Quando for o último dia real do mês, o Warren deve gerar:
1. Relatório das contas do mês corrente.
2. Resumo: pagas, pendentes, parciais, adiadas e a levantar.
3. Bloco principal: **Mensagem para enviar à esposa**, em formato copiável, com contas que ela precisa pagar/confirmar, valores e observações.
4. Bloco interno de controle do Warren: cartão, combustível, contas adiadas e demais itens a levantar.
5. Rodapé de fonte: Cofre financeiro pessoal e Google Sheets.

## Fontes obrigatórias do job

- Cofre: `/data/.openclaw/workspace/`
- Planilha: `Warren — Controle Financeiro Pessoal 2026`
- Spreadsheet ID: `1HS9w4c04l2tUlggaztNPQuk-2BYIDmaTHTI7Df0QCGs`
- Arquivos principais:
  - `[F1] 4-Pessoal/Financas/05-Planos/PLANO_REPASSE_ESPOSA_CONTAS_PESSOAIS_2026-07-06.md`
  - `[F2] memory/context/integracoes/financeiro_status_a_quitar_2026-07-07.md`
  - Aba `Contas a pagar` da planilha.

## Observação

O job não executa pagamentos nem transações. Ele apenas organiza o relatório e entrega no tópico My Finance para Jadielson usar/encaminhar.
