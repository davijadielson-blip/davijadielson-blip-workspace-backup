---
tipo: estado-operacional
subtipo: pendencias
ultimo-update: 2026-05-23
agente-compatibilidade: [claude, openclaw, gpt, hermes]
---

# Pendências

> Atualizar sempre que uma tarefa mudar de status. A IA lê este arquivo para priorizar o Top 3 do dia.

---

## 🔴 Críticas
*(prazo ≤ 3 dias ou bloqueando outro trabalho)*

- [ ] Renovar chave Anthropic local — `scripts/.secrets/anthropic.env` retorna 401 (chave exposta/revogada em 2026-05-24)
- [ ] Revisar e enviar agenda ASCOM à Secretaria — `[F2] memory/outputs/drafts/sms-agenda-ascom-ENTREGA-22maio2026.md` (revisado: false)
- [x] Revogar e renovar chave Anthropic API em console.anthropic.com — feito em 2026-05-24 (Railway atualizado)

---

## 🟡 Importantes
*(prazo ≤ 2 semanas ou impacto direto em cliente)*

- [ ] Finalizar plano de propostas de serviços da Lógika Creative
- [ ] 2026-06-27 — LÓGIKA | soluções digitais: validar visualmente Drive da identidade atual e fechar briefing final de ID visual
- [ ] 2026-06-27 — LÓGIKA | soluções digitais: validar campos da database Notion Leads/Clientes e desenhar fluxo Make.com
- [ ] 2026-06-27 — LÓGIKA | soluções digitais: criar modelos completos das propostas comerciais prioritárias
- [ ] 2026-06-27 — AGENTE CEO LÓGIKA: acompanhar parecer executivo 7/30/90 dias no tópico Telegram
- [ ] Lançamento do vídeo clipe *Entre Tempo*
- [x] Movimentar documentário *O Fio da Memória*
- [ ] Finalizar vídeo JD Auto Center
- [x] Preencher entregas em aberto Câmara / SINDSS / SMS em `[F2] memory/context/pendencias.md`

---

## 🟡 Importantes
*(prazo ≤ 2 semanas ou impacto direto em cliente)*

- [x] Parar daemon local Telegram permanentemente — plist desabilitado em 2026-05-24
- [x] Verificar se `[F1] 5-Frentes/` está no repo GitHub — confirmado em 2026-05-24

---

## ⚪ Backlog
*(sem prazo fixo — fazer quando der)*

- [x] SINDSS — CONTEXTO EDITORIAL condensado em `[F2] memory/agents/sindss.md` e calendário sazonal atualizado (2026-05-23)
- [ ] Preencher CONTEXTO EDITORIAL das frentes Câmara, Lógika, Rogério, Além da Foto (igual ao que existe para Saúde e SINDSS) — melhora qualidade do /gerar
- [ ] Testar `/gerar` nas frentes sem CONTEXTO EDITORIAL para validar qualidade baseline
- [ ] Grade SMS: confirmar cargo de Amanda Peixoto e Hubson Santos (já confirmados) — arquivo atualizado ✅

- [ ] Configurar Dashboard Financeiro integrado ao vault
- [ ] Pull de fontes externas (Gmail/Drive/WhatsApp) — prompt dedicado
- [ ] `2026-05-17.md` vazio na raiz do vault — mover para `[F3] 3-Daily/` ou deletar
- [ ] Preencher card mestre (template-curso) dos cursos em EM ANDAMENTO: ERUPÇÃO DE SEGUIDORES, TURBOSAAS, VENDE-C, CONQUER ENGLISH
- [ ] Mover CONQUER ENGLISH para ESTUDOS/EM ANDAMENTO/ como pasta com card mestre + subpasta de aulas
- [ ] Apagar artefatos de teste do /projeto: `PROJETOS/A INICIAR/TESTE 2/`, `PROJETOS/IDEIAS NOVAS/TESTE 3.md`, `PROJETOS/IDEIAS NOVAS/IDEIA SEM NOME.md`

---

## ⚪ Backlog

- [x] 2026-06-18 — Sync bidirecional configurado: `vault-git-sync-claude.sh` agora faz `git pull --rebase` a cada 5 min independente de mudanças locais

---

## ✅ Resolvidas *(últimas 7 dias)*

- [x] 2026-06-18 — Migração autenticação GitHub: HTTPS com token embutido → SSH com chave ed25519
- [x] 2026-06-18 — Rebase interativo travado resolvido (`rebase --continue`)
- [x] 2026-06-18 — Histórico divergente (local 44 commits + remote 46 commits) unificado via merge


- [x] 2026-05-17 — Câmara + SINDSS: sync Notion→Calendar ativo (0 itens, pronto para receber conteúdo)

- [x] 2026-05-17 — FASE A: NOTION_TOKEN unificado — 404 resolvido
- [x] 2026-05-17 — FASE B: .git movido para fora do OneDrive via symlink
- [x] 2026-05-17 — FASE C: bug all-day event corrigido (end = start + 1 dia)
- [x] 2026-05-17 — FASE D: confirmação estruturada pós-captura no Telegram
- [x] 2026-05-17 — FASE E: lembretes 13h e 17h criados (launchd)
- [x] 2026-05-17 — FASE F: limpeza git (sync logs, artefatos Obsidian, drafts)
- [x] 2026-05-17 — FASE G: inbox — frontmatter escondido, nomes em caixa alta
- [x] 2026-05-17 — FASE H: validação end-to-end — sistema saudável
- [x] 2026-05-17 — Template inbox: seção Destino com triagem tarefa/ideia/projeto
- [x] 2026-05-10 — PAT do GitHub revogado e regenerado (segurança)
- [x] 2026-05-10 — Migração arquitetural v2 — vault + GitHub
