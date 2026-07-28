---
tipo: decisao
data: 2026-07-07
status: implementado
fonte: Lôh + Jadielson
assunto: Desativação dos apps Google no Zapier (conflito com gog)
---

# Decisão — Desativar Google via Zapier (conflito com autenticação direta)

## Motivo

O Zapier MCP estava em conflito com a autenticação direta via `gog` (Google OAuth nativo). Jadielson reportou que estava "dando conflito" — provavelmente duplicidade de ações, tokens concorrentes ou comportamento imprevisível ao acessar Google Drive/Gmail/Calendar por dois caminhos diferentes.

## Decisão

✅ **Desativar TODOS os apps Google do Zapier MCP**, mantendo apenas os apps não-Google (Facebook, Instagram, YouTube via Zapier separado).

## O que foi desabilitado

### Zapier 1 — removido:
| App | Ações removidas |
|-----|----------------|
| Google Drive | 21 ações |
| Google AI Studio (Gemini) | 9 ações |
| Google Calendar | 13 ações |
| Gmail | 12 ações |

### Zapier 3 — removido:
| App | Ações removidas |
|-----|----------------|
| Google Drive | 21 ações |

### Preservado (sem conflito):
- **Zapier 1:** Facebook Pages, Instagram for Business
- **Zapier YouTube:** YouTube (mantido separado)

## Acesso ao Google agora

Apenas via **autenticação direta `gog`** (já configurado e testado):
- `gog_drive pessoal|logika` para Google Drive
- `gog_gmail pessoal|logika` para Gmail
- Google Calendar via acesso nativo do sistema

## 📋 REGRA PROPAGADA PARA O ECOSSISTEMA

Junto com esta desativação, Jadielson determinou e registrei no `AGENTS.md`:

> **🚫 NENHUM agente pode EXCLUIR nada sem revisão humana explícita.**
> - Podem: criar, editar, mover
> - **Não podem jamais:** excluir/apagar
> - Máximo: mover para pasta de quarentena/revisão

Esta regra foi inserida na seção **Safety** do `AGENTS.md` e vale para todos os agentes, subagentes, skills e automações do ecossistema.

## Próximos passos

- [x] Verificar se YouTube via Zapier continua funcionando sem conflito ✅
- [x] Confirmar que Facebook/Instagram no Zapier 1 estão OK ✅