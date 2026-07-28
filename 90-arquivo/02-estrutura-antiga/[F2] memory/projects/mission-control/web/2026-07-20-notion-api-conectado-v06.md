---
tema: 07 20 notion api conectado v06
atualizado_em: 2026-07-22
---

# Mission Control Web MVP v0.6 — CRM Notion conectado

**Data:** 2026-07-20 01:12 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** conectado e testado

## Contexto

Jadielson informou que a integração Notion foi adicionada ao CRM.

## Resultado

A conexão via Notion API direta funcionou.

## Descoberta técnica

O link inicial apontava para a página principal do template CRM:

`66b207e6f14582f391fd01a623d9a4d7`

Essa página contém vários databases internos. O database operacional identificado para o pipeline foi:

`9d3207e6f14582f4bab101bfc90fb58c`

Título no Notion: `Pipeline`

## Configuração aplicada

No app fora do Cofre:

`/data/.openclaw/mission-control-next/.env.local`

foi configurado:

`NOTION_LOGIKA_CRM_DATABASE_ID=9d3207e6f14582f4bab101bfc90fb58c`

O token permanece fora do Cofre.

## Teste da API

Resultado:

`Conectado via Notion API — 7 itens`

Exemplos lidos:

- test — Lead
- Jonathan — Contactado
- Guilherme — Em Negociação
- Kim Wayn — Proposta Enviada
- Gilberto — Contactado

## Ajuste de código

`lib/notionClient.js` foi ajustado para ler propriedades Notion do tipo `status`.

## Build

`npm run build`: OK após configuração.

## Próximos passos

1. Ajustar mapeamento de campos específicos do template CRMaster.
2. Exibir valor, contato, empresa e tarefas pendentes se necessário.
3. Definir se o painel deve usar o database `Pipeline` ou `Todos Cadastros` como fonte principal.
