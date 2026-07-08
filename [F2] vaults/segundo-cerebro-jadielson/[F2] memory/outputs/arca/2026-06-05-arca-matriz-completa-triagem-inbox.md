---
tipo: output
subtipo: matriz-triagem-inbox
gerado-por: arca
supervisionado-por: Alfred
integrado-com: Lôh
revisado: false
data: 2026-06-05
status-colheita: candidato-operacional
origem: pedido direto de Jadielson no tópico Segundo Cérebro / Arca
---

# Matriz completa de triagem do Inbox — Análise da Arca

## 1. Contexto

Jadielson pediu uma análise completa da matriz de triagem do Inbox. A Arca leu o diagnóstico inicial anterior e os arquivos reais em `[F0] 0-Inbox/`.

Regra respeitada: nenhum arquivo do F0 foi movido, deletado ou editado. Esta análise foi salva apenas em F2/memory como camada operacional da IA.

## 2. Estado atual do Inbox

Foram encontrados **21 arquivos Markdown** no F0 Inbox.

O Inbox está capturando bem, mas ainda mistura quatro mundos diferentes:

1. vida pessoal e organização própria;
2. LÓGIKA / produção / clientes;
3. Secretaria de Saúde / demandas institucionais;
4. manutenção do próprio Segundo Cérebro.

O risco principal não é a quantidade de arquivos; é a ausência de decisão de destino. Hoje vários itens estão parados porque todos usam o mesmo modelo genérico:

- tarefa simples;
- ideia/projeto novo;
- projeto em andamento.

Esse modelo é útil, mas insuficiente para o volume real de frentes de Jadielson.

## 3. Critério usado pela Arca

A matriz abaixo usa dois filtros ao mesmo tempo:

### 3.1. Saída operacional

- **Executar**: ação simples, pode virar tarefa e encerrar.
- **Planejar**: precisa virar projeto/plano antes de executar.
- **Encaminhar**: pertence a outra frente/agente.
- **Sistema**: precisa virar processo, template, checklist ou padrão recorrente.
- **Arquivar/Revisar**: teste, item vazio, duplicado, antigo ou sem contexto suficiente.

### 3.2. Banco dos 5 Destinos

Baseado em `[F2] memory/databases/matriz-tarefas.md`:

- 🎯 FOCO: só Jadielson deve fazer.
- 🤝 DELEGAR: pode sair da mão de Jadielson.
- ⚙️ SISTEMA: precisa virar padrão recorrente.
- 📦 BLOCO: tarefa pequena para executar em janela fixa.
- 🗑️ CORTAR: eliminar/reduzir/arquivar.

## 4. Matriz completa por arquivo

| # | Arquivo | Frente provável | Saída | 5 Destinos | Dono sugerido | Urgência | Próxima ação sugerida | Observação |
|---|---|---|---|---|---|---|---|---|
| 01 | `- ALIMENTAR TRELA.md` | Organização pessoal / ferramenta | Executar | 📦 BLOCO | Jadielson ou Arca organiza lembrete | Baixa/média | Definir o que significa “alimentar Trela” e se ainda é ferramenta ativa | Se Trello/Trela não estiver mais em uso, arquivar |
| 02 | `- CONTINUAR A ORGANIZACAO DE ARQUIVOS.md` | Organização digital | Planejar/Sistema | ⚙️ SISTEMA | Arca + Lôh | Média | Transformar em plano de organização digital por etapas | Não executar solto; precisa de método |
| 03 | `- DAR SEGUIMENTO AO PLANO SE SERVIÇOS.md` | LÓGIKA / comercial | Planejar/Encaminhar | 🎯 FOCO + ⚙️ SISTEMA | Jarvis / LÓGIKA | Média/alta | Corrigir título para “plano de serviços” e vincular ao comercial da LÓGIKA | Parece relacionado a oferta/proposta |
| 04 | `- MANDAR ORÇAMENTO PARA QUIEL, KAUA E LIDIO.md` | LÓGIKA / clientes | Executar/Encaminhar | 🎯 FOCO ou 📦 BLOCO | Jarvis / Comercial | Alta se ainda pendente | Confirmar se os orçamentos ainda precisam ser enviados; se sim, preparar mensagem/modelo | Item com risco de perda comercial |
| 05 | `- MOVIMENTAR O FIO DA MEMORIA.md` | Segundo Cérebro | Sistema/Planejar | ⚙️ SISTEMA | Arca | Média | Definir o que é “Fio da Memória” e criar rotina mínima de movimentação | Candidato forte para rotina semanal da Arca |
| 06 | `- PLANE DE SERVICOS.md` | LÓGIKA / comercial | Revisar/Planejar | ⚙️ SISTEMA | Jarvis / Arca | Média | Verificar se é duplicado de “plano de serviços”; consolidar com item 03 | Provável título incompleto |
| 07 | `- PREPARAR LANÇAMENTO DO VIDEO CLIPE.md` | LÓGIKA / produção | Planejar | 🎯 FOCO + ⚙️ SISTEMA | Jarvis / Produção | Média/alta | Criar checklist de lançamento: data, assets, cortes, legenda, publicação, impulsionamento | Projeto com várias etapas |
| 08 | `- RESPONDER BETO SAARA.md` | Comunicação / possível cliente | Executar | 📦 BLOCO | Jadielson / Jarvis se comercial | Alta se ainda não respondido | Confirmar se já respondeu; se não, redigir resposta curta | Tarefa simples, não deve ficar no Inbox |
| 09 | `- Sempre analizar e redefinir conteúdos para os Clientes.md` | LÓGIKA / conteúdo | Revisar/Sistema | ⚙️ SISTEMA | Jarvis / Conteúdo | Baixa até recuperar contexto | Arquivo está vazio; decidir se recria como princípio de revisão editorial ou arquiva | Sem conteúdo, mas o título é bom |
| 10 | `- VENDE-C.md` | Ambíguo / comercial | Revisar | 🗑️ CORTAR ou ⚙️ SISTEMA | Jadielson confirma | Baixa | Perguntar o significado; se não houver memória, arquivar | Título insuficiente |
| 11 | `CONSULTAS CIRURGIÃO GERAL PARA A TRIAGEM DE OUTRA - 02.06.md` | Secretaria de Saúde | Encaminhar/Executar | 📦 BLOCO | Frente Saúde / Secretaria | Alta se data ainda relevante; senão revisar | Verificar se 02/06 já passou e se houve continuidade; arquivar como registro ou virar demanda de saúde | Pode estar vencido |
| 12 | `CRIAR TEMPLATES DE PRODUCAO DE EDICAO DE VIDEOS E STORIES AT.md` | LÓGIKA / produção | Sistema | ⚙️ SISTEMA | Jarvis / Produção | Média/alta | Criar projeto “Templates de produção no Premiere/Claude” com escopo mínimo | Altíssimo valor recorrente |
| 13 | `CRIAR UM CABECALHO NO TOPO MD. COM AS INFORMACOES PRINCIPAIS.md` | Segundo Cérebro / vault | Sistema | ⚙️ SISTEMA | Arca + Lôh | Média | Criar padrão de frontmatter/cabeçalho para notas F1/F2, sem aplicar em massa ainda | Muito importante para automação futura |
| 14 | `CRIAR UM SISTEMA DE FICHA ONLINE PARA A SECRETARIA.md` | Secretaria de Saúde | Planejar/Encaminhar | ⚙️ SISTEMA + 🎯 FOCO | Frente Saúde / Lôh se técnico | Média | Transformar em mini-projeto: objetivo, usuários, campos, ferramenta e autorização | Pode envolver dados sensíveis; cuidado |
| 15 | `CURSOS E IMPLEMENTACOES URGENTES PARA CONCLUIR E RODAR.md` | Estudos / implementação | Planejar | 🎯 FOCO + 📦 BLOCO | Estudos / Alfred | Média | Quebrar em lista: cursos, implementações, prioridade, próximo passo | Título amplo demais |
| 16 | `MANDAR DADOS PARA ASCO DOS SERVIÇOS QUE A SECRETARIA FAZ.md` | Secretaria de Saúde / ASCOM | Executar/Encaminhar | 📦 BLOCO | Frente Saúde / Secretaria | Alta se ainda pendente | Confirmar se já foi enviado; se não, listar dados necessários e montar texto | Tarefa institucional prática |
| 17 | `MOVIMENTAR CONTA BBMD.md` | Finanças / administrativo | Executar/Revisar | 📦 BLOCO ou 🎯 FOCO | My Finance / Jadielson | Média | Confirmar o que é BBMD, risco e prazo; não automatizar sem contexto | Pode envolver dinheiro; precisa cautela |
| 18 | `PASTAS DELETADAS - REVISITAR.md` | Segundo Cérebro / organização | Revisar/Planejar | 🗑️ CORTAR + ⚙️ SISTEMA | Arca | Baixa/média | Fazer triagem por grupos: retomar, ignorar, transformar em referência | Já é um registro útil, não uma tarefa urgente |
| 19 | `REGISTRO HTTPSMEDIA.XTILES.APP4561E4E6B61FF9646E46EF34.md` | Documento / empresa ou pessoal | Revisar/Encaminhar | 📦 BLOCO | Arca + Jadielson confirma | Baixa/média | Identificar o CNPJ e decidir frente: LÓGIKA, cliente ou arquivo morto | Link externo; não mover sem saber |
| 20 | `TESTE DE REATIVAÇÃO 12H01.md` | Teste técnico | Arquivar | 🗑️ CORTAR | Arca / Lôh | Baixa | Após confirmação, arquivar em pasta de testes ou lixeira recuperável | Não tem valor operacional |
| 21 | `teste-loh.md` | Teste técnico | Arquivar | 🗑️ CORTAR | Arca / Lôh | Baixa | Após confirmação, arquivar em pasta de testes ou lixeira recuperável | Não tem valor operacional |

## 5. Agrupamento por prioridade

### Alta prioridade prática

1. `- MANDAR ORÇAMENTO PARA QUIEL, KAUA E LIDIO.md`
2. `- RESPONDER BETO SAARA.md`
3. `MANDAR DADOS PARA ASCO DOS SERVIÇOS QUE A SECRETARIA FAZ.md`
4. `CONSULTAS CIRURGIÃO GERAL PARA A TRIAGEM DE OUTRA - 02.06.md` — só se ainda estiver pendente ou tiver continuidade.

Esses itens têm cara de pendência com outra pessoa ou instituição. Não deveriam ficar parados no Inbox.

### Alta prioridade estrutural

1. `CRIAR TEMPLATES DE PRODUCAO DE EDICAO DE VIDEOS E STORIES AT.md`
2. `CRIAR UM CABECALHO NO TOPO MD. COM AS INFORMACOES PRINCIPAIS.md`
3. `- MOVIMENTAR O FIO DA MEMORIA.md`
4. `- CONTINUAR A ORGANIZACAO DE ARQUIVOS.md`

Esses não são “tarefinhas”; são alavancas de sistema. Se forem bem resolvidos, reduzem bagunça futura.

### Itens que precisam de contexto humano

1. `- VENDE-C.md`
2. `MOVIMENTAR CONTA BBMD.md`
3. `REGISTRO HTTPSMEDIA.XTILES.APP4561E4E6B61FF9646E46EF34.md`
4. `- PLANE DE SERVICOS.md`

A Arca não deve decidir sozinha porque falta significado ou risco.

### Itens prováveis de arquivamento

1. `TESTE DE REATIVAÇÃO 12H01.md`
2. `teste-loh.md`
3. `- Sempre analizar e redefinir conteúdos para os Clientes.md` — se a ideia não for recriada.

## 6. Distribuição por frente

### Central Pessoal / Arca

- `- MOVIMENTAR O FIO DA MEMORIA.md`
- `CRIAR UM CABECALHO NO TOPO MD. COM AS INFORMACOES PRINCIPAIS.md`
- `PASTAS DELETADAS - REVISITAR.md`
- `- CONTINUAR A ORGANIZACAO DE ARQUIVOS.md`

### LÓGIKA / Jarvis

- `- DAR SEGUIMENTO AO PLANO SE SERVIÇOS.md`
- `- PLANE DE SERVICOS.md`
- `- MANDAR ORÇAMENTO PARA QUIEL, KAUA E LIDIO.md`
- `- PREPARAR LANÇAMENTO DO VIDEO CLIPE.md`
- `CRIAR TEMPLATES DE PRODUCAO DE EDICAO DE VIDEOS E STORIES AT.md`
- `- Sempre analizar e redefinir conteúdos para os Clientes.md`
- `- RESPONDER BETO SAARA.md` — se for cliente/comercial.

### Secretaria / Saúde

- `MANDAR DADOS PARA ASCO DOS SERVIÇOS QUE A SECRETARIA FAZ.md`
- `CRIAR UM SISTEMA DE FICHA ONLINE PARA A SECRETARIA.md`
- `CONSULTAS CIRURGIÃO GERAL PARA A TRIAGEM DE OUTRA - 02.06.md`

### Estudos / implementação pessoal

- `CURSOS E IMPLEMENTACOES URGENTES PARA CONCLUIR E RODAR.md`

### Finanças / My Finance

- `MOVIMENTAR CONTA BBMD.md`

### Testes / limpeza

- `TESTE DE REATIVAÇÃO 12H01.md`
- `teste-loh.md`

## 7. Diagnóstico da matriz atual

A matriz atual do Inbox é boa como captura inicial, mas precisa evoluir. Ela pergunta apenas se o item é tarefa, ideia ou projeto. Para o sistema do Jadielson, isso é pouco.

A matriz ideal precisa responder sete perguntas:

1. O que é isto?
2. A qual frente pertence?
3. Quem é o dono?
4. Qual é a próxima ação física?
5. É tarefa, projeto, sistema, referência ou lixo?
6. Exige resposta para alguém?
7. Pode ser movido, ou precisa de confirmação humana?

Sem essas perguntas, o Inbox continua acumulando títulos vagos.

## 8. Matriz recomendada para o novo padrão do Inbox

Cada item novo do Inbox deveria ter este bloco mínimo:

```markdown
## Triagem Arca

**Status:** bruto | triado | em andamento | encerrado | arquivar
**Frente:** pessoal | LÓGIKA | saúde | câmara | sindss | estudos | finanças | segundo-cérebro | indefinido
**Tipo:** tarefa | projeto | sistema | referência | decisão | teste/lixo
**Destino 5D:** FOCO | DELEGAR | SISTEMA | BLOCO | CORTAR
**Dono:** Jadielson | Arca | Alfred | Jarvis | My Finance | Estudos | outro
**Urgência:** alta | média | baixa
**Próxima ação:** 
**Precisa de confirmação humana?** sim | não
**Destino sugerido:** 
```

## 9. Recomendação de execução em 3 rodadas

### Rodada 1 — Desafogar pendências externas

Resolver ou atualizar:

- orçamento para Quiel/Kauã/Lídio;
- responder Beto Saara;
- dados para ASCOM;
- consulta cirurgião geral;
- movimentar BBMD, somente após contexto.

Objetivo: tirar risco social/comercial/institucional do Inbox.

### Rodada 2 — Criar sistemas

Transformar em projetos F2:

- cabeçalho padrão de notas;
- fio da memória;
- templates de edição/vídeos/stories;
- organização de arquivos;
- ficha online da Secretaria.

Objetivo: não só limpar, mas melhorar a máquina.

### Rodada 3 — Limpeza segura

Arquivar ou revisar:

- testes;
- arquivo vazio de conteúdos para clientes;
- VENDE-C;
- CNPJ/link xtiles;
- pastas deletadas.

Objetivo: deixar o F0 só com captura viva.

## 10. O que a Arca pode fazer agora, se Jadielson autorizar

Sem mexer no F1 e sem apagar nada, a Arca pode:

1. criar uma cópia operacional desta matriz em F2 como base de triagem;
2. gerar uma lista de 5 perguntas para Jadielson responder sobre os itens ambíguos;
3. preparar propostas de notas-projeto para os itens de sistema;
4. criar o modelo padrão `Triagem Arca` para novas capturas;
5. só depois de aprovação, mover itens do F0 para destinos corretos.

## 11. Veredito

O Inbox de Jadielson não está desorganizado por excesso de arquivo. Ele está desorganizado por falta de decisão de destino.

A matriz correta deve transformar cada captura em uma destas saídas:

- tarefa executável;
- projeto planejável;
- sistema recorrente;
- referência arquivável;
- item descartável;
- encaminhamento para agente/frente correta.

Minha recomendação como Arca: começar pela Rodada 1, porque existem pendências com pessoas/instituições; depois transformar os itens estruturais em sistemas. A limpeza final vem por último.
