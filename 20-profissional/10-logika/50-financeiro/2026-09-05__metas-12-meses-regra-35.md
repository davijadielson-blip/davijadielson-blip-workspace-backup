---
tema: metas de 12 meses para regra dos 35 por cento
conteudo: plano CFO gradual para a Logika sair do deficit, pagar pro-labore minimo de 10 por cento e mirar despesas + pro-labore ate 35 por cento do faturamento em um ano
setor: Logika Solucoes Digitais
cliente: LÓGIKA
tipo: plano financeiro
prioridade: alta
atualizado_em: 2026-09-05
usar_quando: acompanhar metas mensais de faturamento recorrente, pro-labore, superavit e caixa da Logika
nao_usar_quando: substituir planejamento comercial detalhado ou autorizar novos compromissos sem validacao de Jadielson
---

# Metas CFO - 12 meses para regra dos 35%

## Ponto de partida - setembro/2026

- Receita recorrente atual: **R$ 1.700,00/mês**
- Base operacional minima conhecida:
  - Fixo estrutural: **R$ 1.637,53/mês**
  - Designer recorrente: **R$ 150,00/mês**
  - Total: **R$ 1.787,53/mês**
- Pro-labore minimo desejado: **10% do faturamento**
- Meta final desejada: **despesas + pro-labore <= 35% do faturamento**

## Formula da meta dos 35%

```text
Base operacional + pro-labore <= 35% do faturamento
R$ 1.787,53 + 10% do faturamento <= 35% do faturamento
R$ 1.787,53 <= 25% do faturamento
Faturamento alvo aproximado = R$ 7.150,12/mês
```

Meta arredondada de maturidade: **R$ 7.200,00/mês** de recorrencia.

## Regua gradual

### Marco 1 - ate 3 meses

Objetivo: sair do deficit e ficar em 0x0 operacional.

- Faturamento recorrente alvo: **R$ 1.800,00/mês**
- Receita adicional necessaria sobre hoje: **R$ 100,00/mês**
- Condicao: cobrir a base operacional minima conhecida sem depender de caixa externo.
- Pro-labore: ainda nao tratar como obrigacao cheia; se houver retirada, manter simbolica e controlada.

### Marco 2 - ate 6 meses

Objetivo: pagar pro-labore minimo de **10%** sem quebrar a base operacional.

- Faturamento recorrente alvo: **R$ 2.000,00/mês**
- Receita adicional necessaria sobre hoje: **R$ 300,00/mês**
- Pro-labore estimado: **R$ 200,00/mês**
- Leitura CFO: ainda e apertado, mas ja cria disciplina de retirada minima.

### Marco 3 - ate 9 meses

Objetivo: reduzir despesas + pro-labore para cerca de **60%** do faturamento.

- Faturamento recorrente alvo: **R$ 3.600,00/mês**
- Receita adicional necessaria sobre hoje: **R$ 1.900,00/mês**
- Pro-labore estimado: **R$ 360,00/mês**
- Despesas + pro-labore estimadas: **R$ 2.147,53/mês**
- Caixa/sobra potencial aproximada: **R$ 1.452,47/mês**
- Leitura CFO: fase de controle saudavel, com folga para investimentos temporarios.

### Marco 4 - ate 12 meses

Objetivo: bater a regra dos **35%**.

- Faturamento recorrente alvo: **R$ 7.200,00/mês**
- Receita adicional necessaria sobre hoje: **R$ 5.500,00/mês**
- Pro-labore estimado: **R$ 720,00/mês**
- Despesas + pro-labore estimadas: **R$ 2.507,53/mês**
- Percentual estimado de despesas + pro-labore: **34,83%**
- Caixa/investimento/sobra potencial: **R$ 4.692,47/mês**
- Leitura CFO: empresa em estado forte, com capacidade de investimento e reserva.

## Interpretação CFO

A meta de 35% e possivel, mas exige aumento forte de receita recorrente. A rota recomendada e nao pular etapas:

1. Primeiro estabilizar a operacao.
2. Depois instituir pro-labore minimo.
3. Em seguida criar folga real.
4. Por fim, perseguir a regra dos 35% como padrao de maturidade.

## Cuidados

- Se contratar editor fixo, secretaria ou novo colaborador recorrente, recalcular a meta dos 35%.
- Investimentos temporarios, como drone, mochila e cursos, devem ser pagos preferencialmente pela sobra/caixa de investimento.
- Novas despesas fixas so devem entrar quando houver receita recorrente correspondente.

## Monitoramento aprovado - 2026-09-05

Jadielson autorizou guardar esta regua e pediu alertas financeiros continuos.

Regra operacional:

- A cada nova despesa alimentada, o CFO deve responder com:
  - valor registrado;
  - categoria: fixo estrutural, operacional semi-fixo, investimento temporario/controlavel ou custo variavel de projeto;
  - novo impacto no caixa;
  - comparacao com a meta atual;
  - alerta se aproximar ou ultrapassar o limite da fase.
- A cada nova receita alimentada, o CFO deve responder com:
  - valor registrado;
  - se e receita recorrente ou avulsa;
  - novo total recorrente quando aplicavel;
  - distancia para as metas de 3, 6, 9 e 12 meses;
  - impacto no percentual despesas + pro-labore.
- A cada fechamento mensal, gerar balanco geral com:
  - receitas do mes;
  - despesas fixas, operacionais semi-fixas, variaveis e investimentos temporarios;
  - saldo/superavit/deficit;
  - pro-labore possivel;
  - percentual despesas + pro-labore sobre faturamento;
  - comparacao com a regua dos 35%;
  - alerta e recomendacao para o mes seguinte.

Agendamento ativo atualizado em 2026-09-05:

- Objetivo: balanco mensal no ultimo dia do mes, as **09:00**, horario de Alagoas, no topico CFO.
- `logika-cfo-balanco-mensal-31` - ID `42a7bd74-5024-4977-b968-1c65eeadf291` - meses com 31 dias.
- `logika-cfo-balanco-mensal-30` - ID `f7788566-3ae4-42ed-a85c-ace971d6d92d` - meses com 30 dias.
- `logika-cfo-balanco-mensal-fev-28` - ID `53447120-70ba-465f-803a-eecf087eca47` - fevereiro dia 28.
- `logika-cfo-balanco-mensal-fev-29` - ID `3c8b6d3b-362f-485d-b1fe-112209a2f8a5` - fevereiro dia 29 em ano bissexto.

## Fontes

- Cofre: `DESPESAS FIXOS - mensais.md`, `DESPESAS Variáveis - mensais.md`, `RECEITAS.md`, `2026-09-04__meta-faturamento-superavit-prolabore-10.md`, `2026-09-05__pesquisa-regra-35-despesas-prolabore-investimentos.md`.
