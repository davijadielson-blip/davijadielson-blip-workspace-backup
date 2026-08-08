#!/usr/bin/env python3
"""Migra itens do DB classico antigo para o novo."""
import json, subprocess, sys, time

env_file = '/data/.openclaw/workspace/scripts/.secrets/notion.env'
token = None
with open(env_file) as f:
    for line in f:
        if line.startswith('NOTION_TOKEN='):
            token = line.split('=', 1)[1].strip()
            break

if not token or len(token) < 30:
    print("ERRO token"); sys.exit(1)

NEW_DB_ID = '3b5316b1-9f92-8021-a52f-d97878572db7'
OLD_DB_ID = '717f518f-39a5-4126-af54-07002bbc25d6'  # DB clássico antigo com os 4838

def api(method, path, payload=None):
    cmd = ['curl', '-s', '-w', '\n%{http_code}',
           '-H', 'Authorization: Bearer ' + token,
           '-H', 'Notion-Version: 2022-06-28']
    if method == 'GET':
        cmd.append('https://api.notion.com/v1' + path)
    elif method == 'POST':
        cmd.extend(['-X', 'POST', '-H', 'Content-Type: application/json'])
        cmd.append(json.dumps(payload))
        cmd.append('https://api.notion.com/v1' + path)

    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    out = r.stdout.strip().rsplit('\n', 1)
    body = out[0]
    code = int(out[-1]) if len(out) > 1 and out[-1].isdigit() else 0
    try: return json.loads(body), code, None
    except: return None, code, body[:400]

# Verificar DB antigo
print("=== VERIFICAR DB ANTIGO ===\n", flush=True)
old_info, _, _ = api('GET', '/databases/' + OLD_DB_ID)
if old_info:
    old_total = old_info.get('parent',{}).get('database_id','')
    props = list(old_info.get('properties',{}).keys())
    print(f"DB antigo tem {len(props)} colunas", flush=True)
    print(f"Props: {props}", flush=True)
else:
    print("Nao encontrou DB antigo")

# Query paginas do DB antigo
print("\n=== MIGRAR ===\n", flush=True)
cursor = None; batch = 0; migrated = 0; errors = 0
batch_items = 0

while True:
    batch += 1
    qp = {'database_id': OLD_DB_ID, 'page_size': 100}
    if cursor: qp['start_cursor'] = cursor

    dr, code, de = api('POST', '/search', qp)
    if de or code != 200:
        print(f"ERROR {code}: {de[:200]}"); break

    results = dr.get('results', []) if dr else []
    has_more = dr.get('has_more', False) if dr else False
    next_cursor = dr.get('next_cursor', '') if dr else ''

    if not results:
        print(f"FIM batch {batch}"); break

    batch_items += len(results)
    print(f"Batch {batch}: {len(results)} paginas (total acumulado: {batch_items})", flush=True)

    for page in results:
        pg_id = page.get('id','')
        if pg_id == NEW_DB_ID or pg_id == OLD_DB_ID:
            continue

        pg_props = page.get('properties', {})
        nome = ''; caminho = ''

        for pk, pv in pg_props.items():
            pt = pv.get('type', '')
            if pt == 'title':
                nome = ''.join([t.get('plain_text', '') for t in pv.get('title', [])])
            elif pt == 'rich_text':
                val = ''.join([t.get('plain_text', '') for t in pv.get('rich_text', [])])
                if 'caminho' in pk.lower() or pk == 'cofre':
                    caminho = val

        # Criar pagina no DB novo
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
print(f"\nMigrado: {migrated}\nErros: {errors}", flush=True)
print(f"Banco URL: https://app.notion.com/p/{NEW_DB_ID}\n", flush=True)

# Verificar
vr, vcode, verr = api('POST', '/search', {'query': '', 'filter': {'property': 'parent.database_id', 'string': NEW_DB_ID}, 'page_size': 15})
if vr and vcode == 200:
    found = [r for r in vr.get('results',[]) if r.get('properties',{}).get('Nome')]
    print(f"Verificacao: {len(found)} confirmados\nAmostras:", flush=True)
    for ix, it in enumerate(found[:10]):
        props = it.get('properties', {})
        n = props.get('Nome',{}).get('title',[{}])[0].get('text',{}).get('content','')[:80]
        c = props.get('Caminho Cofre',{}).get('rich_text',[{}])[0].get('text',{}).get('content','')[:100]
        print(f"  {ix+1}. {n}", flush=True)
        print(f"     {c}", flush=True)
else:
    print(f"ERR verif {vcode}", flush=True)
