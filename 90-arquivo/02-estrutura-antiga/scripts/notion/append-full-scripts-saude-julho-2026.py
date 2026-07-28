import os, re, json, requests, time
from pathlib import Path

for file in ['.env','scripts/.secrets/notion.env']:
    p=Path(file)
    if p.exists():
        for line in p.read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                k,v=line.split('=',1); os.environ.setdefault(k.strip(),v.strip().strip('"'))

H={'Authorization':'Bearer '+os.environ['NOTION_TOKEN'],'Notion-Version':'2022-06-28','Content-Type':'application/json'}
md_path=Path('\\[F2\\] memory/outputs/saude-sao-sebastiao/pautas/2026-07/2026-07-08-calendario-julho-a-partir-de-hoje-v3-rodizio-servicos.md')
result_path=Path('\\[F2\\] memory/outputs/saude-sao-sebastiao/notion/2026-07-08-notion-calendario-julho-a-partir-08-v3-result.json')
notion_out=Path('\\[F2\\] memory/outputs/saude-sao-sebastiao/notion')
notion_out.mkdir(parents=True, exist_ok=True)
md=md_path.read_text(encoding='utf-8')
results=json.loads(result_path.read_text(encoding='utf-8'))['results']
by_date={r['date']:r for r in results}

def rt(text):
    return [{'type':'text','text':{'content':str(text)[:2000]}}]

def block(t, text='', **extra):
    if t=='divider': return {'object':'block','type':'divider','divider':{}}
    obj={'rich_text':rt(text)}; obj.update(extra)
    return {'object':'block','type':t,t:obj}

def split_days(text):
    pat=re.compile(r'^## (\d{2}/\d{2}/\d{4}) — ([^—]+) — (.+)$', re.M)
    matches=list(pat.finditer(text))
    out=[]
    for i,m in enumerate(matches):
        start=m.end(); end=matches[i+1].start() if i+1<len(matches) else len(text)
        out.append((m.group(1),m.group(2).strip(),m.group(3).strip(),text[start:end].strip()))
    return out

def extract(section, label):
    m=re.search(rf'\*\*{re.escape(label)}:\*\*\s*(.*?)(?=\n\n\*\*|\n## |\Z)', section, flags=re.S)
    return m.group(1).strip() if m else ''

def story_items(section):
    st=extract(section,'Stories')
    return [x.strip()[2:].strip() for x in st.splitlines() if x.strip().startswith('- ')]

def mk_full_blocks(date, weekday, macro, section):
    feed=extract(section,'Feed')
    gancho=extract(section,'Gancho')
    abordagem=extract(section,'Abordagem')
    legenda=extract(section,'Legenda sugerida')
    stories=story_items(section)
    # parse feed setor/serviço/formato
    setor_servico=feed
    formato=''
    if '(' in feed and feed.endswith(')'):
        formato=feed[feed.rfind('(')+1:-1]
        setor_servico=feed[:feed.rfind('(')].strip()
    if ' — ' in setor_servico:
        setor, servico = setor_servico.split(' — ',1)
    else:
        setor, servico = setor_servico, ''
    children=[
        block('divider'),
        block('heading_1', f'ROTEIRO COMPLETO — {date} — {weekday}'),
        block('callout','Atualização solicitada por Jadielson: a pauta no Notion deve ficar completa, como enviada no chat — com headline, legenda, cenas sugeridas, stories e observações de captação.',icon={'type':'emoji','emoji':'🎬'}),
        block('heading_2','1. Pauta do dia'),
        block('bulleted_list_item',f'Macrofrente: {macro}'),
        block('bulleted_list_item',f'Setor/unidade protagonista do feed: {setor}'),
        block('bulleted_list_item',f'Serviço específico do feed: {servico}'),
        block('bulleted_list_item',f'Formato sugerido: {formato or "Definir entre reels/carrossel conforme material captado"}'),
        block('paragraph','Regra editorial: o feed dá notoriedade a um serviço específico; os stories mostram serviços de apoio da mesma macrofrente. Evitar transformar o tema do mês no centro da pauta quando não houver ação concreta.'),
        block('heading_2','2. Headline / gancho do feed'),
        block('paragraph',gancho),
        block('heading_2','3. Roteiro do feed — cenas sugeridas'),
        block('numbered_list_item',f'Abertura visual: imagem forte do serviço em funcionamento. Texto na tela: “{gancho}”'),
        block('numbered_list_item',f'Serviço protagonista: mostrar {servico or setor} acontecendo na prática, sem expor dados pessoais, prontuários ou pacientes sem autorização.'),
        block('numbered_list_item',f'Detalhe de rotina: registrar mãos, equipamentos, material de trabalho, equipe orientando ou ambiente preparado para reforçar a veracidade do serviço.'),
        block('numbered_list_item',f'Benefício para a população: conectar o serviço à vida real das famílias — acesso, prevenção, acompanhamento, resolutividade ou acolhimento.'),
        block('numbered_list_item','Fechamento: orientação simples e institucional, sem slogan como carimbo. Se usar a ideia “com coração”, inserir naturalmente no texto.'),
        block('heading_2','4. Abordagem narrativa'),
        block('paragraph',abordagem),
        block('heading_2','5. Legenda sugerida'),
        block('paragraph',legenda),
        block('heading_2','6. Stories completos'),
    ]
    for idx,s in enumerate(stories,1):
        title=s.split(':',1)[0].strip() if ':' in s else f'Story {idx}'
        desc=s.split(':',1)[1].strip() if ':' in s else s
        children += [
            block('heading_3',f'Story {idx} — {title}'),
            block('bulleted_list_item',f'Texto na tela: {desc}'),
            block('bulleted_list_item',f'Cena sugerida: registrar imagem limpa e objetiva relacionada a “{title}”, priorizando equipe, ambiente, material de trabalho ou orientação sem exposição sensível.'),
        ]
    children += [
        block('heading_2','7. Cuidados de captação'),
        block('bulleted_list_item','Não mostrar prontuários, CNS, nomes, resultados de exames, placas de veículos ou documentos identificáveis.'),
        block('bulleted_list_item','Evitar close em pacientes sem autorização expressa. Preferir mãos, ambiente, equipe, equipamentos e planos abertos.'),
        block('bulleted_list_item','Se houver fala de profissional, usar frase curta, objetiva e de orientação pública.'),
        block('heading_2','8. Controle de rodízio'),
        block('paragraph',f'Macrofrente: {macro} | Setor: {setor} | Serviço: {servico} | Formato: {formato}.'),
    ]
    return children

updated=[]
for date,weekday,macro,section in split_days(md):
    if date not in by_date: continue
    page_id=by_date[date]['page_id']
    children=mk_full_blocks(date,weekday,macro,section)
    # append in safe batches
    for i in range(0,len(children),90):
        r=requests.patch(f'https://api.notion.com/v1/blocks/{page_id}/children',headers=H,json={'children':children[i:i+90]},timeout=30)
        if r.status_code>=300:
            raise RuntimeError(f'{date} {r.status_code}: {r.text}')
        time.sleep(0.05)
    # update property description/briefing with a richer but bounded summary
    feed=extract(section,'Feed'); gancho=extract(section,'Gancho'); legenda=extract(section,'Legenda sugerida')
    brief=(f'ROTEIRO COMPLETO NO CORPO DA PÁGINA. Feed: {feed}. Headline: {gancho}. Legenda: {legenda[:900]}')[:1900]
    props={'Briefing/Roteiro':{'rich_text':rt(brief)}, 'Observações':{'rich_text':rt('Pauta revisada: contém roteiro completo com headline, legenda, cenas sugeridas, stories e cuidados de captação no corpo da página.')}}
    rr=requests.patch(f'https://api.notion.com/v1/pages/{page_id}',headers=H,json={'properties':props},timeout=30)
    if rr.status_code>=300:
        print('WARN props',date,rr.status_code,rr.text[:300])
    updated.append({'date':date,'page_id':page_id,'url':by_date[date].get('url')})

out={'ok':True,'updated_count':len(updated),'updated':updated}
(notion_out/'2026-07-08-notion-calendario-julho-full-scripts-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))
