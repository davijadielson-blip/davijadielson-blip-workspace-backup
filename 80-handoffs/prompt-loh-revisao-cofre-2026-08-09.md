---
tema: prompt para revisao estrutural do Cofre pela Loh
conteudo: prompt completo para alinhar regras, mapa, autonomia da IA, estrutura real do Cofre, preservacao de agentes e obrigatoriedade de YAML frontmatter
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: handoff operacional
prioridade: maxima
atualizado_em: 2026-08-09
usar_quando: enviar para a Loh executar a revisao estrutural e canonica do Cofre
nao_usar_quando: tratar de ajustes pontuais sem impacto em governanca, agentes, estrutura ou regras do Cofre
---

# Prompt para a Loh - Revisao estrutural do Cofre

Loh, preciso que voce execute uma revisao estrutural e canonica no Cofre, considerando a arvore real atual do workspace e preservando tudo que ja esta em funcionamento.

## Contexto

O ambiente de workspace mudou. Eu, Jadielson, nao consigo mais acessar e editar diretamente o Cofre como antes. Na pratica, quando preciso salvar, organizar, corrigir, consolidar ou atualizar algo, sao os agentes que escrevem por mim.

Por isso, quero revogar as regras antigas que limitam a IA como "so leitora", "bibliotecaria" ou impedem edicao em determinadas areas do Cofre. A regra agora deve ser mais simples: a IA autorizada pode manter o Cofre inteiro, com responsabilidade, rastreabilidade e respeito a decisao humana final.

A arvore real do Cofre hoje ja nao segue mais o modelo antigo F0/F1/F2/F3. A estrutura principal atual esta organizada assim:

```text
/data/.openclaw/workspace/
- arquivos centrais: AGENTS.md, MAPA.md, MEMORY.md, SOUL.md, USER.md, CONSTITUICAO.md e outros arquivos raiz de governanca
- 00-central/ -> notas permanentes/centrais
- 10-pessoal/ -> vida pessoal, rotina, saude, familia, inbox, tarefas
- 20-profissional/ -> LOGIKA e referencias profissionais
- 30-estudos/ -> cursos, livros, metodos, planos, recursos
- 40-projetos/ -> projetos pessoais, profissionais, autorais, trabalho, produtos, ideias
- 50-clientes/ -> Saude, Camara, SINDSS, vereadores e outros clientes
- 60-processos/ -> checklists, rotinas, relatorios, templates, skills operacionais
- 70-agentes/ -> agentes, runtime e squads
- 80-handoffs/ -> passagens de contexto
- 90-arquivo/ -> legado, backups, duplicidades, quarentena e estrutura antiga
- memory/ -> cerebro operacional da IA
- media/ -> midia recebida/referenciada
- scripts/ -> automacoes
- skills/ -> skills ativas do workspace
```

Volume atual aproximado por pasta:

- 90-arquivo/: 2585 arquivos
- 40-projetos/: 1031 arquivos
- 50-clientes/: 662 arquivos
- 30-estudos/: 152 arquivos
- memory/: 148 arquivos
- 10-pessoal/: 136 arquivos
- 20-profissional/: 122 arquivos
- 60-processos/: 100 arquivos
- 70-agentes/: 95 arquivos
- media/: 51 arquivos
- scripts/: 16 arquivos
- 00-central/: 15 arquivos
- skills/: 12 arquivos
- 80-handoffs/: 2 arquivos

## Problema

O MAPA.md e algumas regras canonicas ainda descrevem o modelo antigo com [F0] 0-Inbox/, [F1], [F2] memory/ e [F3] PROJETOS/. Isso esta desalinhado com a estrutura real atual e pode gerar confusao nos agentes.

Tambem ainda existem regras antigas que limitam a IA como "so leitora", "bibliotecaria", "nao editar F1" ou "so Jadielson escreve determinadas areas". Esse modelo nao serve mais, porque o ambiente mudou e, na pratica, quando preciso salvar, organizar ou atualizar o Cofre, sao os agentes que executam a escrita.

## Ponto critico

Ja existem agentes, subagentes, skills, crons, rotinas, scripts, programacoes e tarefas em funcionamento. A reorganizacao nao pode quebrar nada, apagar contexto, invalidar caminhos, prejudicar automacoes ou gerar alucinacoes por mudanca brusca de estrutura.

O objetivo e potencializar o ecossistema, nao retroceder.

## Diretriz canonica nova

"O Cofre e a fonte de verdade do Jadielson. A IA autorizada pode ler, criar, editar, reorganizar, consolidar, mover e manter arquivos do Cofre quando estiver executando pedidos, preservando contexto, melhorando organizacao ou garantindo continuidade. Jadielson permanece como autoridade final sobre sentido, prioridade, publicacao, envio externo, decisoes sensiveis e exclusao definitiva. A autonomia da IA e operacional; a autoridade final e humana."

## Diretriz de preservacao

Antes de alterar, mover, renomear ou consolidar qualquer coisa, faca uma auditoria de dependencias:

- agentes existentes
- subagentes
- skills
- crons
- scripts
- runtimes
- tarefas programadas
- handoffs
- arquivos de configuracao
- referencias internas a caminhos antigos
- instrucoes que apontem para F0/F1/F2/F3
- qualquer rotina que dependa da estrutura atual ou antiga

Nada deve ser movido ou renomeado sem antes identificar quem depende daquele caminho.

## Regra obrigatoria de YAML frontmatter

Todo arquivo `.md` criado, editado ou padronizado no Cofre deve comecar com cabecalho YAML frontmatter para facilitar busca, roteamento e interpretacao pelos agentes.

Modelo minimo obrigatorio:

```yaml
---
tema: <tema principal do arquivo>
conteudo: <resumo do que contem>
setor: <setor relevante>
cliente: <cliente ou Jadielson Davi>
tipo: <tipo do documento>
prioridade: <baixa|media|alta|maxima>
atualizado_em: <data YYYY-MM-DD>
usar_quando: <quando consultar este arquivo>
nao_usar_quando: <quando nao consultar este arquivo>
---
```

Regras:

- Todo novo `.md` deve nascer com YAML frontmatter.
- Se um `.md` existente for editado e estiver sem YAML, adicionar o cabecalho.
- Campos minimos obrigatorios: `tema` e `atualizado_em`.
- Para arquivos importantes, preencher todos os campos do modelo.
- Nao criar Markdown solto sem metadados, porque isso dificulta a busca e a continuidade dos agentes.

## Objetivo

Atualizar o Cofre para que as regras, o mapa e a arvore real estejam alinhados com o uso atual: uma estrutura numerica clara por area, com acesso operacional amplo para a IA autorizada, sem a limitacao antiga F0/F1/F2/F3, mas preservando compatibilidade com o que ja existe.

## Tarefas

### 1. Fazer inventario antes da reorganizacao

- Mapear agentes e subagentes existentes.
- Mapear skills ativas.
- Mapear crons, scripts, automacoes e tarefas programadas.
- Mapear handoffs e runtimes.
- Identificar arquivos que referenciam caminhos antigos.
- Identificar dependencias que podem quebrar se pastas forem movidas ou renomeadas.
- Separar o que e estrutura ativa do que e legado.

### 2. Atualizar o MAPA.md

- Substituir a descricao antiga F0/F1/F2/F3 pela arvore real atual.
- Explicar claramente a funcao de cada pasta principal.
- Registrar que F0/F1/F2/F3 sao termos legados e nao devem mais orientar o roteamento.
- Indicar que a inbox fisica atual esta em 10-pessoal/inbox.
- Indicar que a inbox operacional da IA continua em memory/inbox-externa/.
- Deixar o mapa pratico para qualquer agente saber onde procurar e onde salvar.
- Quando houver compatibilidade necessaria com caminhos antigos, documentar isso explicitamente.

### 3. Revisar AGENTS.md e arquivos centrais de governanca

Procurar e reescrever regras que ainda digam ou impliquem:

- "A IA e bibliotecaria, eu sou o autor"
- "IA so le"
- "nao editar F1"
- "notas autorais so Jadielson escreve"
- "F1 e humano / F2 e IA"
- "camada 4 nunca migra"
- "salvar output so depois de aprovacao"
- qualquer bloqueio operacional que impeca a IA autorizada de manter o Cofre

Trocar essas regras por uma logica de autonomia operacional com responsabilidade.

### 4. Consolidar o modelo novo

A separacao do Cofre deve ser por area, finalidade e sensibilidade, nao por quem pode escrever.

Usar como referencia principal:

- 00-central/ para notas centrais e permanentes
- 10-pessoal/ para vida pessoal, rotina, saude, familia, inbox e tarefas
- 20-profissional/ para LOGIKA e referencias profissionais
- 30-estudos/ para cursos, livros, metodos e planos de estudo
- 40-projetos/ para projetos, ideias, produtos e frentes autorais
- 50-clientes/ para clientes e frentes institucionais
- 60-processos/ para rotinas, checklists, templates e processos
- 70-agentes/ para agentes, runtime e squads
- 80-handoffs/ para passagem de contexto
- 90-arquivo/ para legado, backups, duplicidades, quarentena e estrutura antiga
- memory/ para memoria operacional da IA
- media/ para midias
- scripts/ para automacoes
- skills/ para skills ativas

### 5. Resolver contradicoes sem quebrar compatibilidade

- Auditar arquivos centrais e instrucoes que ainda mencionam a estrutura antiga.
- Diferenciar claramente:
  - estrutura atual valida
  - termos legados
  - caminhos antigos ainda referenciados
  - pastas antigas arquivadas
  - regras revogadas
- Se alguma referencia antiga precisar continuar por compatibilidade, marcar como "legado tecnico temporario".
- Se possivel, criar orientacao de transicao em vez de ruptura brusca.
- Nunca trocar caminhos usados por automacoes sem atualizar tambem as automacoes correspondentes.

### 6. Reorganizar e enxugar

- Mesclar regras parecidas.
- Remover repeticoes.
- Corrigir conflitos entre CONSTITUICAO.md, AGENTS.md, MAPA.md, MEMORY.md, instrucoes de agentes e arquivos de contexto.
- Deixar os documentos mais curtos, praticos e operacionais.
- Priorizar clareza para agentes futuros.
- Evitar reescrever contexto util de forma generica; preservar informacoes especificas.

### 7. Manter salvaguardas absolutas

- Nada de exclusao definitiva sem autorizacao explicita de Jadielson.
- Se algo precisar sair do lugar, mover para 90-arquivo/quarentena ou pasta equivalente de revisao, nunca apagar permanentemente.
- Nao inventar dados.
- Nao misturar vida pessoal, empresa, clientes e projetos.
- Nao publicar, enviar e-mail, postar, compartilhar ou acionar terceiros sem autorizacao clara.
- Decisoes sensiveis devem ser registradas e, quando necessario, validadas.

### 8. Validar antes de finalizar

- Verificar se agentes continuam encontrando SOUL.md, USER.md, MEMORY.md, MAPA.md e AGENTS.md.
- Verificar se skills ainda apontam para caminhos existentes.
- Verificar se scripts e crons nao ficaram com caminhos quebrados.
- Verificar se handoffs continuam legiveis.
- Verificar se o novo mapa orienta corretamente onde salvar cada tipo de conteudo.
- Rodar checagens possiveis sem executar acoes externas sensiveis.

### 9. Fazer auditoria final

Ao concluir, entregar um relatorio com:

- arquivos alterados
- regras revogadas
- regras consolidadas
- referencias F0/F1/F2/F3 removidas ou mantidas como legado
- agentes, subagentes, skills, crons e scripts verificados
- dependencias preservadas
- possiveis riscos restantes
- conflitos encontrados
- pontos que ainda precisam de decisao humana
- resumo da nova estrutura oficial
- commit e push, se tudo estiver consistente

## Resultado esperado

Quero que o Cofre fique alinhado com a estrutura real atual, mais claro, mais enxuto e mais pratico.

O modelo F0/F1/F2/F3 deve deixar de limitar ou confundir os agentes.

A IA autorizada deve poder manter o Cofre inteiro de forma operacional, mas sem quebrar agentes, subagentes, skills, crons, scripts, tarefas, memorias ou programacoes ja existentes.

A intencao e potencializar o ecossistema, preservar o que funciona, corrigir contradicoes e preparar uma base mais forte para o futuro.
