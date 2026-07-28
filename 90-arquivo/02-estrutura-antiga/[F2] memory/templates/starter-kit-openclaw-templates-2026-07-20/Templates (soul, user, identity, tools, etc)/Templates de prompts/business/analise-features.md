---
tema: analise features
atualizado_em: 2026-07-22
---

# 🔧 Use Case: Análise de Features e Roadmap

> Transforme feedback de clientes em roadmap priorizado.

## O que faz

Cruza dados de múltiplas fontes pra priorizar features:
- Pedidos de features no suporte
- Discussões na comunidade
- Análise de concorrentes
- Dados de uso do produto
- Feedback de churn (por que cancelaram)

## Prompt

```
Quero que você me ajude a priorizar o roadmap do meu produto [NOME DO PRODUTO].

Analise estas fontes:
1. Tickets de suporte dos últimos 60 dias — extraia pedidos de features
2. Posts da comunidade — o que as pessoas estão pedindo
3. Motivos de churn — o que faltou pro cliente ficar
4. Concorrentes — features que eles têm e eu não
5. [SE TIVER] Dados de uso — features mais e menos usadas

Me entregue:
1. **Feature requests rankeadas** — por frequência × impacto
2. **Quick wins** — features fáceis de implementar com alto impacto (< 1 semana dev)
3. **Must-have vs nice-to-have** — separar claramente
4. **Comparativo concorrentes** — feature parity, gaps, vantagens
5. **Roadmap sugerido** — próximas 4 semanas, priorizado

Formato: tabela com colunas (Feature | Frequência | Impacto | Esforço | Prioridade).

Use a fórmula: Prioridade = (Frequência × Impacto) / Esforço
```

## Variação: Feedback Loop de Features

```
Configure um cron mensal que:
1. Analisa novos tickets e posts da comunidade
2. Atualiza a lista de feature requests
3. Compara com o roadmap atual
4. Me avisa se alguma feature subiu muito em demanda
5. Salva o histórico pra ver tendências ao longo do tempo
```
