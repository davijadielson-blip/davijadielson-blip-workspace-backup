---
tema: 07 22 encaminhamento alfred loh
atualizado_em: 2026-07-22
---

# 📨 Encaminhamento para Alfred / Lôh

**Data:** 22/07/2026
**Origem:** Agente IA RADAR (Central Pessoal / ESTUDOS)
**Tipo:** Configuração de ambiente + Remoção de integração

## Solicitações

### 1. 🔑 GOG_KEYRING_PASSWORD — Configurar variável de ambiente
- `gog` v0.21.0 está instalado com 2 contas cadastradas
- Ambas as contas exigem `GOG_KEYRING_PASSWORD` para acessar os tokens OAuth em ambiente headless/script
- Sem isso, agentes e scripts não conseguem usar `gog` para operações no Drive, Gmail ou Calendar
- **Ação necessária:** configurar `GOG_KEYRING_PASSWORD` como env var no gateway

### 2. 🗑️ Remover 3 MCPs Zapier residuais
- Decisão de Jadielson (20/07): Zapier removido, `gog` é oficial
- Mas os 3 MCPs Zapier ainda aparecem como ferramentas ativas:
  - `zapier-1` (Google Drive + Slack — ambos residuais)
  - `zapier-3` (vários apps, incluindo Google Drive)
  - `zapier-youtube` (só Notion)
- **Ação necessária:** remover/desabilitar esses MCPs do gateway

### 3. 📁 IA RADAR — Criar pasta no Drive
- Após `gog` operacional, criar: `"IA RADAR - Novidades IA"` no Drive
- Pode ser na conta `logikacreative.mkt@gmail.com` ou `davijadielson@gmail.com` (a confirmar com Jadielson)

## Contexto
- O IA RADAR (tópico ESTUDOS) vai fazer varreduras semanais de IA
- Os materiais brutos (links, destaques) precisam de uma pasta no Drive para arquivos complementares
- A rota oficial é `gog`, não Zapier

## Prioridade
- #1 e #2: **Alta** — impedem operações básicas com Google
- #3: **Média** — pode aguardar resolução de #1