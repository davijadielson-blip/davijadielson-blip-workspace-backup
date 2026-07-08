# Migração Drive pessoal → Drive LÓGIKA — bloqueio de escopo

**Data:** 2026-07-08 01:42 UTC  
**Agente:** Alfred / Central Pessoal  
**Pedido:** Jadielson autorizou prosseguir: “o que for coerente a empresa deve ir para o outro drive”.

## Intenção operacional

Migrar/copiar para o Drive da LÓGIKA os materiais claramente empresariais encontrados no Drive pessoal, sem excluir nada.

## Critério inicial de coerência

Migrar primeiro somente itens de alta confiança:

- Pastas/arquivos com LÓGIKA/LOGIKA/Creative no nome/caminho.
- Formulários e respostas de briefing/diagnóstico comercial.
- Propostas e planilhas de cálculo empresarial.
- Material de identidade visual da LÓGIKA.

Não migrar automaticamente cursos genéricos que apenas citam “empresa”, “cliente” ou “briefing” em contexto educacional.

## Destino pretendido

Drive LÓGIKA (`logikacreative.mkt@gmail.com`), dentro de:

`03_EMPRESA / MIGRADO_DO_DRIVE_PESSOAL_2026-07-08`

## Bloqueio encontrado

Ao tentar criar a pasta destino no Drive LÓGIKA via `gog_drive logika mkdir`, a API retornou:

`Google API error (403 insufficientPermissions): Request had insufficient authentication scopes.`

Isso indica que a conta LÓGIKA está autenticada para leitura/escopos insuficientes, sem permissão OAuth de escrita no Drive.

## O que foi feito

- Nenhum arquivo foi excluído.
- Nenhum arquivo foi movido.
- Nenhum arquivo foi copiado.
- Nenhuma alteração foi aplicada ao Drive nesta etapa.

## Necessidade para prosseguir

Reautorizar `logikacreative.mkt@gmail.com` no `gog` com Drive full.

Comando sugerido:

```bash
gog auth add logikacreative.mkt@gmail.com --services drive,docs,sheets,forms --drive-scope full --force-consent --remote --step 1 --timeout 10m
```

Depois da reautorização, Alfred deve:

1. Criar pasta destino em `03_EMPRESA`.
2. Copiar/migrar somente os itens empresariais de alta confiança.
3. Verificar cópias.
4. Registrar IDs de origem e destino.
5. Só depois discutir limpeza/quarentena dos originais no Drive pessoal.

Fonte: Cofre + Google Drive via `gog` OAuth direto.
