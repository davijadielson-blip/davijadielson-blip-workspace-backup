import os, json, requests
from pathlib import Path

for file in ['.env','scripts/.secrets/notion.env']:
    if Path(file).exists():
        for line in Path(file).read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))

H = {'Authorization': 'Bearer ' + os.environ['NOTION_TOKEN'], 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
CAL_DB = '30d207e6-f145-80d2-a777-d0f6ea3fef1f'  # Calendário de conteúdo
PROD_DB = '375207e6-f145-8111-bba0-e132fd820542' # Produção & Agenda — LÓGIKA
md = Path('F2-memory/outputs/saude-sao-sebastiao/sistema-producao/grade-matriz/2026-calendario-editorial-ciclico-saude-v2.md').read_text()

def rt(text):
    return [{'type':'text','text':{'content':text[:2000]}}]

def block(t, text='', **extra):
    if t == 'divider':
        return {'object':'block','type':'divider','divider':{}}
    obj = {'rich_text': rt(text)}
    obj.update(extra)
    return {'object':'block','type':t,t:obj}

summary = [
    block('heading_1','PANORAMA — Calendário Editorial Cíclico Saúde SSS v2'),
    block('callout','Item fixo criado no Calendário de conteúdo para ficar visível no panorama operacional. Substitui a lógica anterior por ciclo completo: macrofrente por dia + rotação de setores + tema do mês embutido.', icon={'type':'emoji','emoji':'📌'}),
    block('heading_2','Grade macro'),
    block('bulleted_list_item','Segunda: Atenção Básica / Território.'),
    block('bulleted_list_item','Terça: Serviços Especializados / Saúde Bucal / EMULTI.'),
    block('bulleted_list_item','Quarta: Vigilância / Prevenção.'),
    block('bulleted_list_item','Quinta: Rede de Apoio / Humanização.'),
    block('bulleted_list_item','Sexta: Flexível / Bastidores / Prestação de Contas.'),
    block('heading_2','Regra operacional'),
    block('paragraph','A cada semana, variar o setor/serviço dentro da macrofrente. O tema do mês entra embutido como camada narrativa, sem substituir a grade. Usar sexta e semana 5 para compensar setores invisíveis.'),
    block('heading_2','Setores que precisam entrar no ciclo'),
    block('paragraph','PSFs urbanos, rurais e indígenas; ACS; Espaço Cuidar; CEO; Saúde Bucal; EMULTI; PNI; Endemias; Epidemiologia; Vigilância Sanitária; CAPS; Melhor em Casa; Academia da Saúde; Maternidade; Serviço Social; SAMU; Unidade Mista; Farmácia; Laboratório; RH; CPD; Controle e Avaliação; Procuradoria; Almoxarifado; Gestão; Conselho/Participação Social; exames e cirurgias externas.'),
    block('heading_2','Conteúdo completo'),
]
children = summary
for i in range(0, len(md), 1800):
    children.append({'object':'block','type':'code','code':{'rich_text':rt(md[i:i+1800]),'language':'markdown'}})

def find_page_in_db(db, title_prop, needle):
    r = requests.post(f'https://api.notion.com/v1/databases/{db}/query', headers=H, json={'page_size':100})
    r.raise_for_status()
    for p in r.json().get('results',[]):
        prop = p.get('properties',{}).get(title_prop,{})
        title = ''.join(t.get('plain_text','') for t in prop.get('title',[]))
        if needle in title:
            return p
    return None

results = []
# Create/update visible item in Calendário de conteúdo
needle='[PANORAMA] Calendário Editorial Cíclico — Saúde SSS v2'
existing=find_page_in_db(CAL_DB,'Nome do conteúdo',needle)
props_cal={
    'Nome do conteúdo': {'title': rt(needle)},
    'Status': {'status': {'name':'Aprovado para publicação'}},
    'Tipo de conteúdo': {'select': {'name':'Post em redes sociais'}},
    'Plataforma': {'multi_select': [{'name':'Instagram'}]},
    'Data de publicação': {'date': {'start':'2026-07-07'}}
}
if existing:
    pid=existing['id']; url=existing.get('url')
    requests.patch(f'https://api.notion.com/v1/pages/{pid}',headers=H,json={'properties':props_cal,'archived':False}).raise_for_status()
    requests.patch(f'https://api.notion.com/v1/blocks/{pid}/children',headers=H,json={'children':[block('divider'),block('heading_2','Atualização visível — 2026-07-07')]+children}).raise_for_status()
    action='updated'
else:
    r=requests.post('https://api.notion.com/v1/pages',headers=H,json={'parent':{'database_id':CAL_DB},'properties':props_cal,'children':children})
    if r.status_code>=300: raise RuntimeError(r.text)
    data=r.json(); pid=data['id']; url=data.get('url'); action='created'
results.append({'db':'Calendário de conteúdo','action':action,'page_id':pid,'url':url})

# Create/update item in Produção & Agenda too
needle2='[SAÚDE] Atualizar panorama — Calendário Editorial Cíclico v2'
existing=find_page_in_db(PROD_DB,'Nome',needle2)
props_prod={
    'Nome': {'title': rt(needle2)},
    'Frente/Cliente': {'select': {'name':'SAÚDE SÃO SEBASTIÃO'}},
    'Status': {'select': {'name':'Concluído'}},
    'Origem': {'select': {'name':'Telegram'}},
    'Gera conteúdo?': {'select': {'name':'Sim'}},
    'Prioridade': {'select': {'name':'Alta'}},
    'Data de publicação': {'date': {'start':'2026-07-07'}},
    'Observações': {'rich_text': rt('Atualização visível do calendário cíclico v2 no panorama operacional. Macrofrente fixa por dia, rotação por setor/serviço e tema do mês embutido.')}
}
if existing:
    pid2=existing['id']; url2=existing.get('url')
    requests.patch(f'https://api.notion.com/v1/pages/{pid2}',headers=H,json={'properties':props_prod,'archived':False}).raise_for_status()
    requests.patch(f'https://api.notion.com/v1/blocks/{pid2}/children',headers=H,json={'children':[block('divider'),block('heading_2','Atualização visível — 2026-07-07')]+summary}).raise_for_status()
    action2='updated'
else:
    r=requests.post('https://api.notion.com/v1/pages',headers=H,json={'parent':{'database_id':PROD_DB},'properties':props_prod,'children':summary})
    if r.status_code>=300: raise RuntimeError(r.text)
    data=r.json(); pid2=data['id']; url2=data.get('url'); action2='created'
results.append({'db':'Produção & Agenda — LÓGIKA','action':action2,'page_id':pid2,'url':url2})

out={'ok':True,'results':results}
Path('F2-memory/outputs/saude-sao-sebastiao/notion').mkdir(parents=True,exist_ok=True)
Path('F2-memory/outputs/saude-sao-sebastiao/notion/2026-07-07-notion-calendario-v2-visible-fix-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
