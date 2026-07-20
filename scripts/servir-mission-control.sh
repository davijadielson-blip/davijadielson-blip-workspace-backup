#!/bin/bash
# Mission Control - Servidor + Tunnel
# Uso: bash scripts/servir-mission-control.sh

WORKSPACE="/data/.openclaw/workspace"
PID_HTTP="/tmp/mc-http.pid"
PID_SSH="/tmp/mc-ssh.pid"

parar() {
    echo "Parando servicos..."
    [ -f "$PID_HTTP" ] && kill $(cat "$PID_HTTP") 2>/dev/null && rm "$PID_HTTP"
    [ -f "$PID_SSH" ] && kill $(cat "$PID_SSH") 2>/dev/null && rm "$PID_SSH"
    echo "Parou."
    exit 0
}

trap parar SIGINT SIGTERM

# Já tem algum rodando?
[ -f "$PID_HTTP" ] && echo "Servidor ja rodando. Pare primeiro." && exit 1

# Iniciar servidor HTTP
cd "$WORKSPACE"
python3 -m http.server 8899 &
echo $! > "$PID_HTTP"
echo "Servidor HTTP rodando na porta 8899 (pid $(cat $PID_HTTP))"

# Tunnel SSH
echo "Conectando tunnel localhost.run..."
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=30 \
    -R 80:localhost:8899 nokey@localhost.run &
echo $! > "$PID_SSH"

echo "---"
echo "Aguardando tunnel... (30s para estabilizar)"
sleep 5

# Testar
for i in $(seq 1 6); do
    sleep 5
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8899/mission-control.html 2>/dev/null)
    echo "  [$((i*5))s] Servidor local: $HTTP_CODE"
    if [ "$HTTP_CODE" = "200" ]; then
        echo ""
        echo "✅ Servidor OK! Tunnel ativo em https://XXXX.lhr.life"
        echo "   (verifique nos logs do SSH acima)"
        echo ""
        echo "Pressione Ctrl+C para parar."
        break
    fi
done

# Manter rodando
wait