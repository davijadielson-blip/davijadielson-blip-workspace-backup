---
tema: governanca diaria do Cofre e sessoes - 2026-08-18
conteudo: auditoria conservadora de armazenamento, Git, sessoes, agentes, SQLite, logs, caches, anexos temporarios, segredos e backup
setor: governanca agentiva
cliente: Jadielson Davi
tipo: relatorio/limpeza-openclaw
prioridade: alta
atualizado_em: 2026-08-18
usar_quando: verificar resultado da rotina diaria de governanca do Cofre e decisoes de backup/quarentena
nao_usar_quando: substituir decisao humana sobre exclusao definitiva, quarentena ou publicacao externa
---

# Governanca diaria do Cofre e sessoes - 2026-08-18 03:00 UTC

## Escopo executado

- Rotina: `governanca-cofre-sessoes-diaria-0000`
- Modo: seguro/conservador
- Data/hora de referencia: 2026-08-18 03:00 UTC
- Regra maxima aplicada: em caso de duvida, preservar e registrar revisao necessaria.

## Arquivos canonicos carregados

- `CONSTITUICAO.md`
- `AGENTS.md`
- `MAPA.md`
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `MEMORY.md`
- `memory/2026-08-18.md`: ausente
- `memory/2026-08-17.md`: ausente

Observacao: as notas diarias ausentes nao foram criadas automaticamente, conforme regra vigente.

## Auditoria de armazenamento

- Tamanho do Cofre: 134M.
- Espaco do volume: 10G total, 7.1G usado, 3.0G livre, 71% de uso.
- Maiores pastas dentro do Cofre:
  - `.git/`: 67M
  - `90-arquivo/`: 27M
  - `70-agentes/`: 21M
  - `40-projetos/`: 5.4M
  - `50-clientes/`: 3.9M
  - `media/`: 3.9M
  - `memory/`: 2.3M
- Arquivo grande observado: pack Git local `./.git/objects/pack/pack-b332d85141b20ee7a641e8a563f27eb9b3ce42ae.pack` com cerca de 64M.
- Nenhuma limpeza executada.

## Git e backup remoto

- Branch local: `main`.
- Remoto: `git@github.com:davijadielson-blip/davijadielson-blip-workspace-backup.git`.
- `HEAD` local: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- `origin/main` local: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- Hash remoto confirmado via `git ls-remote`: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- Status observado antes deste relatorio: worktree amplo e ambiguo.
- Entradas no `git status --porcelain`: 94.
  - Modificados: 33.
  - Removidos: 19.
  - Nao rastreados: 42.
- Diff rastreado: 52 arquivos, com 266 insercoes e 16926 remocoes.
- Commit/push: bloqueado por seguranca.

Motivo do bloqueio: ha muitas alteracoes anteriores a esta rotina, incluindo governanca, skills, scripts, entregas de cliente, arquivos de memoria, migracao de inbox, remocoes em `memory/inbox-externa/`, retorno de `BOOTSTRAP.md`, `.gog/` e `scripts/data/` nao rastreados. O estado nao esta claro para commit seletivo sem misturar autoria, perder rastreabilidade ou arriscar backup de estado local/sensivel.

## Worktree observado

- Governanca e mapa alterados:
  - `AGENTS.md`
  - `MAPA.md`
  - `MEMORY.md`
  - `TOOLS.md`
  - `00-central/decisoes.md`
  - `00-central/mapa-do-cofre.md`
  - `00-central/notas-permanentes/_MAP.md`
- Skills/scripts alterados:
  - `.agents/skills/source-command-drive-recente/SKILL.md`
  - `.agents/skills/source-command-inbox/SKILL.md`
  - `.agents/skills/source-command-prioridades/SKILL.md`
  - `.agents/skills/source-command-sync-notion-calendar/SKILL.md`
  - `scripts/notion-env.sh`
  - `scripts/sync/notion-cofre-sync.py`
  - `scripts/sync/notion-to-calendar.py`
- Remocoes que exigem conferencia:
  - `10-pessoal/inbox/_README.md`
  - `memory/.dreams/short-term-recall.json`
  - arquivos antigos de `memory/inbox-externa/drive/`
  - arquivos antigos de `memory/inbox-externa/financeiro/`
- Novos caminhos relevantes:
  - `.gog/`
  - `scripts/data/`
  - `00-central/inbox/`
  - `10-pessoal/diario/`
  - `30-estudos/`
  - `40-projetos/agente-solucionador-estrategico/`
  - entregas aprovadas e outputs da Saude
  - `50-clientes/20-camara-municipal/00-indice/2026-08-14-mapa-real-skill-comunicacao-camara.md`
  - relatorios de governanca pendentes de commit de 2026-08-11 a 2026-08-17
  - `BOOTSTRAP.md`, apesar de regra vigente declarar o bootstrap obsoleto/removido.

## Agentes, sessoes e trajetorias

- Agentes locais auditados em `/data/.openclaw/agents/`: 21.
- Sessoes visiveis recentes via OpenClaw: 20 listadas.
- Arquivos locais de sessao `.jsonl` em `/data/.openclaw/agents/*/sessions/`: 722.
- Arquivos locais de sessao `.jsonl` alterados desde 2026-08-16 03:00 UTC: 41.
- Trajetorias `.trajectory.jsonl`: 265 no total; 14 alteradas desde 2026-08-16 03:00 UTC.
- Sessoes recentes observadas:
  - cron atual de governanca;
  - DM principal com pauta do dia 18/08;
  - cron `sinal-proximo-dia-2100`;
  - cron de lembrete pessoal do Alfred;
  - Jarvis/Saude sobre consulta ao Cofre e skill da Saude;
  - crons de pauta/producao;
  - topico da Camara com proposta de skill ainda pendente no Skill Workshop.
- Validacao de conhecimento:
  - a pauta do dia 18/08 ja foi enviada em DM e usa fontes do Cofre e Google Calendar.
  - a orientacao de sempre consultar Cofre/skill para Saude ja esta registrada em memoria recente e foi reforcada em sessao.
  - o mapa preparatorio da Camara ja consta no Cofre em `50-clientes/20-camara-municipal/00-indice/2026-08-14-mapa-real-skill-comunicacao-camara.md`.
  - nao identifiquei decisao permanente nova a consolidar sem validacao humana adicional.
- Nada foi removido ou movido em sessoes/trajetorias.

## SQLite, logs e caches

- Nenhum arquivo SQLite foi identificado dentro do Cofre ativo pela varredura direta.
- SQLite dos agentes fora do Cofre foi auditado por listagem. Bancos principais observados em `/data/.openclaw/agents/*/agent/` e `/data/.openclaw/agents/*/agent/codex-home/`.
- Maiores bancos/logs recentes fora do Cofre:
  - main `logs_2.sqlite`: cerca de 169M.
  - main `openclaw-agent.sqlite`: cerca de 58M.
  - jarvis `logs_2.sqlite`: cerca de 61M.
  - central-topic-agent `logs_2.sqlite`: cerca de 63M.
  - cfo `logs_2.sqlite`: cerca de 40M.
  - alfred `logs_2.sqlite`: cerca de 33M.
- Caches externos dos agentes: cerca de 1.3M a 1.5M por agente em `agent/codex-home/cache`.
- `tmp` externo dos agentes: 0 nos diretorios auditados, apenas locks vazios observados.
- Acao tomada: nenhuma limpeza executada.

## Anexos temporarios e midia

- Dentro do Cofre, `media/` tem 3.9M.
- `70-agentes/runtime/logika/media/` aparece como nao rastreado e precisa revisao antes de qualquer backup.
- Nao encontrei pastas `cache`, `tmp`, `temp`, `attachments` ou `anexos` dentro do Cofre ativo pela varredura direta.
- Nenhum anexo temporario foi movido, deletado ou compactado.
- Removidos: 0.
- Espaco recuperado: 0.

## Auditoria de segredos

- Varredura por nomes/padroes sensiveis foi executada sem imprimir valores.
- `scripts/.secrets/` existe e esta ignorado pelo Git; deve permanecer fora do backup.
- Arquivos locais sensiveis conhecidos preservados e nao exibidos:
  - `scripts/.secrets/gog-keyring-password`
  - `scripts/.secrets/google-calendar-credentials.json`
  - `scripts/.secrets/google-calendar-token.json`
  - `scripts/.secrets/notion.env`
  - `scripts/.secrets/notion-logika-producao.env`
- `.gog/data/keyring/.lock` e `scripts/data/keyring/.lock` aparecem como nao rastreados; revisar/ignorar antes de commit.
- `rg` encontrou muitos arquivos com palavras/padroes como `token`, `secret`, `password` ou `authorization`, sobretudo em scripts e legado. A maior parte parece referencia textual ou codigo, mas exige revisao humana/tecnica antes de backup seletivo amplo.
- Backup remoto bloqueado ate separacao segura de segredos, locks e estado local.

## Consolidacao

- Conhecimento novo consolidado nesta rotina: apenas este relatorio de governanca.
- Decisoes permanentes novas: nenhuma.
- Processos permanentes novos: nenhum.
- Preferencias permanentes novas: nenhuma.
- Pendencias permanentes novas: registradas abaixo como pendencias de governanca.
- Nada foi excluido definitivamente.
- Nada foi movido para quarentena.

## Candidatos a limpeza/quarentena

Nao houve quarentena autorizada. Candidatos abaixo sao apenas para revisao, sem acao automatica:

- `.gog/` e `scripts/data/`: confirmar se devem entrar no `.gitignore` e permanecer fora do versionamento.
- `BOOTSTRAP.md`: revisar reaparecimento, pois a regra vigente diz que o bootstrap esta obsoleto/removido.
- Remocoes de `memory/inbox-externa/`: confirmar se a migracao para `00-central/inbox/externa/` e `90-arquivo/30-regras-obsoletas/2026-08-10-inbox-legado/` esta completa.
- `memory/.dreams/short-term-recall.json.u4s-superseded-*`: possivel artefato de migracao; preservar ate confirmacao.
- Caches externos `agent/codex-home/cache`: candidatos tecnicos futuros, mas pequenos e sem necessidade de limpeza agora.

## Erros e pendencias

- `memory/2026-08-18.md` e `memory/2026-08-17.md` ausentes; preservado conforme regra de nao criar automaticamente.
- Commit/push bloqueado por worktree ambiguo e possivel superficie de segredo/estado local.
- Revisar 94 entradas do `git status` e separar:
  - mudancas canonicas seguras para commit;
  - remocoes que representam migracao confirmada;
  - arquivos que devem entrar em `.gitignore`;
  - scripts que devem ser auditados sem expor tokens;
  - entregas de cliente que ainda precisam consolidacao exata.
- Confirmar se os relatorios de governanca de 2026-08-11 a 2026-08-18 devem entrar juntos em commit futuro.
- Revisar proposta pendente da skill da Camara no Skill Workshop antes de tratar como aplicada.

## Resultado final

- Sessoes analisadas: 20 visiveis via OpenClaw, 722 arquivos locais de sessao por contagem, 41 sessoes recentes e 14 trajetorias recentes por varredura.
- Consolidadas: 1 relatorio de governanca.
- Removidas: 0.
- Espaco recuperado: 0.
- Backup remoto: nao executado.
- Hash remoto confirmado: `91e070c91a244b5c5bb3b8fadbc11413e0f8c072`.
- Status: rotina concluida em modo conservador, com backup bloqueado por seguranca.

Fonte: Cofre (`CONSTITUICAO.md`, `AGENTS.md`, `MAPA.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `MEMORY.md`), filesystem local, Git, OpenClaw sessions, auditoria direta por `find`, `du`, `rg`.
