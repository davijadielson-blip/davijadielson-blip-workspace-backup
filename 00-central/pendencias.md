---
tema: pendencias centrais do Cofre
conteudo: lista atual de pendencias estruturais, revisoes humanas e proximas etapas de limpeza do Cofre
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: pendencias
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: acompanhar o que falta decidir, revisar ou executar na organizacao do Cofre
nao_usar_quando: registrar decisoes finais; use 00-central/decisoes.md
---

# Pendencias centrais

## Revisao humana

- [ ] Revisar, em etapa propria, se `openclaw-workspace-state.json` da raiz deve continuar versionado ou ser tratado como estado tecnico regeneravel.

## Limpeza estrutural restante

- [ ] Fazer curadoria final, por demanda real, dos arquivos classificados como aprovados/rascunhos em frentes de clientes. Motivo: exige leitura de conteudo e, em alguns casos, validacao humana sobre status editorial.
- [ ] Revisar duplicidades internas da Saude somente quando houver divergencia factual entre `fichas-operacionais/`, `servicos-e-competencias/` e `lacunas-a-confirmar/`. Motivo: a navegacao ja foi resolvida por indice; a fusao fina pode alterar contexto editorial.

## Compatibilidade

- [ ] Manter referencias historicas F0/F1/F2/F3 em logs e registros de migracao, mas evitar que aparecam como rota ativa em READMEs, mapas e protocolos.
- [ ] Antes de mover qualquer script, skill, agente, cron ou runtime, verificar referencias com `rg` e registrar origem/destino no relatorio do lote.

## Politica tecnica ativa

- [x] Manter `70-agentes/runtime/*/openclaw-workspace-state.json` fora do Git por padrao. Motivo: sao estado tecnico regeneravel de runtime local.
- [x] Manter `70-agentes/runtime/*/memory/` fora do Git por padrao quando surgir como memoria local nao rastreada. Motivo: pode conter contexto operacional ou sensivel; se algo for util, criar resumo Markdown no Cofre ativo.
- [x] Manter `media/inbound/` fora do Git. Motivo: midias e anexos originais nao sao Markdown, podem conter material sensivel e devem ir para Drive/pasta externa por frente quando forem relevantes.
- [x] Registrar no Cofre apenas Markdown de rastreabilidade para midia/anexo relevante, com YAML frontmatter, resumo, origem, link/ID, status e proximo passo.

## Resolvido em 2026-08-10

- [x] Arquivar os perfis ativos antigos `bibliotecaria` de `.claude/agents/` e `.codex/agents/` em `90-arquivo/30-regras-obsoletas/2026-08-10-agente-bibliotecaria-legado/`, porque contrariavam a autonomia operacional atual.
- [x] Criar indice em `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/README.md`, separando rota ativa, apoio editorial e rastreabilidade.
- [x] Confirmar politica vigente para nao Markdown: midia, binarios, anexos e documentos ficam fora do versionamento por `.gitignore`; no Cofre versionado entra apenas Markdown com sintese, link, status ou referencia.
- [x] Normalizar comandos e perfis ativos em `.claude/` e `.codex/` que ainda usavam persona "bibliotecaria", rotas antigas `[F0]`/`[F1]`/`[F2]` ou conectores Google antigos.
