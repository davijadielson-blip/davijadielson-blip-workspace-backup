---
tipo: decisao
gerado-por: claude
data: 2026-05-10
---

# Decisão: Slash Commands do Vault

## Motivação

Automatizar rotinas recorrentes (daily notes, legendas, posts, manutenção) sem abrir mão da regra de ouro: a IA gera drafts, Jadielson revisa e publica.

## Princípios adotados

1. Todo output nasce em `[F2] claude/outputs/` — nunca direto na pasta da frente
2. Frontmatter padrão em todo arquivo gerado (tipo, frente, gerado-por, comando, revisado, data)
3. Conteúdo publicável gera em paralelo manchete WhatsApp em `outputs/resumos-whatsapp/`
4. Em caso de dúvida, o comando pergunta antes de gerar — nunca presume
5. Toda execução vira log em `[F2] claude/logs/comandos/`

## Exceção aprovada por Jadielson

`/ideia` salva diretamente em `[F1] 5-Frentes/<frente>/Ideias/` — único comando autorizado a escrever fora de `[F2] claude/`. Decisão tomada em 2026-05-10.

## Inventário de comandos

### Tier 1 — Diários

| Comando | Arquivo | Depende de |
|---------|---------|-----------|
| `/hoje` | `hoje.md` | nada |
| `/captura` | `captura.md` | nada |
| `/legenda` | `legenda.md` | `agents/<frente>.md` |
| `/resumo-whats` | `resumo-whats.md` | outputs/legendas/ |
| `/revisar` | `revisar.md` | outputs/ |

### Tier 2 — Por frente

| Comando | Arquivo | Depende de |
|---------|---------|-----------|
| `/roteiro-rogerio` | `roteiro-rogerio.md` | `agents/rogerio.md` |
| `/post-camara` | `post-camara.md` | `agents/camara.md` |
| `/post-sindss` | `post-sindss.md` | `agents/sindss.md` + `databases/calendario-sazonal-sindss.md` |
| `/post-rogerio` | `post-rogerio.md` | `agents/rogerio.md` |
| `/post-logika` | `post-logika.md` | `agents/logika.md` |
| `/post-saude` | `post-saude.md` | `agents/saude.md` + `databases/datas-sazonais/campanhas-saude/` |

### Tier 3 — Estratégicos

| Comando | Arquivo | Depende de |
|---------|---------|-----------|
| `/planejar-semana` | `planejar-semana.md` | `3-Daily/`, `databases/` |
| `/manutencao` | `manutencao.md` | `logs/`, `outputs/` |
| `/sazonal` | `sazonal.md` | `databases/datas-sazonais/` |
| `/aniversariante` | `aniversariante.md` | `databases/aniversariantes/` |
| `/busca` | `busca.md` | vault inteiro |
| `/conecta` | `conecta.md` | vault inteiro |
| `/ideia` | `ideia.md` | `5-Frentes/<frente>/Ideias/` |

## Arquivos de agente criados

`[F2] claude/agents/`: `logika.md`, `saude.md`, `camara.md`, `sindss.md`, `rogerio.md`, `alem-da-foto.md`, `lives.md`

## Dependências pendentes para ativação completa

- `calendario-sazonal-sindss.md` → criado como stub, popular com mais datas ao longo do tempo
- Agentes podem precisar de revisão à medida que as frentes evoluem
