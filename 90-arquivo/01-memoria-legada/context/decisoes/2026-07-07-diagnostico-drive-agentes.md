---
tipo: diagnostico
data: 2026-07-07
status: pendente
fonte: Lôh
assunto: Agentes não acessando Google Drive pessoal
---

# Diagnóstico — Agentes sem acesso ao Google Drive

## Problema reportado

Jadielson reportou que alguns agentes não estão conseguindo acessar o Drive do email pessoal (davijadielson@gmail.com).

## Diagnóstico

**Causa raiz:** As 3 instâncias do Zapier MCP estão com **créditos/tasks esgotados** (erro 402 Payment Required — "insufficient tasks on account").

### Zapier-1 (conexão principal)
- ✅ Google Drive configurado
- ✅ Gmail configurado
- ❌ **Falhando** — 402 Payment Required

### Zapier-3 (conexão secundária)
- ✅ Google Drive configurado
- ❌ **Falhando** — 402 Payment Required

### Zapier-YouTube
- ✅ YouTube configurado
- ❌ **Falhando** — 402 Payment Required (provavelmente)

## Impacto

- ❌ Nenhum agente consegue ler/escrever no Google Drive via Zapier
- ❌ Nenhum agente consegue acessar Gmail via Zapier
- ❌ Nenhum agente consegue acessar YouTube via Zapier
- ✅ Google Calendar ainda pode estar funcionando (via credenciais OAuth diretas em scripts/)
- ✅ Google Drive pode ser acessado via script `gog` (ferramenta alternativa) — ver `scripts/finalizar-drive-readonly-clara.sh`

## Contas de e-mail envolvidas

1. **davijadielson@gmail.com** — pessoal (principal)
2. **logikacreative.mkt@gmail.com** — Lógika Creative

## Solução

### Opção A — Recarregar Zapier
- Acessar: https://mcp.zapier.com/mcp/servers/30c2bcd6-a635-458d-b2eb-fa2c0cc6a929/config
- Fazer upgrade do plano ou recarregar tasks
- Custo: depende do plano Zapier

### Opção B — Usar `gog` (ferramenta Go)
- Já existe script em: `scripts/finalizar-drive-readonly-clara.sh`
- Suporta autenticação OAuth direta com Drive readonly
- Contas cadastradas: logikacreative.mkt@gmail.com e davijadielson@gmail.com
- Vantagem: não depende de Zapier
- Desvantagem: acesso readonly, não tem MCP integrado

### Opção C — Credenciais OAuth diretas via Google API
- Já existe setup em `scripts/setup/google-calendar-auth.py`
- Pode ser estendido para Drive
- Requer configurar escopos adicionais no Google Cloud Console

## Próximo passo
- [ ] Jadielson decidir entre recarregar Zapier ou migrar para autenticação direta
- [ ] Se optar por autenticação direta, configurar Google Drive API + Service Account

## Fontes
- Cofre: `scripts/finalizar-drive-readonly-clara.sh`, `scripts/setup/google-calendar-auth.py`
- Teste real: erro 402 Payment Required em todos os 3 Zapier MCPs