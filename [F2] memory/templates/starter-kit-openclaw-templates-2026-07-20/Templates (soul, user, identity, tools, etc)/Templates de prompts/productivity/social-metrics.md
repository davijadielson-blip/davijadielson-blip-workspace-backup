---
tema: social metrics
atualizado_em: 2026-07-22
---

# 📱 Use Case: Social Media Metrics Sync

> Todas as métricas de redes sociais num único report.

## O que faz

Puxa dados de todas as plataformas e consolida:
- YouTube: subscribers, views, vídeos com melhor performance
- Instagram: followers, engagement rate, texto vs reels
- LinkedIn: impressions, likes/post avg, crescimento
- X/Twitter: followers, tweets, engajamento
- Comparativo semana a semana

## Prompt para configurar

```
Quero que você monitore minhas redes sociais automaticamente.

Minhas redes:
- YouTube: [CANAL]
- Instagram: [PERFIL]
- LinkedIn: [PERFIL]
- X/Twitter: [PERFIL]

Configure:
1. **Sync diário** (cron às 22h, Sonnet):
   - Puxa métricas atualizadas de todas as plataformas
   - Salva snapshot no banco/arquivo

2. **Report semanal** (segunda às 9h):
   - Comparativo semana atual vs anterior
   - Top 3 posts que mais performaram (com link)
   - Plataforma que mais cresceu
   - Recomendação: onde focar essa semana

3. **Alertas** (imediato):
   - Post viralizando (>5x média de engajamento)
   - Queda brusca de followers
   - Comentário negativo com muito alcance

Use RapidAPI como proxy para Instagram e X (cloud IPs são bloqueados).

Entregue no tópico Métricas do Telegram.
```

## Exemplo real

Métricas da Amora:
- YouTube: 69.8k subs, 1.4M views, 276 vídeos
- Instagram: 52.7k followers, 0.87% ER
- Twitter: 2.3k followers, 338 tweets
- LinkedIn: 247 likes/post avg
- Insight descoberto: Instagram texto > reels (21x mais ER!)
