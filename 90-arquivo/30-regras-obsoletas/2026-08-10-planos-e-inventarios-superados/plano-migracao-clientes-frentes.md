---
tema: plano de migração de clientes e frentes
conteudo: mapeamento de fontes legadas para a nova estrutura 50-clientes e próximos lotes
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: plano de migração
prioridade: alta
atualizado_em: 2026-07-26
usar_quando: migrar conteúdos de clientes/frentes para 50-clientes de forma segura
nao_usar_quando: mover arquivos sem registrar origem, destino e forma de desfazer
---

# Plano de migração — Clientes e frentes

## Decisão do Lote 4
Criar estrutura canônica por cliente/frente em `50-clientes/`, sem mover conteúdo legado ainda.

## Mapeamento inicial
### Saúde São Sebastião
Destino: `50-clientes/10-saude-sao-sebastiao/`
Fontes:
- `[F1] 5-Frentes/Saude-Sao-Sebastiao`
- `[F2] memory/saude-sao-sebastiao`
- `[F2] memory/outputs/saude-sao-sebastiao`
- `[F3] PROJETOS/Saude-Sao-Sebastiao`

### Câmara Municipal
Destino: `50-clientes/20-camara-municipal/`
Fontes:
- `[F1] 5-Frentes/Camara-Municipal`

### SINDSS
Destino: `50-clientes/30-sindss/`
Fontes:
- `[F1] 5-Frentes/SINDSS`

### Outros Vereadores
Destino: `50-clientes/40-outros-vereadores/`
Fontes:
- `[F1] 5-Frentes/Outros-Vereadores`

### Outros Clientes
Destino: `50-clientes/50-outros-clientes/`
Fontes:
- `[F1] 5-Frentes/Alem-da-Foto`
- `[F1] 5-Frentes/Lives-Louvor-Reflexao`
- `[F1] 5-Frentes/Logika-Creative/Clientes`

## Próximo passo
Migrar primeiro Saúde São Sebastião, porque é a frente com maior volume e maior risco de mistura contextual.

## Como desfazer
Remover os índices criados em `50-clientes/` e manter fontes legadas intactas. Nenhum arquivo legado foi movido neste lote.
