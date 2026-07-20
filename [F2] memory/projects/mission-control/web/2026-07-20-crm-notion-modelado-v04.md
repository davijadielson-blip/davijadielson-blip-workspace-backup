# Mission Control Web MVP v0.4 — CRM Notion modelado

**Data:** 2026-07-20 00:25 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** Implementado e testado parcialmente; integração real Notion pendente por limite Zapier.

## Pedido

Jadielson autorizou avançar para a modelagem/integração do CRM Notion da Lógika.

## Verificação Notion

As ações Notion estavam habilitadas via Zapier. Porém, ao tentar executar busca/criação no Notion, a chamada retornou erro:

`insufficient tasks on account`

Portanto, a integração real com Notion não pôde ser concluída nesta rodada.

## Entrega realizada mesmo assim

Foi feita a etapa possível e segura:

1. Modelo do CRM Notion criado no Cofre.
2. Camada visual do CRM adicionada ao Mission Control Web.
3. App atualizado para exibir status de integração.
4. Build testado com sucesso.
5. Servidor local testado com conteúdo do CRM.

## Arquivo de modelo criado

`[F2] memory/projects/mission-control/notion-crm-logika-modelo-v01.md`

## App atualizado

Local:

`/data/.openclaw/mission-control-next/`

Arquivos adicionados/alterados:

- `lib/notionCrmModel.js`
- `components/CrmPanel.jsx`
- `app/page.jsx`
- `app/globals.css`

## O CRM no dashboard mostra

- Status: `Aguardando conexão Notion`.
- Nome sugerido do database: `CRM — Lógika Creative`.
- Campos mínimos.
- Pipeline sugerido.
- Leads de exemplo/modelo.
- Aviso de que a execução Notion está pendente.

## Testes

- `npm run build`: OK.
- Teste HTTP local: OK.
- Validações no HTML:
  - `CRM — Lógika Creative`;
  - `Aguardando conexão Notion`;
  - `Lead exemplo`.

## Próximos passos

1. Resolver limite de tarefas Zapier ou usar outro caminho de autenticação Notion.
2. Criar database real no Notion com o modelo definido.
3. Substituir leads de exemplo por dados reais.
4. Criar sincronização real Notion → Mission Control.

## Fonte

- Cofre: `CONSTITUICAO.md`, Mission Control v0.3, artefatos Lógika.
- Ferramenta específica: Zapier/Notion listou ações disponíveis, mas execução retornou erro de conta.
