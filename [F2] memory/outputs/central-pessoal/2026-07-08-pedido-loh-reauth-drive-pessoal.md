# Pedido à Lôh — reautorização Drive pessoal

**Data:** 2026-07-08 00:32 UTC  
**Solicitante:** Jadielson Davi  
**Agente:** Alfred / Central Pessoal

## Contexto

Durante a execução da recomendação pós-auditoria do Drive pessoal, Alfred tentou remover permissões públicas `anyoneWithLink` dos achados de maior risco, mas o `gog` retornou:

`invalid_grant — Token has been expired or revoked`

A correção não foi aplicada. Nenhum arquivo/permissão foi alterado.

## Pedido para Lôh

Reautorizar a conta `davijadielson@gmail.com` no `gog` com Drive full para permitir correção de permissões no Drive pessoal.

## Comando/base técnico

```bash
gog auth add davijadielson@gmail.com --services drive,calendar --drive-scope full --force-consent --remote --step 1
```

Após a reautorização, Alfred deve retomar a lista já salva em:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/acoes_correcao_compartilhamento_publico_2026-07-08.json`

## Observação de segurança

Manter regra: nenhuma exclusão. A ação necessária é apenas remover permissões públicas `anyoneWithLink` dos itens já auditados.
