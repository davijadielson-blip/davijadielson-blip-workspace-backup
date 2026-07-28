---
tema: 07 22 remocao total zapier gog oficial
atualizado_em: 2026-07-22
---

# Decisão — Remoção total da Zapier do ecossistema

**Data:** 2026-07-22
**Decisão de:** Jadielson Davi
**Executado por:** Lôh

## Motivo

Jadielson reportou que subagentes e tópicos insistem em usar Zapier, mesmo após solicitação anterior de exclusão. A Zapier estava limitando o ecossistema (créditos insuficientes, interferência nos fluxos). Tudo deve ser feito via `gog` (Google CLI).

## Ações executadas

1. **Gateway config alterado**: todos os 5 MCPs Zapier desabilitados (`enabled: false`):
   - `zapier-1`
   - `zapier-2`
   - `zapier-3`
   - `zapier-youtube`
   - `canva-zapier`

2. **Backup salvo**: `/data/.openclaw/openclaw.json.bak.zapier-removal`

3. **AGENTS.md atualizado**: seção "🚫 REGRA ABSOLUTA — ZAPIER PROIBIDO NO ECOSSISTEMA" reforçada com:
   - Status atual desativado
   - Proibição explícita para agentes atuais e futuros
   - Caminhos oficiais (`gog`, Tavily, navegador)
   - Regra de correção automática se Zapier for citado em instruções

## Próximo passo

Reiniciar gateway para aplicar as mudanças nos MCPs. Aguardando autorização de Jadielson para restart.

## Vigência

Indefinida. Esta decisão só pode ser revertida por Jadielson Davi.