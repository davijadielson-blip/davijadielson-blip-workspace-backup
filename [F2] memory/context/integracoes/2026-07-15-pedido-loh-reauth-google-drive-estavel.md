# Pedido para Lôh — reautorização Google Drive estável

**Data:** 2026-07-15 15:17 UTC  
**Solicitante:** Jadielson  
**Frente:** CFO / Finanças & Caixa + integração Google Workspace

## Pedido do Jadielson

Jadielson perguntou o que é necessário para reautorizar e pediu que a Lôh corrija de forma mais estável, para não precisar refazer com tanta frequência — idealmente, no máximo uma vez por ano, em janeiro.

## Sintoma atual

Chamadas `gog` para Drive retornaram:

`invalid_grant — Token has been expired or revoked`

Contas afetadas/testadas:
- `davijadielson@gmail.com` — Drive pessoal, usado para comprovantes pessoais/domésticos.
- `logikacreative.mkt@gmail.com` — Drive da empresa, deve receber comprovantes empresariais/LÓGIKA.

## Regra operacional financeira confirmada

- Comprovantes da empresa/LÓGIKA → Drive da empresa (`logikacreative.mkt@gmail.com`).
- Comprovantes pessoais/domésticos → Drive pessoal (`davijadielson@gmail.com`).
- Em caso de dúvida, perguntar antes de subir.

## Correção solicitada à Lôh

Reautorizar e estabilizar OAuth/`gog` para evitar expiração semanal/recorrente:

1. Verificar se o OAuth client/projeto Google usado pelo `gog` está em modo **Testing**. Se estiver, refresh tokens podem expirar em poucos dias; mover para **Production** quando adequado.
2. Garantir escopos corretos:
   - Empresa (`logikacreative.mkt@gmail.com`): Drive com escrita/upload para comprovantes empresariais; Docs/Sheets se necessário; Gmail sem envio.
   - Pessoal (`davijadielson@gmail.com`): Drive com escrita/upload para financeiro pessoal; Calendar conforme já autorizado; Gmail sem envio.
3. Executar reauth via `gog auth add ... --force-consent --remote` para gerar novo refresh token válido.
4. Validar com smoke tests não destrutivos:
   - `drive search` em ambas as contas.
   - upload pequeno de teste em pasta controlada ou pasta já autorizada, sem excluir nada.
5. Documentar no Cofre data da reautorização, escopos e próxima revisão programada para janeiro.

## Comandos de referência já usados no Cofre

```bash
gog auth add logikacreative.mkt@gmail.com --services drive,docs,sheets,forms --drive-scope full --force-consent --remote --step 1 --timeout 10m

gog auth add davijadielson@gmail.com --services drive,calendar --drive-scope full --force-consent --remote --step 1 --timeout 10m
```

Após receber a URL/autorização final, completar com `--step 2 --auth-url '<URL_FINAL>'` conforme fluxo do `gog`.

## Pendência imediata

Depois da correção, espelhar o comprovante recente pendente no Drive correto conforme natureza da despesa:
- `2026-07-15__AGUA-MINERAL__manoel-m-santos__R-18-00__PAGO.jpg`
