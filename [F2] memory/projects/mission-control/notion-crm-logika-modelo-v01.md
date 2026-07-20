# Modelo CRM Notion — Lógika Creative v0.1

**Data:** 2026-07-20 00:23 UTC  
**Status:** modelo pronto; integração real pendente por indisponibilidade de execução Zapier/Notion no momento.  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh

## Objetivo

Criar uma base CRM no Notion para a Lógika Creative, conectável ao Mission Control Web.

## Database recomendado

**Nome:** `CRM — Lógika Creative`

## Propriedades mínimas

| Propriedade | Tipo Notion | Obrigatória | Uso |
|---|---|---:|---|
| Nome | Title | Sim | Nome do lead/cliente |
| Tipo | Select | Sim | Lead, Cliente, Parceiro, Fornecedor |
| Status | Select | Sim | Novo, Em contato, Reunião, Proposta enviada, Negociação, Fechado, Perdido, Pausado |
| Origem | Select | Não | Indicação, Instagram, WhatsApp, Presencial, Cliente atual, Outro |
| Serviço de Interesse | Multi-select | Não | Vídeo, Social Media, Cobertura, Institucional, Tráfego, Automação, Design, Outro |
| Prioridade | Select | Não | Alta, Média, Baixa |
| Valor estimado | Number | Não | Potencial de receita |
| Próxima ação | Text | Sim | Menor ação concreta para avançar |
| Data próxima ação | Date | Não | Prazo de follow-up |
| Responsável | Person/Text | Não | Quem conduz |
| WhatsApp | Phone/Text | Não | Contato |
| Instagram | URL/Text | Não | Perfil |
| Cidade | Text | Não | Localização |
| Observações | Text | Não | Contexto relevante |
| Fonte Cofre | URL/Text | Não | Link/caminho de briefing no Cofre |
| Último contato | Date | Não | Controle comercial |

## Views recomendadas

1. **Pipeline Comercial** — agrupado por Status.
2. **Próximas Ações** — ordenado por Data próxima ação.
3. **Alta Prioridade** — filtro Prioridade = Alta.
4. **Clientes Ativos** — Status = Fechado ou Cliente.
5. **Perdidos/Pausados** — Status = Perdido ou Pausado.

## Regras operacionais

1. Nenhum lead entra sem `Nome`, `Tipo`, `Status` e `Próxima ação`.
2. Toda proposta enviada deve gerar próxima ação com data.
3. Todo cliente fechado deve ter fonte/contexto salvo no Cofre.
4. O Mission Control deve exibir apenas resumo operacional: nome, status, próxima ação e prioridade.
5. Dados sensíveis ou negociações detalhadas devem ficar no Notion/Cofre com cuidado, não em painel público.

## Integração com Mission Control Web

### Fase 1 — Placeholder local

O app exibe modelo e status de integração: `Aguardando conexão Notion`.

### Fase 2 — Conexão

Quando a ação Notion estiver disponível, o app deverá:

- buscar itens do database CRM;
- normalizar campos para cards;
- exibir contagem por status;
- listar próximos follow-ups.

## Status da tentativa de integração

Ações Notion estavam habilitadas no Zapier, mas a execução retornou erro de conta: `insufficient tasks on account`. Portanto, a criação/consulta real no Notion não foi concluída nesta rodada.
