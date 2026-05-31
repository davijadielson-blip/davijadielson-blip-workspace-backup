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
