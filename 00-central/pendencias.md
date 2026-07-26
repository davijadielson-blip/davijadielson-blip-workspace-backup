---
tema: pendências centrais do Cofre
conteudo: lista de pendências estruturais, auditorias e reorganizações aguardando decisão ou execução
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança do Cofre
cliente: Jadielson Davi
tipo: pendências
prioridade: alta
atualizado_em: 2026-07-26
usar_quando: acompanhar o que falta decidir, revisar ou executar na reorganização do Cofre
nao_usar_quando: registrar decisões finais; use 00-central/decisoes.md
---

# Pendências centrais

## Reorganização do Cofre
- [ ] Jadielson aprovar/ajustar a estrutura-alvo.
- [ ] Definir se a nova estrutura numérica substituirá gradualmente os fluxos `[F0]`–`[F3]` ou se funcionará como camada de governança sobre eles.
- [ ] Auditar arquivos `.md` sem YAML frontmatter e corrigir em lotes pequenos.
- [ ] Auditar arquivos não-`.md` dentro do Cofre e decidir destino seguro (Google Drive, arquivo externo ou quarentena), sem apagar.
- [ ] Consolidar duplicidades de pastas (`memory/` vs `[F2] memory/`; `[F2] agentes` vs `[F2] memory/agents`; pastas com escape literal `\[F0\]`, `\[F2\]`).
- [ ] Criar política final de acesso por agente e por área.

## Próximo lote recomendado
- [ ] Lote 3: consolidar pastas duplicadas de memória (`memory/`, `[F2] memory/`, `[F2]memory/`, `\[F2\] memory/`) com plano de movimentação reversível.
- [ ] Lote 4: separar clientes/frentes em `50-clientes/` com índices por cliente.
- [ ] Lote 5: isolar arquivos não-.md sensíveis/técnicos conforme classificação.
