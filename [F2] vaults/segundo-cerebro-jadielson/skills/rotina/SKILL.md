---
tipo: skill
nome: rotina
trigger: "usuário digita 'rotina' ou 'planejar meu dia'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-10
---

# SKILL — rotina (Planejamento do Dia)

> Monta o plano do dia com Top 3 prioritizado, tracker de conteúdo por frente e intenção.
> Ideal para rodar de manhã, após o daily-brief automático das 7h.

---

## Trigger

O usuário digita: `rotina`, `planejar meu dia`, `o que faço hoje`.

---

## Procedimento

### Fase 1 — Contexto do dia

1. Identificar dia da semana e tipo:
   - Seg/Qua/Sex → 🎥 Externo (captações, reuniões, clientes)
   - Ter/Qui/Sáb → 🏢 Agência (edição, conteúdo, organização)
   - Dom → 🗓️ Planejamento / Descanso
2. Verificar fuso: `America/Maceio` (UTC-3)
3. Ler daily-brief do dia se existir: `[F2] memory/sessions/daily-briefs/YYYY-MM-DD.md`

### Fase 2 — Montar Top 3

Prioridade em cascata:
1. 🔴 Deadlines ≤ 3 dias (`[F2] memory/context/deadlines.md`)
2. 🔴 Pendências críticas (`[F2] memory/context/pendencias.md`)
3. 📅 Ação de conteúdo do dia por frente:
   - Câmara: seg/qua/sex → post da linha editorial
   - SINDSS: seg/qua/sex → post; sex → depoimento de servidor
   - Saúde: conforme pauta da semana
   - Lógika: conforme agenda de captação/entrega
4. 🎥 Captação externa se for dia de externo

### Fase 3 — Tracker de conteúdo por frente

Para cada frente ativa, verificar:
- Tem draft pendente de revisão? (`[F2] memory/outputs/`)
- Tem data sazonal chegando nos próximos 5 dias?
- Está no dia de publicação da linha editorial?

### Fase 4 — Entregar plano

```
## Rotina — [dia], [data] — [tipo do dia]

### 🎯 Top 3 de hoje
1. [tarefa crítica ou deadline]
2. [ação de conteúdo prioritária]
3. [ação secundária ou captação]

### 📋 Tracker de conteúdo
| Frente | Status | Ação hoje |
|---|---|---|
| Câmara | [ok/pendente] | [ação] |
| SINDSS | [ok/pendente] | [ação] |
| Saúde | [ok/pendente] | [ação] |
| Lógika | [ok/pendente] | [ação] |

### 💡 Intenção do dia
[1 frase de intenção — gerada com base no contexto]

Bom trabalho, Jadielson.
```

---

## Output esperado

Plano entregue ao usuário. Nenhum arquivo criado — apenas síntese e orientação.

---

## Notas

- Não criar tarefas que não têm base em contexto real do vault
- Dia de planejamento (dom) → sugerir rodada da skill `cerebro` em vez de plano operacional
- Métricas financeiras: omitir por enquanto (dashboard não configurado)
