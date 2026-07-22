---
tema: 07 20 avaliacao arquitetural mission control whatsapp
atualizado_em: 2026-07-22
---

# Avaliação Técnica CTO — Julho 2026

**CTO:** 👤 CTO — Chief Technology Officer  
**Data:** 2026-07-20  
**Reporta a:** Jadielson via LÔH + Alex (TI/software)  
**Status:** ✅ Análise concluída

---

## Sumário

1. [Mission Control Backlog Inteligente — Avaliação Arquitetural](#1-mission-control-backlog-inteligente--avaliação-arquitetural)
2. [WhatsApp Inteligente — Base Técnica](#2-whatsapp-inteligente--base-técnica)
3. [Dívida Técnica — Mapeamento e Priorização](#3-dívida-técnica--mapeamento-e-priorização)
4. [Recomendações Finais e Próximos Passos](#4-recomendações-finais-e-próximos-passos)

---

## 1. Mission Control Backlog Inteligente — Avaliação Arquitetural

### 1.1 Contexto da solicitação

**Origem:** Jadielson, via tópico ESTUDOS > Backlog Inteligente  
**Documento base:** `[F2] memory/context/arquitetura/pedido-loh-avaliar-mission-control-backlog-inteligente-2026-07-20.md`  
**Blueprint:** `[F2] memory/projects/backlog-inteligente/mission-control-blueprint-mvp-v1-2026-07-20.md`  
**PRD:** `[F2] memory/projects/mission-control/2026-07-19-prd-mission-control-integrado.md`  
**Decisão macro:** Opção 5 — Tudo Integrado (Jadielson, 19/07/2026)

**Pergunta-chave:** É viável criar um Mission Control / aplicativo que integre xTiles, Cofre, Google Calendar, Backlog Inteligente e IA?

---

### 1.2 Análise Build vs. Buy

| Critério | Buy (xTiles como plataforma) | Build (app próprio) |
|---|---|---|
| **Velocidade de MVP** | 🟢 Imediato (horas) | 🔴 2-4 semanas (mínimo) |
| **Custo** | 🟢 Já possui conta | 🔴 R$ 5-15k (dev) |
| **Manutenção** | 🟢 Zero | 🔴 Contínua (deploy, bugs, updates) |
| **Personalização** | 🟡 Boa, mas limitada ao que o xTiles permite | 🟢 Total |
| **Integração Cofre** | 🟡 Manual/export; API limitada | 🟢 Nativa (MD → banco) |
| **IA incorporada** | 🔴 Não tem motor de IA nativo | 🟢 Pode embarcar |
| **Autenticação/Segurança** | 🟢 Já tem login xTiles | 🔴 Precisa construir |
| **Parede-d'água** | 🟡 Precisa de boards separados | 🟢 Controle granular |
| **Offline** | 🟢 App mobile xTiles | 🔴 Depende da stack |

**Veredito CTO:** **Buy primeiro, Build depois se validar.**

---

### 1.3 Arquitetura Recomendada (Faseada)

#### Fase 0 — Validação (semanas 1-2) 🟢 JÁ AUTORIZADO POR JADIELSON

```text
xTiles (cockpit humano)
    │
    ├── Boards por área (PESSOAL, PROFISSIONAL, TRABALHO, PROJETOS)
    ├── Templates .md no Cofre espelhados
    └── Captura manual + prints → Agentes → Cofre
```

**Risco:** Duplicação de alimentação. Mitigação: usar regra "xTiles visualiza; Cofre armazena". Captura pode ser no xTiles, mas a decisão/contexto relevante é extraída e salva no Cofre.

#### Fase 1 — Integração Cofre ↔ xTiles (semanas 3-4)

```text
[Cofre] templates .md ──────────────→ [Agentes Lôh] ──→ [xTiles]
                              (copia estruturada via agente)

Fluxo:
1. Templates .md no Cofre (já existem: tarefa, projeto, revisão semanal)
2. Agente lê Cofre → extrai tarefas/projetos relevantes
3. Agente popula xTiles via navegador (browser tool) → automação controlada
4. Jadielson valida/ajusta no xTiles
```

**Stack:** `browser` tool + templates `.md` + agentes Cofre  
**Sem Zapier.** ✅

#### Fase 2 — Ponte Calendar (semanas 3-4, paralelo)

```text
[Google Calendar] ←── gog/scripts ──→ [Cofre]
                                       (calendario.md)

Fluxo:
1. Compromissos/blocos no Google Calendar
2. `gog_calendar` extrai eventos → salva como `calendario.md`
3. Agente usa calendario.md para montar ordem do dia
4. Jadielson ajusta blocos no Calendar → gog puxa atualizações
```

**Stack:** `gog_calendar` + scripts Cofre  
**Sem Zapier.** ✅

#### Fase 3 — Arquitetura de App Próprio (se validado, meses 2-3)

```text
┌─────────────────────────────────────────────────────┐
│                   Frontend                          │
│  Next.js 14+ / Tailwind / shadcn/ui / React Query   │
│  Deploy: Vercel (SSR) ou Cloudflare Pages (SSG)     │
└──────────────────────┬──────────────────────────────┘
                       │ API REST / GraphQL
┌──────────────────────▼──────────────────────────────┐
│                   Backend                           │
│  Next.js API routes ou Fastify standalone           │
│  Autenticação: NextAuth.js (Google OAuth + creds)   │
│  IA: LLM API (GPT-5.5 ou DeepSeek) via route segura │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│               Data Layer                            │
│  Supabase (PostgreSQL + Realtime + Auth)            │
│    ├── Tabela: tasks (projeto, status, hierarquia)  │
│    ├── Tabela: projects (area, responsavel, prazo)  │
│    ├── Tabela: decisions (decisao, contexto, fonte) │
│    ├── Tabela: areas (pessoa, profissional, etc)    │
│    └── Tabela: calendar_events (importadas do gog)  │
│                                                     │
│  Cofre (.md) ←─── sync job ────→ Supabase           │
│  Google Calendar ←── gog ────→ Supabase             │
└─────────────────────────────────────────────────────┘
```

**Stack recomendada (se for construir):**

| Camada | Tecnologia | Justificativa |
|---|---|---|
| Frontend | Next.js 14+ / Tailwind / shadcn/ui | SSR, ecosystem maduro, fácil deploy |
| Estado | React Query + Zustand | Cache server-side + estado local leve |
| Database | Supabase (PostgreSQL) | Realtime, Auth, Storage, hospedado |
| ORM | Drizzle ou Prisma | Type-safe, migrations |
| Auth | NextAuth.js + Google OAuth | SSO via Google já usado |
| IA | API routes seguras → GPT-5.5 | Motor de IA para ordem do dia, fatiamento |
| Deploy | Vercel (front) + Supabase (db) | Zero-ops, escalável |
| Sincronia | Script cron (Cofre → Supabase) | Cofre continua fonte de verdade |

**Custo estimado (app próprio):**

| Item | Custo mensal |
|---|---|
| Vercel Pro | $20/mês |
| Supabase Pro | $25/mês |
| API LLM (uso moderado) | $10-30/mês |
| Domínio | ~R$ 40/ano |
| **Total** | **~$55-75/mês + R$ 40/ano** |

Tempo de desenvolvimento MVP básico (sem IA avançada): **3-4 semanas** full-stack.  
Com motor de IA integrado: **6-8 semanas**.

---

### 1.4 Análise de Riscos Técnicos

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| **Duplicação de alimentação** (xTiles + Cofre) | 🔴 Alta | 🟡 Médio | Estabelecer direção clara: xTiles visualiza, Cofre guarda. Captura pode ser direto no xTiles, mas agente extrai pro Cofre |
| **API xTiles inexistente ou limitada** | 🟡 Média | 🔴 Alto | Validar docs xTiles antes de depender. Alternativa: export/import CSV/MD manual |
| **Vazamento de dados pessoais** | 🟢 Baixa | 🔴 Alto | Parede-d'água: boards separados por área no xTiles; no app, RBAC por scope |
| **App próprio não ser usado** | 🟡 Média | 🔴 Alto | Validar com xTiles primeiro por 7-14 dias. Só construir se houver uso consistente |
| **Escopo crescer sem controle** | 🔴 Alta | 🟡 Médio | PRD com milestones fixos. Toda feature nova → próxima fase |
| **Dependência de API Google (gog)** | 🟢 Baixa | 🟡 Médio | Fallback: export manual .ics → script de parse |

---

### 1.5 Limites do xTiles (identificados)

1. **Sem API pública documentada** — automação via browser é frágil e quebra com updates
2. **Sem motor de IA nativo** — não faz fatiamento, diagnóstico de trava ou ordem do dia
3. **Sem RBAC granular** — parede-d'água depende de boards separados
4. **Export limitado** — CSV/MD possíveis, mas sem delta/sincronia incremental
5. **Offline limitado** — app mobile existe, mas sync pode ser inconsistente

**Veredito:** xTiles é ótimo para **protótipo visual e validação de hábito**. Não é plataforma definitiva para o Mission Control Integrado completo com IA.

---

### 1.6 O que testar primeiro (7-14 dias de validação)

1. **Jadielson usa xTiles como cockpit visual** durante uma semana
2. **Captura no xTiles** → agente extrai decisões/contexto → salva no Cofre
3. **Ordem do dia gerada por IA** no Cofre → Jadielson valida no xTiles
4. **Revisão semanal** usando o template `.md` → ajustes
5. **Google Calendar** mantém blocos → `gog` sincroniza → agente usa

**Critérios de sucesso do piloto:**
- Jadielson usou xTiles por ≥5 dos 7 dias
- ≥10 tarefas capturadas e processadas
- Pelo menos 1 revisão semanal completa
- Sensação de clareza maior que antes
- **Não** sensação de trabalho duplicado

---

## 2. WhatsApp Inteligente — Base Técnica

### 2.1 Situação Atual

WhatsApp é o principal canal de comunicação da Lógika Creative com clientes. Atualmente:

- **Recebimento:** automático via canal configurado
- **Resposta:** Jadielson aprova sugestões antes de enviar
- **Agentes envolvidos:** CRO (atendimento comercial), CCO (conteúdo criativo), operacionais por frente
- **SLA:** não formalizado

### 2.2 Arquitetura Proposta

```text
[WhatsApp] ←── Webhook/Mensageria ──→ [Cofre/Agente]
    │                                       │
    ├── Mensagem recebida                   ├── Analisa contexto (Cofre + histórico)
    ├── Cliente/Lead identificado           ├── Prepara minuta de resposta
    └── Histórico salvo em .md             └── Apresenta para Jadielson aprovar
                                               │
                                          Jadielson aprova? ──sim──→ Envia resposta
                                               │não
                                               └── Ajusta + re-apresenta
```

### 2.3 Pilares Técnicos

| Pilar | Status | Ação necessária |
|---|---|---|
| **Identificação de cliente** | 🟡 Parcial | Criar lookup rápido: número → lead/projeto no CRM Notion/Cofre |
| **Contexto de conversa** | 🟡 Parcial | Histórico salvo em sessões .md, mas sem indexação por número |
| **Minuta inteligente** | 🟢 Possível | GPT-5.5 já consegue sugerir respostas com base no contexto |
| **SLA por tier** | 🔴 Não existe | Precisa definir tier de cliente, tempo de resposta e escalonamento |
| **Escalabilidade** | 🟡 OK para volume atual | Com crescimento, precisa de fila/multi-atendimento |
| **LGPD** | 🔴 Não auditado | CIO precisa avaliar: retenção de mensagens, direito de exclusão |

### 2.4 SLA Recomendado

| Tier | Cliente | Tempo resposta | Cobertura | Quem responde |
|---|---|---|---|---|
| **Diamante** | Contratos mensais/projetos grandes | ≤2h úteis | Seg-Sex 8-18h | Jadielson + CRO |
| **Ouro** | Projetos pontuais recorrentes | ≤4h úteis | Seg-Sex 8-18h | CRO + sugestão CTO |
| **Prata** | Leads em prospecção | ≤8h úteis | Seg-Sex 8-18h | CRO com minuta |
| **Bronze** | Consultas gerais | ≤24h úteis | Seg-Sex | Automatizado + Jadielson valida |

### 2.5 O que precisa ser construído

1. **Lookup de cliente por número** — base no CRM Notion ou Cofre
2. **Histórico indexado por número** — cada interação vira `memory/atendimentos/{numero}/{data}.md`
3. **Template de minuta por tipo de demanda** — orçamento, reclamação, dúvida, pedido
4. **Dashboard de SLA** — planilha Google Sheets via `gog` + script de monitoramento
5. **Protocolo de escalonamento** — se não respondido em X horas, aciona Jadielson

---

## 3. Dívida Técnica — Mapeamento e Priorização

### 3.1 Inventário de Dívida Técnica Atual

| # | Item | Área | Gravidade | Esforço | Prioridade |
|---|---|---|---|---|---|
| **DT-01** | `memory_search` falhando (401 embeddings API key) | Infra Cofre | 🔴 Crítico | 🟡 Médio | **P0 — URGENTE** |
| **DT-02** | Busca semântica indisponível para agentes | Infra Cofre | 🔴 Crítico | 🟡 Médio | **P0 — URGENTE** |
| **DT-03** | Base F2 SAÚDE (288 arquivos) sem curadoria final humana | Conteúdo | 🟡 Moderado | 🔴 Alto | P2 |
| **DT-04** | Duplicatas na estrutura F1 SAÚDE (12 prováveis) | Conteúdo | 🟡 Moderado | 🟡 Médio | P2 |
| **DT-05** | Agentes sem reindexação no SQLite (0 chunks muitos) | Infra Agentes | 🟡 Moderado | 🟢 Baixo | P1 |
| **DT-06** | Sem SLA formalizado para WhatsApp | Operacional | 🟡 Moderado | 🟢 Baixo | P1 |
| **DT-07** | Sem LGPD auditada (CIO depende) | Compliance | 🟡 Moderado | 🟡 Médio | P2 |
| **DT-08** | xTiles ↔ Cofre sem sync automatizado | Arquitetura | 🟢 Leve | 🔴 Alto | P3 |
| **DT-09** | Sem documentação de stack/ferramentas usadas | Conhecimento | 🟢 Leve | 🟢 Baixo | P3 |
| **DT-10** | Sem testes/deploy pipeline para qualquer código | DevOps | 🟡 Moderado | 🔴 Alto | P3 |
| **DT-11** | Vault secundário `[F2] vaults/` com 4410 arquivos (clone GitHub) sem sincronia clara | Infra Cofre | 🟡 Moderado | 🟡 Médio | P2 |
| **DT-12** | AGENTS.md e MAPA.md crescendo sem revisão periódica | Documentação | 🟢 Leve | 🟢 Baixo | P3 |

### 3.2 Prioridades de Ação

#### 🔴 P0 — Esta semana (dias 1-3)

| ID | Ação | Responsável |
|---|---|---|
| **DT-01/02** | Diagnosticar e corrigir chave de API de embeddings. Verificar se é chave expirada, revogada ou configurada incorretamente. Alternativa: reprovisionar a chave no provedor de embeddings. | CTO + Alex |

**Impacto:** `memory_search` parou de funcionar em 20/07. Agentes estão sem busca semântica. Fallback direto funciona, mas é mais lento e menos preciso. Correção é prioridade máxima.

#### 🟡 P1 — Este mês (dias 4-14)

| ID | Ação | Responsável |
|---|---|---|
| **DT-05** | Reindexar agentes principais no SQLite para busca semântica funcional | CTO + Lôh |
| **DT-06** | Formalizar SLA do WhatsApp + criar dashboard de monitoramento (+ planilha) | CTO + CRO + COO |

#### 🟢 P2 — Próximo mês

| ID | Ação |
|---|---|
| **DT-03** | Curadoria humana da base SAÚDE F2 |
| **DT-04** | Unificação de duplicatas SAÚDE F1 |
| **DT-07** | Auditoria LGPD (CIO) |
| **DT-11** | Definir sync vaults/ ↔ GitHub |

---

## 4. Recomendações Finais e Próximos Passos

### 4.1 Resumo das Decisões Recomendadas

| Decisão | Recomendação CTO |
|---|---|
| **Mission Control: Build vs Buy?** | **Buy (xTiles) primeiro, validar por 7-14 dias, construir app próprio depois se validado** |
| **Stack para app próprio?** | Next.js + Supabase + Tailwind + Vercel — $55-75/mês |
| **WhatsApp inteligente?** | Criar lookup + SLA + histórico indexado; não automatizar resposta sem aprovação |
| **Dívida técnica P0?** | Corrigir embeddings API key imediatamente |
| **Zapier?** | ✅ Já removido. `gog` é o caminho oficial |

### 4.2 Próximos Passos Imediatos (para aprovação de Jadielson)

1. **🟢 Corrigir DT-01/02 (P0):** Diagnosticar chave de embeddings — CTO + Alex, hoje
2. **🟢 Validar piloto xTiles:** Jadielson usa xTiles por 7 dias como cockpit visual; CTO acompanha sem construir nada
3. **🟢 SLA WhatsApp:** CTO + CRO + COO definem tiers e formalizam em documento
4. **🟡 Reindexação de agentes (P1):** Após correção de embeddings, reindexar agentes sem chunks

### 4.3 Não Fazer Agora

- ❌ Não construir app próprio antes de validar xTiles
- ❌ Não automatizar WhatsApp sem SLA e LGPD
- ❌ Não mexer em F1 (pastas autorais de Jadielson)
- ❌ Não criar novas integrações que dependam de Zapier
- ❌ Não gastar tempo em DT-08/09/10/12 (P3) antes de P0/P1

---

## Nota Técnica Final

Esta avaliação foi produzida com base no Cofre (`CONSTITUICAO.md`, `AGENTS.md`, `MAPA.md`, `MEMORY.md`, pedido em `[F2] memory/context/arquitetura/`, PRD em `[F2] memory/projects/mission-control/`, blueprint em `[F2] memory/projects/backlog-inteligente/`, decisões em `[F2] memory/decisions/`).

**Fonte:** Cofre (arquivos de contexto, decisões, projetos e arquitetura); Tavily não foi necessário para esta avaliação pois toda a informação necessária estava no Cofre.

---

*CTO — Lógika Creative*  
*Reporta a Jadielson via LÔH + Alex (TI/software)*
