# Mission Control v1

## Caminho do arquivo HTML
`/data/.openclaw/mission-control-web/mission-control.html`

## Versão atual
1.0.0

## Data
2026-07-20

## Changelog
- 1.0.0 — Primeira versão do Mission Control: painel offline em arquivo único, com DATA como fonte única de verdade, mapa clicável do ecossistema, Cofre, frentes, Central Pessoal, automações, integrações, saúde do sistema e rodapé de fontes.

## Como atualizar
1. Abrir o arquivo HTML.
2. Editar somente o objeto `DATA` no topo do `<script>`.
3. Atualizar `DATA.meta.versao`, `DATA.meta.atualizadoEm` e `DATA.meta.changelog`.
4. Não hardcodar conteúdo novo no HTML; todo conteúdo deve sair do `DATA`.
5. Se algum dado não estiver confirmado no Cofre, manter como `pendente`.
6. Ao alterar o HTML, atualizar este registro Markdown.

## Fontes consultadas
- `CONSTITUICAO.md`
- `MAPA.md`
- `AGENTS.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `[F2] agentes/ARQUITETURA-AGENTES.md`
- `[F2] agentes/protocolo-de-orquestracao.md`
- `[F2] agentes/logika-c-level-squad/logika-_MAP-agentes.md`
- `[F2] memory/outputs/reports/2026-07-20-relatorio-simples-sistema.md`
- `cron:list` para automações ativas

## Observações
- A busca semântica (`memory_search`) falhou por erro de chave de embeddings; foi usado fallback por leitura direta do Cofre e ferramentas de listagem, conforme Constituição.
- O HTML foi salvo fora do Cofre, porque o Cofre só aceita Markdown.

## Roadmap v2 — nota registrada, não executada agora
- Contagem real de arquivos por fluxo do Cofre.
- Busca/filtro no mapa.
- Modo apresentação para TV.
- Script que regenera o `DATA` automaticamente a partir do Cofre.

## Validação v1
- Arquivo abre offline diretamente no navegador.
- Sem dependências externas, build ou framework.
- Conteúdo operacional concentrado em `DATA`.
- Foco de teclado visível nos botões do mapa.
- Layout responsivo com grids que colapsam no celular.

## Versão 2.0.0 — App editável

### Caminho do app
`/data/.openclaw/mission-control-next/`

### Como rodar
```bash
cd /data/.openclaw/mission-control-next
npm run dev
```
Abrir no navegador: `http://127.0.0.1:4174`

### Fonte persistente editável
`/data/.openclaw/workspace/[F2] memory/visualizacoes/mission-control-data.md`

### Changelog
- 2.0.0 — Mission Control virou app editável: botão Editar painel, campos editáveis, botão Salvar no Cofre, API local `/api/mission-control`, persistência em Markdown e design com tokens visuais cinema orange & teal.

### Arquitetura de otimização
- UI lê `initialData` do servidor.
- API lê/escreve somente Markdown no Cofre.
- Conteúdo operacional fica no JSON dentro de `mission-control-data.md`.
- Mudanças visuais ficam concentradas em tokens CSS no topo de `globals.css`.
- Próximas melhorias devem referenciar seções por id: `#header`, `#mapa`, `#frentes`, etc.

### Teste
- `npm run build` executado com sucesso em 2026-07-20.

## Acesso externo temporário — 2026-07-20
- Problema: `127.0.0.1` só abre dentro do servidor; no celular de Jadielson não acessa.
- Correção operacional: app reiniciado em `0.0.0.0:4174` com autenticação básica e túnel temporário via localtunnel.
- URL temporária: `https://mission-control-jadielson.loca.lt`
- Observação: túnel é sessão temporária; se cair, pedir à Lôh para reacender o Mission Control.
