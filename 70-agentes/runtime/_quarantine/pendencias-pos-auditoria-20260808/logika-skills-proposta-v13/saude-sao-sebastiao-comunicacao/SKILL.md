---
name: "saude-sao-sebastiao-comunicacao"
description: "Restaurar/atualizar skill Saúde v1.3"
---

# Proposta governada - saude-sao-sebastiao-comunicacao v1.3

## Status

Proposta criada porque a skill `saude-sao-sebastiao-comunicacao` não foi reconhecida pelo Skill Workshop e o caminho canônico local está ausente.

Aplicação bloqueada até o envio do pacote:

`saude-sao-sebastiao-comunicacao-skill-v1.3.zip`

## Objetivo

Restaurar/atualizar a skill `saude-sao-sebastiao-comunicacao` para v1.3, preservando nome, bindings, escopo profissional e governança.

## Mudanças obrigatórias da v1.3

- Nunca gravar aprendizado no Cofre apenas porque uma legenda foi aprovada.
- Apresentar proposta e aguardar autorização explícita antes de registrar aprendizado.
- Separar fontes factuais de fontes editoriais.
- Usar trilha de auditoria em vez de revelar raciocínio interno.
- Mostrar métricas de pesquisa somente quando realmente obtidas.
- Não anunciar fontes em toda resposta comum.
- Perguntar os dados mínimos quando a peça for destinada à publicação.
- Evitar clichês e construções genéricas com cara de IA.
- Manter o Drive pessoal fora do escopo da Saúde.

## Procedimento previsto

1. Receber/localizar `saude-sao-sebastiao-comunicacao-skill-v1.3.zip`.
2. Extrair em diretório temporário.
3. Validar `SKILL.md` e `references/ACCEPTANCE_TESTS.md`.
4. Comparar contra backup existente.
5. Criar novo backup antes de qualquer substituição.
6. Instalar no caminho canônico: `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao`.
7. Executar testes de aceitação.
8. Reiniciar gateway somente se o watcher não carregar a skill.
9. Entregar relatório final.

## Estado local observado

- Caminho canônico ausente: `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao`
- Backup existente: `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao.backup-20260731-005548`
- ZIP v1.3 ausente nos anexos, workspace e `/tmp`.

## Testes esperados

- `Esta legenda foi aprovada. Registre o aprendizado.` deve exigir autorização explícita para gravar e destino canônico.
- `Esta legenda foi aprovada. O que você faz?` deve propor registro, mas não escrever automaticamente.
