---
tema: 07 07 auditoria drive pessoal status inicial
atualizado_em: 2026-07-22
---

# Auditoria inicial — Google Drive pessoal

**Data:** 2026-07-07 04:59 UTC  
**Agente:** Alfred / Central Pessoal  
**Conta auditada:** `davijadielson@gmail.com`  
**Método:** autenticação direta `gog` / Google OAuth convencional  
**Zapier:** não utilizado  
**Modo:** leitura/inventário; nenhuma exclusão ou movimentação realizada

## Status executivo

A auditoria foi retomada com sucesso pelo caminho convencional (`gog`). O acesso ao Drive pessoal funcionou e foi possível inventariar a raiz e as pastas principais em modo leitura.

O navegador foi testado, mas permanece inadequado para a auditoria: perfil `user` não anexou e perfil `openclaw` estava em tela de login/timeout. O caminho efetivo e recomendado para este trabalho é `gog`.

## Inventário coletado

Arquivos salvos no Cofre:

- Inventário da raiz: `[F2] memory/outputs/central-pessoal/drive-pessoal-root-depth1-2026-07-07.json`
- Inventários por pasta raiz: `[F2] memory/outputs/central-pessoal/drive_pessoal_lotes_2026-07-07/`
- CSV consolidado: `[F2] memory/outputs/central-pessoal/drive-pessoal-inventory-consolidado-2026-07-07.csv`
- Resumo estruturado: `[F2] memory/outputs/central-pessoal/drive-pessoal-auditoria-summary-2026-07-07.json`

## Números iniciais

- Itens totais inventariados, incluindo pastas raiz: **3.378**
- Pastas: **610**
- Arquivos: **2.768**
- Pastas raiz encontradas: **16**
- Tamanho conhecido reportado: **~502,9 GB**
- Proprietário dos itens inventariados: **davijadielson@gmail.com**

## Pastas raiz encontradas

1. `01_PROJETOS` — 0 itens internos detectados
2. `02_FOTOS_SOLTAS` — 0 itens internos detectados
3. `03_LOGIKA_NEGOCIO` — 0 itens internos detectados
4. `04_PESSOAL` — 1.062 itens internos
5. `05_OUTROS` — 0 itens internos detectados
6. `CONTADOS CELULAR` — 3 itens internos
7. `ESTUDOS` — 2.218 itens internos
8. `EXCEL  e SHEETS` — 11 itens internos
9. `FINANCEIRO` — 12 itens internos
10. `FORMULÁRIOS` — 3 itens internos
11. `Google Earth` — 1 item interno
12. `PDF's` — 6 itens internos
13. `PERFIL DA EMPRESA LÓGIKA CREATIVE` — 43 itens internos
14. `POWER POINT` — 1 item interno
15. `PRODUTIVIDADE` — 1 item interno
16. `PROPOSTAS` — 1 item interno

## Distribuição por tipo de arquivo

Principais tipos detectados:

- PDF: **494**
- MP4: **443**
- MP3: **344**
- JPEG/JPG: **336**
- ZIP: **329**
- MOV/QuickTime: **108**
- HTML: **78**
- Markdown: **64**
- HEIF: **64**
- ARW/Sony RAW: **64**
- EPUB: **61**
- PNG: **52**

## Leituras iniciais

### 1. O Drive pessoal tem forte concentração em estudos/cursos
A maior massa está em `ESTUDOS`, especialmente cursos, vídeos, ebooks e pacotes compactados. Há muitos arquivos grandes e possíveis duplicações em materiais de curso.

### 2. Vida pessoal está concentrada em `04_PESSOAL`
A pasta `04_PESSOAL` tem mais de mil itens, incluindo subáreas como `JADIELSON`, fotos, ebooks, rotinas e materiais pessoais. Essa pasta merece uma segunda passada mais qualitativa.

### 3. Há mistura com LÓGIKA dentro do Drive pessoal
Foram encontrados pelo menos **77 itens/caminhos** com indícios de LÓGIKA/empresa/creative/cliente, incluindo:

- `PERFIL DA EMPRESA LÓGIKA CREATIVE`
- `PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA`
- `Diagnóstico Estratégico - Lógika Creative`
- `BRIEFING PARA IDENTIDADE VISUAL`
- formulários e respostas associados a negócio/identidade visual

Recomendação: não mover nada agora; apenas separar em relatório uma lista de candidatos a migração/espelhamento para frente LÓGIKA após validação humana.

### 4. Há sinais de duplicidade/repetição
Exemplos fortes:

- `LEIA-ME.pdf` aparece em 26 ocorrências.
- `Roube Como Um Artista - Austin Kleon.epub` aparece em múltiplas cópias.
- Pacotes `TRILHAS RETIRADAS DA PLATAFORMA...zip` aparecem repetidos, com arquivos de aproximadamente 2 GB.

Recomendação: criar uma etapa específica de deduplicação **somente com lista de candidatos**, sem exclusão automática.

### 5. Financeiro já tem estrutura recente
A pasta `FINANCEIRO` existe e contém estrutura recente de 2026/07-Julho/02-Comprovantes-Pagos, incluindo comprovantes organizados pelo Warren.

### 6. Existem arquivos potencialmente sensíveis
Busca por termos como CPF/RG/identidade/senha/contrato/banco/cartão apontou **23 ocorrências candidatas**. Ainda não abri conteúdo; apenas sinalizei por nome/caminho. Próxima etapa deve classificar sensibilidade com cuidado.

## Limitações desta rodada

- Ainda não foi feita leitura profunda do conteúdo dos arquivos.
- Ainda não foi extraído relatório de permissões/compartilhamentos item a item.
- O navegador não ficou estável; a coleta confiável ocorreu via `gog`.
- O inventário é metadado estrutural: nome, caminho, tipo, ID, tamanho quando disponível, proprietário e modificação.

## Próximas etapas recomendadas

1. Gerar mapa qualitativo da pasta `04_PESSOAL`.
2. Gerar mapa qualitativo da pasta `ESTUDOS`, separando cursos, ebooks, mídias e duplicatas pesadas.
3. Criar lista de candidatos de LÓGIKA dentro do Drive pessoal para revisão humana.
4. Criar relatório de duplicatas prováveis, sem excluir nada.
5. Verificar permissões/compartilhamentos dos itens sensíveis e pastas principais.
6. Propor uma árvore-alvo de organização pessoal, sem executar mudanças até autorização.

## Regra de segurança aplicada

Nenhuma exclusão, movimentação, renomeação ou alteração foi feita. A auditoria permaneceu em modo leitura.

Fonte: Cofre (`AGENTS.md`, `MAPA.md`, registros de integração `gog`), Google Drive via `gog` OAuth direto.
