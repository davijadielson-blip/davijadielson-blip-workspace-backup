---
frente: saude-sao-sebastiao
tipo: calendario-editorial
mes: 2026-07
campanha: Julho Amarelo — Hepatites Virais
semana: 1
datas: [2026-07-01, 2026-07-02, 2026-07-03]
revisado: false
status: rascunho
criado_em: 2026-06-22
---

# SMS São Sebastião — Calendário Editorial Julho/2026 — Semana 1

> Revisão V3: headlines recalibradas com base em `12 - BANCO DE REFERENCIAS/00 - GUIA CONDENSADO.md`, `Melhores Headlines.md` e `11 - CONTEXTO EDITORIAL/headlines.md.md`: serviço concreto + benefício + tom humano, evitando frase genérica.

## Confirmação do mês/campanha e prova de ferramentas

- **Calendário:** julho/2026 começa em **quarta-feira, 01/07**, e a última sexta é **31/07**.
- **Campanha do mês:** **Julho Amarelo — prevenção, vigilância e controle das hepatites virais**.
- **Banco Natural/F1 usado:** `/data/.openclaw/workspace/[F1] 5-Frentes/Saude-Sao-Sebastiao/`.
- **Agente/F2 usado:** `/data/.openclaw/workspace/\[F2\] memory/agents/saude.md`.
- **Campanha/F2 usada:** `/data/.openclaw/workspace/\[F2\] memory/databases/datas-sazonais/campanhas-saude/julho-amarelo.md` e `dia-hepatite.md`.
- **Tavily:** `tavily_search` direto: **NÃO CONSEGUI** — API key ausente. Usei `web_search`, que retornou provider `tavily`, e `web_fetch`/gov.br quando possível.
- **Links oficiais/saúde pública consultados:**
  - https://bvsms.saude.gov.br/julho-amarelo-mes-de-luta-contra-as-hepatites-virais-3 — BVS/MS: Julho Amarelo instituído pela Lei nº 13.802/2019 para reforçar vigilância, prevenção e controle das hepatites virais; hepatites A, B e C são as mais comuns no Brasil.
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais — Ministério da Saúde: hepatites virais atingem o fígado, podem ser silenciosas e, quando sintomáticas, podem causar cansaço, febre, mal-estar, enjoo, dor abdominal, pele/olhos amarelados, urina escura e fezes claras.
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais/hepatite-b — Ministério da Saúde: hepatite B pode ser transmitida por relação sexual sem preservativo, sangue contaminado, objetos cortantes e transmissão vertical; gestantes devem ser investigadas no pré-natal.
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais/hepatite-c — Ministério da Saúde: hepatite C pode ser silenciosa/crônica e transmitida por sangue contaminado e materiais não esterilizados.
- **Drive/Workspace visual:** via `gog` encontrei pastas como `LOGO_MARCA`, `LOGOS_ASSINATURAS`, `LOGOS` e projetos `SAUDE EM MOVIMENTO_DIA 3.prproj`. **NÃO CONSEGUI** confirmar paleta oficial/brand kit no Canva/Notion porque não há MCP Canva/Notion exposto nesta sessão.
- **Lôh/ecossistema:** acionamento real tentado via `@loh_analytics`; retorno recebido: a sessão continua Jarvis, não Lôh, sem acesso real a CCO/CMO/DataSUS/CIO como agentes separados. **NÃO simulado**.

## Provas do Banco Natural usadas

- `memory/agents/saude.md`: tom “institucional, humana, útil e presente”; stories com meta mínima de 5 por dia útil; evitar burocratês e exposição sensível.
- `00 - Saúde São Sebastião - MOC.md`: São Sebastião/AL, 7ª Regional de Saúde, cobertura ESF ~92%, 28 UBS, 16 equipes PSF.
- `PNI/PNI.md`: PNI coordena vacinação de rotina, campanhas nacionais, bloqueio vacinal e controle de estoques; salas de vacinação em UBS/PSF; rede de frio; calendário inclui hepatites para crianças, adultos, gestantes e povos indígenas.
- `Vigilância Sanitária/Vigilância Sanitária.md`: base para inspeção, orientação sanitária, alimentos/serviços e proteção coletiva. *(Trecho específico não expandido nesta etapa; usar arquivo antes da versão final se a pauta ganhar roteiro detalhado.)*
- `Endemias/Endemias.md`: dengue, LIRAa, visitas dos ACE, orientação domiciliar e mobilização comunitária.
- `EMULTI/EMULTI.md`: médico, enfermagem, fisioterapia, nutrição, serviço social, psicologia, fonoaudiologia, terapia ocupacional, farmacêutico; domicílio, grupos e matriciamento.
- `CAPS/CAPS.md`: psiquiatria, psicologia, enfermagem, farmácia, terapeuta ocupacional, grupos, oficinas, visitas domiciliares e orientação familiar.
- `Assistência Social/Assistência Social.md`: acolhimento/escuta social, benefícios, CRAS/CREAS, apoio a famílias, violência doméstica identificada na rede, tratamento fora do município e exames de alto custo.
- `Maternidade Municipal/Maternidade Municipal.md`: cuidado com gestantes, parto/puerpério, aleitamento e triagens neonatais. *(Validar cenas internas antes de captação.)*
- `Espaço Cuidar/Espaço Cuidar.md`: especialidades via encaminhamento pelos PSFs/UBSs; cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom.
- `SAMU/SAMU.md`, `Unidade Mista/Unidade Mista.md`, `Referência Hospitalar.md`: base do pilar flexível/urgência/fluxos regionais.

## Mapa Setor → Serviços por pilar

### Segunda — Atenção Básica / Território
- PSFs urbanos, rurais e indígenas: porta de entrada, território, acompanhamento familiar.
- ACS: visitas domiciliares, busca ativa, orientação de fluxo, vínculo com a família.
- Academia de Saúde: atividade física orientada, caminhada, alongamento, grupos de hipertensos, diabéticos, idosos e gestantes.
- Território/UBS: recepção, acolhimento, encaminhamento e acompanhamento contínuo.

### Terça — Serviços Especializados
- CEO: endodontia/canal, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor, atendimento PNE.
- Oftalmologia: consulta, refração/óculos, glaucoma, catarata, retinopatia diabética, triagem escolar.
- Laboratório: hemograma, bioquímica, urina, parasitológico, testes rápidos, pré-natal, vigilância/Lacen.
- Saúde Bucal: prevenção, consultórios nas UBSs, escola, gestantes, idosos.
- Odontomóvel: atendimento itinerante, escolas/comunidades, prevenção e triagem para CEO.

### Quarta — Vigilância / Prevenção
- Vigilância Sanitária: inspeção, orientação sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias/licenciamento.
- Endemias: ACE, dengue/zika/chikungunya, LIRAa, criadouros, bloqueio, educação comunitária.
- PNI: vacinação de rotina, campanhas, bloqueio, rede de frio, hepatite B.
- Campanhas: Julho Amarelo, prevenção às hepatites, educação em saúde.
- Educação em Saúde: mitos e verdades, checklist, orientação simples e comunitária.

### Quinta — Rede de Apoio / Humanização
- EMULTI: fisio, nutrição, psicologia, fono, terapia ocupacional, enfermagem, farmácia clínica, domicílio, matriciamento.
- CAPS: psiquiatria, psicologia, oficinas, grupos, família, visitas, cuidado em liberdade.
- Assistência Social: escuta, benefícios, CRAS/CREAS, TFD, violência, apoio familiar.
- Gestantes/Maternidade: pré-natal articulado, parto/puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.
- Melhor em Casa: curativos, sondas/ostomias, reabilitação, cuidadores, paliativos, pós-hospitalização.
- Espaço Cuidar: especialidades via encaminhamento, acolhimento ambulatorial e continuidade do cuidado.

### Sexta — Flexível / Dia Extra
- SAMU: 192, quando chamar, atendimento pré-hospitalar, integração com urgência.
- Unidade Mista: PA 24h, classificação de risco, urgências clínicas, observação, estabilização/transferência.
- Referências regionais: 7ª Regional, Arapiraca/Maceió quando ultrapassa capacidade municipal.
- Campanhas pontuais/avisos: Julho Amarelo, comunicados de utilidade pública, alertas de fluxo.
- Última sexta: bastidores + prestação de contas.

# Semana 1 completa

## 01/07/2026 — Quarta — Vigilância / Prevenção
**Hierarquia do tema:** Campanha do mês abre o calendário: Julho Amarelo.  
**Feed do dia:** Reels abertura Julho Amarelo.  
**Reels da semana:** 1/3.

### Story 1 — [Campanha Julho Amarelo / Educação em Saúde — F2 campanhas + gov.br/BVSMS]
Cenas sugeridas:
- Cartaz ou card impresso com laço amarelo e texto “Julho Amarelo”.
- Profissional segurando caderneta/cartão de vacina ao lado do material educativo.
- Close em mãos apontando no cartaz as palavras “prevenção”, “vacinação” e “orientação”.
Headline/Legenda: **Julho Amarelo começa na unidade com orientação clara para prevenir hepatites virais.**

### Story 2 — [PNI / Vacinação — PNI.md]
Cenas sugeridas:
- Caderneta de vacinação aberta, sem dados pessoais visíveis.
- Caixa térmica da sala de vacina com a tampa aberta parcialmente, sem mostrar lote.
- Profissional de luvas organizando algodão, descarpack e material de vacinação sem close invasivo de agulha.
Headline/Legenda: **Por trás de cada vacina, existe cuidado, controle e proteção para sua família.**

### Story 3 — [Educação em Saúde / Hepatites — gov.br]
Cenas sugeridas:
- Card “hepatites podem não dar sintomas” em tela ou impresso.
- Mãos marcando um checklist: vacina, preservativo, não compartilhar alicate/lâmina.
- Profissional apontando para ilustração simples de fígado, sem imagem de doença.
Headline/Legenda: **Hepatite nem sempre aparece no corpo. Prevenção aparece nas escolhas do dia a dia.**

### Story 4 — [Vigilância Sanitária / Prevenção em serviços — arquivo F1 VISA]
Cenas sugeridas:
- Fiscal/profissional observando material de higiene/esterilização em ambiente preparado.
- Close em embalagem lacrada ou instrumento esterilizado, sem nome de estabelecimento.
- Prancheta de checklist sanitário com dados cobertos.
Headline/Legenda: **Material esterilizado e orientação sanitária também fazem parte da prevenção às hepatites.**

### Story 5 — [PNI + Campanha / CTA de prevenção — PNI.md + julho-amarelo.md]
Cenas sugeridas:
- Fachada de UBS/PSF sem fila identificável.
- Mural da unidade com material educativo amarelo.
- Profissional apontando para caderneta e fazendo gesto de orientação, sem paciente identificável.
Headline/Legenda: **Na UBS, orientação sobre hepatites começa com uma pergunta simples: “minha prevenção está em dia?”**

### Reel — Abertura Julho Amarelo
Gancho 0–3s: **“Hepatite pode ser silenciosa. Você sabe como se proteger?”**
Cenas mín. 3:
- Laço amarelo/material da campanha na unidade.
- Sala de vacina/caderneta sem dados pessoais.
- Profissional apontando checklist simples de prevenção.
Legenda: **Julho Amarelo começou. A prevenção passa por informação, vacina em dia e orientação na unidade de saúde. Antes de publicar qualquer dado de agenda ou disponibilidade, validar com Jadielson/SMS.**

### Feed — Reels abertura Julho Amarelo
Headline: **Julho Amarelo: informação, vacina e orientação para prevenir antes dos sinais aparecerem.**
Legenda: **Julho Amarelo reforça a importância da prevenção às hepatites virais. Manter a caderneta em dia, buscar orientação e tirar dúvidas na unidade de referência ajuda você e sua família a se cuidarem melhor. Saúde a gente faz com coração.**

---

## 02/07/2026 — Quinta — Rede de Apoio / Humanização
**Hierarquia do tema:** Julho Amarelo como pano de fundo; foco do dia é acolhimento e rede de apoio.  
**Feed do dia:** Reels acolhimento sem tabu.  
**Reels da semana:** 2/3.

### Story 1 — [CAPS / Escuta e saúde mental — CAPS.md]
Cenas sugeridas:
- Roda de cadeiras em sala acolhedora, sem usuários identificáveis.
- Mesa com material de oficina terapêutica: papel, lápis, artesanato.
- Profissional em corredor acolhedor, em plano aberto, sem prontuário.
Headline/Legenda: **Entre escuta, orientação e respeito, o cuidado também acolhe dúvidas sem julgamento.**

### Story 2 — [EMULTI / Apoio multiprofissional — EMULTI.md]
Cenas sugeridas:
- Fisioterapeuta demonstrando exercício simples com faixa/bola.
- Nutricionista mostrando prato educativo ou cartaz alimentar.
- Psicóloga/fono/TO com recurso de orientação na mesa, sem paciente exposto.
Headline/Legenda: **Cuidado multiprofissional é quando exercício, alimentação e escuta caminham juntos por você.**

### Story 3 — [Assistência Social / Caminho e vulnerabilidade — Assistência Social.md]
Cenas sugeridas:
- Mesa de acolhimento com documentos virados para baixo.
- Profissional apontando um fluxo de encaminhamento em papel sem dados pessoais.
- Placa/porta do serviço ou detalhe de pasta institucional sem nome de usuário.
Headline/Legenda: **Quando a família precisa de apoio, a Assistência Social ajuda a organizar o caminho do cuidado.**

### Story 4 — [Gestantes / Maternidade — Maternidade Municipal.md + PNI.md]
Cenas sugeridas:
- Caderneta da gestante fechada ou com dados cobertos.
- Berço/leito preparado, sem mãe ou bebê identificável.
- Profissional mostrando material educativo de aleitamento ou pré-natal.
Headline/Legenda: **Cada orientação no pré-natal fortalece o cuidado da gestante e protege o bebê.**

### Story 5 — [Espaço Cuidar / Continuidade do cuidado — Espaço Cuidar.md]
Cenas sugeridas:
- Fachada/recepção do Espaço Cuidar.
- Encaminhamento coberto sobre mesa, sem nome nem CNS.
- Consultório preparado com cadeira/equipamento, sem paciente.
Headline/Legenda: **Quando a UBS encaminha, o Espaço Cuidar ajuda o cuidado a seguir com mais resolutividade.**

### Reel — Acolhimento sem tabu
Gancho 0–3s: **“Tem pergunta que muita gente guarda por vergonha. Na saúde, dúvida também merece cuidado.”**
Cenas mín. 3:
- Sala acolhedora do CAPS ou roda vazia preparada.
- Profissional da EMULTI mostrando material simples de orientação.
- Mesa da Assistência Social com fluxo coberto e gesto de escuta.
Legenda: **Cuidar também é acolher, orientar e mostrar o caminho certo. No Julho Amarelo, a rede reforça: informação sem tabu ajuda você a se proteger. Validar imagens e autorizações antes de publicar.**

### Feed — Reels acolhimento sem tabu
Headline: **Dúvida acolhida vira orientação. Orientação vira cuidado para você e sua família.**
Legenda: **A rede municipal está presente para orientar com respeito, escuta e cuidado. Se você tem dúvidas sobre prevenção, vacinação, acompanhamento ou encaminhamento, procure sua unidade de referência. Saúde a gente faz com coração.**

---

## 03/07/2026 — Sexta — Flexível / Dia Extra
**Hierarquia do tema:** Dia extra/flexível com utilidade pública; Julho Amarelo como pano de fundo.  
**Feed do dia:** Reels orientação de urgência e fluxo.  
**Reels da semana:** 3/3.

### Story 1 — [SAMU / Quando chamar 192 — SAMU.md]
Cenas sugeridas:
- Ambulância com número 192 em destaque, sem placa do veículo.
- Socorrista checando mochila de emergência.
- Maca ou equipamento de imobilização preparado, sem paciente.
Headline/Legenda: **SAMU 192: atendimento pré-hospitalar para quando cada minuto realmente importa.**

### Story 2 — [Unidade Mista / Porta de urgência — Unidade Mista.md]
Cenas sugeridas:
- Fachada/entrada da Unidade Mista.
- Placa de classificação de risco em destaque.
- Sala de observação vazia ou equipamento preparado, sem paciente.
Headline/Legenda: **Na Unidade Mista, a classificação de risco ajuda cada atendimento a seguir pela necessidade certa.**

### Story 3 — [Referências Regionais / Fluxo responsável — Referência Hospitalar.md]
Cenas sugeridas:
- Mapa simples São Sebastião → Arapiraca/Maceió/7ª Regional.
- Encaminhamento coberto sobre mesa, sem dados pessoais.
- Veículo de apoio/entrada administrativa sem placa e sem pacientes.
Headline/Legenda: **Quando o cuidado precisa seguir para a referência, o encaminhamento organiza o caminho com segurança.**

### Story 4 — [Campanha Pontual / Julho Amarelo no fluxo — julho-amarelo.md]
Cenas sugeridas:
- Card amarelo com “Julho Amarelo” ao lado de material de orientação.
- Profissional segurando cartaz com cuidados: vacina, preservativo, materiais esterilizados.
- Close em frase “procure orientação na unidade” no material impresso.
Headline/Legenda: **Julho Amarelo reforça cuidados simples que protegem antes de a hepatite dar sinais.**

### Story 5 — [Aviso de utilidade pública / Fluxo correto]
Cenas sugeridas:
- Placa “Recepção” ou balcão sem usuários identificáveis.
- Profissional apontando para cartaz de orientação de serviços.
- Tela/arte simples com “UBS para orientação / Unidade Mista para urgência / SAMU 192 para emergência”.
Headline/Legenda: **Saber se é UBS, Unidade Mista ou SAMU evita perda de tempo e orienta melhor sua família.**

### Reel — Orientação de urgência e fluxo
Gancho 0–3s: **“UBS, Unidade Mista ou SAMU? Cada porta tem uma função.”**
Cenas mín. 3:
- Fachada ou placa de UBS/recepção como orientação inicial.
- Unidade Mista com placa de classificação de risco.
- Ambulância/SAMU 192 e equipamento de emergência.
Legenda: **Para orientação e prevenção, procure sua unidade de referência. Para urgências, a Unidade Mista acolhe e classifica o risco. Em emergência, acione o 192. Informação certa ajuda você a buscar o cuidado certo.**

### Feed — Reels orientação de fluxo
Headline: **UBS, Unidade Mista ou SAMU: entender o fluxo ajuda você a buscar o cuidado certo.**
Legenda: **Orientação, prevenção e acompanhamento começam na unidade de referência. Situações de urgência devem ser avaliadas pela rede de pronto atendimento, e emergências devem acionar o 192. Antes de publicar qualquer regra operacional específica, validar com Jadielson/SMS.**

---

## Matriz de cobertura — Semana 1

| Data | Pilar | Serviços cobertos | Reels |
|---|---|---|---|
| 01/07 | Vigilância/Prevenção | Julho Amarelo, Educação em Saúde, PNI, Vigilância Sanitária | 1 |
| 02/07 | Rede de Apoio/Humanização | CAPS, EMULTI, Assistência Social, Gestantes/Maternidade, Espaço Cuidar | 1 |
| 03/07 | Flexível/Dia Extra | SAMU, Unidade Mista, Referências Regionais, Campanha Pontual, Aviso de Fluxo | 1 |

### Cobertura acumulada por serviço
- **PNI:** vacinação/caderneta/rede de frio simbólica; hepatite B como prevenção.
- **Educação em Saúde:** hepatites silenciosas, checklist de prevenção, CTA para unidade.
- **Vigilância Sanitária:** segurança de materiais/serviços e prevenção sem sensacionalismo.
- **CAPS:** acolhimento sem tabu e cuidado em liberdade.
- **EMULTI:** equipe multiprofissional e orientação ampliada.
- **Assistência Social:** escuta, fluxo e apoio familiar.
- **Maternidade/Gestantes:** orientação segura e cuidado materno-infantil sem expor pacientes.
- **Espaço Cuidar:** continuidade via encaminhamento.
- **SAMU:** 192 e emergência.
- **Unidade Mista:** acolhimento, risco e pronto atendimento.
- **Referências Regionais:** fluxo responsável quando ultrapassa capacidade municipal.
- **Campanha Pontual/Avisos:** Julho Amarelo e orientação de portas de entrada.

### Rodízio PSFs
- Semana 1 não tem segunda-feira. Rodízio de PSFs urbanos/rurais/indígenas começa na Semana 2.

## Pendências antes de publicar
- Validar com Jadielson/SMS qualquer menção de disponibilidade de vacina, teste, agenda, horário, local específico ou número.
- Confirmar autorização de imagem para profissionais/pacientes; evitar pacientes identificáveis.
- Confirmar identidade visual oficial: paleta, logo e brand kit. Localizei pastas no Drive, mas não confirmei brand kit Canva/Notion.
