#!/usr/bin/env python3
"""Popula o banco classico novo com os ~4838 itens do DS antigo."""
import json, subprocess, sys, time

env_file = '/data/.openclaw/workspace/scripts/.secrets/notion.env'
token = None
with open(env_file) as f:
    for line in f:
        if line.startswith('NOTION_TOKEN='):
            token = line.split('=', 1)[1].strip()
            break

if not token or len(token) < 30:
    print("ERRO"); sys.exit(1)

NEW_DB_ID = '3b5316b1-9f92-8021-a52f-d97878572db7'
OLD_DS_ID = 'a3803ed8-abf8-47da-9a52-ae8bf889b865'

def api(method, path, payload=None):
    cmd = [
        'curl', '-s', '-w', '\n%{http_code}',
        '-H', 'Authorization: Bearer ' + token,
        '-H', 'Notion-Version: 2022-06-28',
    ]
    if method == 'GET':
        cmd.append('https://api.notion.com/v1' + path)
    else:
        cmd.extend(['-X', method, '-H', 'Content-Type: application/json'])
        cmd.append(json.dumps(payload))
        cmd.append('https://api.notion.com/v1' + path)

    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    out = r.stdout.strip().rsplit('\n', 1)
    body = out[0]
    code = int(out[-1]) if len(out) > 1 and out[-1].isdigit() else 0

    try:
        return json.loads(body), code, None
    except:
        return None, code, body[:400]

# Contar DS
print("=== Passo 1: Verificar DS ===\n", flush=True)
cnt, _, _ = api('POST', '/data_sources/' + OLD_DS_ID + '/query', {'page_size': 1})
ds_total = cnt.get('total', '?') if cnt else '?'
print(f"DS antigo tem ~{ds_total} itens\n--- MIGRACAO ---\n", flush=True)

# Migrar
cursor = None
batch = 0
migrated = 0
errors = 0

while True:
    batch += 1
    qp = {'page_size': 100}
    if cursor:
        qp['start_cursor'] = cursor

    dr, code, de = api('POST', '/data_sources/' + OLD_DS_ID + '/query', qp)
    if de or code != 200:
        print(f"ERROR query {code}: {de[:200]}"); break

    items = dr.get('results', []) if dr else []
    has_more = dr.get('has_more', False) if dr else False
    next_cursor = dr.get('next_cursor', '') if dr else ''

    if not items:
        print(f"FIM na batch {batch}"); break

    print(f"Batch {batch}: {len(items)} -> paginas...", flush=True)

    for item in items:
        ds_props = item.get('properties', {})
        nome = ''
        caminho = ''

        for pk, pv in ds_props.items():
            pt = pv.get('type', '')
            if pt == 'title':
                nome = ''.join([t.get('plain_text', '') for t in pv.get('title', [])])
            elif pt == 'rich_text':
                val = ''.join([t.get('plain_text', '') for t in pv.get('rich_text', [])])
                if 'caminho' in pk.lower() or pk == 'cofre':
                    caminho = val

        page_pay = {
            "parent": {"type": "database_id", "database_id": NEW_DB_ID},
            "properties": {
                "Nome": {"title": [{"text": {"content": nome or caminho or 'Sem titulo'}}]},
                "Caminho Cofre": {"rich_text": [{"text": {"content": caminho}}]},
            },
        }

        pr, pcode, pe = api('POST', '/pages', page_pay)
        if pe and pcode != 200:
            errors += 1
            if errors <= 3:
                print(f"  ERRO: {pe[:150]}", flush=True)
        elif pr and pr.get('object') == 'page':
            migrated += 1

    if migrated % 200 == 0:
        print(f"Progresso: {migrated}", flush=True)
        time.sleep(0.1)

    if not has_more or not next_cursor:
        break
    cursor = next_cursor
    time.sleep(0.05)

# Resumo
print("\n" + "=" * 60, flush=True)
print(f"MIGRACAO CONCLUIDA!", flush=True)
print(f"\nMigrado: {migrated} paginas criadas\n", flush=True)
print(f"Erros: {errors}\n", flush=True)
print(f"Banco URL: https://app.notion.com/p/{NEW_DB_ID}\n", flush=True)

# Verificar total
vr, vcode, verr = api('POST', '/databases/' + NEW_DB_ID + '/query', {'page_size': 10})
if vr and vcode == 200:
    vt = vr.get('total', '?')
    print(f"Verificacao: {vt} totais confirmados no banco novo\nAmostras:", flush=True)
    for ix, it in enumerate(vr.get('results', [])[:10]):
        props = it.get('properties', {})
        n = props.get('Nome', {}).get('title', [{}])[0].get('text', {}).get('content', '')[:70]
        c = props.get('Caminho Cofre', {}).get('rich_text', [{}])[0].get('text', {}).get('content', '')[:90]
        protected = '[PROT]' if it.get('in_trash') else '     '
        print(f"\n  {protected}{ix+1}. {n}", flush=True)
        print(f"     {c}", flush=True)
else:
    print(f"Erro verificacao HTTP:{vcode} {verr}", flush=True)
