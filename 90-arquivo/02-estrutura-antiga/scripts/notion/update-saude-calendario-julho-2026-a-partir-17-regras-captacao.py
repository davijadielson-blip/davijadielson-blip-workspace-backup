import os, json, time, requests
from pathlib import Path

for file in ['.env','scripts/.secrets/notion.env']:
    p = Path(file)
    if p.exists():
        for line in p.read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))

TOKEN = os.environ['NOTION_TOKEN']
H = {'Authorization': f'Bearer {TOKEN}', 'Notion-Version': '2022-06-28', 'Content-Type': 'application/json'}
PROD_DB = '375207e6-f145-8111-bba0-e132fd820542'
OUT = Path('[F2] memory/outputs/saude-sao-sebastiao/notion')
OUT.mkdir(parents=True, exist_ok=True)

items = [
    {
        'date':'2026-07-17','date_br':'17/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação de contas',
        'tema':'Fluxo da rede em situação de urgência e encaminhamento',
        'protagonista':'Unidade Mista + SAMU + Referências Regionais',
        'formato':'Feed de fotos ou reels curto, conforme material disponível',
        'headline':'Quando a situação aperta, a rede organiza o cuidado com responsabilidade.',
        'roteiro':['Unidade Mista como porta de acolhimento e classificação de risco.','Explicar que a gravidade orienta a prioridade do atendimento.','Mostrar o papel do SAMU/192 em urgência real.','Explicar referências regionais quando o cuidado precisa ir além do município.','Fechar orientando procurar a unidade de referência e acionar 192 em urgência real.'],
        'stories':['Unidade Mista: “Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.”','Classificação de risco: explicar que prioridade depende da gravidade.','SAMU/192: “Na urgência de verdade, o 192 orienta e chega para salvar tempo.”','Referências Regionais: “Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.”','CTA: procure sua unidade de referência; em urgência real, acione 192.'],
        'publicar':'Publicar Unidade Mista + SAMU + Referências Regionais como orientação de fluxo da rede, sem transformar em especializados avulsos.',
        'guardar':'Psiquiatria/Psicologia do Espaço Cuidar, fisioterapia domiciliar ou nas academias, educação física, nutrição em unidade se estiver acontecendo.',
        'validar':'Imagem real de Unidade Mista/SAMU; se algum especializado de sexta é oportunidade forte; qualquer dado de horário, agenda ou quantidade.'
    },
    {'date':'2026-07-20','date_br':'20/07/2026','weekday':'Segunda','macro':'Atenção Básica / Território','tema':'Vacina contra hepatite B: proteção em todas as fases da vida','protagonista':'PNI + sala de vacina + PSFs Karapotó Plak-Ô/Terra Nova','formato':'Reels serviço','headline':'Vacina contra hepatite B: proteção em todas as fases da vida.','roteiro':['Abrir na unidade/sala de vacina ou material educativo.','Mostrar caderneta, orientação e rotina segura sem dados pessoais.','Explicar que hepatite B tem prevenção e vacina em diferentes fases da vida.','Conectar com território e UBS/PSF como porta de orientação.','Fechar chamando para verificar situação vacinal na unidade.'],'stories':['Abertura com headline da vacina contra hepatite B.','Prova visual: sala de vacina, caderneta sem dados ou equipe orientando.','Detalhe técnico simples: vacina e prevenção.','Utilidade pública: procurar UBS/PSF para orientação.','CTA: confira sua caderneta na unidade de referência.'],'publicar':'Publicar PNI/vacinação como Atenção Básica e prevenção no território.','guardar':'Especialistas de segunda só entram se reforçarem continuidade da Atenção Básica; caso contrário, guardar para terça.','validar':'Se a sala de vacina/PNI estará disponível para imagem e se há alguma orientação oficial local.'},
    {'date':'2026-07-21','date_br':'21/07/2026','weekday':'Terça','macro':'Serviços Especializados','tema':'Oftalmologia: visão, diabetes e acesso especializado','protagonista':'Oftalmologia','formato':'Carrossel ou reels se houver imagem forte','headline':'Oftalmologia: visão, diabetes e acesso especializado.','roteiro':['Abrir com gancho sobre visão e prevenção.','Mostrar ambiente/equipe/fluxo ou material educativo sem expor usuário.','Explicar que diabéticos, idosos e crianças podem precisar de avaliação visual.','Reforçar acesso via PSF/UBS e regulação municipal.','Fechar orientando procurar unidade de referência.'],'stories':['Abertura com headline de oftalmologia.','Prova visual do serviço/ambiente/equipe sem exposição.','Detalhe: visão, diabetes, óculos, glaucoma/catarata sem prometer vaga.','Fluxo: PSF/UBS → encaminhamento/regulação.','CTA: procure a unidade de referência.'],'publicar':'Terça é pilar natural para especializados; publicar Oftalmologia como protagonista.','guardar':'Aproveitar materiais captados fora da terça que estavam guardados, se fortalecerem o tema.','validar':'Números, agenda e disponibilidade antes de citar; 600/mês apenas se confirmado para a peça.'},
    {'date':'2026-07-22','date_br':'22/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção','tema':'Vigilância Sanitária protege o que a população consome e utiliza','protagonista':'Vigilância Sanitária','formato':'Reels educativo','headline':'Nem toda proteção aparece, mas ela está presente na rotina da cidade.','roteiro':['Abrir com atuação da VISA como prevenção coletiva.','Mostrar checklist, orientação ou ambiente sem identificar estabelecimento.','Explicar riscos sanitários em alimentos, serviços, medicamentos/cosméticos ou piscinas.','Trazer dica prática para população.','Fechar reforçando orientação e prevenção.'],'stories':['Abertura: proteção coletiva também é rotina.','VISA em orientação/checklist sem expor estabelecimento.','Detalhe técnico simples sobre risco sanitário.','Dica prática para população.','CTA: orientação e fiscalização ajudam a prevenir riscos.'],'publicar':'Publicar VISA/prevenção. Especializado só entra se for prevenção/orientação.','guardar':'Ginecologia ou outro especializado de quarta deve ser captado e guardado se não reforçar prevenção.','validar':'Evitar expor estabelecimento, denúncia ou situação sensível.'},
    {'date':'2026-07-23','date_br':'23/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização','tema':'Maternidade e puerpério: cuidado da gestante ao recém-nascido','protagonista':'Maternidade / puerpério','formato':'Reels humanizado','headline':'Os primeiros cuidados deixam marcas para a vida inteira.','roteiro':['Abrir com ambiente preparado, orientação ou material materno-infantil.','Mostrar acolhimento da gestante/puérpera sem exposição.','Explicar aleitamento, testes do bebê, vacina RN ou urgências obstétricas em linguagem simples.','Conectar com rede de apoio e continuidade do cuidado.','Fechar com orientação para acompanhamento na unidade.'],'stories':['Abertura: cuidado da gestante ao recém-nascido.','Ambiente/material preparado sem expor bebê sem autorização.','Orientação sobre puerpério, aleitamento ou triagens.','Rede de apoio e continuidade do cuidado.','CTA: procure sua unidade para orientação.'],'publicar':'Publicar humanização/rede de apoio. Especializado só entra se reforçar acolhimento e continuidade.','guardar':'Cirurgia Geral/agenda especializada de quinta: captar se houver, guardar para terça se não casar.','validar':'Autorização de imagem de mães/bebês e qualquer informação assistencial.'},
    {'date':'2026-07-24','date_br':'24/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação de contas','tema':'Prestação de contas: ações especializadas e cuidado contínuo','protagonista':'Espaço Cuidar + Odontomóvel + Academia + Farmácia + Assistência Social','formato':'Feed de fotos ou reels de bastidores','headline':'Cuidado contínuo também aparece nos bastidores da rede.','roteiro':['Abrir com bastidores/fluxo de serviços.','Mostrar um protagonista claro do dia e serviços de apoio nos stories.','Explicar como a rede organiza cuidado contínuo sem prometer agenda.','Reconhecer equipes e orientar acesso pela unidade de referência.','Fechar com prestação qualitativa da semana.'],'stories':['Abertura: sexta de bastidores e prestação.','Espaço Cuidar ou serviço protagonista do dia, se fizer sentido.','Academia/Farmácia/Odontomóvel como apoio, conforme imagem disponível.','Orientação de fluxo pela unidade.','CTA institucional de continuidade do cuidado.'],'publicar':'Publicar só o que couber como prestação, bastidor, humanização ou oportunidade forte.','guardar':'Psiquiatria/Psicologia e demais especializados de sexta se não reforçarem o ângulo.','validar':'Qual serviço será protagonista e se há autorização de imagem.'},
    {'date':'2026-07-27','date_br':'27/07/2026','weekday':'Segunda','macro':'Atenção Básica / Território','tema':'UBS na véspera do Dia Mundial das Hepatites: onde buscar orientação','protagonista':'Atenção Básica + Laboratório + PNI; PSFs Grotão/Lagoa Seca/Maracujá/Pedra Preta/Sapé','formato':'Reels chamada','headline':'Na dúvida, a orientação começa na sua unidade de referência.','roteiro':['Abrir na UBS/PSF como porta de entrada.','Mostrar orientação, PNI ou laboratório sem dados pessoais.','Explicar prevenção/testes/vacina como caminho organizado na rede.','Conectar com Dia Mundial das Hepatites sem transformar tudo em campanha genérica.','Fechar orientando procurar a unidade.'],'stories':['Abertura: UBS como ponto de orientação.','PNI/laboratório/recepção em fluxo seguro.','Detalhe sobre hepatites, testes ou vacina.','PSFs do território como referência.','CTA: procure sua unidade para orientação.'],'publicar':'Publicar Atenção Básica/território com gancho de hepatites.','guardar':'Pediatria/Cardiologia ou outros especializados só entram se forem continuidade da Atenção Básica.','validar':'Disponibilidade de imagens em UBS/PNI/Laboratório e orientação oficial.'},
    {'date':'2026-07-28','date_br':'28/07/2026','weekday':'Terça','macro':'Serviços Especializados / campanha focal','tema':'Dia Mundial das Hepatites Virais: prevenir, testar e tratar salva vidas','protagonista':'PNI + Laboratório + Farmácia + Atenção Básica','formato':'Reels principal do mês','headline':'Hepatite pode ser silenciosa; prevenir, testar e tratar salva vidas.','roteiro':['Abrir com data focal e gancho forte.','Mostrar vacina, teste, orientação ou fluxo sem expor dados.','Explicar prevenção, testagem e tratamento de forma simples.','Mostrar a rede integrada: UBS, laboratório, farmácia e acompanhamento.','Fechar com CTA para orientação na unidade.'],'stories':['Abertura: Dia Mundial das Hepatites Virais.','Vacina/teste/material educativo sem dados.','Fluxo de cuidado: UBS, laboratório, farmácia.','Orientação de prevenção sem alarmismo.','CTA: procure sua unidade e tire dúvidas.'],'publicar':'Publicar como peça principal do Julho Amarelo. Por ser terça, pode incorporar materiais especializados pertinentes.','guardar':'Materiais não relacionados à campanha ficam no banco para próximas terças.','validar':'Texto oficial, serviços disponíveis e qualquer dado operacional.'},
    {'date':'2026-07-29','date_br':'29/07/2026','weekday':'Quarta','macro':'Vigilância / Prevenção','tema':'Prevenção continua: hepatites, dengue e segurança sanitária','protagonista':'Vigilância + Endemias + VISA','formato':'Carrossel ou reels se houver campo','headline':'Prevenção é rotina: dentro de casa, na rua e nos serviços.','roteiro':['Abrir com prevenção integrada.','Mostrar Endemias/VISA/orientação sem expor dados.','Trazer checklist prático de prevenção.','Conectar hepatites, dengue e segurança sanitária com serviços reais.','Fechar com corresponsabilidade população + equipe.'],'stories':['Abertura: prevenção continua.','Endemias em campo ou checklist de criadouros.','VISA/orientação sanitária.','Hepatites: informação/teste/vacina quando pertinente.','CTA: prevenção funciona melhor com equipe e população.'],'publicar':'Publicar vigilância/prevenção. Especializado de quarta só entra se reforçar orientação preventiva.','guardar':'Ginecologia/outros especializados sem conexão devem ser guardados.','validar':'Imagens de campo e mensagens técnicas.'},
    {'date':'2026-07-30','date_br':'30/07/2026','weekday':'Quinta','macro':'Rede de Apoio / Humanização','tema':'Rede de apoio: assistência social, CAPS e cuidado sem preconceito','protagonista':'Assistência Social + CAPS + Melhor em Casa + EMULTI','formato':'Reels humanizado','headline':'Cuidar também é acolher sem julgamento e seguir junto.','roteiro':['Abrir com rede de apoio e acolhimento.','Mostrar equipe, ambiente ou rotina sem expor usuários.','Explicar vínculo, família, domicílio e continuidade.','Conectar CAPS, Melhor em Casa, EMULTI e assistência social com cuidado integral.','Fechar com CTA respeitoso para buscar orientação.'],'stories':['Abertura: rede de apoio sem preconceito.','CAPS/assistência/EMULTI em ambiente seguro.','Melhor em Casa ou cuidado domiciliar como continuidade.','Orientação à família/cuidador.','CTA: procure sua unidade/serviço de referência.'],'publicar':'Publicar humanização/rede de apoio. Especializado entra apenas como acolhimento/continuidade.','guardar':'Cirurgia Geral ou especializado sem conexão deve ir para banco de terça.','validar':'Privacidade extrema em saúde mental, vulnerabilidade e domicílio.'},
    {'date':'2026-07-31','date_br':'31/07/2026','weekday':'Sexta','macro':'Flexível / Bastidores / Prestação de contas','tema':'Fechamento do Julho Amarelo: bastidores, equipes e continuidade do cuidado','protagonista':'Balanço qualitativo da rede / todos os setores com recorte seguro','formato':'Reels balanço','headline':'O mês fecha, mas o cuidado continua na rotina da rede.','roteiro':['Abrir com fechamento do mês e continuidade do cuidado.','Usar imagens de bastidores/equipes/serviços sem expor dados.','Reconhecer atuação de diferentes setores sem listar números não confirmados.','Orientar continuidade: UBS, prevenção, acompanhamento e serviços.','Fechar com mensagem institucional de cuidado permanente.'],'stories':['Abertura: fechamento do Julho Amarelo.','Bastidores/equipes da rede.','Prevenção e continuidade do cuidado.','Serviços de apoio captados durante o mês.','CTA: procure sua unidade e mantenha o cuidado em dia.'],'publicar':'Publicar balanço qualitativo e bastidores; números só se confirmados.','guardar':'Especializados de sexta só entram se forem oportunidade forte/humanização.','validar':'Números, balanço oficial e imagens selecionadas.'},
]

capture_by_weekday = {
    'Segunda': [
        'Espaço Cuidar: Pediatria + Cardiologia — captar como continuidade da Atenção Básica; se não reforçar o pilar, guardar para terça.',
        'EMULTI/Fisioterapia: Academia Polo manhã/tarde; Academia Rancho manhã/tarde; Academia Cana Brava manhã/tarde; Lagoa Seca/Gongo/Maracujá; Ranielle visita domiciliar pela manhã.',
        'Psicologia: Gabriel em Peroba; Naely no Espaço Cuidar; Rayane no Espaço Cuidar; Thalita no Espaço Cuidar.',
        'Nutrição: ativa nas unidades; Emanoela com grupo no Rancho na segunda, quando confirmado.'
    ],
    'Terça': [
        'Espaço Cuidar: Pneumologia — terça é pilar natural de Serviços Especializados.',
        'EMULTI/Fisioterapia: Academia Polo tarde; Academia Rancho tarde; Academia Cana Brava manhã/tarde; Lagoa Seca/Gongo/Maracujá; Ranielle visita domiciliar pela manhã.',
        'Psicologia: Gabriel manhã São José e tarde Peroba; Naely Espaço Cuidar; Luciana Espaço Cuidar; Thalita Espaço Cuidar.',
        'Educação Física: Larisse na Academia Cana Brava; captar se reforçar a pauta ou guardar para promoção da saúde.'
    ],
    'Quarta': [
        'Espaço Cuidar: Ginecologia — publicar só se reforçar prevenção/orientação; se não, guardar para terça.',
        'Oftalmologia: primeira quarta-feira do mês; captar na primeira semana quando houver atendimento/agenda confirmada.',
        'EMULTI/Fisioterapia: Academia Polo tarde; Academia Cana Brava manhã/tarde; UBS Flexeiras; Lagoa Seca/Gongo/Maracujá; Lyvia manhã Mata/Cana Brava; Ranielle visita domiciliar pela manhã.',
        'Psicologia: Luciana no Espaço Cuidar; Naely visita domiciliar à tarde; Thalita Espaço Cuidar.',
        'Educação Física: Anny manhã Flexeiras; Larisse tarde Academia Polo.'
    ],
    'Quinta': [
        'Espaço Cuidar: Cirurgia Geral — publicar só se for acolhimento/continuidade; se não, guardar para terça.',
        'EMULTI/Fisioterapia: Academia Polo manhã; Academia Rancho manhã; Academia Cana Brava manhã/tarde; UBS Flexeiras; Janaina tarde Pedra Preta/Capim Branco; Ranielle visita domiciliar pela manhã.',
        'Psicologia: Rayane e Thalita no Espaço Cuidar.',
        'Educação Física: Anny tarde PV Mata; Larisse no Posto São José.',
        'Nutrição: ativa nas unidades; captar se houver atendimento/grupo em rota.'
    ],
    'Sexta': [
        'Espaço Cuidar: Psiquiatria — só publicar hoje se couber como humanização/rede de cuidado/oportunidade forte; senão, guardar para terça.',
        'Psicologia: registro de palestras/visitas às sextas; Rayane e Thalita no Espaço Cuidar — cuidado extremo com privacidade.',
        'EMULTI/Fisioterapia: Academia Polo manhã/tarde; Academia Rancho manhã; Academia Cana Brava manhã/tarde; UBS Flexeiras; Ranielle visita domiciliar pela manhã; Janaina manhã Curralinho/Terra Nova.',
        'Educação Física: Anny manhã Flexeiras e tarde Academia Polo; Larisse tarde Academia Cana Brava.',
        'Nutrição: ativa nas unidades; captar se houver atendimento/grupo em rota.'
    ]
}

def rt(text):
    return [{'type':'text','text':{'content':str(text)[:2000]}}]

def block(t, text='', **extra):
    if t == 'divider':
        return {'object':'block','type':'divider','divider':{}}
    obj = {'rich_text': rt(text)}
    obj.update(extra)
    return {'object':'block','type':t,t:obj}

def page_blocks(it):
    children = [
        block('divider'),
        block('heading_1', f"ATUALIZAÇÃO 17/07 — roteiro + cronogramas de captação"),
        block('callout', 'Regra aplicada: a publicação segue o pilar editorial do dia; os cronogramas dos setores entram como lembrete de captação. Fora da terça, especializado só publica se reforçar o pilar; se não, captar e guardar para a próxima terça de especializados.', icon={'type':'emoji','emoji':'✅'}),
        block('heading_2', '1. Pilar editorial do dia'),
        block('paragraph', f"{it['date_br']} — {it['weekday']} — {it['macro']}"),
        block('heading_2', '2. Pauta principal / protagonista'),
        block('bulleted_list_item', f"Tema: {it['tema']}"),
        block('bulleted_list_item', f"Protagonista: {it['protagonista']}"),
        block('bulleted_list_item', f"Formato sugerido: {it['formato']}"),
        block('heading_2', '3. Headline / gancho'),
        block('paragraph', it['headline']),
        block('heading_2', '4. Roteiro da publicação'),
    ]
    for r in it['roteiro']:
        children.append(block('numbered_list_item', r))
    children.append(block('heading_2', '5. Stories'))
    for s in it['stories']:
        children.append(block('numbered_list_item', s))
    children += [block('heading_2','6. Cronogramas do dia para lembrar captação')]
    for c in capture_by_weekday[it['weekday']]:
        children.append(block('bulleted_list_item', c))
    children += [
        block('heading_2', '7. Decisão editorial'),
        block('bulleted_list_item', f"O que publicar hoje: {it['publicar']}"),
        block('bulleted_list_item', f"O que captar e guardar: {it['guardar']}"),
        block('bulleted_list_item', f"O que validar com Jadielson/SMS: {it['validar']}"),
        block('heading_2', '8. Cuidados fixos'),
        block('bulleted_list_item', 'Não expor pacientes, rostos sem autorização, prontuários, guias, CNS, resultados, documentos, placas de veículos ou telas de sistema.'),
        block('bulleted_list_item', 'Cronograma é lembrete de captação, não autorização automática para divulgar agenda/horário.'),
        block('bulleted_list_item', 'Confirmar dados operacionais antes de publicar: agenda, horários, quantidades, disponibilidade e fluxo.'),
    ]
    return children

def find_by_title(title):
    cursor=None
    while True:
        payload={'page_size':100}
        if cursor: payload['start_cursor']=cursor
        r=requests.post(f'https://api.notion.com/v1/databases/{PROD_DB}/query', headers=H, json=payload, timeout=30)
        r.raise_for_status(); data=r.json()
        for p in data.get('results',[]):
            prop=p.get('properties',{}).get('Nome',{})
            t=''.join(x.get('plain_text','') for x in prop.get('title',[]))
            if t == title:
                return p
        if not data.get('has_more'): return None
        cursor=data.get('next_cursor')

updated=[]
for it in items:
    title=f"SMS São Sebastião — {it['date_br']} — {it['weekday']}"
    page=find_by_title(title)
    if not page:
        raise RuntimeError(f'Página não encontrada: {title}')
    page_id=page['id']
    props={
        'Status': {'select': {'name':'Aguardando aprovação'}},
        'Prioridade': {'select': {'name':'Alta'}},
        'Briefing/Roteiro': {'rich_text': rt(f"ATUALIZAÇÃO 17/07: {it['macro']} | {it['tema']} | Protagonista: {it['protagonista']} | Inclui cronogramas do dia para captação e regra: especializado fora da terça só entra se reforçar o pilar.")},
        'Observações': {'rich_text': rt('Atualizado por Jarvis em 17/07/2026 a partir das regras aprovadas: roteiro/programação deve separar publicação do dia e captação por cronograma dos setores; materiais especializados fora da terça devem ser guardados se não reforçarem o pilar.')},
    }
    pr=requests.patch(f'https://api.notion.com/v1/pages/{page_id}', headers=H, json={'properties':props}, timeout=30)
    if pr.status_code >= 300:
        raise RuntimeError(f'Erro propriedades {title}: {pr.status_code} {pr.text}')
    children=page_blocks(it)
    for i in range(0, len(children), 90):
        rr=requests.patch(f'https://api.notion.com/v1/blocks/{page_id}/children', headers=H, json={'children': children[i:i+90]}, timeout=30)
        if rr.status_code >= 300:
            raise RuntimeError(f'Erro blocos {title}: {rr.status_code} {rr.text}')
        time.sleep(0.05)
    updated.append({'date': it['date_br'], 'title': title, 'page_id': page_id, 'url': page.get('url')})
    time.sleep(0.08)

out={'ok': True, 'updated_count': len(updated), 'updated': updated, 'note': 'Atualizadas somente páginas de 17/07 a 31/07/2026.'}
path=OUT/'2026-07-17-notion-calendario-julho-a-partir-17-regras-captacao-result.json'
path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))
