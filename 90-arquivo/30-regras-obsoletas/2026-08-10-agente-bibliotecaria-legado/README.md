---
tema: arquivamento do agente bibliotecaria legado
conteudo: rastreabilidade do arquivamento dos perfis antigos bibliotecaria em Claude e Codex
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: rastreabilidade
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: auditar por que o agente bibliotecaria saiu da rota ativa
nao_usar_quando: orientar a operacao atual do Cofre; use AGENTS.md, MAPA.md e 00-central/mapa-do-cofre.md
---

# Agente bibliotecaria legado

Esta pasta preserva os perfis antigos associados a `bibliotecaria`, retirados da rota ativa em 2026-08-10.

## Origem e destino

- Origem: `.claude/agents/bibliotecaria.md`
- Destino: `90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/bibliotecaria.claude.md`
- Origem: `.codex/agents/bibliotecaria.toml`
- Destino: `90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/bibliotecaria.codex.toml`

## Motivo

Os perfis antigos ainda traziam instrucoes como "IA e bibliotecaria", "nunca move", "nunca renomeia" e rotas baseadas em `[F1]`/`[F2]`, em conflito com a regra atual do Cofre:

- IA autorizada pode manter o Cofre operacionalmente;
- Jadielson continua autoridade final sobre sentido, prioridade, publicacao, envio externo, decisoes sensiveis e exclusao definitiva;
- `[F0]`, `[F1]`, `[F2]` e `[F3]` sao legado tecnico/historico, nao rota operacional.

## Dependencias verificadas

Antes da movimentacao, foi executada busca por `bibliotecaria`, `bibliotecária` e `@bibliotecaria` fora de `90-arquivo/`.

Resultado: as referencias remanescentes estavam em:

- handoff da revisao canonica;
- relatorios da revisao;
- decisoes centrais que revogam a regra antiga;
- memoria historica;
- pendencia central agora resolvida.

Nao foi encontrada dependencia ativa chamando esses arquivos como agente obrigatorio.
