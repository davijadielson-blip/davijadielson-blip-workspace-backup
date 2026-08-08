---
tema: prompt em quarentena para atualizacao da skill Saude v1.3
conteudo: prompt operacional recebido em runtime para atualizar a skill saude-sao-sebastiao-comunicacao, preservado para revisao governada
setor: governanca de skills
cliente: Jadielson Davi
tipo: proposta em quarentena
prioridade: media
atualizado_em: 2026-08-08
usar_quando: revisar historico e requisitos da proposta de atualizacao da skill Saude v1.3
nao_usar_quando: executar alteracao de skill sem Skill Workshop ou autorizacao explicita
---

# Prompt para atualizar a skill da Saúde para v1.3

Atualize a skill `saude-sao-sebastiao-comunicacao` para a versão 1.3 usando o pacote fornecido.

## Regras da operação

1. Trabalhe somente dentro do ecossistema já existente.
2. Faça backup integral da versão ativa antes da substituição.
3. Não altere o cofre da Saúde, exceto para registrar tecnicamente a versão instalada, caso esse registro já exista no padrão do workspace.
4. Não crie memória paralela.
5. Preserve o nome da skill e seus bindings.
6. Valide a estrutura e compare os arquivos antes de aplicar.
7. Use o Skill Workshop, se estiver disponível e configurado, para criar uma proposta governada; caso não esteja disponível, aplique a substituição local com backup e diff.
8. Reinicie o Gateway com segurança somente se o watcher não carregar a nova versão.
9. Execute os testes de `references/ACCEPTANCE_TESTS.md`.
10. Entregue um relatório final com:
   - caminho instalado;
   - versão anterior;
   - versão nova;
   - backup criado;
   - arquivos alterados;
   - resultado de cada teste;
   - falhas ou pendências.

## Mudanças obrigatórias

- Nunca gravar aprendizado no cofre apenas porque uma legenda foi aprovada.
- Apresentar proposta e aguardar autorização explícita.
- Separar fontes factuais de fontes editoriais.
- Usar trilha de auditoria em vez de revelar raciocínio interno.
- Mostrar métricas de pesquisa somente quando realmente obtidas.
- Não anunciar fontes em toda resposta comum.
- Perguntar os dados mínimos quando a peça for destinada à publicação.
- Evitar clichês e construções genéricas com “cara de IA”.
- Manter o Drive pessoal fora do escopo da Saúde.
