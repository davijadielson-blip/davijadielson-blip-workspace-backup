#!/usr/bin/env bash
# Transcreve áudio localmente via whisper-cpp (sem OpenAI API) e salva no vault.
# Uso: bash scripts/transcrever.sh <caminho-do-audio>

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIO_FILE="${1:-}"
MODEL="${WHISPER_MODEL:-/data/.openclaw/models/whisper/ggml-tiny.bin}"
OUTPUT_DIR="$VAULT_ROOT/[F2] memory/inbox-externa/audio/audio-transcricoes"

if [ -z "$AUDIO_FILE" ]; then
  echo "Uso: bash scripts/transcrever.sh <caminho-do-audio>"
  echo "Formatos suportados: mp3, mp4, m4a, wav, ogg, flac, webm"
  exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
  echo "Erro: arquivo não encontrado: $AUDIO_FILE"
  exit 1
fi

if ! command -v whisper-cli >/dev/null 2>&1; then
  echo "Erro: whisper-cli não encontrado. Instale com: brew install whisper-cpp"
  exit 1
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "Erro: ffmpeg não encontrado. Instale com: brew install ffmpeg"
  exit 1
fi

if [ ! -s "$MODEL" ]; then
  echo "Erro: modelo Whisper local não encontrado: $MODEL"
  echo "Baixe, por exemplo:"
  echo "  mkdir -p /data/.openclaw/models/whisper"
  echo "  curl -L -o /data/.openclaw/models/whisper/ggml-tiny.bin https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-tiny.bin"
  exit 1
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H-%M")
BASENAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//' | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
mkdir -p "$OUTPUT_DIR"

RUN_USER="${USER:-$(id -un 2>/dev/null || echo openclaw)}"
TMP_WAV="/tmp/transcrever-$RUN_USER-$$.wav"
TMP_OUT="/tmp/transcrever-$RUN_USER-$$"
cleanup() {
  rm -f "$TMP_WAV" "$TMP_OUT.txt" "$TMP_OUT.log"
}
trap cleanup EXIT

echo "Transcrevendo localmente via whisper-cpp: $AUDIO_FILE"
echo "Modelo: $MODEL"
echo ""

ffmpeg -y -v error -i "$AUDIO_FILE" -ar 16000 -ac 1 -c:a pcm_s16le "$TMP_WAV"
whisper-cli -m "$MODEL" -f "$TMP_WAV" -l pt -otxt -of "$TMP_OUT" >"$TMP_OUT.log" 2>&1 || {
  echo "Erro ao transcrever com whisper-cpp:"
  cat "$TMP_OUT.log"
  exit 1
}

TRANSCRICAO=$(sed 's/[[:space:]]\+$//' "$TMP_OUT.txt" | sed '/^$/N;/^\n$/D')

if [ -z "$TRANSCRICAO" ]; then
  echo "Erro: transcrição vazia. Log:"
  cat "$TMP_OUT.log"
  exit 1
fi

OUTPUT_FILE="$OUTPUT_DIR/${DATE}-${TIME}-${BASENAME}.md"

cat > "$OUTPUT_FILE" << MARKDOWN
---
tipo: inbox-externa
fonte: audio-whisper-cpp-local
data: ${DATE}
arquivo-original: $(basename "$AUDIO_FILE")
modelo-whisper: $(basename "$MODEL")
idioma: portuguese
frente: ""
revisado: false
---

# Transcrição — $(basename "$AUDIO_FILE")

**Data:** ${DATE} às $(date +"%H:%M")
**Arquivo:** \`$(basename "$AUDIO_FILE")\`
**Modelo:** whisper-cpp local — \`$(basename "$MODEL")\`

---

## Transcrição

${TRANSCRICAO}

---

## Processamento

> **Frente:** *(classificar manualmente)*
> **Contexto:** *(adicionar contexto da gravação)*
> **Ação gerada:** *(pendência ou decisão extraída)*
MARKDOWN

echo ""
echo "Transcrição salva em:"
echo "  $OUTPUT_FILE"
echo ""
echo "Próximo passo: rode /audio-importar para estruturar a nota no vault."
