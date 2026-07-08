---
description: Arquiva link de referência de um arquivo do Drive — uso: /drive-arquivo <ID ou URL>
---

Você é a bibliotecária do vault. Arquive um link de referência de um arquivo do Google Drive.

O ID ou URL do arquivo é: `$ARGUMENTS`

Se `$ARGUMENTS` estiver vazio, pergunte ao usuário o ID ou URL antes de prosseguir.

**PASSO 1 — Obter metadados**

Use `mcp__claude_ai_Google_Drive__get_file_metadata`:
- fileId: extraia o ID de `$ARGUMENTS` (se for URL, pegue o trecho após `/d/` ou `?id=`)

**PASSO 2 — Identificar frente**

Baseie-se no nome e caminho do arquivo para classificar a frente (mesmo critério de `/drive-recente`).

**PASSO 3 — Criar nota de referência**

Salve em `[F2] memory/inbox-externa/drive/YYYY-MM-DD-[slug-nome].md`:

```yaml
---
tipo: inbox-externa
fonte: google-drive
data: YYYY-MM-DD
frente: [frente detectada]
arquivo-nome: [nome do arquivo]
arquivo-id: [ID]
arquivo-tipo: [documento/planilha/pasta/vídeo]
arquivo-modificado: YYYY-MM-DD
proprietario: [email]
revisado: false
---

# [Nome do arquivo]

**Frente:** [frente]
**Tipo:** [tipo]
**Modificado:** DD/MM/YYYY
**Proprietário:** [email]

## Link de acesso
- ID: `[ID]`
- URL: `https://drive.google.com/file/d/[ID]/view`

## Contexto
[Uma linha explicando para que serve este arquivo — se souber pelo nome/contexto]

## Próximo passo sugerido
[ ] Revisar conteúdo
[ ] Associar a tarefa/entrega específica
[ ] Mover referência para [F1]
```

**PASSO 4 — Confirmar**

```
✅ Referência arquivada: [F2] memory/inbox-externa/drive/YYYY-MM-DD-[slug].md
Frente detectada: [frente]
Arquivo: [nome]
```
