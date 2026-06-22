---
tipo: calendario-editorial
frente: saude-sao-sebastiao-social-media
cliente: "SMS São Sebastião"
mes: 2026-07
campanha_central: "Julho Amarelo — prevenção às hepatites virais"
semana: 1
periodo: "2026-07-01 a 2026-07-03"
gerado_por: "Jarvis / LÓGIKA"
revisado: false
status: draft-para-validacao-humana
fonte_de_verdade: "WORKSPACE NATURAL — F1 Frentes + F2 memory"
observacao: "Publicação depende de validação humana de Jadielson e confirmação operacional da SMS."
---

# SAÚDE — SOCIAL MEDIA · JULHO/2026 · SEMANA 1

## Confirmação
- Julho/2026 começa em uma quarta-feira: 01/07/2026.
- Campanha central: Julho Amarelo — prevenção às hepatites virais.
- Data focal localizada no banco: 28/07 — Dia Mundial das Hepatites Virais.

## Provas de base e ferramentas

### Banco/F1 e F2
- `[F1] 5-Frentes/Saude-Sao-Sebastiao/00 - Saúde São Sebastião - MOC.md`: “Município | São Sebastião — AL”; “Regional | 7ª Regional de Saúde (AL)”; “Cobertura ESF | ~92% da população”; “Total UBS | 28 unidades”.
- `[F2] memory/agents/saude.md`: “Uma voz institucional, humana, útil e presente — que mostra serviço real, orienta com clareza e fala com a população sem burocracia nem artificialidade”; “Stories — Meta mínima: 5 por dia útil”.
- `[F2] memory/databases/datas-sazonais/campanhas-saude/julho-amarelo.md`: `descricao: Julho Amarelo — Hepatites Virais`; `observacao: Campanha de prevenção às hepatites A, B e C.`
- `[F2] memory/databases/datas-sazonais/campanhas-saude/dia-hepatite.md`: `data: 2026-07-28`; `descricao: Dia Mundial das Hepatites Virais`; `observacao: Data focal do Julho Amarelo.`

### Arquivos F1 específicos lidos para a Semana 1
- `PNI/PNI.md`: PNI coordena “ações de imunização”; possui “Sala de Vacinação em cada UBS e PSF” e “Central de Rede de Frio”; calendário inclui “Adultos: Influenza anual, dT, Hepatites” e “Gestantes: dTpa, Influenza, Hepatite B”.
- `Vigilância Sanitária/Vigilância Sanitária.md`: VISA protege a saúde mediante “controle sanitário de produtos, serviços, ambientes e processos”; atua em estabelecimentos de saúde, alimentos, medicamentos/cosméticos e meio ambiente/saúde, incluindo salões de beleza.
- `Endemias/Endemias.md`: monitora dengue, esquistossomose, chikungunya, zika; realiza LIRAa; visitas dos ACE com “orientações durante as visitas” e “mapeamento de imóveis e focos ativos”.
- `EMULTI/EMULTI.md`: programa municipal de assistência domiciliar especializada; evita internações desnecessárias; faz atendimentos compartilhados, individuais, em grupo, matriciamento e visitas domiciliares.
- `CAPS/CAPS.md`: referência municipal em saúde mental comunitária; tratamento em liberdade; oferece atendimento individual, grupos, oficinas terapêuticas, visitas domiciliares, atendimento à família e acolhimento em crise.
- `Melhor em Casa/Melhor em Casa.md`: programa federal de atenção domiciliar; equipe EMAD; atende pacientes pós-hospitalização, idosos acamados, pacientes crônicos complexos, cuidados paliativos e pessoas com deficiência grave.
- `Espaço Cuidar/Espaço Cuidar.md`: centro de atenção especializada ambulatorial; acesso via encaminhamento pelos PSFs e UBSs; complementa a Atenção Básica sem substituí-la.
- `SAMU/SAMU.md`: serviço de urgência móvel; número 192; abrangência regional com base descentralizada; atendimento no local e remoção segura.
- `Unidade Mista/Unidade Mista.md`: referência municipal para urgências; pronto atendimento 24h; estabilização antes de transferência; articulação com SAMU e referência hospitalar.
- `Referência Hospitalar.md`: fluxo São Sebastião → Arapiraca → Maceió; regulação municipal/estadual; transporte sanitário para pacientes regulados.

### Tavily / web
- `web_search` usado com provider `tavily`.
- Link oficial usado: Ministério da Saúde — Calendário de Saúde / Julho: https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/c/calendario/saude/julho
  - Retorno Tavily: “Julho amarelo - Mês de luta contra as hepatites virais. (Data instituída pela Lei nº 13.802/2019)” e “28/07 - Dia Mundial de Luta Contra as Hepatites Virais”.
- Indicadores Hepatites / Ministério da Saúde: https://indicadoreshepatites.aids.gov.br/
  - `web_fetch` confirmou “Planilha de todos os municípios” em `/documentos/PainelHepatites.xlsx`.
- PainelHepatites.xlsx, fonte SINAN/SVSA/MS, município São Sebastião/AL código 270880: 22 casos totais; A 11; B 10; C 1; D 0. Validar com Jadielson antes de publicar.

### MCPs / Drive / Canva / Notion / Ecossistema
- Drive via `gog`, conta `logikacreative.mkt@gmail.com`: consegui buscar e localizar pastas/ativos prováveis: `SAÚDE SÃO SEBASTIÃO`, `SAÚDE - SÃO SEBASTIÃO`, `LOGO_MARCA`, `LOGOS_ASSINATURAS`, `LOGO MARCA E POSICIONAMENTO`, `LOGOS`. Para uso visual final, precisa abrir/baixar/validar os ativos oficiais.
- Canva MCP: NÃO CONSEGUI — não há ferramenta Canva disponível nesta sessão.
- Notion MCP: NÃO CONSEGUI — não há ferramenta Notion disponível nesta sessão.
- Lôh/CCO/CMO/CIO como subagentes: NÃO CONSEGUI acionar; `agents_list` retornou apenas `jarvis`. Não simulei retorno.

---

## 01/07 — Quarta-feira
**Pilar fixo:** Vigilância / Prevenção  
**Hierarquia do tema:** campanha do mês manda — abertura do Julho Amarelo.  
**Setores/serviços do dia:** Campanha/Educação em Saúde, PNI, Vigilância Sanitária, Endemias.  
**Post de feed:** sim.  
**Reel:** sim.

### Stories — 5 unidades

Story 1 — [Julho Amarelo / Educação em Saúde — Vigilância / Prevenção; ancorado em `julio-amarelo.md` + Calendário MS]
Cenas sugeridas (mín. 3):
• calendário de julho sobre a mesa, com o dia 01/07 circulado em amarelo;  
• cartaz “Julho Amarelo — hepatites virais” sendo colocado na recepção ou mural da Secretaria;  
• profissional segurando material com três palavras visíveis: “prevenção”, “vacinação”, “orientação”.
Headline/Legenda: **Julho começa com um alerta para você: hepatite pode ser silenciosa, mas a orientação chega antes do medo.**

Story 2 — [PNI / Sala de Vacina — Vigilância / Prevenção; ancorado em `PNI.md`]
Cenas sugeridas (mín. 3):
• cartão de vacina aberto sobre o balcão, com nome e dados fora do enquadramento;  
• profissional folheando a caderneta e apontando para a parte de hepatites/vacinas;  
• sala de vacina ou rede de frio em plano aberto, sem mostrar lote, senha, tela ou informação restrita.
Headline/Legenda: **Seu cartão de vacina pode mostrar se sua proteção precisa de atenção: leve à unidade e confira com a equipe.**

Story 3 — [Vigilância Sanitária / Materiais seguros — Vigilância / Prevenção; ancorado em `Vigilância Sanitária.md`]
Cenas sugeridas (mín. 3):
• alicate, lâmina ou objeto perfurocortante embalado/esterilizado em close;  
• coletor de perfurocortantes em bancada limpa;  
• profissional apontando para uma plaquinha: “material esterilizado ou descartável”.
Headline/Legenda: **Antes do alicate encostar em você, observe o cuidado: material seguro também previne hepatites.**

Story 4 — [Educação em Saúde / Hepatites A, B e C — Vigilância / Prevenção; ancorado em `julio-amarelo.md`]
Cenas sugeridas (mín. 3):
• quadro ou folha com “Hepatite A, B e C” escrito em letras grandes;  
• profissional gravando fala curta com fundo neutro e linguagem simples;  
• close em folder com perguntas: “como prevenir?”, “quando buscar orientação?”, “onde procurar?”.
Headline/Legenda: **Se você entende como a hepatite se transmite, fica mais fácil proteger sua rotina e sua família.**

Story 5 — [Endemias / LIRAa e prevenção em julho — Vigilância / Prevenção; ancorado em `Endemias.md`]
Cenas sugeridas (mín. 3):
• agente de endemias com prancheta chegando a uma rua, sem identificar residência;  
• recipiente sendo vistoriado ou virado para evitar água parada;  
• prancheta do ACE com dados cobertos e orientação visual “10 minutos no quintal”.
Headline/Legenda: **Julho também pede cuidado no quintal: se o agente de endemias passar aí, ele está do seu lado.**

### Reel — [Abertura Julho Amarelo — Vigilância / Prevenção]
Gancho 0–3s: **Hepatite pode ficar em silêncio. A prevenção não pode.**  
Cenas sugeridas (mín. 3):
• calendário de julho sendo marcado no dia 01/07;  
• cartão de vacina conferido por profissional, com dados protegidos;  
• alicate/lâmina ou material perfurocortante embalado em bancada limpa;  
• profissional mostrando três palavras: “vacina”, “prevenção”, “orientação”;  
• tela final: “Julho Amarelo — procure orientação na rede de saúde”.
Legenda: **Julho Amarelo reforça a prevenção às hepatites virais. Informação clara, vacinação quando indicada, materiais seguros e orientação na rede ajudam você a cuidar antes do risco. Validar disponibilidade de testagem/vacinação e fluxos locais com Jadielson antes de publicar.**

### Post de feed — [Abertura do Julho Amarelo]
Headline: **Julho Amarelo: informação, vacina e orientação para proteger você antes do risco.**
Legenda: **Começa o Julho Amarelo, mês de prevenção às hepatites virais. A campanha reforça cuidados importantes: conferir a vacinação quando indicado, não compartilhar objetos cortantes, observar materiais seguros e procurar orientação na rede de saúde. Hepatite pode ser silenciosa; informação clara também é cuidado. Validar fluxos locais antes de publicar.**

---

## 02/07 — Quinta-feira
**Pilar fixo:** Rede de Apoio / Humanização  
**Hierarquia do tema:** Julho Amarelo como pano de fundo; pilar organiza acolhimento, escuta e orientação sem tabu.  
**Setores/serviços do dia:** EMULTI, CAPS, Melhor em Casa, Espaço Cuidar.  
**Post de feed:** sim.  
**Reel:** sim.

### Stories — 5 unidades

Story 1 — [EMULTI / Atenção domiciliar especializada — Rede de Apoio / Humanização; ancorado em `EMULTI.md`]
Cenas sugeridas (mín. 3):
• profissional da EMULTI separando material de orientação domiciliar sobre mesa limpa;  
• folha com “alimentação, remédio, cuidado em casa” ao lado de caneta, sem dados de paciente;  
• profissional falando em plano médio: “se tiver dúvida, procure a equipe”.
Headline/Legenda: **Quando a orientação entra na sua rotina de casa, o cuidado fica mais possível para você e sua família.**

Story 2 — [CAPS / Escuta e cuidado em liberdade — Rede de Apoio / Humanização; ancorado em `CAPS.md`]
Cenas sugeridas (mín. 3):
• cadeiras em roda antes de uma atividade, sem usuários identificáveis;  
• mesa de oficina terapêutica com papel, tinta, lápis ou artesanato;  
• cartaz com “escuta, vínculo, respeito” em parede ou mesa.
Headline/Legenda: **Se a dúvida vem com medo ou vergonha, o CAPS lembra: cuidado começa com escuta e respeito.**

Story 3 — [Melhor em Casa / Atenção domiciliar — Rede de Apoio / Humanização; ancorado em `Melhor em Casa.md`]
Cenas sugeridas (mín. 3):
• bolsa de atendimento domiciliar sendo preparada;  
• material de curativo/luvas sobre mesa, sem paciente;  
• equipe saindo para visita em plano externo, sem mostrar endereço ou residência identificável.
Headline/Legenda: **Para quem não consegue ir até a unidade, a orientação pode chegar com cuidado até a família.**

Story 4 — [Espaço Cuidar / Encaminhamento especializado — Rede de Apoio / Humanização; ancorado em `Espaço Cuidar.md`]
Cenas sugeridas (mín. 3):
• sala ou recepção do Espaço Cuidar com cadeiras vazias ou fluxo sem identificação;  
• guia/encaminhamento genérico com dados cobertos;  
• profissional apontando o caminho “PSF/UBS → encaminhamento → Espaço Cuidar”.
Headline/Legenda: **Quando a UBS encaminha você, o Espaço Cuidar ajuda a continuar o cuidado sem você ficar perdido no caminho.**

Story 5 — [Rede de apoio / Orientação sem tabu — Rede de Apoio / Humanização; ancorado em `EMULTI.md` + `CAPS.md`]
Cenas sugeridas (mín. 3):
• mão segurando card amarelo “perguntar também é se cuidar”;  
• profissional em fala curta, com ambiente neutro e acolhedor;  
• tela final com CTA “leve sua dúvida à equipe de saúde”.
Headline/Legenda: **Você não precisa guardar dúvida por vergonha: leve sua pergunta, a rede existe para orientar com respeito.**

### Reel — [Orientação sem tabu — Rede de Apoio / Humanização]
Gancho 0–3s: **Dúvida sobre saúde não é vergonha. É motivo para buscar orientação.**  
Cenas sugeridas (mín. 3):
• EMULTI preparando material de orientação domiciliar;  
• roda/sala do CAPS com cartaz “escuta e respeito”;  
• bolsa do Melhor em Casa sendo preparada;  
• guia genérica do Espaço Cuidar com dados cobertos;  
• tela final: “informação, acolhimento e cuidado”.
Legenda: **No Julho Amarelo, falar de hepatites virais também é acolher dúvidas. A rede orienta, escuta e ajuda você a entender caminhos de prevenção sem medo e sem tabu. Validar fluxos, testagem e disponibilidade de serviços com Jadielson antes de publicar.**

### Post de feed — [Humanização / Julho Amarelo]
Headline: **Cuidado também é orientar sem medo, sem tabu e sem julgamento.**
Legenda: **A prevenção às hepatites virais precisa chegar de forma clara e humana. Na atenção domiciliar, no CAPS, nos grupos ou nos encaminhamentos, a orientação faz diferença quando respeita a realidade de cada pessoa. Em caso de dúvida, procure a rede de saúde. Validar fluxos locais antes da publicação.**

---

## 03/07 — Sexta-feira
**Pilar fixo:** Flexível / Dia Extra  
**Hierarquia do tema:** Julho Amarelo como campanha; sexta organizada como bastidores, fluxo e aviso.  
**Setores/serviços do dia:** PNI/Rede de Frio, SAMU, Unidade Mista, Referência Hospitalar/Regulação, Secretaria/campanha.  
**Post de feed:** sim.  
**Reel:** sim.

### Stories — 5 unidades

Story 1 — [Secretaria / Bastidores da campanha — Flexível; ancorado no MOC + cronograma Julho]
Cenas sugeridas (mín. 3):
• mesa com calendário de julho, marca-texto amarelo e roteiro da campanha;  
• folders/cartazes sendo separados para unidades;  
• checklist com “unidades, vacinação, orientação, prevenção” marcado à caneta.
Headline/Legenda: **Antes da informação chegar até você, a rede se organiza para falar claro e orientar melhor.**

Story 2 — [PNI / Rede de Frio — Flexível; ancorado em `PNI.md`]
Cenas sugeridas (mín. 3):
• caixa térmica, geladeira ou sala de vacina em enquadramento seguro;  
• profissional conferindo material sem mostrar lote, tela ou dados;  
• caderneta sem identificação ao lado de folder amarelo.
Headline/Legenda: **Por trás da vacina que protege você, existe conservação, conferência e cuidado todos os dias.**

Story 3 — [Referência Hospitalar / Regulação — Flexível; ancorado em `Referência Hospitalar.md`]
Cenas sugeridas (mín. 3):
• computador em tela neutra, sem sistema/dados de paciente;  
• encaminhamento genérico com informações cobertas;  
• desenho simples do fluxo São Sebastião → Arapiraca → Maceió.
Headline/Legenda: **Se seu cuidado precisa seguir para referência, a regulação ajuda a organizar o caminho certo.**

Story 4 — [SAMU / 192 — Flexível; ancorado em `SAMU.md`]
Cenas sugeridas (mín. 3):
• ambulância do SAMU parada, sem simular ocorrência;  
• detalhe do número 192 na arte ou na viatura;  
• profissional em prontidão, sem cena dramática ou paciente.
Headline/Legenda: **Se for urgência de verdade, o 192 existe para chegar até você com o cuidado certo.**

Story 5 — [Unidade Mista / Pronto Atendimento — Flexível; ancorado em `Unidade Mista.md`]
Cenas sugeridas (mín. 3):
• fachada/placa da Unidade Mista em plano aberto;  
• recepção/triagem sem mostrar rosto ou ficha de paciente;  
• sala de observação vazia ou corredor sem identificação de usuários.
Headline/Legenda: **Quando o cuidado não pode esperar, a Unidade Mista acolhe, avalia e orienta o próximo passo.**

### Reel — [Bastidores e caminho certo da rede — Flexível]
Gancho 0–3s: **A prevenção que chega até você começa antes, nos bastidores da rede.**  
Cenas sugeridas (mín. 3):
• equipe separando calendário/folders do Julho Amarelo;  
• sala de vacina/rede de frio em conferência segura;  
• mesa de regulação com documento genérico e fluxo São Sebastião → Arapiraca → Maceió;  
• ambulância SAMU parada com 192;  
• fachada da Unidade Mista e tela final “use a rede do jeito certo”.
Legenda: **A rede se organiza para fortalecer a prevenção em julho. No Julho Amarelo, a Secretaria reforça informação, orientação, vacinação quando indicada e uso correto dos serviços de saúde. Validar fluxos, disponibilidade e números com Jadielson antes de publicar.**

### Post de feed — [Bastidores / Semana 1]
Headline: **A rede se prepara para fazer o Julho Amarelo chegar com clareza até você.**
Legenda: **Prevenção não acontece só no card: começa na organização das equipes, na sala de vacina, na orientação das unidades e no caminho certo dentro da rede. A primeira semana de julho abre a campanha com informação sobre hepatites virais e reforço aos serviços que orientam a população. Saúde a gente faz com coração.**

---

# Matriz de cobertura — Semana 1

| Data | Pilar | Setores/serviços usados | Arquivo F1 ancorado | Julho Amarelo | Reel |
|---|---|---|---|---|---|
| 01/07 | Vigilância / Prevenção | Educação em Saúde, PNI, Vigilância Sanitária, Endemias | PNI.md; Vigilância Sanitária.md; Endemias.md | Abertura da campanha | Sim |
| 02/07 | Rede de Apoio / Humanização | EMULTI, CAPS, Melhor em Casa, Espaço Cuidar | EMULTI.md; CAPS.md; Melhor em Casa.md; Espaço Cuidar.md | Orientação sem tabu | Sim |
| 03/07 | Flexível / Dia Extra | Secretaria, PNI/Rede de Frio, Regulação, SAMU, Unidade Mista | MOC; PNI.md; Referência Hospitalar.md; SAMU.md; Unidade Mista.md | Bastidores e fluxo | Sim |

## Controle de equilíbrio
- PSFs urbanos/rurais/indígenas ainda não entram porque julho começa na quarta-feira; rodízio de Atenção Básica/Território começa na segunda, 06/07.
- Semana 1 cobre prevenção, acolhimento e fluxo da rede sem repetir setor de forma sequencial dentro do mesmo pilar.
- Pendente para Semana 2: iniciar PSFs urbanos/rurais, Laboratório/CEO/Oftalmologia/Odontomóvel, e reforçar PNI/Endemias com campanha.

## Guard-rails
- Validar com Jadielson antes de publicar: dados epidemiológicos, números, disponibilidade de testagem, vacinação, fluxos locais, agenda e nomes de profissionais/autoridades.
- LGPD: não mostrar cartão/caderneta com nome, prontuário, guia, ficha, tela de sistema, endereço, rosto de paciente/usuário sem autorização.
- Não prometer testagem, vacina, atendimento, mutirão, transporte ou vaga sem confirmação operacional.
