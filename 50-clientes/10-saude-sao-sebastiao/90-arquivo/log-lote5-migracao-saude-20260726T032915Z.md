---
tema: log do lote 5 de migração Saúde São Sebastião
conteudo: movimentações realizadas, origem, destino, contagem, desfazer e pendências
nicho: ecossistema agêntico Lôh/Jadielson
setor: clientes e governança do Cofre
cliente: Saúde São Sebastião
tipo: log de execução
prioridade: alta
atualizado_em: 2026-07-26
usar_quando: auditar ou desfazer a migração real da frente Saúde São Sebastião
nao_usar_quando: consultar conteúdo operacional; use contexto.md e fontes.md
---

# Log lote 5 — Migração real Saúde São Sebastião

## Snapshot
- `90-arquivo/50-backups-snapshots/lote5-saude-before-20260726T032915Z.md`

## Movimentações
- `[F1] 5-Frentes/Saude-Sao-Sebastiao` → `50-clientes/10-saude-sao-sebastiao/20-fontes/base-legada-f1-frente` (279 arquivos)
- `[F2] memory/saude-sao-sebastiao` → `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2` (228 arquivos)
- `[F2] memory/outputs/saude-sao-sebastiao` → `50-clientes/10-saude-sao-sebastiao/30-entregas/outputs-f2` (36 arquivos)
- `[F3] PROJETOS/Saude-Sao-Sebastiao` → `50-clientes/10-saude-sao-sebastiao/30-entregas/projetos-f3` (2 arquivos)

## Como desfazer
Mover cada destino de volta para a origem correspondente. As notas `_ORIGEM_MIGRACAO.md` dentro de cada pasta também registram origem/destino.

## Pendências
- Revisar duplicidades internas entre `Projetos de Conteudo` e `Projetos de Conteúdo`.
- Separar materiais aprovados de rascunhos.
- Consolidar um resumo editorial validado.
