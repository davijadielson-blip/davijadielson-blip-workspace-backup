#!/usr/bin/env bash
set -u
export PATH=/home/linuxbrew/.linuxbrew/bin:$PATH
source /data/.openclaw/workspace/scripts/gog-auth.sh
cd /data/.openclaw/workspace
OUT="[F2] memory/outputs/central-pessoal/drive_pessoal_lotes_2026-07-07"
mkdir -p "$OUT"
python3 - <<'PY' > /tmp/drive_roots.tsv
import json
p='[F2] memory/outputs/central-pessoal/drive-pessoal-root-depth1-2026-07-07.json'
d=json.load(open(p))
for it in d['items']:
    print(it['id']+'\t'+it['name'].replace('/','_'))
PY
while IFS=$'\t' read -r id name; do
  safe=$(python3 - <<'PY' "$name"
import sys,re,unicodedata
s=sys.argv[1]
s=re.sub(r'[^\w.-]+','_',s, flags=re.UNICODE).strip('_')[:80]
print(s or 'sem_nome')
PY
)
  echo "== $name =="
  if timeout 180s gog --account davijadielson@gmail.com --json drive inventory --parent "$id" --depth 0 --max 0 > "$OUT/${safe}_${id}.json"; then
    python3 - <<'PY' "$OUT/${safe}_${id}.json"
import json,sys,os
p=sys.argv[1]
d=json.load(open(p))
print('items', len(d.get('items', [])), 'bytes', os.path.getsize(p))
PY
  else
    echo "ERRO_TIMEOUT_OR_FAIL $name" | tee "$OUT/${safe}_${id}.error"
  fi
done < /tmp/drive_roots.tsv
