---
tipo: skill
nome: parse-captura
trigger: "usuário envia texto livre para captura (Telegram, Claude.ai ou Notion)"
agente-compatibilidade: [claude, openclaw, gpt]
ultimo-update: 2026-05-11
---

# SKILL — parse-captura (Captura Universal)

> Parseia qualquer texto livre e cria uma entrada estruturada no banco 📥 Captura Geral do Notion.
> Funciona via Telegram (cron), Claude.ai (interativo) ou Notion direto.

---

## Trigger

- Usuário envia mensagem de captura via Telegram
- Usuário digita algo como: "captura: reunião com Ceiça sexta 14h SINDSS"
- Script `scripts/cron-jobs/telegram-polling.sh` chama este fluxo automaticamente

---

## Campos do banco Captura Geral

| Campo | Tipo | Obrigatório |
|---|---|---|
| Título | Texto | Sim — extraído da primeira frase |
| Tipo | Select | Inferido: Reunião, Compromisso, Gravação, Edição, Publicação, Tarefa, Captura |
| Frente | Select | Inferido por palavras-chave |
| Data | Date | Inferida: hoje, amanhã, weekday, DD/MM, YYYY-MM-DD |
| Pessoas | Multi-select | Inferidas por nomes conhecidos |
| Status | Select | Sempre "A fazer" na criação |
| Origem | Select | Telegram / Claude.ai / Manual Notion |
| Notas | Texto | Texto original completo |

---

## Procedimento (modo interativo — Claude.ai)

1. Receber texto do usuário
2. Extrair campos com `parse-captura.py` ou manualmente
3. Confirmar com o usuário se ambíguo: "Entendi como Reunião na sexta, 14h, frente SINDSS. Certo?"
4. Criar entrada via Notion MCP (`notion-create-pages` no data source `633e7c8f-db08-48a1-a87c-30c006da539f`)
5. Retornar URL da entrada criada

---

## Regras de inferência

### Tipo
| Keyword | Tipo |
|---|---|
| reunião, meet, call | Reunião |
| gravação, gravar, filmar | Gravação |
| edição, editar, cortar | Edição |
| publicar, post, postar | Publicação |
| compromisso, consulta, médico, visita | Compromisso |
| tarefa, fazer, finalizar, entregar | Tarefa |
| (default) | Captura |

### Frente
| Keyword | Frente |
|---|---|
| saúde, secretaria, sus, psf | Saúde São Sebastião |
| câmara, vereador, sessão, plenária | Câmara Municipal |
| sindss, sindicato, servidor, ceiça | SINDSS |
| rogério, rocha | Rogério Rocha |
| josi, vando, manoel, gongo | Outros Vereadores |
| lógika, logika, agência, audiovisual | Lógika Creative |
| além da foto, documental | ALÉM DA FOTO |
| lives, louvor, gospel | Lives Louvor |
| pessoal, família, eloáh | Pessoal |
| (default) | Geral |

### Data/hora
| Expressão | Resultado |
|---|---|
| hoje | data de hoje |
| amanhã | hoje + 1 |
| segunda/terça/…/domingo | próxima ocorrência |
| DD/MM ou DD/MM/AAAA | data literal |
| 14h, 14h30, 14:30 | horário (DateTimeformat) |

---

## Modo automático (Telegram)

O script `telegram-polling.sh` roda a cada 2 minutos via launchd:
1. Chama `getUpdates` no Bot API
2. Para cada mensagem do chat configurado: chama `parse-captura.py`
3. Salva offset para não reprocessar

---

## Modo Calendar

Entradas com Tipo = Compromisso / Reunião / Gravação e Data preenchida
são automaticamente sincronizadas para o Google Calendar pelo `notion-to-calendar.py`
(roda todo dia às 7h junto com o daily-brief).

---

## Output esperado

```
✅ Capturado: https://notion.so/35d207e6...
```

Ou, no modo interativo, confirmação com link e resumo dos campos interpretados.
