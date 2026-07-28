---
tema: daily briefing
atualizado_em: 2026-07-22
---

# ☀️ Use Case: Daily Briefing

> Acorde todos os dias com um resumo do que precisa de atenção.

## O que faz

Cron automático que roda todo dia de manhã e consolida:
- Agenda do dia (eventos nas próximas 24h)
- Emails urgentes não lidos
- Métricas do negócio (se configurado)
- Redes sociais (performance dos últimos posts)
- Projetos com prazo se aproximando
- Lembretes pendentes

## Prompt para configurar

```
Quero que você crie um Daily Briefing automático que rode todo dia às [HORÁRIO] da manhã.

O briefing deve incluir:
1. 📅 **Agenda** — eventos de hoje e amanhã (Google Calendar)
2. 📧 **Emails** — urgentes não lidos (se Gmail integrado)
3. 📊 **Métricas** — resumo rápido do negócio (se integrado)
4. 📱 **Redes sociais** — performance dos últimos posts
5. 📋 **Projetos** — status dos projetos ativos, alertar prazos próximos
6. ⏰ **Lembretes** — pendências que eu pedi pra lembrar

Formato:
- Máximo 10 linhas — sou ocupado, quero ser rápido
- Se não tem nada urgente, diga "Dia tranquilo 😎" e pronto
- Se tem algo urgente, destaque com ⚠️
- Entregue no [TELEGRAM/WHATSAPP]

Configure como cron com:
- sessionTarget: isolated
- payload: agentTurn
- delivery: announce
- model: Sonnet (não precisa de Opus pra isso)
```

## Exemplo de output

```
☀️ Briefing — Terça 18/02

📅 14h: Call com investidor (Zoom)
📅 17h: Lembrete gravar vídeo YouTube

📊 MRR: R$8.2k (+1.5% semana) ✅
⚠️ 3 failed payments pendentes (R$347)

📱 Post LinkedIn de ontem: 2.3k views, 89 likes — acima da média

📋 Projeto Content Waterfall: 3 peças pendentes de aprovação

Dia produtivo pela frente! 🚀
```
