# Integração Google Calendar — Central Pessoal / Alfred

**Data:** 2026-07-09
**Solicitante:** Jadielson Davi
**Origem:** Telegram — Central Pessoal / tópico Alfred

## Pedido
Jadielson perguntou se havia acesso ao Google Calendar e autorizou prosseguir com a configuração.

## Ação realizada
- Google Calendar foi habilitado no MCP/Zapier.
- Conexão detectada: conta Google de Jadielson (`davijadielson@gmail.com`).
- Ações habilitadas incluem: buscar calendários, consultar eventos, buscar períodos ocupados, criar eventos, atualizar eventos, mover eventos, adicionar/remover participantes e criar calendário.

## Bloqueio encontrado
Ao testar a leitura de calendários, o Zapier retornou erro:

```text
insufficient tasks on account
402 Payment Required
```

Interpretação: a integração está configurada/habilitada, mas a execução prática está bloqueada por limite/crédito/tarefas da conta Zapier/MCP.

## Próximo passo necessário
Jadielson precisa revisar/liberar tarefas no Zapier/MCP ou plano/limite da conta para que Alfred/Lôh possam consultar/criar eventos de calendário por essa via.

URL de configuração MCP/Zapier:
https://mcp.zapier.com/mcp/servers/68504adf-0b04-436d-85f7-ceb6903b76d3/config

## Regra operacional
Depois que o bloqueio for resolvido, validar primeiro com consulta simples de calendários antes de criar/alterar qualquer evento.

## Consulta solicitada — “o que tem lá previsto?”
Jadielson perguntou o que havia previsto no Google Calendar. Como a leitura real do Calendar segue bloqueada por `insufficient tasks on account`, Alfred informou que não conseguiu ver a agenda real do Calendar e usou como referência apenas a agenda inicial registrada no Cofre em `2026-07-09-pendencias-tarefas-rotina-producao-projetos.md`.
