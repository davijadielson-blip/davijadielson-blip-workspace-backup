#!/bin/bash
# Transcreve áudio via OpenAI Whisper API e salva em [F2] memory/inbox-externa/audio/audio-transcricoes/
# Uso: bash scripts/transcrever.sh <caminho-do-audio>

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
AUDIO_FILE="${1:-}"

if [ -z "$AUDIO_FILE" ]; then
  echo "Uso: bash scripts/transcrever.sh <caminho-do-audio>"
  echo "Formatos suportados: mp3, mp4, m4a, wav, ogg, flac, webm"
  exit 1
fi

if [ ! -f "$AUDIO_FILE" ]; then
  echo "Erro: arquivo não encontrado: $AUDIO_FILE"
  exit 1
fi

# Carrega OPENAI_API_KEY do ambiente ou do .env do workspace.
if [ -z "${OPENAI_API_KEY:-}" ] && [ -f "$VAULT_ROOT/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  source "$VAULT_ROOT/.env"
  set +a
fi

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "Erro: OPENAI_API_KEY não encontrado no ambiente nem em $VAULT_ROOT/.env"
  exit 1
fi

if ! command -v curl >/dev/null 2>&1; then
  echo "Erro: curl não encontrado."
  exit 1
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H-%M")
BASENAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//' | tr ' ' '-' | tr '[:upper:]' '[:lower:]')
OUTPUT_DIR="$VAULT_ROOT/[F2] memory/inbox-externa/audio/audio-transcricoes"
TEMP_JSON="/tmp/openai-whisper-$$.json"
mkdir -p "$OUTPUT_DIR"

cleanup() {
  rm -f "$TEMP_JSON"
}
trap cleanup EXIT

echo "Transcrevendo via OpenAI Whisper API: $AUDIO_FILE"
echo "Modelo: whisper-1"
echo ""

HTTP_CODE=$(curl -sS -w "%{http_code}" -o "$TEMP_JSON" \
  https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@${AUDIO_FILE}" \
  -F "model=whisper-1" \
  -F "language=pt" \
  -F "response_format=json")

if [ "$HTTP_CODE" -lt 200 ] || [ "$HTTP_CODE" -ge 300 ]; then
  echo "Erro: API OpenAI retornou HTTP $HTTP_CODE"
  python3 - <<'PY' "$TEMP_JSON" 2>/dev/null || cat "$TEMP_JSON"
import json,sys
try:
    data=json.load(open(sys.argv[1]))
    err=data.get('error', data)
    print(err.get('message', err) if isinstance(err, dict) else err)
except Exception:
    print(open(sys.argv[1]).read())
PY
  exit 1
fi

TRANSCRICAO=$(python3 - <<'PY' "$TEMP_JSON"
import json,sys
with open(sys.argv[1], encoding='utf-8') as f:
    data=json.load(f)
print(data.get('text','').strip())
PY
)

if [ -z "$TRANSCRICAO" ]; then
  echo "Erro: API não retornou texto de transcrição."
  cat "$TEMP_JSON"
  exit 1
fi

OUTPUT_FILE="$OUTPUT_DIR/${DATE}-${TIME}-${BASENAME}.md"

cat > "$OUTPUT_FILE" << MARKDOWN
---
tipo: inbox-externa
fonte: audio-openai-whisper-api
data: ${DATE}
arquivo-original: $(basename "$AUDIO_FILE")
modelo-whisper: whisper-1
idioma: portuguese
frente: ""
revisado: false
---

# Transcrição — $(basename "$AUDIO_FILE")

**Data:** ${DATE} às $(date +"%H:%M")
**Arquivo:** \`$(basename "$AUDIO_FILE")\`
**Modelo:** OpenAI Whisper API — whisper-1

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
