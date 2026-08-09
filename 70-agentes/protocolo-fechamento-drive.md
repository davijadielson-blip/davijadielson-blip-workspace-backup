---
tema: protocolo de fechamento de tarefas com arquivos no Drive
conteudo: regra operacional para agentes salvarem entregaveis no Google Drive e reportarem link antes de encerrar tarefas
setor: governanca agentiva, operacoes, producao
cliente: Jadielson Davi
tipo: protocolo-operacional
prioridade: alta
atualizado_em: 2026-08-09
usar_quando: qualquer agente concluir tarefa que gere arquivo, midia, documento, planilha, roteiro, briefing, relatorio ou entregavel externo
nao_usar_quando: respostas simples em chat que nao gerem arquivo nem entregavel a preservar
---

# Protocolo de Fechamento no Drive

## Regra principal

Nenhuma tarefa com arquivo ou entregavel externo deve ser marcada como concluida enquanto o agente nao confirmar onde o material ficou salvo.

## Checklist obrigatorio

1. Identificar se a tarefa gerou arquivo, midia, documento, planilha, relatorio, briefing, roteiro, arte, render ou qualquer entregavel que precisa persistir.
2. Salvar o arquivo no destino correto:
   - materiais profissionais da Logika/clientes: Google Drive profissional `logikacreative.mkt@gmail.com`;
   - materiais do proprio ecossistema, contexto e decisoes: Cofre em `/data/.openclaw/workspace/`;
   - materiais pessoais: somente quando a tarefa pedir claramente e dentro do escopo pessoal autorizado.
3. Para Google Drive, usar `gog` oficial carregando o ambiente:

```bash
cd /data/.openclaw/workspace
source scripts/gog-auth.sh
gog_drive logika upload <arquivo-local> --parent <folder-id>
```

Para materiais pessoais autorizados:

```bash
cd /data/.openclaw/workspace
source scripts/gog-auth.sh
gog_drive pessoal upload <arquivo-local> --parent <folder-id>
```

4. Conferir o arquivo no Drive com `gog_drive <conta> get <file-id>` ou busca pelo nome do arquivo.
5. Reportar no fechamento:
   - nome do arquivo;
   - conta do Drive usada;
   - pasta/destino;
   - link do Drive;
   - status: salvo, pendente de revisao ou bloqueado.

## Se o agente nao souber a pasta correta

Nao declarar concluido como final. O agente deve:

1. extrair e salvar no Cofre apenas o que for pertinente em `.md`: resumo, metadados, texto extraido, status, origem, pendencia e proximo passo;
2. manter o arquivo bruto fora do Git e fora do destino canonico do Cofre quando possivel;
3. pedir roteamento para Lôh/Jarvis com nome do arquivo, frente, cliente e sugestao de destino;
4. assim que o `gog` estiver disponivel, subir o arquivo ao Drive correto, atualizar o `.md` com link/ID e remover o status de pendente;
5. se nao houver acesso ao Drive, fechar como `pendente de Drive`, nunca como `concluido`.

## Proibicoes

- Nao apagar arquivos locais nem do Drive para corrigir a falha.
- Nao usar Zapier.
- Nao declarar "concluido" apenas porque o texto foi respondido no chat.
- Nao usar conta pessoal para frente profissional sem autorizacao explicita.
- Nao manter arquivo bruto permanente no Cofre quando ja existir `.md` pertinente e Drive disponivel.

## Frase padrao de fechamento

`Entregavel salvo: <nome> | destino: <conta/pasta> | link: <url> | pendencias: <nenhuma/ou descricao>.`
