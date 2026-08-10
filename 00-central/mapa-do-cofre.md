---
tema: mapa central do Cofre reorganizado
conteudo: estrutura firme por áreas, finalidade de cada pasta, regras de acesso contextual e rotas de salvamento
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: mapa operacional
prioridade: máxima
atualizado_em: 2026-08-10
usar_quando: decidir onde buscar ou salvar qualquer informação no Cofre
nao_usar_quando: substituir CONSTITUICAO.md; este mapa operacional complementa a lei maior
---

# Mapa do Cofre reorganizado

## Princípio central
O Cofre é alimentado primariamente por agentes. Portanto, a nova estrutura abandona a lógica de “pastas onde agentes não podem escrever” e adota a lógica de **responsabilidade, rastreabilidade e acesso contextual mínimo**.

Agentes podem criar/editar arquivos quando a tarefa exigir, mas devem:
1. preservar fatos e fontes;
2. não apagar arquivos;
3. não expor segredos;
4. separar rascunho de decisão;
5. registrar decisões e pendências nos lugares centrais.

## Estrutura-alvo

```txt
workspace/
 00-central/       governança, mapa, regras, decisões, pendências, glossário
 10-pessoal/       vida pessoal, rotina, saúde, finanças pessoais, família, propósito
 20-profissional/  carreira, Lógika, operação profissional interna
 30-estudos/       cursos, leituras, fichamentos, trilhas de aprendizagem
 40-projetos/      projetos autorais/iniciativas com começo, meio e fim
 50-clientes/      contexto, estratégia e entregáveis por cliente/frente externa
 60-processos/     SOPs, checklists, templates e automações documentadas
 70-agentes/       mapa, escopos, handbooks e protocolos dos agentes
 80-handoffs/      passagens formais entre agentes
 90-arquivo/       legado, duplicidades, quarentena e revisão
 memory/           memória operacional ativa, sessões, outputs e inbox externa
 media/            mídias recebidas ou referenciadas
 scripts/          automações executáveis
 skills/           skills ativas do workspace
```

## Legado F0/F1/F2/F3

Os fluxos `[F0]`, `[F1]`, `[F2]` e `[F3]` foram migrados para a estrutura numerada e agora são apenas referência histórica/técnica. Use-os somente para interpretar logs, memórias antigas e dependências temporárias.

Antes de mover ou renomear qualquer caminho antigo ainda referenciado, audite agentes, skills, scripts, crons, runtimes, handoffs e configurações.

## Arquivamento sem exclusão

Quando um arquivo ativo estiver obsoleto, duplicado, contraditório ou irrelevante operacionalmente, ele deve sair da rota ativa sem ser apagado:

- `90-arquivo/20-duplicidades/` para duplicidades claras;
- `90-arquivo/30-regras-obsoletas/` para planos, inventários e regras superadas;
- `90-arquivo/40-revisao-humana/` quando houver dúvida sobre valor histórico, autoria ou destino;
- subpastas datadas para cada lote de limpeza.

Toda movimentação deve registrar origem, destino, motivo e dependências verificadas em relatório do lote.

## Regra de acesso
Acesso não é definido por “pode escrever/não pode escrever”, e sim por **necessidade operacional**:
- agente recebe o mínimo de contexto necessário;
- agente registra o que fez;
- agente cita arquivos consultados;
- LÔH coordena cruzamentos entre áreas.

## Rotas de salvamento
| Tipo | Salvar em |
|---|---|
| Decisão final | `00-central/decisoes.md` |
| Pendência transversal | `00-central/pendencias.md` |
| Regra/protocolo | `00-central/regras-de-uso.md` ou `60-processos/` |
| Mapa/índice | `00-central/mapa-do-cofre.md` |
| Glossário | `00-central/glossario.md` |
| Agente/escopo | `70-agentes/` |
| Handoff | `80-handoffs/` |
| Pessoa/rotina/saúde/finanças pessoais | `10-pessoal/` |
| Lógika/carreira/operação profissional | `20-profissional/` |
| Curso/estudo/fichamento | `30-estudos/` |
| Projeto autoral | `40-projetos/` |
| Cliente/frente externa | `50-clientes/` |
| Checklist/template/processo | `60-processos/` |
| Legado/duplicado/antigo | `90-arquivo/` somente após aprovação quando envolver mover arquivo |

## Subpastas-base criadas

Cada área recebeu subpastas `00-indice`, áreas operacionais numeradas e `90-arquivo` local. Os índices `README.md` explicam finalidade, regra de uso e limites de cada pasta.
