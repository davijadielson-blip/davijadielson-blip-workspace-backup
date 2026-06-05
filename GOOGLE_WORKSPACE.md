# GOOGLE_WORKSPACE.md — Acesso operacional da Clara/Jarvis

Atualizado pela Lôh em 2026-06-05 UTC.

## Estado

A integração Google Workspace está configurada neste ambiente via CLI `gog`.

A Clara/Secretária não deve depender do navegador/Chrome para Google Calendar ou Drive. O navegador pode pedir login e não representa o estado real da integração.

## Contas conectadas

- `davijadielson@gmail.com`
- `logikacreative.mkt@gmail.com`
- `loh.open.logika@gmail.com`

## Escopo autorizado

- Calendar: leitura e escrita sob comando.
- Docs: leitura/criação/edição sob comando.
- Sheets: leitura/criação/edição sob comando.
- Drive: acesso `drive.file`; leitura/busca do que o escopo permitir; sem exclusões sem confirmação explícita.
- Gmail: somente leitura; não enviar e-mail.
- Contacts: leitura quando disponível.

## Como usar

Antes de rodar comandos `gog`, usar:

```bash
export GOG_KEYRING_BACKEND=file
export GOG_KEYRING_PASSWORD="$(cat /data/.openclaw/credentials/gog/keyring-password)"
```

Sempre usar `--account` explícito e, quando houver Gmail no contexto, `--gmail-no-send`.

Exemplos seguros:

```bash
gog --account davijadielson@gmail.com --gmail-no-send calendar events --from now --max 10
```

```bash
gog --account logikacreative.mkt@gmail.com --gmail-no-send drive search "trashed=false" --max 20
```

```bash
gog --account logikacreative.mkt@gmail.com --gmail-no-send docs cat <docId>
```

## Regra de resposta da Clara

Se Jadielson autorizar uma auditoria de Agenda/Drive, Clara deve dizer que a integração existe via `gog` e executar leitura segura quando tiver ferramenta de terminal disponível.

Não responder “não encontrei conector Workspace” sem antes verificar/usar `gog`.

Se a sessão não expuser terminal/exec, responder: “Preciso executar via `gog`/terminal ou acionar a Lôh para rodar a consulta técnica”, em vez de concluir que a integração não existe.
