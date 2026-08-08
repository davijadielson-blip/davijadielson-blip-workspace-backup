#!/usr/bin/env python3
"""Migra DS Cofre Index para banco classico de paginas no MAPA 360."""
import json
import os
import urllib.request
import urllib.error
import time
import sys
from pathlib import Path

env_file = '/data/.openclaw/workspace/scripts/.secrets/notion.env'
token = ''
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

def req(method, path, payload=None):
    url = 'https://api.notion.com/v1' + path
    body = json.dumps(payload).encode() if payload else None
    headers = {
        'Authorization': 'Bearer ' + token,
        'Notion-Version': '2022-06-28',
        'Content-Type': 'application/json',
    }
    r = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        resp = urllib.request.urlopen(r, timeout=90)
        return json.loads(resp.read().decode()), None
    except urllib.error.HTTPError as e:
        raw = e.read().decode()[:800]
        return None, raw

# Create DB with all property keys explicitly defined per Notion spec
print("=== Criando banco classico ===", flush=True)

ALL_TYPES_NULL = {
    "title": None,
    "rich_text": [],
    "number": None,
    "url": None,
    "select": None,
    "multi_select": [],
    "people": [],
    "email": None,
    "phone_number": None,
    "date": None,
    "checkbox": None,
    "files": [],
    "relation": [],
}

db_pay = {
    "parent": {"type": "page_id", "page_id": MAPA_PAGE_ID},
    "icon": {"type": "emoji", "emoji": "\U0001F4CB"},
    "title": [{"type": "text", "text": {"content": "Cofre Index"}}],
    "description": [{"type": "text", "text": {"content": "Index completo do Cofre"}}],
    "properties": {
        "Nome": dict(ALL_TYPES_NULL, **{"title": {}}),
        "Caminho Cofre": dict(ALL_TYPES_NULL, **{"rich_text": {}}),
        "Frente": dict(ALL_TYPES_NULL, **{"select": {}}),
        "Tipo": dict(ALL_TYPES_NULL, **{"select": {}}),
        "Status Sync": dict(ALL_TYPES_NULL, **{"select": {}}),
        "Protegido": dict(ALL_TYPES_NULL, **{"checkbox": {}}),
        "Hash": dict(ALL_TYPES_NULL, **{"rich_text": {}}),
        "Fluxo": dict(ALL_TYPES_NULL, **{"select": {}}),
        "Direcao Sync": dict(ALL_TYPES_NULL, **{"select": {}}),
    },
}

result, err = req('POST', '/pages', db_pay)

if result and result.get('object') == 'database':
    DB_ID = result['id']
    prop_names = list(result['properties'].keys())
    print(f"BANCO CRIADO! ID: {DB_ID}", flush=True)
    print(f"Props: {prop_names}\n", flush=True)

    # Count DS items
    count_r, _ = req('POST', '/data_sources/'+OLD_DS_ID+'/query', {'page_size': 1})
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

        dr, de = req('POST', '/data_sources/'+OLD_DS_ID+'/query', qp)
        if de:
            print(f"ERROR query: {de[:200]}"); break

        items = dr.get('results',[]) if dr else []
        hm = dr.get('has_more',False) if dr else False
        nc = dr.get('next_cursor','') if dr else ''

        if not items:
            print(f"FIM no batch {batch_num}"); break

        print(f"Batch {batch_num}: {len(items)} itens...", flush=True)

        for item in items:
            ds_p = item.get('properties',{})
            nome = ''; caminho = ''

            for pk,pv in ds_p.items():
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
                    "Nome":{"title":[{"text":{"content":nome or caminho or 'Sem titulo'}}]},
                    "Caminho Cofre":{"rich_text":[{"text":{"content":caminho}}]},
                },
            }

            pr, pe = req('POST', '/pages', pp)
            if pe:
                berrs += 1
                if berrs <= 5:
                    print(f"  ERRO pagina: {pe[:150]}", flush=True)
            elif pr and pr.get('object') == 'page':
                migrated += 1

        if migrated % 500 == 0:
            print(f"Progresso: {migrated}", flush=True)
            time.sleep(0.1)

        if not hm or not nc:
            print("Ultimo batch."); break

        cursor = nc
        time.sleep(0.05)

    print("\n"+"="*60, flush=True)
    print(f"MIGRACAO CONCLUIDA!", flush=True)
    print(f"Total: {migrated} paginas criadas", flush=True)
    print(f"Erros: {berrs}", flush=True)
    print(f"\nURL: https://app.notion.com/p/{DB_ID}", flush=True)

    vr, verr = req('POST', '/databases/'+DB_ID+'/query', {'page_size': 10})
    if vr:
        vt = vr.get('total','?')
        print(f"\nConfirmado: {vt} totais no novo banco\nAmostras:", flush=True)
        for ix, it in enumerate(vr.get('results',[])[:10]):
            p = it.get('properties',{})
            n = p.get('Nome',{}).get('title',[{}])[0].get('text',{}).get('content','')[:60]
            c = p.get('Caminho Cofre',{}).get('rich_text',[{}])[0].get('text',{}).get('content','')[:80]
            print(f"  {ix+1}. {n}", flush=True)
            print(f"     {c}", flush=True)
    else:
        print(f"Erro verificacao: {verr}", flush=True)
else:
    print(f"FAIL: {err[:600]}", flush=True)
