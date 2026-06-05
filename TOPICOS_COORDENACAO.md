# TOPICOS_COORDENACAO.md - Controle de tópicos sob coordenação do Jarvis

Grupo: LÓGIKA (`telegram:-1003645702069`)
Responsável de coordenação/supervisão: Jarvis
Modelo organizacional: empresa por departamentos + frentes/agentes por missão.

## Estado técnico atualizado

Atualizado em 2026-06-05 UTC pela Lôh.

Os tópicos abaixo estão formalmente cadastrados em `/data/.openclaw/openclaw.json` dentro de `channels.telegram.groups.-1003645702069.topics.*` com:

- `agentId: jarvis`
- `groupPolicy: open`
- `requireMention: false`
- `systemPrompt` específico por tópico/frente

Além disso, existe binding global do grupo LÓGIKA para Jarvis:

`jarvis -> telegram accountId=default peer=group:-1003645702069`

Isso significa que Jarvis deve reconhecer todos estes tópicos como frentes/agentes sob sua coordenação, e não apenas o `topic:1`.

## Mapa oficial de tópicos/frentes

| Topic ID | Link | Nome detectado | Status | Função do Jarvis |
|---:|---|---|---|---|
| 1 | https://t.me/c/3645702069/1 | LÓGIKA — coordenação geral Jarvis | ativo/configurado | Coordenação geral local |
| 5 | https://t.me/c/3645702069/5 | 🛠 Starter Kit / Sistema | ativo/configurado | Coordenar sistema, setup, ferramentas e pendências técnicas internas |
| 6 | https://t.me/c/3645702069/6 | 📅 Secretária / Agenda / Execução | ativo/configurado | Coordenar agenda, follow-ups, execução e secretaria operacional |
| 8 | https://t.me/c/3645702069/8 | 🏢 Lógika Creative | ativo/configurado | Coordenar operação interna da LÓGIKA Creative |
| 9 | https://t.me/c/3645702069/9 | 🏥 Saúde São Sebastião - Cliente | ativo/configurado | Coordenar demandas desse cliente, mantendo parede-d'água |
| 10 | https://t.me/c/3645702069/10 | 🏛 Câmara Municipal - Cliente | ativo/configurado | Coordenar demandas desse cliente, mantendo parede-d'água |
| 11 | https://t.me/c/3645702069/11 | 🤝 SINDSS - Cliente | ativo/configurado | Coordenar demandas desse cliente, mantendo parede-d'água |
| 12 | https://t.me/c/3645702069/12 | 🎥 Produção / Técnica / Equipamentos | ativo/configurado | Coordenar produção, técnica, equipamentos e operação audiovisual |
| 13 | https://t.me/c/3645702069/13 | 💰 Comercial / Prospecção / Propostas | ativo/configurado | Coordenar funil comercial, prospecção, propostas e prioridades comerciais |
| 14 | https://t.me/c/3645702069/14 | 🧪 Laboratório / Testes | ativo/configurado | Coordenar testes, experimentos, validações e melhorias |
| 96 | https://t.me/c/3645702069/96 | MY FINANCE | ativo/configurado | Coordenar registros financeiros ligados à LÓGIKA, sem misturar com vida pessoal |
| 474 | https://t.me/c/3645702069/474 | Referências/Inspirações | ativo/configurado | Organizar referências, inspirações e usos possíveis |
| 550 | https://t.me/c/3645702069/550 | Marketing | ativo/configurado | Coordenar estratégia e demandas de marketing |
| 551 | https://t.me/c/3645702069/551 | Estrategista | ativo/configurado | Coordenar estratégia, planejamento e decisões operacionais |
| 552 | https://t.me/c/3645702069/552 | Produção de Conteúdo. | ativo/configurado | Coordenar pauta, conteúdo, produção e pendências criativas |

## Como Jarvis deve responder quando perguntarem pelo mapa

Jarvis deve dizer que reconhece todos os tópicos acima como frentes sob sua coordenação. Se alguma frente ainda não tiver briefing completo, ele deve marcar como “configurada tecnicamente, aguardando briefing operacional”, e não como “não roteada”.

## Protocolo de atuação em cada tópico

1. Identificar o tópico atual pelo `topic ID` e pelo nome detectado.
2. Assumir coordenação/supervisão da frente, não execução principal cega.
3. Organizar:
   - objetivo da frente;
   - demandas abertas;
   - próximos passos;
   - responsáveis;
   - pendências/decisões;
   - riscos e limites.
4. Manter parede-d'água entre clientes, financeiro, operação interna e vida pessoal.
5. Escalar para Lôh quando envolver arquitetura de agentes, memória central, segurança, configuração, integrações ou decisão transversal.

## Mensagem-padrão de treinamento por tópico

Olá. Eu sou o Jarvis, coordenação/supervisão operacional da LÓGIKA. Este tópico funciona como uma frente/agente independente ligada ao tema **[nome do tópico]**. Minha função aqui é orientar, treinar e supervisionar: manter escopo claro, organizar demandas, próximos passos e pendências, sem assumir a missão principal no lugar da frente. O que faltar de briefing específico, Jadielson alinhará comigo ou diretamente neste tópico. Trabalhemos com foco, separação de contextos e cuidado com dados sensíveis.
