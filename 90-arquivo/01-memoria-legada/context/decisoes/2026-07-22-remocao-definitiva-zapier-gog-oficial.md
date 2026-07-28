---
tipo: decisao
data: 2026-07-22
status: implementado
fonte: Jadielson → Alfred (Central Pessoal)
assunto: Remoção definitiva de todas as MCPs Zapier do ecossistema
---

# Decisão — Remoção definitiva do Zapier + instrução obrigatória para todos os agentes

## Contexto

Jadielson reportou que subagentes e tópicos continuam tentando usar Zapier, mesmo após a migração para GOG (Google OAuth direto via CLI). As MCPs estavam apenas desabilitadas (`enabled: false`), mas ainda presentes no `openclaw.json`, fazendo com que os agentes as "enxergassem" como disponíveis.

## Decisão

✅ **Remover COMPLETAMENTE** todas as entradas Zapier do gateway config (não apenas desabilitar)
✅ **Atualizar system prompt** do agente `main` com proibição explícita de Zapier
✅ **Atualizar AGENTS.md** com instrução reforçada para agentes atuais e futuros
✅ **Registrar decisão** para propagação no ecossistema

## Ações executadas

1. **Backup** salvo em `/data/.openclaw/openclaw.json.bak.zapier-removal-v2`
2. **MCPs removidos do config:**
   - ~~zapier-1~~ 🗑️ removido
   - ~~zapier-2~~ 🗑️ removido
   - ~~zapier-3~~ 🗑️ removido
   - ~~zapier-youtube~~ 🗑️ removido
   - ~~canva-zapier~~ 🗑️ removido
3. **System prompt do agente `main`** atualizado com artigos 11-15 proibindo Zapier
4. **AGENTS.md** — Seção "REGRA ABSOLUTA — ZAPIER PROIBIDO" reforçada
5. **Ata de decisão** salva neste arquivo

## Caminhos oficiais (NUNCA Zapier)

| Serviço | Como acessar |
|---------|-------------|
| Google Drive | `gog drive` (CLI via terminal) |
| Google Calendar | `gog calendar` (CLI via terminal) |
| Gmail | `gog gmail` (CLI via terminal) — somente leitura |
| Google Docs/Sheets | `gog` (CLI via terminal) |
| Web/Fontes externas | `tavily_search`, `tavily_extract`, `web_search` |
| YouTube | Navegador ou pesquisa Tavily |
| Canva | Navegador (canva.com) |

## Regra para todos os agentes (atuais e futuros)

> 🔴 **ZAPIER ESTÁ COMPLETAMENTE PROIBIDO NO ECOSSISTEMA.**
> NENHUM agente, subagente, tópico, skill, cron, automação ou fluxo pode:
> - Usar, chamar, executar ou depender de qualquer ferramenta Zapier
> - Habilitar, reprovisionar, descobrir ações ou auto-provisionar Zapier
> - Mencionar Zapier como alternativa viável
> - Criar skills, scripts ou automações que dependam de Zapier
>
> ✅ Tudo é feito via GOG (Google OAuth direto via terminal/CLI).
>
> Se um briefing, script, roteiro, demanda ou instrução citar Zapier, considere **falha de procedimento** e corrija imediatamente para o caminho GOG/fonte direta.

## Próximos passos

- [ ] Reiniciar gateway para aplicar alterações
- [ ] Verificar se agents subagentes (topicos) estão operando sem Zapier
- [ ] Se novos agentes forem criados, garantir que herdem esta instrução via AGENTS.md