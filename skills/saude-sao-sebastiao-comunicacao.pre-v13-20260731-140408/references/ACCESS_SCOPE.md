---
tema: escopo de acesso da skill saude
conteudo: referencia operacional da skill saude-sao-sebastiao-comunicacao
setor: saude e comunicacao institucional
cliente: Secretaria Municipal de Saude de Sao Sebastiao
tipo: referencia de skill
prioridade: alta
atualizado_em: 2026-07-31
usar_quando: usar a skill saude-sao-sebastiao-comunicacao em demandas da Saude
nao_usar_quando: demandas fora da frente Saude Sao Sebastiao
---

# Escopo de acesso desta skill

## Permitido

- Cofre/workspace da Saúde:
  `/data/.openclaw/workspace/50-clientes/10-saude-sao-sebastiao`
- Contexto operacional:
  `/data/.openclaw/workspace/50-clientes/10-saude-sao-sebastiao/10-contexto/operacional`
- Google Drive profissional:
  `logikacreative.mkt@gmail.com`
- Fontes oficiais externas e Tavily, quando necessários.

## Proibido

- Google Drive pessoal:
  `davijadielson@gmail.com`

A proibição vale para busca, listagem, abertura, exportação, download, edição, compartilhamento, movimentação ou exclusão.

## Regra de falha segura

Quando um arquivo não for encontrado no cofre ou no Drive profissional:

1. não consulte automaticamente o Drive pessoal;
2. informe que a fonte profissional foi insuficiente;
3. peça que a LOH ou um contexto autorizado faça a recuperação, ou que o usuário forneça o arquivo;
4. prossiga somente com dados confirmados.

## Motivo

A skill da Saúde pertence ao domínio profissional. A conta pessoal fica restrita à LOH e aos contextos ESTUDOS, CENTRAL PESSOAL e PROJETOS.
