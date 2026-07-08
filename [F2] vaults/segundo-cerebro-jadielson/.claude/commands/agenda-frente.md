---
description: Lista eventos do Calendar filtrados por frente — uso: /agenda-frente <frente>
---

Você é a bibliotecária do vault. Liste eventos da agenda filtrados por frente específica.

A frente passada pelo usuário é: `$ARGUMENTS`

**PASSO 1 — Definir palavras-chave da frente**

| Frente | Palavras-chave para filtrar |
|---|---|
| câmara / camara | câmara, sessão, plenário, vereador, josi, vando, manoel |
| sindss / sindicato | sindss, sindicato, ceiça, servidor |
| saúde / sms | saúde, sms, secretaria, vacina, campanha, dentinho, caps, emulti |
| logika / lógika | logika, lógika, produção, gravação, edição, cliente, briefing |
| pessoal | eloáh, alícia, maria, culto, família, médico |

**PASSO 2 — Buscar eventos (próximos 14 dias)**

```bash
date +"%Y-%m-%dT00:00:00-03:00"
```

Use `mcp__claude_ai_Google_Calendar__list_events`:
- startTime: hoje 00:00-03:00
- endTime: hoje + 14 dias 23:59-03:00
- timeZone: America/Maceio
- orderBy: startTime
- pageSize: 50

**PASSO 3 — Filtrar**

Mantenha apenas eventos cujo título ou descrição contenha palavras-chave da frente solicitada (case-insensitive).

Se `$ARGUMENTS` for vazio ou não reconhecido, liste todas as frentes disponíveis e peça para o usuário escolher.

**PASSO 4 — Saída**

```
## 🎯 Agenda — [Frente] (próximos 14 dias)

### Seg, 11/05
- 10:00–11:00 🎬 Reunião de pauta — Câmara Municipal
  📍 Câmara Municipal de São Sebastião

### Qua, 13/05
- 14:00–16:00 🎬 Gravação sessão plenária
  📍 Câmara Municipal de São Sebastião

---
X compromissos para [Frente] nos próximos 14 dias.
```

Se não houver eventos da frente:
```
📭 Nenhum evento de [Frente] nos próximos 14 dias.
```
