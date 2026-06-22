---
tipo: decisoes-mensais
mes: 2026-05
ultimo-update: 2026-05-18
agente-compatibilidade: [claude, openclaw, gpt, hermes]
---

# Decisões — Maio 2026

> Registro consolidado das decisões arquiteturais tomadas neste mês.
> Fonte: migração de `[F2] memory/decisions/` (8 arquivos) + decisões da migração v2.

---

## 18/05 — Bot Telegram com 8 comandos interativos + long polling

**Contexto:** bot só fazia captura por prefixo e tinha latência de 60–120s (launchd StartInterval:120).
**Decisão:**
- 4 comandos simples: `/start`, `/status`, `/agenda`, `/buscar`
- 3 ações sobre última captura: `/confirmar`, `/cancelar` (botão obrigatório), `/repetir`
- 1 menu interativo: `/menu` (botões inline + fluxo 5 telas + histórico Voltar)
- Estado conversacional em `scripts/state/telegram-state.json`, expira em 1h
- Operação imediata (sem rascunho), `/cancelar` exige clique explícito
- Convertido para daemon long-polling (KeepAlive + timeout=25) — latência de 60s → <1s
- TMP com PID fixo (`/tmp/tg-polling-$$.json`) para evitar conflito em loop persistente
**Status:** ✅ Implementado e validado (latência <1s confirmada pelo Jadielson)

---

## 17/05 — .git movido para fora do OneDrive via symlink

**Contexto:** OneDrive segurava locks em `.git/objects` durante `git commit/push` nos crons, causando `fatal: mmap failed: Resource deadlock avoided` em daily-brief e saturday-planning.
**Decisão:** `.git` movido para `~/.mapa-obsidian-git`, symlink criado em `$VAULT/.git`.
**Implicação:** ao clonar em outra máquina, o `.git` precisa ser clonado separado (o symlink não viaja).
**Owner:** Jadielson. **Status:** ✅ Implementado em 17/05/2026

---

## 17/05 — Token Notion unificado em NOTION_TOKEN

**Contexto:** dois tokens coexistiam (`NOTION_TOKEN` e `NOTION_SYNC_TOKEN`), cada um com acesso a databases diferentes. `notion-to-calendar.py` usava o token errado (hardcoded), causando 404 no sync.
**Decisão:** manter apenas `NOTION_TOKEN` (integration `segundo-cerebro-escrita`). Saúde Editorial reconectada via Notion Connections.
**Owner:** Jadielson. **Status:** ✅ Implementado em 17/05/2026

---

## 11/05 — Saída da Emily da equipe

**Decisão:** Emily não faz mais parte da equipe. Removida de todos os registros em `[F2] memory/`.
**Impacto:** custo de R$200/mês deixa de existir. Tarefas redistribuídas para Jadielson.
**Obs:** 2 notas em `[F1] 4-Pessoal/Proposito-e-Vida/Plano Estratégico/` ainda mencionam Emily — edição manual de Jadielson quando quiser.
**Owner:** Jadielson. **Status:** ✅ Tomada

---

## 11/05 — Reorganização de canais e horários dos crons

**Decisão:**
- Briefings entregues por Telegram (primário) + Email Gmail SMTP (backup).
- Sábado 17h substitui domingo 8h — libera domingo para descanso/família.
- Sexta 18h substitui 16h45 — evita conflito com sessões da Câmara.
- Domingo sem cron automático.
**Owner:** Jadielson. **Status:** ✅ Tomada

---

## [10/05] Migração Arquitetural v2

**Contexto:** Fusão da estrutura existente (3 Fluxos + 4 Camadas + subagents + slash commands + hooks) com o kit de segundo cérebro maduro (context/, sessions/, skills/, scripts/, _MAP.md, PROPAGATION.md).

**Decisões:**
- Renomeada `[F2] claude/` → `[F2] memory/` (mais semântico, alinhado com o kit)
- CLAUDE.md movido para raiz do vault (carregamento prioritário pelo Claude Code)
- Adotada estrutura `[F2] memory/context/` com 5 arquivos de estado atual
- Adotado `PROPAGATION.md` como protocolo formal de propagação
- Adotados mapas `_MAP.md` em todas as pastas principais
- Adotadas skills: `cerebro`, `rotina`, `salve`, `reindex`
- Ativados 3 cron-jobs: daily-brief (7h), sunday-planning (dom 8h), friday-maintenance (sex 16h45)
- Configurado Git local + GitHub remoto privado + push por commit

**Mantidos sem mudança:** regra de ouro, 3 Fluxos, 4 Camadas, subagents, slash commands, hooks, visualizações.

**Próximas evoluções (separadas):** pull de fontes externas (Gmail/Drive/WhatsApp), dashboard financeiro integrado.

**Owner:** Jadielson + Claude Code | **Status:** ✅ Em execução

---

## [10/05] Estrutura Inicial do Vault — 3 Fluxos + 4 Camadas

**Contexto:** Vault anterior misturava notas autorais, outputs de IA e referências sem separação clara.

**Decisão:** Adotar o método 3 Fluxos + 4 Camadas como estrutura permanente.

**Decisões específicas:**
- `CLAUDE_OBSIDIAN.md` → arquivado em `[F2] memory/decisions/`; CLAUDE.md único na raiz
- Rogério Rocha → cliente **inativo** em `[F1] 5-Frentes/Inativos/`
- Pastas vazias → deletadas

**Status:** ✅ Implementada

---

## [10/05] Subagents Nativos do Claude Code

**Contexto:** Briefings em `[F2] memory/agents/` dependiam de invocação manual. Subagents nativos em `.claude/agents/` permitem invocação por `@nome` ou automática.

**Decisão:** Manter dois sistemas coexistindo — briefings em `[F2] memory/agents/` (contexto rico) + subagents em `.claude/agents/` (invocação nativa).

**Subagents criados:** @logika, @rogerio, @saude, @camara, @sindss, @vereadores, @alem-da-foto, @lives-louvor, @pessoal, @bibliotecaria.

**Status:** ✅ Implementado

---

## [10/05] Slash Commands do Vault

**Decisão:** 22 comandos em `.claude/commands/` cobrindo rotina, legendas, posts por frente, agenda e manutenção. Todo output nasce em `[F2] memory/outputs/` — nunca direto na pasta da frente.

**Comandos:** /hoje, /captura, /legenda, /revisar, /post-saude, /post-camara, /post-sindss, /post-rogerio, /post-logika, /roteiro-rogerio, /planejar-semana, /manutencao, /sazonal, /aniversariante, /busca, /conecta, /ideia, /resumo-whats, /agenda, /agendar, /sincronizar-sazonais, /bloquear-rotina.

**Status:** ✅ Implementado

---

## [10/05] Hooks do Claude Code

**Decisão:** 4 hooks em `.claude/hooks/` cobrindo SessionStart (briefing automático), PromptGuard (proteções de fluxo), PostWrite (automações pós-escrita) e Stop (log incremental).

**Regra:** hooks nunca publicam, nunca decidem, nunca bloqueiam o fluxo.

**Status:** ✅ Implementado

---

## [10/05] Integração Google Calendar

**Decisão:** Usar MCP nativo `mcp__claude_ai_Google_Calendar__*` para buscar eventos reais. Classificação por frente via `[F2] memory/databases/regras-classificacao-agenda.md`.

**Comandos que usam:** /agenda, /agendar, /hoje, /bloquear-rotina, /sincronizar-sazonais.

**Status:** ✅ Implementado

---

## [10/05] Convenção de Tags de Produção

**Tags adotadas:**
- `#producao/ideia` — conceito não desenvolvido
- `#producao/roteiro` — texto escrito, aguardando captação
- `#producao/captura` — gravação realizada, aguardando edição
- `#producao/edicao` — em edição
- `#producao/revisao` — editado, aguardando aprovação
- `#producao/publicado` — publicado em plataforma

**Status:** ✅ Adotada

---

## 16/05 — Sistema Operacional Pessoal — Diretor de Comunicação

**Contexto:** Salto conceitual de "homem-banda reativo" para "Diretor de Comunicação com sistema completo". Sessão de maior escala arquitetural do vault até agora.

**Decisões tomadas:**
- Rotina-Diretor formalizada em `[F2] memory/context/rotina.md` (Inversão Biológica + tetos + Zero-Sum + Ancoragem)
- Matriz dos 5 Destinos criada com 37 tarefas categorizadas em `[F2] memory/databases/matriz-tarefas.md`
- Plano de 30 dias com despertar progressivo (06h → 04h30) criado em `[F2] memory/projects/plano-30-dias-diretor.md`
- Cockpit Híbrido: Database Notion "🚀 Cockpit Diretor" (ID: e6d0b774-ebe0-4761-a61b-1a30e16db091) + `cockpit.html` gerado pelo daily-brief
- 4 camadas de skills mapeadas em `[F2] memory/_MAP-skills.md` com gatilhos automáticos
- Projeto Regra 1/3 (patrimônio judaico) iniciado em `[F2] memory/projects/regra-1-3-patrimonio.md` — revisão trimestral
- Hub.md reordenado com nova hierarquia: Agora → Top 3 → Cockpit → Inbox → Horas Institucionais → Status dos Sistemas
- CLAUDE.md atualizado para v3.1 com Instrução Primária de Diretor de Comunicação no topo
- PROPAGATION.md atualizado com 4 novas regras (janela institucional, Matriz, SOP/Sistema, Regra 1/3)
- `[F2] memory/projects/` criada como nova subpasta (não existia)

**Owner:** Jadielson + Claude Code (sessão 2026-05-16)
**Status:** ✅ Implementado — tag v3.2.0-sistema-operacional-diretor
**Próxima revisão:** 2026-06-15 (KPIs do plano 30 dias) + 2026-08-14 (Regra 1/3 — trimestral)

---

## [10/05] Paleta de Cores por Frente (Canvas)

| Frente | Cor | Código Obsidian |
|---|---|---|
| Lógika Creative | Azul | `"6"` |
| Saúde | Ciano | `"5"` |
| Câmara Municipal | Amarelo | `"3"` |
| SINDSS | Vermelho | `"1"` |
| Outros Vereadores | Amarelo | `"3"` |
| ALÉM DA FOTO | Verde | `"4"` |
| Lives de Louvor | Laranja | `"2"` |
| Rogério Rocha (inativo) | Roxo | `"7"` |

**Status:** ✅ Adotada

---

## [10/05] Camada de Visualização

**Decisão:** Criar Hub central, Canvas geral, dashboards Dataview e diagramas Mermaid em `[F2] memory/visualizations/`.

**Arquivos criados:** Hub.md, Vault-Map.canvas, comandos.md, subagents.md + dashboards e diagramas por frente.

**Status:** ✅ Implementada

---

## [24/05] Reapontamento do sistema pro vault novo após path fantasma

**Contexto:** vault velho (`OneDrive-Pessoal/Documentos/Obsidian Vault 4/MAPA OBSIDIAN`) não existia mais. Symlink `/Users/servicepro/MAPA OBSIDIAN` apontava para esse path fantasma. Crons rodavam contra o vazio silenciosamente desde a migração do OneDrive.

**Causa raiz:** vault foi migrado/recriado em `OneDrive-Pessoal(2)/01_PESSOAL/Obsidian Vault 4/MAPA OBSIDIAN` em momento não-rastreado. Symlink nunca foi atualizado. Plists já usavam o path novo correto (migrados anteriormente). Somente o symlink e o arquivo `.git` estavam desatualizados.

**Decisões tomadas:**
- Symlink atualizado: agora aponta para `OneDrive-Pessoal(2)/01_PESSOAL/Obsidian Vault 4/MAPA OBSIDIAN`
- Arquivo `.git` corrigido: adicionado prefixo `gitdir:` obrigatório (estava apenas o path raw)
- `telegram-state.json` limpo: fluxo expirado com path velho removido
- Plists: já estavam corretos — nenhuma edição necessária
- Crons: reativados via `launchctl unload` + `load` — todos 7 carregados, 6 com exit code 0, cockpit-server rodando na porta 8765

**Validação:** daily-brief executado manualmente — commit, email e Telegram chegaram. ✅

**Status:** ✅ Reapontado e testado.

**Próximos passos:**
- Não usar mais `OneDrive-Pessoal/Documentos/` para nada relacionado ao vault
- Considerar arquivar o OneDrive-Pessoal antigo se não houver mais nada útil

---

## [24/05] Consolidação final dos crons + fix EDEADLK do Telegram

**Contexto:** após reapontamento (v3.3.1), descoberta de 3 crons fora do controle:
- `cockpit-server` (exit code 78 histórico)
- `monthly-archive` (criado 23/mai por sessão externa)
- `telegram-polling.disabled` (desativado — bot parado)

**Investigação:**
- `cockpit-server` — já estava rodando (200 OK porta 8765). Exit code 78 era histórico de 20/mai. Nenhuma ação necessária.
- `monthly-archive` — script correto, paths relativos, sem hardcoded. Roda dia 1/mês às 8h. Primeira execução: 1/jun. Nenhuma ação necessária.
- `telegram-polling` — identificado bug EDEADLK: `telegram-router.py` recarregava `telegram-commands.py` do vault (OneDrive) a cada mensagem via `spec.loader.exec_module`. Quando OneDrive sincronizava em paralelo → kernel retornava `EDEADLK` → crash em loop.

**Fix aplicado:**
- `telegram-router.py`: `_cmds()` e `_sm()` transformados de "recarrega por mensagem do vault" para "carrega uma vez de `/tmp/tg-lib`" (cópias que `telegram-polling.sh` já faz no startup).
- `telegram-commands.py`: `_load_once` ajustado para preferir `/tmp/tg-lib` via `_lib_path()`.
- Reativado via `launchctl load -w` (o plist tinha estado "disabled" gravado internamente no launchd além do nome de arquivo).

**Validação:** mensagem `/i teste` respondida em menos de 1 segundo. ✅

**Crons ativos finais (8 total):**
- `daily-brief`, `midday-reminder`, `end-of-day-reminder`, `friday-maintenance`, `saturday-planning`, `monthly-archive` — exit code 0
- `cockpit-server` — rodando na porta 8765 (exit code 78 histórico, processo ativo)
- `telegram-polling` — PID ativo, long-poll < 1s

**Status:** ✅ Sistema consolidado — v3.3.2.

---

### [24/05] Migração estrutural completa dos projetos — v3.4.0

**Contexto:** Vault tinha projetos espalhados em pastas fora do pipeline (Projetos-Pessoais/, [F1] 5-Frentes/Projetos/, [F1] 4-Pessoal/, MEUS PROPÓSITOS/), todos como arquivos .md planos sem estrutura padrão.

**Decisão:** Migrar todos para estrutura de pasta padrão: `<NOME>/<NOME>.md` + `1-briefing.md` + `proximas-etapas.md` + subpastas (2-pesquisas, 3-dados, 4-decisoes, 5-resumos-semanais, 6-entregas, 7-arquivo). Templates em `PROJETOS/_templates/`.

**Lotes executados:**
- Lote 1: EM ANDAMENTO (1 projeto — O FIO DA MEMÓRIA)
- Lote 2: A INICIAR (25 projetos — script Python)
- Lote 3A/B: Projetos-Pessoais (25 planos + 3 subpastas → A INICIAR)
- Lote 3C: Frentes/Projetos (9 Pensando → A INICIAR, 1 Arquivado → PAUSADO)
- Lote 4: [F1] 4-Pessoal (10 root + 7 MEUS PROPÓSITOS → A INICIAR)
- Lote 5: PROJETOS/MEUS PROPÓSITOS (12 projetos → A INICIAR)

**Resultado final:** 1 EM ANDAMENTO · 91 A INICIAR · 1 PAUSADO · 1 IDEIA NOVA.
Validação: todos os projetos têm main file + `tipo: projeto` + `frente:`. ✅

**Pendências manuais (duplicatas):** ~10 itens marcados com sufixo `(Pessoal)` ou `(Propósitos)` para consolidação pelo Jadielson.

**Status:** ✅ Migração concluída — tag v3.4.0.

---

### [24/05] Auditoria Fase D — 5 arquivos do Sistema Operacional — v3.5.0

**Contexto:** 5 arquivos centrais do Sistema Operacional criados em 16/05 nunca foram revisados após a migração.

**Arquivos auditados:**
- `[F2] memory/context/rotina.md` — 🟡 Despertar Progressivo atualizado (Semana 1 ✅ → Semana 2 atual); `revisado: true`
- `[F2] memory/databases/matriz-tarefas.md` — ✅ Correto; `revisado: true`
- `[F2] memory/projects/regra-1-3-patrimonio.md` — ✅ Correto (Sessão 1 aguarda Jadielson); `revisado: true`
- `[F2] memory/projects/plano-30-dias-diretor.md` — 🟡 `semana-atual: 1 → 2`; typo "treinsar" → "treinar"; `revisado: true`
- `[F2] memory/_MAP-skills.md` — 🟡 Nota stale `/mnt/skills/user/` substituída por nota de objetivo futuro; `revisado: true`

**Status:** ✅ Auditoria concluída — prontos para tag v3.5.0.
