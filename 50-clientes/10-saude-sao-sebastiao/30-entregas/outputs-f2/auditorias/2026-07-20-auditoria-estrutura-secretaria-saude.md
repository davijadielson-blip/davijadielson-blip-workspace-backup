---
tipo: auditoria
frente: saude-sao-sebastiao
area: estrutura-da-secretaria
solicitante: Jadielson Davi
data: 2026-07-20
status: concluida-primeira-passada
fonte_principal: "[F1] 5-Frentes/Saude-Sao-Sebastiao/01 - Estrutura Organizacional/"
---

# Auditoria — Estrutura da Secretaria de Saúde São Sebastião

## 1. Escopo auditado

Pasta canônica auditada:

`[F1] 5-Frentes/Saude-Sao-Sebastiao/01 - Estrutura Organizacional/`

Arquivos de apoio lidos/cruzados:

- `[F1] 5-Frentes/Saude-Sao-Sebastiao/00 - Saúde São Sebastião - MOC.md`
- `[F1] 5-Frentes/Saude-Sao-Sebastiao/99 - Ficha Resumo.md`
- MOCs internos de PSFs, UBSs e Setores Complementares
- Pastas operacionais/legadas da raiz da frente Saúde para identificar material ainda não incorporado ao núcleo canônico.

## 2. Inventário rápido

### Pasta canônica

| Área | Pastas | Arquivos `.md` |
|---|---:|---:|
| Estrutura Organizacional total | 42 | 74 |
| PSFs | 18 | 45 |
| UBSs | 0 | 6 |
| Setores Complementares | 21 | 22 |

### Estrutura principal

- `00 - Estrutura - MOC.md`
- `PSFs/`
- `UBSs/`
- `Setores Complementares/`

## 3. Achados principais

### 3.1. A estrutura canônica existe e é acessível

A pasta `01 - Estrutura Organizacional` funciona como núcleo organizado da base. Ela tem MOC principal, MOCs de PSFs, UBSs e Setores Complementares, além de arquivos detalhados por unidade/setor.

**Avaliação:** boa base para consulta editorial e operacional.

### 3.2. Inconsistência nos números de PSFs

Foram encontrados três números diferentes no Cofre:

- `00 - Saúde São Sebastião - MOC.md`: **Total PSF 16 equipes**.
- `00 - Estrutura - MOC.md`: **5 urbanas + 9 rurais + 2 indígenas = 16**.
- `PSFs/00 - PSFs - MOC.md`: afirma **17 equipes** e lista **5 urbanas + 10 rurais + 2 indígenas = 17**.
- Auditoria por arquivos confirmou **17 arquivos de PSF**:
  - 5 urbanos;
  - 10 rurais;
  - 2 indígenas.

**Provável ajuste necessário:** atualizar os MOCs que ainda falam em 16 / 9 rurais, ou confirmar com documento oficial se Sapé entra como equipe ativa. Hoje, pelo próprio Cofre, Sapé está listado e possui arquivo.

### 3.3. Inconsistência nos números de UBSs

Foram encontrados números diferentes:

- `00 - Saúde São Sebastião - MOC.md`: **Total UBS 28 unidades**.
- `00 - Estrutura - MOC.md`: **4 distritais + 23 zona rural = 28**.
- `UBSs/00 - UBSs - MOC.md`: declara **27 UBSs**, mas também diz “Urbanas 5” e “Rurais — por PSF 23”. No resumo final aparece “Rurais 22” e “Total 27”.
- Auditoria por arquivos encontrou:
  - 27 arquivos de UBS dentro dos PSFs: 5 urbanas + 22 rurais.
  - 4 arquivos de distritos em `UBSs/`: Distrito I, II, III e IV.

**Risco:** a base mistura duas lógicas de contagem:

1. UBS física vinculada a PSF;  
2. UBS distrital/organização sanitária.

**Ação recomendada:** definir oficialmente se o total editorial deve ser:

- **27 UBS físicas**; ou
- **28 unidades** por critério administrativo; ou
- **27 UBS + 4 distritos sanitários** como camadas diferentes.

### 3.4. Setores Complementares: MOC lista 26, mas pasta canônica detalha 20

O MOC de Setores Complementares lista 26 setores. A pasta canônica detalha 20 pastas/setores.

**Setores listados no MOC sem pasta canônica detalhada:**

1. Epidemiologia
2. Gabinete do Secretário
3. Recursos Humanos
4. Almoxarifado
5. CPD
6. Procuradoria

**Observação:** alguns desses conteúdos existem em pastas operacionais/legadas na raiz, como:

- `RECURSOS HUMANOS/` — 15 arquivos `.md`;
- `PROCURADORIA SAÚDE/` — 8 arquivos `.md`.

Mas ainda não foram incorporados ao padrão canônico `01 - Estrutura Organizacional/Setores Complementares/`.

### 3.5. Existem pastas antigas/operacionais úteis fora da estrutura canônica

A raiz da frente Saúde contém pastas operacionais com material potencialmente valioso:

- `RECEPÇÃO/` — contém `REALIZA.md`;
- `LABORATÓRIO/` — contém `DADOS.md`;
- `ESPAÇO CUIDAR - CENTRO DE ESPECIALIDADES/` — 17 arquivos, incluindo especialidades e ECG;
- `RECURSOS HUMANOS/` — 15 arquivos;
- `PROCURADORIA SAÚDE/` — 8 arquivos;
- `EMULT/` — 15 arquivos;
- `SERVIÇ0 SOCIAL/` — 1 arquivo;
- `Hospital , Pronto Atendimento/` — 2 arquivos;
- `PNI - PROGRAMA NACIONAL DE IMUNIZAÇÃO/` — 15 arquivos.

**Avaliação:** há conteúdo de granularidade maior fora do núcleo canônico. Isso explica por que algumas respostas podem ficar rasas se o agente consultar apenas `01 - Estrutura Organizacional` e não cruzar com as pastas operacionais.

### 3.6. Recepção/Regulação está subdescrita no núcleo canônico

No arquivo canônico `Secretaria.md`, a recepção aparece como:

- atendimento presencial e por telefone;
- marcação de exames da atenção básica e especializada via regulação;
- protocolo e documentos;
- arquivo;
- apoio administrativo;
- orientação de fluxo.

Mas o detalhamento fino de “quais exames”, fluxo real, documentos exigidos, horários, responsáveis e relação com SISREG não está suficientemente consolidado no arquivo canônico.

**Risco editorial:** tratar recepção como balcão administrativo simples, quando ela funciona como frente de acesso/regulação/marcação de exames.

### 3.7. Links wiki aparentemente íntegros dentro do recorte auditado

Foi feita checagem automática simples de links `[[wikilinks]]` nos arquivos principais da estrutura. Não apareceram links quebrados evidentes no recorte auditado.

**Observação:** essa checagem não valida qualidade do destino, apenas existência aproximada dos arquivos.

## 4. Riscos práticos para produção de conteúdo

1. **Número errado em card institucional**  
   PSFs e UBSs aparecem com contagens divergentes.

2. **Setores importantes invisíveis**  
   RH, Procuradoria, CPD, Almoxarifado, Gabinete e Epidemiologia estão no MOC, mas não têm pasta canônica detalhada.

3. **Subaproveitamento de conteúdo legado**  
   Pastas como Espaço Cuidar, PNI, RH, Procuradoria e EMULT têm material rico fora da estrutura canônica.

4. **Recepção/Regulação subestimada**  
   A recepção deve ser tratada como serviço de organização de acesso, especialmente para marcação de exames e regulação.

5. **Mistura entre estrutura real e estrutura editorial**  
   Alguns arquivos servem como mapa institucional; outros como banco de pauta. Hoje as camadas estão próximas, mas nem sempre separadas.

## 5. Recomendações

### Prioridade 1 — Validar números oficiais

Confirmar com a SMS:

- total correto de equipes PSF: 16 ou 17;
- se Sapé conta como equipe ativa;
- total correto de UBSs: 27 ou 28;
- como os distritos sanitários entram na contagem.

### Prioridade 2 — Criar notas canônicas faltantes

Criar, dentro de `Setores Complementares/`, arquivos para:

- Epidemiologia;
- Gabinete do Secretário;
- Recursos Humanos;
- Almoxarifado;
- CPD;
- Procuradoria.

Como `[F1]` é área de referência criativa/humana, recomenda-se só executar essa reorganização com autorização explícita de Jadielson.

### Prioridade 3 — Consolidar Recepção/Regulação

Criar ou enriquecer o arquivo canônico da Secretaria com seção específica:

- Recepção/Regulação;
- marcação de exames;
- exemplos de exames/serviços regulados;
- fluxo UBS/PSF → solicitação → regulação → agendamento;
- cuidados editoriais: não prometer vaga, data ou exame sem confirmação.

### Prioridade 4 — Incorporar material legado útil

Fazer uma segunda etapa de auditoria comparando pasta canônica vs pastas operacionais:

- `RECEPÇÃO/`
- `LABORATÓRIO/`
- `ESPAÇO CUIDAR - CENTRO DE ESPECIALIDADES/`
- `PNI - PROGRAMA NACIONAL DE IMUNIZAÇÃO/`
- `EMULT/`
- `RECURSOS HUMANOS/`
- `PROCURADORIA SAÚDE/`

Objetivo: transformar material disperso em notas de referência ou anexos operacionais consistentes.

### Prioridade 5 — Criar índice editorial por setor

Criar em `[F2] memory/outputs/saude-sao-sebastiao/` um índice de uso editorial:

- setor;
- pilar editorial principal;
- pilar secundário;
- temas possíveis;
- cuidados de LGPD/validação;
- arquivos fonte.

## 6. Classificação editorial preliminar dos setores

| Setor | Pilar principal | Pilar secundário |
|---|---|---|
| PSFs / UBSs / ACS | Atenção Básica/Território | Prestação de contas |
| PNI | Vigilância/Prevenção | Atenção Básica |
| Laboratório | Serviços Especializados | Vigilância/Prevenção |
| Espaço Cuidar | Serviços Especializados | Humanização |
| Oftalmologia | Serviços Especializados | Prestação de contas |
| CEO / Saúde Bucal / Odontomóvel | Serviços Especializados | Atenção Básica |
| Recepção/Regulação/Secretaria | Bastidores/Prestação de Contas | Serviços Especializados |
| Unidade Mista / SAMU | Urgência / Prestação de Serviço | Bastidores |
| CAPS | Rede de Apoio/Humanização | Serviços Especializados |
| EMULTI / Melhor em Casa | Rede de Apoio/Humanização | Atenção Domiciliar |
| Assistência Social | Rede de Apoio/Humanização | Bastidores de acesso |
| Endemias / Vigilância Sanitária | Vigilância/Prevenção | Prestação de contas |
| Farmácia | Atenção Básica/Programas | Bastidores/Prestação |
| Academia de Saúde | Atenção Básica/Promoção | Humanização |
| RH / Procuradoria / CPD / Almoxarifado / Gabinete | Bastidores/Prestação | Gestão/Institucional |

## 7. Próximos passos sugeridos

1. Jadielson validar se pode haver intervenção nos arquivos `[F1]` ou se a consolidação deve ficar inicialmente só em `[F2]`.
2. Fazer segunda auditoria focada nas pastas operacionais/legadas e no aproveitamento delas.
3. Corrigir o calendário editorial com a classificação de Recepção/Regulação em Serviços Especializados quando o tema for marcação de exames.
4. Criar matriz oficial `Setor → Pilar → Conteúdo → Fonte` para o agente de Saúde não depender de memória solta.

## 8. Conclusão

A estrutura é forte e consultável, mas precisa de limpeza de consistência. Os principais problemas são:

- divergência de contagem PSF/UBS;
- setores listados sem nota canônica;
- conteúdo operacional rico fora da pasta canônica;
- Recepção/Regulação subdescrita para o papel real que exerce;
- necessidade de uma matriz editorial por setor.

A recomendação é não apagar nem mover nada sem revisão humana. Primeiro consolidar diagnóstico e, se aprovado, fazer reorganização por etapas.
