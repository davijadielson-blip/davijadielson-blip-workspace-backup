---
tema: 07 07 auditoria drive pessoal reteste 0500
atualizado_em: 2026-07-22
---

# Auditoria do Drive pessoal — reteste 05:00 UTC

**Data:** 2026-07-07 05:00 UTC  
**Agente:** Alfred / Central Pessoal  
**Conta:** `davijadielson@gmail.com`  
**Método:** `gog` / Google OAuth direto  
**Zapier:** não utilizado  
**Modo:** leitura, sem alterações

## Resultado do reteste

O acesso convencional foi testado novamente e está funcionando.

Comandos confirmaram:

- Conta pessoal autenticada: `davijadielson@gmail.com`
- Escopo Drive disponível via `gog`
- Listagem da raiz do Drive pessoal funcionando
- Auditoria read-only de compartilhamentos funcionando

## Raiz do Drive confirmada

Foram confirmadas 16 pastas raiz:

1. `01_PROJETOS`
2. `02_FOTOS_SOLTAS`
3. `03_LOGIKA_NEGOCIO`
4. `04_PESSOAL`
5. `05_OUTROS`
6. `CONTADOS CELULAR`
7. `ESTUDOS`
8. `EXCEL  e SHEETS`
9. `FINANCEIRO`
10. `FORMULÁRIOS`
11. `Google Earth`
12. `PDF's`
13. `PERFIL DA EMPRESA LÓGIKA CREATIVE`
14. `POWER POINT`
15. `PRODUTIVIDADE`
16. `PROPOSTAS`

## Auditoria inicial de compartilhamento

Arquivo gerado:

`[F2] memory/outputs/central-pessoal/drive-pessoal-sharing-audit-root-depth2-2026-07-07.json`

A auditoria inicial de compartilhamento na raiz/profundidade 2 analisou 57 itens e encontrou **3 achados públicos/anyone-with-link**:

1. `EXCEL  e SHEETS/PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA`
   - Permissão: anyone-with-link
   - Papel: reader
   - Observação: material de LÓGIKA dentro do Drive pessoal.

2. `FORMULÁRIOS/Rapidinho: Me Conta do Seu Negócio!`
   - Permissão: anyone-with-link
   - Papel: writer
   - Observação: atenção maior, pois `writer` para qualquer pessoa com link pode permitir resposta/edição conforme configuração do formulário.

3. `PROPOSTAS/PROPROSTA PRESTAÇÃO DE SERVIÇO 02`
   - Permissão: anyone-with-link
   - Papel: reader

## Observação operacional

Tentativa de auditoria profunda de compartilhamentos em `04_PESSOAL` e `ESTUDOS` é mais lenta, porque exige checagem de permissões item a item. Uma amostra limitada foi iniciada para evitar travamento longo.

## Segurança

Nenhuma exclusão, movimentação, renomeação ou alteração foi feita.

Fonte: Google Drive via `gog` OAuth direto; Cofre (`AGENTS.md`, `MAPA.md`, integração `google_drive_jadielson.md`).
