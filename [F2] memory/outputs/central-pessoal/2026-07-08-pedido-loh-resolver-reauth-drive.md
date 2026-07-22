---
tema: 07 08 pedido loh resolver reauth drive
atualizado_em: 2026-07-22
---

# Pedido à Lôh — resolver reautorização do Drive pessoal

**Data:** 2026-07-08 00:34 UTC  
**Solicitante:** Jadielson Davi  
**Agente:** Alfred / Central Pessoal

## Pedido de Jadielson

Jadielson perguntou se Alfred poderia pedir à Lôh e resolver a reautorização necessária para continuar a correção dos compartilhamentos públicos do Drive pessoal.

## Situação técnica

A correção de permissões públicas do Drive pessoal está bloqueada por OAuth:

`invalid_grant — Token has been expired or revoked`

Ação necessária: reautorizar `davijadielson@gmail.com` no `gog` com Drive full.

## URL de autorização gerada

Foi gerada URL via:

```bash
gog auth add davijadielson@gmail.com --services drive,calendar --drive-scope full --force-consent --remote --step 1 --timeout 10m
```

A saída indicou `state_reused=true` e pediu step 2 com `--auth-url <redirect-url>`.

## Procedimento para Lôh/Jadielson

1. Abrir a URL OAuth gerada pelo comando acima.
2. Fazer login/autorização com `davijadielson@gmail.com`.
3. Copiar a URL final de redirecionamento/erro do navegador.
4. Enviar para Alfred executar o step 2:

```bash
gog auth add davijadielson@gmail.com --services drive,calendar --drive-scope full --force-consent --remote --step 2 --auth-url '<URL_FINAL>'
```

## Depois da reautorização

Alfred deve retomar:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/acoes_correcao_compartilhamento_publico_2026-07-08.json`

Objetivo: remover apenas permissões `anyoneWithLink` dos 14 itens públicos já auditados. Sem excluir, mover ou renomear arquivos.
