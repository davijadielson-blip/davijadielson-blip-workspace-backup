---
tema: integracoes notion
conteudo: status das conexoes Notion usadas pelo ecossistema, sem armazenar tokens ou credenciais em Markdown
setor: operacoes tecnicas e produtividade
cliente: Jadielson Davi
tipo: contexto-operacional
prioridade: alta
atualizado_em: 2026-08-11
usar_quando: conectar, testar, auditar ou operar areas de trabalho do Notion pelo OpenClaw
nao_usar_quando: buscar tokens, segredos ou credenciais completas
---

# Integracoes Notion

## 2026-08-06 - Conta particular MAPA 360

Jadielson solicitou a criacao de uma nova conexao com uma conta particular do Notion para trabalhar no workspace.

Status inicial:

- Conexao local configurada via `scripts/.secrets/notion.env`.
- Token armazenado apenas em arquivo de segredo local, com permissao `600`.
- Variaveis carregadas por `scripts/notion-env.sh`: `NOTION_TOKEN`, `NOTION_API_TOKEN` e `NOTION_API_VERSION`.
- CLI oficial `ntn` instalada e validada na versao `0.21.8`.
- Teste `users/me` validado com sucesso.
- Integracao identificada como bot no workspace `MAPA 360`.
- Busca inicial no Notion retornou `0` paginas/databases acessiveis.

Status apos compartilhamento da pagina:

- Jadielson criou e compartilhou a pagina-mae `MAPA 360` com a integracao.
- Pagina-mae acessivel pela API: `https://app.notion.com/p/MAPA-360-3b4316b19f9280249128c2631a992e4d`.
- Estrutura inicial materializada dentro do Notion em 2026-08-06:
  - 10 paginas de navegacao: Painel Hoje, Pessoal, Profissional - LOGIKA, Frentes Ativas, Producao de Conteudo, Projetos e Tarefas, Decisoes e Memoria Operacional, Arquivos e Referencias, Agentes e Sistema Loh, Governanca do MAPA 360.
  - 11 databases: Captura Geral, Projetos, Tarefas, Clientes e Leads, Conteudos, Frentes, Pessoas, Reunioes e Atas, Decisoes, Arquivos - Drive Index, Rotina e Habitos.
  - 19 registros iniciais criados em Frentes, Decisoes, Projetos, Tarefas, Captura Geral e Arquivos - Drive Index.

Leitura operacional:

A autenticacao esta funcionando e a pagina-mae `MAPA 360` ja esta operavel. O Notion agora funciona como camada visual/operacional; o Cofre continua sendo a fonte de verdade em Markdown, e arquivos nao Markdown continuam indo para o Drive.

Proximo passo:

Refinar views, relacionamentos entre databases, templates internos e importacao seletiva do Cofre/Drive. Evitar migracao automatica de notas autorais do Fluxo 1 sem validacao humana.

Atualizacao de governanca:

- Jadielson autorizou importar tudo em paralelo, comecando pelo essencial.
- O Notion `MAPA 360` deve funcionar como painel visivel e operacional do Cofre.
- Tarefas com data/hora seguem no Calendar; Notion fica como painel de gestao.
- Conteudo pessoal pode ser estruturado de forma completa no Notion particular.
- Alteracoes no Notion podem atualizar o Cofre automaticamente quando forem operacionais e governadas.
- Fluxo 1 autoral permanece protegido por revisao antes de alteracoes diretas.

Registro de arquitetura: `memory/context/notion-painel-cofre-sync.md`.

Implementacao complementar:

- Criadas databases `Cofre Index` e `Sync Log` no Notion `MAPA 360`.
- Indexados 80 arquivos essenciais do Cofre no Notion.
- Criado script `scripts/sync/notion-cofre-sync.py` para sincronizacao governada Notion -> Cofre.
- Teste seco inicial: 80 itens verificados, sem erros e sem gravacoes.

Regra de seguranca:

Nao registrar token ou segredo completo em Markdown. O Cofre deve guardar apenas status, origem, caminho seguro da credencial, resultado de testes e proximas acoes.

## 2026-08-11 - Producao & Agenda LOGIKA via Loh-bot

Jadielson confirmou que o `MAPA 360` deve ficar mais ligado ao uso pessoal/estrategico, enquanto a base `Producao & Agenda - LOGIKA` deve ser operada por integracao separada de producao.

Status operacional:

- Integracao local de producao configurada em `scripts/.secrets/notion-logika-producao.env`.
- Token armazenado apenas em arquivo de segredo local, com permissao `600`.
- Variaveis usadas: `NOTION_LOGIKA_TOKEN`, `NOTION_PRODUCAO_DATABASE_ID` e `NOTION_API_VERSION`.
- Teste `users/me` validado com sucesso.
- Integracao identificada como bot `Loh-bot` no workspace `LOGIKA CREATIVE`.
- Database acessivel pela API: `Producao & Agenda - LOGIKA`.
- ID operacional: `375207e6-f145-8111-bba0-e132fd820542`.
- Propriedades lidas na validacao: `Nome`, `Status`, `Data de publicacao`, `Data do evento`, `Frente/Cliente`, `Plataforma`, `Tipo de conteudo`, `Entregas previstas`, `Briefing/Roteiro`, `Observacoes`, `Responsavel`, `Prioridade`, `Arquivos/Links`, `Link de origem`, `Origem`, `Tipo`, `Gera conteudo?`, `Criado em`, `Ultima edicao`.

Teste seco em `scripts/sync/notion-to-calendar.py`:

- A rotina passou a carregar `scripts/.secrets/notion-logika-producao.env` alem do `notion.env`.
- A consulta da base de producao usa `NOTION_LOGIKA_TOKEN`, preservando o token do `MAPA 360` para o painel pessoal/Cofre.
- Resultado da leitura seca em 2026-08-11: 56 itens elegiveis no Notion, sendo 54 da Saude e 2 da LOGIKA.

Propagacao para agentes:

- `scripts/notion-env.sh` carrega tanto `notion.env` quanto `notion-logika-producao.env`.
- `TOOLS.md` documenta os dois escopos Notion e as variaveis que os agentes podem usar.
- A skill `.agents/skills/source-command-sync-notion-calendar/SKILL.md` orienta agentes a carregar o ambiente, validar leitura seca e so rodar sync completo com confirmacao para atualizar Calendar.

Leitura operacional:

O acesso a base de producao esta funcional neste ambiente. O proximo passo, antes de rodar sincronizacao completa com Google Calendar, e validar se as regras de status, datas e criacao/atualizacao de eventos estao corretas para nao duplicar eventos antigos.

Diretriz operacional confirmada em 2026-08-11:

- Toda pauta definida para producao da LOGIKA deve ser lancada na base `Producao & Agenda - LOGIKA`.
- Para pautas de cobertura/evento, criar um item por dia/evento, mantendo a pauta de producao dentro da pagina do item.
- Nao usar a base pessoal `MAPA 360` para lancamento operacional de pautas da producao; ela fica como painel pessoal/estrategico.
- Usar o acesso de producao da integracao `Loh-bot` e as variaveis carregadas por `scripts/notion-env.sh`.
- Nao registrar tokens ou segredos no Cofre; manter apenas nomes de integracao, caminhos seguros e regras de uso.
