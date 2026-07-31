---
tema: simplificação da estrutura operacional da Saúde São Sebastião
conteudo: log de reorganização para reduzir subpastas profundas e facilitar consulta por agentes
setor: comunicação institucional e organização do Cofre
cliente: Saúde São Sebastião
tipo: log de organização
prioridade: alta
atualizado_em: 2026-07-30
usar_quando: auditar a reorganização da estrutura operacional da Secretaria de Saúde
nao_usar_quando: buscar a fonte operacional atual sem precisar do histórico da mudança
---

# Log - Simplificação da Estrutura Operacional

Data: 2026-07-30

## Motivo

Jadielson observou que a estrutura operacional estava com muitas subpastas uma dentro da outra e que isso poderia confundir agentes ou fazer conteúdos importantes passarem despercebidos.

## Nova entrada operacional

`50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/`

## Movimentações principais

- Matrizes de `10-contexto/memoria-operacional-f2/01-matrizes/` foram movidas para `10-contexto/operacional/01-matrizes/`.
- Visões gerais de `10-contexto/memoria-operacional-f2/02-estrutura/` foram achatadas em `10-contexto/operacional/02-visoes-gerais/`.
- Fichas e documentos por setor de `10-contexto/memoria-operacional-f2/05-ambientes-operacionais/` foram achatados em `10-contexto/operacional/03-fichas-setores/`, separados por tipo:
  - `fichas-operacionais/`
  - `servicos-e-competencias/`
  - `ideias-de-conteudo/`
  - `lacunas-a-confirmar/`
  - `fontes-f1-incorporadas/`
  - `conteudo-f1-incorporado/`
- READMEs de categorias foram preservados em `10-contexto/operacional/90-readmes-categorias/`.

## Estrutura antiga

As pastas antigas esvaziadas foram movidas para:

`50-clientes/10-saude-sao-sebastiao/90-arquivo/estrutura-operacional-antiga-2026-07-30/`

## Garantias

- Nenhum arquivo foi apagado.
- A consulta operacional ficou com menos níveis de profundidade.
- A entrada recomendada para agentes agora é `10-contexto/operacional/README.md`.
