---
tema: governanca diaria do Cofre e sessoes - 2026-08-25
conteudo: auditoria conservadora de armazenamento, Git, sessoes, agentes, SQLite, logs, caches, anexos temporarios, segredos e backup
setor: governanca agentiva
cliente: Jadielson Davi
tipo: relatorio/limpeza-openclaw
prioridade: alta
atualizado_em: 2026-08-25
usar_quando: verificar resultado da rotina diaria de governanca do Cofre e decisoes de backup/quarentena
nao_usar_quando: substituir decisao humana sobre exclusao definitiva, quarentena ou publicacao externa
---

# Governanca diaria do Cofre e sessoes - 2026-08-25 03:00 UTC

## Escopo executado

- Rotina: `governanca-cofre-sessoes-diaria-0000`
- Modo: seguro/conservador
- Data/hora de referencia: 2026-08-25 03:00 UTC
- Regra maxima aplicada: em caso de duvida, preservar e registrar revisao necessaria.

## Arquivos canonicos carregados

- `CONSTITUICAO.md`
- `AGENTS.md`
- `MAPA.md`
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `MEMORY.md`
- `memory/2026-08-25.md`: ausente
- `memory/2026-08-24.md`: ausente

Observacao: as notas diarias ausentes nao foram criadas automaticamente, conforme regra vigente.

## Auditoria de armazenamento

- Tamanho de `/data/.openclaw`: 2.7G.
- Tamanho do Cofre local: 146M.
- Espaco do volume `/data`: 10G total, 7.2G usado, 2.9G livre, 72% de uso.
- Maiores areas do Cofre no recorte consultado:
  - `70-agentes`: 32M.
  - `90-arquivo`: 27M.
  - `40-projetos`: 5.4M.
  - `media`: 4.4M.
  - `50-clientes`: 4.0M.
  - `memory`: 2.3M.
- Nenhuma limpeza executada.
- Removidos: 0.
- Espaco recuperado: 0.

## Git e backup remoto

- Branch local: `main`.
- Remoto: `git@github.com:davijadielson-blip/davijadielson-blip-workspace-backup.git`.
- `HEAD` local: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- `origin/main` apos `git fetch --prune origin`: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- `git ls-remote origin refs/heads/main`: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- Entradas no `git status --porcelain` antes deste relatorio: 106.
  - Modificados: 43.
  - Removidos: 23.
  - Nao rastreados: 50.
- Commit/push: bloqueado por seguranca.

Motivo do bloqueio: o worktree continua amplo e ambiguo, com alteracoes anteriores em governanca, memoria, scripts, skills, entregas de cliente, financeiro, migracao de inbox, remocoes em `memory/inbox-externa/`, retorno de `BOOTSTRAP.md`, estado local em `scripts/data/` e midia de runtime. A varredura de segredos tambem apontou referencias sensiveis em Markdown legado e scripts. Nao ha base segura para commit seletivo sem revisao humana/tecnica.

## Worktree observado

- Governanca e mapa alterados: `AGENTS.md`, `MAPA.md`, `MEMORY.md`, `TOOLS.md`, `00-central/decisoes.md`, `00-central/mapa-do-cofre.md` e `00-central/notas-permanentes/_MAP.md`.
- Skills/scripts alterados: `.agents/skills/source-command-*`, `scripts/notion-env.sh`, `scripts/sync/notion-cofre-sync.py` e `scripts/sync/notion-to-calendar.py`.
- Financeiro alterado: arquivos da LÓGIKA e registros em `00-central/inbox/externa/financeiro/`.
- Entregas recentes de Saude e Camara aparecem como nao rastreadas ou modificadas em pastas de aprovados/producao.
- Remocoes que exigem conferencia: `10-pessoal/inbox/_README.md`, `memory/.dreams/short-term-recall.json` e arquivos antigos em `memory/inbox-externa/`.
- Novos caminhos relevantes: `00-central/inbox/`, `10-pessoal/diario/`, `10-pessoal/30-saude/documentos/`, `40-projetos/agente-solucionador-estrategico/`, `90-arquivo/30-regras-obsoletas/2026-08-10-inbox-legado/`, `BOOTSTRAP.md`, `scripts/data/` e `70-agentes/runtime/logika/media/`.

## Agentes, sessoes e trajetorias

- Sessoes visiveis via OpenClaw: 20 primeiras listadas, incluindo cron atual, DM principal, crons de agenda, Alfred, My Finance, Jarvis/Logika, Estudos e CFO.
- Subagentes ativos/recentes deste job: 0.
- Status da sessao atual: gateway ativo, modelo OpenAI, contexto saudavel, sem fila.
- Arquivos locais de sessao `.jsonl` em `/data/.openclaw/agents/*/sessions/`: 546.
- Trajetorias `.trajectory.jsonl`: 320.
- Arquivos de sessao/trajetoria recentes nas ultimas 24h: 26.
- Validacao conservadora: nao identifiquei decisao permanente nova com confianca suficiente para alterar `MEMORY.md` ou `00-central/decisoes.md` nesta rotina. Materiais recentes importantes parecem ja estar como arquivos Markdown no Cofre ou permanecem como pendencias de revisao no worktree.

## SQLite, logs e caches

- Bancos SQLite e similares em `/data/.openclaw`: 100.
- Banco principal recente observado: `/data/.openclaw/agents/main/agent/openclaw-agent.sqlite`, 57M, atualizado em 2026-08-25.
- Logs recentes: `/tmp/openclaw/openclaw-2026-08-25.log` e `/tmp/openclaw/openclaw-2026-08-24.log`.
- Logs totais no recorte `/data/.openclaw` + `/tmp/openclaw`: 15.
- Cache/temp observado:
  - `/data/.openclaw/agents/*/agent/codex-home/cache`, cerca de 1.3M a 1.7M por agente.
  - `/data/.openclaw/agents/*/agent/codex-home/.tmp`, cerca de 78M em alguns agentes.
  - `/data/.openclaw/tmp`.
  - `scripts/sync/__pycache__`.
- Nenhuma limpeza executada.

## Anexos temporarios e midia

- Midia externa recente preservada em `/data/.openclaw/media/inbound/`, incluindo imagens, audios, PDFs e DOCX recebidos entre 2026-08-10 e 2026-08-24.
- Midia do runtime preservada em `70-agentes/runtime/*/media/`.
- Ha duplicidades aparentes de audio/imagem e arquivos de pauta/roteiro, mas nao houve confirmacao suficiente de consolidacao completa em `.md` e/ou Drive.
- Removidos: 0.
- Espaco recuperado: 0.

## Auditoria de segredos

- `scripts/.secrets/` esta ignorado pelo Git, incluindo credenciais locais de Google/Notion/keyring.
- `.gog/` segue ignorado pelo Git.
- `scripts/data/keyring/.lock` aparece como nao rastreado e deve ser classificado antes de qualquer commit.
- Varredura por padroes sensiveis encontrou referencias a `token`, `secret`, `password`, `authorization`, `client_secret` e `GOG_KEYRING_PASSWORD` em scripts, memoria e relatorios.
- Ponto critico: ha senhas Hotmart em Markdown pessoal/estudos/profissional legado. Valores nao foram reproduzidos neste relatorio. Recomenda-se migrar esses dados para armazenamento seguro e manter no Cofre apenas referencia sem segredo.
- Backup remoto bloqueado ate saneamento/revisao desses pontos.

## Consolidacao

- Conhecimento novo consolidado nesta rotina:
  - este relatorio de governanca.
- Decisoes permanentes novas: nenhuma.
- Processos permanentes novos: nenhum.
- Preferencias permanentes novas: nenhuma.
- Pendencias permanentes novas: registradas abaixo como pendencias de governanca.
- Nada foi excluido definitivamente.
- Nada foi movido para quarentena.

## Candidatos a limpeza/quarentena

Nao houve quarentena autorizada. Candidatos abaixo sao apenas para revisao:

- `scripts/data/`: confirmar se e apenas estado local de keyring/cache e se deve ser ignorado pelo Git.
- `BOOTSTRAP.md`: revisar reaparecimento, pois a regra vigente diz que o bootstrap esta obsoleto/removido.
- Remocoes de `memory/inbox-externa/`: confirmar se a migracao para `00-central/inbox/externa/` e `90-arquivo/30-regras-obsoletas/2026-08-10-inbox-legado/` esta completa.
- `70-agentes/runtime/*/media/inbound/` e `/data/.openclaw/media/inbound/`: validar se anexos ja foram resumidos em `.md` e enviados/registrados no Drive quando aplicavel.
- `memory/.dreams/short-term-recall.json.u4s-superseded-*` e arquivos `.migrated`: possiveis artefatos de migracao; preservar ate confirmacao.
- Entradas Markdown com senhas Hotmart: revisar/migrar para local seguro, sem exclusao automatica.
- Caches `.tmp` dos agentes: so considerar limpeza depois de confirmada ausencia de execucoes pendentes e backup seguro.

## Erros e pendencias

- `memory/2026-08-25.md` e `memory/2026-08-24.md` ausentes; preservado conforme regra de nao criar automaticamente.
- Commit/push bloqueado por worktree ambiguo e possivel superficie de segredo/estado local.
- Revisar 106 entradas do `git status` e separar:
  - mudancas canonicas seguras para commit;
  - remocoes que representam migracao confirmada;
  - arquivos que devem entrar em `.gitignore`;
  - anexos que devem permanecer fora do Git e ser referenciados por Markdown;
  - senhas ou credenciais que devem sair de Markdown antes de backup amplo.
- Verificar se todo conhecimento relevante das sessoes recentes ja esta consolidado nos arquivos novos nao rastreados antes de arquivar ou limpar sessoes antigas.

## Resultado final

- Sessoes analisadas: 20 sessoes visiveis listadas + 26 arquivos recentes principais + 546 arquivos locais de sessao contados + 320 trajetorias contadas.
- Consolidadas: 1 relatorio.
- Removidas: 0.
- Espaco recuperado: 0.
- Backup/hash: backup interrompido; remoto confirmado em `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- Estado: preservar tudo e aguardar revisao humana/tecnica do worktree antes de commit/push.
