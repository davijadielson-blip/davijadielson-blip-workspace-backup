#!/usr/bin/env python3
import json, csv, pathlib, collections, re, os, hashlib
from datetime import datetime
BASE=pathlib.Path('/data/.openclaw/workspace')
OUT=BASE/'[F2] memory/outputs/central-pessoal'
ROOT=OUT/'drive-pessoal-root-depth1-2026-07-07.json'
LOTES=OUT/'drive_pessoal_lotes_2026-07-07'
REPORT_DIR=OUT/'drive_pessoal_auditoria_completa_2026-07-07'
REPORT_DIR.mkdir(parents=True, exist_ok=True)
folder_mt='application/vnd.google-apps.folder'

def load_items():
    items=[]
    if ROOT.exists():
        for it in json.load(open(ROOT)).get('items',[]):
            it['_top_source']='ROOT'; items.append(it)
    for p in sorted(LOTES.glob('*.json')):
        try: data=json.load(open(p))
        except Exception: continue
        for it in data.get('items',[]):
            it['_top_source']=p.name
            items.append(it)
    # dedup by id+path to avoid exact duplicate inventory records; keep duplicates if same id appears under same path only once
    seen=set(); out=[]
    for it in items:
        key=(it.get('id'), it.get('path') or it.get('name'))
        if key in seen: continue
        seen.add(key); out.append(it)
    return out
items=load_items()
files=[i for i in items if i.get('mimeType')!=folder_mt]
folders=[i for i in items if i.get('mimeType')==folder_mt]

def top_root(path):
    if not path: return '(raiz)'
    return path.split('/')[0]

def norm_name(n):
    n=(n or '').strip().lower()
    n=re.sub(r'^(c[óo]pia de|copy of)\s+','',n)
    n=re.sub(r'\s*\(\d+\)(?=\.)','',n)
    n=re.sub(r'\s+',' ',n)
    return n

def size_int(it):
    try: return int(it.get('size') or 0)
    except Exception: return 0

def human(n):
    n=float(n or 0)
    for u in ['B','KB','MB','GB','TB']:
        if n < 1024 or u=='TB': return f'{n:.1f} {u}'
        n/=1024

# Basic stats
by_top=collections.Counter(top_root(i.get('path') or i.get('name')) for i in items)
by_type=collections.Counter(i.get('mimeType') or 'unknown' for i in files)
by_ext=collections.Counter((pathlib.Path(i.get('name','')).suffix.lower() or '(sem extensão)') for i in files)

# Duplicates candidates by normalized name+size
by_dup=collections.defaultdict(list)
for it in files:
    by_dup[(norm_name(it.get('name')), it.get('size') or '')].append(it)
dup_groups=[(k,v) for k,v in by_dup.items() if len(v)>1 and k[0]]
dup_groups.sort(key=lambda kv: (len(kv[1]), int(kv[0][1] or 0) if str(kv[0][1]).isdigit() else 0), reverse=True)

# Large files
large=sorted(files, key=size_int, reverse=True)[:100]

# Categories / candidates
cats={
 'logika_empresa': ['logika','lógika','creative','cliente','briefing','identidade visual','proposta','prestação de serviço','negócio','empresa'],
 'financeiro': ['financeiro','comprovante','boleto','pagamento','pago','recibo','fatura','pix','banco','cartão','cartao','valor da hora'],
 'sensivel_pessoal': ['cpf','rg','identidade','certidão','certidao','senha','contrato','banco','cartão','cartao','proesp','digitalização','documento'],
 'familia_casa': ['eloah','mãe','mae','maria','casa','aniversario','aniversário','família','familia'],
 'estudos_cursos': ['curso','aula','ebook','livro','mentoria','asimo','youtube','execução máxima','estudos'],
 'fotos_midias': ['foto','fotos','img_','jpg','jpeg','png','heic','arw','mp4','mov'],
}
hits={k:[] for k in cats}
for it in items:
    text=((it.get('path') or '')+' '+(it.get('name') or '')).lower()
    for cat, words in cats.items():
        if any(w in text for w in words): hits[cat].append(it)

# Write CSVs
with open(REPORT_DIR/'duplicatas_candidatas.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['grupo','nome_normalizado','size','ocorrencias','path','id','mimeType'])
    for gi,(k,v) in enumerate(dup_groups,1):
        for it in v:
            w.writerow([gi,k[0],k[1],len(v),it.get('path') or it.get('name'),it.get('id'),it.get('mimeType')])
with open(REPORT_DIR/'arquivos_grandes_top100.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f); w.writerow(['size_bytes','size_human','path','id','mimeType'])
    for it in large:
        w.writerow([size_int(it),human(size_int(it)),it.get('path') or it.get('name'),it.get('id'),it.get('mimeType')])
for cat, arr in hits.items():
    with open(REPORT_DIR/f'candidatos_{cat}.csv','w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(['path','name','id','mimeType','size','modifiedTime'])
        for it in arr:
            w.writerow([it.get('path') or it.get('name'),it.get('name'),it.get('id'),it.get('mimeType'),it.get('size'),it.get('modifiedTime')])

# Markdown report
md=[]
md.append('# Auditoria do Drive pessoal — relatório complementar\n')
md.append(f'**Gerado em:** {datetime.utcnow().isoformat()}Z  \n')
md.append('**Modo:** leitura; nenhuma alteração executada.\n')
md.append('## Sumário numérico\n')
md.append(f'- Itens únicos inventariados: **{len(items)}**\n')
md.append(f'- Pastas: **{len(folders)}**\n')
md.append(f'- Arquivos: **{len(files)}**\n')
md.append(f'- Tamanho conhecido: **{human(sum(size_int(i) for i in files))}**\n')
md.append('\n## Maiores concentrações por raiz/caminho\n')
for k,v in by_top.most_common(25): md.append(f'- `{k}`: **{v}** itens\n')
md.append('\n## Tipos de arquivo mais comuns\n')
for k,v in by_type.most_common(20): md.append(f'- `{k}`: **{v}**\n')
md.append('\n## Extensões mais comuns\n')
for k,v in by_ext.most_common(20): md.append(f'- `{k}`: **{v}**\n')
md.append('\n## Categorias candidatas por nome/caminho\n')
for k,v in hits.items(): md.append(f'- `{k}`: **{len(v)}** candidatos — arquivo: `candidatos_{k}.csv`\n')
md.append('\n## Duplicatas candidatas\n')
md.append(f'- Grupos com mesmo nome normalizado e mesmo tamanho: **{len(dup_groups)}**\n')
for gi,(k,v) in enumerate(dup_groups[:15],1):
    md.append(f'### Grupo {gi}: `{k[0]}` — {len(v)} ocorrências — tamanho {human(int(k[1] or 0) if str(k[1]).isdigit() else 0)}\n')
    for it in v[:8]: md.append(f'- `{it.get("path") or it.get("name")}`\n')
md.append('\n## Arquivos grandes — top 20\n')
for it in large[:20]: md.append(f'- **{human(size_int(it))}** — `{it.get("path") or it.get("name")}`\n')
md.append('\n## Leitura estratégica inicial\n')
md.append('- `ESTUDOS/CURSOS` concentra a maior massa e deve ser tratado como biblioteca/arquivo de formação, com deduplicação assistida.\n')
md.append('- `04_PESSOAL/JADIELSON` e correlatos concentram vida pessoal e potenciais documentos sensíveis; devem ter prioridade na auditoria de privacidade.\n')
md.append('- Existem materiais de LÓGIKA/negócio dentro do Drive pessoal; recomenda-se lista de candidatos para revisão humana antes de qualquer migração.\n')
md.append('- Não há base para exclusão automática; todas as duplicatas são apenas candidatas.\n')
(REPORT_DIR/'relatorio_complementar.md').write_text(''.join(md), encoding='utf-8')

summary={
 'items':len(items),'folders':len(folders),'files':len(files),'known_size_bytes':sum(size_int(i) for i in files),
 'by_top':by_top.most_common(50),'by_type':by_type.most_common(50),'by_ext':by_ext.most_common(50),
 'category_counts':{k:len(v) for k,v in hits.items()}, 'duplicate_group_count':len(dup_groups),
 'top_large':[(size_int(i),i.get('path') or i.get('name'),i.get('id'),i.get('mimeType')) for i in large[:50]],
}
(REPORT_DIR/'summary_complementar.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(REPORT_DIR)
print(json.dumps(summary,ensure_ascii=False,indent=2)[:3000])
