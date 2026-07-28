---
tipo: liberacao
data: 2026-07-07
status: concluido
agente: Lôh
responsavel: Warren
assunto: Liberação de escrita no Drive pessoal para organização de comprovantes
---

# Liberação — Drive pessoal (davijadielson@gmail.com) com escopo de escrita

## Motivo

Warren precisava criar pastas e fazer upload de 7 comprovantes de julho no Drive pessoal de Jadielson, mas o token OAuth estava configurado apenas com escopo **readonly** (Drive), resultando em erro `403 insufficientPermissions`.

## O que foi feito

1. **Removido** o token antigo (readonly) da conta pessoal
2. **Reautorizado** via Google OAuth com `--drive-scope="full"` (Drive full access)
3. **Confirmado** — criação de pasta bem-sucedida ✅
4. **Atualizado** o `gog-auth.sh` para refletir o novo escopo

## Escopos agora autorizados para pessoal

- 📧 Gmail (modify)
- 🗂️ Drive (full)
- 📅 Calendar
- 📄 Docs / 📊 Sheets

## Regra aplicável

> Conforme política do ecossistema: Warren e demais agentes **podem criar e editar**, mas **NUNCA excluir** sem revisão humana. Máximo: mover para lixeira/quarentena.

## Destino dos comprovantes

```
FINANCEIRO / 2026 / 07-Julho / 02-Comprovantes-Pagos
```

Os 7 comprovantes de julho já estão prontos no Cofre, organizados e validados pelo Warren.

## Comando para Warren

```bash
gog_drive pessoal mkdir "2026" --parent <ID_FINANCEIRO>
gog_drive pessoal mkdir "07-Julho" --parent <ID_2026>
gog_drive pessoal mkdir "02-Comprovantes-Pagos" --parent <ID_07-Julho>
# Upload dos comprovantes...
```

Fonte: Lôh (decisão técnica), Cofre (gog-auth.sh), Google OAuth API.