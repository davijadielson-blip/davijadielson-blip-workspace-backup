# Auditoria do Google Drive pessoal — plano, escopo e status inicial

**Data:** 2026-07-07
**Solicitante:** Jadielson Davi
**Agente:** Alfred / Central Pessoal
**Canal:** Telegram — Central Pessoal / tópico Alfred

## Pedido recebido
Jadielson informou que no Drive pessoal existem vários arquivos e pastas pertinentes à vida pessoal e solicitou uma auditoria em todo o Drive.

## Parede-d'água e premissas
- Tratar como frente de **vida pessoal**, mantendo separação total de LÓGIKA/clientes e demais frentes.
- Não excluir, apagar ou remover nada.
- A auditoria deve ser inicialmente **read-only**.
- Qualquer ação de organização efetiva, movimentação, compartilhamento, renomeação ou quarentena deve exigir etapa posterior com validação humana.

## Acesso tentado
- Google Drive via Zapier MCP foi habilitado/consultado.
- Conta conectada apresentada pela ferramenta: `logikacreative.mkt@gmail.com`.
- Tentativa de chamada read-only via Google Drive API (`files.list`, `trashed=false`) falhou por limitação operacional da conta Zapier: `insufficient tasks on account` / HTTP 402.
- Tentativa de navegador com perfil de usuário não conectou ao Chrome existente; perfil OpenClaw não foi validado como logado.

## Status
Auditoria ainda **não executada** por bloqueio de acesso operacional ao Drive/API.

## Plano recomendado da auditoria

### Fase 0 — Confirmação de acesso
1. Confirmar se o Drive a auditar é o Drive associado à conta exibida pela integração ou outro Drive pessoal.
2. Liberar um caminho de acesso operacional:
   - Zapier com quota/tarefas disponíveis; ou
   - navegador logado acessível; ou
   - exportação/relatório do Google Drive; ou
   - Takeout/listagem CSV; ou
   - conta/API de serviço apropriada, se aplicável.

### Fase 1 — Inventário estrutural
- Listar todas as pastas e arquivos não enviados à lixeira.
- Capturar metadados: nome, tipo, ID, caminho/parent, proprietário, tamanho, data de criação, data de modificação, compartilhamento, link de visualização.
- Reconstruir árvore de pastas.

### Fase 2 — Classificação pessoal
Classificar itens em categorias prováveis:
- Documentos pessoais e identidade.
- Família/casa/saúde.
- Finanças pessoais.
- Estudos e formações.
- Projetos pessoais.
- Fé/igreja/conteúdo pessoal.
- Arquivos legados/desorganizados.
- Duplicados ou versões antigas.
- Materiais sensíveis.
- Mistura indevida com LÓGIKA/clientes.

### Fase 3 — Riscos e oportunidades
- Detectar arquivos compartilhados externamente.
- Identificar itens públicos/com link aberto.
- Sinalizar documentos sensíveis fora de pasta adequada.
- Identificar pastas sem padrão de nomeação.
- Mapear duplicatas, arquivos grandes e arquivos abandonados.
- Sugerir árvore-alvo para vida pessoal.

### Fase 4 — Entregáveis
- Relatório executivo.
- Inventário estruturado em CSV/Markdown.
- Mapa de pastas atual.
- Mapa de riscos de compartilhamento.
- Plano de reorganização sem exclusões.
- Lista de ações propostas para validação humana.
- Materiais para Arca organizar no Segundo Cérebro, se houver conteúdo de conhecimento/captura.

## Próximos passos
1. Informar ao Jadielson que o bloqueio atual é quota/tarefas do Zapier e/ou acesso de navegador.
2. Solicitar/confirmar o caminho de acesso preferido.
3. Após acesso, executar a auditoria em modo somente leitura e salvar entregáveis em `[F2] memory/outputs/central-pessoal/`.

## Fontes internas
- `/data/.openclaw/workspace/AGENTS.md`
- `/data/.openclaw/workspace/MAPA.md`
- Tentativas com Zapier Google Drive MCP em 2026-07-07
