# MAPA — Workspace do Jarvis / LÓGIKA

> Mapa central de navegação do workspace do Jarvis. Use este arquivo para localizar identidade, regras, memória, skills, integrações e frentes operacionais da LÓGIKA.

## Arquivos raiz principais

| Arquivo | Função | Quando ler |
|---|---|---|
| `IDENTITY.md` | Identidade do Jarvis, papel e escopo | Boot / alinhamento de persona |
| `SOUL.md` | Tom, postura e estilo de atuação | Boot / respostas sensíveis |
| `USER.md` | Informações sobre Jadielson Davi e preferências de trabalho | Boot / personalização |
| `AGENTS.md` | Regras operacionais e sequência de boot | Boot / segurança |
| `MEMORY.md` | Memória consolidada de decisões e fatos persistentes | Antes de continuidade e decisões |
| `TOPICOS.md` | Mapa dos tópicos/áreas da LÓGIKA | Roteamento operacional |
| `TOPICOS_COORDENACAO.md` | Coordenação dos tópicos/frentes sob Jarvis | Organização interna |
| `AUTORIZACOES.md` | Autorizações operacionais registradas | Antes de ações externas/sensíveis |
| `GOOGLE_WORKSPACE.md` | Notas e regras de integração Google Workspace | Agenda, Drive, Docs/Sheets/Gmail leitura |
| `INTEGRACOES-MCP-REDES.md` | Integrações e redes/MCP | Antes de mexer em integrações |
| `HEARTBEAT.md` | Rotinas/checagens recorrentes | Autonomia e acompanhamento |
| `MAPA.md` | Este arquivo | Navegação geral |

## Pastas principais

```text
workspace-jarvis/
├── memory/          → Memória operacional, outputs, decisões e registros de continuidade
├── skills/          → Skills do Starter Kit e capacidades modulares
│   ├── starter/     → Jornada/checklists do Starter Kit
│   ├── canais/      → Canais opcionais, incluindo WhatsApp
│   ├── operacional/ → Backup, segurança, rotinas e operações
│   └── planejamento/→ Planejamento, execução e verificação
├── templates/       → Templates do Starter Kit
├── exemplos/        → Exemplos de referência do kit
├── _curso/          → Material didático do Starter Kit / curso
├── media/           → Arquivos de mídia locais gerados/recebidos
└── .audit/          → Trilhas locais de auditoria/execução
```

## Estado das configurações recentes

| Item | Status | Observação |
|---|---|---|
| Starter Kit | Instalado no workspace Jarvis | 19 skills detectadas em `skills/` |
| WhatsApp | Validado em modo read-only/teste | Relink limpo em 2026-06-21; origem `+55 11 95108-0607`; smoke test inbound + resposta controlada OK |
| Telegram | Canal principal operacional | Tópico 5 usado para Starter Kit/Sistema |
| Google Workspace | Autorizado via `gog` conforme regras internas | Usar CLI, não navegador, e sempre com `--account` explícito |
| MAPA.md | Criado | Esta versão inaugura o mapa central do Jarvis |

## Navegação rápida

| Estou buscando... | Onde ir |
|---|---|
| Regras do papel do Jarvis | `IDENTITY.md`, `SOUL.md`, `AGENTS.md` |
| Preferências e contexto de Jadielson | `USER.md`, `MEMORY.md` |
| Frentes/tópicos da LÓGIKA | `TOPICOS.md`, `TOPICOS_COORDENACAO.md` |
| Histórico de decisões e fatos persistentes | `MEMORY.md` e arquivos em `memory/` |
| Skills instaladas | `skills/_registry.md` e `_registry.md` por categoria |
| WhatsApp | `skills/canais/wizard-whatsapp/SKILL.md` + `MEMORY.md` |
| Google Workspace | `GOOGLE_WORKSPACE.md` + instruções de uso do `gog` |
| Materiais do Starter Kit | `_curso/`, `README.md`, `FAQ.md`, `manifesto.md` |

## Regras de atualização

- Atualizar este `MAPA.md` quando surgir pasta principal nova, integração relevante ou mudança estrutural do workspace.
- Não usar o mapa para registrar cada pequena decisão; decisões recorrentes devem ir para `MEMORY.md` ou arquivos específicos em `memory/`.
- Não sobrescrever identidade, regras ou integrações sem autorização explícita de Jadielson.
- Para arquitetura de agentes, memória central, configuração, segurança, integrações e decisões transversais, acionar/encaminhar para Lôh.

---

*Criado em 2026-06-21 por Jarvis, seguindo o Starter Kit OpenClaw v2.5.7.*
