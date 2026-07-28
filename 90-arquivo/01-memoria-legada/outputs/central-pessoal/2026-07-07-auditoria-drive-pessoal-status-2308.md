---
tema: 07 07 auditoria drive pessoal status 2308
atualizado_em: 2026-07-22
---

# Status — Auditoria Drive pessoal 23:08 UTC

**Data:** 2026-07-07 23:08 UTC  
**Agente:** Alfred / Central Pessoal  
**Conta:** `davijadielson@gmail.com`

## Situação atual

A varredura completa de permissões dos **3.378 itens** foi concluída.

## Processamento

- Itens esperados: **3.378**
- Itens com permissões processadas: **3.378**
- Restantes: **0**
- Erros históricos registrados: **66**
- Erros ainda não resolvidos: **0** — os IDs que tinham erro aparecem posteriormente nos resultados processados.

## Achados de compartilhamento

Foram encontrados achados de compartilhamento público/externo no arquivo:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/permissoes_todos_achados.csv`

A lista contém itens `anyoneWithLink` e itens compartilhados com `logikacreative.mkt@gmail.com`.

Principais achados:

- Vários ePUBs em `EBOOKs/` com `anyoneWithLink` como leitor.
- `PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA` com `anyoneWithLink` como leitor.
- `BRIEFING PARA IDENTIDADE VISUAL` compartilhado com `logikacreative.mkt@gmail.com` como editor.
- `Rapidinho: Me Conta do Seu Negócio!` com `anyoneWithLink` como editor e também compartilhado com `logikacreative.mkt@gmail.com` como editor.
- `PROPROSTA PRESTAÇÃO DE SERVIÇO 02` com `anyoneWithLink` como leitor.

## O que ainda falta

A auditoria técnica/inventário já está concluída. Falta apenas a etapa de **consolidação editorial/final**:

1. Corrigir/normalizar o CSV de achados de permissões para incluir cabeçalho.
2. Produzir o relatório final executivo da auditoria.
3. Transformar achados em plano de ação priorizado.
4. Separar recomendações em:
   - corrigir compartilhamentos;
   - revisar LÓGIKA dentro do Drive pessoal;
   - organizar estudos/cursos;
   - deduplicar candidatos;
   - proteger sensíveis pessoais.
5. Submeter qualquer ação prática a Jadielson antes de executar.

## Segurança

Nenhuma alteração foi feita no Google Drive. Tudo permaneceu em modo leitura.

Fonte: Cofre + Google Drive via `gog` OAuth direto.
