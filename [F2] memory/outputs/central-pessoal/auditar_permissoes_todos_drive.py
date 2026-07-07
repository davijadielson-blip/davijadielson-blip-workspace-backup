#!/usr/bin/env python3
import json,csv,pathlib,subprocess,os,time,sys
BASE=pathlib.Path('/data/.openclaw/workspace')
OUT=BASE/'[F2] memory/outputs/central-pessoal'
REP=OUT/'drive_pessoal_auditoria_completa_2026-07-07'
INV=OUT/'drive-pessoal-inventory-consolidado-2026-07-07.csv'
RESULT=REP/'permissoes_todos_resultado.jsonl'
FIND=REP/'permissoes_todos_achados.csv'
ERR=REP/'permissoes_todos_erros.jsonl'
seen=set()
if RESULT.exists():
    for line in RESULT.read_text(encoding='utf-8',errors='ignore').splitlines():
        try: seen.add(json.loads(line)['id'])
        except Exception: pass
rows=[]
with open(INV,encoding='utf-8') as f:
    for r in csv.DictReader(f):
        if r.get('id') and r['id'] not in seen: rows.append(r)
print('restantes',len(rows),'já_processados',len(seen), flush=True)
env=os.environ.copy(); env['PATH']='/home/linuxbrew/.linuxbrew/bin:'+env.get('PATH','')
write_header=not FIND.exists()
with open(RESULT,'a',encoding='utf-8') as rf, open(ERR,'a',encoding='utf-8') as ef, open(FIND,'a',newline='',encoding='utf-8') as cf:
    w=csv.DictWriter(cf,fieldnames=['id','path','permissionType','role','email','permId'])
    if write_header: w.writeheader()
    for idx,row in enumerate(rows,1):
        fid=row['id']
        cmd=f"export PATH=/home/linuxbrew/.linuxbrew/bin:$PATH; source /data/.openclaw/workspace/scripts/gog-auth.sh && gog --account davijadielson@gmail.com --json drive permissions {fid}"
        try:
            cp=subprocess.run(['bash','-lc',cmd],capture_output=True,text=True,timeout=18,env=env)
            if cp.returncode!=0:
                ef.write(json.dumps({'id':fid,'path':row.get('path'),'error':(cp.stderr or cp.stdout)[-800:]},ensure_ascii=False)+'\n'); ef.flush(); continue
            data=json.loads(cp.stdout)
            rec={'id':fid,'path':row.get('path'),'permissionCount':data.get('permissionCount'),'permissions':data.get('permissions',[])}
            rf.write(json.dumps(rec,ensure_ascii=False)+'\n'); rf.flush()
            for perm in rec['permissions']:
                typ=perm.get('type'); email=perm.get('emailAddress','') or ''
                if typ=='anyone' or (typ in ('user','group','domain') and email and email!='davijadielson@gmail.com'):
                    w.writerow({'id':fid,'path':row.get('path'),'permissionType':typ,'role':perm.get('role'),'email':email,'permId':perm.get('id')}); cf.flush()
        except Exception as e:
            ef.write(json.dumps({'id':fid,'path':row.get('path'),'error':repr(e)},ensure_ascii=False)+'\n'); ef.flush()
        if idx%100==0: print('processados_nesta_execucao',idx,'restantes_estimados',len(rows)-idx, flush=True)
print('fim', flush=True)
