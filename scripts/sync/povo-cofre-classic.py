#!/usr/bin/env python3
"""Popula banco classico do Cofre Index com os 4838 itens do DS."""
import json
import subprocess
import sys
from pathlib import Path

# Le token direto do arquivo - sempre puro, sem ***
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

NEW_DB_ID = '3b5316b1-9f92-8021-a52f-d97878572db7'
OLD_DS_ID = 'a3803ed8-abf8-47da-9a52-ae8bf889b865'

def call_api(method, path, payload=None):
    """Chama a API Notion usando curl com auth Bearer correta."""
    cmd = [
        'curl', '-s', '-w', '\n%{http_code}',
        '-H', 'Authorization: Bearer ' + token,
        '-H', 'Notion-Version: 2022-06-28',
    ]

    if method == 'GET':
        url = 'https://api.notion.com/v1' + path
        cmd.append(url)
    elif method == 'PATCH':
        url = 'https://api.notion.com/v1' + path
        cmd.extend(['-X', 'PATCH'])
        cmd.extend(['-H', 'Content-Type: application/json'])
        cmd.append(json.dumps(payload))
        cmd.append(url)
    elif method == 'POST':
        url = 'https://api.notion.com/v1' + path
        cmd.extend(['-X', 'POST'])
        cmd.extend(['-H', 'Content-Type: application/json'])
        cmd.append(json.dumps(payload))
        cmd.append(url)

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    parts = result.stdout.rsplit('\n', 1)
    body = parts[0] if len(parts) > 1 else ''
    http_code = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0

    if body.strip().startswith('{') or body.strip().startswith('['):
        try:
            return json.loads(body), http_code, None
        except json.JSONDecodeError:
            return None, http_code, body[:500]
    return None, http_code, body[:500]

print(f"Token OK ({len(token)} chars)\n", flush=True)

# ===== PASSO 1: Adicionar colunas ao banco =====
print("=== Passo 1: Adicionar colunas ===\n", flush=True)

update_pay = {
    "properties": {
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

result, code, err = call_api('PATCH', '/databases/' + NEW_DB_ID, update_pay)

if err or code != 200:
    print(f"FALHA ao adicionar props: {err}\nHTTP: {code}", flush=True)
else:
    prop_names = list(result.get('properties', {}).keys())
    print(f"Props adicionadas com sucesso!", flush=True)
    print(f"Todas as colunas: {prop_names}\n", flush=True)

# ===== PASSO 2: Contar itens do DS antigo =====
print("=== Passo 2: Contar itens do DS antigo ===\n", flush=True)

count_r, _, _ = call_api('POST', '/data_sources/' + OLD_DS_ID + '/query', {'page_size': 1})
ds_total = count_r.get('total','?') if count_r else '?'
print(f"DS antigo tem ~{ds_total} itens para migrar\n", flush=True)

# ===== PASSO 3: Migrar items =====
print("=== Passo 3: Migrar itens ===\n", flush=True)

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

    print(f"Batch {batch_num}: {len(items)} -> criando paginas...", flush=True)

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

        # Construir propriedades da pagina
        page_props = {
            "parent":{"type":"database_id","database_id":NEW_DB_ID},
            "properties":{
                "Nome":{"title":[{"text":{"content":nome or caminho or 'Sem titulo'}}]},
                "Caminho Cofre":{"rich_text":[{"text":{"content":caminho}}]},
            },
        }

        pr, _, pe = call_api('POST', '/pages', page_props)
        if pe:
            berrs += 1
            if berrs <= 3:
                print(f"  ERRO pagina: {pe[:150]}", flush=True)
        elif pr and pr.get('object') == 'page':
            migrated += 1

    if migrated % 500 == 0:
        print(f"Progresso ate agora: {migrated}", flush=True)
        import time
        time.sleep(0.1)

    if not hm or not nc:
        break
    cursor = nc
    import time
    time.sleep(0.05)

# ===== RESUMO =====
print("\n"+"="*60, flush=True)
print(f"MIGRACAO CONCLUIDA!\n", flush=True)
print(f"Migrado: {migrated} paginas criadas\n", flush=True)
print(f"Erros: {berrs}\n", flush=True)
print(f"URL do banco: https://app.notion.com/p/{NEW_DB_ID}\n", flush=True)

# Verificar total
vr, _, verr = call_api('POST', '/databases/'+NEW_DB_ID+'/query', {'page_size': 15})
if vr and not verr:
    vt = vr.get('total','?')
    print(f"Verificacao: {vt} totais confirmados\nAmostras:", flush=True)
    for ix, it in enumerate(vr.get('results',[])[:15]):
        p = it.get('properties',{})
        n = p.get('Nome',{}).get('title',[{}])[0].get('text',{}).get('content','')[:70]
        c = p.get('Caminho Cofre',{}).get('rich_text',[{}])[0].get('text',{}).get('content','')[:90]
        f = p.get('Frente',{}).get('select',{}).get('name','')
        print(f"\n  {ix+1}. {n}", flush=True)
        print(f"     {c}", flush=True)
        if f:
            print(f"     Frente: {f}", flush=True)
else:
    print(f"Erro verificacao: {verr}", flush=True)
