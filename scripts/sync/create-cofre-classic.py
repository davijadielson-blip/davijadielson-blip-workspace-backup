#!/usr/bin/env python3
"""Cria banco classico e migra itens do DS antigo usando curl."""
import json
import subprocess
import sys
from pathlib import Path

# Le token direto do arquivo
env_file = '/data/.openclaw/workspace/scripts/.secrets/notion.env'
token = None
with open(env_file) as f:
    for line in f:
        if line.startswith('NOTION_TOKEN='):
            token = line.split('=', 1)[1].strip()
            break

if not token or len(token) < 30:
    print("ERRO: Token invalido")
    sys.exit(1)

MAPA_PAGE_ID = '3b4316b1-9f92-8024-9128-c2631a992e4d'
OLD_DS_ID = 'a3803ed8-abf8-47da-9a52-ae8bf889b865'

def call_api(method, path, payload=None):
    """Chama a API Notion usando curl - garante auth correta."""
    cmd = [
        'curl', '-s', '-w', '\n%{http_code}',
        '-H', f'Authorization: Bearer {token}',
        '-H', 'Notion-Version: 2022-06-28',
    ]

    if method == 'GET':
        cmd.append(f'https://api.notion.com/v1{path}')
    else:
        cmd.extend(['-X', method])
        cmd.extend(['-H', 'Content-Type: application/json'])
        cmd.append(json.dumps(payload))
        cmd.append(f'https://api.notion.com/v1{path}')

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    parts = result.stdout.rsplit('\n', 1)
    body = parts[0] if len(parts) > 1 else ''
    http_code = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0

    if body.strip().startswith('{'):
        try:
            return json.loads(body), http_code, None
        except json.JSONDecodeError:
            return None, http_code, body
    return None, http_code, body

print(f"Token OK ({len(token)} chars)\n", flush=True)

# PASSO 1: Criar banco clássico
print("=== Passo 1: Criar banco clÃ¡ssico ===\n", flush=True)

db_pay = {
    "parent": {"type": "page_id", "page_id": MAPA_PAGE_ID},
    "title": [{"text": {"content": "Cofre Index"}}],
    "description": [{"text": {"content": "Index completo do Cofre - 4838 arquivos Markdown"}}],
    "properties": {
        "Nome": {"title": {}},
        "Caminho Cofre": {"rich_text": {}},
        "Frente": {"select": {}},
        "Tipo": {"select": {}},
        "Status Sync": {"select": {}},
        "Protegido": {"checkbox": {}},
        "Hash": {"rich_text": {}},
        "Fluxo": {"select": {}},
        "Direcao Sync": {"select": {}},
    },
}

result, code, err = call_api('POST', '/pages', db_pay)

if result and result.get('object') == 'database':
    DB_ID = result['id']
    prop_names = list(result['properties'].keys())
    print(f"BANCO CRIADO!", flush=True)
    print(f"ID: {DB_ID}", flush=True)
    print(f"Props: {prop_names}\n", flush=True)

    # Contar itens do DS
    count_r, _, _ = call_api('POST', '/data_sources/' + OLD_DS_ID + '/query', {'page_size': 1})
    ds_total = count_r.get('total','?') if count_r else '?'
    print(f"DS tem ~{ds_total} itens\n--- INICIAR MIGRACAO ---\n", flush=True)

    cursor = None
    batch_num = 0
    migrated = 0
    berrs = 0

    while True:
        batch_num += 1
        qp = {'page_size': 100}
        if cursor:
            qp['start_cursor'] = cursor

        dr, _, de = call_api('POST', '/data_sources/' + OLD_DS_ID + '/query', qp)
        if de:
            print(f"ERROR query: {de[:200]}"); break

        items = dr.get('results',[]) if dr else []
        hm = dr.get('has_more',False) if dr else False
        nc = dr.get('next_cursor','') if dr else ''

        if not items:
            print(f"FIM batch {batch_num}"); break

        print(f"Batch {batch_num}: {len(items)} -> paginas...", flush=True)

        for item in items:
            ds_p = item.get('properties',{})
            nome = ''
            caminho = ''

            for pk, pv in ds_p.items():
                pt = pv.get('type','')
                if pt == 'title':
                    nome = ''.join([t.get('plain_text','') for t in pv.get('title',[])])
                elif pt == 'rich_text':
                    val = ''.join([t.get('plain_text','') for t in pv.get('rich_text',[])])
                    if 'caminho' in pk.lower() or pk == 'cofre':
                        caminho = val

            pp = {
                "parent":{"type":"database_id","database_id":DB_ID},
                "properties":{
                    "Nome":{"title":[{"text":{"content":nome or caminho}}]},
                    "Caminho Cofre":{"rich_text":[{"text":{"content":caminho}}]},
                },
            }

            pr, _, pe = call_api('POST', '/pages', pp)
            if pe:
                berrs += 1
                if berrs <= 3:
                    print(f"  ERRO: {pe[:150]}", flush=True)
            elif pr and pr.get('object') == 'page':
                migrated += 1

        if migrated % 500 == 0:
            print(f"Progresso: {migrated}", flush=True)
            import time
            time.sleep(0.1)

        if not hm or not nc:
            break
        cursor = nc
        import time
        time.sleep(0.05)

    print("\n"+"="*60, flush=True)
    print(f"MIGRADO: {migrated}", flush=True)
    print(f"Erros: {berrs}", flush=True)
    print(f"\nURL: https://app.notion.com/p/{DB_ID}\n", flush=True)

    # Verificar
    vr, verr = call_api('POST', '/databases/'+DB_ID+'/query', {'page_size': 10})
    if vr and not verr:
        vt = vr.get('total','?')
        print(f"Confirmado: {vt} totais\nAmostras:", flush=True)
        for ix, it in enumerate(vr.get('results',[])[:10]):
            p = it.get('properties',{})
            n = p.get('Nome',{}).get('title',[{}])[0].get('text',{}).get('content','')[:60]
            c = p.get('Caminho Cofre',{}).get('rich_text',[{}])[0].get('text',{}).get('content','')[:80]
            print(f"\n  {ix+1}. {n}", flush=True)
            print(f"     {c}", flush=True)
    else:
        print(f"\nErro verificacao: {verr}", flush=True)
else:
    print(f"FAIL: {err[:600]}", flush=True)
    if code != 200:
        print(f"Codigo HTTP: {code}", flush=True)
