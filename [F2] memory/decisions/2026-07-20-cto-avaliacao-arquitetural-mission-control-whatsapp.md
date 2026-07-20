# Decisão — Avaliação Arquitetural CTO: Mission Control + WhatsApp

**Data:** 2026-07-20  
**Agente:** 👤 CTO — Chief Technology Officer  
**Decisor da análise:** CTO (recomendação para Jadielson via Lôh)  
**Status:** ✅ Análise concluída, aguardando validação de Jadielson

---

## Decisões recomendadas

### 1. Mission Control — Build vs. Buy

**Recomendação:** **Buy primeiro (xTiles), Build depois se validar.**

- xTiles como protótipo visual por 7-14 dias
- Só construir app próprio (Next.js + Supabase + Tailwind + Vercel, ~$55-75/mês) se houver uso consistente comprovado
- Stack para app próprio documentada: Next.js 14+, Supabase (PostgreSQL + Realtime + Auth), Drizzle/Prisma ORM, NextAuth.js, Vercel deploy

### 2. WhatsApp Inteligente — Base Técnica

**Recomendação:** Avançar com estruturação gradual.

- Criar lookup de cliente por número (CRM Notion/Cofre)
- Indexar histórico por número (`memory/atendimentos/{numero}/`)
- Formalizar SLA por tier (Diamante/Ouro/Prata/Bronze)
- Não automatizar resposta sem aprovação de Jadielson
- CIOPrecisa auditar LGPD antes de avançar com retenção de mensagens

### 3. Dívida Técnica — P0 Urgente

**Recomendação:** Corrigir `memory_search` (embeddings API key 401) imediatamente — afeta todos os agentes.

### 4. Zapier

**Decisão já vigente:** ✅ Removido. `gog` é oficial. CTO reforça que não deve ser reintroduzido.

---

## Arquivos gerados nesta avaliação

- `[F2] memory/outputs/cto/2026-07-20-avaliacao-arquitetural-mission-control-whatsapp.md` — avaliação completa
- `[F2] memory/agents/cto.md` — prompt do agente CTO
- Este registro

---

## Pendências técnicas aprovadas (aguardando Jadielson)

1. ✅ Validação da decisão Mission Control (Build vs. Buy)
2. ✅ Validação do SLA WhatsApp tiers
3. ✅ Autorização para diagnóstico da chave de embeddings (P0)
4. ✅ Autorização para reindexação de agentes (P1)

---

## Fontes

Cofre: `[F2] memory/context/arquitetura/pedido-loh-avaliar-mission-control-backlog-inteligente-2026-07-20.md`, `[F2] memory/projects/mission-control/2026-07-19-prd-mission-control-integrado.md`, `[F2] memory/projects/backlog-inteligente/mission-control-blueprint-mvp-v1-2026-07-20.md`, `[F2] memory/decisions/2026-07-20-remocao-total-zapier-gog-oficial.md`, `MEMORY.md`, `AGENTS.md`, `CONSTITUICAO.md`.