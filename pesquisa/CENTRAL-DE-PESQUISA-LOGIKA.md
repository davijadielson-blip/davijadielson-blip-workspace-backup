# Central de Pesquisa LÓGIKA — mapa de bases e integrações

> Criado em 2026-06-05. Dono: Jadielson Davi. Agente responsável: Lôh. Uso: enriquecer pesquisas, estratégias, conteúdos, propostas, roteiros, diagnósticos e decisões da LÓGIKA.

## Objetivo

Criar uma central de pesquisa que combine contexto interno da LÓGIKA, bases dos clientes, referências criativas, dados públicos confiáveis e pesquisa web atualizada. A ideia é que qualquer pedido importante seja respondido com contexto específico, não só com conhecimento genérico.

## Estado atual das fontes

| Fonte | Estado | Uso principal | Observação |
|---|---|---|---|
| Memória/Workspace OpenClaw | Conectado | Decisões, histórico, agentes, planos | Base de continuidade da Lôh |
| Vault / Segundo Cérebro | Conectado localmente | Estudos, outputs F2, mapas, reflexões, projetos pessoais/profissionais | F1 deve ser leitura/sugestão; escrita autônoma preferencial em F2 |
| Notion LÓGIKA | Conectado | Projetos, produção, prompts, bases operacionais | Já auditado; algumas permissões dependem de compartilhamento com integração |
| Google Drive LÓGIKA | Conectado com `drive.readonly` amplo | Auditoria estrutural, arquivos, pastas, materiais | Sem permissão destrutiva; leitura ampla validada |
| Google Docs/Sheets/Calendar | Conectado via `gog` | Documentos, planilhas, agenda, rotinas | Escrita sob comando; Gmail sem envio automático |
| GitHub | Conectado para workspace/vault | Backup, histórico, documentação técnica | Ações críticas exigem validação explícita |
| Web aberta | Disponível via `web_search`/`web_fetch`/browser | Tendências, referências, ferramentas, dados atuais | Boa para pesquisa ampla, mas precisa cruzar com contexto interno |
| Tavily | Instalado, mas desativado | Pesquisa web enriquecida/RAG web | Precisa ativar/configurar chave se quisermos usar como buscador dedicado |
| Redes sociais LÓGIKA/clientes | Ainda não conectadas formalmente | Performance, linguagem, referências, tendências | Pode começar por links/prints/exports; APIs vêm depois |
| OneDrive | Ainda não conectado diretamente | Pastas de clientes, arquivos históricos | Pode migrar/subir para Drive, Vault ou GitHub conforme tipo de arquivo |

## Respostas diretas às dúvidas do Jadielson

### 1. Como conectar nossas redes?

Depende do nível desejado:

**Nível 1 — rápido e suficiente para começar**
- Criar uma base `Referências / Redes Sociais` no Notion ou Drive.
- Colar links de posts, perfis, reels, campanhas, concorrentes e inspirações.
- Adicionar tags: cliente, tema, formato, objetivo, status, observações.
- A Lôh/Clara/Jarvis usam links + contexto para análise.

**Nível 2 — organizado e mais rico**
- Exportar relatórios das plataformas: Instagram/Meta, TikTok, YouTube Studio.
- Subir CSV/PDF/prints em uma pasta por cliente.
- Criar uma planilha de performance com: data, formato, tema, alcance, engajamento, salvamentos, comentários, CTR, observações.

**Nível 3 — integração técnica/API**
- Meta Graph API / Meta Business Suite para Instagram e Facebook.
- YouTube Data API / YouTube Analytics API.
- TikTok for Business/API quando disponível.
- Exige credenciais, permissões e manutenção. É melhor fazer depois que a central manual estiver bem desenhada.

Recomendação: começar no nível 1 + 2. API só depois, quando já soubermos quais métricas importam.

### 2 e 3. Como conecto?

Para cada fonte, o caminho mais seguro é:

1. Definir a finalidade: pesquisa, histórico, performance, criação, atendimento ou decisão.
2. Escolher o repositório certo: Notion, Drive, Vault ou GitHub.
3. Padronizar campos/tags.
4. Subir links/arquivos/exportações.
5. Testar com um pedido real: “analise estas 10 referências e proponha pauta para cliente X”.

Conexões recomendadas por tipo:

| Tipo de conteúdo | Melhor lugar | Por quê |
|---|---|---|
| Links de referência | Notion | Fácil de classificar, comentar e filtrar |
| Arquivos de cliente, mídia, PDF, imagens | Google Drive | Melhor para volume e arquivos pesados |
| Estudos, sínteses, outputs dos agentes | Vault F2 | Bom para memória estruturada e evolução |
| Documentação técnica, prompts versionados, processos | GitHub/workspace | Histórico e versionamento |
| Métricas em CSV/planilha | Google Sheets | Fácil de analisar e atualizar |
| Dados sensíveis/clientes | Drive/Notion com cuidado | Evitar espalhar em git sem necessidade |

### 4 e 5. Posso subir pastas do OneDrive? Ou melhor conectar via GitHub?

Pode subir, mas **não recomendo GitHub para tudo**.

**Melhor caminho:**
- Arquivos pesados, mídia, imagens, PDFs, documentos de cliente → **Google Drive**.
- Documentos de conhecimento, sínteses, estudos e outputs de IA → **Vault**.
- Processos, prompts, planos, documentação técnica e arquivos markdown → **GitHub/workspace**.
- Bases comerciais e organização de clientes → **Notion/Sheets**.

GitHub é ótimo para versionar texto e sistema. Não é ideal para pasta grande com mídia bruta, arquivos de cliente ou material sensível.

Sugestão prática para OneDrive:

```text
OneDrive antigo
→ triagem
  → Drive: mídias, arquivos, PDFs, documentos de cliente
  → Vault F2: estudos, sínteses, aprendizados, contexto útil
  → Notion: cadastros, projetos, CRM, links organizados
  → GitHub: processos, prompts, planos, markdowns
```

### 6. Como compor uma biblioteca de referências? Precisa baixar ou link serve?

Link já serve para começar, mas o ideal é combinar:

- **Link**: serve para acesso rápido e rastreabilidade.
- **Print ou arquivo baixado**: importante quando o conteúdo pode sumir, mudar ou ficar privado.
- **Resumo/anotação**: é o que torna a referência útil para IA.
- **Tags**: cliente, formato, objetivo, emoção, estilo, técnica, status.

Modelo mínimo de uma referência:

```text
Título:
Link:
Fonte/plataforma:
Cliente/frente:
Formato: reel | carrossel | vídeo longo | anúncio | roteiro | landing
Por que é útil:
O que copiar/adaptar:
O que evitar:
Tags:
```

Regra: se for referência estratégica/importante, salve link + print/download + anotação. Se for só inspiração leve, link + nota já basta.

### 7. Como anexar bases públicas/dados? Apenas link?

Para fontes públicas, link é suficiente para começo, mas pesquisa robusta pede três camadas:

1. **Link oficial** — fonte primária.
2. **Resumo próprio** — por que essa fonte importa.
3. **Arquivo local quando relevante** — PDF, relatório, tabela ou print se o conteúdo puder sumir.

Exemplos úteis para a LÓGIKA:
- IBGE Cidades — dados de São Sebastião/AL.
- DataSUS/Ministério da Saúde — campanhas e indicadores.
- Portais da Prefeitura/Câmara/Secretarias.
- TSE/legislação/diários oficiais quando envolver comunicação pública.
- Relatórios de plataformas: Meta, TikTok, YouTube, Google Trends.

## Estrutura recomendada da Central de Pesquisa

### No Notion

Criar uma database principal: **Central de Pesquisa — LÓGIKA**.

Campos sugeridos:
- Nome
- Tipo: referência, cliente, dado público, tendência, concorrente, prompt, roteiro, relatório, insight
- Frente: LÓGIKA, Saúde, Câmara, SINDSS, Comercial, Marketing, Produção, Conteúdo
- Cliente
- Plataforma/Fonte
- Link
- Arquivo no Drive
- Status: bruto, triado, útil, aproveitado, arquivar
- Prioridade: alta, média, baixa
- Tags
- Observação estratégica
- Próxima ação
- Data de captura

Views sugeridas:
- Inbox de pesquisa
- Por cliente
- Por frente
- Referências criativas
- Dados públicos
- Tendências e mercado
- Prompts/Comandos
- Para usar esta semana

### No Google Drive

Criar pasta: **LÓGIKA / Central de Pesquisa**.

Estrutura sugerida:

```text
Central de Pesquisa/
  00_Inbox/
  01_Clientes/
    Secretaria de Saúde/
    Câmara Municipal/
    SINDSS/
    Outros/
  02_Referencias_Criativas/
    Reels/
    Campanhas/
    Roteiros/
    Identidade Visual/
  03_Dados_Publicos/
    IBGE/
    Saude_DataSUS/
    Prefeitura/
    Camara/
  04_Relatorios_e_Metricas/
    Meta/
    TikTok/
    YouTube/
    Google/
  05_Biblioteca_de_Prompts/
  99_Arquivo/
```

### No Vault

Usar F2 para sínteses e outputs de IA:

```text
[F2] memory/context/logika/pesquisa/
[F2] memory/outputs/logika/pesquisa/
[F2] memory/agents/logika/clara/
```

Nada de jogar mídia pesada no Vault se não for necessário. Vault deve guardar inteligência, síntese e contexto, não virar depósito bruto.

### No GitHub/workspace

Guardar:
- Este mapa.
- Planos.
- Prompts versionados.
- Templates markdown.
- Processos operacionais.
- Índices e metadados, sem dados sensíveis brutos.

## Tavily

Checagem feita em 2026-06-05:

- Plugin `@openclaw/tavily-search` aparece instalado.
- Estado atual: **disabled**.
- Portanto, Tavily **não está conectado/ativo agora**.

Para ativar, precisamos:
1. Ter uma chave Tavily válida.
2. Configurar o plugin no OpenClaw.
3. Reiniciar/recarregar Gateway.
4. Fazer smoke test com uma busca real.

Enquanto isso, a Lôh já consegue usar `web_search`, `web_fetch` e navegador para pesquisa web.

## Prioridade de implantação

### Fase 1 — Organizar sem API nova

- [ ] Criar database Notion `Central de Pesquisa — LÓGIKA`.
- [ ] Criar pasta Drive `LÓGIKA / Central de Pesquisa`.
- [ ] Definir campos/tags padrão.
- [ ] Migrar 20-50 referências iniciais com links e anotações.
- [ ] Separar pastas vindas do OneDrive por tipo: Drive, Notion, Vault ou GitHub.

### Fase 2 — Bases comerciais e clientes

- [ ] Criar/organizar CRM de leads/clientes.
- [ ] Subir briefings, propostas, histórico de atendimento e materiais de cada cliente.
- [ ] Criar modelo de pesquisa por cliente.
- [ ] Criar planilha de performance das redes.

### Fase 3 — Pesquisa web enriquecida

- [ ] Ativar Tavily ou outro buscador dedicado, se desejado.
- [ ] Criar lista de fontes confiáveis fixas.
- [ ] Criar rotina de pesquisa semanal por frente/cliente.

### Fase 4 — APIs de redes sociais

- [ ] Conectar Meta Business/Instagram.
- [ ] Conectar YouTube Studio/Analytics.
- [ ] Avaliar TikTok.
- [ ] Definir dashboard mínimo de performance.

## Regra operacional para agentes

Antes de responder pedidos estratégicos da LÓGIKA, consultar na ordem:

1. Memória/workspace para decisões e contexto já definido.
2. Notion/Drive/Vault se o pedido envolver cliente, produção, arquivo, prompt, referência ou projeto.
3. Web aberta/Tavily para tendências e dados atuais.
4. Dados públicos oficiais quando envolver comunicação institucional, saúde, município, política pública ou vendas para órgão público.

Nunca depender só de uma fonte quando a decisão for importante.

## Decisão complementar — 2026-06-05

Jadielson confirmou o desenho operacional:

- Redes sociais começam por fluxo manual/semiautomático: links, prints, downloads quando necessário, anotações e relatórios/exportações. APIs ficam para uma fase posterior.
- Notion será usado como grade/agregador principal para links de referência e dados públicos.
- Arquivos que hoje estão no OneDrive devem migrar preferencialmente para Google Drive, especialmente documentos, planilhas, PDFs, mídia e materiais de cliente.
- GitHub fica reservado para arquivos leves/versionáveis: markdowns, processos, prompts, planos e documentação técnica.
- Vault segue como lugar de inteligência e síntese, não como depósito bruto de mídia.
- Referências devem ter um tópico/agente próprio para captura, estudo, classificação e encaminhamento ao setor pertinente.

## Agente/tópico recomendado — Referências & Pesquisa

Nome sugerido: **Radar**.

Função:
- Receber links, prints, downloads e anotações de referências.
- Classificar cada entrada por cliente/frente, formato, tema, objetivo e potencial de uso.
- Fazer estudo curto: por que isso importa, o que adaptar, o que evitar, para qual setor encaminhar.
- Encaminhar para Jarvis/Clara/Marketing/Comercial/Produção conforme o caso.
- Manter a grade Notion `Central de Pesquisa — LÓGIKA` organizada.

Fluxo ideal:

```text
Jadielson manda referência no tópico Radar
→ Radar classifica
→ salva/solicita cadastro na Central de Pesquisa
→ produz nota curta de estudo
→ encaminha para setor pertinente
```

Campos mínimos para cada referência:
- Título
- Link ou arquivo/print no Drive
- Fonte/plataforma
- Cliente/frente
- Tipo/formato
- Por que chamou atenção
- O que pode ser adaptado
- Risco/cuidados
- Encaminhamento recomendado
- Status: bruto, triado, estudado, encaminhado, aproveitado, arquivado

## Dados públicos

Dados públicos também entram no Notion como agregador, mas com preferência por fonte oficial.

Formato recomendado:
- Link oficial
- Órgão/fonte
- Tema
- Cliente/frente relacionada
- Resumo em linguagem simples
- Possível uso em conteúdo/campanha/venda
- Arquivo local no Drive quando for relatório/PDF importante

## Tavily — habilitação

Link para criar/acessar conta e gerar chave:

- https://app.tavily.com/home

Documentação oficial:

- https://docs.tavily.com/documentation/quickstart

Depois que Jadielson gerar a API key, deve enviar a chave para a Lôh por canal seguro/privado. A Lôh então configura o plugin `tavily`, ativa o provider e faz smoke test.

Estado atual verificado:
- Plugin `tavily` instalado/bundled no OpenClaw.
- Estado: `disabled`.
- Caminho de config esperado: `plugins.entries.tavily.config.webSearch.apiKey`.
- Provider opcional: `tools.web.search.provider = tavily`.

## Ajuste — tópico de referências já existe

Jadielson confirmou que no grupo da LÓGIKA já existe um tópico voltado a novidades/referências/inspirações. Portanto, a recomendação não é criar outro tópico do zero, mas **treinar e padronizar o tópico existente** para funcionar como agente de captura, estudo e encaminhamento de referências.

Na arquitetura atual da LÓGIKA, o tópico `474` está mapeado como **Referências/Inspirações**. Esse tópico pode assumir a função proposta para o agente `Radar`, mantendo ou ajustando o nome conforme Jadielson preferir.

Fluxo recomendado:

```text
Referência enviada no tópico Referências/Inspirações
→ agente classifica e estuda
→ registra na Central de Pesquisa/Notion quando aplicável
→ aponta destino: Marketing, Comercial, Produção, Cliente específico, Clara ou Jarvis
```

## Estrutura recomendada no Google Drive

Criar uma pasta raiz clara da empresa:

```text
LÓGIKA/
  00_Central_de_Pesquisa/
    00_Inbox/
    01_Referencias_e_Inspiracoes/
    02_Dados_Publicos/
    03_Relatorios_e_Metricas/
    04_Prompts_e_Comandos/
  01_Clientes/
    Secretaria_de_Saude/
    Camara_Municipal/
    SINDSS/
    Outros/
  02_Comercial/
    Propostas/
    Planos_de_Servico/
    Leads_e_CRM/
  03_Producao/
    Roteiros/
    Briefings/
    Materiais_Brutos/
    Entregas/
  04_Marca_Logika/
    Identidade_Visual/
    Portfolio/
    Apresentacoes/
  99_Arquivo/
```

Regra: arquivos migrados do OneDrive entram primeiro em `00_Inbox/` ou na pasta do cliente/frente correspondente. Depois Clara/Jarvis podem ajudar a reorganizar.

## Estrutura recomendada no Notion

Criar uma **database**, não apenas uma página simples, com o nome:

**Central de Pesquisa — LÓGIKA**

A página pode existir como “capa”, mas o centro operacional deve ser database para permitir filtros, tags e views.

Campos mínimos:
- Nome
- Tipo
- Frente
- Cliente
- Link
- Arquivo no Drive
- Fonte/plataforma
- Tags
- Observação estratégica
- Encaminhamento
- Status
- Data de captura

Views iniciais:
- Inbox
- Referências/Inspirações
- Dados Públicos
- Por Cliente
- Para estudar
- Encaminhadas
- Aproveitadas

## Decisão arquitetural — reduzir dependência do Notion

Jadielson propôs e a Lôh concorda: como links são essencialmente texto/contexto, eles podem ser analisados pelos próprios agentes e armazenados em **Vault e/ou GitHub/workspace**, reduzindo a dependência do Notion.

Nova diretriz:

- **Notion** fica prioritariamente para grade de produção, execução e visualização operacional.
- **Vault F2** guarda estudos, análises, sínteses, aprendizados e outputs dos agentes.
- **GitHub/workspace** guarda documentos leves, índices, processos, prompts, mapas e análises versionáveis.
- **Google Drive** vira base operacional da Secretária para arquivos de cliente, CRM, banco de clientes, documentos, planilhas, relatórios e materiais migrados do OneDrive.
- **Google Sheets/Drive** podem ser usados para CRM e banco de clientes, facilitando manuseio pela Secretária.

## Tópicos/agentes recomendados para pesquisa e bases

Além do tópico já existente de Referências/Inspirações, criar ou padronizar tópicos específicos sob Jarvis:

1. **Referências/Inspirações**
   - Links, prints, downloads, campanhas, ideias criativas.
   - Saída: análise curta + encaminhamento para Marketing/Produção/Comercial/cliente.

2. **Redes Sociais & Métricas**
   - Instagram, Meta Business, YouTube, TikTok, Google Analytics/Search Console quando conectados.
   - Saída: leitura de performance, padrões, oportunidades e recomendações.

3. **Bases Públicas & Dados Oficiais**
   - IBGE, DataSUS, portais oficiais, prefeitura, câmara, legislação, notícias públicas relevantes.
   - Saída: contexto confiável para conteúdo institucional, campanhas e propostas.

4. **CRM & Banco de Clientes**
   - Leads, clientes, contatos, histórico, status, propostas, briefings e materiais.
   - Preferência de armazenamento: Google Drive/Sheets, com organização pela Secretária.

## Estrutura simplificada do Drive

Jadielson decidiu criar apenas a pasta principal e jogar os arquivos iniciais nela. Isso é aceitável e prático, desde que Clara/Secretária assuma a organização posterior.

Pasta principal sugerida:

```text
LÓGIKA
```

Fluxo:

```text
Jadielson cria pasta LÓGIKA
→ joga arquivos migrados do OneDrive na raiz ou em uma Inbox simples
→ Clara audita e organiza
→ Jarvis valida estrutura estratégica quando necessário
```

Regra da Secretária:
- Pode organizar, renomear classificações internas, propor pastas e criar estrutura sob comando.
- Não deve excluir permanentemente arquivos.
- Movimentações amplas/irreversíveis devem ser propostas antes, ou executadas em lote controlado se Jadielson autorizar claramente.

## Formato recomendado para armazenar análises de links no Vault/GitHub

Para cada referência ou link relevante, o agente pode criar um markdown leve:

```markdown
# Referência: {título}

- Link:
- Fonte/plataforma:
- Data de captura:
- Frente/cliente:
- Tipo:
- Resumo:
- O que aproveitar:
- O que evitar:
- Encaminhamento recomendado:
- Status:
```

Destinos:

```text
Vault F2: estudos e análises vivas dos agentes
workspace/contextos: bancos de contexto e índices leves
workspace/pesquisa: mapas, listas e planos de pesquisa
Drive: arquivos anexos, prints, PDFs, relatórios e mídia
```
