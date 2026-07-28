---
tema: README
atualizado_em: 2026-07-22
---

# 📋 Editais Culturais — Análise e Acompanhamento

## Status
🟢 Ativo — 2026-07-22

## Responsável
Jack Lemley (Agente Temático da Central Pessoal)

## Objetivo
Analisar editais culturais, extrair informações essenciais, classificar aderência e apoiar decisões de inscrição.

## Fluxo de trabalho
1. Jadielson envia edital (link, PDF, texto) no tópico Telegram
2. Agente analisa e extrai: órgão, prazo, valor, área, requisitos, documentação
3. Classifica aderência (🔴 🟡 🟢) com justificativa
4. Registra análise no Cofre com nome padronizado
5. Sugere próximos passos

## 📁 Repositório Central no Google Drive
**Link:** [EDITAIS CULTURAIS - Google Drive](https://drive.google.com/drive/folders/1JPl3QgSAzaspDgfmawOsiGrOcTcFuP9j)

Todos os editais (atuais e futuros) serão armazenados nesta pasta. O agente deve:
- ✅ Verificar periodicamente a pasta em busca de novos arquivos
- ✅ Analisar cada edital encontrado (PDF, link, DOCX)
- ✅ Manter este README atualizado com o status de cada um

## 🔍 Monitoramento
- **Frequência:** Diário (via cron) para verificar novos arquivos na pasta do Drive
- **Método:** Browser (perfil logado) ou Zapier/Drive API quando tarefas disponíveis
- **Backup:** Jadielson pode também enviar links diretamente neste tópico Telegram

## Editais analisados

| Edital | Órgão | Prazo | Valor | Aderência | Status |
|---|---|---|---|---|---|
| FOMENTO 002/2026 — Ações Culturais PNAB | Porto Real do Colégio/AL | 29/07/2026 | R$ 47.927,22 (total) | 🟡 Média | ⏳ Aguardando confirmação_

## Padrão de salvamento
`edital-NOME-DATA.md` em `[F3] PROJETOS/03_PROJETOS/01_Autorais_Culturais/Editais Culturais/`