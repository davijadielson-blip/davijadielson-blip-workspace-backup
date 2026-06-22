---
tipo: mapa
subtipo: skills-e-comandos
gerado-por: claude
revisado: true
criado-em: 2026-05-16
ultimo-update: 2026-05-16
---

# Mapa de Skills — Quando Usar Cada Uma

> Este arquivo responde "qual skill invocar em qual situação" — para não ter que lembrar nomes na hora.
> Atualizar sempre que nova skill for adicionada ou situação nova for identificada.

---

## Camada 1 — Skills do Vault (em `skills/`)

Skills portáveis, funcionam em qualquer LLM que leia Markdown.

| Situação | Skill | Como invocar | Frequência |
|---|---|---|---|
| Iniciar sessão de trabalho novo / trocar de LLM | `cerebro` | Digite "cerebro" | Toda nova sessão significativa |
| Planejar o dia — Top 3 + tracker de frentes | `rotina` | Digite "rotina" | Todo dia antes de começar |
| Fechar sessão — commit, push, log, pendências | `salve` | Digite "salve" | Fim de cada sessão de trabalho |
| Trocar de LLM — reindexar contexto do vault | `reindex` | Digite "reindex" | Sempre que mudar de IA |
| Processar item bruto da inbox para nota estruturada | `parse-captura` | Digite "parse-captura" | Quando processar `[F0] 0-Inbox/` |

---

## Camada 2 — Pack de Skills Estratégicas (referenciadas)

> Estas skills foram documentadas no plano do Sistema Operacional Pessoal como **objetivo futuro** — ainda não implementadas.
> Quando criadas, salvar em `skills/` e mover para a Camada 1.
> Por enquanto, usar como referência de intenção ao planejar automações.

| Situação | Skill | Quando invocar |
|---|---|---|
| Identifiquei processo repetitivo na [[../databases/matriz-tarefas\|Matriz]] (⚙️ SISTEMA) | `mapa-de-oportunidades-de-automacao` | Toda vez que aparecer tarefa nova marcada ⚙️ SISTEMA |
| Quero avaliar onde IA economiza mais tempo | `scanner-de-processos-com-impacto-de-ia` | A cada 30 dias — revisão da Semana 4 do [[../projects/plano-30-dias-diretor\|Plano]] |
| Criei prompt que vou repetir muitas vezes | `cofre-de-prompts-para-operacao-com-ia` | Sempre que perceber que estou repetindo o mesmo prompt |
| Vou padronizar checklist ou processo repetitivo | `sop-operacional-escalavel` | Semana 2 do plano 30 dias (padronização) e sempre que ⚙️ SISTEMA virar SOP |
| Subagent errou tom, contexto ou personagem | `forja-de-system-prompts-para-ia-customizada` | Quando subagent receber feedback negativo em revisão |
| Vou decidir se automatizo ou contrato | `roi-de-implementacao-de-ia-com-payback` | Antes de qualquer decisão de automação ou ferramenta nova |
| Vou contratar alguém pra delegar | `descricao-de-vaga-magnetica` | Quando Ewander migrar pro Notion OU quando contratar substituto |
| Manutenção geral do segundo cérebro | `obsidian-second-brain` | Toda sexta (friday-maintenance) — audit de notas órfãs, duplicatas |

---

## Camada 3 — Slash Commands por Situação

### Produção de Conteúdo

| Situação | Comando | Frente |
|---|---|---|
| Gerar legenda com hashtags + manchete WhatsApp | `/legenda` | Qualquer frente |
| Post da Secretaria de Saúde | `/post-saude` | SMS |
| Post da Câmara Municipal | `/post-camara` | Câmara |
| Post do SINDSS | `/post-sindss` | SINDSS |
| Post da Lógika Creative | `/post-logika` | Lógika |
| Post do Rogério Rocha (mandato) | `/post-rogerio` | Rogério |
| Roteiro de vídeo completo Rogério | `/roteiro-rogerio` | Rogério |
| Manchete WhatsApp de legenda existente | `/resumo-whats` | Qualquer frente |

### Captura e Organização

| Situação | Comando |
|---|---|
| Captura rápida de ideia/texto | `/captura` |
| Registrar ideia na frente correta | `/ideia` |
| Abrir ou criar daily de hoje com Calendar | `/hoje` |
| Ver todos os drafts pendentes de revisão | `/revisar` |

### Agenda e Calendar

| Situação | Comando |
|---|---|
| Ver agenda dos próximos N dias | `/agenda` |
| Criar evento com confirmação | `/agendar` |
| Detectar conflitos de agenda | `/conflitos-agenda` |
| Ver agenda filtrada por frente | `/agenda-frente` |
| Cruzar Calendar com Gmail | `/agenda-email` |
| Criar blocos recorrentes de rotina | `/bloquear-rotina` |
| Sincronizar datas sazonais no Calendar | `/sincronizar-sazonais` |

### Fontes Externas

| Situação | Comando |
|---|---|
| Ver e-mails das últimas 24h por frente | `/inbox` |
| Filtrar Gmail por cliente específico | `/inbox-cliente` |
| Ver arquivos Drive modificados recentemente | `/drive-recente` |
| Buscar arquivo no Drive | `/drive-buscar` |
| Arquivar referência de arquivo do Drive | `/drive-arquivo` |
| Processar exportação .txt do WhatsApp | `/whats-importar` |
| Transcrever áudio com Whisper | `/audio-importar` |
| Forçar sync Notion → Calendar | `/sync-notion-calendar` |

### Inteligência do Vault

| Situação | Comando |
|---|---|
| Buscar tema em todo o vault | `/busca` |
| Encontrar conexão entre dois temas | `/conecta` |
| Ver datas sazonais próximas por frente | `/sazonal` |
| Ver aniversariantes da SMS do mês | `/aniversariante` |
| Importar planilha financeira | `/financeiro` |

### Planejamento e Gestão

| Situação | Comando |
|---|---|
| Cruzamento Gmail + Drive + Calendar → Top 3 | `/prioridades` |
| Ritual de domingo — nota semanal completa | `/planejar-semana` |
| Ritual de sexta — manutenção do vault | `/manutencao` |
| Gerar cockpit.html e abrir no browser | `/cockpit` |

---

## Camada 4 — Subagents por Frente

> Invocar com `@nome` ou deixar o Claude decidir pela frente do contexto.

| Frente | Subagent | Nunca usar para |
|---|---|---|
| Lógika Creative | `@logika` | Conteúdo de clientes políticos |
| Rogério Rocha (mandato) | `@rogerio` | Qualquer menção a eleição |
| Secretaria de Saúde | `@saude` | Conteúdo político |
| Câmara Municipal (instituição) | `@camara` | Post individual de vereador |
| SINDSS | `@sindss` | Fora do calendário editorial |
| Josi / Vando / Manoel (individual) | `@vereadores` | Câmara como instituição |
| Canal Além da Foto | `@alem-da-foto` | Conteúdo comercial ou político |
| Lives de Louvor | `@lives-louvor` | Polêmica doutrinária |
| Vida pessoal | `@pessoal` | Qualquer frente profissional |
| Organização e busca no vault | `@bibliotecaria` | Geração de conteúdo de frente |

---

## Hooks de Skills — Gatilhos Automáticos

> Situações que devem disparar sugestão de skill automaticamente.

```
📌 Quando nova tarefa entrar na Matriz com destino ⚙️ SISTEMA:
   → sugerir: sop-operacional-escalavel (documentar antes de esquecer)

📌 Quando identificar 3+ ocorrências do mesmo prompt em [F2] memory/sessions/:
   → sugerir: cofre-de-prompts-para-operacao-com-ia (cristalizar o prompt)

📌 Quando subagent receber feedback negativo em revisão de output:
   → sugerir: forja-de-system-prompts-para-ia-customizada (refinar o prompt)

📌 Quando avaliar nova automação, ferramenta ou contratação:
   → invocar: roi-de-implementacao-de-ia-com-payback (calcular antes de decidir)

📌 Quando chegar à Semana 3 do plano (30/05):
   → invocar: descricao-de-vaga-magnetica (preparar para delegar)

📌 Quando o cockpit mostrar horas institucionais > 20h/sem:
   → acionar: Regra Zero-Sum (ver [F2] memory/context/rotina.md)

📌 Toda sexta, no friday-maintenance:
   → verificar: obsidian-second-brain (notas órfãs, duplicatas, links quebrados)
```

---

## Hierarquia de Decisão

```
Tenho uma tarefa nova:
  ↓
1. Existe slash command específico? → usar o comando
2. A tarefa envolve uma frente específica? → invocar @subagent
3. É uma decisão estratégica ou processo a padronizar? → consultar este mapa (Camada 2)
4. É organização/busca no vault? → @bibliotecaria
5. Nada se aplica → Claude principal
```

---

## Conexões

- [[../CLAUDE.md]] — hierarquia completa do sistema
- [[visualizations/Hub]] — central de comando
- [[../databases/matriz-tarefas]] — toda tarefa ⚙️ SISTEMA gera gatilho aqui
- [[../projects/plano-30-dias-diretor]] — semana 2 e 3 ativam skills estratégicas

---

*Criado: 2026-05-16 · Atualizar ao adicionar nova skill ou comando*
