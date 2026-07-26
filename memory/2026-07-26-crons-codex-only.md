---
tema: crons usando apenas Codex
conteudo: registro/configuração de crons com política Codex-only
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança, operações e conteúdo
cliente: Jadielson Davi
tipo: configuração
prioridade: média
atualizado_em: 2026-07-26
usar_quando: consultar histórico ou contexto relacionado a crons usando apenas Codex
nao_usar_quando: substituir decisões finais em 00-central/decisoes.md
---

# 2026-07-26 — Crons travados em Codex-only

**Solicitante:** Jadielson Davi  
**Mensagem:** “Pode colocar os cron para rodarem obrigatoriamente em CODEX”  
**Objetivo:** impedir novo consumo automático de créditos OpenRouter por jobs agendados.

## Ação aplicada

Todos os **9 crons ativos** com `payload.kind = agentTurn` foram atualizados para execução obrigatória em Codex-only:

```json
"model": "openai-codex/gpt-5.5",
"fallbacks": []
```

## Crons ativos atualizados

1. `eac72b16-9b61-4d5c-bd3c-d02e488fab2e` — `limpeza-diaria-cache`
2. `47a57e6e-ff54-4881-bb08-17d95e23d20c` — `backup-workspace-github-3h`
3. `888d851b-658e-48b1-9acd-45f5d248292e` — `LÔH — Resumo geral de HOJE com links (06h)`
4. `4cf67e57-3648-46fe-890c-be88abeab892` — `LÔH — Resumo geral de AMANHÃ (21h)`
5. `57dedc40-9e35-4a97-9f3b-dce40df333fe` — `IA RADAR — Varredura Semanal`
6. `2e1a22a8-f04e-4d10-8742-8655047c2c34` — `CFO — Relatório mensal LÓGIKA`
7. `55801eae-7ea5-4628-9382-d7c1a0055aaf` — `WARREN — Relatório mensal de contas`
8. `d75daf99-f4f1-468d-b0d4-b9d3a6885a03` — `Lembrete Webinar LPG/LAB - Dia 1`
9. `ad058647-e7e5-4b2a-aaa6-fe138d61bc91` — `briefing-estrategico-semanal`

## Crons desativados com OpenRouter explícito também saneados

Para evitar surpresa caso sejam reativados no futuro, quatro jobs desativados que tinham modelo OpenRouter explícito foram alterados para Codex-only:

1. `2b05d3c0-8d7c-417b-a642-3e6c3c2a8747` — `Clara - acompanhamento skills G4`
2. `b06d57db-36d9-4d6b-8c4c-7ace966805ed` — `Clara — Reporte de Atrasos`
3. `d17bfe69-7b52-44f5-a9bd-20e62e0f0470` — `Clara — Reporte Matinal`
4. `e900c3d9-6ce4-4921-94bc-d096a7a2a94c` — `jarvis-revisao-inbox-logika-seg-sab`

## Política resultante

- Crons ativos não usam OpenRouter como fallback.
- Se Codex falhar, expirar OAuth ou bater limite, o cron deve falhar seguro em vez de gastar OpenRouter.
- OpenRouter permanece disponível apenas na configuração geral/manual dos agentes, não nos crons ativos.

## Validação

`cron list` confirmou que os 9 jobs ativos `agentTurn` estão com:

```json
"model": "openai-codex/gpt-5.5",
"fallbacks": []
```

Fonte: Cofre (`CONSTITUICAO.md`, auditoria OpenRouter 2026-07-26), `cron list`, `cron update`.
