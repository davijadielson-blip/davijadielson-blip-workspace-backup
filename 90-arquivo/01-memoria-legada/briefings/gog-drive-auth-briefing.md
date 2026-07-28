---
tema: gog drive auth briefing
atualizado_em: 2026-07-22
---

# Briefing — Google/gog Drive Autorização
**Última atualização:** 2026-07-15  
**Validade:** Até janeiro/2027 (próxima revisão)

---

## Resumo para Agentes

O sistema `gog` (Google OAuth CLI, v0.21.0) está configurado com duas contas Google para upload de comprovantes no Drive.

### Contas Autorizadas

| Conta | Escopos | Finalidade |
|-------|---------|------------|
| `logikacreative.mkt@gmail.com` | drive (full), docs, sheets, forms | Comprovantes da empresa LÓGIKA |
| `davijadielson@gmail.com` | drive (full), calendar | Comprovantes pessoais |

### Pré-requisitos para usar gog

```bash
# A variável GOG_KEYRING_PASSWORD é OBRIGATÓRIA
# Usar a senha canônica dos arquivos de secrets
export GOG_KEYRING_PASSWORD="$(cat /data/.openclaw/credentials/gog/keyring-password)"
```

Sem ela, o gog não consegue descriptografar os tokens — retorna erro de keyring.

**⚠️ Não criar senha própria!** Sempre usar a senha canônica dos arquivos:
- `/data/.openclaw/credentials/gog/keyring-password`
- `/data/.openclaw/workspace/scripts/.secrets/gog-keyring-password`

Se a senha mudar, re-exportar e re-importar os tokens:
```bash
export OLD="senha-antiga"
export NEW="$(cat /data/.openclaw/credentials/gog/keyring-password)"
GOG_KEYRING_PASSWORD=$OLD gog auth tokens export email@ --out /tmp/token.json
GOG_KEYRING_PASSWORD=$NEW gog auth tokens import /tmp/token.json
```

### Comandos Úteis

```bash
# Upload de arquivo para a raiz do Drive da empresa
gog drive -a logikacreative.mkt@gmail.com upload caminho/do/arquivo.pdf

# Upload com nome personalizado
gog drive -a logikacreative.mkt@gmail.com upload recibo.pdf --name "2026-07-15_comprovante_pix_servicoX.pdf"

# Upload em pasta específica (parent folder ID)
gog drive -a logikacreative.mkt@gmail.com upload recibo.pdf --parent 1U6us-zXwjjAExu321JdLIakiypE-PFU9

# Pesquisar arquivos no Drive
gog drive -a logikacreative.mkt@gmail.com search "comprovante" --limit 5

# Listar pastas raiz
gog drive -a logikacreative.mkt@gmail.com ls --limit 10

# Upload pessoal
gog drive -a davijadielson@gmail.com upload comprovante_pessoal.pdf
```

### Estrutura de Pastas (Drive Empresa - logikacreative)

Pastas principais na raiz:
- `01_CLIENTES` — pastas de clientes
- `06_PARADOS_OUTROS` — projetos parados
- `99_TRIAGEM_E_QUARENTENA` — arquivos em triagem
- `PACKS` — pacotes gráficos
- `SOMBRAS EM PNG` — assets

### Histórico da Correção

1. **Problema original:** `invalid_grant — Token has been expired or revoked`
2. **Causa 1:** Keyring corrompido — `GOG_KEYRING_PASSWORD` estava vazia
3. **Causa 2:** Projeto OAuth `logika-openclaw-gog` estava em modo **Testing** (refresh tokens expiram em 7 dias)
4. **Solução:** 
   - Keyring reconfigurado com senha fixa
   - Tokens antigos removidos e reautorizados (15/jul/2026)
   - Projeto publicado como **"Em produção"** no Google Cloud Console
5. **Resultado:** Refresh tokens NÃO expiram mais em 7 dias

### Próxima Revisão

- **Janeiro/2027** — Verificar se os tokens ainda estão válidos
- Se `invalid_grant` aparecer novamente, verificar:
  1. Se `GOG_KEYRING_PASSWORD` está definida corretamente
  2. Se o projeto ainda está "Em produção" no Google Cloud
  3. Reautorizar com `gog auth add --force-consent --remote`

### Detalhes Técnicos do Projeto

- **Projeto Google Cloud:** `logika-openclaw-gog`
- **Client ID:** `814986081043-8gjtlblvle38loa4sapdkrqkhkq9l5ef.apps.googleusercontent.com`
- **Client Secret armazenado:** no keyring do gog
- **Config:** `/data/.config/gogcli/config.json`
- **Keyring:** `/data/.local/share/gogcli/keyring/` (backend file, criptografado)
- **Credentials file:** `/data/.local/share/gogcli/credentials-814986081043-8gjtlblvle38loa4sapdkrqkhkq9l5ef.json`
- **Tipo de app:** Externo, "Em produção" (não verificado, sem escopos sensíveis)