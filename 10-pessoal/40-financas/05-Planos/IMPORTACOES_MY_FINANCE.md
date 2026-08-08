---
tema: IMPORTACOES MY FINANCE
atualizado_em: 2026-08-01
---

# Importações My Finance

Registro de dados enviados por Jadielson no tópico My Finance e transformados em resumo seguro por Warren.

## 2026-08-08 — Comprovante: remédio para resfriado — upload pendente

- Arquivo local preservado: `70-agentes/runtime/central-pessoal/media/inbound/openclaw-staged-2ae8fd20-41f3-4ed1-9e76-020506e95974/Comprovante_2026-08-08_013222---3863b466-ac1d-46df-8f62-ec989d781455.pdf`
- Valor: **R$ 20,00**.
- Pagamento: Pix efetivado em **06/08/2026 às 19:19:05**.
- Descrição informada: **remédio para resfriado**; categoria provisória Saúde/Farmácia.
- ID da transação Pix: `E0036030520260806221872d437b6df3`.
- Destino pretendido: Drive pessoal > FINANCEIRO > comprovantes pessoais.
- **Status: NÃO CONCLUÍDO — sem ID de arquivo do Drive.**
- Erro técnico em 2026-08-08 08:08 UTC: `gog auth doctor --check` identificou falha `aes.KeyUnwrap(): integrity check failed` para os tokens OAuth; 0 tokens legíveis. O `GOG_KEYRING_PASSWORD` está definido, mas não corresponde às credenciais criptografadas armazenadas.
- Nova tentativa em 2026-08-08 08:23 UTC: falha persistente no `gog auth doctor --check`; 0 tokens legíveis e o Drive não pôde ser consultado. Nenhum upload foi iniciado; portanto, não existe ID nem link.
- Nova tentativa em 2026-08-08 09:51 UTC: falha persistente no `gog auth doctor --check`; 0 tokens OAuth legíveis (`aes.KeyUnwrap(): integrity check failed`). O upload não foi iniciado.
- Nova tentativa em 2026-08-08 10:10 UTC: falha persistente no `gog auth doctor --check`; as três contas continuam sem tokens legíveis. O upload não foi iniciado.
- Ação: não repetir upload mutável indiscriminadamente; aguardar correção/reautorização efetiva do keyring por Alfred/LÔH. Não lançar a despesa no controle sem confirmação explícita.

## 2026-08-01 — Comprovante: abastecimento carro

Arquivo de destino atualizado: `02-Despesas/DESPESAS_VARIAVEIS_E_CONTROLE.md`

Resumo extraído do comprovante Caixa e da observação de Jadielson:

- Descrição: **abastecimento carro**.
- Valor pago: **R$ 292,73**.
- Pagamento realizado via **Pix** em **01/08/2026**, às **11:37:48**.
- Recebedor: **Auto Posto Avenida**.
- CNPJ do recebedor: **18.990.675/0001-90**.
- Instituição do recebedor: **Itaú Unibanco S.A.**
- ID da transação: **E00360305202608011437cc5e686ab47**.
- Desconto informado por Jadielson: **R$ 47,00**, já abatido do total por promoção da seguradora **Estrela Brasil**.
- Valor antes do desconto: **R$ 339,73**.
- Destino correto do comprovante: **Drive pessoal > FINANCEIRO > comprovantes pessoais**.
- Status técnico: envio ao Drive pendente neste runtime. Após correção de Jadielson, foi confirmado que o binário `gog` existe em `/home/linuxbrew/.linuxbrew/Cellar/gogcli/0.21.0/bin/gog`, mas este agente ainda não enxerga credenciais/tokens em `/data/.local/share/gogcli`; PDF movido para área técnica temporária fora do Cofre em `/data/.openclaw/tmp/financeiro-pendente-upload/2026-08/2026-08-01__AUTO-POSTO-AVENIDA__abastecimento-carro__R-292-73__desconto-estrela-brasil-47-00.pdf`.
- Regra vigente: no Cofre fica apenas `.md`; demais arquivos ficam no Drive pessoal.

## 2026-07-30 — Comprovante: segunda parcela do IPVA

Arquivo de destino atualizado: `03-Dividas-e-Passivos/DIVIDAS_E_PASSIVOS.md`

Resumo extraído do comprovante Caixa:

- Descrição: **segunda parcela IPVA carro**.
- Valor: **R$ 111,17**.
- Pagamento realizado em **30/07/2026**, às **14:28**.
- Convênio: **Secretaria da Fazenda**.
- Data de vencimento e débito: **30/07/2026**.
- Destino correto do comprovante: **Drive pessoal > FINANCEIRO > comprovantes pessoais**.
- Status técnico: envio ao Drive pendente neste runtime. O binário `gog` foi localizado posteriormente, mas este agente ainda não enxerga credenciais/tokens em `/data/.local/share/gogcli`; PDF mantido fora do Cofre em área técnica temporária para posterior upload.
- Regra reforçada por Jadielson: no Cofre fica apenas `.md`; demais arquivos ficam no Drive pessoal.

## 2026-06-18 — Print: Despesas essenciais e imperdoáveis

Arquivo de destino atualizado: `02-Despesas/DESPESAS_FIXAS_PESSOAIS.md`

Resumo extraído:

- Total informado no print: **R$ 4.527,83**
- Itens: financiamento casa, luz, água, plano funeral, mercado/alimentação, prestação carro, prestação moto, escola Eloáh, seguro carro e seguro moto.
- Vencimentos: não preenchidos na captura.
- Ponto de atenção: comparar com despesas já registradas anteriormente para confirmar se internet, água mineral e plano telefônico ainda entram no orçamento pessoal.

## 2026-06-18 — Prints: Gastos Fixos e Gastos Variáveis

Arquivos de destino atualizados:

- `02-Despesas/DESPESAS_FIXAS_PESSOAIS.md`
- `02-Despesas/DESPESAS_VARIAVEIS_E_CONTROLE.md`

Resumo extraído:

- Gastos Fixos: **R$ 5.847,68** na captura, misturando lançamentos de fevereiro e março/2026.
- Gastos Variáveis: **R$ 1.381,49** na captura, misturando janeiro, fevereiro e março/2026.
- Itens em aberto destacados no print de fixos: internet e academia.
- Itens variáveis para cancelar/negociar: curso de autoajuda, curso de vendas e curso de gestão do tempo.
- Combustível aparece em aberto no cartão: R$ 480,00.

Próxima conciliação necessária: separar por mês de competência e confirmar o que é recorrente mensal versus lançamento histórico/quitado.

## 2026-06-18 — Print: Entradas

Arquivo de destino atualizado: `01-Receitas/RECEITAS_PESSOAIS.md`

Resumo extraído:

- Salário: **R$ 3.882,51**
- Pró-labore: **R$ 0,00**
- Renda extra: **R$ 0,00**
- Total da captura: **R$ 3.882,51**

Ponto de conciliação: confirmar se R$ 3.882,51 substitui o valor anterior de R$ 3.820,00 como salário líquido recorrente.

## 2026-06-18 — Print: Parcelamentos de Farmácia e Suplementos

Arquivo de destino atualizado: `03-Dividas-e-Passivos/DIVIDAS_E_PASSIVOS.md`

Resumo extraído:

- Pague Menos: R$ 350,77 em 4 parcelas de R$ 87,69.
- Pague Menos: R$ 187,83 em 4 parcelas de R$ 45,46.
- Mais Farma: R$ 109,00 em 12 parcelas de R$ 9,08.
- Pague Menos: R$ 315,92 em 7 parcelas de R$ 45,13.
- Imperium/Suplementos: R$ 105,00 em 3 parcelas de R$ 35,00.

Ponto de conciliação: confirmar saldo restante, pois o print mostra meses marcados, mas não permite fechar com segurança o que ainda está em aberto.

## 2026-06-18 — Texto: Assinaturas

Arquivo de destino atualizado: `02-Despesas/ASSINATURAS.md`

Resumo informado por Jadielson:

- Amazon Prime: R$ 169,00 anual — **cancelada**.
- iCloud: R$ 66,90 mensal — **ativa**.
- Kindle Unlimited: R$ 24,90 mensal — **cancelada**.

Impacto mensal ativo confirmado: **R$ 66,90**.

## 2026-06-18 — Texto: Dívidas principais e consignados

Arquivo de destino atualizado: `03-Dividas-e-Passivos/DIVIDAS_E_PASSIVOS.md`

Resumo informado por Jadielson:

- Banco BS2: **R$ 1.400,00**, dívida antiga de 2022.
- Consignados:
  - Valor inicial total dos empréstimos: **R$ 105.525,73**.
  - Saldo total remanescente: **R$ 164.159,92**.
  - Custo total das parcelas: **R$ 219.360,24**.
  - Impacto mensal nos descontos: **R$ 1.960,96**.
  - Salário bruto estimado: **R$ 5.295,01**.
  - Salário líquido atual com empréstimos: **R$ 3.334,05**.
  - Percentual comprometido do bruto: **37,03%**.
  - Salário líquido sem empréstimos: **R$ 5.295,01**.
- Financiamento casa: saldo restante de **R$ 63.094,83** em 12/2024.

Ponto de conciliação: confirmar divergência entre salário líquido do relatório de consignados, R$ 3.334,05, e entrada recente da captura, R$ 3.882,51.

## 2026-06-18 — Decisão: usar dados enviados até o momento como base

Arquivo de destino atualizado: `00-Painel/PAINEL_FINANCEIRO_PESSOAL.md`

Decisão de Jadielson: usar como base operacional os dados já enviados no tópico My Finance até este ponto.

Base resumida:

- Receita operacional da captura: **R$ 3.882,51**.
- Despesas essenciais/imperdoáveis da captura: **R$ 4.527,83**.
- Assinatura ativa confirmada: iCloud, **R$ 66,90/mês**.
- Dívida BS2: **R$ 1.400,00**.
- Consignados: saldo remanescente **R$ 164.159,92**, impacto mensal já descontado **R$ 1.960,96**.
- Financiamento casa: saldo restante **R$ 63.094,83** em 12/2024.

Diagnóstico inicial: base já negativa em aproximadamente **R$ 645,32** antes de variáveis, cartão e demais pendências; com iCloud, aproximadamente **R$ 712,22**.
