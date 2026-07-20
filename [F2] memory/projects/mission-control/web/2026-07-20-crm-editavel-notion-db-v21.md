# Mission Control v2.1 — CRM editável com Notion como database

**Data:** 2026-07-20 03:15 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Contexto

Jadielson abriu o Mission Control pelo túnel, mas observou que não conseguia editar. A direção correta foi definida: o Mission Control deve ser interface independente, usando o Notion apenas como database.

## Entrega

Foi criada a primeira camada de edição direta do CRM pelo Mission Control, gravando no Notion via API.

## O que agora é editável

### Leads/pipeline

- Status.
- Telefone.
- E-mail.
- Último contato.

### Tarefas

- Data final/prazo.
- Marcar como feita.

## Arquivos criados/alterados

No app:

- `lib/notionMutations.js`
- `app/api/logika-crm/route.js`
- `components/CrmEditor.jsx`
- `components/CrmPanel.jsx`
- `app/globals.css`

## Como funciona

- Frontend envia `PATCH` para `/api/logika-crm`.
- API server-side atualiza a página/tarefa no Notion.
- Depois recarrega dados da Notion API.
- Token Notion permanece server-side.

## Testes

- `npm run build`: OK.
- Servidor produção reiniciado.
- Smoke test externo pelo Cloudflare Tunnel: OK.

URL atual do túnel temporário:

`https://likewise-threats-its-payroll.trycloudflare.com`

## Observação

Esta é a primeira camada de CRUD. Ainda não inclui criação de novos leads/tarefas nem edição de todos os campos, mas já remove a dependência de abrir o Notion para correções básicas.

## Próximos passos

1. Criar formulário de novo lead.
2. Criar formulário de nova tarefa por lead.
3. Adicionar botões de ação rápida: follow-up enviado, pausar, perdido, fechado.
4. Melhorar UX sem reload completo.
