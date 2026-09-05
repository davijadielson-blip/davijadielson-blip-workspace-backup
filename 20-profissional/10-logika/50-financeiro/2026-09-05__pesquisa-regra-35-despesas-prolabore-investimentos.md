---
tema: pesquisa sobre regra de 35 por cento de despesas com pro-labore
conteudo: analise CFO sobre a recomendacao de manter despesas da empresa, incluindo pro-labore, ate 35 por cento do faturamento e deixar o restante em caixa/investimentos
setor: Logika Solucoes Digitais
cliente: LÓGIKA
tipo: pesquisa financeira
prioridade: alta
atualizado_em: 2026-09-05
usar_quando: definir teto percentual de despesas, pro-labore, caixa e investimento da Logika
nao_usar_quando: substituir orientacao contabil formal ou decisao de retirada sem validacao de Jadielson
---

# Pesquisa CFO - regra de 35% para despesas + pro-labore

## Pergunta

Jadielson relatou ter participado de curso em que recomendavam que todas as despesas da empresa, ja incluindo pro-labores, nao deveriam passar de **35% do faturamento**, deixando o restante no caixa da empresa para investimentos.

## Veredito CFO

A regra **procede como disciplina financeira agressiva**, mas nao como padrao universal.

Ela parece alinhada a modelos de caixa como o **Profit First**, que recomenda separar o faturamento em contas/caixinhas antes de gastar. Porem, nas referencias pesquisadas, a divisao geralmente separa:

- lucro;
- pro-labore/retirada do dono;
- impostos;
- despesas operacionais;
- reservas/investimentos.

Ou seja: **35% costuma aparecer como limite de despesas operacionais ou overhead**, nao necessariamente como "todas as despesas + pro-labore".

## Referencias externas consultadas

- Business Queensland: ponto de equilibrio ocorre quando receita cobre despesas operacionais e custo dos servicos; recomenda incluir salario/retirada do dono nas despesas e monitorar percentuais por categoria.
- Relay/Profit First: para negocios com receita real ate US$ 250 mil/ano, a grade inicial citada e aproximadamente 5% lucro, 50% pagamento do dono, 15% impostos e 30% despesas operacionais; em faixas maiores, despesas operacionais podem ir a 40%, 50% ou 65%.
- NetSuite: percentual de folha varia muito por setor; muitos negocios operam com 15% a 30% de folha, mas servicos intensivos em trabalho podem chegar a percentuais maiores.
- U.S. Chamber/CO: nao ha regra fixa para pagamento do dono; negocios pequenos de servico costumam definir retirada com base em fluxo de caixa livre e necessidade de reinvestimento.
- Damodaran/Stern: margens variam bastante por setor; advertising aparece com margem operacional e liquida muito diferentes, reforcando que nao ha percentual unico universal.

## Aplicacao na Logika

Dados atuais do Cofre:

- Receita recorrente atual: **R$ 1.700,00/mês**
- Base fixa estrutural: **R$ 1.637,53/mês**
- Base operacional minima conhecida, incluindo designer: **R$ 1.787,53/mês**
- Pro-labore minimo desejado: **10% do faturamento**

Se a Logika quiser aplicar literalmente a regra "despesas + pro-labore <= 35%", usando a base operacional minima conhecida:

```text
Base operacional + 10% do faturamento <= 35% do faturamento
R$ 1.787,53 <= 25% do faturamento
Faturamento minimo aproximado = R$ 7.150,12/mês
```

Se considerar somente a base fixa estrutural:

```text
R$ 1.637,53 <= 25% do faturamento
Faturamento minimo aproximado = R$ 6.550,12/mês
```

## Recomendacao CFO para a Logika

Usar a regra dos 35% como **meta de maturidade**, nao como regra imediata.

Para a fase atual, recomenda-se uma escada:

1. **Fase 1 - sobrevivencia organizada:** despesas + pro-labore ate 75% do faturamento.
2. **Fase 2 - controle saudavel:** despesas + pro-labore ate 60% do faturamento.
3. **Fase 3 - empresa forte:** despesas + pro-labore ate 45% do faturamento.
4. **Fase 4 - alto caixa/investimento:** despesas + pro-labore ate 35% do faturamento.

Meta pratica atual:

- Curto prazo: buscar pelo menos **R$ 2.800,00/mês** de recorrencia.
- Meta saudavel: buscar **R$ 3.200,00 a R$ 3.800,00/mês**.
- Meta de alta disciplina 35%: mirar **R$ 6.500,00 a R$ 7.200,00/mês**, antes de tratar essa regra como obrigatoria.

## Fontes

- Cofre: `DESPESAS FIXOS - mensais.md`, `DESPESAS Variáveis - mensais.md`, `RECEITAS.md`, `2026-09-04__meta-faturamento-superavit-prolabore-10.md`.
- Business Queensland: https://www.business.qld.gov.au/running-business/finance/essentials/break-even-profit
- Relay/Profit First: https://relayfi.com/blog/profit-first-accounts/
- NetSuite: https://www.netsuite.com/portal/resource/articles/financial-management/small-business-payroll-percentage.shtml
- U.S. Chamber/CO: https://www.uschamber.com/co/run/finance/how-to-calculate-business-owners-salary
- Damodaran/Stern: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/margin.html
