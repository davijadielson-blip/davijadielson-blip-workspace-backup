---
tema: 07 15 gog auth drive fix
atualizado_em: 2026-07-22
---

# Correção de Autorização Google/gog — Drive
**Data:** 2026-07-15  
**Responsável:** Lôh (orquestração)  
**Status:** ✅ Concluído (pendente publicação do projeto no Google Cloud)

---

## Problema

O Jarvis reportou `invalid_grant — Token has been expired or revoked` ao tentar usar o Google Drive via gog, nas contas:
- **logikacreative.mkt@gmail.com** — Drive da empresa (comprovantes LÓGIKA)
- **davijadielson@gmail.com** — Drive pessoal (comprovantes pessoais)

## Causas Raiz

### 1. Keyring corrompido (CAUSA IMEDIATA)
O keyring do gog usava backend `file` mas a variável `GOG_KEYRING_PASSWORD` **estava vazia** (length 0). Os tokens armazenados estavam criptografados com uma senha anterior e não podiam ser descriptografados.

**Solução aplicada:**
- Configurado keyring `file` com senha fixa via `gog auth keyring file`
- Removidos todos os keyring files corrompidos
- Reimportadas as credenciais OAuth do cliente
- Reautorizadas ambas as contas do zero

### 2. Projeto OAuth estava em "Testing" (CAUSA ESTRUTURAL) ✅ RESOLVIDO
O projeto Google Cloud `logika-openclaw-gog` (client_id: `814986081043-8gjtlblvle38loa4sapdkrqkhkq9l5ef`) estava em **modo Testing**.  
→ **Testing:** refresh tokens expiram em **7 dias** (hard cap do Google)  
→ **Production:** refresh tokens não expiram (a menos que revogados manualmente ou inativos por 6 meses)

**✅ RESOLVIDO em 2026-07-15:** Usuário publicou o app no Google Cloud Console.
- Status: **"Em produção"** (In Production)
- Tipo: **Externo** (External)
- Limite: 0 de 100 usuários (verificação pendente, mas 7-day expiry removido)
- Os tokens gerados hoje **não expiram mais em 7 dias**.

---

## Comandos Executados

### Preparação do keyring
```bash
export GOG_KEYRING_PASSWORD="logika-gog-keyring-2026"
gog auth keyring file
# Removeu keyring corrompido e reimportou credentials
gog auth credentials set /data/.local/share/gogcli/credentials-814986081043-8gjtlblvle38loa4sapdkrqkhkq9l5ef.json
```

### Autorização — logikacreative.mkt@gmail.com (Drive empresa)
```bash
gog auth add logikacreative.mkt@gmail.com \
  --services drive,docs,sheets,forms \
  --drive-scope full \
  --force-consent \
  --remote --step 1 --timeout 10m
# Usuário autorizou via URL → step 2 completado
```

**Escopos autorizados:** Drive (full), Docs, Sheets, Forms  
**Finalidade:** Upload de comprovantes de pagamento, recibos, contratos da LÓGIKA Creative

### Autorização — davijadielson@gmail.com (Drive pessoal)
```bash
gog auth add davijadielson@gmail.com \
  --services drive,calendar \
  --drive-scope full \
  --force-consent \
  --remote --step 1 --timeout 10m
# Usuário autorizou via URL → step 2 completado
```

**Escopos autorizados:** Drive (full), Calendar  
**Finalidade:** Upload de comprovantes pessoais, recibos, documentos financeiros

---

## Testes Realizados

### ✅ Drive Search (ambas as contas)
- logikacreative.mkt: encontrou comprovantes existentes, listou pastas raiz
- davijadielson: encontrou comprovantes pessoais, listou pastas raiz

### ✅ Upload (não destrutivo)
- logikacreative.mkt: arquivo `TESTE-UPLOAD-LOH-*.txt` criado e removido com sucesso
- davijadielson: arquivo `TESTE-UPLOAD-LOH-*.txt` criado e removido com sucesso

### ✅ Doctor passou
- `gog auth doctor`: status OK, 2 tokens legíveis

---

## Próxima Revisão

| Item | Data | Responsável |
|------|------|-------------|
| ✅ Projeto `logika-openclaw-gog` publicado (Production) | **2026-07-15** | Jadielson ✅ |
| Revisão periódica de refresh tokens | **Janeiro/2027** | Lôh |
| Verificação do app Google (se solicitada) | Conforme notificação do Google | Jadielson |

## Instruções para Publicar no Google Cloud

1. Acessar: https://console.cloud.google.com/apis/credentials/consent?project=logika-openclaw-gog
2. Verificar se está "Testing" ou "In production"
3. Se Testing → clicar em "PUBLISH APP"
4. Preencher dados necessários (domínio, política de privacidade)
5. Submeter para verificação (~24-48h)
6. Após aprovação, os refresh tokens **não expiram mais em 7 dias**

## Notas

- O comando `gog config show` falha com `expected "<key>"` porque o config.json está vazio `{}` — isso não afeta o funcionamento, as configurações estão no keyring.
- A variável `GOG_KEYRING_PASSWORD` precisa ser mantida em todos os ambientes (shell, serviços, agente) para o gog funcionar.
- Token `loh.open.logika@gmail.com` também foi removido por estar corrompido; reautorizar se necessário.

### 🔑 Senha Canônica do Keyring

A senha canônica do keyring está armazenada em:
- `/data/.openclaw/credentials/gog/keyring-password`
- `/data/.openclaw/workspace/scripts/.secrets/gog-keyring-password`

**Uso pelos agentes:**
```bash
export GOG_KEYRING_PASSWORD="$(cat /data/.openclaw/credentials/gog/keyring-password)"
```

**Importante:** Sempre usar esta senha, não criar uma ad-hoc. Se a senha mudar, re-exportar e re-importar os tokens via `gog auth tokens export/import`.