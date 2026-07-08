#!/bin/bash
# Backup automático do workspace → GitHub (segundo-cérebro)
# Executado pelo cron diário às 03:00 BRT

cd /data/.openclaw/workspace || exit 1

DATA=$(date +%Y-%m-%d-%H%M)

git add -A
git commit --allow-empty -m "backup: $DATA"
git push backup main 2>&1

echo "Backup concluído: $DATA"
