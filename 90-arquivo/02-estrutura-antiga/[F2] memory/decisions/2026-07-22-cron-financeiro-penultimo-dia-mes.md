---
tema: 07 22 cron financeiro penultimo dia mes
atualizado_em: 2026-07-22
---

# Decisão — Cron mensal financeiro no penúltimo dia do mês

**Data:** 2026-07-22
**Decisor:** Jadielson Davi
**Status:** vigente

## Contexto
Jadielson solicitou que os lembretes financeiros mensais (pessoal e empresa) passassem do último para o penúltimo dia do mês, pois no último dia a rotina é de pagamentos e fechamento.

## Decisões

### 1. Warren (Finanças Pessoais) — Atualizado
- **Cron existente** (`55801eae`) reativado e ajustado
- **Agente:** my-finance (Warren)
- **Agenda:** Penúltimo dia do mês, 08:00 BRT
- **Expressão cron:** `0 8 27-30 * *` (o agente valida se é o penúltimo real)
- **Entrega:** Tópico FINANCEIRO da Central Pessoal (chat -1003740871403, thread 12)
- **Conteúdo:** Relatório de contas pessoais + mensagem copiável para a esposa

### 2. CFO (Finanças LÓGIKA/Empresa) — Novo
- **Cron criado** (`2e1a22a8`) 
- **Agente:** cfo (CFO)
- **Agenda:** Penúltimo dia do mês, 08:00 BRT
- **Expressão cron:** `0 8 27-30 * *` (o agente valida se é o penúltimo real)
- **Entrega:** Tópico CFO - Finanças & Caixa (chat -1003645702069, thread 1466)
- **Conteúdo:** Relatório financeiro da LÓGIKA com contas a pagar no último dia

### Regra de validação (ambos)
Ambos os crons rodam nos dias 27-30, mas cada agente verifica se HOJE é o penúltimo dia REAL do mês antes de gerar relatório. Isso cobre meses de 28, 29, 30 e 31 dias.

## ⚠️ Alerta técnico
Ambos os crons usam `sessionTarget: "isolated"` e podem sofrer do mesmo problema de autenticação que afetou os resumos diários (falta de chave API no perfil do agente isolado + créditos OpenRouter baixos). Jadielson ciente.