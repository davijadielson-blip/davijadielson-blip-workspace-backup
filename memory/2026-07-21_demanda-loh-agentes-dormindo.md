---
tema: 07 21 demanda loh agentes dormindo
atualizado_em: 2026-07-22
---

# Demanda: Agentes dormindo / economia de créditos OpenRouter

**Data:** 2026-07-21
**Origem:** Jadielson Davi (tópico SAÚDE - SOCIAL MEDIA, msg 7797)
**Recebido por:** Jarvis

## Relato

Jadielson reportou:
1. Consumo elevado de créditos OpenRouter desde 2026-07-20
2. Suspeita de agentes rodando em segundo plano sem necessidade
3. Cota diária do GPT Codex pode ter esgotado, com fallback automático para outros modelos amplificando gastos
4. Solicitação explícita: **"colocar agentes para dormir e só despertar quando forem acionados"**

## Ação necessária (Lôh)

- Avaliar configuração de fallbacks de modelo
- Verificar background tasks / cron jobs que possam estar consumindo créditos
- Implementar política de agentes "dormentes" (só acordam sob demanda)
- Revisar limites de consumo por agente/sessão

## Encaminhamento

Demanda registrada no Cofre para Lôh. Pendente de ação.

## ✅ Resolvido em 24/07/2026

**O que foi feito:**
1. Política de agentes dormentes definida e registrada como decisão permanente
2. Agentes agora SÓ acordam quando requisitados por Jadielson, Lôh ou cron explícito
3. Proibição de despertar em cadeia (agente A não desperta agente B sem passar pela Lôh)
4. Modelo primário corrigido para `openai-codex/gpt-5.5` — OpenRouter só como fallback

**Arquivos registrados:**
- `[F2] memory/decisions/2026-07-24-decisoes.md` — decisões do dia

**Fonte:** Jadielson Davi (24/07/2026, 20:29 UTC, áudio no Telegram)