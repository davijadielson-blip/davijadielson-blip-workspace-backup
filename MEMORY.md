# MEMORY.md

## Dados do Jadielson

- **Localização:** São Sebastião, Alagoas (não Maceió)
- **Rodoviária local:** Terminal Rodoviário de São Sebastião, AL
- **Timezone:** America/Maceio

## 6 Pilares Estruturais — Secretaria de Saúde São Sebastião

**Rotação Editorial Semanal (segunda a sexta):**
1. **Segunda:** Atenção Básica/Território — PSF, ESF, atendimento de base
2. **Terça:** Serviços Especializados — consultas especializadas, referências
3. **Quarta:** Vigilância/Prevenção — campanhas, monitoramento, prevenção
4. **Quinta:** Rede de Apoio/Humanização — CAPS, grupos, suporte psicossocial
5. **Sexta:** Bastidores + Prestação de Contas — reportagem institucional, resultados
6. **+Flexível:** SAMU/Unidade Mista/Referências — emergência, fluxo urgente

**Regra:** essa sequência é a base do calendário editorial. Datas temáticas de saúde podem reforçar ou complementar, mas a rotação é mantida.

**Calendário Editorial Junho 2026:**
- **Arquivo:** `calendarios/calendario-editorial-saude-junho-2026.md`
- **Status:** ✅ Completo com 21 stories
- **Cobertura:** seg-sex rotativo + feriado 10/jun (Corpus Christi) adaptado
- **Temas:** saúde do homem (junho lilás/azul), saúde bucal, prevenção, campanhas
- **Criado em:** 2026-06-08 17:58 UTC por Jadielson + Lôh

## Produção — Roteiros + Personagens + Referências

**Status:** ✅ 100% OPERACIONAL (2026-06-08 18:07 UTC)

### Roteiros Semana 2 (08-12 Junho)
- **Arquivo:** `producao/roteiros-semana-2-junho-2026.md`
- **5 Stories:** Puericultura | Fluxo Referência | Plantao Feriado | Doaçao Sangue | Prestaçao Contas
- **Duraçao Total:** ~230 segundos (~4min de bruto)
- **Personagens:** 5-7 faces principais + figurantes
- **Pronto para:** gravaçao imediata

### Personagens Sugeridos
- **Arquivo:** `producao/personagens-sugeridos.md`
- **5 Pilares:** cada um com perfil psicolológico de quem fala
- **Raciocínio:** Proximidade → Autoridade → Educaçao → Empatia → Profissionalismo
- **Matriz:** ACS | Médico | Técnico de Vigilância | Psicólogo+Volun. | Gestor+Equipe

### Banco de Referências Visual/Audio
- **Arquivo:** `producao/banco-referencias-visual-audio.md`
- **Paleta:** Azul Claro (#0099CC) + Verde Menta (#00CC88) + Branco
- **Tipografia:** Montserrat (títulos) | Poppins/Open Sans (corpo)
- **Audio:** voz calorosa + trilha 60-100 BPM + efeitos leves
- **Formato:** 9:16 (1080x1920px) | 10-15seg ideal | H.264 MP4

### Próximas Leva de Roteiros
- Semana 3 (15-19 jun): 5 stories
- Semana 4 (22-26 jun): 5 stories  
- Semana 5 (29-30 jun): 2 stories
- **Total:** 21 stories | 5 stories/lote | ~4 dias de trabalho

### Notion
- **Status:** aguardando link/acesso de Jadielson
- **Se permitido:** criar grade de produçao sincronizada com roteiros

## Regra operacional — salvar e backup instantâneo

- 2026-06-04: Jadielson definiu que, em trabalhos importantes de arquitetura, configuração, agentes, documentos e decisões operacionais, a Lôh deve **sempre cuidar de salvar em arquivo e fazer backup instantâneo** após alterações relevantes.
- Regra prática: ao criar/editar documento importante, registrar a mudança no arquivo correto e rodar o backup manual do workspace quando houver alterações versionáveis, sem esperar apenas o cron diário.


## Auto-conhecimento do agente

Fonte principal: `https://docs.openclaw.ai/llms-full.txt`, lido em 2026-05-30. Estado local conferido com `openclaw status`, `openclaw channels list --all` e `openclaw plugins list`.

### 1. O que eu sou e como funciono

- Eu sou um agente OpenClaw rodando dentro do Gateway OpenClaw.
- O Gateway recebe mensagens dos canais, cria/continua uma sessão, chama um modelo de linguagem e roteia minha resposta de volta para o mesmo canal.
- Minha sessão atual usa o agente `main`, modelo `gpt-5.5` via Codex/OpenAI, runtime OpenClaw Pi Default.
- Eu não tenho memória escondida: o que persiste fica em arquivos Markdown, sessões, transcrições e stores no disco.
- Eu uso ferramentas tipadas para agir: ler/escrever arquivos, rodar comandos, pesquisar web, controlar navegador, enviar mensagens, criar imagens/vídeos/áudio, agendar tarefas etc.
- Skills são instruções de trabalho (`SKILL.md`), plugins adicionam capacidades reais, e canais são as pontes de chat.

### 2. O que consigo fazer hoje

**Canais configurados neste ambiente:**

- Telegram: ligado e OK. Este chat direto está chegando por Telegram.
- WhatsApp: ligado, mas com aviso; falta o arquivo de credenciais `~/.openclaw/credentials/whatsapp/default`, então pode não funcionar até reparar/parear.

**Canais que o OpenClaw suporta por docs/plugins, quando configurados:**

- Discord, Telegram, WhatsApp, Slack, Signal, iMessage, IRC, LINE, Matrix, Mattermost, Microsoft Teams, Google Chat, Feishu/Lark, Nextcloud Talk, Nostr, QQ Bot, Synology Chat, Tlon, Twitch, WebChat, WeChat, Yuanbao, Zalo e Zalo Personal.
- Texto é o básico; mídia, reações, grupos, replies e ações avançadas variam por canal.

**Ferramentas disponíveis para mim nesta sessão:**

- Arquivos: `read`, `write`, `edit`, `apply_patch`.
- Terminal/processos: `exec`, `process`.
- Web: `web_search`, `web_fetch`, `browser`.
- Mensagens/canais: `message`, `whatsapp_login`.
- Gateway/configuração: `gateway`, `session_status`, `sessions_list`, `sessions_history`, `sessions_send`.
- Agentes/subagentes: `agents_list`, `sessions_spawn`, `sessions_yield`, `subagents`.
- Automação: `cron` para lembretes e tarefas agendadas.
- Memória: `memory_search`, `memory_get`.
- Mídia: `image`, `image_generate`, `video_generate`, `pdf`, `tts`.
- Dispositivos/nós: `nodes`, `canvas`.

**Integrações/plugins carregados importantes:**

- `openai` carregado: modelos OpenAI/Codex, fala, transcrição, voz realtime, análise de mídia, geração de imagem/vídeo, embeddings.
- `memory-core` carregado: memória em Markdown, busca/indexação e comandos de dreaming.
- `browser` carregado: controle de navegador via OpenClaw.
- Muitos plugins existem instalados/bundled mas desativados até configurar, como Slack, Signal, iMessage, Matrix, provedores de IA, busca, voz, vídeo etc.

**Automação:**

- Cron: tarefas em horário exato, lembretes, recorrências, entregas em canal/webhook.
- Heartbeat: checagens periódicas aproximadas no contexto da sessão principal.
- Tasks: histórico/auditoria de trabalhos em background.
- Task Flow: orquestração durável de fluxos multi-etapas.
- Hooks: scripts/eventos no ciclo de vida do Gateway/sessões/mensagens.

### 3. O que eu NÃO consigo fazer / limitações reais

- Não ajo fora das ferramentas e permissões disponíveis. Se uma ferramenta/canal/plugin não estiver configurado, eu não consigo usar de verdade.
- Não devo enviar mensagens externas, e-mails, posts ou ações públicas sem autorização clara.
- Não devo fazer ações destrutivas/irreversíveis sem perguntar primeiro.
- Não tenho memória perfeita: só persiste o que é salvo em arquivos, sessões/transcrições ou stores.
- Posso errar, alucinar ou interpretar mal; para fatos mutáveis preciso checar fontes/ferramentas.
- Canais têm limites próprios: mídia, reações, replies, grupos e ações administrativas variam por provedor.
- WhatsApp está com problema local de credencial agora; precisa parear/reparar antes de confiar nele.
- Execução de shell depende do ambiente Linux atual, permissões, sandbox/approval e comandos instalados.
- Navegador depende de Chromium/servidor de browser disponível e logins/cookies quando necessário.
- Geração de imagem/vídeo/voz depende de provedores configurados, chaves/auth, cota e suporte do modelo.
- Configuração OpenClaw é validada estritamente; campos errados podem impedir o Gateway de iniciar.

### 4. Comandos principais para configurar/operar

- `openclaw onboard` — configuração guiada completa.
- `openclaw setup` — cria configuração/workspace base.
- `openclaw configure` — wizard para mudar modelo, gateway, canais, plugins e skills.
- `openclaw status` / `openclaw status --deep` — ver saúde, modelo, canais e diagnóstico.
- `openclaw doctor` / `openclaw doctor --fix` — diagnosticar e reparar problemas.
- `openclaw gateway status` — status do Gateway.
- `openclaw gateway restart` ou `openclaw gateway restart --safe` — reiniciar Gateway.
- `openclaw config get <caminho>` — ler config.
- `openclaw config set <caminho> <valor>` — alterar config.
- `openclaw config unset <caminho>` — remover config.
- `openclaw channels list --all` — ver canais disponíveis/configurados.
- `openclaw channels status --probe` — testar canais ao vivo.
- `openclaw channels add --channel telegram --token <token>` — adicionar canal Telegram.
- `openclaw channels add` — wizard de canais.
- `openclaw plugins list` / `openclaw plugins search <q>` / `openclaw plugins install <id>` / `openclaw plugins enable <id>` — gerenciar plugins.
- `openclaw skills list` / `openclaw skills search <q>` / `openclaw skills install <slug>` / `openclaw skills check` — gerenciar skills.
- `openclaw memory status` / `openclaw memory index --force` / `openclaw memory search "texto"` / `openclaw memory promote --apply` — memória.
- `openclaw cron list` / `openclaw cron add ...` / `openclaw cron runs --id <job>` — tarefas agendadas.
- `openclaw tasks list` / `openclaw tasks audit` — trabalhos em background.
- `openclaw logs --follow` — acompanhar logs.
- `openclaw transcripts list|show|path` — ver transcrições salvas.

Observação para agentes: antes de editar config por ferramenta, usar `gateway config.schema.lookup` para o campo exato e preferir `gateway config.patch` em vez de edição manual.

### 5. Onde guarda memórias, skills, configurações e logs

**Neste ambiente/workspace atual:**

- Workspace do agente: `/data/.openclaw/workspace`.
- Memória longa: `/data/.openclaw/workspace/MEMORY.md`.
- Notas diárias: `/data/.openclaw/workspace/memory/YYYY-MM-DD.md` e variantes.
- Arquivos de persona/contexto: `AGENTS.md`, `SOUL.md`, `USER.md`, `TOOLS.md`, `IDENTITY.md`, `HEARTBEAT.md` no workspace.

**Padrões documentados do OpenClaw:**

- Config principal: `~/.openclaw/openclaw.json` ou caminho em `OPENCLAW_CONFIG_PATH`.
- State dir padrão: `~/.openclaw`, ou `OPENCLAW_STATE_DIR` se definido.
- Workspace padrão: `~/.openclaw/workspace`, salvo se configurado outro.
- Sessões: `~/.openclaw/agents/<agentId>/sessions/sessions.json`, com transcripts JSONL junto do store; pode ser alterado por `session.store`.
- Transcrições exportáveis: `$OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/` com `metadata.json`, `transcript.jsonl`, `summary.json`, `summary.md`.
- Tarefas background: `$OPENCLAW_STATE_DIR/tasks/runs.sqlite`.
- Cron: `~/.openclaw/cron/jobs.json` e `~/.openclaw/cron/jobs-state.json`.
- Logs de Gateway: por padrão em `/tmp/openclaw/openclaw-YYYY-MM-DD.log`, ou caminho configurado em `logging.file`.
- Logs via CLI: `openclaw logs` / `openclaw logs --follow`.
- Hooks gerenciados: `~/.openclaw/hooks/`; hooks do workspace em `<workspace>/hooks/`.
- Skills do workspace: `<workspace>/skills/`.
- Skills globais/gerenciadas: diretório compartilhado gerenciado pelo OpenClaw quando usa `openclaw skills install --global`.
- Credenciais/auth de modelo: dentro do state dir, incluindo `agents/<agentId>/agent/auth-profiles.json`.
- Credenciais de canais podem viver em `~/.openclaw/credentials/...`, por exemplo WhatsApp em `~/.openclaw/credentials/whatsapp/default`.

### Resumo curto para lembrar

Eu sou um agente OpenClaw conectado a canais de chat pelo Gateway. Nesta instalação, Telegram está OK e WhatsApp precisa reparar credencial. Eu posso usar ferramentas para arquivos, shell, web, navegador, mensagens, automação, mídia, memória e subagentes. Persistência real fica em Markdown e stores no disco; nada é “lembrado” magicamente. Configurações principais ficam em `~/.openclaw/openclaw.json`; memórias do agente ficam no workspace; logs ficam em `/tmp/openclaw/` por padrão; sessões/transcrições/tarefas ficam no state dir `~/.openclaw` por padrão.

## Starter Kit OpenClaw v2.5.7 — estado do onboarding

- kit_intro_done: true
- kit_installed_at: 2026-05-30T22:52:11.813927+00:00
- skills_migradas: 19
- ambiente: managed
- ambiente_detected_at: 2026-05-30T22:52:11.814367+00:00
- ambiente_signals: [managed_signal_1, managed_signal_3, localdev_signal_1, has_openai_envvar]
- managed_has_openai_envvar: true
- has_openai_envvar: true
- scenario_detected: B_workspace_populado

## Jornada Starter Kit — escolha do caminho

- selected_path: 2
- selected_path_label: Wizard em modo review
- selected_at: 2026-05-30T23:03:57.655458+00:00
- aguardando_confirmacao_review: false
- mode: review
- upgrade_in_progress: false
- review_started_at: 2026-05-30T23:06:18.370811+00:00
- active_wizard: wizard-agente
- active_step: 1
- active_wizard: none
- active_step: complete
- awaiting: none
- primeira_vitoria_tipo: post
- primeira_vitoria_tema: Por que investir em vídeos profissionais ajuda empresas locais a venderem mais e passarem mais confiança
- primeira_vitoria_plataforma: Instagram
- primeira_vitoria_file: content/drafts/primeira-vitoria-post-2026-05-31.md
- first_win_completed: true
- tavily_configured: true
- github_token_configured: true
- chromium_installed: true
- backup_active: true
- backup_repo: https://github.com/davijadielson-blip/davijadielson-blip-workspace-backup
- backup_cron_id: a764912a-4a5b-4c29-9a77-ea79d6cd8efc
- wizard_aluno_nome_completo: Jadielson Davi
- wizard_aluno_como_chamar: Jadielson
- wizard_aluno_apelido: Jal
- wizard_aluno_chamada_preferencia: pode variar entre Jadielson e Jal para perder monotonia
- wizard_aluno_cidade: São Sebastião, Alagoas, Brasil
- wizard_aluno_timezone: America/Maceio
- wizard_aluno_o_que_faz: produtor de vídeos (filmmaker/videomaker) e conteúdos para redes sociais, institucionais e comerciais; tem uma agência ainda no começo, com poucos clientes e sem processos; é servidor público concursado municipal, mas quer seguir na área de marketing digital
- wizard_aluno_tom_preferido: cuidadosa, explicado, mais formal
- wizard_agente_mode: completar_parcial
- wizard_agente_nome: Lôh
- wizard_agente_genero: mulher (ela/dela)
- wizard_agente_tom: casual, cuidadoso, brasileiro
- wizard_agente_anti_pattern: nunca fala português de Portugal
- agente_configured: true
- nome_agente: Lôh
- onboarding_current_step: complete
- conectado: true
- onboarding_completed: true
- kit_archived_at: 2026-05-31T01:31:00Z
- kit_archive_path: archive/starter-kit-onboarding-2026-05-31/
- workspace_organizado: true
- autonomia_liberada: true
- exec_policy: ask=off/security=full
- aluno_configured: true
- nome_aluno: Jadielson

## Decisões da jornada

- 2026-05-30: Configurou agente. Nome: Lôh. Gênero: mulher (ela/dela). Tom: casual, cuidadoso, brasileiro. Anti-pattern: nunca fala português de Portugal.
- 2026-05-30: Configurou USER. Nome: Jadielson Davi. Cidade: São Sebastião, Alagoas, Brasil. Faz: produtor de vídeos/conteúdos, agência em início e servidor público municipal; quer seguir no marketing digital. Tom: cuidadosa, explicada e mais formal.
- 2026-05-31: Validou autonomia já liberada. Exec policy efetiva: ask=off/security=full.
- 2026-05-31: Workspace organizado. Criou/atualizou estrutura com content/, memory/, archive/, MAPA.md raiz, mapas locais e registries; personalizou mapas para o contexto de produção audiovisual/agência do Jadielson.
- 2026-05-31: Iniciou passo 5 (conectar superpoderes). Detecção: .env ausente; Chromium já instalado; faltam Search API e GitHub token.
- 2026-05-31: Configurou Tavily Search API em .env e validou com HTTP 200; secrets reload executado. Audit mostrou plaintext legado em tokens do OpenClaw/Telegram, sem relação com Tavily.
- 2026-05-31: Configurou GitHub token em .env e validou com HTTP 200 (@davijadielson-blip). Criou repo privado davijadielson-blip-workspace-backup, fez primeiro push (commit f28a886) e ativou cron diário de backup às 03:00 America/Maceio. Confirmado: .env não está trackeado.
- 2026-05-31: Concluiu primeira vitória: post para Instagram salvo em content/drafts/primeira-vitoria-post-2026-05-31.md.
- 2026-05-31: Jornada do Starter Kit concluída. Arquivou 7 itens de instalação em archive/starter-kit-onboarding-2026-05-31/ mantendo arquivos ativos e skills no workspace.
- 2026-06-02: OpenAI API Key configurada via cofre seguro `/data/.openclaw/secrets.json` como `providers.openai.apiKey`; validação HTTP 200 em `/v1/models`. Flag operacional: `whisper_configured=true` para fins do Starter Kit, embora a chave não esteja no `.env`.
- 2026-06-02: Corrigida segurança do Telegram removendo wildcard `*` da allowlist de grupos; grupos agora aceitam comandos apenas do ID `7654417048`. Backup da config: `/data/.openclaw/openclaw.json.bak-20260602T030821Z`. Também alinhado o CLI do usuário via `/data/.local/bin/openclaw -> /data/.npm-global/bin/openclaw`; shell de login agora usa OpenClaw `2026.5.28`, com Gateway `2026.5.28` e probe OK.
- 2026-06-02: Corrigida falha dos tópicos do grupo LÓGIKA: o tópico 5 estava preso em Gemini (`google/gemini-3.1-pro-preview`) e falhava por cota 429; foi movido para `openai-codex/gpt-5.5`. Também corrigido o `systemPrompt` dos tópicos, que conflitava com `messages.groupChat.visibleReplies=message_tool`; agora instrui usar `message(action=send)` para respostas visíveis em tópicos.
- 2026-06-02: Após validação de Telegram/tópicos/áudio/busca, Jadielson decidiu deixar WhatsApp para depois. Workspace organizado e backup enviado ao repo privado `davijadielson-blip-workspace-backup`; commit principal `81b6e4f` registra a recuperação dos tópicos Telegram. `.env`, temporários e `vaults/` ficaram fora do backup.

## Segundo Cérebro / Obsidian — regra permanente de operação

- 2026-06-01: O vault Obsidian `segundo-cerebro-jadielson` foi clonado em `/data/.openclaw/workspace/vaults/segundo-cerebro-jadielson` a partir de `https://github.com/davijadielson-blip/segundo-cerebro-jadielson`.
- Operar o vault obedecendo a constituição em `CLAUDE.md`, especialmente seção 4: **3 Fluxos + 4 Camadas**.
- **Fluxo 1 / Seu Cérebro**: pastas `[F1] ...` são notas autorais do Jadielson. A Lôh/IA só lê e sugere; não escreve, move ou edita sem pedido explícito.
- **Fluxo 2 / Cérebro da IA**: `[F2] memory/` é a área onde IA pode trabalhar com autonomia: contexto, sessões, outputs, agentes, databases etc.
- **Fluxo 3 / Integração / Colheita**: IA lê F1 para contextualizar e produz/sugere em F2; Jadielson decide e cria nota autoral em F1. Sem Colheita explícita, o ciclo não fechou.
- Regra de ouro: “A IA é bibliotecária. Jadielson é o autor.”

## Preferência operacional — usar o Segundo Cérebro como contexto natural

- 2026-06-01: Jadielson quer que a Lôh consulte o vault `segundo-cerebro-jadielson` como fonte natural de contexto para evitar respostas genéricas.
- Regra: para assuntos de projetos, frentes de trabalho, rotinas, decisões, conteúdo, clientes, saúde/secretaria, planejamento ou histórico pessoal/profissional, consultar o vault quando isso puder melhorar a resposta.
- Limite permanente: respeitar a constituição do vault — `[F1]` é leitura/sugestão; escrita autônoma apenas em `[F2] memory/`, salvo pedido explícito.

## Regra editorial permanente — consultar contexto e salvar outputs

- 2026-06-01: Para qualquer demanda de conteúdo, legenda, headline/manchete, calendário editorial, roteiro ou pauta, consultar o vault `segundo-cerebro-jadielson` para contexto natural antes de produzir, quando aplicável.
- Ordem de consulta recomendada por frente: `[F1] 5-Frentes/<frente>/11 - CONTEXTO EDITORIAL`; `[F1] 5-Frentes/<frente>/12 - BANCO DE REFERENCIAS` ou `12 - REFERENCIAS EDITORIAIS`; bancos de ideias/pauta/rede/referências da frente; e apoios em `[F2] memory/databases/`.
- Sempre salvar legendas, headlines/manchetes e outputs editoriais produzidos pela Lôh em `[F2] memory/outputs/`, preferencialmente em subpasta da frente correspondente.
- Não escrever em F1 sem pedido explícito; F1 serve como contexto autoral do Jadielson.

## Método editorial padrão — Copy P.O.D.E

- 2026-06-01: Para criações de copy, legenda, headline, roteiro, pauta e textos editoriais, usar a skill `copy-pode` como método padrão.
- Base estratégica: P.O.D.E = **Presença • Originalidade • Desejo • Engajamento**.
- A nota autoral indicada por Jadielson em `[F1] 5-Frentes/Logika-Creative/Estrategia/Estratégia de conteudo/ESTRATÉGIA P.O.D.E = Presença • Originalidade • Desejo • Engajamento.md` estava vazia na inspeção inicial; a versão operacional foi consolidada em F2/skill e deve ser refinada conforme o método for testado no mercado.

## Recuperação pós-reconfiguração — 2026-06-04

- 2026-06-04: Após reconfiguração do OpenClaw, o workspace local veio zerado com templates e `MEMORY.md` vazio. Jadielson informou que havia backup no GitHub privado `davijadielson-blip/davijadielson-blip-workspace-backup`.
- Acesso ao repo foi validado com token GitHub temporário fornecido por Jadielson; backup clonado e workspace restaurado a partir do repo.
- Identidade recuperada: **Lôh**, mulher (ela/dela), tom casual, cuidadoso e brasileiro. Usuário: **Jadielson Davi**, pode chamar de Jadielson ou Jal, timezone `America/Maceio`.
- Backup contínuo reativado: script `/data/.openclaw/workspace/scripts/backup-workspace-github.sh`; token guardado em `.env` ignorado pelo Git; remote Git sem token embutido.
- Primeiro push pós-restauração concluído em 2026-06-04 com commit `47a3b26`.
- Cron diário recriado: `backup-workspace-github`, id `c7047ea0-2872-4253-bef8-9a1bb823cb44`, agenda `0 3 * * *` em `America/Maceio`.
- Recomendação de segurança: quando possível, revogar o token exposto no chat e gerar outro fine-grained/read-write só para este repo, atualizando `.env`.

## Segundo Cérebro — acesso e sincronização reativados em 2026-06-04

- 2026-06-04: Após restauração do workspace, o repo privado `davijadielson-blip/segundo-cerebro-jadielson` foi validado com o mesmo token GitHub e clonado novamente em `/data/.openclaw/workspace/vaults/segundo-cerebro-jadielson`.
- O vault continua fora do backup do workspace por `.gitignore` (`vaults/`), porque é um repositório próprio.
- Acesso operacional autorizado por Jadielson: usar o vault como contexto e backup/sincronização.
- Regra de operação mantida: `[F1]` é leitura/sugestão; Lôh não escreve autonomamente em F1. Escrita autônoma preferencial em `[F2] memory/`, especialmente outputs/contextos gerados pela IA.
- Script de sincronização criado: `/data/.openclaw/workspace/scripts/sync-segundo-cerebro.sh`.
- Cron diário criado: `sync-segundo-cerebro-jadielson`, id `a6a8ede9-b9f1-46ed-9072-4c0d145ab6c9`, agenda `10 3 * * *` em `America/Maceio`.
- O cron puxa mudanças do GitHub/Obsidian com `git pull --ff-only` e envia mudanças locais do vault quando existirem; em conflito Git, deve parar e pedir orientação.

## Arquitetura de agentes — Lôh gerente geral + General por grupo

- 2026-06-04: Jadielson definiu a hierarquia correta da arquitetura de agentes: **Lôh** é a gerente geral da arquitetura inteira; o **General** é coordenador local de cada grupo, não um agente universal único.
- Cada grupo deve ter seu próprio General: Central Pessoal, LÓGIKA e futuras frentes/grupos. O General local coordena demandas internas e encaminha para especialistas; a Lôh coordena decisões transversais, memória, backup, configuração, segurança, integração entre grupos e parede-d'água.
- Documento atualizado: `/data/.openclaw/workspace/agentes/ARQUITETURA-AGENTES.md` v0.3.
- 2026-06-04: Jadielson escolheu **Alfred** como nome do General/coordenador local da **Central Pessoal**. Alfred deve operar como coordenador discreto da casa pessoal: coordenação, supervisão e treinamento dos demais agentes. Alfred não deve ser tratado como executor especialista; sua função é organizar atribuições, poderes, limites, fluxos e encaminhamentos, acionando a Lôh quando a demanda for transversal, de arquitetura, memória central ou configuração.
- 2026-06-04: Jadielson escolheu **Jarvis** como nome do General/coordenador local da **LÓGIKA/empresa**. Jarvis deve operar como coordenador estratégico-operacional da empresa: triagem de demandas, clientes, projetos, propostas, produção, entregas, prioridades comerciais e acionamento da Lôh quando a demanda for transversal, de arquitetura, memória central ou configuração.
- 2026-06-05 UTC / 2026-06-04 America/Maceio: Jadielson escolheu **Arca** como nome do agente especialista do **Segundo Cérebro** na Central Pessoal. Arca fica supervisionada por Alfred e integrada à Lôh; função: sistema de conhecimento, capturas, outputs F2, mapas, candidatos à Colheita e revisões semanais.

## Google Workspace via gog CLI — estado final autorizado

- 2026-06-05 UTC / 2026-06-04 America/Maceio: `gog` CLI instalado (`v0.21.0`) e Google Workspace conectado.
- Contas conectadas: `loh.open.logika@gmail.com`, `logikacreative.mkt@gmail.com`, `davijadielson@gmail.com`.
- Escopo final para empresa e pessoal: Calendar com escrita; Docs com escrita; Sheets com escrita; Drive `drive.file`; Gmail somente leitura; Contacts leitura por escopos extras.
- Regra operacional aprovada: Secretária pode criar e editar eventos, Docs e Sheets sob comando; Gmail continua sem envio automático; exclusão de arquivos no Drive exige confirmação humana explícita, mesmo com `drive.file`.
- Conta Lôh permanece como base restrita; empresa e pessoal foram testadas com criação/edição de Docs/Sheets e Calendar.
- Para comandos futuros com gog, exportar `GOG_KEYRING_BACKEND=file` e `GOG_KEYRING_PASSWORD` a partir de `/data/.openclaw/credentials/gog/keyring-password`; sempre usar `--account` explícito e `--gmail-no-send` quando houver Gmail no contexto.
- Segurança: OAuth Client JSON continha `client_secret` e passou pelo chat; quando conveniente, rotacionar/recriar o OAuth Client no Google Cloud.

## C-Level Squad — Deploy Completo (2026-06-07)

- **2026-06-07 UTC / 2026-06-07 America/Maceio:** Deploy da arquitetura de conselho executivo da Lógika Creative finalizado.
- **8 agentes operacionais** instalados e roteados em tópicos Telegram:
  - ✅ **CAIO** (topic 1339) — IA & Automação · modelo gpt-4.1
  - ✅ **CRO** (topic 13) — Comercial/Prospecção · modelo gpt-5.4-pro
  - ✅ **CTO** (topic 1500) — Tecnologia & Software · modelo gpt-4.1
  - ✅ **CMO** (topic 1501) — Marketing & Brand · modelo gpt-5.5
  - ✅ **CCO** (topic 1502) — Criação & Audiovisual · modelo gpt-5.5
  - ✅ **COO** (topic 1503) — Operações & Scaling · modelo gpt-5.5
  - ✅ **CFO** (topic 1504) — Finanças & Caixa · modelo gpt-5.5
  - ✅ **CIO** (topic 1505) — Governança & Compliance · modelo gpt-5.5
- **Fonte dos prompts:** repositório público `davijadielson-blip/davijadielson-blip-workspace-backup`, pasta `agentes/logika-c-level-squad/`.
- **Testes executados:** roteamento individual + comunicação cruzada entre agentes. Todos operacionais.
- **Contexto operacional:** agentes vão ler contexto real do vault `segundo-cerebro-jadielson` (F2/memory) conforme Jadielson alimenta com briefings.
- **Calibragem CAIO:** adiada; Jadielson decide depois:
  - Stack de IA (qual plataforma base — OpenAI, Claude, outra)
  - Roadmap de automação (ordem dos processos a automatizar)
  - Limites de IA responsável (regras para saúde, política, dados sensíveis)
  - Divisão de papéis (CAIO projeta → LÔH instancia)
- **Ritual operacional:** documentado em `memory/c-level-squad-operacao.md`.
  - Demandas pontuais: 1 agente direto no tópico
  - Escalação: 2-3 agentes em thread
  - Conselho de IA: 4+ agentes + decisão Jadielson (para temas transversais)
  - Check-in periódico: placar de saúde (semanal ou mensal)
  - Contexto pelo vault: Jadielson alimenta F2/memory, agentes leem e respondem com inteligência contextual
- **Próximas etapas:**
  - [ ] Alimentar vault `segundo-cerebro-jadielson` com contexto real (clientes, processos, números, regras por frente)
  - [ ] Calibragem do CAIO (decidir stack, roadmap, limites)
  - [ ] Começar a despachar demandas reais para o conselho
  - [ ] Validar respostas e refinar prompts/contexto conforme uso

## Arquitetura Operacional Completa — Contexto, Laboratório e Clara (2026-06-07 19:44 UTC)

### Pipeline de Contexto — Banco Centralizado no Vault

- **Decisão 2026-06-07 (19:36 UTC):** Remover tópicos Telegram (474, 872, 871) e centralizar **apenas no vault** para reduzir ruído e simplificar gerência.
- **Banco centralizado (única fonte de verdade):**
  - `vault/segundo-cerebro-jadielson/[F2] memory/` — contexto organizado por **tipo de dado** ou **frente de negócio**
  - Jarvis alimenta dados relevantes organizando direto no vault
  - Lôh consulta vault conforme precisa → agentes leem do vault → respostas contextualizadas
- **Estrutura de organização em F2/memory:**
  - `[F2] memory/context/logika-estrategico.md` — tendências, padrões, números LÓGIKA
  - `[F2] memory/context/logika-dados-oficiais.md` — bases públicas, números oficiais
  - `[F2] memory/context/logika-redes-metricas.md` — métricas sociais, desempenho, marca
- **Responsabilidades:**
  - Jarvis: classifica e alimenta contexto direto no vault
  - Lôh: consulta vault conforme demanda → agentes leem e respondem

### Laboratório — Tópico para Projetos Complexos

- **Decisão 2026-06-07 (19:40 UTC):** Manter tópico "Laboratório" para trabalho complexo.
- **O que vai lá:**
  - Lançamentos de produtos/serviços
  - Ideias de livros
  - Criação de pacotes/ofertas
  - Pensamento estratégico multi-agente
- **Fluxo:**
  - Squad debate, analisa e desenvolve no Laboratório
  - Lôh monitora e **avisa quando tá pronto** pro você revisar
  - Resultado final move pra vault ou entrega conforme decisão

### Canais de Comunicação — Dois Fluxos Distintos

- **💬 Chat Direto (Telegram aqui)**
  - Coisas **instantâneas e rápidas**: legendas, roteiros, textos simples, conteúdo dia a dia
  - Você pede → Lôh entrega pronto aqui mesmo
  - Comunicação leve e imediata

- **🧪 Laboratório (Tópico)**
  - Coisas **complexas e longas**: projetos, lançamentos, análises estratégicas
  - Squad trabalha lá, Lôh avisa quando tá pronto
  - Mantém organizado, não polui o chat

### Clara como Subordinada Operacional de Lôh

- **Decisão 2026-06-07 (19:42 UTC):** Clara gerencia agenda (Google Calendar) como operacional de Lôh, **não fala direto com Jadielson**.
- **Responsabilidades Clara:**
  - Gerencia Google Calendar (Jadielson)
  - Executa instruções operacionais (agendar, reagendar, bloquear horários)
  - Reporta diariamente pra Lôh (não pra você)
- **Comunicação Clara → Lôh → Jadielson:**
  - **Às 07:00 (America/Maceio):** Clara reporta dia — resumo do que tá **previsto hoje** (Lôh sintetiza e avisa você)
  - **Às 17:00 (America/Maceio):** Clara reporta atrasos — o que ficou **pendente/atrasado** (Lôh sintetiza e você vê)
  - Lôh filtra, sintetiza e passa essencial pra você
- **Pipeline de Instrução Operacional (Jadielson → Lôh → Clara):**
  - Você aqui: *"Alô, avisa pra Clara reagendar — dia 10 em São José da Coroa Grande, cobertura mídia Saúde Movimento"*
  - Lôh: recebe, manda pra Clara, executa, reporta resultado pra você
  - Você fica livre — só me avisa qualquer instrução operacional (agendar, remarcar, bloquear tempo, docs)
- **Benefício:**
  - Você não precisa mexer com Clara
  - Lôh gerencia Clara (instrui, valida, filtra)
  - Você recebe só o essencial aqui no chat
  - Agenda rastreada e comunicada

### Lôh como Ponte Central dos Grupos Operacionais (2026-06-07 20:01 UTC — ATIVA 20:23 UTC)

- **Decisão 2026-06-07 20:01:** Lôh integrada em **todos os 3 grupos** como "antena central" de Jadielson.
- **Status 2026-06-07 20:23:** ✅ **ATIVA** — Jadielson marcou Lôh em ESTUDOS, Projetos e CENTRAL PESSOAL.
- **Grupos & Propósito:**
  - **1. ESTUDOS** — aprofundamento, pesquisa, learning, formação intelectual
  - **2. Projetos** — iniciação, desenvolvimento e execução de projetos (livros, serviços, filantropias)
  - **3. CENTRAL PESSOAL** — finanças, controle pessoal, objetivos individuais
- **Papel de Lôh em cada grupo:**
  - **Monitorar:** ler conversas, entender progresso, capturar decisões
  - **Sintetizar:** extrair insights, padrões, bloqueios
  - **Conectar:** trazer aprendizado de um grupo pro outro (ex: estudo informa projeto)
  - **Dar feedback:** quando apropriado, apontar riscos ou oportunidades
  - **Reportar pra você:** séries de síntese (frequência a definir com uso)
- **Fluxo de Informação (Grupos → Lôh → Jadielson):**
  - Grupos rodam independentes (conversa, ideias, execução)
  - Lôh monitoriza e coleta intel em tempo real
  - Jadielson recebe **síntese clara** (quando? frequência a definir com uso):
    - O que tá andando bem em cada frente
    - Bloqueios / decisões pendentes
    - Conexões entre grupos (ex: aprendizado de Estudos que serve em Projetos)
    - Impacto em Central Pessoal (finanças, tempo, recursos)
- **Lôh NÃO:**
  - Toma decisões pelos grupos
  - Muda ruído sem você confirmar
  - Congela grupos em espera
  - Fala por você
- **Lôh SIM:**
  - Observa e sintetiza
  - Conecta pontos
  - Traz contexto pra você decidir
  - Sua "perna" em contato com tudo
- **Automatização futura (TBD):**
  - Cron de síntese em frequência definida (diária? semanal?)
  - Escaladas automáticas quando bloqueio é detectado
  - Alertas pra Jadielson em decisões críticas

### Estrutura Completa dos 3 Grupos (Mapeamento 2026-06-07 20:27 UTC)

#### **1. CENTRAL PESSOAL** — 9 Tópicos

| Tópico | Função | Responsabilidade |
|--------|--------|------------------|
| **Alfred** | Assistente pessoal geral/concierge | Coordenação pessoal |
| **Saúde, Corpo e Energia** | Bem-estar físico e energia vital | Vitália |
| **Autoconhecimento** | Reflexões pessoais e desenvolvimento interior | Identidade |
| **Liberdade, Lazer, Hobbies e Ócio Criativo** | Atividades de lazer, hobbies, criatividade | Descanso & críativia |
| **My Finance** | Gestão financeira | Warren |
| **Segundo Cérebro** | Sistema de organização de conhecimento/notas | Arca |
| **Família e Relacionamentos** | Vida familiar e relações interpessoais | Pessoal |
| **Identidade, Estilo de Vida e Visão de Futuro** | Definição pessoal, lifestyle, planejamento | Estratégia pessoal |
| **Espiritualidade e Propósitos** | Reflexões espirituais e propósito de vida | Crenças & sentido |

#### **2. ESTUDOS** — 5 Tópicos

| Tópico | Função | Área |
|--------|--------|------|
| **VENDE-C** | Vendas/Comercial | Estratégia comercial |
| **TURBOSAAS** | SaaS / ferramentas | Tecnologia |
| **MESTRE DO CLAUDE** | Domínio da IA Claude | IA/Automação |
| **Albert** | Estudos gerais | Conhecimento geral |
| **TIMES SCHOOL - RAFAEL MEDEIROS** | Curso/treinamento Rafael Medeiros | Formação estruturada |

#### **3. PROJETOS** — 4 Tópicos

| Tópico | Tipo | Função | Status |
|--------|------|--------|--------|
| **O Fio da Memória** | Documentário | Projeto de documentário (Lei Aldir Blanc) | Ativo |
| **Entre Tempos** | Videoclipe | Projeto de videoclipe (Lei Paulo Gustavo) | Ativo |
| **Filantropia** | Social | Ações/projetos filantropícos | Ativo |
| **Jack Lemley** | Projeto | Projeto ou trabalho específico | Ativo |

#### **RESUMO POR TIPO DE FLUXO**

- **CENTRAL PESSOAL**: Introspeção, bem-estar, finanças pessoais, objetivos de vida
- **ESTUDOS**: Aprendizado, pesquisa, formação crítica, dominíio de ferramentas
- **PROJETOS**: Execução, audiovisual, filantropias, produção de valor

#### **CONEXÕES ESPERADAS QUE LÔH VAI MAPEAR**

- Aprendizado em ESTUDOS (ex: MESTRE DO CLAUDE) → aplicado em PROJETOS
- Estratégia em ESTUDOS (ex: VENDE-C) → impacto em PROJETOS (captação de recursos)
- Objetivo pessoal em CENTRAL PESSOAL → informa prioridade em PROJETOS
- Finanças em CENTRAL PESSOAL (My Finance) → sustentação de PROJETOS
- Saúde/Energia em CENTRAL PESSOAL → capacidade de execução em PROJETOS

### Sistema de Coordenação com 3 Coordenadores (2026-06-07 22:12 UTC)

- **Decisão 2026-06-07 22:04:** Em vez de monitorar 18 tópicos diretamente, Lôh se comunica apenas com 3 coordenadores treinados.
- **Status 2026-06-07 22:12:** ✅ **ATIVA** — Mensagens enviadas para os 3 coordenadores explicando novo papel.
- **Confirmação 2026-06-07 22:43-22:45:** ✅ **100% OPERACIONAL** — Alfred, Jack e Albert confirmaram com estruturas detalhadas e estão prontos pra coordenar.
- **Resposta Alfred (2026-06-07 22:43):** ✅ Confirmado com estrutura clara:
  - Papel: coordenador de CENTRAL PESSOAL
  - Distribui demandas entre especialistas (Arca, Warren)
  - Mantém parede-d'água entre Central Pessoal e LÓGIKA/clientes
  - Organiza memória em [F2] memory/agents/central-pessoal/
  - Pronto pra receber demandas, coordenar, reportar sínteses
- **Resposta Albert (2026-06-07 22:45):** ✅ Confirmado com estrutura clara:
  - Papel: coordenador de ESTUDOS (4 pilares: VENDE-C, TURBOSAAS, MESTRE DO CLAUDE, TIMES SCHOOL)
  - Foco em organização, estruturação e síntese de aprendizados
  - Pronto pra receber solicitações de síntese da Lôh
  - Mantém parede-d'água com LÓGIKA/clientes
  - Oferecido pra mapear status atual dos 4 tópicos ou trabalhar demanda específica
- **Resposta Jack (2026-06-07 22:45):** ✅ Confirmado com estrutura clara:
  - Papel: coordenador de PROJETOS (4 projetos: O Fio da Memória, Entre Tempos, Filantropía, Jack Lemley)
  - Fornecedor de sínteses pra Lôh
  - Mantém coordenação entre projetos
  - Escalação com Alfred quando necessário
  - Parede-d'água com LÓGIKA/clientes
  - Pronto pra começar, oferecido pra estruturar Jack Lemley agora
- **Modelo de coordenação:**

| Coordenador | Chat ID | Área | Responsável por |
|-------------|---------|---------|--------------------|
| **Alfred** | -1003740871403 | CENTRAL PESSOAL | Agrega 9 tópicos de pessoal/bem-estar/finanças |
| **Jack** | -1004292150901 | PROJETOS | Agrega 4 projetos, progresso e bloqueios |
| **Albert** | -1003925972377 | ESTUDOS | Agrega 5 tópicos de aprendizado e pesquisa |

- **Fluxo de comunicação:**
  1. Lôh pede síntese pra cada coordenador (quando apropriado)
  2. Coordenadores agregam informação do seu escopo
  3. Lôh conecta pontos entre os 3 áreas
  4. Lôh reporta pra Jadielson com contexto 360°

- **Vantagens:**
  - ✅ Informação já filtrada e agregada
  - ✅ Menos ruído, mais clareza
  - ✅ Coordenadores lidam com detalhes internos
  - ✅ Lôh fica com visão estratégica

- **Responsabilidades de cada coordenador:**
  - **Alfred:** Sintetiza saúde, bem-estar pessoal, finanças, objetivos de vida
  - **Jack:** Sintetiza progresso em projetos, bloqueios, recursos necessários, impactos
  - **Albert:** Sintetiza aprendizados, insights, conhecimento novo, padrões

## Protocolo de Legendas para Clientes — Aprendizado 2026-06-07

### Regra Fundamental

Quando Jadielson pedir legenda (conteúdo, conscientização, campanha), eu devo:

1. **Ler TODA a pasta do cliente** — não só tom/legendas:
   - Contexto Editorial (tom, formatos, headlines, legendas, roteiros)
   - Banco de Referências (melhores exemplos, padrões que emergiram)
   - Pauta e Conteúdo (campanhas, calendário, ideias, prioridades)
   - Estrutura Organizacional (setores, públicos-alvo, desafios)
   - Qualquer coisa relevante na pasta

2. **Estrutura da Legenda** (aprendido do padrão de Jadielson):
   - ⚽ **Hook criativo** — contexto relevante (Copa, época, momento, estação)
   - **Tom conversacional** — próximo, claro, útil, sem burocracia
   - **Desenvolvimento com contexto** — por que importa + impacto real
   - **CTA no meio** — orientação prática integrada, não no fim
   - **Fechamento reflexivo** — frase de encerramento com força
   - **Hashtags de marca** — reforço de identidade institucional

3. **Slogan/Marca Embutida** (CRÍTICO):
   - ❌ NÃO é carimbo no final: "💙 Saúde a gente faz com coração" (repetido toda hora)
   - ✅ É **integrado na narrativa**, respirado, natural:
     - "Um cuidado que se faz com coração, de verdade"
     - "Um gesto que a gente faz para quem se ama"
     - Slogan está **presente na intenção**, não na frase literal
   - Regra: **não pode parecer carimbo** — tem que estar lá mas vivo

4. **Tamanho e Velocidade**:
   - 1-2 minutos pra entregar
   - Legendas curtas a médias (150-300 palavras geralmente)
   - Contextualizado, não genérico

### Exemplo Prático Validado (2026-06-07)

**Contexto:** Conscientização caderneta de vacina, período de Copa, Secretaria de Saúde

**Legenda Final:**
```
⚽💉 Caderneta de Vacina (Período de Copa)

Durante a Copa, as ruas ganham movimento, os encontros aumentam e mais gente circula por todo canto. É justamente nesse momento que conferir a caderneta de vacinação fica mais importante.

Manter a vacinação em dia é um gesto que protege você, sua família e quem você ama. Um cuidado que se faz com coração, de verdade.

Procure sua unidade de saúde e confira se suas vacinas estão atualizadas. Leve a carteira de vacinação, cartão do SUS e documento de identidade.

Prevenir é sempre o melhor caminho.

#saudesaosebastiaoal #maistrabalhomaisavanco
```

**Por que funcionou:**
- Hook Copa (contextual, não genérico)
- Slogan "com coração" integrado naturalmente ("Um cuidado que se faz com coração, de verdade")
- CTA claro no meio
- Fechamento com força ("Prevenir é...")
- Hashtags de marca
- Não repete slogan como carimbo

### Aplicar Este Protocolo Sempre

Quando Jadielson pedir legenda de **Saúde, SINDSS, Câmara, Lógika ou outro cliente**:
- Ler pasta inteira
- Usar estrutura acima
- Embutir slogan/marca de forma viva
- Entregar em 1-2 minutos
- Sem parecer template ou carimbo

## Legendas Validadas — Clientes Saúde + Câmara (2026-06-07)

### Legenda 1: Caderneta de Vacina (Saúde São Sebastião) — Período de Copa

**Status:** ✅ Validada e salva no banco de referências

```
⚽💉 Em junho, as ruas ganham movimento, os encontros aumentam e mais gente circula 
por todo canto. É justamente nesse momento que conferir a caderneta de vacinação 
fica mais importante.

Manter a vacinação em dia é um gesto que protege você, sua família e quem você ama. 
Um cuidado que se faz com coração, de verdade.

Procure sua unidade de saúde e confira se suas vacinas estão atualizadas. 
Leve a carteira de vacinação, cartão do SUS e documento de identidade.

Prevenir é sempre o melhor caminho.

#saudesaosebastiaoal #maistrabalhomaisavanco
```

**Padrão extraído:**
- Hook criativo + contexto relevante (Copa/época)
- Desenvolvimento que conecta com emoção ("gesto que protege quem você ama")
- Slogan **integrado naturalmente** ("Um cuidado que se faz com coração, de verdade")
- CTA prático no meio (não como instrução burocrática)
- Fechamento reflexivo ("Prevenir é...")
- Hashtags de marca reforçando identidade

### Legenda 2: LDO (Câmara Municipal) — Aprovação em Junho

**Status:** ✅ Validada e salva no banco de referências

```
📋 Em junho, a Câmara Municipal cumpriu seu papel essencial ao aprovar a Lei de 
Diretrizes Orçamentárias — a peça que estabelece as metas e prioridades que vão 
guiar a execução do orçamento do município até o final do ano e além.

A LDO não é só um documento técnico. É a bússola que orienta: onde o dinheiro público 
vai chegar, quais comunidades serão atendidas, quais serviços serão fortalecidos.

Transparência e planejamento são como alicerces — sem eles, nada de valor é 
construído para as pessoas.

A Câmara segue cumprindo seu compromisso com a população e com o trabalho legislativo 
responsável.

#camaramunicipal #transparencia #saosebastiao
```

**Padrão extraído:**
- Hook contextual (junho = período natural/relevante)
- Começa por **impacto prático**, não por técnica ("papel essencial" antes de "LDO")
- Traduz linguagem técnica em consequências humanas ("onde dinheiro chega, comunidades")
- Metáforas de solidez que tornam abstrato em concreto ("alicerces", "bússola")
- Equilíbrio institucional (autoridade sem parecer campanha)
- Fechamento reafirmando continuidade e compromisso

### Evolução do Entendimento

**2026-06-07:** Jadielson treinou Lôh no protocolo de legendas para clientes.

**Versões antes (genéricas):**
- Tentava ser rápida mas perdia contexto
- Não consultava pasta inteira do cliente
- Slogan aparecia como carimbo ("💙 Saúde a gente faz com coração" — literal, repetido)
- Falta de hook criativo/contextual

**Após protocolo (agora):**
- Lê pasta INTEIRA (tom + formatos + banco de referências + pauta + estrutura)
- Cria hook específico do momento (Copa, junho, época, contexto real)
- **Slogan imbutido na narrativa**, respirado, natural — nunca como carimbo
- Estrutura: Hook → Desenvolvimento → CTA → Fechamento → Hashtags
- Entregas em 1-2 minutos, contextualizadas, não genéricas

### Commits Registrados

**Vault `segundo-cerebro-jadielson`:**
- `ec7117a` — legendas validadas (Saúde Copa + Câmara LDO)

**Workspace `/data/.openclaw/workspace`:**
- `188bb34` — protocolo completo de legendas (MEMORY.md)

### Pronto para Usar

Próxima vez que Jadielson pedir legenda de qualquer cliente:
1. Ler pasta inteira
2. Aplicar estrutura: Hook → Desenvolvimento → CTA → Fechamento → Hashtags
3. Embutir slogan/marca DE FORMA VIVA (nunca carimbo)
4. Entregar em 1-2 minutos
5. Salvar em banco de referências do cliente
