# RITUAL OPERACIONAL — C-Level Squad da Lógika

Data: 2026-06-07  
Status: Ativo  
Versão: 1.0

---

## 🎯 Princípio Fundamental

O C-Level Squad é um **conselho de inteligência distribuído no Telegram**. Não é:
- Uma ferramenta de automação cega (cada agente tem poder limitado)
- Um substituto para decisões humanas (você decide; agentes informam)
- Um simulador genérico (eles leem contexto real do vault)

É:
- Um **multiplier do seu tempo** — você pergunta, 8 cérebros respondem em paralelo
- Um **sistema de checks & balances** — cada agente aponta riscos do seu eixo
- Uma **forma de pensar estruturada** — decisões vêm de múltiplas lentes

---

## 1. DEMANDAS PONTUAIS (dia a dia)

Quando você tem uma pergunta simples ou task que cabe em uma cadeira.

### Padrão

```
[tópico do agente]
[comando direto]

Exemplo: @cro — temos 5 leads quentes. Vale a pena vender pacote anual ou semestral?
```

### Tempo de resposta esperado

- **Rápido:** 30min-1h (agente responde com análise + recomendação)
- **Normal:** 1-4h (agente aprofunda com contexto do vault)
- **Nada demora mais que 8h** (se demorar, é trava externa — você intervém)

### Exemplos reais

**Comercial:**
```
CRO: qual a taxa de conversão do funil nos últimos 30 dias?
```

**Técnico:**
```
CTO: quanto custa escalar suporte pra 5 clientes novos? Qual o SLA que dá pra prometer?
```

**Finanças:**
```
CFO: qual a margem operacional de cada linha de serviço?
```

**Marketing:**
```
CMO: como posicionar a linha de TI/WhatsApp inteligente pra Câmara e SINDSS?
```

---

## 2. ESCALAÇÃO (quando 2+ agentes precisam colaborar)

Quando você tem uma demanda que mexe em múltiplas áreas.

### Padrão Tipo A — Demanda cruzada simples

```
@[agente1] @[agente2] — [contexto]
[agente1]: [pergunta 1]
[agente2]: [pergunta 2]
```

### Padrão Tipo B — Análise de viabilidade

```
Pensei em [novo serviço/projeto].
@CMO: como posicionar? 
@CRO: qual preço?
@CFO: qual margem?
@CTO: viável tecnicamente?
```

### Tempo de resposta esperado

- **Respostas chegam em 2-4h** (cada um responde no seu thread)
- **Você sintetiza as respostas e toma a decisão**
- Se houver conflito (tipo "CFO diz não viável; CRO diz sim, vai dar dinheiro"), você convoca Conselho

### Exemplos reais

**Lançar novo serviço:**
```
Vamos oferecer "WhatsApp inteligente com IA" como produto novo.
@CMO: qual o posicionamento? Em qual segmento?
@CRO: qual preço competitivo?
@CFO: qual investimento em desenvolvimento? Qual break-even?
@CTO: qual a stack técnica? Tempo de execução?
@CAIO: qual a maturidade? Risco de IA?
```

**Escalação de produção:**
```
Recebemos 3 clientes novos ao mesmo tempo. Conseguimos entregar?
@COO: qual o gargalo? Precisa mais gente?
@CCO: qual o prazo de produção?
@CTO: infra aguenta?
@CFO: qual o custo?
```

---

## 3. CONSELHO DE IA (decisões complexas, transversais)

Quando a decisão é **estratégica** e mexe com **3+ áreas** simultaneamente.

### Padrão

```
@loh convoca conselho
Tema: [tema complexo]
Prazo: [quanto tempo pra responder]
Lentes convocadas: [quais agentes]

Contexto: [background]
```

### Como funciona

1. LÔH **recebe** a convocação
2. LÔH **convida** as lentes (C-Levels) relevantes
3. **Cada um responde** com sua perspectiva
4. LÔH **sintetiza** as posições
5. **Você aprova/rejeita/ajusta**

### Quando convocar

- Decisão afeta receita E operação
- Há desacordo entre agentes
- Risco legal/compliance envolvido
- Investimento significativo

### Exemplo real

```
LÔH: Conselho.
Tema: Aumentar de 3 para 8 clientes em 3 meses.
Lentes: COO, CRO, CFO, CTO, CIO.
Prazo: 4h.

Contexto: Recebemos ofertas de 5 clientes novos. Margem boa, demanda real.
Dúvida: conseguimos entregar sem comprometer qualidade/caixa/conformidade?

COO: análise de capacidade operacional
CRO: análise de relacionamento/margem
CFO: impacto no caixa
CTO: capacidade técnica
CIO: risco de compliance/dados

```

---

## 4. CHECK-IN PERIÓDICO (semanal ou mensal)

Cada semana (ou mês), você puxa o **placar de saúde** da empresa via agentes.

### Padrão

```
Placar [período: semana X / mês X]

@coo: quantos processos saíram do manual para L1/L2?
@cro: qual o funil? (leads → proposta → fechado)
@cfo: qual o runway de caixa?
@cio: tem algum risco de conformidade pendente?
@caio: qual a maturidade de automação hoje?
```

### O que esperar

- **COO:** tendência de automação / gargalos novos
- **CRO:** quantitativo do funil / conversão / ticket médio
- **CFO:** dias de caixa restantes / queima de caixa / margem por cliente
- **CIO:** alertas de conformidade / acessos problemáticos / riscos
- **CAIO:** processos prontos pra automação / ROI das automações existentes

### Por que importa

Você consegue **monitorar a saúde** sem estar em reunião cara com todo mundo. Cada um entrega número/diagnóstico, você vê padrões.

---

## 5. CONTEXTO VINDO DO VAULT (como alimentar)

Os agentes **leem contexto do vault automaticamente**. Você alimenta, eles usam.

### Como funciona

Você coloca informação em `segundo-cerebro-jadielson` (GitHub), a Lôh sincroniza, e os agentes leem quando precisam.

### O que colocar lá

**Para CRO (comercial):**
- `[F2] memory/agents/logika-cro.md` → funil atual, leads, prospectos, estágio, ticket médio, clientes por segmento

**Para COO (operações):**
- `[F2] memory/context/operacao.md` → capacidade da equipe, processos documentados, gargalos conhecidos, OKRs atuais

**Para CFO (finanças):**
- `[F2] memory/context/financeiro.md` → margens por serviço, custos fixos/variáveis, caixa atual, previsão

**Para CMO (marketing):**
- `[F2] memory/agents/logika-cmo.md` → posicionamento por segmento, pilares de conteúdo, audiências, métricas

**Para CCO (criação):**
- `[F2] memory/agents/logika-cco.md` → padrão criativo, templates, guia de marca por cliente, capacidade de produção

**Para CTO (tecnologia):**
- `[F2] memory/agents/logika-cto.md` → stack técnica, SLAs atuais, capacidade de infra, roadmap técnico

**Para CIO (governança):**
- `[F2] memory/agents/logika-cio.md` → políticas de dados, conformidade LGPD, acessos, ferramentas usadas, riscos conhecidos

### Exemplo

Se você quer que o CRO responda "qual a margem do serviço X?", coloque:
```markdown
# [F2] memory/agents/logika-cro.md

## Serviços & Margens

| Serviço | Preço Médio | Custo | Margem | Clientes |
|---------|------------|-------|--------|----------|
| Vídeo Institucional | R$5k | R$1.5k | 70% | 5 |
| WhatsApp Inteligente | R$2k/mês | R$800 | 60% | 2 |
| Suporte Técnico Gerenciado | R$1.5k/mês | R$600 | 60% | 1 |
```

Quando você perguntar, o CRO vai ler isso e responder **com inteligência**, não genérico.

---

## 6. QUANDO ESCALAR PARA VOCÊ (humano)

Agentes **param e pedem decisão humana** em:

| Tópico | Quem Decide | Quem Executa |
|--------|-------------|--------------|
| Preço / negociação comercial | Jadielson | Jadielson + CRO |
| Investimento / custo significativo | Jadielson + CFO | Jadielson + contador |
| Questão jurídica | Jadielson | advogado externo |
| Criação / direção final | Jadielson | Jadielson + Ewander |
| Autoaprovação de automação | Jadielson | LÔH + CAIO |

### Exemplo

```
CTO: "Viabilidade: sim. Custo de infra pra escalar: R$3k/mês.
Recomendação: implementar. Precisa da sua aprovação do investimento."
→ Você aprova, CFO autoriza, CTO executa (com Alex)
```

---

## 🔄 FLUXO VISUAL

```
Pergunta simples (1 agente)
        ↓
        └→ 30min - 1h → Resposta + recomendação

Pergunta cruzada (2-3 agentes)
        ↓
        └→ 2-4h → Cada um responde → Você sintetiza

Decisão complexa (4+ agentes)
        ↓
        └→ Conselho convocado → 4h → LÔH sintetiza → Você aprova

Check-in periódico (todos os 8)
        ↓
        └→ Semanal/mensal → Placar de saúde → Você vê padrões

Contexto muda
        ↓
        └→ Você atualiza vault → Agentes leem → Próximas respostas melhoram
```

---

## 💡 DICAS PRÁTICAS

1. **Seja específico:** "funil comercial" é vago; "qual a taxa de conversão de proposta para fechamento?" é claro.

2. **Contexto custa pouco:** se o agente não souber o background, ele pode perguntar ou assumir genérico. Alimentar o vault é investimento.

3. **Síntese é sua responsabilidade:** os agentes respondem *perspectives*; você que vê padrões e decide.

4. **Teste antes de usar em produção:** faz uma pergunta de teste, vê como responde, ajusta contexto se precisar.

5. **Confie nos números:** quando CFO diz "margem ruim", provavelmente está certo. Quando CRO diz "demanda alta", valida com CFO.

---

## 📝 REVISÕES

- **v1.0** (2026-06-07): Ritual inicial após deploy do C-Level Squad.

---

*Criado pela Lôh após deploy completo do C-Level Squad. Ajuste conforme o uso mostrar o que funciona.*
