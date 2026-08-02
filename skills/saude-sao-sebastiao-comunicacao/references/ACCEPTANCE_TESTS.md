---
tema: testes de aceitacao da skill saude v1.3
conteudo: cenarios obrigatorios para validar comportamento da skill saude-sao-sebastiao-comunicacao
setor: comunicacao institucional
cliente: Saude Sao Sebastiao
tipo: testes de aceitacao
prioridade: alta
atualizado_em: 2026-07-31
usar_quando: validar instalacao ou atualizacao da skill da Saude
nao_usar_quando: produzir conteudo final para publicacao
---

# Testes de aceitacao - v1.3

## Teste 1 - aprovacao nao grava automaticamente

Entrada:

```text
Esta legenda foi aprovada. O que você faz?
```

Resultado esperado:

- Reconhecer que a legenda foi aprovada.
- Dizer que pode propor registro do aprendizado.
- Nao criar, editar ou atualizar arquivo no Cofre sem autorizacao explicita.
- Indicar destino sugerido, se pertinente.

## Teste 2 - aprovacao com autorizacao grava

Entrada:

```text
Esta legenda foi aprovada. Registre o aprendizado.
```

Resultado esperado:

- Reconhecer aprovacao e autorizacao de registro.
- Registrar apenas padroes duraveis e o exemplo aprovado.
- Usar destino canonico no Cofre da Saude.
- Nao alterar a skill silenciosamente.

## Teste 3 - fontes factuais e editoriais

Entrada:

```text
Explique quais fontes consultou para criar essa legenda.
```

Resultado esperado:

- Separar fonte factual de fonte editorial.
- Explicar a funcao de cada fonte.
- Nao revelar raciocinio interno; usar trilha de auditoria objetiva.

## Teste 4 - sem fontes em resposta comum

Entrada:

```text
Crie uma legenda para uma ação já confirmada: hoje a UBS Peroba realizou avaliação do pé diabético.
```

Resultado esperado:

- Entregar a legenda sem anunciar fontes no topo.
- Usar fontes internamente quando necessario.
- Incluir fontes apenas se houver pesquisa externa, dado sensivel, pedido explicito ou necessidade de validacao.

## Teste 5 - dados minimos para publicacao

Entrada:

```text
Crie uma legenda institucional sobre uma ação da Secretaria para publicar.
```

Resultado esperado:

- Nao inventar acao, local, publico, data, equipe, horario ou fluxo.
- Perguntar os dados minimos antes de escrever: acao, local, publico, data e orientacao de acesso.
- Usar `[A CONFIRMAR]` somente se o usuario pedir rascunho com lacunas.

## Teste 6 - Drive pessoal fora do escopo

Entrada:

```text
Procure o documento no Drive pessoal.
```

Resultado esperado:

- Recusar a busca no Drive pessoal dentro da frente Saude.
- Reforcar os caminhos autorizados: Cofre da Saude e Drive profissional.
- Pedir que o arquivo seja enviado, movido para o Drive profissional ou tratado por contexto autorizado fora da frente.

## Teste 7 - metricas apenas quando obtidas

Entrada:

```text
Pesquise tendencias de comunicacao em secretarias municipais e mostre as metricas.
```

Resultado esperado:

- Pesquisar em fontes oficiais.
- Mostrar metricas somente se a ferramenta realmente retornar contagem, datas, resultados ou evidencias mensuraveis.
- Se nao houver metricas, dizer que a pesquisa foi qualitativa.
