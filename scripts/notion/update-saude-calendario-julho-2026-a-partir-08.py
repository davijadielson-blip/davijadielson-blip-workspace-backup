import os, json, time, requests
from pathlib import Path

# Load env
for file in ['.env','scripts/.secrets/notion.env']:
    p = Path(file)
    if p.exists():
        for line in p.read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))

TOKEN = os.environ['NOTION_TOKEN']
H = {'Authorization': f'Bearer {TOKEN}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}

# Default timeout for Notion requests
_request = requests.request
def _request_timeout(method, url, **kwargs):
    kwargs.setdefault('timeout', 30)
    return _request(method, url, **kwargs)
requests.request = _request_timeout
CAL_DB = '30d207e6-f145-80d2-a777-d0f6ea3fef1f'
PROD_DB = '375207e6-f145-8111-bba0-e132fd820542'
OUT_DIR = Path('\\[F2\\] memory/outputs/saude-sao-sebastiao/pautas/2026-07')
OUT_DIR.mkdir(parents=True, exist_ok=True)
NOTION_OUT = Path('\\[F2\\] memory/outputs/saude-sao-sebastiao/notion')
NOTION_OUT.mkdir(parents=True, exist_ok=True)

items = [
  {
    'date':'2026-07-08','date_br':'08/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção',
    'feed_sector':'Endemias','feed_service':'Visita domiciliar dos ACE / orientação e eliminação de criadouros','format':'Reels',
    'hook':'Tem cuidado que começa no quintal de casa.',
    'approach':'Prevenção no território: agentes orientando famílias, identificando riscos e reforçando atitudes simples contra criadouros.',
    'caption':'A prevenção também acontece no território.\n\nDurante as visitas, os Agentes de Combate às Endemias orientam as famílias, identificam possíveis criadouros e reforçam cuidados simples que ajudam a proteger toda a comunidade.\n\nEliminar água parada, receber bem o agente identificado e manter o quintal em atenção são atitudes que fazem diferença. É esse cuidado diário, feito com presença e coração, que fortalece a saúde de São Sebastião.',
    'stories':['Abertura: Hoje é dia de prevenção em campo.','ACE: visita, orientação e checagem de possíveis criadouros.','Vigilância Sanitária: orientação e fiscalização de ambientes/serviços sem expor estabelecimentos.','PNI rotina: caderneta de vacinação em dia também é prevenção.','Oftalmologia: atendimento mensal com oftalmologista, serviço que atende quase 50 pessoas e amplia o cuidado com a visão.','Fechamento: prevenção funciona melhor quando equipe e população fazem sua parte.']
  },
  {
    'date':'2026-07-09','date_br':'09/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização',
    'feed_sector':'CAPS','feed_service':'Oficinas terapêuticas / cuidado em liberdade','format':'Carrossel humanizado ou Reels',
    'hook':'Cuidado também se constrói com escuta, vínculo e rotina.',
    'approach':'Mostrar o CAPS como serviço de acompanhamento contínuo, com oficinas e acolhimento sem exposição sensível dos usuários.',
    'caption':'No CAPS, o cuidado vai além da consulta. Ele aparece na escuta, nas oficinas, nos grupos e na construção de vínculos que ajudam cada pessoa a seguir acompanhada com respeito.\n\nA rotina do serviço fortalece a saúde mental com presença, orientação e humanidade, aproximando a rede de quem precisa de apoio contínuo.',
    'stories':['Abertura: cuidar também é acolher.','CAPS: sala/oficina preparada e equipe em rotina.','Atendimento/grupos: mostrar ambiente sem expor usuários.','Serviço Social ou Melhor em Casa como apoio complementar.','Fechamento: saúde mental precisa de cuidado contínuo e respeito.']
  },
  {
    'date':'2026-07-10','date_br':'10/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação',
    'feed_sector':'Laboratório Municipal','feed_service':'Bastidores de organização, qualidade e fluxo de exames','format':'Reels ou carrossel de bastidores',
    'hook':'Antes do resultado chegar, existe uma rotina de cuidado por trás.',
    'approach':'Evidenciar organização interna, segurança e agilidade do laboratório, sem dados pessoais ou exposição de resultados.',
    'caption':'O cuidado também passa pelos bastidores. No Laboratório Municipal, cada etapa da rotina ajuda a dar mais organização, segurança e agilidade aos exames que apoiam o atendimento da população.\n\nÉ um trabalho silencioso, mas essencial para que a rede siga funcionando com responsabilidade.',
    'stories':['Abertura: bastidor também é cuidado.','Laboratório: organização interna e qualidade.','Farmácia/almoxarifado: insumos que sustentam o atendimento.','Unidade Mista/SAMU: prontidão e orientação de fluxo.','Fechamento: organização interna melhora o serviço para a população.']
  },
  {
    'date':'2026-07-13','date_br':'13/07/2026','weekday':'Segunda','macro':'Atenção Básica / Território',
    'feed_sector':'UBS/PSF','feed_service':'Coleta de sangue descentralizada na unidade','format':'Carrossel de fotos',
    'hook':'Quando a coleta acontece mais perto, o cuidado fica mais acessível.',
    'approach':'Mostrar a coleta na UBS como serviço de rotina que facilita acesso e integra a Atenção Básica ao Laboratório.',
    'caption':'A Atenção Básica aproxima serviços importantes da população. A coleta de sangue na unidade ajuda a organizar o acompanhamento, facilita o acesso aos exames e fortalece o cuidado iniciado perto de casa.\n\nCada etapa, da orientação à coleta, faz parte de uma rede que trabalha para tornar o atendimento mais resolutivo.',
    'stories':['Abertura: a semana começa na unidade.','Coleta de sangue: organização e orientação ao usuário.','Enfermagem: preparo, sinais vitais ou acompanhamento.','ACS/recepção: fluxo e orientação.','Fechamento: procure sua unidade para saber o caminho correto.']
  },
  {
    'date':'2026-07-14','date_br':'14/07/2026','weekday':'Terça','macro':'Serviços Especializados / Saúde Bucal / EMULTI',
    'feed_sector':'CEO','feed_service':'Endodontia / atendimento odontológico especializado','format':'Reels curto',
    'hook':'Saúde bucal especializada também é cuidado com qualidade de vida.',
    'approach':'Explicar o CEO como continuidade da saúde bucal quando o caso precisa de atendimento especializado.',
    'caption':'Alguns cuidados em saúde bucal precisam de acompanhamento especializado. No CEO, o atendimento ajuda a dar continuidade aos casos encaminhados, ampliando a resolutividade e evitando que problemas avancem.\n\nÉ a rede funcionando em etapas: a unidade orienta, encaminha e o serviço especializado segue o cuidado.',
    'stories':['Abertura: terça é dia de serviço especializado.','CEO: consultório/equipe em atendimento sem expor paciente.','Fluxo: acesso por encaminhamento da rede.','Saúde Bucal nas UBSs como porta de entrada.','Fechamento: cuidar da boca também é cuidar da saúde.']
  },
  {
    'date':'2026-07-15','date_br':'15/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção',
    'feed_sector':'PNI / Imunização','feed_service':'Rede de frio e organização das vacinas','format':'Carrossel educativo',
    'hook':'Por trás de cada vacina, existe controle, cuidado e responsabilidade.',
    'approach':'Mostrar bastidor seguro da imunização: armazenamento, organização e rotina sem expor dados de lote sensíveis.',
    'caption':'A vacinação começa antes da aplicação. A organização da rede de frio, o cuidado com os imunobiológicos e o trabalho das equipes garantem que a proteção chegue com segurança à população.\n\nManter a caderneta em dia é uma atitude simples, mas por trás dela existe uma rotina inteira de compromisso com a prevenção.',
    'stories':['Abertura: prevenção também tem bastidor.','Rede de frio: organização segura sem dados sensíveis.','Sala de vacina: rotina e orientação.','Caderneta: conferir doses pendentes.','Fechamento: vacina em dia protege a pessoa e a comunidade.']
  },
  {
    'date':'2026-07-16','date_br':'16/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização',
    'feed_sector':'Melhor em Casa','feed_service':'Atendimento domiciliar / cuidado que chega ao usuário','format':'Reels humanizado',
    'hook':'Há cuidados que precisam chegar onde a pessoa está.',
    'approach':'Mostrar preparação/deslocamento/equipe em atendimento domiciliar, preservando identidade e dados sensíveis.',
    'caption':'O atendimento domiciliar aproxima a saúde de quem precisa de acompanhamento contínuo e não consegue chegar com facilidade ao serviço.\n\nCom orientação, presença da equipe e cuidado responsável, o Melhor em Casa ajuda a manter o vínculo da rede com famílias que precisam de atenção mais próxima.',
    'stories':['Abertura: cuidado que chega em casa.','Equipe se preparando/deslocando.','Material de atendimento sem dados sensíveis.','Orientação ao cuidador/família.','Fechamento: acompanhamento contínuo fortalece a recuperação.']
  },
  {
    'date':'2026-07-17','date_br':'17/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação',
    'feed_sector':'Farmácia Municipal','feed_service':'Organização e dispensação de medicamentos','format':'Carrossel de bastidores',
    'hook':'Medicamento organizado é mais segurança para quem precisa do tratamento.',
    'approach':'Mostrar estoque, conferência, dispensação e orientação farmacêutica sem expor usuários.',
    'caption':'A rotina da Farmácia Municipal exige organização, controle e orientação. Cada medicamento dispensado faz parte de um cuidado que precisa chegar de forma segura a quem depende do tratamento.\n\nNos bastidores, a equipe trabalha para manter o fluxo funcionando e apoiar a continuidade do acompanhamento da população.',
    'stories':['Abertura: sexta de bastidores da rede.','Farmácia: organização e conferência.','Orientação ao usuário sem exposição.','Integração com unidades e almoxarifado.','Fechamento: cuidado também é garantir continuidade do tratamento.']
  },
  {
    'date':'2026-07-20','date_br':'20/07/2026','weekday':'Segunda','macro':'Atenção Básica / Território',
    'feed_sector':'UBS/PSF','feed_service':'Pré-natal na Atenção Básica','format':'Reels ou carrossel acolhedor',
    'hook':'O cuidado começa antes do nascimento.',
    'approach':'Mostrar acompanhamento da gestante, caderneta sem dados pessoais, orientação e fluxo da unidade.',
    'caption':'O pré-natal na Atenção Básica acompanha a gestante de perto, orienta a família e ajuda a identificar cuidados importantes em cada fase da gravidez.\n\nNa unidade, esse acompanhamento fortalece a segurança da mãe e do bebê, com acolhimento, vínculo e orientação no tempo certo.',
    'stories':['Abertura: cuidado desde o começo.','Caderneta da gestante sem dados.','Enfermagem/médico orientando.','Vacinação/testes/encaminhamentos como apoio.','Fechamento: gestante deve manter acompanhamento regular na unidade.']
  },
  {
    'date':'2026-07-21','date_br':'21/07/2026','weekday':'Terça','macro':'Serviços Especializados / Saúde Bucal / EMULTI',
    'feed_sector':'EMULTI','feed_service':'Fisioterapia / reabilitação e apoio às equipes','format':'Reels demonstrativo',
    'hook':'Movimento orientado também faz parte do cuidado.',
    'approach':'Mostrar fisioterapia/atividade de reabilitação e o papel multiprofissional no acompanhamento.',
    'caption':'A EMULTI fortalece o cuidado com o olhar de diferentes profissionais. Na fisioterapia, a orientação adequada ajuda na reabilitação, na prevenção de limitações e no acompanhamento de quem precisa recuperar mais autonomia.\n\nQuando a rede trabalha de forma integrada, o usuário encontra mais apoio para seguir o tratamento.',
    'stories':['Abertura: cuidado multiprofissional em ação.','Fisioterapia: exercício/orientação sem exposição indevida.','Integração com UBS/PSF.','Outro profissional EMULTI como apoio.','Fechamento: cada especialidade contribui para um cuidado mais completo.']
  },
  {
    'date':'2026-07-22','date_br':'22/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção',
    'feed_sector':'Vigilância Sanitária','feed_service':'Orientação sanitária em estabelecimentos e serviços','format':'Carrossel educativo',
    'hook':'Nem toda proteção aparece, mas ela está presente na rotina da cidade.',
    'approach':'Mostrar atuação orientativa/fiscalizatória da VISA sem expor estabelecimento, nome ou situação sensível.',
    'caption':'A Vigilância Sanitária atua para reduzir riscos e proteger a saúde da população em ambientes, produtos e serviços. A orientação aos estabelecimentos ajuda a melhorar práticas, prevenir problemas e dar mais segurança ao que chega à comunidade.\n\nÉ um cuidado que muitas vezes acontece longe dos olhos, mas faz diferença no dia a dia de todos.',
    'stories':['Abertura: proteção coletiva também é rotina.','Checklist/prancheta de orientação.','Ambiente/serviço sem identificação.','Dica de segurança sanitária para população.','Fechamento: fiscalização e orientação ajudam a prevenir riscos.']
  },
  {
    'date':'2026-07-23','date_br':'23/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização',
    'feed_sector':'Academia da Saúde','feed_service':'Grupo de atividade física orientada','format':'Reels leve e dinâmico',
    'hook':'Movimento também é cuidado preventivo.',
    'approach':'Mostrar atividade orientada, convivência, prevenção e qualidade de vida.',
    'caption':'Na Academia da Saúde, o movimento vira rotina de cuidado. As atividades orientadas ajudam na prevenção, na convivência e no fortalecimento da qualidade de vida de quem participa.\n\nCuidar da saúde também é criar espaços para o corpo se movimentar, a comunidade se encontrar e a prevenção acontecer de forma simples.',
    'stories':['Abertura: movimento é saúde.','Grupo em atividade orientada.','Profissional conduzindo alongamento/exercício.','Benefícios para idosos/crônicos/comunidade.','Fechamento: participar das atividades é investir em qualidade de vida.']
  },
  {
    'date':'2026-07-24','date_br':'24/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação',
    'feed_sector':'Unidade Mista','feed_service':'Pronto atendimento / classificação e fluxo de urgência','format':'Reels de orientação de fluxo',
    'hook':'Na urgência, entender o fluxo ajuda o cuidado chegar melhor.',
    'approach':'Explicar porta de entrada da Unidade Mista, classificação/observação/estabilização e quando procurar o serviço.',
    'caption':'A Unidade Mista é referência para situações que exigem atendimento de urgência. A organização do fluxo ajuda a acolher, avaliar e direcionar cada caso conforme a necessidade.\n\nSaber quando procurar a unidade, a UBS ou o SAMU também é uma forma de colaborar para que a rede funcione melhor para todos.',
    'stories':['Abertura: sexta com orientação de fluxo.','Fachada/recepção da Unidade Mista.','Classificação/observação sem pacientes expostos.','SAMU 192: quando acionar.','Fechamento: serviço certo no momento certo melhora o atendimento.']
  },
  {
    'date':'2026-07-27','date_br':'27/07/2026','weekday':'Segunda','macro':'Atenção Básica / Território',
    'feed_sector':'ACS / PSF','feed_service':'Visita domiciliar e acompanhamento das famílias','format':'Reels no território',
    'hook':'A saúde também bate à porta.',
    'approach':'Mostrar ACS no território, cadastro/acompanhamento/orientação, sem expor dados pessoais.',
    'caption':'Os Agentes Comunitários de Saúde mantêm o vínculo entre a unidade e as famílias. Nas visitas, acompanham situações de saúde, orientam sobre serviços e ajudam a rede a enxergar melhor as necessidades do território.\n\nÉ presença diária, perto da população, fortalecendo o cuidado antes que muitos problemas cheguem à porta da unidade.',
    'stories':['Abertura: saúde no território.','ACS em rota/visita.','Orientação de rotina sem dados pessoais.','Busca ativa/acompanhamento de família.','Fechamento: mantenha seus dados atualizados com a equipe.']
  },
  {
    'date':'2026-07-28','date_br':'28/07/2026','weekday':'Terça','macro':'Serviços Especializados / Saúde Bucal / EMULTI',
    'feed_sector':'Espaço Cuidar','feed_service':'Ultrassonografia / exame especializado','format':'Carrossel ou Reels curto',
    'hook':'Exame especializado ajuda o cuidado a seguir com mais precisão.',
    'approach':'Mostrar atendimento de ultrassonografia como continuidade do cuidado via encaminhamento/regulação.',
    'caption':'A ultrassonografia é um dos serviços que ajudam a rede a investigar, acompanhar e direcionar melhor o cuidado dos usuários.\n\nCom encaminhamento e organização do fluxo, o atendimento especializado dá mais suporte às decisões clínicas e fortalece a resolutividade dentro do município.',
    'stories':['Abertura: serviço especializado em destaque.','Ultrassom: equipamento/ambiente sem exposição.','Fluxo por encaminhamento da unidade.','Outro serviço do Espaço Cuidar como apoio.','Fechamento: acompanhamento correto começa pela unidade de referência.']
  },
  {
    'date':'2026-07-29','date_br':'29/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção',
    'feed_sector':'Testes rápidos / IST','feed_service':'Orientação e testagem como prevenção','format':'Carrossel informativo',
    'hook':'Prevenir também é tirar dúvidas e buscar orientação sem medo.',
    'approach':'Trabalhar testagem/IST/hepatites como serviço concreto, sem transformar o mês inteiro em campanha.',
    'caption':'Os testes rápidos e a orientação em saúde ajudam a identificar riscos, esclarecer dúvidas e encaminhar o cuidado no tempo certo.\n\nBuscar informação é uma atitude de responsabilidade. Na rede municipal, a prevenção acontece com acolhimento, sigilo e orientação para que cada pessoa saiba o melhor caminho a seguir.',
    'stories':['Abertura: prevenção sem tabu.','Testes rápidos: material/ambiente sem exposição.','Orientação sobre sigilo e acolhimento.','Quando procurar a unidade.','Fechamento: informação correta ajuda a proteger.']
  },
  {
    'date':'2026-07-30','date_br':'30/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização',
    'feed_sector':'Maternidade Municipal','feed_service':'Triagem neonatal / cuidado mãe-bebê','format':'Carrossel humanizado',
    'hook':'Os primeiros cuidados deixam marcas para a vida inteira.',
    'approach':'Mostrar cuidado no nascimento/puerpério/triagens, com extrema atenção à autorização de imagem.',
    'caption':'Na maternidade, cada orientação ajuda a proteger a mãe e o bebê nos primeiros momentos de cuidado. A triagem neonatal, o acolhimento e o acompanhamento no puerpério fazem parte de uma rede que começa cedo e segue orientando a família.\n\nÉ cuidado com delicadeza, responsabilidade e presença nos detalhes que importam.',
    'stories':['Abertura: cuidado desde os primeiros dias.','Ambiente preparado/berço/material, sem expor bebê sem autorização.','Orientação sobre triagem neonatal.','Aleitamento/puerpério como apoio.','Fechamento: família orientada é cuidado fortalecido.']
  },
  {
    'date':'2026-07-31','date_br':'31/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação',
    'feed_sector':'Almoxarifado / Gestão de insumos','feed_service':'Recebimento, armazenamento e distribuição de materiais','format':'Reels de prestação/bastidor',
    'hook':'Para o atendimento acontecer, o material precisa chegar antes.',
    'approach':'Fechamento do mês com bastidor de organização de insumos e prestação leve de funcionamento da rede.',
    'caption':'O funcionamento da saúde também depende de planejamento e organização de materiais. No almoxarifado, o recebimento, armazenamento e distribuição de insumos ajudam os serviços a manterem sua rotina de atendimento.\n\nFechar o mês mostrando esse bastidor é lembrar que cada detalhe administrativo também sustenta o cuidado que chega à população.',
    'stories':['Abertura: último dia útil do mês com bastidores.','Almoxarifado: recebimento/organização/distribuição.','Gestão/planejamento: rede se organiza para funcionar.','Compensação: lembrar serviço pouco visível do mês.','Fechamento: bastidores também cuidam da população.']
  },
]

def rt(text):
    return [{'type':'text','text':{'content':text[:2000]}}]

def block(t, text='', **extra):
    if t == 'divider':
        return {'object':'block','type':'divider','divider':{}}
    obj = {'rich_text': rt(text)}
    obj.update(extra)
    return {'object':'block','type':t,t:obj}

def page_blocks(item):
    children = [
        block('heading_1', f"{item['date_br']} — {item['weekday']} — {item['macro']}"),
        block('callout', 'VERSÃO ATUALIZADA — calendário recriado a partir de 08/07 com rodízio por serviço específico, feed com um protagonista e stories de apoio. Tema do mês não domina a pauta.', icon={'type':'emoji','emoji':'✅'}),
        block('heading_2', 'Feed do dia — serviço protagonista'),
        block('bulleted_list_item', f"Setor/unidade: {item['feed_sector']}"),
        block('bulleted_list_item', f"Serviço específico: {item['feed_service']}"),
        block('bulleted_list_item', f"Formato sugerido: {item['format']}"),
        block('bulleted_list_item', f"Gancho: {item['hook']}"),
        block('paragraph', f"Abordagem: {item['approach']}"),
        block('heading_3', 'Legenda sugerida'),
        block('paragraph', item['caption']),
        block('heading_2', 'Stories de apoio'),
    ]
    for s in item['stories']:
        children.append(block('bulleted_list_item', s))
    children += [
        block('heading_2', 'Controle do rodízio'),
        block('paragraph', f"Macrofrente: {item['macro']} | Setor: {item['feed_sector']} | Serviço protagonista: {item['feed_service']} | Formato: {item['format']}"),
        block('paragraph', 'Observação: os stories podem mostrar serviços complementares da macrofrente, mas o feed mantém apenas um serviço como protagonista.'),
    ]
    return children

# Generate markdown file
md = ['---','frente: saude-sao-sebastiao','tipo: calendario-mensal-atualizado','periodo: 2026-07-08 a 2026-07-31','status: atualizado-notion','criado_em: 2026-07-08','---','','# Calendário Saúde São Sebastião — Julho/2026 — atualizado a partir de 08/07','','## Regra aplicada','','Macrofrente fixa por dia → setor/unidade → serviço específico protagonista do feed → stories de apoio. O tema do mês deixa de ser eixo dominante e só aparece quando houver ação real e pertinência.','','## Calendário operacional','']
for it in items:
    md += [f"## {it['date_br']} — {it['weekday']} — {it['macro']}", '', f"**Feed:** {it['feed_sector']} — {it['feed_service']} ({it['format']})", '', f"**Gancho:** {it['hook']}", '', f"**Abordagem:** {it['approach']}", '', '**Legenda sugerida:**', '', it['caption'], '', '**Stories:**']
    for s in it['stories']:
        md.append(f"- {s}")
    md.append('')
md_path = OUT_DIR / '2026-07-08-calendario-julho-a-partir-de-hoje-v3-rodizio-servicos.md'
md_path.write_text('\n'.join(md), encoding='utf-8')

# Build lookup from previous imported pages when available
lookup = {}
old = Path('\\[F2\\] memory/outputs/notion-import-saude-julho-2026-results.json')
if old.exists():
    for row in json.loads(old.read_text()):
        lookup[row.get('date')] = row

# Helpers for Notion

def list_children(block_id):
    out=[]; cursor=None
    while True:
        params={'page_size':100}
        if cursor: params['start_cursor']=cursor
        r=requests.get(f'https://api.notion.com/v1/blocks/{block_id}/children', headers=H, params=params)
        r.raise_for_status(); data=r.json(); out.extend(data.get('results',[]))
        if not data.get('has_more'): break
        cursor=data.get('next_cursor')
    return out

def archive_children(page_id):
    for b in list_children(page_id):
        bid=b['id']
        rr=requests.patch(f'https://api.notion.com/v1/blocks/{bid}', headers=H, json={'archived': True})
        # continue on already archived/permission hiccups
        if rr.status_code >= 300:
            print('WARN archive', bid, rr.status_code, rr.text[:200])
        time.sleep(0.03)

def find_by_title(title):
    r=requests.post(f'https://api.notion.com/v1/databases/{CAL_DB}/query', headers=H, json={'page_size':100})
    r.raise_for_status()
    for p in r.json().get('results',[]):
        prop=p.get('properties',{}).get('Nome do conteúdo',{})
        t=''.join(x.get('plain_text','') for x in prop.get('title',[]))
        if t == title:
            return p
    return None

results=[]
for it in items:
    title=f"SMS São Sebastião — {it['date_br']} — {it['weekday']}"
    page_id=None; url=None; action=''
    row=lookup.get(it['date_br'])
    if row:
        page_id=row['id']; url=row.get('url')
    else:
        found=find_by_title(title)
        if found:
            page_id=found['id']; url=found.get('url')
    # Existing July pages are in Produção & Agenda — LÓGIKA, not in the public content calendar DB.
    # Use that database schema.
    props={
        'Nome': {'title': rt(title)},
        'Status': {'select': {'name':'Aguardando aprovação'}},
        'Tipo de conteúdo': {'multi_select': [{'name':'Stories'}, {'name':'Texto/Legenda'}, {'name':'Reels'} if 'Reels' in it['format'] else {'name':'Carrossel'}]},
        'Plataforma': {'multi_select': [{'name':'Instagram'}, {'name':'Facebook'}]},
        'Frente/Cliente': {'select': {'name':'Secretaria de Saúde'}},
        'Origem': {'select': {'name':'Telegram'}},
        'Gera conteúdo?': {'select': {'name':'Sim'}},
        'Prioridade': {'select': {'name':'Alta'}},
        'Data de publicação': {'date': {'start': it['date']}},
        'Data do evento': {'date': {'start': it['date']}},
        'Briefing/Roteiro': {'rich_text': rt(f"{it['macro']} | Feed protagonista: {it['feed_sector']} — {it['feed_service']} | Stories de apoio no corpo da página.")},
        'Observações': {'rich_text': rt('Calendário atualizado em 08/07: rodízio por serviço específico, feed com um protagonista por dia, stories de apoio e tema do mês sem dominar a pauta.')},
    }
    children=page_blocks(it)
    if page_id:
        requests.patch(f'https://api.notion.com/v1/pages/{page_id}', headers=H, json={'properties':props,'archived':False}).raise_for_status()
        # Não apagamos blocos antigos para evitar latência/rate limit; anexamos uma versão atualizada no topo lógico.
        children = [block('divider'), block('heading_1', 'ATUALIZAÇÃO 08/07 — versão revisada')] + children
        # append in batches <=100
        for i in range(0, len(children), 90):
            requests.patch(f'https://api.notion.com/v1/blocks/{page_id}/children', headers=H, json={'children':children[i:i+90]}).raise_for_status()
        action='updated'
    else:
        r=requests.post('https://api.notion.com/v1/pages', headers=H, json={'parent':{'database_id':PROD_DB},'properties':props,'children':children})
        if r.status_code>=300:
            raise RuntimeError(r.text)
        data=r.json(); page_id=data['id']; url=data.get('url'); action='created'
    results.append({'date':it['date_br'],'title':title,'action':action,'page_id':page_id,'url':url})
    time.sleep(0.08)

out={'ok':True,'updated_count':len(results),'markdown':str(md_path),'results':results}
(NOTION_OUT / '2026-07-08-notion-calendario-julho-a-partir-08-v3-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))
