# [F2] — FLUXO 2: SISTEMA (Segundo Cérebro)

**O que significa:** Inteligência do sistema. Segundo cérebro dos agentes. Contexto, decisões, outputs, definições.

**Agentes:** Gerenciam livremente — escrevem, leem, atualizam. É o playground do sistema.

**Jadielson:** Valida e aprova o que o sistema produz. Não edita diretamente.

**Pastas neste fluxo:**

| Pasta | Conteúdo |
|---|---|
| `memory/` | **Coração do sistema** — contextos, decisões, outputs, templates, projetos, sessões |
| `agentes/` | Definições e prompts de cada agente |
| `archive/` | Histórico, backups, material legado |
| `vaults/` | Clone do repositório GitHub (sincronização) |
| `scripts/` | Automação (não editar) |
| `skills/` | Módulos de habilidade (não editar) |

## 🧠 REGRA: Workspace é o CÉREBRO CENTRAL

**Antes de qualquer resposta, TODO agente DEVE:**

1. **Consultar o workspace inteiro primeiro** — não só `[F2] memory/`. O contexto relevante pode estar em `[F1]`, `[F3]` ou qualquer outra pasta. O workspace é sua base de conhecimento primária.
2. **Buscar na web (via Tavily) só depois** — quando o workspace não tiver a resposta. Tavily é complementar, nunca substituto.
3. **Registrar tudo que for pertinente** — informações novas, decisões, aprendizados, contextos relevantes encontrados → salvar em `[F2] memory/context/` ou no arquivo do dia. Se não for salvo, não existiu.
4. **Aprender entre sessões** — memória não sobrevive a restart. Use `[F2] memory/` como ponte. Registre descobertas, ajustes de comportamento, e regras para o futuro.
5. **"Não consegui" é melhor que inventar** — se o workspace não tem a resposta E a web não ajudou, diga claramente. Não alucine.