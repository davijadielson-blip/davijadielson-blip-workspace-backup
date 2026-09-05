---
tema: relatorio da revisao do Cofre etapa 2
conteudo: sondagem, movimentacoes, arquivos atualizados, contradicoes resolvidas, dependencias verificadas e riscos restantes
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: relatorio de revisao
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: auditar a segunda etapa de limpeza do Cofre e entender o que saiu da rota ativa
nao_usar_quando: substituir MAPA.md, AGENTS.md ou 00-central/decisoes.md
---

# Revisao do Cofre - etapa 2 - limpeza da rota ativa

## Objetivo

Deixar o Cofre mais limpo, claro e menos contraditorio, sem apagar historico e sem quebrar automacoes. A revisao foi conservadora: itens com dependencia provavel ou valor operacional recente foram mantidos.

## Sondagem realizada

- Mapeadas as pastas `00-central/` a `90-arquivo/`, `memory/`, `skills/`, `scripts/`, `70-agentes/` e `80-handoffs/`.
- Buscadas referencias a F0/F1/F2/F3, "bibliotecaria", "IA so le", "nao editar F1", BOOTSTRAP, Zapier e comandos de exclusao.
- Verificados arquivos `.md` sem YAML frontmatter.
- Verificadas referencias internas antes das movimentacoes com `rg`.
- Verificados scripts ativos de sync Notion/Calendar com `python3 -m py_compile`.

## Arquivos movidos para 90-arquivo

Destino: `90-arquivo/30-regras-obsoletas/2026-08-10-planos-e-inventarios-superados/`

- `00-central/03-cockpit-projetos.md`
- `00-central/classificacao-arquivos-nao-md.md`
- `00-central/diagnostico-e-proposta-reorganizacao-cofre.md`
- `00-central/inventario-arquivos-nao-md.md`
- `00-central/inventario-frentes-f1-restantes.md`
- `00-central/inventario-md-sem-frontmatter.md`
- `00-central/plano-consolidacao-memorias.md`
- `00-central/plano-migracao-clientes-frentes.md`

Destino: `90-arquivo/40-revisao-humana/2026-08-10-itens-fora-da-rota-ativa/`

- `00-central/manifesto.md`
- `40-projetos/README-legado.md`

## Arquivos atualizados

- `HEARTBEAT.md`: fontes obrigatorias atualizadas para a estrutura numerada atual.
- `MAPA.md`: adicionadas rotas de arquivamento/revisao em `90-arquivo/`.
- `00-central/mapa-do-cofre.md`: adicionada politica de arquivamento sem exclusao.
- `00-central/decisoes.md`: registrada a etapa 2 e atualizadas referencias de documentos arquivados.
- `00-central/pendencias.md`: pendencias antigas substituidas por lista atual.
- `00-central/notas-permanentes/_MAP.md`: removida regra antiga de F1/IA somente leitura e substituida pela logica atual.
- `00-central/inbox/_README.md`: removida regra antiga de F0 e "sistema nao edita".
- `40-projetos/00-mapa.md`: removida regra antiga de `[F3] PROJETOS` como estrutura atual.
- `70-agentes/_MANDATORY.md`: `MAPA.md` passa a ser rota principal; `_MAP.md` e local/legado.
- `20-profissional/90-referencias/caio-architect.md`: removida mencao operacional a Zapier MCP.
- `40-projetos/30-projetos-autorais/01_Autorais_Culturais/Editais Culturais/README.md`: metodo de Drive alinhado para browser, `gog drive` ou API direta aprovada.
- `memory/2026-08-10.md`: adicionado frontmatter YAML.
- `70-agentes/runtime/central-pessoal/memory/2026-08-08.md`: adicionado frontmatter YAML em arquivo runtime vazio.

## Duplicidades consolidadas

- Nao houve fusao de conteudo profundo nesta etapa.
- A consolidacao foi de rota: documentos de diagnostico, inventario e plano que duplicavam a funcao atual de `MAPA.md`, `00-central/mapa-do-cofre.md`, `00-central/decisoes.md` e `00-central/pendencias.md` sairam de `00-central/`.

## Contradicoes resolvidas

- Removidas da rota ativa instrucoes antigas de:
  - F0 como inbox operacional atual;
  - F3 como mapa atual de projetos;
  - IA apenas leitora ou "sistema nao edita";
  - heartbeat buscando fontes atuais em `[F2] memory/`, `[F1] 5-Frentes/` e `[F3] PROJETOS/`;
  - Zapier como metodo operacional em documento ativo de projeto/referencia.

## Itens mantidos por duvida

- `README.md`, `CHANGELOG.md` e `FAQ.md` da raiz: parecem material do Starter Kit/OpenClaw e exigem decisao humana antes de sair da raiz.
- Bases de cliente em `50-clientes/*/20-fontes/base-legada-f1-frente/`: contem mapas e referencias antigas, mas tambem preservam origem migrada e contexto editorial; precisam de lote especifico por cliente.
- Duplicidades internas da Saude em `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/`: ha muitos arquivos com mesmo nome em subpastas diferentes, mas a funcao de cada subpasta precisa ser revisada antes de mover.
- Arquivos de runtime e estados OpenClaw nao rastreados em `70-agentes/runtime/`: mantidos fora do escopo do commit ate revisao de sensibilidade.

## Dependencias verificadas

- `rg` por caminhos movidos fora de `90-arquivo/`: referencias restantes relevantes ficam em historico (`memory/2026-07-26.md`) e em `00-central/decisoes.md`, agora com observacao de arquivamento.
- `scripts/sync/notion-cofre-index-import.py`, `scripts/sync/notion-cofre-sync.py` e `scripts/sync/notion-to-calendar.py`: `py_compile` OK.
- Busca por Zapier fora de `90-arquivo/`: restaram mencoes historicas em `memory/` e regras de proibicao; mencoes operacionais ativas corrigidas.
- Verificacao de frontmatter `.md`: sem pendencias apos ajustes.

## Riscos restantes

- `MEMORY.md` ainda contem registros historicos com F2/F3, mas como memoria longa e historica; nao foi alterado nesta etapa para evitar perda de contexto.
- Alguns mapas `_MAP.md` dentro de bases migradas continuam com nomenclatura antiga; precisam de lote por frente para nao quebrar rastreabilidade.
- Ha arquivos nao rastreados anteriores no worktree que nao pertencem diretamente a esta revisao e foram preservados.
- Commit deve incluir apenas a revisao atual e arquivos relacionados, evitando estados runtime sensiveis nao auditados.

## Recomendacoes de proxima etapa

1. Fazer lote especifico para `50-clientes/10-saude-sao-sebastiao/`, revisando duplicidades internas e indices de fichas/setores.
2. Decidir se arquivos raiz do Starter Kit/OpenClaw saem da rota ativa para `90-arquivo/40-revisao-humana/`.
3. Criar indices curtos por area (`20-profissional/`, `40-projetos/`, `50-clientes/`) quando a navegacao ainda depender de nomes legados extensos.
4. Auditar estados runtime nao rastreados antes de qualquer commit amplo.

## Resultado

O Cofre ficou com `00-central/` mais enxuto, mapas ativos mais alinhados com a estrutura numerada e menos instrucoes contraditorias na rota consultada pelos agentes. Nada foi excluido definitivamente.
