---
tema: PROTOCOLO HEARTBEAT SEGURO
atualizado_em: 2026-07-22
---

# Protocolo de Heartbeat seguro — Lôh/Jadielson

Natureza: proposta aditiva. Não ativa heartbeat automaticamente.

## Objetivo

Dar proatividade útil sem transformar a Lôh em spam.

## Fase 0 — estado atual

`HEARTBEAT.md` raiz está essencialmente vazio, portanto chamadas periódicas ficam desativadas.

Isso deve ser preservado até Jadielson aprovar ativação.

## Fase 1 — piloto recomendado

Se Jadielson aprovar no futuro:

- Frequência: 1 vez ao dia, manhã.
- Canal: mesmo canal principal de conversa.
- Conteúdo: briefing ultra curto.
- Máximo: 5 itens.
- Se nada importante: silêncio ou “Dia tranquilo” apenas quando solicitado.

## Checks iniciais permitidos

Começar com apenas 1 check por semana:

1. Prioridades e pendências do Cofre.
2. Depois, agenda/cron/lembretes.
3. Depois, conteúdo/clientes.
4. Depois, mensagens/e-mails, se integração estiver clara.

## Anti-spam

Não mandar mensagem se:

- não houver novidade relevante;
- for quiet hour;
- for só confirmação sem valor;
- a informação ainda não foi verificada;
- o usuário não pediu monitoramento daquele tema.

## Modelo de briefing futuro

```md
☀️ Briefing — {data}

1. Prioridade principal:
2. Prazo/risco:
3. Pendência parada:
4. Oportunidade:
5. Próximo passo sugerido:

Fonte: Cofre (...).
```

## Regra de ativação

Não editar `HEARTBEAT.md` para ativar automações sem autorização explícita de Jadielson.
