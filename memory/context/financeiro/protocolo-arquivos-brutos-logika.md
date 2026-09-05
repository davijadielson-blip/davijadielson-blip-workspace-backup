---
tema: protocolo de arquivos brutos financeiros da Logika
conteudo: regra operacional para armazenar comprovantes e arquivos brutos fora do Cofre, mantendo no Cofre apenas texto extraido em Markdown
setor: Logika Solucoes Digitais
cliente: Jadielson Davi
tipo: protocolo financeiro
prioridade: maxima
atualizado_em: 2026-08-08
usar_quando: registrar comprovantes, notas fiscais, recibos, imagens, PDFs ou anexos financeiros da Logika
nao_usar_quando: tratar finanças pessoais ou materiais autorais do Fluxo 1
---

# Protocolo - Arquivos brutos financeiros da Logika

## Regra definida por Jadielson

Em 2026-08-08, Jadielson determinou:

- Nunca salvar arquivos brutos no Cofre para nao pesar no armazenamento.
- O Cofre deve guardar apenas textos extraidos, resumos, metadados, links, IDs e registros em Markdown.
- Arquivos brutos, como imagens, PDFs, comprovantes, notas fiscais, audios e videos, devem ficar no Drive ou em outra origem externa aprovada.
- Quando houver arquivo bruto relevante, criar ou atualizar um `.md` no Cofre com:
  - descricao do arquivo;
  - dados extraidos;
  - status;
  - link/ID do Drive quando existir;
  - observacao de que o bruto nao esta armazenado no Cofre.

## Aplicacao imediata

- Registros financeiros da Logika devem continuar em `00-central/inbox/externa/financeiro/empresa/`.
- Comprovantes originais devem ir para o Drive empresarial `logikacreative.mkt@gmail.com`.
- Se um bruto entrar temporariamente durante processamento, ele deve ser removido do Cofre ao final da rotina, sem exclusao definitiva sem revisao humana.

## Fonte

- Pedido de Jadielson no topico Telegram `CFO - Financas & Caixa`, em 2026-08-08: "NUNCA SALVE OS ARQUIVOS BRUTOS NO COFRE PARA NAO PESAR NO ARMENZAMENTO. APENAS EXTRAIR TEXTOS E CONVERTER EM MARKDOWN".
- MAPA do Cofre ja define que somente Markdown vai para o Cofre e demais arquivos vao para Drive/origem externa aprovada.
