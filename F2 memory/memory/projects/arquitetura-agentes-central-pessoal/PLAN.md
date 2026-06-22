# Plano: Configuração dos agentes da Central Pessoal

> Criado em 2026-06-05. Status: planejamento/execução.

## Objetivo

Configurar a Central Pessoal como primeiro grupo operacional da arquitetura de agentes, com Alfred como General local e quatro especialistas: Segundo Cérebro, My Finance, Projetos Pessoais e Estudos. A prioridade é deixar função, limites, tom, thread_id/topic_id, prompt e rotina mínima de heartbeat/crons definidos antes de seguir para LÓGIKA/Jarvis.

## Sucesso =

- [ ] Alfred configurado como General da Central Pessoal.
- [ ] Todos os tópicos/agentes da Central Pessoal confirmados por Jadielson.
- [ ] `thread_id/topic_id` de cada tópico registrado.
- [ ] Prompt operacional final de cada agente salvo.
- [ ] Parede-d'água pessoal × LÓGIKA registrada.
- [ ] Heartbeat/checklist mínimo definido.
- [ ] Backup do workspace feito após a configuração.

## Agentes previstos

1. Alfred — General/coordenador local da Central Pessoal.
2. Segundo Cérebro — organização de notas, ideias, mapas e memória pessoal.
3. My Finance — finanças pessoais, contas, orçamento e alertas.
4. Projetos Pessoais — projetos pessoais/transversais e priorização.
5. Estudos — estudos, resumos, mapas mentais e evolução técnica.

## Tarefas

### Fase 1: Inventário dos tópicos

- [ ] **T1.1** — Confirmar nomes finais dos 5 agentes.
  - Verificação: lista final aprovada por Jadielson.
  - Estimativa: 10min.
  - Depende de: nenhuma.
  - Progresso: Alfred confirmado como General da Central Pessoal; Arca confirmado como agente do Segundo Cérebro.

- [ ] **T1.2** — Capturar `thread_id/topic_id` de cada tópico da Central Pessoal.
  - Verificação: cada agente com tópico registrado em `agentes/ARQUITETURA-AGENTES.md`.
  - Estimativa: 15-30min.
  - Depende de: Jadielson mandar mensagem em cada tópico ou informar os IDs.
  - Progresso: Alfred registrado como `topic_id: 1`; Arca / Segundo Cérebro registrado como `topic_id: 13`; My Finance registrado como `topic_id: 12`.

### Fase 2: Prompts e limites

- [ ] **T2.1** — Fechar prompt final do Alfred.
  - Verificação: prompt salvo no documento de arquitetura.
  - Estimativa: 20min.
  - Depende de: T1.1.

- [ ] **T2.2** — Fechar prompts finais dos 4 especialistas.
  - Verificação: prompts salvos no documento de arquitetura.
  - Estimativa: 40-60min.
  - Depende de: T1.1.

- [ ] **T2.3** — Registrar parede-d'água Central Pessoal × LÓGIKA.
  - Verificação: regra explícita salva no documento.
  - Estimativa: 10min.
  - Depende de: nenhuma.

### Fase 3: Rotina mínima

- [ ] **T3.1** — Definir heartbeat/checklist da Central Pessoal.
  - Verificação: `HEARTBEAT.md` atualizado com checagens leves e seguras.
  - Estimativa: 15min.
  - Depende de: T1.1.

- [ ] **T3.2** — Definir quais agentes precisam cron agora e quais ficam só sob demanda.
  - Verificação: tabela de crons planejados/adiados salva.
  - Estimativa: 15min.
  - Depende de: T2.2.

### Fase 4: Aplicação técnica

- [ ] **T4.1** — Verificar forma correta de configurar roteamento/personas por tópico no OpenClaw.
  - Verificação: config/schema/documentação consultados antes de alteração.
  - Estimativa: 20-40min.
  - Depende de: T1.2 e prompts finais.
  - Progresso: schema consultado em `channels.telegram.groups.*.topics.*` e `agents.list.*`; campos relevantes confirmados: `agentId`, `systemPrompt`, `requireMention`, `groupPolicy`, `agents.list[].systemPromptOverride`.

- [ ] **T4.2** — Aplicar configuração com backup.
  - Verificação: config validada/recarregada, agentes respondendo nos tópicos corretos.
  - Estimativa: 30-60min.
  - Depende de: T4.1.
  - Progresso: configuração individual aplicada em 2026-06-05 para Alfred (`1`), Warren (`12`), Arca (`13`) e links enviados (`224`, `221`, `222`, `219`, `218`, `11`) com agentes próprios por tópico. Backup de config criado antes da alteração.

## Dependências externas

- Jadielson precisa confirmar/criar os tópicos da Central Pessoal.
- Para capturar `thread_id`, idealmente Jadielson manda uma mensagem em cada tópico chamando a Lôh ou informando o nome do agente.
- Alterações reais de config devem ser feitas só depois de consultar schema/documentação e com backup.

## Riscos

- Misturar contexto pessoal com LÓGIKA.
  - Mitigação: parede-d'água explícita em todos os prompts.
- Criar agentes demais antes de validar Alfred.
  - Mitigação: Alfred primeiro, especialistas depois.
- Configurar crons demais e gerar ruído/custo.
  - Mitigação: começar com heartbeat leve e crons mínimos.

## Estado atual

- Arquitetura base já existe em `agentes/ARQUITETURA-AGENTES.md`.
- Alfred já foi definido por Jadielson como General da Central Pessoal.
- Chat da Central Pessoal conhecido: `-1003740871403`.
- Alfred registrado anteriormente como tópico `thread_id/topic_id: 1` no documento de arquitetura.
- Arca definido por Jadielson como agente especialista do Segundo Cérebro no tópico `thread_id/topic_id: 13`.
- My Finance confirmado como especialista de finanças pessoais no tópico `thread_id/topic_id: 12`; prompt inicial salvo em `agentes/ARQUITETURA-AGENTES.md`.
- Links enviados por Jadielson em 2026-06-05 foram configurados individualmente após captura dos títulos reais: `224` → `identidade-visao-futuro`; `221` → `liberdade-lazer-ocio`; `222` → `autoconhecimento`; `219` → `saude-corpo-energia`; `218` → `familia-relacionamentos`; `11` → `espiritualidade-propositos`.
- Próximo passo recomendado: testar uma mensagem real em cada tópico e ajustar tom/persona conforme Jadielson preferir.

---

*Atualizar este arquivo conforme execução. Não criar arquivo novo para o mesmo plano.*
