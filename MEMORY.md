---
tema: memória de longo prazo e decisões do ecossistema
conteudo: protocolo Cofre+Tavily, salvamento pertinente, orquestração, ativação de agentes, políticas de serviço mútuo, decisões arquiteturais, remoção do Zapier, autenticações gog
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança, operações, tecnologia
cliente: Jadielson Davi
tipo: memória/registro de decisões
prioridade: máxima
atualizado_em: 2026-08-09
usar_quando: consultar decisões passadas, protocolos vigentes, histórico de ativações e políticas
nao_usar_quando: operação diária (AGENTS.md) ou mapa do workspace (MAPA.md)
---

## 🔐 Arquitetura - Cofre / Fonte de Verdade Única

**Nome oficial:** a partir de 2026-06-25, o workspace principal passa a ser chamado de **Cofre**.

**Definição:** **Cofre** = workspace principal (`/data/.openclaw/workspace/`), onde fica o segundo cérebro operacional de Jadielson: contexto, decisões, memória, agentes, processos e materiais de trabalho.

**Regra fundamental:** o **Cofre** (`/data/.openclaw/workspace/`) é a ÚNICA fonte de verdade primária.

- **Tudo** que agentes criam, decidem, aprendem ou anotam → Cofre
- **GitHub** (`https://github.com/davijadielson-blip/segundo-cerebro-jadielson` e repositório operacional de backup) é **backup apenas** - unidirecional; pode ser usado quando necessario para recuperacao tecnica, auditoria historica, comparacao de estado e rollback seletivo, sem substituir o Cofre local como fonte primaria
- **Nunca** escrever direto no GitHub
- **Nunca** consultar o GitHub como fonte primária

## 🧭 Estrutura Oficial do Cofre — Modelo Numerado

**Atualizado em 2026-08-09 por autorização de Jadielson via handoff `80-handoffs/prompt-loh-revisao-cofre-2026-08-09.md`.**

O Cofre passou a ser orientado pela estrutura real numerada:

- `00-central/` — governança, mapas, decisões, regras, pendências e notas centrais
- `10-pessoal/` — vida pessoal, rotina, saúde, família, inbox e tarefas
- `20-profissional/` — LÓGIKA, carreira e referências profissionais
- `30-estudos/` — cursos, livros, métodos, planos e recursos de estudo
- `40-projetos/` — projetos pessoais, profissionais, autorais, produtos e ideias
- `50-clientes/` — clientes e frentes institucionais
- `60-processos/` — checklists, rotinas, relatórios, templates e processos
- `70-agentes/` — agentes, runtime, squads, escopos e protocolos
- `80-handoffs/` — passagens formais de contexto
- `90-arquivo/` — legado, backups, duplicidades, quarentena e estrutura antiga
- `memory/` — memória operacional ativa da IA
- `media/` — mídias recebidas/referenciadas
- `scripts/` — automações
- `skills/` — skills ativas

Os termos `[F0]`, `[F1]`, `[F2]` e `[F3]` ficam como **legado técnico/histórico**. Podem aparecer em registros antigos e dependências temporárias, mas não devem orientar salvamento novo nem limitar a atuação da IA autorizada.

Diretriz canônica: a IA autorizada pode ler, criar, editar, reorganizar, consolidar, mover e manter arquivos do Cofre quando estiver executando pedidos, preservando contexto, melhorando organização ou garantindo continuidade. Jadielson permanece como autoridade final sobre sentido, prioridade, publicação, envio externo, decisões sensíveis e exclusão definitiva.

## 🧭 Protocolo Infalível de Consulta - Cofre + Tavily

**Ativado por Jadielson em 2026-06-25.**

**Escopo:** este protocolo vale para todos os clientes atuais, novos clientes, futuros clientes, agentes atuais e agentes futuros do ecossistema Jadielson/Lógika.

Para qualquer pedido, antes de responder, todo agente deve seguir esta ordem:

1. **Consultar o Cofre primeiro** - buscar nos arquivos relevantes de `/data/.openclaw/workspace/` antes de formular a resposta.
2. **Usar Tavily/Pesquisador quando precisar de informação externa, atualizada ou complementar** - especialmente quando o Cofre não tiver resposta suficiente, quando houver fatos mutáveis, notícias, referências de mercado, legislação, tendências ou dados que exigem validação externa.
3. **Só buscar outras fontes depois** - navegador, web genérica, APIs, GitHub ou outras bases entram apenas se Cofre + Tavily não resolverem ou se a tarefa exigir uma fonte específica.
4. **Nunca entregar resposta genérica sem lastro** - se não consultou, não finja. Consulte primeiro ou diga claramente que não conseguiu consultar.
5. **Fallback obrigatório quando embeddings falharem** - erro de cota, rate limit ou indisponibilidade de `memory_search` NÃO autoriza pular o Cofre. O agente deve consultar por leitura direta: `_MAP.md`, `MAPA.md`, `MEMORY.md`, `memory/*.md`, `00-central/` a `90-arquivo/`, `scripts/`, `skills/`, `find`, `grep/rg` e `read`. Se não encontrar, deve listar os caminhos verificados.
6. **Rodapé obrigatório de fontes** - ao final de respostas analíticas, estratégicas, operacionais ou informacionais, incluir uma linha curta: `Fonte: Cofre (...arquivo...), Tavily (...quando usado...), ou ferramenta específica`.

**Objetivo:** tornar as respostas mais humanas, precisas, contextualizadas e profissionais - nunca amadoras ou genéricas.

---

# 📌 Protocolo de Orquestração - Registrado em 2026-06-21

**Regra fundamental:** LÔH é a ÚNICA camada de orquestração. Nenhum agente invoca ou simula outro agente.

**Regras para TODOS os agentes:**
1. 🚫 Sem simulação de agentes
2. 🚫 Sem coordenação sem Lôh
3. 📩 Pedidos de orquestração via: DM Lôh | tópico do agente
4. 📖 Workspace é fonte primária única
5. ✅ Checklist antes de responder

---

# 🆕 POLÍTICA DE HARMONIA E SERVIÇO MÚTUO ENTRE AGENTES

## Versão 1 - Registrada em 2026-06-21

**Ativada por:** Jadielson (dono)
**Natureza:** Mudança de política de orquestração

## Princípio

**LÔH CONECTA, NÃO BLOQUEIA.** Colaboração entre agentes corporativos é LIBERADA. Bloquear colaboração legítima é erro.

## Perímetro Corporativo (Colaboração Livre)

Qualquer agente corporativo PODE pedir ajuda a outro. Eu roteio:
- CCO + operacionais → arte, motion, templates, identidade visual
- CMO + operacionais → copy, performance, tendências
- Bases Públicas & Dados → dados oficiais
- Redes Sociais & Métricas → desempenho
- CIO/Compliance → LGPD, exposição
- CAIO → automação
- C-Levels entre si, operacionais entre si, especializados com todos

**Fluxo obrigatório:**
1. Agente solicita ajuda
2. LÔH roteia ao colega certo
3. Colega EXECUTA e devolve resposta REAL
4. LÔH entrega de volta

**Proibido:** simular consulta a outro agente. Se precisa do CCO, vai ao CCO de verdade.

## Perímetro Confidencial (Parede D'água - CONTINUA ISOLADO)

- CENTRAL PESSOAL (9 agentes pessoais: Alfred, Warren, Arca, etc.)

---

## 🆕 Versão 2 - SERVIÇO MÚTUO - Atualizada em 2026-07-20

**Ativada por:** Jadielson (dono)
**Natureza:** Fortalecimento da cultura de colaboração

### Princípio

**AGENTES SERVEM UNS AOS OUTROS.** O ecossistema não é uma coleção de ilhas - é um time. Cada agente existe para servir Jadielson, e servir Jadielson inclui servir os colegas de equipe quando solicitado.

### O que muda

- **Antes:** "Pode pedir ajuda, mas passa pela Lôh"
- **Agora:** "Deve servir quando solicitado. Colaboração direta é esperada, não exceção"

### Regras

1. **Todo agente DEVE atender pedidos de outros agentes** quando a solicitação estiver dentro de sua competência
2. **Prioridade:** a demanda de Jadielson sempre vem primeiro. Se estiver ocupado com Jadielson, avise e peça pra voltar depois
3. **Sem burocracia:** se um CMO pede algo ao CCO, o CCO atende - não precisa de autorização da Lôh para colaborações simples
4. **Lôh entra:** quando a colaboração envolver múltiplos agentes, decisão transversal, risco ou arquitetura
5. **Proibido:** ignorar, atrasar deliberadamente ou responder de forma genérica a pedidos de colegas
6. **Qualidade:** servir o colega com a mesma excelência que serviria Jadielson

### Exemplos práticos

- CMO pede ao CCO → CCO cria o briefing/arte solicitado
- CRO pede ao CFO → CFO calcula margem da proposta
- COO pede ao CAIO → CAIO desenha automação do processo
- CCO pede ao CMO → CMO valida se a peça está alinhada com a marca

### Vigência

Esta política entra em vigor em **20 de Julho de 2026** e vale para todos os agentes corporativos (C-Levels, operacionais, especializados). A parede d'água da Central Pessoal permanece inalterada.
- Arquivos [F1] 4-Pessoal (isolados no workspace)
- Dados financeiros/sigilosos pessoais de Jadielson
- Dados protegidos de pacientes/clientes (validação humana necessária)

**Dois sentidos:** Nada corporativo acessa o pessoal. Nada pessoal acessa o corporativo.

## Teste Real (21/06/2026) ✅

**Cenário:** SAÚDE → solicita identidade visual ao CCO para Julho Amarelo
**Resultado:** ✅ Roteamento real executado. CCO respondeu com briefing completo (briefing-identidade-visual-julho-amarelo-2026.md).
**Documento gerado:** `[F2] memory/outputs/briefing-identidade-visual-julho-amarelo-2026.md`

## O que é responsabilidade de Jadielson

- Publicação de conteúdo institucional → validação humana
- Guard-rails de cada cliente (Saúde, Câmara, SINDSS) → seguem acordados
- Workspace como fonte de verdade → backup GitHub automático

---

## 📱 Fluxo de Projetos - Grupo PROJETOS no Telegram

**Grupo:** PROJETOS
**Chat ID:** -1004292150901

**Regra:** A partir de 18/06/2026, todo projeto em andamento é discutido no grupo PROJETOS, cada um em seu tópico. A conversa direta (DM) continua para assuntos gerais, dúvidas rápidas e coordenação.

**Tópicos ativos:**
- 🎙️ Sala de Visita (topic_id: 151) - Estudo de parceria Logika × Sala de Visita
- 🎬 CapCut Reels (topic_id: 1224) — Produção de Instagram Reels via CapCut Web
- 📋 Editais Culturais (topic_id: 1495) — Análise de editais culturais e leis de incentivo

---

## Destaque de Comunicação - Headline "Arraiá da Saúde"

*   **Headline:** "No clima dos festejos juninos, a Academia da Saúde Polo também virou espaço de alegria, convivência e cuidado."
*   **Contexto:** Refere-se à adaptação da Academia da Saúde Polo para eventos juninos, destacando a transformação em um local de alegria, convivência e cuidado, sob o guarda-chuva da Secretaria de Saúde.
*   **Data de Registro:** 2026-06-17
---
# Mapeamento de Tópicos no Telegram (Grupo LÓGIKA) - Registrado em 2026-06-19

Este registro consolida os tópicos e seus respectivos C-Levels/Agentes no grupo "LÓGIKA" do Telegram, servindo como referência para orquestração e comunicação.

## C-Levels & Tópicos Principais:
⚙️ **COO (Operações & Scaling):**
 └─ 1465 (COO - PRINCIPAL)

📈 **CRO (Receita & Vendas):**
 └─ 13 (Comercial / Prospecção / Propostas - PRINCIPAL)

📣 **CMO (Marketing & Brand):**
 └─ 1463 (CMO - PRINCIPAL)

🎬 **CCO (Criação & Audiovisual):**
 └─ 1464 (CCO - PRINCIPAL)

💰 **CFO (Finanças & Caixa):**
 └─ 1466 (CFO - PRINCIPAL)

🤖 **CAIO (IA & Automação):**
 └─ 1339 (CAIO - PRINCIPAL)

👤 **CTO (Tecnologia & Software):**
 └─ 1462 (CTO - PRINCIPAL)

📋 **CIO (Governança & Compliance):**
 └─ 1467 (CIO - PRINCIPAL)

---
## Tópicos Secundários e de Referência:

**CMO (Marketing & Brand):**
 └─ 871 (Redes Sociais & Métricas)
 └─ 474 (Novidades/Referências/Inspirações)
 └─ 6 (Redes Sociais & Métricas - antigo, manter referência)

**CTO (Tecnologia & Software):**
 └─ 14 (Laboratório / Testes)

**CIO (Governança & Compliance):**
 └─ 872 (Bases Públicas & Dados Oficiais)

---
## Tópicos Adicionais (Clientes/Projetos):
 └─ 3672 (SAÚDE - SOCIAL MEDIA)
 └─ 3844 (SINDSS - SOCIAL MEDIA)

---
# Ativação de Agentes - Deploy Onda 1

## ✅ CAIO - Ativado em 2026-06-19

**Agente:** 🤖 CAIO - Chief AI Officer
**Tópico:** 1339 (CAIO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:99bc19f9-e05a-49a0-8330-add9ce0e2b5f`
**Responsável:** Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1339 (message_id: 3876)

**Funções:**
- Projetar novos agentes na roupagem-casa
- Classificar processos na escada de maturidade (L0→L3)
- Propor automações com ROI estimado
- Avaliar riscos de IA responsável
- Melhorar/calibrar agentes existentes

**Próximos passos:** Aguardando Jadielson para definir calibragens pendentes (stack de IA, roadmap de automação, limites de IA responsável)

---

# Ativação de Agentes - Deploy Onda 2

## ✅ CRO - Ativado em 2026-06-19

**Agente:** 📈 CRO - Chief Revenue Officer
**Tópico:** 13 (Comercial / Prospecção / Propostas no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:2e0f7b15-467f-48e2-b9fe-c3e3b77a22a4`
**Responsável:** Reporta a Jadielson (Closer) via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 13 (message_id: 3882)

**Funções:**
- Operar máquina de vendas (Pré→Venda→Pós)
- Qualificar leads e montar dossiês
- Estruturar propostas para o Closer
- Gerenciar cadência de follow-up
- Monitorar churn e oportunidades de upsell
- Operar atendimento inteligente via WhatsApp

---

## ✅ CTO - Ativado em 2026-06-19

**Agente:** 👤 CTO - Chief Technology Officer
**Tópico:** 1462 (CTO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:bcb080ab-974a-4e53-bb27-5460393b162a`
**Responsável:** Alex (especialista TI/software) + Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1462 (message_id: 3883)

**Funções:**
- Avaliar viabilidade técnica de demandas
- Decidir Build vs. Buy
- Desenhar arquitetura técnica de sistemas
- Definir SLA e planos de suporte
- Estruturar base técnica do WhatsApp inteligente
- Mapear e priorizar dívida técnica

---

# Ativação de Agentes - Deploy Onda 3

## ✅ CCO - Ativado em 2026-06-19

**Agente:** 🎬 CCO - Chief Creative Officer
**Tópico:** 1464 (CCO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:3215c5cb-18dd-4728-8ad5-d6d30c2a6864`
**Responsável:** Reporta a Jadielson via LÔH (direção/edição) + Ewander (design)
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1464 (message_id: 3897)

**Funções:**
- Criar roteiros e storyboards com estrutura de 3 atos
- Definir direção criativa (tom, referências, padrão visual)
- Criar templates de produção reutilizáveis
- Gerar briefings de captação (B-roll)
- Montar guias de consistência por cliente
- Definir o que escalar via IA vs. mão humana

---

## ✅ CMO - Ativado em 2026-06-19

**Agente:** 📣 CMO - Chief Marketing Officer
**Tópico:** 1463 (CMO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:6f491713-b73e-4460-b3e6-d64ab3d5462d`
**Responsável:** Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1463 (message_id: 3898)

**Funções:**
- Definir STP (Segmentação, Target, Posicionamento)
- Mapear funil de demanda
- Estruturar Go-To-Market de novos serviços
- Definir direção de marca e pilares de conteúdo
- Interpretar performance de marketing

---

# Ativação de Agentes - Deploy Onda 4

## ✅ COO - Ativado em 2026-06-19

**Agente:** ⚙️ COO - Chief Operating Officer
**Tópico:** 1465 (COO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:426cca38-2256-4b11-b60b-99589b61f417`
**Responsável:** Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1465 (message_id: 3904)

**Funções:**
- Mapear processos operacionais com donos e handoffs
- Propor OKRs trimestrais
- Diagnosticar gargalos com soluções
- Montar matriz RACI por projeto
- Entregar placar de KPIs mensais
- Avaliar prontidão para escala

---

## ✅ CFO - Ativado em 2026-06-19

**Agente:** 💰 CFO - Chief Financial Officer
**Tópico:** 1466 (CFO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:d0773022-a3b0-43ff-8b63-0a0a042c3b75`
**Responsável:** Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1466 (message_id: 3905)

**Funções:**
- Monitorar fluxo de caixa (entradas vs. saídas)
- Calcular margem por serviço e rentabilidade por cliente
- Emitir alertas financeiros proativos
- Analisar impacto financeiro de decisões
- Apoiar precificação junto ao CRO

---

# Ativação de Agentes - Deploy Onda 5

## ✅ CIO - Ativado em 2026-06-19

**Agente:** 📋 CIO - Chief Information Officer
**Tópico:** 1467 (CIO no grupo LÓGIKA)
**Sub-agent session:** `agent:main:subagent:ff6a281f-54de-4e14-9216-0c8d1baafb53`
**Responsável:** Reporta a Jadielson via LÔH
**Status:** 🟢 Ativo
**Mensagem de ativação:** Enviada ao tópico 1467 (message_id: 3926)

**Funções:**
- Avaliar conformidade LGPD de práticas e ferramentas
- Propor políticas de dados e governança
- Avaliar fornecedores/ferramentas antes de adotar
- Mapear acessos de humanos e agentes
- Emitir alertas de risco com planos de mitigação
- Realizar checklists de conformidade geral

---

# Status do Deploy

| Onda | Agentes | Status |
|---|---|---|
| 1 | CAIO | ✅ Ativo |
| 2 | CRO + CTO | ✅ Ativos |
| 3 | CCO + CMO | ✅ Ativos |
| 4 | COO + CFO | ✅ Ativos |
| 5 | CIO | ✅ Ativo |

---

# Briefing Pós-Deploy - Decisões Críticas (2026-06-19)

## 1️⃣ OKRs da Lógica
**Status:** 🔵 HOLD (Jadielson alimenta depois)
**Impacto:** COO esperando
**Próxima ação:** Jadielson define objetivos estratégicos

## 2️⃣ Segmentos + Posicionamento Brand
**Status:** 🔵 HOLD (Jadielson define depois)
**Impacto:** CMO + CCO esperando
**Próxima ação:** Jadielson define segmentos prioritários + diferencial central

## 3️⃣ CRM → Notion
**Status:** ✅ GO AGORA
**CRM:** https://www.notion.so/CRM-1a3207e6f14581e5a470df65b1366185
**LEADS:** https://www.notion.so/Leads-Clientes-1a3207e6f14581a69dcef1930727f9f3
**Responsável:** CRO 📈
**Impacto:** CRO pode operar máquina de vendas com dados em tempo real.

Ação: CRO deve garantir que dados do CRM (notion) estejam consistentes com o que é passado para a máquina de vendas.

---

# Ativação de Agentes - Deploy Onda 4 (2026-06-19)

**Grupo:** LÓGIKA (-1003645702069)
**Status:** ✅ 9/9 agentes especializados ativados em paralelo

## 📱 CÂMARA Social Media
**Tópico:** 3951 | **Sub-agent:** `agent:main:subagent:03c88a1c-8df8-43d3-bf35-498f2e6517ad`
**Prompt base:** vault `[F2] memory/agents/camara.md`

## 🏥 SAÚDE Social Media
**Tópico:** 3672 | **Sub-agent:** `agent:main:subagent:2f9da906-a423-4ff4-885e-6ecbe48a2aab`
**Prompt base:** vault `[F2] memory/agents/saude.md`

## 📢 SINDSS Social Media
**Tópico:** 3844 | **Sub-agent:** `agent:main:subagent:7b4ea35a-993a-4017-bb65-040ef269bb3b`
**Prompt base:** vault `[F2] memory/agents/sindss.md`

## 🗂️ Bases Públicas & Dados
**Tópico:** 872 | **Sub-agent:** `agent:main:subagent:46078a43-cd47-4935-9d43-44ea8b1819cc`
**Função:** Pesquisa, coleta e integração de dados de bases públicas oficiais (IBGE, Transparência, DataSUS, TSE, etc.)

## 📊 Redes Sociais & Métricas
**Tópico:** 871 | **Sub-agent:** `agent:main:subagent:33cabb06-4578-4ad1-b67a-8fe211331b95`
**Função:** Monitoramento de métricas, relatórios de performance, recomendações de otimização

## 📋 Clara (Secretária)
**Tópico:** 6 | **Sub-agent:** `agent:main:subagent:8a203b82-34a2-4b1f-977a-706895fb3e1c`
**Função:** Secretária executiva - agendas, docs, lembretes, coordenação

## 🔧 Suporte Técnico (NOVO - 2026-07-24)
**Tópico:** 8200 | **Sub-agent:** `agent:cto:subagent:78449cf4-143f-4643-a70f-b1609560223a`
**Criado por:** Jarvis, sob ordem de Jadielson Davi
**Função:** Suporte técnico hands-on — software de edição (Premiere, After Effects, CapCut, DaVinci), exportação, codecs, hardware, troubleshooting

## 🧪 Laboratório / Testes
**Tópico:** 14 | **Sub-agent:** `agent:main:subagent:e6e964f3-0350-4cb9-9257-7356f0b24cd4`
**Função:** Testes, experimentos, sandbox operacional, PoCs

## 💡 Novidades/Refs/Inspirações
**Tópico:** 474 | **Sub-agent:** `agent:main:subagent:1eb811ca-3fba-4a16-af53-34012ff13ccc`
**Função:** Curadoria de referências, tendências, cases e inspirações

## 🎯 Jarvis (Direção)
**Tópico:** 1 | **Sub-agent:** `agent:main:subagent:653df5b5-a17c-4dc1-bf99-81b5b094ff3b`
**Função:** Direção estratégica, crescimento, posicionamento, oportunidades

---
# Central Pessoal - 9 Agentes Pessoais Ativados (2026-06-19)

**Grupo:** Central Pessoal (-1003740871403)
**ISOLAMENTO TOTAL:** Parede d'água - nenhuma integração com Lógika.

| Agente | Ícone | Tópico | Status |
|---|---|---|---|
| Alfred | 🤖 | 1 | ✅ Ativo |
| My Finance (Warren) | 💰 | 12 | ✅ Ativo |
| Segundo Cérebro (Arca) | 🧠 | 13 | ✅ Ativo |
| Saúde, Corpo e Energia | 💪 | 219 | ✅ Ativo |
| Autoconhecimento | 🪞 | 222 | ✅ Ativo |
| Liberdade, Lazer, Hobbies | 🎨 | 221 | ✅ Ativo |
| Família e Relacionamentos | 👨‍👩‍👧‍👦 | 218 | ✅ Ativo |
| Identidade e Futuro | 🎯 | 224 | ✅ Ativo |
| Espiritualidade e Propósitos (Moisés) | ✨ | 11 | ✅ Ativo |

**Prompts:** `[F2] memory/agents/central-pessoal/`

---

# 📦 Starter Kit v2.5.7 - Complementos Instalados em 2026-06-22

**Origem:** `starter-kit-openclaw-v2.5.7.zip` (Pixel Educação)
**Ação:** Migração de materiais complementares sem sobrescrita.

## Estrutura adicionada

| Caminho | Conteúdo | Natureza |
|---|---|---|
| `workspace/templates/` | 10 arquivos (7 .md + 3 .html) | Moldes canônicos de arquivos raiz + HTMLs de report |
| `workspace/exemplos/` | 7 arquivos (Amora) | Exemplo preenchido de IDENTITY, USER, SOUL, AGENTS, MAPA, HEARTBEAT |
| `workspace/archive/cheatsheets-legacy-v1.0/` | 10 cheatsheets | Legado v1.0 (memória, skills, multi-agente, etc.) |
| `workspace/` raiz | 6 arquivos | README, FAQ, manifesto, CHANGELOG, MENSAGENS-TESTERS |

**Impacto operacional:** Nenhum. Material de referência/consulta apenas.
**Skills e agentes:** Não alterados.
**Nada sobrescrito:** Arquivos preexistentes preservados.


# 🟡 Frentes em Standby (Atualizado 2026-06-22)

Agentes com prompt pronto mas NÃO ativados por decisão de Jadielson:

| Agente | Frente | Motivo |
|---|---|---|
| @rogerio | Rogério Rocha (mandato vereador) | Pausa - sem atendimento no momento |
| @vereadores | Josi Curtinhos, Vando da Cana Brava, Manoel do Gongo | Pausa - sem atendimento no momento |
| @alem-da-foto | Canal documental | Pausa - sem atendimento no momento |
| @lives-louvor | Lives gospel | Pausa - sem atendimento no momento |
| @bibliotecaria | Organização do vault | Legado arquivado em 2026-08-10; não usar como agente ativo |

**Decisão registrada em:** `[F2] memory/context/decisoes/2026-06.md`

## 📱 Protocolo WhatsApp - Sugestão Primeiro

Quando uma mensagem chegar pelo WhatsApp, o fluxo é:

1. **Recebo** a mensagem (já acontece automaticamente)
2. **Analiso** o contexto: workspace, F2 memory, histórico
3. **Preparo** uma sugestão de resposta
4. **Apresento** pra Jadielson: a mensagem original + análise + resposta sugerida
5. **Aguardo aprovação** antes de responder

**Regra:** nunca responder diretamente sem apresentar a sugestão primeiro. A não ser que Jadielson peça resposta imediata.

**Exceção:** se Jadielson disser "pode responder" ou similar, aí responde direto.

## Política histórica de prioridade de modelos dos agentes - 2026-06-26

Status em 2026-07-30: **superada tecnicamente**. Manter esta seção apenas como histórico do incidente.

Sequência definida à época por Jadielson:

1. Primário: `openai-codex/gpt-5.5` (GPT-5.5 Codex)
2. Fallback: `openrouter/deepseek/deepseek-v4-flash`
3. Fallback: `openrouter/google/gemini-2.5-flash-lite`

Correção canônica posterior: o Gateway/OpenClaw deve usar `openai/gpt-5.5` como ID técnico primário. O ID antigo `openai-codex/gpt-5.5` gerou `model not found` em alguns agentes/tópicos e acionou fallback indevido para OpenRouter.

## Política canônica atual de modelos dos agentes - 2026-07-30

Verificação em 2026-07-30: `/data/.openclaw/openclaw.json`, `openclaw config validate --json`, `openclaw models status --json` e `openclaw agents list --json` estão convergentes.

Regra atual:

1. ID técnico primário em configuração: `openai/gpt-5.5`.
2. Consciência operacional: este é o GPT-5.5 oficial do ecossistema.
3. Não usar `openai-codex/gpt-5.5` como primário em `openclaw.json`.
4. Se aparecer banner `Model Fallback: openrouter/...`, tratar como incidente a investigar, pois indica saída do primário.
5. Registros antigos que citam `openai-codex/gpt-5.5` devem ser lidos como histórico, não como instrução vigente.

---

## 🌐 Protocolo Global Obrigatório - Cofre, Mapa Geral, Tavily e Registro Permanente

**Ativado por Jadielson em 2026-06-27. Vale para todos os agentes, subagentes, tópicos, grupos e frentes do ecossistema.**

1. **Seguir sempre o mapa geral do Cofre**
   - O Cofre oficial é `/data/.openclaw/workspace/`.
   - Todo agente deve consultar `AGENTS.md`, `MAPA.md`, `MEMORY.md` quando permitido, e os caminhos `00-central/`, `10-pessoal/`, `20-profissional/`, `30-estudos/`, `40-projetos/`, `50-clientes/`, `60-processos/`, `70-agentes/`, `80-handoffs/`, `90-arquivo/`, `memory/`, `scripts/` e `skills/` relevantes antes de decidir onde salvar.
   - É proibido criar workspace paralelo, pasta paralela ou "cofre próprio" fora do Cofre.

2. **Consultar o Cofre antes de responder**
   - Antes de qualquer resposta analítica, estratégica, operacional, informacional ou contextual, consultar o Cofre.
   - Se `memory_search` falhar por cota, rate limit ou indisponibilidade, usar fallback direto: `read`, `find`, `grep`, `_MAP.md`, `MAPA.md`, `MEMORY.md`, `memory/*.md`, `00-central/` a `90-arquivo/`, `scripts/` e `skills/` relevantes.

3. **Usar Tavily/Pesquisador como fonte externa principal**
   - Quando precisar de informação externa, atualizada ou complementar, usar Tavily/Pesquisador como primeira fonte externa.
   - Browser, web genérica, APIs ou outras fontes entram depois, quando Cofre + Tavily não forem suficientes ou quando a tarefa exigir uma fonte específica.

4. **Registrar fonte no rodapé**
   - Toda resposta analítica, estratégica, operacional ou informacional deve terminar com fonte curta, por exemplo:
     `Fonte: Cofre (...), Tavily (...), ferramenta específica (...).`
   - Se não encontrou no Cofre após fallback direto, dizer quais caminhos foram verificados.

5. **Registrar com governança**
   - Não confiar em chat/sessão como memória. Chat é transitório. Cofre é continuidade.
   - Decisões, aprendizados, contexto de cliente/projeto, briefing, roteiro, checklist, plano, ata, diagnóstico, configuração, correção, link importante, resumo de Drive/Trello/WhatsApp/e-mail e qualquer informação útil para continuidade devem ser propostos para registro no Cofre.
   - O registro durável acontece com autorização explícita de Jadielson, rotina canônica aprovada, necessidade operacional já prevista ou aprovação leve por reação/resposta positiva.
   - Aprovação leve: reação **👍** ou **❤️**, ou respostas como **"obrigado"**, **"obg"**, **"muito bom"**, **"vou usar"** e equivalentes. Nesses casos, salvar o que for pertinente sem pedir nova autorização.
   - Nenhuma skill deve criar `memory/*.md` automaticamente fora dos caminhos canônicos e das permissões vigentes.
   - Use o destino correto do mapa geral:
     - decisões/configuração: `00-central/decisoes.md`, `memory/context/decisoes/` ou frente equivalente;
     - outputs, roteiros, briefings, drafts: `memory/outputs/`, `50-clientes/` ou subpasta da frente;
     - projetos: `40-projetos/` para estrutura central e `memory/projects/` para acompanhamento operacional da IA;
     - sessões/logs: `memory/sessions/`;
     - agentes/prompts: `70-agentes/` e `memory/agents/`.

6. **Regra de ouro**
   - Se é importante o bastante para orientar uma próxima ação, decisão ou continuidade, então deve ser salvo no Cofre.
   - Nunca deixe conhecimento pertinente apenas no chat.

7. **Separação Cofre x Drive**
   - Somente Markdown (`.md`) deve ser salvo no Cofre.
   - Arquivos não Markdown, como imagens, vídeos, áudios, PDFs, anexos, planilhas, compactados e binários, devem ficar no Drive ou armazenamento externo aprovado.
   - Quando um arquivo externo for importante para continuidade, criar no Cofre um `.md` com resumo, link/ID, origem, status e próximos passos.


---

## Regra geral - Cofre correto por projeto/tópico (2026-06-27)

Decisão de Jadielson no grupo PROJETOS, tópico Jack Lemley: a regra aplicada ao **DOCUMENTÁRIO O FIO DA MEMÓRIA** passa a valer para **todos os tópicos/projetos atuais e novos**.

- Cada projeto/tópico deve operar dentro do **Cofre oficial correto**, preferencialmente em `/data/.openclaw/workspace/[F3] PROJETOS/...`, quando houver pasta oficial definida.
- **Drive** fica para arquivos, mídia e entregáveis.
- **Cofre** é a fonte de verdade operacional: decisões, contexto, pesquisas, inventários, auditorias, drafts e checkpoints.
- Não usar diretórios paralelos/soltos fora do Cofre oficial.
- Para projetos/tópicos novos, confirmar/assumir a estrutura canônica correta antes de produzir ou salvar materiais.
- Regra transversal/arquitetura/memória central/segurança/integrações: alinhar com Alfred/Lôh.

Caso de referência: **O FIO DA MEMÓRIA** usa `/data/.openclaw/workspace/[F3] PROJETOS/EM ANDAMENTO/DOCUMENTÁRIO O FIO DA MEMÓRIA/`; apoio operacional em `/data/.openclaw/workspace/memory/projects/projetos/o-fio-da-memoria/`; não usar `/data/.openclaw/workspace-fio-memoria-doc/`.

Registro detalhado: `memory/decisoes/2026-06-27-regra-geral-cofre-projetos-topicos.md`.

### Complemento - Debate ecossistêmico quando necessário

Quando o tema for complexo, estratégico, controverso, criativo ou exigir visão multidisciplinar, agentes e tópicos podem acionar o ecossistema para um debate mais acalorado e produtivo sobre o assunto.

Regras:

- O debate deve ser real, com especialistas/agentes adequados, e não simulação de vozes.
- A invocação deve passar pela Lôh/orquestração quando envolver mais de uma frente, decisão transversal, cliente, projeto importante, risco ou arquitetura.
- Cada agente convidado deve contribuir dentro da própria competência, com argumentos, contrapontos, riscos, oportunidades e recomendação.
- O agente solicitante deve sintetizar o debate em decisão, próximos passos e fonte.
- Tudo que for útil para continuidade deve ser salvo no Cofre, no caminho correto do mapa geral.
- O objetivo é elevar a qualidade da decisão, não gerar ruído ou disputa performática.

---

## 2026-07-09 - Validação da Arquitetura Alfred como Secretário Pessoal/Triador

**Solicitante:** Jadielson Davi
**Validado por:** Lôh (Orquestradora Tier 0)
**Status:** ✅ Arquiteto validado e documentado

Jadielson confirmou que Alfred (General da Central Pessoal) deve atuar como secretário pessoal com capacidade de triar demandas e encaminhar entre grupos.

### Decisões da validação

1. **Papel confirmado:** Alfred é General da Central Pessoal + Secretário Pessoal/Triador. Papeis compatíveis.
2. **Acesso entre grupos:** Alfred NÃO lê todos os grupos diretamente. A ponte entre grupos é feita pela Lôh. Alfred prepara a rota e sugere; Lôh executa o encaminhamento real.
3. **Matriz de Roteamento:** criada e documentada com 15 tipos de demanda, destino, nível de autonomia e gatilho de escala para Lôh.
4. **Níveis de Autonomia:** Autônomo (🟢) / Preparar Minuta (🟡) / Encaminhar interno (🟠) / Escalar Lôh (🔴).
5. **Paredes-d'água preservadas:** pessoal ↔ LÓGIKA, pessoal ↔ instituições, F1 ↔ F2.
6. **Log obrigatório:** todo encaminhamento registrado em `[F2] memory/context/central-pessoal/encaminhamentos-alfred.md`.
7. **Comando /triar:** criado para Jadielson enviar demandas de qualquer grupo para a triagem do Alfred.

### Arquivos criados/atualizados

- `[F2] memory/agents/central-pessoal/alfred-secretario-pessoal.md` - prompt completo do Alfred com matriz, autonomia, limites e referências
- `[F2] memory/context/central-pessoal/encaminhamentos-alfred.md` - log de rastreabilidade
- `[F2] memory/context/central-pessoal/comando-triar-alfred.md` - instruções do /triar
- `[F2] memory/decisions/2026-07-08-alfred-secretario-pessoal.md` - já existia, mantido
- `[F2] memory/context/central-pessoal/2026-07-09-requisitos-acesso-alfred-secretario.md` - já existia, mantido

### Próximos passos

- Alfred agora deve operar com o prompt atualizado.
- Jadielson pode testar o /triar de qualquer grupo.
- Log de encaminhamentos começa vazio - primeiro encaminhamento real será o marco zero.
- Sempre que Alfred escalar para Lôh, Lôh executa a ponte real entre grupos.


## 🚫 Zapier removido - `gog` é oficial para Google

Jadielson reforçou em 20/07/2026: **Zapier estava atrapalhando e deve ser removido de vez**. A integração Google roda bem via **`gog`** e esse é o caminho oficial.

- Zapier MCP **não deve ser usado** para Google, Notion, Miro, YouTube ou qualquer outra integração operacional.
- Ações Zapier habilitadas foram desativadas nos servidores disponíveis: Gmail, Google Calendar, Google Drive, Notion e Miro.
- Agentes **não devem habilitar, reprovisionar, descobrir ações ou sugerir Zapier** sem autorização explícita posterior de Jadielson.
- Se algum briefing/rotina citar "Zapier" como fonte, tratar como erro de procedimento e corrigir para `gog`, API direta, MCP específico ou script local.
- Alternativas:
  - Google Drive → `gog_drive`
  - Gmail → `gog_gmail`
  - Google Calendar → `gog_calendar` ou scripts diretos do Cofre
  - Google Sheets → `gog`/scripts diretos com OAuth Google
  - Notion/outros sistemas → API direta, MCP específico ou scripts locais
  - Web → `tavily_search`, `tavily_extract`, `web_search`, `browser`

## ✅ Gog - 3 contas autenticadas (2026-07-22)

| Conta | Escopos | Status |
|---|---|---|
| `davijadielson@gmail.com` | calendar, drive | ✅ desde 2026-07-15 |
| `logikacreative.mkt@gmail.com` | docs, drive, forms, sheets | ✅ desde 2026-07-15 |
| `loh.open.logika@gmail.com` | drive, calendar | ✅ autenticada em 2026-07-22 |

**Configuração durável:**
- `GOG_KEYRING_PASSWORD` persistida em `/data/.profile`
- Credenciais OAuth (client_id + client_secret) em `/data/.local/share/gogcli/`
- Refresh tokens criptografados no keyring file-based do gog
- Backup no Cofre via GitHub a cada 3h

📁 Decisões vigentes:
- `[F2] memory/decisions/2026-07-20-remocao-total-zapier-gog-oficial.md`
- `[F2] memory/decisions/2026-07-22-gog-auth-loh-concluido.md`
- `[F2] memory/decisions/2026-07-22-renovacao-tokens-gog-3-contas.md`

---

## ✅ 2026-07-22 - Renovação tokens OAuth Google Drive

**Problema:** Agentes reclamando que não conseguiam acessar o Google Drive. Diagnóstico: todos os tokens OAuth do `gog` nas 3 contas estavam expirados/revogados (`invalid_grant: Token has been expired or revoked`).

**Solução:** Jadielson e Lôh reautorizaram manualmente as 3 contas via OAuth:
1. 🔴 → ✅ **Lógika** (`logikacreative.mkt@gmail.com`) — concluído
2. 🔴 → ✅ **Pessoal** (`davijadielson@gmail.com`) — concluído
3. 🔴 → ✅ **Lôh** (`loh.open.logika@gmail.com`) — concluído

**Método:** Lôh usou a API direta do Google (`POST oauth2.googleapis.com/token`) para trocar o código de autorização por refresh token, sem depender do callback local do `gog` que estava expirando. Refresh tokens importados com `gog auth import --refresh-token-stdin --force`.

**Resultado:** ✅ Drive funcionando nas 3 contas. Agentes voltaram a ter acesso.

---

## ✅ 2026-07-17 - Decisões extraídas

Em 17/07/2026, a varredura diária encontrou uma decisão/aprovação operacional relevante na frente **SAÚDE Social Media**. A maior parte das sessões do período foi cron-driven (backups, Guard C-Level, heartbeats e rotinas), mas houve registro de regra aprovada por Jadielson para uso dos cronogramas reais dos setores na programação diária.

### Decisões e aprovações

- **SAÚDE Social Media - Matriz de cronogramas dos setores:** a partir de 2026-07-17, todo roteiro/programação diária da Saúde deve incluir, além da pauta editorial do dia, um bloco de **lembretes de captação por cronograma real dos setores**.
- **Regra fina aprovada:** fora da terça, serviço especializado só entra na publicação se reforçar o pilar do dia; se não reforçar, a orientação é captar e guardar para a próxima terça de Serviços Especializados.
- **Pauta 17/07/2026:** sexta-feira flexível, com foco em bastidores/prestação de contas/fluxo da rede; pauta principal sugerida: Unidade Mista + SAMU + Referências Regionais.

📁 Registro completo: `[F2] memory/decisions/2026-07-17-decisoes.md`

---

## ✅ 2026-07-18 - Varredura diária de decisões

Em 18/07/2026, a extração diária verificou as sessões `.jsonl` do dia anterior e **não encontrou decisões, aprovações ou debates estratégicos humanos** a registrar. O recorte continha 106 sessões `.jsonl`: 104 entradas cron e 2 heartbeats/lembretes internos, sem mensagens humanas diretas.

### Resultado

- **Debates:** nenhum debate estratégico identificado.
- **Decisões:** nenhuma decisão nova identificada.
- **Aprovações:** nenhuma aprovação humana nova identificada.
- **Ignorados:** crons rotineiros, backups, pautas automáticas, syncs operacionais, lembretes PG/PD e heartbeats.

📁 Registro completo: `[F2] memory/decisions/2026-07-18-decisoes.md`

## ✅ 2026-07-20 - Correções estruturais: subagentes, fallbacks e prompts C-Level

### Decisões e ações

- **Diagnóstico de falha de subagentes:** CMO e CCO falharam por rate limit do OpenAI Codex, compartilhado com a sessão principal. Hipótese confirmada: mesmo provider, mesma chave OAuth, 0 tokens consumidos.
- **Configuração de fallbacks de modelo:** `agents.defaults.subagents.model` configurado com cadeia de 3 níveis: Codex (primário, mais barato) → OpenRouter DeepSeek (fallback) → Google Gemini Lite (último recurso). Timeout elevado para 300s.
- **Regra de obediência nos prompts:** todos os 8 C-Levels receberam instrução de obediência a comandos diretos ("Responda APENAS em N linha(s)"), inserida antes do Protocolo Global para evitar leitura do Cofre em testes/pings.
- **Testes comprovados:** 5/8 C-Levels completaram spawn com sucesso (CAIO 24s, CIO 58s, CFO 1m10s, CTO 1m45s, COO 2m34s). Os 3 que timeoutaram caíram no Codex ainda limitado.

📁 Registros: `[F2] memory/decisions/2026-07-20-diagnostico-subagentes-cmo-cco-rate-limit.md`, `[F2] memory/decisions/2026-07-20-revisao-prompts-c-levels-obediencia-fallbacks.md`

- **Retorno do rate limit (20/07 tarde):** config de subagentes estava sumindo pós-restart do Gateway. Reaplicada e verificada: `model` + `runTimeoutSeconds=300` persistem agora. CCO rodou via OpenRouter DeepSeek: 3min45s, 97K tokens, curadoria Saúde concluída. Comprovado que fallback funciona quando Codex limita.

📁 `[F2] memory/decisions/2026-07-20-politica-servico-mutuo-entre-agentes.md`

---

## 🖥️ Ambiente Técnico — Infraestrutura do Container

**Consolidado do BOOTSTRAP.md original em 2026-07-24.**

- **Hospedagem:** Hostinger Docker container
- **Usuário:** non-root (comandos executados pelo agente, não pelo usuário)
- **Homebrew:** Instalado e disponível no container
- **Workspace raiz:** `/data/.openclaw/workspace/`
- **Modelo de IA:** `openai/gpt-5.5` como ID técnico canônico atual da Lôh e dos agentes. Registros antigos com `openai-codex/gpt-5.5` são históricos e não devem ser usados como configuração vigente.

### Regra de execução de comandos

O usuário (Jadielson) **não tem acesso ao terminal** do Docker container. Comandos que precisam rodar no terminal DEVEM ser executados pelo agente automaticamente, sem solicitar que o usuário os execute. Ver também `AGENTS.md` seção de ferramentas.

---

## ✅ 2026-07-24 — Nome oficial da empresa redefinido

**Decisão:** Jadielson definiu o nome oficial da empresa como **LÓGIKA - SOLUÇÕES DIGITAIS**.

- **Nome anterior:** LÓGIKA CREATIVE (referências ainda existem em arquivos históricos, mas o nome oficial passa a ser o novo)
- **Registrado em:** `USER.md` (seção "O que faço")
- **Impacto:** Usar o novo nome em comunicações oficiais, briefings, propostas e identidade. Arquivos históricos com o nome antigo não precisam ser renomeados — apenas o nome ativo/vigente é o novo.

## ✅ 2026-07-24 — Limpeza de BOOTSTRAP.md concluída

**Ação:** Todos os 13 BOOTSTRAP.md foram removidos dos workspaces ativos e arquivados.

- **Workspace principal:** `BOOTSTRAP.md` movido para `[F2] archive/backup-bootstrap/`
- **12 workspaces paralelos:** BOOTSTRAP.md copiados para `[F2] archive/backup-bootstrap/paralelos/` e removidos dos diretórios originais
- **GitHub backup:** Mantido (backup automático do repositório)
- **Consolidação:** Informações úteis (ambiente técnico, regra de execução de comandos) já integradas em `MEMORY.md` e `AGENTS.md`
- **Autorização extra (24/07):** Jadielson autorizou a remoção definitiva do archive do workspace principal. Pasta `[F2] archive/backup-bootstrap/` deletada. BOOTSTRAP.md só existe agora no backup do GitHub (`segundo-cerebro-jadielson`).
