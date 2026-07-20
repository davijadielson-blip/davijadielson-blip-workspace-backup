# Mission Control Web v1.3 — Higiene CRM

**Data:** 2026-07-20 01:42 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Pedido

Jadielson pediu para seguir após a visão de aging comercial.

## Entrega

Foi criada a seção **Higiene CRM** dentro do Mission Control, apontando correções recomendadas no Notion.

## Regras de higiene implementadas

O sistema identifica:

1. **Tarefa atrasada** — tarefa aberta com status atrasado.
2. **Contato incompleto** — lead sem telefone e sem e-mail.
3. **Contato antigo** — lead com aging crítico.
4. **Registro teste** — possíveis registros de teste no pipeline.
5. **Tarefa sem data** — tarefa aberta sem prazo definido.

## Resultado atual

Consulta via Notion API direta:

- Itens de higiene CRM: 16.
- Críticas: 2 tarefas atrasadas.
- Altas: contatos incompletos e contatos antigos.
- Médias: registro teste e tarefas sem data.

## Principais correções recomendadas

1. Crítica — Guilherme — Follow Up — 857 dias de atraso.
2. Crítica — Gustavo — Enviar Proposta — 843 dias de atraso.
3. Alta — test — sem telefone e sem e-mail.
4. Alta — Gilberto — sem telefone e sem e-mail.
5. Alta — test — 850 dias sem contato.
6. Alta — Jonathan — 683 dias sem contato.
7. Alta — Guilherme — 683 dias sem contato.
8. Alta — Kim Wayn — 683 dias sem contato.
9. Alta — Gilberto — 683 dias sem contato.
10. Alta — João — 683 dias sem contato.
11. Alta — Gustavo — 683 dias sem contato.
12. Média — test — possível lead de teste no pipeline.

## Alterações no app

Local:

`/data/.openclaw/mission-control-next/`

Arquivos alterados:

- `lib/notionClient.js`
- `components/CrmPanel.jsx`
- `app/globals.css`
- `scripts/snapshot-logika-crm.mjs`

## Testes

- `npm run build`: OK.
- Consulta direta Notion API: OK.
- `npm run snapshot:crm`: OK.

## Impacto operacional

Agora o Mission Control não apenas mostra pipeline e risco, mas aponta exatamente o que limpar/corrigir no CRM para melhorar a confiabilidade comercial.

## Próximos passos recomendados

1. Criar plano de limpeza CRM em checklist.
2. Criar mensagens de follow-up sugeridas para leads críticos.
3. Criar rotina semanal de higiene CRM.
