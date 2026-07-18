# Boleto a pagar — Hotmart/EBANX — curso/capacitação

- **Registro:** 2026-07-18 16:27 UTC
- **Origem:** Telegram LÓGIKA — tópico 1466 `CFO - Finanças & Caixa`
- **Solicitação de Jadielson:** guardar, lembrar de pagar na data e incluir como despesa temporária da empresa por se tratar de curso/capacitação em andamento.
- **Classificação:** LÓGIKA / Financeiro / Despesa temporária da empresa / Curso-capacitação.
- **Status:** PENDENTE / A PAGAR
- **Vencimento:** 2026-07-23
- **Valor:** R$ 112,34
- **Beneficiário:** EBANX Pagamentos LTDA.
- **Sacador/Avalista / estabelecimento:** Hotmart
- **Data do documento/processamento:** 2026-07-18
- **Número do documento:** 173288398
- **Carteira:** 109
- **Nosso número/código do documento:** 109/73288398-4
- **Linha digitável:** 34191.09735 28839.840544 89356.830003 6 15160000011234
- **Arquivo local:** `[F2] memory/inbox-externa/financeiro/empresa/2026/07-Julho/02-Boletos-a-pagar/2026-07-18__BOLETO-HOTMART-EBANX__curso-capacitacao__R-112-34__vence-2026-07-23__PENDENTE.pdf`

## Observações operacionais

- Não marcar como recorrência fixa ainda. Tratar como **despesa temporária/variável de capacitação**, com acompanhamento enquanto Jadielson estiver fazendo cursos.
- Lembrar Jadielson no dia do vencimento para pagamento.
- Após pagamento, anexar comprovante e mudar status para **PAGO** no controle financeiro.
- Dados pessoais do pagador existem no boleto; evitar expor em mensagens públicas.

## Registro externo executado

- **Drive LÓGIKA:** enviado para `03_FINANCEIRO_EMPRESA/03_COMPROVANTES_NF/COMPROVANTES/2026/07-Julho/02-Boletos-a-pagar`.
- **Drive ID:** `1Nhz-ruQ8KWhvkRRD-jeW7TlkbPW4Yld0`
- **Drive link:** https://drive.google.com/file/d/1Nhz-ruQ8KWhvkRRD-jeW7TlkbPW4Yld0/view?usp=drivesdk
- **Planilha:** `Receitas e Despesas — LÓGIKA` / aba `Lancamentos` / linha `A3:N3`.
- **ID do lançamento:** `LOG-DESP-TEMP-20260718-HOTMART`

## Lembrete agendado

- **Cron job:** `a1cc11b4-b939-4a26-a94c-9ccea8911664`
- **Quando:** 2026-07-23 09:00 BRT (12:00 UTC)
- **Canal/tópico:** Telegram LÓGIKA / tópico 1466 `CFO - Finanças & Caixa`

## Atualização — parcelamento informado por Jadielson em 2026-07-18 16:40 UTC

Jadielson corrigiu/complementou a condição de pagamento:

- Este boleto de **R$ 112,34**, vencimento **2026-07-23**, é a **parcela 1/11** mensal.
- Existem **mais 10 parcelas mensais** no mesmo valor informado no boleto atual, com vencimento no mesmo dia do mês (**dia 23**), salvo novo boleto/valor diferente enviado depois.
- Além dessas parcelas mensais, houve uma **entrada no ato da aquisição**. Valor/data exatos da entrada ainda precisam ser confirmados por Jadielson ou por comprovante; registrar sem contaminar totais até confirmação.
- Classificação mantida: **LÓGIKA / Financeiro / Despesa temporária da empresa / Curso-capacitação**.

### Cronograma provisório registrado

| Parcela | Vencimento | Valor | Status |
|---:|---|---:|---|
| Entrada | ato da aquisição | valor a confirmar | INFORMADA / A CONFIRMAR |
| 1/11 | 2026-07-23 | R$ 112,34 | PENDENTE |
| 2/11 | 2026-08-23 | R$ 112,34 | PREVISTO |
| 3/11 | 2026-09-23 | R$ 112,34 | PREVISTO |
| 4/11 | 2026-10-23 | R$ 112,34 | PREVISTO |
| 5/11 | 2026-11-23 | R$ 112,34 | PREVISTO |
| 6/11 | 2026-12-23 | R$ 112,34 | PREVISTO |
| 7/11 | 2027-01-23 | R$ 112,34 | PREVISTO |
| 8/11 | 2027-02-23 | R$ 112,34 | PREVISTO |
| 9/11 | 2027-03-23 | R$ 112,34 | PREVISTO |
| 10/11 | 2027-04-23 | R$ 112,34 | PREVISTO |
| 11/11 | 2027-05-23 | R$ 112,34 | PREVISTO |

**Total das 11 parcelas mensais:** R$ 1.235,74.  
**Total geral com entrada:** R$ 1.235,74 + valor da entrada a confirmar.

Próxima ação: quando Jadielson enviar comprovante/valor da entrada, registrar como pago/histórico; quando cada parcela for paga, anexar comprovante e baixar a respectiva linha.

## Registro operacional executado após atualização do parcelamento

- Planilha `Receitas e Despesas — LÓGIKA` atualizada:
  - Linha original ajustada para **parcela 1/11**.
  - Linhas futuras adicionadas para parcelas **2/11 a 11/11**.
  - Linha informativa criada para **entrada no ato da aquisição — valor a confirmar**, com valor R$ 0,00 apenas para não contaminar total financeiro até confirmação.
- Lembretes mensais criados para todo dia 23, 09:00 BRT, de 2026-07-23 a 2027-05-23.

### IDs dos lembretes

| Parcela | Vencimento | Cron job |
|---:|---|---|
| 1/11 | 2026-07-23 | `a1cc11b4-b939-4a26-a94c-9ccea8911664` |
| 2/11 | 2026-08-23 | `b61920ac-cb68-4862-9957-17e4dd14d2f1` |
| 3/11 | 2026-09-23 | `47738fa5-8a8a-44c5-8b51-0d2053564761` |
| 4/11 | 2026-10-23 | `2b5fadd6-3cfb-4284-969f-a8c7dd6953cc` |
| 5/11 | 2026-11-23 | `1d8cfdcb-6c57-4cd3-953c-741710701646` |
| 6/11 | 2026-12-23 | `739efb8e-f488-423a-8d14-d55b20ae8e4a` |
| 7/11 | 2027-01-23 | `2dfe0b08-5c93-4454-aa88-ce81df499d00` |
| 8/11 | 2027-02-23 | `81bfe8e1-4fd9-4909-af9f-e804fe745e1b` |
| 9/11 | 2027-03-23 | `04fb84f0-1e00-4463-b216-076bc50a5bc2` |
| 10/11 | 2027-04-23 | `29b1fa35-b003-4659-b7f4-da26ea75f0fd` |
| 11/11 | 2027-05-23 | `f7199f9d-692c-4e8c-8894-3157a44732c9` |
