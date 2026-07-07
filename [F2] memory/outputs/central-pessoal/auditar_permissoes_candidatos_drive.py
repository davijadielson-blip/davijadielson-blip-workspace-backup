#!/usr/bin/env python3
import json,csv,pathlib,subprocess,os,time
BASE=pathlib.Path('/data/.openclaw/workspace')
OUT=BASE/'[F2] memory/outputs/central-pessoal'
REP=OUT/'drive_pessoal_auditoria_completa_2026-07-07'
FILES=['candidatos_logika_empresa.csv','candidatos_financeiro.csv','candidatos_sensivel_pessoal.csv']
ids={}
for fn in FILES:
    p=REP/fn
    if not p.exists(): continue
    with open(p,encoding='utf-8') as f:
        for row in csv.DictReader(f):
            fid=row.get('id')
            if fid: ids[fid]=row
print('candidatos únicos',len(ids))
results=[]; findings=[]; errors=[]
env=os.environ.copy(); env['PATH']='/home/linuxbrew/.linuxbrew/bin:'+env.get('PATH','')
# keyring password via bash source easier
for idx,(fid,row) in enumerate(ids.items(),1):
    cmd=f"export PATH=/home/linuxbrew/.linuxbrew/bin:$PATH; source /data/.openclaw/workspace/scripts/gog-auth.sh && gog --account davijadielson@gmail.com --json drive permissions {fid}"
    try:
        cp=subprocess.run(['bash','-lc',cmd],capture_output=True,text=True,timeout=25,env=env)
        if cp.returncode!=0:
            errors.append({'id':fid,'path':row.get('path'),'error':cp.stderr[-500:] or cp.stdout[-500:]}); continue
        data=json.loads(cp.stdout)
        perms=data.get('permissions',[])
        rec={'id':fid,'path':row.get('path'),'name':row.get('name'),'permissionCount':data.get('permissionCount'),'permissions':perms}
        results.append(rec)
        for perm in perms:
            typ=perm.get('type'); role=perm.get('role'); email=perm.get('emailAddress','')
            is_public=(typ=='anyone')
            is_external=(typ in ('user','group','domain') and email and not email.endswith('@gmail.com') and email!='davijadielson@gmail.com')
            # gmail.com is not truly internal for a personal account, but keep public first; user shares still logged separately
            is_user_other=(typ in ('user','group','domain') and email and email!='davijadielson@gmail.com')
            if is_public or is_user_other:
                findings.append({'id':fid,'path':row.get('path'),'permissionType':typ,'role':role,'email':email,'permId':perm.get('id')})
    except Exception as e:
        errors.append({'id':fid,'path':row.get('path'),'error':repr(e)})
    if idx%25==0: print('processados',idx,'findings',len(findings),'errors',len(errors))
(REP/'permissoes_candidatos_resultado.json').write_text(json.dumps({'results':results,'findings':findings,'errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
with open(REP/'permissoes_candidatos_achados.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['id','path','permissionType','role','email','permId']); w.writeheader(); w.writerows(findings)
print('concluído', 'resultados',len(results),'findings',len(findings),'errors',len(errors))
for f in findings[:30]: print(f)
