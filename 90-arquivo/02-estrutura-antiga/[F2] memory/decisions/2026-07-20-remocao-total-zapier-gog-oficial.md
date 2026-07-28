---
tema: 07 20 remocao total zapier gog oficial
atualizado_em: 2026-07-22
---

# 🔴 Decisão: Remoção Total do Zapier — `gog` é o Caminho Oficial para Google

**Data da decisão:** 20/07/2026
**Reforçado em:** 22/07/2026 (Jadielson)
**Status:** ✅ Decidido — Pendente de execução final

## Decisão

O Zapier MCP **deve ser removido totalmente** do ecossistema. Toda integração Google passa a ser via **`gog`** (CLI oficial).

## Motivos

- Zapier estava atrapalhando (créditos expirados, limitações de plano gratuito)
- `gog` é mais direto, sem camadas intermediárias
- Decisão de Jadielson: Google via `gog` apenas

## Ações já executadas

- ✅ `gog` instalado (v0.21.0) com contas:
  - `davijadielson@gmail.com` (pessoal)
  - `logikacreative.mkt@gmail.com` (Lógika)
- ✅ Ações Google removidas dos Zapiers (data original 14/07)
- ✅ MEMORY.md atualizado com regras

## Executado em 22/07

- ✅ **MCPs Zapier desabilitados no gateway** (zapier-1, zapier-2, zapier-3, zapier-youtube, canva-zapier)
- ✅ **AGENTS.md atualizado** com regra absoluta e tabela de caminhos oficiais
- ✅ **Decisão reforçada**: Jadielson confirmou — Zapier proibido em todo o ecossistema

## Pendências

1. **🔴 GOG_KEYRING_PASSWORD** — configurar variável de ambiente no gateway
2. **🔴 IA RADAR** — criar pasta "IA RADAR - Novidades IA" no Drive (pode ser via gog)

## Alternativas oficiais pós-remoção

| Serviço | Alternativa |
|---------|-------------|
| Google Drive | `gog drive` |
| Gmail | `gog gmail` |
| Google Calendar | `gog calendar` / scripts Cofre |
| Google Sheets | `gog` / scripts OAuth |
| Web geral | `tavily_search`, `tavily_extract`, `web_search` |
