#!/usr/bin/env python3
import json, pathlib, subprocess, datetime, time, os
BASE=pathlib.Path('/data/.openclaw/workspace')
OUT=BASE/'[F2] memory/outputs/central-pessoal'
LOTES=OUT/'drive_pessoal_lotes_2026-07-07'
RUN=OUT/'drive_pessoal_migracao_logika_2026-07-08'
RUN.mkdir(parents=True, exist_ok=True)
DEST_ROOT='1RLmU3ArJZ8YXdjvUh21heW4BcXB8_JK4'
LOGIKA='logikacreative.mkt@gmail.com'
PESSOAL='davijadielson@gmail.com'
ENV=os.environ.copy(); ENV['PATH']='/home/linuxbrew/.linuxbrew/bin:'+ENV.get('PATH',''); ENV['GOMAXPROCS']='1'

def run(cmd, timeout=180):
    full=f'export GOMAXPROCS=1; export PATH=/home/linuxbrew/.linuxbrew/bin:$PATH; source /data/.openclaw/workspace/scripts/gog-auth.sh; {cmd}'
    cp=subprocess.run(['bash','-lc',full],capture_output=True,text=True,timeout=timeout,env=ENV)
    return cp

def gog_json(cmd, timeout=180):
    cp=run(cmd,timeout)
    if cp.returncode!=0:
        raise RuntimeError((cp.stderr or cp.stdout)[-2000:])
    return json.loads(cp.stdout) if cp.stdout.strip() else {}

log={'timestamp':datetime.datetime.utcnow().isoformat()+'Z','destRoot':DEST_ROOT,'folders':{},'copied':[],'shared':[],'errors':[],'skipped':[]}

def mkdir(name,parent):
    key=(parent,name)
    if str(key) in log['folders']: return log['folders'][str(key)]
    try:
        data=gog_json(f'gog --account {LOGIKA} --json drive mkdir {json.dumps(name)} --parent {parent}',120)
        fid=data['folder']['id']; log['folders'][str(key)]=fid; print('MKDIR',name,fid); return fid
    except Exception as e:
        log['errors'].append({'op':'mkdir','name':name,'parent':parent,'error':repr(e)}); raise

def share_source(fid, role='reader'):
    cp=run(f'gog --account {PESSOAL} --force --json drive share {fid} --to user --email {LOGIKA} --role {role}',120)
    rec={'fileId':fid,'role':role,'returncode':cp.returncode,'stdout':cp.stdout[-1000:],'stderr':cp.stderr[-1000:]}
    log['shared'].append(rec)
    if cp.returncode!=0: print('SHARE_ERR',fid,(cp.stderr or cp.stdout)[:200])
    return cp.returncode==0

def copy_as_logika(src_id,name,parent,path,extra=None):
    cp=run(f'gog --account {LOGIKA} --json drive copy {src_id} {json.dumps(name)} --parent {parent}',240)
    rec={'srcId':src_id,'name':name,'path':path,'parentDest':parent,'returncode':cp.returncode,'stdout':cp.stdout[-2000:],'stderr':cp.stderr[-2000:]}
    if extra: rec.update(extra)
    if cp.returncode==0:
        try:
            data=json.loads(cp.stdout); rec['destId']=data.get('file',{}).get('id'); rec['webViewLink']=data.get('file',{}).get('webViewLink')
        except Exception: pass
        log['copied'].append(rec); print('COPY_OK',path,'->',rec.get('destId'))
        return True
    # retry by sharing file directly
    share_source(src_id,'reader')
    cp2=run(f'gog --account {LOGIKA} --json drive copy {src_id} {json.dumps(name)} --parent {parent}',240)
    rec['retry_returncode']=cp2.returncode; rec['retry_stdout']=cp2.stdout[-2000:]; rec['retry_stderr']=cp2.stderr[-2000:]
    if cp2.returncode==0:
        try:
            data=json.loads(cp2.stdout); rec['destId']=data.get('file',{}).get('id'); rec['webViewLink']=data.get('file',{}).get('webViewLink')
        except Exception: pass
        log['copied'].append(rec); print('COPY_OK_RETRY',path,'->',rec.get('destId'))
        return True
    log['errors'].append({'op':'copy','srcId':src_id,'path':path,'error':(cp.stderr or cp.stdout)[-1200:],'retry_error':(cp2.stderr or cp2.stdout)[-1200:]})
    print('COPY_ERR',path,(cp2.stderr or cp2.stdout)[:300])
    return False

# Destination folders
f_idv=mkdir('01_IDENTIDADE_VISUAL_LOGIKA',DEST_ROOT)
f_forms=mkdir('02_FORMULARIOS_BRIEFINGS',DEST_ROOT)
f_docs=mkdir('03_PLANILHAS_E_DOCUMENTOS',DEST_ROOT)
f_prop=mkdir('04_PROPOSTAS',DEST_ROOT)
f_triagem=mkdir('99_TRIAGEM_EMPRESA',DEST_ROOT)

# Share relevant parent folders to allow copy access
for fid in ['1p2ibCUenge-zMD5nYkvCRv-ex7Dz_JbS','1YM3J9OgK_X9jb_BNNPOaN_wEbuQNwt30','1363Ca5U98y3Gnr7XjBA1HWypeGGHdarr','1ytWOD3DwDTB4-M4I3hCUc8byDRAM5Zuo']:
    share_source(fid,'reader')

# IDV folder tree copy
idv_file=LOTES/'PERFIL_DA_EMPRESA_LÓGIKA_CREATIVE_1p2ibCUenge-zMD5nYkvCRv-ex7Dz_JbS.json'
items=json.load(open(idv_file)).get('items',[])
folder_map={'':f_idv}
for it in items:
    path=it.get('path','')
    if it.get('mimeType')=='application/vnd.google-apps.folder':
        parts=path.split('/')
        parent_rel='/'.join(parts[:-1])
        parent_id=folder_map.get(parent_rel,f_idv)
        folder_map[path]=mkdir(parts[-1],parent_id)
for it in items:
    if it.get('mimeType')=='application/vnd.google-apps.folder': continue
    path=it.get('path',''); parts=path.split('/'); parent_rel='/'.join(parts[:-1])
    dest_parent=folder_map.get(parent_rel,f_idv)
    copy_as_logika(it['id'],it.get('name') or parts[-1],dest_parent,path,{'category':'identidade_visual'})

# Selected high-confidence company files outside IDV
selected=[
 ('1EctKFJqehDmOIFnp9h3zLSKWez-QuFvObnMoLJpDHfc','PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA',f_docs,'PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA'),
 ('18EZLKQ8gPWlQq1xmt0diUWCfGUoZ3niMX8LFFW3Rqco','Rapidinho: Me Conta do Seu Negócio! (respostas)',f_forms,'Rapidinho: Me Conta do Seu Negócio! (respostas)'),
 ('1pg2wFusjqwFfA4vbY_BDKrykLPxXj_1xO7gCqbu_rvY','BRIEFING PARA IDENTIDADE VISUAL',f_forms,'BRIEFING PARA IDENTIDADE VISUAL'),
 ('1jtbeCfg5Y5kdvjDvpahEzAu0xp0FvINH25mz9Uv2ta4','Diagnóstico Estratégico - Lógika Creative',f_forms,'Diagnóstico Estratégico - Lógika Creative'),
 ('1ZhXl_PlzmBcuxkeJp_r1AA5sgN_ni9ga5R3uPV-VCmk','Rapidinho: Me Conta do Seu Negócio!',f_forms,'Rapidinho: Me Conta do Seu Negócio!'),
 ('1zK_IUKc7rNC9e9PpV8fvjsG79x9o9-EdwrH2YiUq73E','PROPROSTA PRESTAÇÃO DE SERVIÇO 02',f_prop,'PROPROSTA PRESTAÇÃO DE SERVIÇO 02'),
 ('17slfVN399Xkh3XMNj7jVTj3rbkXrAwQs','Cópia de Raio x da empresa.xlsx',f_triagem,'Cópia de Raio x da empresa.xlsx'),
]
# first selected spreadsheet was already copied in a prior test; copy it again would duplicate. include all anyway? skip to avoid duplicate.
already={'1EctKFJqehDmOIFnp9h3zLSKWez-QuFvObnMoLJpDHfc':'1IlowZmIvb1QQQg-D4TBb-MfQBcGazh1fPZ3bQwQnOcE'}
for src,name,parent,path in selected:
    if src in already:
        log['skipped'].append({'srcId':src,'path':path,'reason':'já copiado em teste válido','destId':already[src]})
        continue
    share_source(src,'reader')
    copy_as_logika(src,name,parent,path,{'category':'alta_confianca'})

# Save log
p=RUN/'resultado_migracao_logika_alta_confianca.json'
p.write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
print('DONE copied',len(log['copied']),'errors',len(log['errors']),'skipped',len(log['skipped']),'log',p)
