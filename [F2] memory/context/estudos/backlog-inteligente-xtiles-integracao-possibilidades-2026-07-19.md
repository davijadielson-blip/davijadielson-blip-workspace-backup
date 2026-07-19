# Backlog Inteligente — xTiles: possibilidades de integração

**Data:** 2026-07-19  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Pergunta:** “É possível se integrar a ele?”

## Resposta curta

Sim, é possível integrar o xTiles ao ecossistema, mas em camadas. A integração mais segura agora parece ser: xTiles como painel visual + Google Calendar para compromissos/blocos + Cofre como fonte de verdade do método e registros.

## O que foi encontrado

Pelo Cofre, Jadielson já conhecia/usava xTiles em algum nível. Pela pesquisa externa, xTiles oferece:

- tarefas com data, horário, lembretes e recorrência;
- visualização de tarefas no planner/calendário;
- integração com Google Calendar e Outlook, incluindo sync bidirecional segundo documentação pública;
- importação/exportação em Markdown e CSV, além de exportação PDF/PNG;
- menção pública a “API & Integrations” e “MCP access” em beta/planos, mas isso precisa ser validado dentro da conta/plano de Jadielson.

## Camadas possíveis de integração

### 1. Integração operacional simples

- xTiles: painel visual do Backlog Inteligente.
- Google Calendar: compromissos e blocos de tempo.
- Cofre: método, decisões, análises, templates e memória.

### 2. Integração por calendário

Como o xTiles sincroniza com Google Calendar, a Central pode continuar usando `gog` para ler/criar eventos no Google Calendar. Assim, compromissos/blocos podem aparecer no xTiles via sync de calendário.

### 3. Integração por Markdown/CSV

Como xTiles suporta import/export Markdown/CSV, o Cofre pode gerar arquivos `.md` e tabelas estruturadas para importação manual/semi-automática no xTiles.

### 4. Integração via MCP/API

Há indício público de MCP access/API em beta. Se a conta de Jadielson tiver acesso, pode ser possível criar integração mais direta com o ecossistema. Isso exige verificação técnica com Lôh/arquitetura antes de usar em produção.

### 5. Browser automation

Se não houver API/MCP oficial, ainda pode haver automação por navegador, mas deve ser última opção por ser mais frágil.

## Recomendação

Antes de integrar de verdade, fazer uma prova de conceito:

1. Criar no xTiles um painel `Backlog Inteligente`.
2. Criar áreas: Inbox, Mapa 360, Projetos/Listas, Ordem do Dia, Revisão Semanal.
3. Conectar Google Calendar ao xTiles.
4. Testar se tarefas com data/horário e compromissos aparecem bem.
5. Verificar se a conta de Jadielson mostra opção de API/MCP.
6. Se houver API/MCP, escalar para Lôh para desenho de integração oficial.

## Decisão operacional provisória

xTiles pode ser tratado como candidato forte para painel visual do Backlog Inteligente, mas a fonte de verdade do método continua no Cofre. Qualquer integração profunda deve passar por Lôh por envolver arquitetura, segurança e autenticação.

## Fontes

- Cofre: avaliação inicial de xTiles e método operacional v4 do Backlog Inteligente.
- Tavily: documentação pública xTiles Help/Pricing/Google Calendar Integration.
