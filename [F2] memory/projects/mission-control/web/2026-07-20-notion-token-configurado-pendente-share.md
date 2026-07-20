# Notion API — token configurado e pendência de compartilhamento

**Data:** 2026-07-20 01:09 UTC  
**Contexto:** Mission Control Web / CRM Lógika

## O que foi feito

O token Notion foi configurado no app fora do Cofre:

`/data/.openclaw/mission-control-next/.env.local`

Também foi configurado:

`NOTION_LOGIKA_CRM_DATABASE_ID=66b207e6f14582f391fd01a623d9a4d7`

## Segurança

O token não foi salvo no Cofre. O Cofre registrou apenas o status operacional.

## Testes

- `npm run build`: OK.
- A API Notion foi testada diretamente.

## Resultado do teste Notion API

A Notion respondeu `404 object_not_found`, informando que não encontrou database/page/block com o ID recebido e orientando compartilhar com a integração `Mission Control Lógika`.

## Diagnóstico provável

1. O CRM ainda não foi compartilhado com a integração Notion; ou
2. O link recebido aponta para página (`/p/`) e não para o database real interno; ou
3. O ID correto do database é outro, dentro da página CRMaster.

## Próxima ação necessária

No Notion, abrir a página/database do CRM e adicionar a conexão:

`Mission Control Lógika`

Depois reenviar, se possível, o link direto do database/tabela CRM real.
