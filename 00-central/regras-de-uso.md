---
tema: regras centrais de uso do Cofre pelos agentes
conteudo: protocolo local-first, colaboração entre agentes, escrita responsável, fontes, decisões, pendências e handoffs
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança agentiva
cliente: Jadielson Davi
tipo: regras operacionais
prioridade: máxima
atualizado_em: 2026-08-09
usar_quando: antes de qualquer agente responder, pesquisar, decidir, mover arquivo ou passar tarefa adiante
nao_usar_quando: substituir CONSTITUICAO.md, AGENTS.md ou MAPA.md; estes continuam tendo precedência
---

# Regras de uso do Cofre

## 1. Princípio
O Cofre é a fonte primária de verdade do ecossistema. Como ele é alimentado principalmente por agentes, a regra não é bloquear escrita por pasta; a regra é **escrita responsável, rastreável e útil ao time**.

## 2. Ordem obrigatória de busca
1. Consultar o Cofre.
2. Se busca semântica falhar, usar leitura direta: `CONSTITUICAO.md`, `AGENTS.md`, `MAPA.md`, `MEMORY.md`, `memory/*.md`, `00-central/`, `10-pessoal/`, `20-profissional/`, `30-estudos/`, `40-projetos/`, `50-clientes/`, `60-processos/`, `70-agentes/`, `80-handoffs/`, `90-arquivo/`, `scripts/`, `skills/` e pastas relevantes.
3. Se não encontrar, declarar: **“não encontrei no COFRE”**.
4. Só então usar Tavily/Pesquisador ou outra fonte externa necessária.

## 3. Como agentes escrevem no Cofre
Agentes podem criar/editar arquivos em qualquer área quando a tarefa exigir, desde que:
- usem YAML frontmatter;
- citem fontes quando decidirem algo importante;
- separem fato, hipótese e sugestão;
- não tratem rascunho como decisão;
- registrem decisões finais em `00-central/decisoes.md`;
- registrem pendências transversais em `00-central/pendencias.md`;
- registrem passagem de contexto em `80-handoffs/`;
- não apaguem arquivos sem autorização explícita.

Referências `[F0]`, `[F1]`, `[F2]` e `[F3]` são legado técnico/histórico. Não limitam escrita e não orientam salvamento novo.

## 4. Segurança e contexto mínimo
Cada agente deve acessar apenas o contexto necessário para sua função. Dados pessoais, financeiros, saúde, clientes, `.env`, segredos e materiais sensíveis não devem ser compartilhados fora do escopo.

## 5. Fato, hipótese e sugestão
- **Fato:** está registrado em arquivo/fonte consultada.
- **Hipótese:** inferência plausível, ainda não confirmada.
- **Sugestão:** recomendação do agente.

## 6. Padrão de arquivo `.md`
Todo `.md` novo ou editado deve começar com YAML frontmatter, contendo no mínimo `tema` e `atualizado_em`; para arquivos importantes, usar cabeçalho completo.

## 7. Rodapé de fonte
Respostas analíticas, estratégicas, operacionais ou informacionais devem terminar com fonte curta: `Fonte: Cofre (...), Tavily (...), ferramenta específica (...)`.
