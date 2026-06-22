# Análise do mapa do curso OpenClaw — prioridades para quitação

Data: 2026-06-05 UTC
Solicitante: Jadielson Davi
Fonte principal analisada: Google Drive “Construindo seus primeiros agentes (Mini-curso Openclaw v2 stand-alone)”
Link: https://drive.google.com/drive/folders/1plqRaWoEN13mLY8rnUJV8KNzk-4a8Jl-

## Evidências consultadas

- Documento do Drive `1.📍 LEIA PRIMEIRO (MAPA DO CURSO)` exportado como texto.
- Estrutura visível da pasta do Drive:
  - `💡 Cases de inspiração`
  - `📋 Referências para seu agente (material complementar)`
  - `📝 Transcrições do mini-curso`
  - `🧠 Materiais Aula`
  - `🧰 Templates (soul, user, identity, tools, etc)`
  - `🛠️ Starter kit (wizard openclaw)`
  - `Migrando do Claude para ChatGPT`
  - `1.📍 LEIA PRIMEIRO (MAPA DO CURSO)`
  - `2. Faça download desta pasta do Google Drive e mande para seu agente`
  - `3. Changelog (atualizações dos materiais)`
  - `Se você veio do mini-curso 1.0 - O que você precisa saber`
- Índice local do curso: `_curso/INDICE.md`.
- Relatório local: `reports/reanalise-starter-kit-v2.5.7-2026-06-04.md`.
- Comando `openclaw status --deep`.
- Comando `openclaw cron list`.

## Conclusão executiva

A instalação principal do curso/Starter Kit está praticamente quitada no ambiente da Lôh.

Não há pendência crítica de Starter Kit, identidade, workspace, memória básica, skills do kit, backup ou Google Workspace. O que falta agora não é “fazer o curso do zero”; é fechar pendências operacionais e transformar a estrutura em uso real para a LÓGIKA.

## O que já está quitado ou muito avançado

### 1. Base do agente e Starter Kit

Status: quitado.

- Arquivos essenciais existem: `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `MAPA.md`, `HEARTBEAT.md`, `TOOLS.md`, `MEMORY.md`.
- Todas as skills do Starter Kit v2.5.7 estão presentes.
- Jornada do Starter Kit consta como concluída.
- Primeira vitória existe em `content/drafts/primeira-vitoria-post-2026-05-31.md`.
- Material do curso já está preservado localmente em `_curso/`.

### 2. Memória e organização do workspace

Status: quitado com manutenção contínua.

- `MEMORY.md` está ativo e com decisões importantes.
- `MAPA.md` organiza o workspace.
- Existem pastas para conteúdo, memória, projetos, skills, arquivo e relatórios.
- Regra operacional de salvar e fazer backup instantâneo já está registrada.

### 3. Backup GitHub

Status: quitado.

- Cron `backup-workspace-github` ativo diariamente às 03:00 America/Maceio.
- Script `scripts/backup-workspace-github.sh` existe.

### 4. Segundo cérebro / Obsidian

Status: avançado.

- Cron `sync-segundo-cerebro-jadielson` ativo diariamente às 03:10 America/Maceio.
- Vault local existe em `vaults/segundo-cerebro-jadielson`.

### 5. Google Workspace

Status: quitado para o escopo aprovado.

- `gog` CLI instalado e contas conectadas.
- Contas conectadas: Lôh, LÓGIKA e pessoal.
- Calendar/Docs/Sheets com escrita; Drive limitado; Gmail somente leitura; Contacts leitura.
- Regra de segurança aprovada: Gmail sem envio automático; exclusão de Drive exige confirmação humana.

### 6. Multiagentes / arquitetura

Status: avançado, mas ainda em fase de desenho/ativação prática.

- Arquitetura definida: Lôh como gerente geral.
- Alfred definido como General da Central Pessoal.
- Jarvis definido como General da LÓGIKA.
- Documento principal: `agentes/ARQUITETURA-AGENTES.md`.

## Pendências reais para “quitar”

### P0 — Fechar WhatsApp

Prioridade: alta.
Motivo: é o canal operacional mais importante para uso real com clientes, rotina e agência.

Estado atual pelo `openclaw status --deep`:

- Telegram: ON / OK.
- WhatsApp: ON / SETUP / not linked.

Ação recomendada:

1. Rodar o wizard/pareamento do WhatsApp.
2. Confirmar envio/recebimento.
3. Registrar a conta/canal em `TOOLS.md` ou memória operacional.

### P0 — Reduzir risco de segurança do exec full

Prioridade: alta.
Motivo: o status mostra `Exec security=full`; isso é poderoso, mas arriscado.

Estado atual:

- Security audit: 0 critical, 2 warnings.
- Warning principal: `Exec security=full is configured`.

Ação recomendada:

1. Decidir se mantém full por enquanto por causa da fase de implantação.
2. Se quiser produção mais segura, migrar para allowlist/ask prompts.
3. Registrar uma política clara: quando Lôh pode executar direto e quando precisa pedir.

### P1 — Transformar Jarvis em operação real da LÓGIKA

Prioridade: alta para aplicação prática.
Motivo: a arquitetura existe, mas precisa virar rotina operacional.

O que falta:

- Definir escopo final do Jarvis.
- Criar/ativar comportamento por grupo/tópico da LÓGIKA.
- Padronizar triagem de tarefas, clientes, produção, propostas e entregas.
- Integrar com o Notion já diagnosticado.

Ação recomendada:

1. Fechar o documento de poderes/limites do Jarvis.
2. Criar checklist operacional diário/semanal.
3. Validar fluxo: mensagem no grupo → triagem → tarefa → acompanhamento → entrega.

### P1 — Fechar Mission Control / painel de comando

Prioridade: média-alta.
Motivo: é a parte final do curso que dá visão de controle.

O que falta:

- Escolher onde será o controle principal: Notion, Obsidian, planilha ou dashboard simples.
- Padronizar indicadores mínimos:
  - tarefas abertas;
  - clientes/projetos ativos;
  - calendário;
  - pendências de conteúdo;
  - automações ativas;
  - riscos/alertas.

### P1 — Notion da LÓGIKA: sair do diagnóstico para uso diário

Prioridade: média-alta.
Motivo: existem muitos arquivos de diagnóstico/migração, mas precisa estabilizar o uso.

Sinais locais:

- Há vários arquivos `notion-logika-*` indicando trabalho avançado de inventário, schemas e migração.

Ação recomendada:

1. Definir a base final única.
2. Arquivar bases/testes antigas.
3. Criar rotina de entrada única: Inbox LÓGIKA.
4. Conectar Jarvis/Lôh ao processo.

### P2 — Atualização do OpenClaw

Prioridade: média/baixa, não fazer automaticamente.

Estado atual:

- `openclaw status --deep` mostra atualização disponível `2026.6.1`.

Regra:

- Só atualizar com pedido explícito do Jadielson.

### P2 — Service/systemd

Prioridade: média/baixa.

Estado atual:

- Gateway service: systemd user not installed.
- Node service: systemd user not installed.

Interpretação:

- Não impede uso atual se o Gateway está rodando.
- Mas para produção estável, vale planejar serviço/autostart/recovery.

### P2 — Heartbeat prático

Prioridade: média.

Estado atual:

- Heartbeat ativo a cada 30min.
- `HEARTBEAT.md` ainda está praticamente vazio.

Ação recomendada:

- Criar checklist leve de checagens periódicas: agenda, inbox, backups, Notion/Jarvis, alertas.

## Ordem recomendada de execução

1. Parear WhatsApp.
2. Definir política de segurança do exec/configuração.
3. Fechar Jarvis como coordenador real da LÓGIKA.
4. Estabilizar Notion/Inbox LÓGIKA.
5. Montar Mission Control mínimo.
6. Preencher Heartbeat com checagens úteis.
7. Só depois avaliar update do OpenClaw e systemd/autostart.

## Veredito

Para critério de curso/Starter Kit: pode considerar quase quitado.

Para critério de aplicação real na agência: ainda faltam WhatsApp, Jarvis operacional, Notion estabilizado e Mission Control mínimo.

Minha recomendação é não reabrir o curso inteiro. Tratar agora como fase de fechamento operacional, com foco no que gera uso diário e reduz risco.

## Atualização de prioridade após resposta do Jadielson

Após a devolutiva do Jadielson em 2026-06-05, a fila recomendada foi ajustada:

1. Configurar todos os agentes ainda hoje, começando pela **Central Pessoal**.
2. Deixar **WhatsApp** para mais tarde.
3. Deixar ajuste de **segurança/exec full** para depois, sem travar a configuração dos agentes.
4. Prosseguir com **LÓGIKA/Jarvis** após avançar na Central Pessoal.
5. Manter **Notion/Inbox LÓGIKA** em andamento, sem bloquear a configuração dos agentes.
6. Deixar **Mission Control** para depois, pois agora é considerado mais estético do que essencial.
7. Definir **Heartbeat** corretamente como parte da configuração operacional.
8. Deixar **update OpenClaw/systemd/autostart** para depois.

Prioridade prática revisada: **arquitetura de agentes > Central Pessoal primeiro > Heartbeat definido > LÓGIKA/Jarvis depois > canais/update/painéis depois**.
