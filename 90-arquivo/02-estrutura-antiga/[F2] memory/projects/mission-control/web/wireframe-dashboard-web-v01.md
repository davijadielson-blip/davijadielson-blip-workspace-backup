---
tema: wireframe dashboard web v01
atualizado_em: 2026-07-22
---

# Wireframe — Dashboard Web Mission Control v0.1

**Status:** aprovado como direção inicial — web primeiro  
**Data:** 2026-07-19 23:48 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh

## Decisão base

Jadielson definiu:

- Interface: **web primeiro**.
- CRM da Lógika: **Notion**.
- Estudo principal da semana: **Comunidade 1P**.
- Dashboard visual: **começar pelo web**.

---

## 1. Objetivo do dashboard web

Criar uma interface visual simples para enxergar:

- Top 3 da semana;
- cards em andamento;
- pendências aguardando Jadielson;
- status das frentes principais;
- produção de conteúdo;
- agentes responsáveis;
- links para arquivos do Cofre.

---

## 2. Stack recomendada

### MVP web recomendado

- **Frontend:** Next.js + Tailwind.
- **Dados no início:** arquivos Markdown estruturados do Cofre, exportados/convertidos depois.
- **CRM:** Notion para Leads/Clientes da Lógika.
- **Deploy futuro:** Vercel ou Cloudflare Pages.

### Regra importante

No Cofre só entram arquivos `.md`. Código, imagens, builds, JSON, HTML ou assets do app devem ser criados fora do Cofre ou em repositório/app apropriado, mantendo o Cofre como fonte documental.

---

## 3. Telas do MVP

### Tela 1 — Cockpit Geral

Componentes:

- saudação/status;
- Top 3 da semana;
- cards em andamento;
- cards aguardando Jadielson;
- alerta de risco;
- botão/link para placar semanal.

### Tela 2 — Lógika Creative

Componentes:

- pendências críticas;
- CRM Notion: leads/clientes, quando integrado;
- calendário editorial;
- proposta comercial;
- KPIs financeiros mínimos.

### Tela 3 — Frentes Institucionais

Abas:

- Saúde São Sebastião;
- Câmara Municipal;
- SINDSS.

Componentes:

- planejamento vs publicado;
- checklist de cobertura;
- calendário semanal;
- status de aprovação/publicação.

### Tela 4 — Estudos e Produtividade

Componentes:

- estudo principal: Comunidade 1P;
- objetivo da semana;
- método ativo;
- aplicação prática;
- revisão programada;
- checklist pessoal leve.

### Tela 5 — Agentes

Componentes:

- Lôh;
- Jarvis;
- Alfred;
- C-Level Squad;
- Central Pessoal;
- quando acionar cada um.

### Tela 6 — Decisões e Memória

Componentes:

- últimas decisões;
- próximos passos;
- links do Cofre;
- changelog do Mission Control.

---

## 4. Layout textual

```text
┌──────────────────────────────────────────────┐
│ Mission Control — Jadielson / Lôh            │
│ Semana: 20 a 26 jul | Status: Operacional    │
├──────────────────────────────────────────────┤
│ TOP 3                                        │
│ 1. Lógika Creative                           │
│ 2. Saúde / Câmara / SINDSS                   │
│ 3. Comunidade 1P + Produtividade             │
├──────────────────────────────────────────────┤
│ EM ANDAMENTO                                 │
│ [LOG-001] Placar único Lógika                │
│ [SAU-001] Rotina diária Saúde                │
│ [MC-001] Placar semanal                      │
├──────────────────────────────────────────────┤
│ AGUARDANDO JADIELSON                         │
│ [CRM] Notion — definir base/campos           │
│ [WEB] validar wireframe                      │
├──────────────────────────────────────────────┤
│ LINKS RÁPIDOS                                │
│ Placar semanal | Backlog | Artefatos | PRD   │
└──────────────────────────────────────────────┘
```

---

## 5. Dados mínimos para protótipo

| Entidade | Campos |
|---|---|
| Card | id, título, frente, status, prioridade, responsável, próxima ação, fonte, critério de pronto |
| Frente | nome, status, risco, objetivo, fonte |
| Decisão | data, decisão, fonte, impacto |
| Estudo | nome, objetivo, tempo, método ativo, aplicação, revisão |
| Publicação | frente, data, pauta, status, link/observação |

---

## 6. Próximas etapas técnicas

1. Validar este wireframe.
2. Definir local correto do código/app fora do Cofre, respeitando a Constituição.
3. Criar protótipo Next.js estático.
4. Alimentar protótipo inicialmente por dados manuais/exportados.
5. Integrar Notion CRM da Lógika.
6. Depois integrar rotinas/atualizações automáticas.
