---
tema: protocolo drive brutos cursos
atualizado_em: 2026-07-22
---

# Protocolo — Drive para brutos de cursos e Cofre para aprendizagem

**Data:** 2026-07-14
**Origem:** Tópico Telegram ESTUDOS / Albert
**Solicitante:** Jadielson Davi

## Decisão
Jadielson confirmou que, para cada curso/aprendizado, se ainda não existir pasta correspondente no Google Drive pessoal, o agente de estudos deve criar a pasta e salvar nela os arquivos brutos do curso.

## Regra operacional proposta
1. Ao receber material bruto de curso — PDF, vídeo, áudio, apostila, link exportável, anexo, pacote, ebook ou arquivo relacionado — verificar se já existe pasta do curso em `Drive pessoal > ESTUDOS`.
2. Se existir, usar a pasta existente.
3. Se não existir, criar pasta do curso **dentro da pasta macro `ESTUDOS`**. A pasta macro oficial é sempre `ESTUDOS` no Drive pessoal; subpastas como `CURSOS`, `EBOOKs` ou categorias só podem existir abaixo dela.
4. Salvar no Drive apenas os brutos/originais.
5. Salvar no Cofre as notas organizadas: plano, resumo, checklist, perguntas, flashcards, progresso, revisão e próximos passos.
6. Registrar em nota do Cofre o link/ID da pasta do Drive quando disponível.
7. Manter parede-d'água entre estudos pessoais e LÓGIKA/clientes. Se o curso for diretamente ligado à LÓGIKA ou cliente, escalar para Alfred/Lôh antes de misturar estruturas.

## Status técnico em 2026-07-14
- Drive pessoal está autenticado via `gog`, mas o contexto atual registrado informa escopo `Drive(readonly)`.
- A CLI `gog drive` possui comandos de escrita (`mkdir`, `upload`, `move`), mas a execução real pode exigir reautorização com escopo de escrita.
- Até liberação técnica de escrita, Albert pode: verificar, mapear, orientar, organizar no Cofre e preparar nomes/estrutura; criação/upload no Drive dependerá de escopo write autorizado.

## Caminho base
- Drive: `ESTUDOS/` — pasta macro oficial para brutos de aprendizagem. ID conhecido no inventário: `1v83qc8EBnAtDlKXFpADKg0AiJTqr309G`.
- Cofre: `[F1] ESTUDOS/` e `[F2] memory/context/estudos/` — conhecimento organizado e continuidade.


## Confirmação de Jadielson — pasta macro
Em 2026-07-14, Jadielson confirmou explicitamente: “mas a pasta macro deve ser esta `ESTUDOS`”. Portanto, nenhum curso deve ser criado fora dessa pasta macro no Drive pessoal, salvo autorização explícita posterior.

## Confirmação final
Jadielson pediu para salvar tudo e confirmou a decisão em 2026-07-14. Este protocolo passa a ser a referência operacional para organização de brutos de cursos no Drive pessoal.

## Reforço operacional — 2026-07-19

Jadielson reforçou, após upload do PDF do curso Backlog Inteligente, que o arquivo bruto não deve ficar solto na pasta macro `ESTUDOS` quando não houver pasta específica do curso.

Regra reforçada para Albert e agentes de estudos:

1. Antes de subir qualquer bruto de curso no Drive pessoal, procurar uma pasta específica do curso dentro de `ESTUDOS`.
2. Se a pasta específica não existir, criar uma pasta com nome claro do curso/aprendizado.
3. Subir o bruto dentro da pasta específica do curso, não diretamente na macro `ESTUDOS`.
4. Registrar no Cofre o link/ID da pasta e dos arquivos relevantes.
5. Usar `gog` como caminho oficial para Google Drive; não usar Zapier para Google.

Caso já tenha sido salvo solto por engano, corrigir movendo o arquivo para a pasta específica do curso quando possível.
