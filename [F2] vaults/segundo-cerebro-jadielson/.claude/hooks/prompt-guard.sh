#!/usr/bin/env bash
# Hook: UserPromptSubmit — Guarda de publicação e Rogério
# Saída: aviso não-bloqueante (exit 0 sempre)

INPUT=$(cat)
PROMPT=$(echo "$INPUT" | python3 -c \
  "import sys,json; d=json.load(sys.stdin); print(d.get('prompt','').lower())" \
  2>/dev/null || echo "")

[ -z "$PROMPT" ] && exit 0

# Gatilhos de publicação — frases completas (não palavras soltas)
PUB_PATTERN="publicar agora|postar agora|envia esse|manda esse|posta esse|sobe esse|envia para o instagram|posta no stories|posta no feed"

if echo "$PROMPT" | grep -qiE "$PUB_PATTERN"; then
  printf "⚠️  **Lembrete de fluxo:** eu não publico diretamente — isso é trabalho seu. Posso deixar o conteúdo finalizado e pronto para você colar. Quer que eu faça isso?\n\n"
fi

# Gatilho Rogério + eleição
if echo "$PROMPT" | grep -qiE "rogerio|rogério"; then
  if echo "$PROMPT" | grep -qiE "eleição|eleicao|votos|campanha|candidato|vote em|reeleição|reeleicao|eleitor"; then
    printf "⚠️  **Atenção — Rogério Rocha:** ele já foi reeleito. Todo conteúdo é de **mandato em exercício** — sem referência a eleição, voto ou campanha. Posso reformular o pedido nesse contexto.\n\n"
  fi
fi

exit 0
