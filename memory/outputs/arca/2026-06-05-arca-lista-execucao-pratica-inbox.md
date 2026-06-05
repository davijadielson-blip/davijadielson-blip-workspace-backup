---
tipo: output
subtipo: lista-execucao-pratica-inbox
gerado-por: arca
supervisionado-por: Alfred
integrado-com: Lôh
revisado: false
data: 2026-06-05
status-colheita: candidato-operacional
origem: continuação da matriz completa de triagem do Inbox
---

# Lista de execução prática — Inbox F0

## 1. Objetivo

Transformar a matriz completa de triagem do Inbox em uma sequência prática de ações, começando pelas pendências externas mais sensíveis e avançando para sistemas, revisão e limpeza.

Regra de segurança: esta lista não move, apaga nem edita arquivos do F0. Ela organiza o que deve ser feito e quais decisões Jadielson precisa confirmar.

## 2. Visão geral da execução

A triagem deve acontecer em 4 blocos:

1. **Bloco A — Pendências externas urgentes:** itens que envolvem resposta para pessoas, cliente, Secretaria ou dinheiro.
2. **Bloco B — Sistemas estruturais:** itens que não são tarefa simples; viram padrão, projeto ou rotina.
3. **Bloco C — Ambíguos:** itens que precisam de resposta curta de Jadielson antes da Arca decidir destino.
4. **Bloco D — Limpeza segura:** testes, arquivo vazio e registros que podem ser arquivados depois de confirmação.

## 3. Bloco A — Pendências externas urgentes

### A1 — Orçamentos para Quiel, Kauã e Lídio

- **Arquivo:** `- MANDAR ORÇAMENTO PARA QUIEL, KAUA E LIDIO.md`
- **Frente:** LÓGIKA / comercial
- **Risco se ficar parado:** perda de oportunidade ou ruído comercial.
- **Dono sugerido:** Jadielson + Jarvis quando LÓGIKA estiver operacional.
- **Próxima ação prática:** Jadielson responder se esses orçamentos ainda estão pendentes.

**Pergunta para Jadielson:**

> Esses orçamentos para Quiel, Kauã e Lídio ainda precisam ser enviados? Se sim, são três orçamentos diferentes ou uma mesma proposta adaptada?

**Se SIM:** Arca/Jarvis deve preparar uma lista de dados necessários:

- serviço solicitado;
- valor ou faixa;
- prazo;
- forma de pagamento;
- mensagem curta para envio.

**Destino depois:** LÓGIKA / Comercial / Propostas.

---

### A2 — Responder Beto Saara

- **Arquivo:** `- RESPONDER BETO SAARA.md`
- **Frente:** comunicação / possível cliente ou contato pessoal.
- **Risco se ficar parado:** deixar pessoa sem resposta.
- **Dono sugerido:** Jadielson.
- **Próxima ação prática:** confirmar se já respondeu.

**Pergunta para Jadielson:**

> Você já respondeu Beto Saara? Se não, ele é contato pessoal, cliente ou assunto institucional?

**Se ainda não respondeu:** preparar uma resposta curta em 3 versões:

1. direta;
2. cordial;
3. profissional/comercial.

**Destino depois:** executar e arquivar como tarefa encerrada.

---

### A3 — Mandar dados para ASCOM dos serviços da Secretaria

- **Arquivo:** `MANDAR DADOS PARA ASCO DOS SERVIÇOS QUE A SECRETARIA FAZ.md`
- **Frente:** Secretaria de Saúde / ASCOM.
- **Risco se ficar parado:** atraso institucional/comunicação pública.
- **Dono sugerido:** Jadielson / frente Saúde.
- **Próxima ação prática:** levantar quais dados a ASCOM pediu.

**Pergunta para Jadielson:**

> Esses dados para a ASCOM ainda estão pendentes? Quais serviços precisam entrar: nomes dos serviços, horários, locais, responsáveis, contatos ou todos?

**Se SIM:** montar uma checklist de coleta:

- nome do serviço;
- local de atendimento;
- horário;
- público atendido;
- profissional/responsável;
- documentos necessários;
- contato/fluxo de marcação.

**Destino depois:** Frente Saúde / ASCOM / Conteúdo ou referência institucional.

---

### A4 — Consultas cirurgião geral / triagem 02.06

- **Arquivo:** `CONSULTAS CIRURGIÃO GERAL PARA A TRIAGEM DE OUTRA - 02.06.md`
- **Frente:** Secretaria de Saúde.
- **Risco se ficar parado:** pode ser demanda vencida ou registro útil não arquivado.
- **Dono sugerido:** Jadielson / frente Saúde.
- **Próxima ação prática:** checar se a data 02/06 já foi resolvida.

**Pergunta para Jadielson:**

> Essa triagem de cirurgião geral do dia 02/06 já aconteceu e pode virar registro, ou ainda tem continuidade/pendência?

**Se já aconteceu:** arquivar como registro de saúde.

**Se ainda tem continuidade:** transformar em demanda ativa com:

- data;
- local;
- quantidade de consultas;
- responsável;
- próxima comunicação necessária.

**Destino depois:** Frente Saúde / Atendimento / Triagens ou Conteúdo institucional.

---

### A5 — Movimentar conta BBMD

- **Arquivo:** `MOVIMENTAR CONTA BBMD.md`
- **Frente:** finanças / administrativo.
- **Risco se ficar parado:** financeiro, mas não dá para agir sem contexto.
- **Dono sugerido:** Jadielson + My Finance quando configurado.
- **Próxima ação prática:** entender o que é BBMD e qual movimento precisa ser feito.

**Pergunta para Jadielson:**

> O que é BBMD e que tipo de movimentação precisa fazer? É pagamento, transferência, conferência, aplicação, cobrança ou só lembrete?

**Regra de segurança:** nenhuma automação financeira deve ser feita sem confirmação explícita.

**Destino depois:** My Finance / Contas / Pendências.

## 4. Bloco B — Sistemas estruturais

### B1 — Cabeçalho padrão das notas Markdown

- **Arquivo:** `CRIAR UM CABECALHO NO TOPO MD. COM AS INFORMACOES PRINCIPAIS.md`
- **Frente:** Segundo Cérebro / Arca.
- **Valor:** alto. Facilita leitura por IA, busca, automação e organização.
- **Próxima ação prática da Arca:** criar um modelo de cabeçalho padrão para novas notas.

**Proposta mínima:**

```yaml
---
tipo:
frente:
status:
origem:
data:
revisado: false
responsavel:
tags: []
---
```

**Cuidado:** não aplicar automaticamente em todas as notas F1 sem aprovação. Primeiro criar padrão em F2.

---

### B2 — Fio da Memória

- **Arquivo:** `- MOVIMENTAR O FIO DA MEMORIA.md`
- **Frente:** Segundo Cérebro / Arca.
- **Valor:** alto. Pode virar ritual semanal de revisão e continuidade.
- **Próxima ação prática da Arca:** definir o que entra no Fio da Memória.

**Proposta:**

O Fio da Memória deve registrar:

- decisões importantes;
- pendências que continuam abertas;
- ideias que voltam muitas vezes;
- aprendizados sobre como Jadielson trabalha;
- candidatos à Colheita;
- links entre projetos e frentes.

**Destino depois:** rotina semanal da Arca, supervisionada por Alfred.

---

### B3 — Templates de produção de edição de vídeos e stories

- **Arquivo:** `CRIAR TEMPLATES DE PRODUCAO DE EDICAO DE VIDEOS E STORIES AT.md`
- **Frente:** LÓGIKA / Produção.
- **Valor:** muito alto. Reduz retrabalho.
- **Próxima ação prática:** transformar em projeto com escopo mínimo.

**Primeiro pacote sugerido:**

1. template de Reels institucional;
2. template de Stories de cobertura;
3. template de chamada/evento;
4. template de depoimento;
5. checklist de exportação.

**Destino depois:** LÓGIKA / Produção / Templates.

---

### B4 — Organização de arquivos

- **Arquivo:** `- CONTINUAR A ORGANIZACAO DE ARQUIVOS.md`
- **Frente:** organização digital / Lôh + Arca.
- **Valor:** alto, mas perigoso se feito no impulso.
- **Próxima ação prática:** criar um plano de organização sem mover arquivos ainda.

**Primeiro passo seguro:** inventariar áreas bagunçadas e criar regra de nomes/pastas antes de mexer.

**Destino depois:** projeto de organização digital.

---

### B5 — Sistema de ficha online para a Secretaria

- **Arquivo:** `CRIAR UM SISTEMA DE FICHA ONLINE PARA A SECRETARIA.md`
- **Frente:** Secretaria de Saúde.
- **Valor:** alto, mas envolve dados sensíveis.
- **Próxima ação prática:** definir escopo e limites.

**Perguntas mínimas:**

- ficha para qual serviço?
- vai coletar dados pessoais/sensíveis?
- quem acessa?
- qual ferramenta será usada?
- precisa autorização institucional?

**Regra de segurança:** não criar formulário real com dados sensíveis sem confirmação clara.

## 5. Bloco C — Itens ambíguos que precisam de resposta curta

### C1 — VENDE-C

- **Arquivo:** `- VENDE-C.md`
- **Pergunta:** o que significa “VENDE-C”? É venda, produto, cliente, curso, campanha ou código antigo?
- **Se Jadielson não lembrar:** arquivar como item sem contexto.

### C2 — PLANE DE SERVICOS

- **Arquivo:** `- PLANE DE SERVICOS.md`
- **Pergunta:** isso é duplicado de “plano de serviços” ou é outra coisa?
- **Se for duplicado:** consolidar com o item `- DAR SEGUIMENTO AO PLANO SE SERVIÇOS.md`.

### C3 — Registro xtiles / CNPJ

- **Arquivo:** `REGISTRO HTTPSMEDIA.XTILES.APP4561E4E6B61FF9646E46EF34.md`
- **Pergunta:** esse CNPJ é da LÓGIKA, de cliente ou de outro contexto?
- **Se for LÓGIKA:** mover depois para referência empresarial.
- **Se for cliente:** mover depois para pasta do cliente/frente correta.
- **Se não tiver utilidade:** arquivar.

### C4 — Arquivo vazio de conteúdos para clientes

- **Arquivo:** `- Sempre analizar e redefinir conteúdos para os Clientes.md`
- **Pergunta:** quer recriar isso como princípio editorial da LÓGIKA?
- **Se sim:** transformar em checklist de revisão de conteúdo.
- **Se não:** arquivar por estar vazio.

## 6. Bloco D — Limpeza segura

Estes itens parecem seguros para arquivamento depois de confirmação:

1. `TESTE DE REATIVAÇÃO 12H01.md`
2. `teste-loh.md`

Item para revisão, não descarte imediato:

3. `PASTAS DELETADAS - REVISITAR.md`

**Recomendação:** criar uma pasta de arquivamento recuperável para testes, não deletar permanente.

## 7. Checklist de execução sugerida para Jadielson

### Primeiro checkpoint — responder só 8 perguntas

Jadielson pode responder em áudio ou texto, na ordem:

1. Orçamentos para Quiel/Kauã/Lídio ainda estão pendentes?
2. Beto Saara já foi respondido? Ele é cliente, pessoal ou institucional?
3. Dados para ASCOM ainda precisam ser enviados? Quais dados?
4. A triagem de cirurgião de 02/06 já passou ou ainda tem continuidade?
5. O que é BBMD e qual movimentação precisa?
6. O que significa VENDE-C?
7. PLANE DE SERVIÇOS é duplicado do plano de serviços?
8. O CNPJ/link xtiles é de quem?

### Segundo checkpoint — Arca executa organização F2

Depois dessas respostas, a Arca pode preparar:

- lista final de ações externas;
- rascunhos de mensagens quando necessário;
- projetos F2 dos sistemas estruturais;
- proposta de arquivamento seguro dos testes;
- mapa de destino para cada arquivo do F0.

### Terceiro checkpoint — mover arquivos só com autorização

Somente depois da conferência, mover ou arquivar arquivos do F0.

## 8. Próxima ação recomendada agora

A Arca recomenda começar com uma pergunta única, para destravar o bloco mais urgente:

> Jadielson, dos itens externos, quais ainda estão pendentes hoje: orçamento Quiel/Kauã/Lídio, Beto Saara, ASCOM, cirurgião 02/06 e BBMD?

Com essa resposta, a Arca consegue montar a lista de execução real, sem depender de suposição.
