import os, json, requests
from pathlib import Path

for file in ['.env','scripts/.secrets/notion.env']:
    if Path(file).exists():
        for line in Path(file).read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))

T = os.environ['NOTION_TOKEN']
H = {'Authorization': f'Bearer {T}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
principal_db = '1a3207e6-f145-81ed-9513-fb900301f00e'
strategy_page = '1a3207e6-f145-812b-af61-c2e8d16cd79f'
md_path = Path('F2-memory/outputs/saude-sao-sebastiao/sistema-producao/grade-matriz/2026-calendario-editorial-ciclico-saude-v2.md')
md = md_path.read_text()

def rt(text):
    return [{'type': 'text', 'text': {'content': text[:2000]}}]

def block(t, text='', **extra):
    if t == 'divider':
        return {'object': 'block', 'type': 'divider', 'divider': {}}
    obj = {'rich_text': rt(text)}
    obj.update(extra)
    return {'object': 'block', 'type': t, t: obj}

# Find existing item in principal database
res = requests.post(f'https://api.notion.com/v1/databases/{principal_db}/query', headers=H, json={'page_size': 100})
res.raise_for_status()
existing = None
for p in res.json().get('results', []):
    title = ''
    for prop in p.get('properties', {}).values():
        if prop.get('type') == 'title':
            title = ''.join(t.get('plain_text', '') for t in prop.get('title', []))
    if 'Calendário Editorial Cíclico' in title and 'v2' in title:
        existing = p
        break

summary_blocks = [
    block('heading_1', 'Calendário Editorial Cíclico — Saúde SSS v2'),
    block('callout', 'Atualização oficial: macrofrente fixa por dia + rotação por setor/serviço + tema do mês embutido + controle de cobertura total.', icon={'type': 'emoji', 'emoji': '✅'}),
    block('paragraph', 'Versão atualizada em 2026-07-07 a partir da diretriz confirmada por Jadielson. O objetivo é diversificar a produção, incluir toda a estrutura da Secretaria e evitar setores invisíveis.'),
    block('heading_2', 'Grade macro semanal'),
    block('bulleted_list_item', 'Segunda: Atenção Básica / Território — PSFs, ACS, recepção, pré-natal, puericultura, HIPERDIA e rotina das unidades.'),
    block('bulleted_list_item', 'Terça: Serviços Especializados / Saúde Bucal / EMULTI — Espaço Cuidar, CEO, especialidades, exames, cirurgias externas e equipe multiprofissional.'),
    block('bulleted_list_item', 'Quarta: Vigilância / Prevenção — PNI, Endemias, Epidemiologia, Vigilância Sanitária, testes rápidos e campanhas educativas.'),
    block('bulleted_list_item', 'Quinta: Rede de Apoio / Humanização — CAPS, Melhor em Casa, Academia da Saúde, Maternidade, Serviço Social e grupos prioritários.'),
    block('bulleted_list_item', 'Sexta: Flexível / Bastidores / Prestação — SAMU, Unidade Mista, Farmácia, Laboratório, RH, CPD, Controle e Avaliação, Procuradoria, Almoxarifado, Gestão e Conselho.'),
    block('heading_2', 'Regra de uso'),
    block('paragraph', 'O tema do mês entra como camada narrativa, não como substituto da grade. A cada semana, escolher setor/serviço diferente dentro da macrofrente e registrar o que já apareceu para compensar omissões.'),
    block('heading_2', 'Conteúdo completo salvo no Cofre e espelhado abaixo'),
]
chunks = []
for i in range(0, len(md), 1800):
    chunks.append({'object': 'block', 'type': 'code', 'code': {'rich_text': rt(md[i:i+1800]), 'language': 'markdown'}})
children = summary_blocks + chunks

if existing:
    page_id = existing['id']
    url = existing.get('url')
    requests.patch(f'https://api.notion.com/v1/pages/{page_id}', headers=H, json={'archived': False}).raise_for_status()
    patch_children = [block('divider'), block('heading_2', 'Atualização registrada em 2026-07-07'), block('paragraph', 'Nova atualização anexada abaixo. Ver conteúdo completo em blocos de markdown.')] + children
    r = requests.patch(f'https://api.notion.com/v1/blocks/{page_id}/children', headers=H, json={'children': patch_children})
    r.raise_for_status()
    action = 'updated_existing'
else:
    payload = {
        'parent': {'database_id': principal_db},
        'properties': {
            'Nome': {'title': rt('Calendário Editorial Cíclico — Saúde SSS v2')},
            'Status': {'status': {'name': 'Em andamento'}}
        },
        'children': children
    }
    r = requests.post('https://api.notion.com/v1/pages', headers=H, json=payload)
    if r.status_code >= 300:
        raise RuntimeError(r.text)
    data = r.json()
    page_id = data['id']
    url = data.get('url')
    action = 'created'

ref_blocks = [
    block('divider'),
    block('heading_2', 'Atualização — Calendário Editorial Cíclico v2'),
    block('paragraph', f'Calendário v2 criado/atualizado no panorama PRINCIPAL da Saúde. Página: {url}'),
    block('paragraph', 'Diretriz: macrofrente fixa por dia, rotação interna por setor/serviço, tema do mês embutido e controle de cobertura total.')
]
r2 = requests.patch(f'https://api.notion.com/v1/blocks/{strategy_page}/children', headers=H, json={'children': ref_blocks})
r2.raise_for_status()
out = {'ok': True, 'action': action, 'page_id': page_id, 'url': url, 'strategy_page_updated': True}
Path('F2-memory/outputs/saude-sao-sebastiao/notion').mkdir(parents=True, exist_ok=True)
Path('F2-memory/outputs/saude-sao-sebastiao/notion/2026-07-07-notion-calendario-ciclico-v2-update-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(json.dumps(out, ensure_ascii=False, indent=2))
