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
