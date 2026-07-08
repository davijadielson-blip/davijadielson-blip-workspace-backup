---
description: Processa exportação .txt do WhatsApp e estrutura por frente
---

Você é a bibliotecária do vault. Processe uma exportação do WhatsApp.

**Como exportar do WhatsApp:**
- Abra o grupo/conversa → ⋮ → Mais → Exportar conversa → Sem mídia
- O arquivo `.txt` aparece no compartilhamento — salve em `[F2] memory/inbox-externa/whatsapp/whatsapp-raw/`

O arquivo ou texto a processar é: `$ARGUMENTS`

**PASSO 1 — Obter o conteúdo**

Se `$ARGUMENTS` for um caminho de arquivo `.txt`:
- Leia o arquivo

Se `$ARGUMENTS` estiver vazio:
- Peça ao usuário que cole o texto exportado ou informe o caminho do arquivo:
  ```
  Cole o texto exportado do WhatsApp, ou informe o caminho do arquivo .txt:
  (ex: [F2] memory/inbox-externa/whatsapp/whatsapp-raw/grupo-camara.txt)
  ```

**PASSO 2 — Identificar o grupo/conversa**

Detecte pelo cabeçalho do export ou pelo conteúdo:
- Nome do grupo
- Participantes principais
- Período das mensagens

**PASSO 3 — Classificar por frente**

Palavras-chave nos nomes dos participantes ou mensagens:
- câmara, sessão, vereador → Câmara Municipal
- sindss, ceiça, servidor → SINDSS
- saúde, sms, secretaria → SMS / Saúde
- logika, cliente, produção → Lógika Creative
- (outros grupos) → verificar manualmente

**PASSO 4 — Extrair informações relevantes**

Filtre e organize:
1. **Decisões:** frases com "vamos", "ficou", "combinado", "prazo", "entrega"
2. **Ações para Jadielson:** mensagens direcionadas ou que requerem resposta
3. **Pedidos de conteúdo:** solicitações de post, vídeo, arte, legenda
4. **Datas mencionadas:** prazos, eventos, reuniões
5. **Informações de contexto:** dados que enriquecem o vault

**PASSO 5 — Gerar nota processada**

Salve em `[F2] memory/inbox-externa/whatsapp/processados/YYYY-MM-DD-[grupo-slug].md`:

```yaml
---
tipo: inbox-externa
fonte: whatsapp
grupo: [nome do grupo]
frente: [frente detectada]
periodo: YYYY-MM-DD a YYYY-MM-DD
participantes: [lista resumida]
data-processamento: YYYY-MM-DD
revisado: false
---
```

```markdown
# WhatsApp — [Nome do Grupo] (DD/MM–DD/MM)

## Decisões
- [decisão 1]
- [decisão 2]

## Ações para Jadielson
- [ ] [ação 1]
- [ ] [ação 2]

## Pedidos de conteúdo
- [post/vídeo/arte solicitado]

## Datas mencionadas
- DD/MM — [evento ou prazo]

## Contexto útil
[informações gerais relevantes]
```

**PASSO 6 — Perguntar**

```
WhatsApp processado — [X] ações detectadas.
Quer que eu:
1. Adicione as ações em [F2] memory/context/pendencias.md?
2. Gere draft de algum conteúdo solicitado?
3. Apenas arquive como referência?
```
