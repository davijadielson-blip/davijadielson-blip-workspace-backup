# Backlog Inteligente — Template de Fatiamento Executivo v2

**Data:** 2026-07-19 03:24 UTC  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente` (`topic_id: 489`).  
**Contexto:** Jadielson corrigiu a interpretação anterior: o prompt não deve ser interrogativo nem gerar nova etapa de diagnóstico extensa. Deve ser um comando direto para o agente/tópico fatiar o projeto/estudo em microtarefas executáveis.

## Correção de entendimento

O prompt padrão deve funcionar como uma **ordem operacional neutra** para qualquer agente/tópico.

Ele deve dizer, em essência:

- considerando este projeto/estudo que já estamos debatendo;
- desmembre o todo em partes menores;
- organize em fases, subprojetos e microtarefas;
- indique sequência de execução;
- entregue um caminho claro para trabalhar aos poucos.

Não deve focar em perguntar “qual é o resultado esperado?” quando o contexto já existe. A função principal é **quebrar para executar**.

## Template canônico sugerido

```text
Considerando este projeto/estudo/frente que estamos debatendo neste tópico, faça um fatiamento inteligente para execução.

Não trate como uma ideia solta. Assuma o contexto já existente neste tópico e transforme o todo em partes menores, claras e executáveis.

Organize assim:

1. Visão geral do todo
- Resuma em poucas linhas o que precisa ser realizado ou avançado.

2. Quebra em partes maiores
- Separe em fases, blocos ou subprojetos.
- Dê nomes claros para cada parte.

3. Microtarefas executáveis
- Para cada parte, liste tarefas pequenas e objetivas.
- Cada tarefa deve começar com verbo de ação.
- Evite tarefas vagas como “organizar”, “pensar” ou “resolver” sem explicar o que fazer.

4. Ordem sugerida de execução
- Mostre o que vem primeiro, segundo e terceiro.
- Indique o que destrava o restante.

5. Próximas ações imediatas
- Liste as 3 primeiras microtarefas que posso executar agora ou nos próximos dias.

6. Critério de avanço
- Diga como saberemos que essa etapa avançou o suficiente para passar para a próxima.

7. Versão enxuta final
- No final, entregue um checklist simples, em ordem, para eu seguir.

Importante:
- Não complique.
- Não transforme tudo em teoria.
- Não faça muitas perguntas antes de fatiar.
- Se faltar alguma informação, assuma uma hipótese razoável e marque como “a confirmar”.
- O objetivo é me ajudar a sair da visão grande para tarefas pequenas, executáveis e sequenciais.
```

## Uso previsto

Esse prompt pode ser usado em tópicos/frentes como:

- `PROJETOS > O Fio da Memória`.
- `ESTUDOS > Comunidade 1P`.
- `ESTUDOS > VENDE-C`.
- Outras frentes do Mapa 360.

## Fonte

Cofre: `CONSTITUICAO.md`, `backlog-inteligente-prompt-padrao-fatiamento-2026-07-19.md` + áudio corretivo de Jadielson no Telegram.