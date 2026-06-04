# MEMORY.md

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
- upgrade_in_progress: true
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
