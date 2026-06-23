# SAÚDE – SOCIAL MEDIA · JULHO/2026 — CALENDÁRIO EDITORIAL V2

> Status: **rascunho operacional para validação humana de Jadielson/SMS antes de publicar**. Não usar como publicação automática.

## 1) Prova de bases, poderes e limitações

**Banco/F1 usado:** leitura direta em `/data/.openclaw/workspace/`. Arquivos-base: MOC da frente, `memory/agents/saude.md`, campanhas de saúde, arquivos de setores complementares e PSFs.

**Trechos-base citados:**
- **PSF:** [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.
- **ACS:** [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.
- **Academia:** [F1] .../Academia de Saúde.md — ginástica, alongamento, caminhada orientada, grupos de hipertensos, diabéticos, idosos e gestantes.
- **CEO:** [F1] .../CEO.md — endodontia, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor e atendimento PNE.
- **Oftalmologia:** [F1] .../Oftalmologia.md — consultas oftalmológicas, refração/óculos, glaucoma, catarata, retinopatia diabética e triagem escolar.
- **Laboratório:** [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.
- **Saúde Bucal:** [F1] .../Saúde Bucal.md — odontologia nas UBSs, prevenção, ações escolares, gestantes, idosos e coordenação com CEO.
- **Odontomóvel:** [F1] .../Odontomóvel.md — atendimento itinerante, comunidades rurais/escolas, prevenção e triagem para CEO.
- **Vigilância Sanitária:** [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.
- **Endemias:** [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.
- **PNI:** [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.
- **Educação em Saúde:** [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.
- **EMULTI:** [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.
- **CAPS:** [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.
- **Assistência Social:** [F1] .../Assistência Social.md — escuta social, benefícios, CRAS/CREAS, violência, TFD, exames e apoio a famílias.
- **Maternidade:** [F1] .../Maternidade Municipal.md — trabalho de parto, parto normal/humanizado, puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.
- **Melhor em Casa:** [F1] .../Melhor em Casa.md — curativos, medicação, sondas/ostomias, fisioterapia, cuidadores, paliativos e pós-hospitalização.
- **Espaço Cuidar:** [F1] .../Espaço Cuidar.md — cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom via encaminhamento.
- **SAMU:** [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.
- **Unidade Mista:** [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.
- **Referências Regionais:** [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.
- **Campanha Pontual:** [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.
- **Bastidores/Prestação:** [F1] MOC + saude.md — prestação de contas sem números não confirmados; registros qualitativos e validação humana.

**Fatos oficiais externos:**
- Tavily direto: **NÃO CONSEGUI** — `tavily_search` retornou falta de API key.
- Busca web/fetch acessível retornou Ministério da Saúde:
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais — hepatites virais são infecções que atingem o fígado; muitas vezes silenciosas; tipos A, B e C são comuns no Brasil.
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais/hepatite-b — transmissão sexual, sangue contaminado, objetos cortantes, transmissão vertical; investigação em gestantes e vacinação conforme situação.
  - https://www.gov.br/saude/pt-br/assuntos/saude-de-a-a-z/h/hepatites-virais/hepatite-c — HCV pode ser silencioso/crônico; transmissão por sangue contaminado, materiais não esterilizados e objetos de uso pessoal.

**MCPs/Workspace visual:**
- Drive via `gog` com conta `logikacreative.mkt@gmail.com`: localizei itens/pastas como `LOGO_MARCA`, `LOGOS_ASSINATURAS`, `LOGOS`, e vários projetos `SAUDE EM MOVIMENTO_DIA 3.prproj`. **NÃO CONSEGUI** confirmar paleta oficial/Canva/Notion porque não há ferramenta MCP Notion/Canva exposta nesta sessão; precisaria token/conector MCP ou link de brand kit.

**Lôh/ecossistema:**
- Acionamento real tentado via sessão visível `telegram:@loh_analytics`. Retorno: essa rota está com `agentId=jarvis`, não Lôh; allowlist não permite acionar CCO/CMO/CIO/DataSUS como agentes. Portanto **NÃO CONSEGUI** acionar Lôh/CCO/CMO/DataSUS/CIO de verdade. Recomendações aplicadas por Jarvis: visual amarelo com branco/verde institucional quando aprovado, copy concreta, LGPD nas cenas, sem números não confirmados.

## 2) Guard-rails aplicados
- Nunca puxar serviço de outro pilar no dia.
- Cada story/reel tem 3 cenas visuais específicas.
- Sem rosto/dado sensível de paciente sem autorização. Evitar prontuário, nome em tubo, tela de sistema, placa de veículo, endereço e documento legíveis.
- Dados de testagem, estoque, agenda, nomes e números: **validar com Jadielson antes de publicar**.

## 3) Mapa Setor → Serviços
### Segunda — Atenção Básica/Território
- PSFs urbanos, rurais e indígenas
- ACS e visitas domiciliares
- Academia de Saúde: ginástica, caminhada, grupos de crônicos/idosos/gestantes
- território/UBS/porta de entrada
### Terça — Serviços Especializados
- CEO: canal, diagnóstico bucal, periodontia, cirurgia oral menor, PNE
- Oftalmologia: consulta, refração, glaucoma, catarata, retinopatia diabética, triagem escolar
- Laboratório: hemograma, bioquímica, EAS, parasitológico, testes rápidos hepatites/HIV/sífilis, pré-natal
- Saúde Bucal: UBS, prevenção, escola, gestante, idoso
- Odontomóvel: itinerante, escola/comunidade, triagem CEO
### Quarta — Vigilância/Prevenção
- Vigilância Sanitária: alimentos, serviços, medicamentos/cosméticos, denúncias/licenciamento
- Endemias: LIRAa, ACE, dengue, esquistossomose, leishmaniose, roedores/escorpiões
- PNI: rotina, campanhas, bloqueio, rede de frio, hepatite B
- Campanhas e educação em saúde: Julho Amarelo e orientações preventivas
### Quinta — Rede de Apoio/Humanização
- EMULTI: fisio, nutrição, psicologia, fono, TO, enfermagem, farmácia clínica, domicílio/matriciamento
- CAPS: psiquiatria, psicologia, oficinas, grupos, família, visitas
- Assistência Social: benefícios, TFD, violência, apoio familiar
- Maternidade: parto, puerpério, aleitamento, triagens, BCG/hep B RN
- Melhor em Casa: curativos, sondas, reabilitação, cuidadores, paliativos
- Espaço Cuidar: cardiologia, pediatria, ginecologia, cirurgia, psicologia, psiquiatria, neuro, ultrassom
### Sexta — Flexível/Dia Extra
- SAMU: 192, pré-hospitalar, quando chamar
- Unidade Mista: PA 24h, risco, estabilização, observação
- Referências regionais: Arapiraca/Maceió/7ª Regional conforme fluxo
- Campanhas pontuais/avisos
- 31/07: bastidores + prestação de contas

## 4) Calendário dia a dia

## Semana 1 — 01/07 Quarta — Vigilância/Prevenção
**Story 1 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 2 — [PNI — [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.]**
Cenas sugeridas (mín. 3):
- caderneta de vacinação aberta.
- profissional retirando vacina da caixa térmica.
- sala de vacina com descarpack e algodão.
Headline/Legenda: **Caderneta em dia é proteção para você e para quem vive com você.**

**Story 3 — [Laboratório — [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.]**
Cenas sugeridas (mín. 3):
- tubos identificados sem nome visível.
- profissional com luvas na bancada.
- caixa de testes rápidos lacrada/mesa de coleta.
Headline/Legenda: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**

**Story 4 — [Vigilância Sanitária — [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.]**
Cenas sugeridas (mín. 3):
- fiscal conferindo validade em prateleira.
- termômetro em câmara fria/geladeira.
- formulário de inspeção sem dados do estabelecimento.
Headline/Legenda: **Por trás do alimento seguro, tem vigilância trabalhando por você.**

**Story 5 — [Educação em Saúde — [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.]**
Cenas sugeridas (mín. 3):
- cartaz sendo colado no mural.
- profissional conversando em roda.
- mão marcando checklist de prevenção no card impresso.
Headline/Legenda: **Informação simples hoje evita preocupação amanhã.**

**Feed — Reels abertura Julho Amarelo [Campanha Pontual]**
- Headline: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**
- Legenda: Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels abertura Julho Amarelo**
- Gancho 0–3s: “Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.”
- Cenas mín. 3:
  - laço amarelo/card de hepatites.
  - caderneta + preservativo/material educativo.
  - profissional apontando cartaz Julho Amarelo.
- Legenda: Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 1 — 02/07 Quinta — Rede de Apoio/Humanização
**Story 1 — [EMULTI — [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.]**
Cenas sugeridas (mín. 3):
- fisioterapeuta guiando exercício domiciliar.
- nutricionista com prato educativo.
- fono/TO usando recurso simples de reabilitação.
Headline/Legenda: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**

**Story 2 — [CAPS — [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.]**
Cenas sugeridas (mín. 3):
- roda de grupo com cadeiras.
- mesa de oficina com artesanato.
- profissional conversando em corredor acolhedor sem expor usuário.
Headline/Legenda: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**

**Story 3 — [Assistência Social — [F1] .../Assistência Social.md — escuta social, benefícios, CRAS/CREAS, violência, TFD, exames e apoio a famílias.]**
Cenas sugeridas (mín. 3):
- mesa de acolhimento com documentos virados.
- assistente social apontando fluxo em papel.
- placa CRAS/CREAS ou encaminhamento coberto.
Headline/Legenda: **Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.**

**Story 4 — [Maternidade — [F1] .../Maternidade Municipal.md — trabalho de parto, parto normal/humanizado, puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.]**
Cenas sugeridas (mín. 3):
- leito/berço preparado.
- profissional orientando caderneta da gestante.
- detalhe de kit neonatal/aleitamento sem rosto.
Headline/Legenda: **Gestante bem orientada chega mais segura para viver esse momento.**

**Story 5 — [Espaço Cuidar — [F1] .../Espaço Cuidar.md — cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom via encaminhamento.]**
Cenas sugeridas (mín. 3):
- placa/recepção do espaço.
- agenda/encaminhamento sem dados pessoais.
- consultório especializado preparado com equipamento.
Headline/Legenda: **Especialidade funciona melhor quando você segue o fluxo da sua unidade.**

**Feed — Reels acolhimento sem tabu [CAPS]**
- Headline: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**
- Legenda: Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels acolhimento sem tabu**
- Gancho 0–3s: “Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.”
- Cenas mín. 3:
  - roda de grupo com cadeiras.
  - mesa de oficina com artesanato.
  - profissional conversando em corredor acolhedor sem expor usuário.
- Legenda: Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 1 — 03/07 Sexta — Flexível/Dia Extra
**Story 1 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Story 2 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Story 3 — [Referências Regionais — [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.]**
Cenas sugeridas (mín. 3):
- mapa simples São Sebastião→Arapiraca/Maceió.
- encaminhamento coberto.
- van/veículo de apoio parado sem placa visível.
Headline/Legenda: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**

**Story 4 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 5 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Feed — Reels orientação de urgência [SAMU]**
- Headline: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**
- Legenda: Na urgência de verdade, o 192 orienta e chega para salvar tempo. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels orientação de urgência**
- Gancho 0–3s: “Na urgência de verdade, o 192 orienta e chega para salvar tempo.”
- Cenas mín. 3:
  - ambulância com 192 em destaque.
  - socorrista checando mochila de emergência.
  - maca/equipamento de imobilização pronto.
- Legenda: Na urgência de verdade, o 192 orienta e chega para salvar tempo. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

### Matriz de cobertura acumulada — Semana 1
- Serviços/Setores cobertos: Campanha Pontual, PNI, Laboratório, Vigilância Sanitária, Educação em Saúde, REEL:Campanha Pontual, EMULTI, CAPS, Assistência Social, Maternidade, Espaço Cuidar, REEL:CAPS, SAMU, Unidade Mista, Referências Regionais, REEL:SAMU.
- Rodízio territorial: ainda sem segunda-feira; começa em 06/07.
- Reels planejados na semana: 3 (mínimo exigido: 3).

## Semana 2 — 06/07 Segunda — Atenção Básica/Território
**Story 1 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 2 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Story 3 — [Academia — [F1] .../Academia de Saúde.md — ginástica, alongamento, caminhada orientada, grupos de hipertensos, diabéticos, idosos e gestantes.]**
Cenas sugeridas (mín. 3):
- grupo alongando em círculo.
- educador físico demonstrando movimento.
- garrafas/colchonetes e pessoas caminhando na praça.
Headline/Legenda: **Mexer o corpo com orientação também é prevenção para sua saúde.**

**Story 4 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 5 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Feed — Reels território PSFs urbanos [PSF]**
- Headline: **Seu cuidado começa aqui pertinho, na unidade do seu território.**
- Legenda: Seu cuidado começa aqui pertinho, na unidade do seu território. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels território PSFs urbanos**
- Gancho 0–3s: “Seu cuidado começa aqui pertinho, na unidade do seu território.”
- Cenas mín. 3:
  - fachada da UBS/PSF com placa legível.
  - recepção com usuário sendo orientado sem rosto.
  - sala de atendimento com mesa, cartão SUS e material educativo.
- Legenda: Seu cuidado começa aqui pertinho, na unidade do seu território. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 2 — 07/07 Terça — Serviços Especializados
**Story 1 — [CEO — [F1] .../CEO.md — endodontia, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor e atendimento PNE.]**
Cenas sugeridas (mín. 3):
- cadeira odontológica preparada.
- profissional mostrando radiografia/modelo dental.
- instrumentais esterilizados sobre bandeja.
Headline/Legenda: **Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa.**

**Story 2 — [Laboratório — [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.]**
Cenas sugeridas (mín. 3):
- tubos identificados sem nome visível.
- profissional com luvas na bancada.
- caixa de testes rápidos lacrada/mesa de coleta.
Headline/Legenda: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**

**Story 3 — [Oftalmologia — [F1] .../Oftalmologia.md — consultas oftalmológicas, refração/óculos, glaucoma, catarata, retinopatia diabética e triagem escolar.]**
Cenas sugeridas (mín. 3):
- paciente lendo tabela de acuidade sem identificação.
- armação/caixa de lentes na mesa.
- equipamento de exame em close.
Headline/Legenda: **Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento.**

**Story 4 — [Saúde Bucal — [F1] .../Saúde Bucal.md — odontologia nas UBSs, prevenção, ações escolares, gestantes, idosos e coordenação com CEO.]**
Cenas sugeridas (mín. 3):
- escovódromo ou escova/modelo dental.
- dentista orientando gestante/criança sem rosto.
- consultório odontológico da UBS preparado.
Headline/Legenda: **Seu sorriso também faz parte da saúde da família.**

**Story 5 — [Odontomóvel — [F1] .../Odontomóvel.md — atendimento itinerante, comunidades rurais/escolas, prevenção e triagem para CEO.]**
Cenas sugeridas (mín. 3):
- veículo/estrutura itinerante estacionado.
- cadeira odontológica portátil pronta.
- kit de higiene entregue na comunidade/escola.
Headline/Legenda: **Quando o cuidado chega mais perto, a prevenção entra na rotina da comunidade.**

**Feed — Carrossel fluxo especializado [CEO]**
- Headline: **Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa.**
- Legenda: Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

## Semana 2 — 08/07 Quarta — Vigilância/Prevenção
**Story 1 — [PNI — [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.]**
Cenas sugeridas (mín. 3):
- caderneta de vacinação aberta.
- profissional retirando vacina da caixa térmica.
- sala de vacina com descarpack e algodão.
Headline/Legenda: **Caderneta em dia é proteção para você e para quem vive com você.**

**Story 2 — [Endemias — [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.]**
Cenas sugeridas (mín. 3):
- ACE batendo no portão com crachá.
- vistoria em caixa d’água/calha.
- larvitrampa/ovitrampa ou prancheta do LIRAa em close.
Headline/Legenda: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**

**Story 3 — [Vigilância Sanitária — [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.]**
Cenas sugeridas (mín. 3):
- fiscal conferindo validade em prateleira.
- termômetro em câmara fria/geladeira.
- formulário de inspeção sem dados do estabelecimento.
Headline/Legenda: **Por trás do alimento seguro, tem vigilância trabalhando por você.**

**Story 4 — [Educação em Saúde — [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.]**
Cenas sugeridas (mín. 3):
- cartaz sendo colado no mural.
- profissional conversando em roda.
- mão marcando checklist de prevenção no card impresso.
Headline/Legenda: **Informação simples hoje evita preocupação amanhã.**

**Story 5 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Feed — Reels vacina/testagem hepatites [PNI]**
- Headline: **Caderneta em dia é proteção para você e para quem vive com você.**
- Legenda: Caderneta em dia é proteção para você e para quem vive com você. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels vacina/testagem hepatites**
- Gancho 0–3s: “Caderneta em dia é proteção para você e para quem vive com você.”
- Cenas mín. 3:
  - caderneta de vacinação aberta.
  - profissional retirando vacina da caixa térmica.
  - sala de vacina com descarpack e algodão.
- Legenda: Caderneta em dia é proteção para você e para quem vive com você. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 2 — 09/07 Quinta — Rede de Apoio/Humanização
**Story 1 — [CAPS — [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.]**
Cenas sugeridas (mín. 3):
- roda de grupo com cadeiras.
- mesa de oficina com artesanato.
- profissional conversando em corredor acolhedor sem expor usuário.
Headline/Legenda: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**

**Story 2 — [EMULTI — [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.]**
Cenas sugeridas (mín. 3):
- fisioterapeuta guiando exercício domiciliar.
- nutricionista com prato educativo.
- fono/TO usando recurso simples de reabilitação.
Headline/Legenda: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**

**Story 3 — [Melhor em Casa — [F1] .../Melhor em Casa.md — curativos, medicação, sondas/ostomias, fisioterapia, cuidadores, paliativos e pós-hospitalização.]**
Cenas sugeridas (mín. 3):
- maleta de visita domiciliar.
- profissional higienizando mãos antes do cuidado.
- cuidador recebendo orientação em papel sem dados.
Headline/Legenda: **Cuidar em casa é orientar a família e proteger quem mais precisa.**

**Story 4 — [Maternidade — [F1] .../Maternidade Municipal.md — trabalho de parto, parto normal/humanizado, puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.]**
Cenas sugeridas (mín. 3):
- leito/berço preparado.
- profissional orientando caderneta da gestante.
- detalhe de kit neonatal/aleitamento sem rosto.
Headline/Legenda: **Gestante bem orientada chega mais segura para viver esse momento.**

**Story 5 — [Assistência Social — [F1] .../Assistência Social.md — escuta social, benefícios, CRAS/CREAS, violência, TFD, exames e apoio a famílias.]**
Cenas sugeridas (mín. 3):
- mesa de acolhimento com documentos virados.
- assistente social apontando fluxo em papel.
- placa CRAS/CREAS ou encaminhamento coberto.
Headline/Legenda: **Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.**

**Feed — Reels cuidado humanizado [CAPS]**
- Headline: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**
- Legenda: Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels cuidado humanizado**
- Gancho 0–3s: “Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.”
- Cenas mín. 3:
  - roda de grupo com cadeiras.
  - mesa de oficina com artesanato.
  - profissional conversando em corredor acolhedor sem expor usuário.
- Legenda: Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 2 — 10/07 Sexta — Flexível/Dia Extra
**Story 1 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Story 2 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Story 3 — [Referências Regionais — [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.]**
Cenas sugeridas (mín. 3):
- mapa simples São Sebastião→Arapiraca/Maceió.
- encaminhamento coberto.
- van/veículo de apoio parado sem placa visível.
Headline/Legenda: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**

**Story 4 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 5 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Feed — Post estático utilidade pública [Unidade Mista]**
- Headline: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**
- Legenda: Quando a situação aperta, a Unidade Mista acolhe e classifica o risco. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

### Matriz de cobertura acumulada — Semana 2
- Serviços/Setores cobertos: PSF, ACS, Academia, REEL:PSF, CEO, Laboratório, Oftalmologia, Saúde Bucal, Odontomóvel, PNI, Endemias, Vigilância Sanitária, Educação em Saúde, Campanha Pontual, REEL:PNI, CAPS, EMULTI, Melhor em Casa, Maternidade, Assistência Social, REEL:CAPS, SAMU, Unidade Mista, Referências Regionais.
- Rodízio PSFs: urbanos Centro/Cruzeiro/Peroba; ACS; Academia.
- Reels planejados na semana: 3 (mínimo exigido: 3).

## Semana 3 — 13/07 Segunda — Atenção Básica/Território
**Story 1 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 2 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Story 3 — [Academia — [F1] .../Academia de Saúde.md — ginástica, alongamento, caminhada orientada, grupos de hipertensos, diabéticos, idosos e gestantes.]**
Cenas sugeridas (mín. 3):
- grupo alongando em círculo.
- educador físico demonstrando movimento.
- garrafas/colchonetes e pessoas caminhando na praça.
Headline/Legenda: **Mexer o corpo com orientação também é prevenção para sua saúde.**

**Story 4 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 5 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Feed — Reels férias e caderneta no território [Academia]**
- Headline: **Mexer o corpo com orientação também é prevenção para sua saúde.**
- Legenda: Mexer o corpo com orientação também é prevenção para sua saúde. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels férias e caderneta no território**
- Gancho 0–3s: “Mexer o corpo com orientação também é prevenção para sua saúde.”
- Cenas mín. 3:
  - grupo alongando em círculo.
  - educador físico demonstrando movimento.
  - garrafas/colchonetes e pessoas caminhando na praça.
- Legenda: Mexer o corpo com orientação também é prevenção para sua saúde. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 3 — 14/07 Terça — Serviços Especializados
**Story 1 — [Oftalmologia — [F1] .../Oftalmologia.md — consultas oftalmológicas, refração/óculos, glaucoma, catarata, retinopatia diabética e triagem escolar.]**
Cenas sugeridas (mín. 3):
- paciente lendo tabela de acuidade sem identificação.
- armação/caixa de lentes na mesa.
- equipamento de exame em close.
Headline/Legenda: **Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento.**

**Story 2 — [Laboratório — [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.]**
Cenas sugeridas (mín. 3):
- tubos identificados sem nome visível.
- profissional com luvas na bancada.
- caixa de testes rápidos lacrada/mesa de coleta.
Headline/Legenda: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**

**Story 3 — [CEO — [F1] .../CEO.md — endodontia, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor e atendimento PNE.]**
Cenas sugeridas (mín. 3):
- cadeira odontológica preparada.
- profissional mostrando radiografia/modelo dental.
- instrumentais esterilizados sobre bandeja.
Headline/Legenda: **Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa.**

**Story 4 — [Saúde Bucal — [F1] .../Saúde Bucal.md — odontologia nas UBSs, prevenção, ações escolares, gestantes, idosos e coordenação com CEO.]**
Cenas sugeridas (mín. 3):
- escovódromo ou escova/modelo dental.
- dentista orientando gestante/criança sem rosto.
- consultório odontológico da UBS preparado.
Headline/Legenda: **Seu sorriso também faz parte da saúde da família.**

**Story 5 — [Odontomóvel — [F1] .../Odontomóvel.md — atendimento itinerante, comunidades rurais/escolas, prevenção e triagem para CEO.]**
Cenas sugeridas (mín. 3):
- veículo/estrutura itinerante estacionado.
- cadeira odontológica portátil pronta.
- kit de higiene entregue na comunidade/escola.
Headline/Legenda: **Quando o cuidado chega mais perto, a prevenção entra na rotina da comunidade.**

**Feed — Carrossel visão e diabetes [Oftalmologia]**
- Headline: **Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento.**
- Legenda: Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

## Semana 3 — 15/07 Quarta — Vigilância/Prevenção
**Story 1 — [Endemias — [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.]**
Cenas sugeridas (mín. 3):
- ACE batendo no portão com crachá.
- vistoria em caixa d’água/calha.
- larvitrampa/ovitrampa ou prancheta do LIRAa em close.
Headline/Legenda: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**

**Story 2 — [Vigilância Sanitária — [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.]**
Cenas sugeridas (mín. 3):
- fiscal conferindo validade em prateleira.
- termômetro em câmara fria/geladeira.
- formulário de inspeção sem dados do estabelecimento.
Headline/Legenda: **Por trás do alimento seguro, tem vigilância trabalhando por você.**

**Story 3 — [PNI — [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.]**
Cenas sugeridas (mín. 3):
- caderneta de vacinação aberta.
- profissional retirando vacina da caixa térmica.
- sala de vacina com descarpack e algodão.
Headline/Legenda: **Caderneta em dia é proteção para você e para quem vive com você.**

**Story 4 — [Educação em Saúde — [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.]**
Cenas sugeridas (mín. 3):
- cartaz sendo colado no mural.
- profissional conversando em roda.
- mão marcando checklist de prevenção no card impresso.
Headline/Legenda: **Informação simples hoje evita preocupação amanhã.**

**Story 5 — [Endemias — [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.]**
Cenas sugeridas (mín. 3):
- ACE batendo no portão com crachá.
- vistoria em caixa d’água/calha.
- larvitrampa/ovitrampa ou prancheta do LIRAa em close.
Headline/Legenda: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**

**Feed — Reels ACE em campo [Endemias]**
- Headline: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**
- Legenda: Se o agente de endemias bater na sua porta, abra: ele está do seu lado. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels ACE em campo**
- Gancho 0–3s: “Se o agente de endemias bater na sua porta, abra: ele está do seu lado.”
- Cenas mín. 3:
  - ACE batendo no portão com crachá.
  - vistoria em caixa d’água/calha.
  - larvitrampa/ovitrampa ou prancheta do LIRAa em close.
- Legenda: Se o agente de endemias bater na sua porta, abra: ele está do seu lado. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 3 — 16/07 Quinta — Rede de Apoio/Humanização
**Story 1 — [EMULTI — [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.]**
Cenas sugeridas (mín. 3):
- fisioterapeuta guiando exercício domiciliar.
- nutricionista com prato educativo.
- fono/TO usando recurso simples de reabilitação.
Headline/Legenda: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**

**Story 2 — [Melhor em Casa — [F1] .../Melhor em Casa.md — curativos, medicação, sondas/ostomias, fisioterapia, cuidadores, paliativos e pós-hospitalização.]**
Cenas sugeridas (mín. 3):
- maleta de visita domiciliar.
- profissional higienizando mãos antes do cuidado.
- cuidador recebendo orientação em papel sem dados.
Headline/Legenda: **Cuidar em casa é orientar a família e proteger quem mais precisa.**

**Story 3 — [CAPS — [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.]**
Cenas sugeridas (mín. 3):
- roda de grupo com cadeiras.
- mesa de oficina com artesanato.
- profissional conversando em corredor acolhedor sem expor usuário.
Headline/Legenda: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**

**Story 4 — [Maternidade — [F1] .../Maternidade Municipal.md — trabalho de parto, parto normal/humanizado, puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.]**
Cenas sugeridas (mín. 3):
- leito/berço preparado.
- profissional orientando caderneta da gestante.
- detalhe de kit neonatal/aleitamento sem rosto.
Headline/Legenda: **Gestante bem orientada chega mais segura para viver esse momento.**

**Story 5 — [Espaço Cuidar — [F1] .../Espaço Cuidar.md — cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom via encaminhamento.]**
Cenas sugeridas (mín. 3):
- placa/recepção do espaço.
- agenda/encaminhamento sem dados pessoais.
- consultório especializado preparado com equipamento.
Headline/Legenda: **Especialidade funciona melhor quando você segue o fluxo da sua unidade.**

**Feed — Reels domicílio e vínculo [EMULTI]**
- Headline: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**
- Legenda: Quando sair de casa é difícil, o cuidado também pode encontrar você. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels domicílio e vínculo**
- Gancho 0–3s: “Quando sair de casa é difícil, o cuidado também pode encontrar você.”
- Cenas mín. 3:
  - fisioterapeuta guiando exercício domiciliar.
  - nutricionista com prato educativo.
  - fono/TO usando recurso simples de reabilitação.
- Legenda: Quando sair de casa é difícil, o cuidado também pode encontrar você. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 3 — 17/07 Sexta — Flexível/Dia Extra
**Story 1 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Story 2 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Story 3 — [Referências Regionais — [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.]**
Cenas sugeridas (mín. 3):
- mapa simples São Sebastião→Arapiraca/Maceió.
- encaminhamento coberto.
- van/veículo de apoio parado sem placa visível.
Headline/Legenda: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**

**Story 4 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 5 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Feed — Feed de fotos orientação de fluxo [Referências Regionais]**
- Headline: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**
- Legenda: Quando precisa ir além do município, a rede organiza o caminho com responsabilidade. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

### Matriz de cobertura acumulada — Semana 3
- Serviços/Setores cobertos: PSF, ACS, Academia, REEL:Academia, Oftalmologia, Laboratório, CEO, Saúde Bucal, Odontomóvel, Endemias, Vigilância Sanitária, PNI, Educação em Saúde, REEL:Endemias, EMULTI, Melhor em Casa, CAPS, Maternidade, Espaço Cuidar, REEL:EMULTI, Unidade Mista, SAMU, Referências Regionais, Campanha Pontual.
- Rodízio PSFs: urbanos/rurais iniciais; férias/caderneta; ACS; Academia.
- Reels planejados na semana: 3 (mínimo exigido: 3).

## Semana 4 — 20/07 Segunda — Atenção Básica/Território
**Story 1 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 2 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Story 3 — [Academia — [F1] .../Academia de Saúde.md — ginástica, alongamento, caminhada orientada, grupos de hipertensos, diabéticos, idosos e gestantes.]**
Cenas sugeridas (mín. 3):
- grupo alongando em círculo.
- educador físico demonstrando movimento.
- garrafas/colchonetes e pessoas caminhando na praça.
Headline/Legenda: **Mexer o corpo com orientação também é prevenção para sua saúde.**

**Story 4 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 5 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Feed — Reels PSFs rurais e indígenas [PSF]**
- Headline: **Seu cuidado começa aqui pertinho, na unidade do seu território.**
- Legenda: Seu cuidado começa aqui pertinho, na unidade do seu território. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels PSFs rurais e indígenas**
- Gancho 0–3s: “Seu cuidado começa aqui pertinho, na unidade do seu território.”
- Cenas mín. 3:
  - fachada da UBS/PSF com placa legível.
  - recepção com usuário sendo orientado sem rosto.
  - sala de atendimento com mesa, cartão SUS e material educativo.
- Legenda: Seu cuidado começa aqui pertinho, na unidade do seu território. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 4 — 21/07 Terça — Serviços Especializados
**Story 1 — [Laboratório — [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.]**
Cenas sugeridas (mín. 3):
- tubos identificados sem nome visível.
- profissional com luvas na bancada.
- caixa de testes rápidos lacrada/mesa de coleta.
Headline/Legenda: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**

**Story 2 — [CEO — [F1] .../CEO.md — endodontia, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor e atendimento PNE.]**
Cenas sugeridas (mín. 3):
- cadeira odontológica preparada.
- profissional mostrando radiografia/modelo dental.
- instrumentais esterilizados sobre bandeja.
Headline/Legenda: **Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa.**

**Story 3 — [Oftalmologia — [F1] .../Oftalmologia.md — consultas oftalmológicas, refração/óculos, glaucoma, catarata, retinopatia diabética e triagem escolar.]**
Cenas sugeridas (mín. 3):
- paciente lendo tabela de acuidade sem identificação.
- armação/caixa de lentes na mesa.
- equipamento de exame em close.
Headline/Legenda: **Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento.**

**Story 4 — [Saúde Bucal — [F1] .../Saúde Bucal.md — odontologia nas UBSs, prevenção, ações escolares, gestantes, idosos e coordenação com CEO.]**
Cenas sugeridas (mín. 3):
- escovódromo ou escova/modelo dental.
- dentista orientando gestante/criança sem rosto.
- consultório odontológico da UBS preparado.
Headline/Legenda: **Seu sorriso também faz parte da saúde da família.**

**Story 5 — [Odontomóvel — [F1] .../Odontomóvel.md — atendimento itinerante, comunidades rurais/escolas, prevenção e triagem para CEO.]**
Cenas sugeridas (mín. 3):
- veículo/estrutura itinerante estacionado.
- cadeira odontológica portátil pronta.
- kit de higiene entregue na comunidade/escola.
Headline/Legenda: **Quando o cuidado chega mais perto, a prevenção entra na rotina da comunidade.**

**Feed — Carrossel exames e hepatites [Laboratório]**
- Headline: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**
- Legenda: Um exame bem orientado ajuda você a cuidar antes que o problema avance. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

## Semana 4 — 22/07 Quarta — Vigilância/Prevenção
**Story 1 — [Vigilância Sanitária — [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.]**
Cenas sugeridas (mín. 3):
- fiscal conferindo validade em prateleira.
- termômetro em câmara fria/geladeira.
- formulário de inspeção sem dados do estabelecimento.
Headline/Legenda: **Por trás do alimento seguro, tem vigilância trabalhando por você.**

**Story 2 — [Endemias — [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.]**
Cenas sugeridas (mín. 3):
- ACE batendo no portão com crachá.
- vistoria em caixa d’água/calha.
- larvitrampa/ovitrampa ou prancheta do LIRAa em close.
Headline/Legenda: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**

**Story 3 — [PNI — [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.]**
Cenas sugeridas (mín. 3):
- caderneta de vacinação aberta.
- profissional retirando vacina da caixa térmica.
- sala de vacina com descarpack e algodão.
Headline/Legenda: **Caderneta em dia é proteção para você e para quem vive com você.**

**Story 4 — [Educação em Saúde — [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.]**
Cenas sugeridas (mín. 3):
- cartaz sendo colado no mural.
- profissional conversando em roda.
- mão marcando checklist de prevenção no card impresso.
Headline/Legenda: **Informação simples hoje evita preocupação amanhã.**

**Story 5 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Feed — Reels prevenção fora da UBS [Vigilância Sanitária]**
- Headline: **Por trás do alimento seguro, tem vigilância trabalhando por você.**
- Legenda: Por trás do alimento seguro, tem vigilância trabalhando por você. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels prevenção fora da UBS**
- Gancho 0–3s: “Por trás do alimento seguro, tem vigilância trabalhando por você.”
- Cenas mín. 3:
  - fiscal conferindo validade em prateleira.
  - termômetro em câmara fria/geladeira.
  - formulário de inspeção sem dados do estabelecimento.
- Legenda: Por trás do alimento seguro, tem vigilância trabalhando por você. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 4 — 23/07 Quinta — Rede de Apoio/Humanização
**Story 1 — [Maternidade — [F1] .../Maternidade Municipal.md — trabalho de parto, parto normal/humanizado, puerpério, aleitamento, triagens neonatais, BCG/hepatite B ao nascer.]**
Cenas sugeridas (mín. 3):
- leito/berço preparado.
- profissional orientando caderneta da gestante.
- detalhe de kit neonatal/aleitamento sem rosto.
Headline/Legenda: **Gestante bem orientada chega mais segura para viver esse momento.**

**Story 2 — [Assistência Social — [F1] .../Assistência Social.md — escuta social, benefícios, CRAS/CREAS, violência, TFD, exames e apoio a famílias.]**
Cenas sugeridas (mín. 3):
- mesa de acolhimento com documentos virados.
- assistente social apontando fluxo em papel.
- placa CRAS/CREAS ou encaminhamento coberto.
Headline/Legenda: **Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.**

**Story 3 — [CAPS — [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.]**
Cenas sugeridas (mín. 3):
- roda de grupo com cadeiras.
- mesa de oficina com artesanato.
- profissional conversando em corredor acolhedor sem expor usuário.
Headline/Legenda: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**

**Story 4 — [EMULTI — [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.]**
Cenas sugeridas (mín. 3):
- fisioterapeuta guiando exercício domiciliar.
- nutricionista com prato educativo.
- fono/TO usando recurso simples de reabilitação.
Headline/Legenda: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**

**Story 5 — [Espaço Cuidar — [F1] .../Espaço Cuidar.md — cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom via encaminhamento.]**
Cenas sugeridas (mín. 3):
- placa/recepção do espaço.
- agenda/encaminhamento sem dados pessoais.
- consultório especializado preparado com equipamento.
Headline/Legenda: **Especialidade funciona melhor quando você segue o fluxo da sua unidade.**

**Feed — Reels gestante e rede de apoio [Maternidade]**
- Headline: **Gestante bem orientada chega mais segura para viver esse momento.**
- Legenda: Gestante bem orientada chega mais segura para viver esse momento. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels gestante e rede de apoio**
- Gancho 0–3s: “Gestante bem orientada chega mais segura para viver esse momento.”
- Cenas mín. 3:
  - leito/berço preparado.
  - profissional orientando caderneta da gestante.
  - detalhe de kit neonatal/aleitamento sem rosto.
- Legenda: Gestante bem orientada chega mais segura para viver esse momento. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 4 — 24/07 Sexta — Flexível/Dia Extra
**Story 1 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Story 2 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Story 3 — [Referências Regionais — [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.]**
Cenas sugeridas (mín. 3):
- mapa simples São Sebastião→Arapiraca/Maceió.
- encaminhamento coberto.
- van/veículo de apoio parado sem placa visível.
Headline/Legenda: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**

**Story 4 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 5 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Feed — Post aviso semana final Julho Amarelo [Campanha Pontual]**
- Headline: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**
- Legenda: Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

### Matriz de cobertura acumulada — Semana 4
- Serviços/Setores cobertos: PSF, ACS, Academia, REEL:PSF, Laboratório, CEO, Oftalmologia, Saúde Bucal, Odontomóvel, Vigilância Sanitária, Endemias, PNI, Educação em Saúde, Campanha Pontual, REEL:Vigilância Sanitária, Maternidade, Assistência Social, CAPS, EMULTI, Espaço Cuidar, REEL:Maternidade, SAMU, Unidade Mista, Referências Regionais.
- Rodízio PSFs: rurais e indígenas destacados; ACS; Academia.
- Reels planejados na semana: 3 (mínimo exigido: 3).

## Semana 5 — 27/07 Segunda — Atenção Básica/Território
**Story 1 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 2 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Story 3 — [Academia — [F1] .../Academia de Saúde.md — ginástica, alongamento, caminhada orientada, grupos de hipertensos, diabéticos, idosos e gestantes.]**
Cenas sugeridas (mín. 3):
- grupo alongando em círculo.
- educador físico demonstrando movimento.
- garrafas/colchonetes e pessoas caminhando na praça.
Headline/Legenda: **Mexer o corpo com orientação também é prevenção para sua saúde.**

**Story 4 — [PSF — [F1] .../01 - Estrutura Organizacional/PSFs/*/PSF *.md — arquivos por PSF urbano, rural e indígena; território/UBS/equipe de referência.]**
Cenas sugeridas (mín. 3):
- fachada da UBS/PSF com placa legível.
- recepção com usuário sendo orientado sem rosto.
- sala de atendimento com mesa, cartão SUS e material educativo.
Headline/Legenda: **Seu cuidado começa aqui pertinho, na unidade do seu território.**

**Story 5 — [ACS — [F1] .../Atenção Básica.md — responsabilidades incluem 16 PSFs, 28 UBSs, visitas domiciliares por ACS e indicadores da APS.]**
Cenas sugeridas (mín. 3):
- ACS com crachá chegando à rua.
- mão apontando endereço no mapa da microárea.
- prancheta/tablet com checklist sem dados pessoais.
Headline/Legenda: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**

**Feed — Reels chamada territorial 28/07 [ACS]**
- Headline: **Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.**
- Legenda: Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels chamada territorial 28/07**
- Gancho 0–3s: “Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo.”
- Cenas mín. 3:
  - ACS com crachá chegando à rua.
  - mão apontando endereço no mapa da microárea.
  - prancheta/tablet com checklist sem dados pessoais.
- Legenda: Se o ACS bater na sua porta, receba: ele ajuda sua família a chegar ao cuidado certo. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 5 — 28/07 Terça — Serviços Especializados
**Story 1 — [Laboratório — [F1] .../Laboratório Municipal.md — hemograma, bioquímica, EAS/urocultura, parasitológico, testes rápidos HIV/sífilis/hepatites B e C, exames de pré-natal.]**
Cenas sugeridas (mín. 3):
- tubos identificados sem nome visível.
- profissional com luvas na bancada.
- caixa de testes rápidos lacrada/mesa de coleta.
Headline/Legenda: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**

**Story 2 — [CEO — [F1] .../CEO.md — endodontia, diagnóstico bucal/câncer de boca, periodontia, cirurgia oral menor e atendimento PNE.]**
Cenas sugeridas (mín. 3):
- cadeira odontológica preparada.
- profissional mostrando radiografia/modelo dental.
- instrumentais esterilizados sobre bandeja.
Headline/Legenda: **Dor e problema na gengiva têm caminho: a UBS encaminha para o CEO quando precisa.**

**Story 3 — [Oftalmologia — [F1] .../Oftalmologia.md — consultas oftalmológicas, refração/óculos, glaucoma, catarata, retinopatia diabética e triagem escolar.]**
Cenas sugeridas (mín. 3):
- paciente lendo tabela de acuidade sem identificação.
- armação/caixa de lentes na mesa.
- equipamento de exame em close.
Headline/Legenda: **Enxergar melhor muda a rotina — e sua unidade orienta o caminho do atendimento.**

**Story 4 — [Saúde Bucal — [F1] .../Saúde Bucal.md — odontologia nas UBSs, prevenção, ações escolares, gestantes, idosos e coordenação com CEO.]**
Cenas sugeridas (mín. 3):
- escovódromo ou escova/modelo dental.
- dentista orientando gestante/criança sem rosto.
- consultório odontológico da UBS preparado.
Headline/Legenda: **Seu sorriso também faz parte da saúde da família.**

**Story 5 — [Odontomóvel — [F1] .../Odontomóvel.md — atendimento itinerante, comunidades rurais/escolas, prevenção e triagem para CEO.]**
Cenas sugeridas (mín. 3):
- veículo/estrutura itinerante estacionado.
- cadeira odontológica portátil pronta.
- kit de higiene entregue na comunidade/escola.
Headline/Legenda: **Quando o cuidado chega mais perto, a prevenção entra na rotina da comunidade.**

**Feed — Reels principal Dia Mundial das Hepatites [Laboratório]**
- Headline: **Um exame bem orientado ajuda você a cuidar antes que o problema avance.**
- Legenda: Um exame bem orientado ajuda você a cuidar antes que o problema avance. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels principal Dia Mundial das Hepatites**
- Gancho 0–3s: “Um exame bem orientado ajuda você a cuidar antes que o problema avance.”
- Cenas mín. 3:
  - tubos identificados sem nome visível.
  - profissional com luvas na bancada.
  - caixa de testes rápidos lacrada/mesa de coleta.
- Legenda: Um exame bem orientado ajuda você a cuidar antes que o problema avance. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 5 — 29/07 Quarta — Vigilância/Prevenção
**Story 1 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Story 2 — [PNI — [F1] .../PNI.md — vacinação de rotina, campanhas nacionais, bloqueios, rede de frio e calendário vacinal.]**
Cenas sugeridas (mín. 3):
- caderneta de vacinação aberta.
- profissional retirando vacina da caixa térmica.
- sala de vacina com descarpack e algodão.
Headline/Legenda: **Caderneta em dia é proteção para você e para quem vive com você.**

**Story 3 — [Vigilância Sanitária — [F1] .../Vigilância Sanitária.md — inspeção sanitária, alimentos, serviços, medicamentos/cosméticos, denúncias e licenciamento.]**
Cenas sugeridas (mín. 3):
- fiscal conferindo validade em prateleira.
- termômetro em câmara fria/geladeira.
- formulário de inspeção sem dados do estabelecimento.
Headline/Legenda: **Por trás do alimento seguro, tem vigilância trabalhando por você.**

**Story 4 — [Endemias — [F1] .../Endemias.md — dengue, LIRAa, visitas ACE, armadilhas, pontos estratégicos, controle de vetores, educação comunitária.]**
Cenas sugeridas (mín. 3):
- ACE batendo no portão com crachá.
- vistoria em caixa d’água/calha.
- larvitrampa/ovitrampa ou prancheta do LIRAa em close.
Headline/Legenda: **Se o agente de endemias bater na sua porta, abra: ele está do seu lado.**

**Story 5 — [Educação em Saúde — [F1] .../Endemias.md + PNI.md + Vigilância Sanitária.md — mobilização, campanhas e orientação comunitária.]**
Cenas sugeridas (mín. 3):
- cartaz sendo colado no mural.
- profissional conversando em roda.
- mão marcando checklist de prevenção no card impresso.
Headline/Legenda: **Informação simples hoje evita preocupação amanhã.**

**Feed — Carrossel prevenção continua [Campanha Pontual]**
- Headline: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**
- Legenda: Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.

## Semana 5 — 30/07 Quinta — Rede de Apoio/Humanização
**Story 1 — [Assistência Social — [F1] .../Assistência Social.md — escuta social, benefícios, CRAS/CREAS, violência, TFD, exames e apoio a famílias.]**
Cenas sugeridas (mín. 3):
- mesa de acolhimento com documentos virados.
- assistente social apontando fluxo em papel.
- placa CRAS/CREAS ou encaminhamento coberto.
Headline/Legenda: **Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.**

**Story 2 — [CAPS — [F1] .../CAPS.md — psiquiatria, psicologia, enfermagem, farmácia, grupos, oficinas, visitas e orientação familiar.]**
Cenas sugeridas (mín. 3):
- roda de grupo com cadeiras.
- mesa de oficina com artesanato.
- profissional conversando em corredor acolhedor sem expor usuário.
Headline/Legenda: **Você não precisa enfrentar tudo sozinho: saúde mental também é cuidado da rede.**

**Story 3 — [Melhor em Casa — [F1] .../Melhor em Casa.md — curativos, medicação, sondas/ostomias, fisioterapia, cuidadores, paliativos e pós-hospitalização.]**
Cenas sugeridas (mín. 3):
- maleta de visita domiciliar.
- profissional higienizando mãos antes do cuidado.
- cuidador recebendo orientação em papel sem dados.
Headline/Legenda: **Cuidar em casa é orientar a família e proteger quem mais precisa.**

**Story 4 — [EMULTI — [F1] .../EMULTI.md — médico, enfermagem, fisio, nutrição, serviço social, psicologia, fono, TO, farmacêutico, matriciamento e domicílio.]**
Cenas sugeridas (mín. 3):
- fisioterapeuta guiando exercício domiciliar.
- nutricionista com prato educativo.
- fono/TO usando recurso simples de reabilitação.
Headline/Legenda: **Quando sair de casa é difícil, o cuidado também pode encontrar você.**

**Story 5 — [Espaço Cuidar — [F1] .../Espaço Cuidar.md — cardiologia, pediatria, ginecologia, cirurgia geral, psicologia, psiquiatria, neurologia e ultrassom via encaminhamento.]**
Cenas sugeridas (mín. 3):
- placa/recepção do espaço.
- agenda/encaminhamento sem dados pessoais.
- consultório especializado preparado com equipamento.
Headline/Legenda: **Especialidade funciona melhor quando você segue o fluxo da sua unidade.**

**Feed — Reels rede de apoio sem preconceito [Assistência Social]**
- Headline: **Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.**
- Legenda: Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels rede de apoio sem preconceito**
- Gancho 0–3s: “Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho.”
- Cenas mín. 3:
  - mesa de acolhimento com documentos virados.
  - assistente social apontando fluxo em papel.
  - placa CRAS/CREAS ou encaminhamento coberto.
- Legenda: Quando a dificuldade pesa, a rede ajuda você a encontrar o caminho. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

## Semana 5 — 31/07 Sexta — Última sexta — Bastidores + Prestação de Contas
**Story 1 — [Bastidores/Prestação — [F1] MOC + saude.md — prestação de contas sem números não confirmados; registros qualitativos e validação humana.]**
Cenas sugeridas (mín. 3):
- timeline de fotos do mês.
- quadro de planejamento com dados sensíveis cobertos.
- servidores em roda de alinhamento de costas/lateral.
Headline/Legenda: **O cuidado que aparece para você começa com muita gente trabalhando antes.**

**Story 2 — [SAMU — [F1] .../04 - Rede e Referências/SAMU.md + Setores Complementares/SAMU.md — 192, atendimento pré-hospitalar e integração com rede de urgência.]**
Cenas sugeridas (mín. 3):
- ambulância com 192 em destaque.
- socorrista checando mochila de emergência.
- maca/equipamento de imobilização pronto.
Headline/Legenda: **Na urgência de verdade, o 192 orienta e chega para salvar tempo.**

**Story 3 — [Unidade Mista — [F1] .../Unidade Mista.md — PA 24h, classificação de risco, observação, urgências, estabilização/transferência e equipe móvel.]**
Cenas sugeridas (mín. 3):
- porta do PA 24h.
- placa de classificação de risco.
- sala de observação/equipamento monitor sem paciente identificável.
Headline/Legenda: **Quando a situação aperta, a Unidade Mista acolhe e classifica o risco.**

**Story 4 — [Referências Regionais — [F1] .../04 - Rede e Referências/Referência Hospitalar.md — referência para procedimentos/consultas acima da capacidade municipal.]**
Cenas sugeridas (mín. 3):
- mapa simples São Sebastião→Arapiraca/Maceió.
- encaminhamento coberto.
- van/veículo de apoio parado sem placa visível.
Headline/Legenda: **Quando precisa ir além do município, a rede organiza o caminho com responsabilidade.**

**Story 5 — [Campanha Pontual — [F2] .../campanhas-saude/julho-amarelo.md + dia-hepatite.md — Julho Amarelo e 28/07 Dia Mundial das Hepatites Virais.]**
Cenas sugeridas (mín. 3):
- laço amarelo/card de hepatites.
- caderneta + preservativo/material educativo.
- profissional apontando cartaz Julho Amarelo.
Headline/Legenda: **Hepatite pode ser silenciosa; informação, vacina e teste ajudam você a se proteger.**

**Feed — Reels balanço qualitativo [Bastidores/Prestação]**
- Headline: **O cuidado que aparece para você começa com muita gente trabalhando antes.**
- Legenda: O cuidado que aparece para você começa com muita gente trabalhando antes. Procure sua unidade de referência para orientação. Dados, agenda e disponibilidade devem ser validados com Jadielson antes de publicar.
**Reel — Reels balanço qualitativo**
- Gancho 0–3s: “O cuidado que aparece para você começa com muita gente trabalhando antes.”
- Cenas mín. 3:
  - timeline de fotos do mês.
  - quadro de planejamento com dados sensíveis cobertos.
  - servidores em roda de alinhamento de costas/lateral.
- Legenda: O cuidado que aparece para você começa com muita gente trabalhando antes. Julho Amarelo reforça que informação e prevenção salvam tempo no cuidado. Validação humana antes da publicação.

### Matriz de cobertura acumulada — Semana 5
- Serviços/Setores cobertos: PSF, ACS, Academia, REEL:ACS, Laboratório, CEO, Oftalmologia, Saúde Bucal, Odontomóvel, REEL:Laboratório, Campanha Pontual, PNI, Vigilância Sanitária, Endemias, Educação em Saúde, Assistência Social, CAPS, Melhor em Casa, EMULTI, Espaço Cuidar, REEL:Assistência Social, Bastidores/Prestação, SAMU, Unidade Mista, Referências Regionais, REEL:Bastidores/Prestação.
- Rodízio PSFs: fechamento territorial; urbanos, rurais e indígenas contemplados no mês por blocos de segunda.
- Reels planejados na semana: 4 (mínimo exigido: 3).

## 5) Observação final de produção
Este calendário é draft. Onde houver dado epidemiológico, estoque, disponibilidade de teste/vacina, horário, agenda, número de atendimentos, nome de profissional/autoridade ou imagem identificável: **validar com Jadielson/SMS antes de publicar**.
