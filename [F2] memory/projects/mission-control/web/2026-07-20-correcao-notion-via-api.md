# Correção — Notion via API, não Zapier

**Data:** 2026-07-20 00:26 UTC  
**Informado por:** Jadielson Davi  
**Registrado por:** Lôh

## Correção

Jadielson informou: “o notion ta via api”.

## Impacto

A integração real do CRM Notion da Lógika não deve depender do Zapier. O caminho correto passa a ser **Notion API direta**.

## Ajuste de direção

Próxima etapa técnica do Mission Control:

1. Implementar cliente Notion API direto no app/serviço.
2. Usar variáveis de ambiente para token e database id.
3. Nunca expor token no frontend.
4. Criar rota server-side/API route para consultar CRM.
5. Manter no painel apenas dados resumidos: nome, status, prioridade, próxima ação.

## Variáveis esperadas

- `NOTION_TOKEN`
- `NOTION_LOGIKA_CRM_DATABASE_ID`

## Observação

O registro anterior mencionava Zapier porque as ações Notion estavam disponíveis, mas o caminho correto foi corrigido por Jadielson para API direta.
