---
description: Transcreve áudio com Whisper local e estrutura nota no vault — uso: /audio-importar <caminho>
---

Você é a bibliotecária do vault. Transcreva um áudio e estruture a nota.

O caminho do arquivo de áudio é: `$ARGUMENTS`

**PASSO 1 — Verificar argumento**

Se `$ARGUMENTS` estiver vazio:
```
Para usar este comando:
1. Rode no terminal: bash scripts/transcrever.sh /caminho/do/audio.mp3
2. Depois: /audio-importar [F2] memory/inbox-externa/audio/audio-transcricoes/YYYY-MM-DD-nome.md

Formatos suportados: mp3, mp4, m4a, wav, ogg, flac, webm

Pré-requisito (instalar uma vez):
  pip install openai-whisper
```

**PASSO 2 — Verificar se é arquivo de transcrição ou áudio**

Se `$ARGUMENTS` terminar em `.md`:
- Leia o arquivo — já é uma transcrição gerada pelo `scripts/transcrever.sh`
- Vá ao PASSO 4 diretamente

Se for arquivo de áudio (`.mp3`, `.wav`, etc.):
- Instrua o usuário a rodar o script primeiro:
  ```
  bash scripts/transcrever.sh "$ARGUMENTS"
  ```
- Aguarde e prossiga com o `.md` gerado

**PASSO 3 — Ler transcrição**

Leia o arquivo `.md` em `[F2] memory/inbox-externa/audio/audio-transcricoes/`.

**PASSO 4 — Analisar e classificar**

Da transcrição, extraia:

1. **Frente:** qual frente está sendo discutida? (Câmara, SMS, SINDSS, Lógika, Pessoal)
2. **Tipo:** reunião, voicenote, entrevista, captura de campo, outro
3. **Participantes mencionados:** nomes detectados
4. **Decisões tomadas:** frases decisivas ("vamos fazer X", "ficou definido", "prazo é")
5. **Ações geradas:** tarefas implícitas ou explícitas
6. **Temas principais:** lista de até 5 tópicos

**PASSO 5 — Atualizar o arquivo**

Preencha os campos `frente:` e adicione seção de análise ao arquivo `.md`:

```markdown
## Análise (gerada por IA)

**Frente:** [frente detectada]
**Tipo:** [reunião/voicenote/entrevista/outro]
**Participantes:** [lista]

### Decisões detectadas
- [decisão 1]
- [decisão 2]

### Ações geradas
- [ ] [ação 1] → adicionar em pendencias.md?
- [ ] [ação 2]

### Temas principais
[tema 1] · [tema 2] · [tema 3]
```

**PASSO 6 — Perguntar**

```
Transcrição analisada. Quer que eu:
1. Adicione as ações detectadas em [F2] memory/context/pendencias.md?
2. Gere um draft de conteúdo baseado nesta gravação?
3. Apenas arquive como referência (revisado: false)?
```

Aguarde a resposta antes de agir.
