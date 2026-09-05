---
tema: notion como painel visivel do cofre
conteudo: arquitetura de sincronizacao governada entre Notion MAPA 360, Cofre, Drive e Calendar
setor: operacoes tecnicas e governanca documental
cliente: Jadielson Davi
tipo: contexto-operacional
prioridade: maxima
atualizado_em: 2026-08-06
usar_quando: operar, sincronizar ou auditar o Notion MAPA 360 como painel editavel do Cofre
nao_usar_quando: buscar credenciais, tokens ou conteudo bruto de arquivos nao Markdown
---

# Notion como painel visivel do Cofre

## Decisao

Jadielson autorizou que o Notion `MAPA 360` seja usado como painel visivel e operacional do Cofre, inclusive com possibilidade de alteracoes no Notion atualizarem o Cofre automaticamente, conforme governanca abaixo.

## Arquitetura

- **Cofre**: fonte de verdade primaria para Markdown, memoria, decisoes, regras, contexto e registros canonicos.
- **Notion MAPA 360**: painel visual, operacional e editavel para gestao diaria, dashboards, databases, filtros e revisao humana.
- **Drive**: destino de arquivos nao Markdown; Notion e Cofre guardam apenas indice, resumo, link, status e proximos passos.
- **Calendar**: destino de tarefas/compromissos com data e hora reais. Notion gerencia status e contexto.

## Regra de sincronizacao

### Notion -> Cofre

Alteracoes feitas no Notion podem atualizar automaticamente o Cofre quando:

- o item for operacional;
- houver campo/caminho de origem do Cofre;
- o registro estiver marcado como apto para sincronizar;
- a alteracao nao tocar nota autoral protegida do Fluxo 1.

### Protecao do Fluxo 1

Notas autorais em `[F1]` continuam protegidas. O Notion pode exibir indice, resumo e referencias dessas notas, mas alteracoes feitas no Notion que afetem conteudo autoral devem virar item de revisao antes de serem aplicadas.

### Cofre -> Notion

O Cofre pode alimentar o Notion com:

- frentes;
- projetos;
- tarefas;
- decisoes;
- contexto operacional;
- outputs aprovados;
- indices de arquivos externos;
- registros de memoria e governanca.

## Regras praticas

- Tarefas com data/hora: Calendar para agenda real; Notion para painel de gestao.
- Tarefas sem horario: Notion como gestor visual; Cofre guarda contexto quando for relevante para continuidade.
- Arquivos nao Markdown: Drive; Notion e Cofre apenas indexam.
- Conteudo sensivel pessoal: permitido no Notion particular `MAPA 360`, pois Jadielson informou que apenas ele acessa esse perfil. Ainda assim, preservar linguagem discreta e evitar exposicao desnecessaria.
- Tokens e credenciais: nunca registrar em Markdown.

## Proximos passos

1. Criar database `Cofre Index` no Notion para mapear arquivos Markdown e seus caminhos.
2. Criar database `Sync Log` no Notion para auditoria de sincronizacoes.
3. Importar lote essencial do Cofre para o `MAPA 360`.
4. Criar rotina/script de sincronizacao governada Notion -> Cofre.
5. Criar fila de revisao para alteracoes que toquem Fluxo 1.

## Implementacao inicial - 2026-08-06

Databases criadas no Notion:

- `Cofre Index`
  - Data source ID: `a3803ed8-abf8-47da-9a52-ae8bf889b865`
  - Funcao: indice operacional dos arquivos Markdown do Cofre no Notion.
- `Sync Log`
  - Data source ID: `a0991308-eea4-455b-94fb-7dae2d184409`
  - Funcao: auditoria de sincronizacoes entre Cofre e Notion.

Lote inicial:

- 80 arquivos essenciais do Cofre foram indexados no `Cofre Index`.
- O lote inclui arquivos raiz de governanca, contexto Notion, decisoes, LÓGIKA e registros operacionais prioritarios.

Script criado:

- `scripts/sync/notion-cofre-sync.py`

Comportamento do script:

- Roda em `dry-run` por padrao.
- Usa `--apply` para gravar alteracoes permitidas.
- Aplica direto apenas em caminhos operacionais liberados.
- Arquivos protegidos ou Fluxo 1 geram proposta em `00-central/inbox/externa/notion/revisao/`.
- Teste seco em 2026-08-06: 80 itens verificados, 0 erros, 0 gravacoes.

## Checkpoint - 2026-08-07

Importador em lote criado:

- `scripts/sync/notion-cofre-index-import.py`

Comportamento:

- Consulta caminhos ja existentes no `Cofre Index`.
- Importa somente arquivos Markdown ainda nao indexados.
- Classifica por fluxo, tipo, frente, protecao, direcao de sync, hash e resumo.
- Permite continuar por lotes sem duplicar registros.

Lote executado:

- Existentes antes: 80.
- Pendentes antes: 4.758.
- Importados no lote: 250.
- Erros: 0.
- Total aproximado indexado apos lote: 330.

## Checkpoint - 2026-08-07 - lote 500

Lote executado apos pergunta de estimativa:

- Existentes antes: 330.
- Pendentes antes: 4.508.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 830.

Observacao:

O lote de 500 funcionou sem erro, mas levou mais tempo. Proximos lotes podem seguir em blocos de 500 quando houver janela, ou blocos menores quando for melhor receber checkpoints mais frequentes.

## Checkpoint - 2026-08-07 - lote 500 adicional

Lote executado apos validacao de status:

- Existentes antes: 830.
- Pendentes antes: 4.008.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 1.330.
- Restante aproximado: 3.508.

## Checkpoint - 2026-08-07 - lote 500 adicional 2

Lote executado na continuidade da importacao:

- Existentes antes: 1.330.
- Pendentes antes: 3.508.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 1.830.
- Restante aproximado: 3.008.

## Checkpoint - 2026-08-07 - lote 500 adicional 3

Lote executado na continuidade da importacao:

- Existentes antes: 1.830.
- Pendentes antes: 3.008.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 2.330.
- Restante aproximado: 2.508.

## Checkpoint - 2026-08-07 - lote 500 adicional 4

Lote executado na continuidade da importacao:

- Existentes antes: 2.330.
- Pendentes antes: 2.508.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 2.830.
- Restante aproximado: 2.008.

## Checkpoint - 2026-08-07 - lote 500 adicional 5

Lote executado na continuidade da importacao:

- Existentes antes: 2.830.
- Pendentes antes: 2.008.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 3.330.
- Restante aproximado: 1.508.

## Checkpoint - 2026-08-07 - lote 500 adicional 6

Lote executado na continuidade da importacao:

- Existentes antes: 3.330.
- Pendentes antes: 1.508.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 3.830.
- Restante aproximado: 1.008.

## Checkpoint - 2026-08-07 - lote 500 adicional 7

Lote executado na continuidade da importacao:

- Existentes antes: 3.830.
- Pendentes antes: 1.008.
- Importados no lote: 500.
- Erros: 0.
- Total aproximado indexado apos lote: 4.330.
- Restante aproximado: 508.

## Checkpoint - 2026-08-07 - fechamento da importacao do indice

Lote final executado:

- Existentes antes: 4.330.
- Pendentes antes: 508.
- Importados no lote final: 508.
- Erros: 0.
- Total validado no `Cofre Index`: 4.838.
- Pendentes apos validacao: 0.

Status:

- Importacao completa do indice Markdown do Cofre para o Notion concluida.
- Proxima etapa: refinamento de views/dashboards e ativacao de rotina recorrente apos teste real de edicao Notion -> Cofre.

Validacao tecnica:

- `scripts/sync/notion-cofre-sync.py` foi ajustado para localizar o CLI `ntn` em `/data/.npm-global/bin/ntn` quando o binario nao estiver no `PATH`.
- Adicionada opcao `--max-items` para smoke test de sincronizacao sem percorrer a base inteira.
- Smoke test executado com `--max-items 10`: 10 itens checados, 10 ignorados corretamente, 0 erros.
