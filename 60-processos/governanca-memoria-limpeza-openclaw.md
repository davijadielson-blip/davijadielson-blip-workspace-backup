---
tema: governanca de memoria e limpeza do OpenClaw
conteudo: politica operacional para consolidar memoria no Cofre, reter sessoes temporarias e executar manutencao segura de armazenamento
nicho: ecossistema agentico Loh/Jadielson
setor: governanca, operacoes e armazenamento
cliente: Jadielson Davi
tipo: processo operacional
prioridade: maxima
atualizado_em: 2026-07-29
usar_quando: orientar agentes sobre registro de memoria, encerramento de sessoes, retencao, limpeza diaria e protecoes de arquivos criticos
nao_usar_quando: substituir decisoes centrais em 00-central/decisoes.md ou autorizar exclusao permanente sem revisao humana
---

# Governanca de memoria e limpeza do OpenClaw

## Principio central

O Cofre (`/data/.openclaw/workspace/`) e a fonte oficial da verdade. Sessoes sao temporarias e nao devem funcionar como memoria permanente.

Regra final: **consolidar antes de limpar. Preservar conhecimento, eliminar residuos.**

## O que deve ser registrado no Cofre

Registrar antes de encerrar tarefa ou sessao sempre que houver valor permanente:

- decisoes tomadas;
- regras definidas;
- preferencias permanentes;
- mudancas de estrategia;
- status de projetos;
- proximos passos;
- responsabilidades;
- prazos;
- processos aprovados;
- aprendizados reutilizaveis;
- informacoes necessarias para continuidade entre sessoes;
- correcoes de informacoes antigas;
- documentos, referencias e links estrategicos.

O registro deve ser claro, resumido, datado quando necessario, colocado no workspace correto, sem duplicacoes desnecessarias e atualizado quando substituir decisao anterior.

Quando uma informacao nova contrariar outra antiga, atualizar a fonte oficial e registrar brevemente o motivo. Nao manter duas versoes conflitantes como se ambas fossem validas.

## O que nao deve virar memoria

Nao registrar no Cofre:

- saudacoes;
- agradecimentos;
- testes;
- mensagens incompletas;
- tentativas que falharam sem aprendizado;
- repeticoes;
- respostas intermediarias;
- raciocinios descartados;
- logs tecnicos sem utilidade futura;
- conteudos temporarios;
- arquivos duplicados;
- detalhes operacionais que ja perderam validade;
- conversas que nao alteraram decisao, estrategia ou execucao.

Pergunta de filtro: **essa informacao sera necessaria em outra sessao para tomar decisao, executar tarefa ou manter coerencia?** Se nao, nao registrar.

## Encerramento de sessao

Antes de considerar uma sessao concluida:

1. Identificar tudo que possui valor permanente.
2. Registrar as informacoes no workspace adequado.
3. Atualizar decisoes, projetos e proximos passos.
4. Confirmar que nenhum dado estrategico existe somente na sessao.
5. Classificar o restante como temporario, operacional ou descartavel.

Nunca depender exclusivamente do historico da sessao para manter contexto relevante.

## Hierarquia de fontes

Ao buscar contexto, usar esta prioridade:

1. Cofre oficial do projeto.
2. Memorias consolidadas e documentos aprovados.
3. Configuracao e instrucoes do agente.
4. Estado atual do projeto.
5. Sessoes recentes, apenas como apoio operacional.
6. Sessoes antigas, somente quando houver necessidade explicita de auditoria ou recuperacao historica.

Quando uma sessao antiga contrariar o Cofre, prevalece o Cofre, salvo evidencia de que ele esta desatualizado.

## Politica de retencao de sessoes

Manter somente:

- sessoes em andamento;
- sessoes recentes ainda nao consolidadas;
- sessoes vinculadas a tarefas pendentes;
- sessoes com decisoes ainda nao registradas;
- sessoes necessarias para auditoria, continuidade ou recuperacao;
- sessoes agendadas, automacoes e processos ativos.

Sessoes ja consolidadas no Cofre podem ser marcadas para limpeza ou revisao, respeitando as protecoes abaixo.

## Limpeza diaria apos 00h00

A rotina diaria deve:

1. Fazer diagnostico do espaco utilizado.
2. Identificar sessoes e artefatos temporarios.
3. Confirmar que informacoes relevantes ja foram registradas no Cofre.
4. Preservar sessoes ativas, recentes ou pendentes.
5. Remover ou isolar somente itens claramente descartaveis, conforme as protecoes.
6. Produzir relatorio resumido da limpeza.

Priorizar revisao de arquivos temporarios, caches regeneraveis, downloads temporarios, clones temporarios de plugins, logs antigos sem valor operacional, trajetorias ja consolidadas, duplicados, artefatos sem referencia e sessoes antigas ja resumidas.

## Backup oficial

O backup paralelo oficial do Cofre usa exclusivamente:

`https://github.com/davijadielson-blip/davijadielson-blip-workspace-backup`

Branch principal: `main`.

O GitHub e apenas copia de seguranca. O Cofre local continua sendo a fonte oficial de verdade. Nunca tratar o GitHub como workspace ativo.

Antes de qualquer limpeza ou quarentena relevante:

1. verificar estado do Git;
2. auditar possiveis segredos;
3. fazer commit seletivo apenas de arquivos seguros;
4. executar push para `origin/main`;
5. confirmar que o hash existe no remoto;
6. somente entao marcar candidatos a limpeza/quarentena.

Nunca executar `git push --force`, `git reset --hard`, `git clean` ou reescrita automatica de historico.

## Job ativo

Em 2026-07-29 foi criado o job OpenClaw `governanca-cofre-sessoes-diaria-0000`, ID `df970ab7-4083-433f-b007-b34e6c68d130`.

- Agenda: todos os dias as 00h00.
- Fuso: `America/Maceio`.
- Modo inicial: auditoria/simulacao conservadora.
- Exclusao permanente: bloqueada.
- Saida: relatorio em `60-processos/relatorios/limpeza-openclaw/` e resumo para Jadielson.

## Protecoes obrigatorias

Nunca apagar automaticamente:

- `workspace`;
- `workspace-*`;
- `memory`;
- configuracoes;
- credenciais;
- prompts;
- instrucoes dos agentes;
- `openclaw-agent.sqlite`;
- `sessions.json`;
- backups;
- projetos;
- documentos oficiais;
- arquivos de decisao;
- sessoes ativas;
- sessoes com pendencias.

Tambem nao remover diretorios completos de agentes sem autorizacao explicita.

Comandos amplos como `rm -rf /data/.openclaw/agents/*` ou `rm -rf /data/.openclaw/*` sao proibidos.

Antes de qualquer limpeza relevante:

- fazer simulacao;
- listar o que sera removido ou isolado;
- calcular espaco estimado;
- confirmar que nao e essencial;
- preferir selecao por tipo, idade e status;
- em caso de duvida, classificar como `revisao necessaria`.

Pela regra superior de seguranca do ecossistema, exclusao permanente depende de autorizacao humana explicita. Quando houver duvida ou quando o item puder ter valor, mover para quarentena/revisao em vez de apagar.

## Trajetorias e sessoes

Arquivos de trajetoria e registros detalhados de execucao nao sao a fonte oficial da memoria.

Eles podem ser marcados para limpeza quando:

- a sessao ja estiver concluida;
- as decisoes ja estiverem no Cofre;
- nao houver tarefa pendente;
- nao forem necessarios para auditoria;
- nao estiverem ligados a execucao ativa.

Manter periodo minimo de seguranca para sessoes recentes e ultimos dias de atividade. Nao apagar arquivos apenas pelo tamanho; analisar funcao, vinculo e relevancia.

## Controle preventivo

Monitorar diariamente:

- uso total do disco;
- crescimento por agente;
- volume das pastas de sessoes;
- quantidade de arquivos de trajetoria;
- caches;
- logs;
- temporarios;
- duplicacoes;
- agentes ou automacoes gerando dados em excesso.

Limiares:

- 70%: emitir alerta preventivo;
- 80%: iniciar limpeza segura;
- 90%: suspender tarefas nao essenciais e priorizar liberacao;
- 95%: executar protocolo emergencial, preservando dados criticos.

Investigar crescimentos anormais, nao apenas limpar o sintoma.

## Relatorio diario

Salvar relatorio em area administrativa do Cofre, nao dentro de sessao descartavel, com:

```text
Data e hora:
Uso antes:
Uso depois:
Espaco liberado:
Arquivos removidos:
Sessoes preservadas:
Itens pendentes de revisao:
Possivel causa do crescimento:
Acao preventiva recomendada:
```

Destino recomendado: `60-processos/relatorios/limpeza-openclaw/`.

## Criterio de sucesso

A rotina esta correta quando:

- decisoes relevantes estao no Cofre;
- agentes retomam trabalho sem depender de sessoes antigas;
- nenhuma memoria estrategica e perdida;
- sessoes temporarias nao crescem indefinidamente;
- disco permanece abaixo dos limites de risco;
- limpeza e seletiva, auditavel e reversivel;
- informacoes irrelevantes nao contaminam o workspace.
