# Prompt — Notion criar Mission Control — Backlog Inteligente v5

**Data:** 2026-07-20  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Uso:** copiar e colar no Notion AI para criar a página/sistema.

---

## Prompt para Notion AI

Crie uma página no Notion chamada **Backlog Inteligente — Mission Control v5**.

Quero um sistema de organização pessoal para capturar, organizar, priorizar, agendar, executar e revisar demandas. O sistema precisa funcionar para uma mente com TDAH/energia variável, então deve ser visual, simples, prático e com baixa fricção.

Não quero apenas uma matriz de tarefas. Quero um sistema hierárquico de organização:

```text
Área / Tema → Projeto → Subprojeto → Tarefa → Subtarefa / Próxima ação
```

A página deve funcionar como um painel central com links para bancos de dados e visões filtradas.

---

# Estrutura da página principal

Crie as seguintes seções na página:

1. **Dashboard — Hoje**
2. **Inbox — Captura Bruta**
3. **Áreas / Temas**
4. **Projetos**
5. **Subprojetos**
6. **Tarefas**
7. **Agenda / Tempo**
8. **Matriz Eisenhower**
9. **Esforço x Impacto**
10. **Travados / Protocolo 10 min**
11. **Revisão Semanal**
12. **Templates**
13. **Organizar com IA**

Use callouts, divisores, headings, toggles e visual limpo.

---

# Bancos de dados necessários

Crie estes bancos de dados no Notion:

## 1. Banco de dados: Áreas

Propriedades:
- **Nome** — title
- **Função** — text
- **Status** — select: Ativa, Atenção, Pausada, Encerrada
- **Projetos** — relation com Projetos
- **Observações** — text

Registros iniciais:
- Saúde / Energia
- Família
- Estudos
- Finanças
- Projetos pessoais
- Trabalho / LÓGIKA — manter separado por parede-d'água
- Organização / Sistemas

---

## 2. Banco de dados: Projetos

Propriedades:
- **Projeto** — title
- **Área** — relation com Áreas
- **Objetivo** — text
- **Resultado desejado** — text
- **Status** — select: Ativo, Pausado, Incubado, Concluído, Cancelado
- **Prioridade** — select: P1, P2, P3
- **Prazo macro** — date
- **Próxima ação** — text
- **Subprojetos** — relation com Subprojetos
- **Tarefas** — relation com Tarefas
- **Links** — url ou text

Registro exemplo:
- Projeto: Backlog Inteligente v5
- Área: Estudos / Organização
- Objetivo: criar sistema pessoal de execução
- Status: Ativo
- Prioridade: P1
- Próxima ação: montar painel Notion v0

---

## 3. Banco de dados: Subprojetos

Propriedades:
- **Subprojeto** — title
- **Projeto pai** — relation com Projetos
- **Objetivo** — text
- **Status** — select: Ativo, Pausado, Incubado, Concluído
- **Próxima ação** — text
- **Tarefas** — relation com Tarefas

Registros exemplo:
- Painel 1 Página — Projeto pai: Backlog Inteligente v5
- Integração Notion/Cofre — Projeto pai: Backlog Inteligente v5
- Teste piloto 7 dias — Projeto pai: Backlog Inteligente v5

---

## 4. Banco de dados: Tarefas

Propriedades:
- **Tarefa** — title
- **Área** — relation com Áreas
- **Projeto** — relation com Projetos
- **Subprojeto** — relation com Subprojetos
- **Responsável** — person ou text
- **Status** — select: Capturada, Esclarecida, Fatiada, Agendada, Executando, Concluída, Incubada, Descartada
- **Prioridade** — select: P1, P2, P3
- **Impacto** — select: Alto, Médio, Baixo
- **Complexidade** — select: Fácil, Média, Difícil
- **Energia** — select: Leve, Média, Pesada
- **PG/PD** — select: PG, PD, Essencial, Incubação
- **Prazo de execução** — date
- **Prazo de entrega** — date
- **Próxima ação** — text
- **Critério de concluído** — text
- **Padrão de trava** — select: Nenhum, Perfeição, Hiperfoco seletivo, Evitação emocional, Superestimação de tempo, Sobrecarga de início, Revisão infinita, Colapso pós-esforço
- **Delegável** — select: Sim, Não, Talvez
- **Eisenhower** — select: Fazer agora, Planejar, Delegar, Revisar/Eliminar
- **Esforço x Impacto** — select: Quick Win, Planejar para fazer, Executar quando possível, Possibilidade de descarte
- **Tipo** — select: Tarefa, Compromisso, Ideia, Preocupação, Decisão
- **Links** — url ou text

Inclua uma descrição na database:

```text
Fórmula da tarefa boa: Verbo + objeto + contexto + critério de conclusão + prazo de execução.
```

---

## 5. Banco de dados: Agenda / Blocos

Propriedades:
- **Item** — title
- **Tipo** — select: Compromisso, Bloco de foco, Bloco de estudo, Bloco financeiro, Bloco mensagens, Família, Descanso
- **Data e horário** — date
- **Tarefa vinculada** — relation com Tarefas
- **Preparação necessária** — text
- **Status** — select: Agendado, Feito, Reagendado, Cancelado

Inclua a regra:

```text
Compromisso tem horário fixo. Tarefa precisa de bloco de execução.
```

---

## 6. Banco de dados: Revisões Semanais

Propriedades:
- **Semana** — title
- **Data da revisão** — date
- **O que avancei** — text
- **O que ficou parado** — text
- **O que está atrasado** — text
- **Principal padrão de trava** — select: Perfeição, Hiperfoco seletivo, Evitação emocional, Superestimação de tempo, Sobrecarga de início, Revisão infinita, Colapso pós-esforço
- **Microvitória PG** — text
- **PD crítica** — text
- **Funcionou 70%?** — checkbox
- **O que cortar/delegar/incubar** — text
- **Próxima semana** — text

---

# Visões filtradas na página principal

Na página principal, crie links/embeds ou views filtradas:

## Dashboard — Hoje

Criar uma visão da database Tarefas filtrada por:
- Prazo de execução é hoje; ou
- Status não é Concluída/Descartada; e
- Prioridade P1/P2.

Mostrar propriedades:
- Tarefa
- Projeto
- Prioridade
- Energia
- Próxima ação
- Padrão de trava

Também criar blocos manuais:

### Tarefa #1 do dia
- Tarefa:
- Próxima ação:
- Bloco de execução:
- Energia necessária:
- Critério de concluído:

### 3 prioridades de hoje
1.
2.
3.

### Fechamento do dia
- O que concluí:
- O que ficou aberto:
- 3 prioridades de amanhã:

---

## Inbox — Captura Bruta

Criar uma visão da database Tarefas filtrada por:
- Status = Capturada.

Texto de apoio:

```text
Não decidir demais na captura. Só tirar da cabeça.
Depois classificar em: Área → Projeto → Subprojeto → Tarefa → Próxima ação.
```

---

## Projetos e Subprojetos

Criar visualizações:
- Projetos por status.
- Projetos por área.
- Subprojetos agrupados por projeto pai.

---

## Matriz Eisenhower

Criar uma board view da database Tarefas agrupada por **Eisenhower** com colunas:
- Fazer agora
- Planejar
- Delegar
- Revisar/Eliminar

Cores sugeridas:
- Fazer agora: vermelho/rosa
- Planejar: azul/verde
- Delegar: amarelo
- Revisar/Eliminar: cinza

---

## Esforço x Impacto

Criar uma board view da database Tarefas agrupada por **Esforço x Impacto** com colunas:
- Quick Win
- Planejar para fazer
- Executar quando possível
- Possibilidade de descarte

---

## Travados / Protocolo 10 min

Criar uma visão da database Tarefas filtrada por:
- Padrão de trava não é Nenhum; ou
- Status = Incubada/Fatiada e sem avanço.

Adicionar o protocolo:

```text
1. Nomear a tarefa travada.
2. Identificar o padrão de trava.
3. Reduzir para menor ação.
4. Preparar ambiente.
5. Executar 10 minutos.
6. Decidir: continuar, pausar, reagendar ou descartar.
```

---

## Revisão Semanal

Criar template de nova revisão com perguntas:

1. O que avancei?
2. O que ficou parado?
3. O que está atrasado?
4. O que está travado?
5. Qual foi meu principal padrão de trava?
6. Qual foi minha maior microvitória PG?
7. Qual PD crítica precisa de atenção?
8. O sistema funcionou 70%?
9. O que corto, delego ou incubo?
10. O que entra na próxima semana?

Inclua a frase:

```text
Rotina 70% funcional é melhor que rotina perfeita abandonada.
```

---

# Templates internos

Crie templates para:

1. Nova tarefa
2. Novo projeto
3. Novo subprojeto
4. Compromisso
5. Revisão diária
6. Revisão semanal
7. Protocolo 10 minutos
8. Painel 1 Página

---

# Seção “Organizar com IA”

Crie uma seção com este prompt para eu usar dentro do Notion:

```text
Quando eu enviar uma lista solta, classifique cada item como área, projeto, subprojeto, tarefa, compromisso, ideia ou preocupação.

Para cada item:
1. Reescreva com clareza.
2. Se for tarefa, comece com verbo.
3. Defina área, projeto e subprojeto quando possível.
4. Sugira próxima ação.
5. Sugira prioridade P1/P2/P3.
6. Sugira impacto, complexidade e energia.
7. Sugira Eisenhower e Esforço x Impacto.
8. Sugira se entra em Hoje, Semana, Backlog, Agenda, Travados ou Incubação.
9. Se estiver vago, faça perguntas de clareza.
10. Se estiver travado, aplique o Protocolo 10 min.
```

---

# Estilo visual

Use:
- página limpa;
- seções com emojis discretos;
- callouts para regras importantes;
- bancos de dados relacionados;
- boards para matrizes;
- tabelas para projetos e tarefas;
- visual simples para uso diário.

O resultado deve parecer um **Mission Control pessoal**, não uma planilha pesada.
