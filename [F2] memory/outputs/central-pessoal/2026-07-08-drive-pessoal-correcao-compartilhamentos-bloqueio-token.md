# Correção de compartilhamentos — bloqueio por token Google

**Data:** 2026-07-08 00:31 UTC  
**Agente:** Alfred / Central Pessoal  
**Conta:** `davijadielson@gmail.com`  
**Pedido:** Jadielson autorizou prosseguir com a recomendação após a auditoria do Drive pessoal.

## Ação pretendida

Remover permissões públicas `anyoneWithLink` dos 14 achados de compartilhamento público identificados na auditoria, incluindo:

- ePUBs públicos em `EBOOKs/`
- `PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA`
- `Rapidinho: Me Conta do Seu Negócio!`
- `PROPROSTA PRESTAÇÃO DE SERVIÇO 02`

Arquivo de plano salvo:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/acoes_correcao_compartilhamento_publico_2026-07-08.json`

## Resultado

A correção **não foi aplicada**.

Primeira tentativa sem `--force` foi recusada pelo `gog`, por segurança operacional.

Segunda tentativa com `--force`, com autorização explícita do usuário, falhou em todos os itens por erro OAuth:

`invalid_grant — Token has been expired or revoked`

Arquivo de log salvo:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/resultado_correcao_compartilhamento_publico_FORCE_2026-07-08.json`

## Diagnóstico

O inventário e a auditoria de permissões funcionaram antes, mas no momento da ação mutante (`drive unshare`) o token da conta pessoal não conseguiu renovar/acessar a API.

`gog auth doctor` indicou keyring e tokens legíveis, mas chamada real ao Drive retornou `invalid_grant`.

## Necessidade para prosseguir

Reautorizar a conta `davijadielson@gmail.com` no `gog` com Drive full.

Comando/base usados para gerar URL de reautorização:

```bash
gog auth add davijadielson@gmail.com --services drive,calendar --drive-scope full --force-consent --remote --step 1
```

Foi gerada URL de OAuth com instrução de step 2, mas ela exige intervenção/autorização humana.

## Segurança

Nenhum arquivo foi excluído, movido, renomeado ou teve permissão alterada nesta tentativa.

Fonte: Cofre + Google Drive via `gog` OAuth direto.
