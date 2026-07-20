# Pedido à Lôh — Avaliação técnica do Mission Control Backlog Inteligente

**Data:** 2026-07-20  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Solicitante:** Jadielson Davi  
**Preparado por:** agente temático do tópico Backlog Inteligente.

## Contexto

Jadielson perguntou se seria possível criar um Mission Control/aplicativo no estilo das telas enviadas, com matriz Eisenhower, matriz esforço x impacto, cadastro inteligente de tarefas, agenda, backlog, projetos e organização com IA.

Foi criado o blueprint inicial:

`[F2] memory/projects/backlog-inteligente/mission-control-blueprint-mvp-v1-2026-07-20.md`

## Pedido para Lôh

Avaliar arquitetura técnica e viabilidade de integração para um possível Mission Control do Backlog Inteligente, considerando:

1. xTiles como protótipo visual e/ou fonte operacional.
2. Cofre como fonte de verdade/memória em Markdown.
3. Google Calendar via `gog` como camada de compromissos e blocos.
4. Possível API/MCP/export do xTiles.
5. Segurança/autenticação.
6. Parede-d'água entre vida pessoal e LÓGIKA/clientes.
7. Caminho evolutivo: xTiles MVP → Cofre estruturado → Calendar → app próprio.

## Restrições

- Não iniciar desenvolvimento pesado sem validação de uso real.
- Não duplicar alimentação manual entre xTiles e Cofre.
- Não usar Zapier para Google.
- Salvar no Cofre apenas `.md`; brutos/documentos ficam no Drive.

## Resultado esperado

Uma recomendação arquitetural com:

- stack sugerida, se app próprio fizer sentido;
- estratégia de sincronização;
- limites do xTiles;
- o que testar primeiro;
- riscos técnicos;
- próximos passos aprováveis por Jadielson.
