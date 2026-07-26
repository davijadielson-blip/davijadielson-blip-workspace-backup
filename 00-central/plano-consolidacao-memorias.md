---
tema: plano de consolidação das memórias do Cofre
conteudo: definição canônica, plano reversível para memory e [F2] memory, riscos e próximos passos
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: plano de migração
prioridade: máxima
atualizado_em: 2026-07-26
usar_quando: consolidar pastas de memória sem quebrar agentes, buscas ou histórico
nao_usar_quando: mover arquivos sem registrar etapa em decisões
---

# Plano de consolidação das memórias

## Decisão operacional do lote 3
A consolidação deve preservar compatibilidade com agentes e histórico. Portanto, neste lote:

- `memory/` permanece como **memória ativa de sessão/dia**, porque vários protocolos e agentes já consultam `memory/YYYY-MM-DD.md`.
- `[F2] memory/` permanece como **memória operacional legada e base histórica rica** até migração por área.
- Pastas vazias/duplicadas por erro de nome (`[F2]memory/`, `\[F2\] memory/`) podem ser arquivadas em `90-arquivo/20-duplicidades/`.
- A migração de conteúdo não vazio será feita por lote temático, não por arrasto cego.

## Alvo futuro
- Memória transversal e regras: `00-central/`.
- Memória diária/sessões: `memory/`.
- Conteúdo por área: `10-pessoal/`, `20-profissional/`, `30-estudos/`, `40-projetos/`, `50-clientes/`, `60-processos/`, `70-agentes/`, `80-handoffs/`.
- Legado/duplicado: `90-arquivo/`.

## Riscos evitados
- Quebrar agentes que esperam `memory/YYYY-MM-DD.md`.
- Perder histórico rico dentro de `[F2] memory/`.
- Misturar clientes, pessoal e decisões centrais em uma única migração.

## Próximos lotes sugeridos
1. Migrar `[F2] memory/context/governanca/` e `[F2] memory/context/decisoes/` para `00-central/` ou `60-processos/`, mantendo notas de origem.
2. Migrar `[F2] memory/agents/` para `70-agentes/`.
3. Migrar `[F2] memory/saude-sao-sebastiao/` e outputs relacionados para `50-clientes/10-saude-sao-sebastiao/`.
4. Migrar `[F2] memory/projects/` por projeto para `40-projetos/`.
