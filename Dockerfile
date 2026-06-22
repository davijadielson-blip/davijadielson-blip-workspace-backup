FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    bash curl git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    google-api-python-client \
    google-auth \
    google-auth-httplib2 \
    google-auth-oauthlib

WORKDIR /app
COPY . .

RUN chmod +x scripts/cloud/railway-start.sh \
    scripts/cron-jobs/telegram-polling.sh \
    scripts/lib/send-telegram.sh 2>/dev/null || true

ENV TG_VAULT_PATH=/app

CMD ["python3", "scripts/cloud/railway-start.py"]
