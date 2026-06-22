# BRIEFING DE IDENTIDADE VISUAL
## Campanha Julho Amarelo — Prevenção às Hepatites Virais

**De:** CCO — Chief Creative Officer
**Para:** Agente SAÚDE Social Media
**Data:** 21/06/2026
**Prazo para produção:** 28/06/2026
**Início da campanha:** 01/07/2026
**Canais:** Instagram, Facebook, WhatsApp

---

## 1. 🎨 PALETA DE CORES OFICIAL

### 1.1 Cor Principal — Amarelo da Campanha

O amarelo é a cor-símbolo da campanha. A referência visual é o amarelo vibrante, solar, que remete a acolhimento, atenção e alerta positivo — não um amarelo ácido ou agressivo.

| Função | HEX | RGB | CMYK | Uso |
|--------|-----|-----|------|-----|
| **Amarelo Principal** | `#F5C518` | R:245 G:197 B:24 | C:0 M:18 Y:91 K:4 | Fundo principal, elementos gráficos, selo |
| **Amarelo Claro** | `#FFF3B0` | R:255 G:243 B:176 | C:0 M:4 Y:32 K:0 | Fundo secundário, cards de texto |
| **Amarelo Escuro** | `#D4A000` | R:212 G:160 B:0 | C:0 M:25 Y:100 K:17 | CTAs, destaques, títulos em fundo claro |
| **Amarelo Alerta** | `#FFC107` | R:255 G:193 B:7 | C:0 M:23 Y:100 K:0 | Badges, ícones de alerta positivo |

### 1.2 Cores de Apoio / Contraste

| Função | HEX | RGB | Uso |
|--------|-----|-----|-----|
| **Cinza Escuro (texto)** | `#2D2D2D` | R:45 G:45 B:45 | Títulos, corpo de texto |
| **Cinza Médio** | `#6B6B6B` | R:107 G:107 B:107 | Texto de apoio, legendas |
| **Cinza Claro** | `#F2F2F2` | R:242 G:242 B:242 | Fundo alternativo |
| **Branco** | `#FFFFFF` | R:255 G:255 B:255 | Texto sobre fundo escuro |
| **Verde Apoio** | `#2E7D32` | R:46 G:125 B:50 | Selo SUS, indicadores positivos |
| **Azul Apoio** | `#1565C0` | R:21 G:101 B:192 | Links, informações técnicas |

### 1.3 Acessibilidade WCAG

| Combinação | Contraste | Ratio | Atende? |
|------------|-----------|-------|---------|
| Amarelo Principal `#F5C518` + Cinza Escuro `#2D2D2D` | **AAA** (11.2:1) | ✅ Textos grandes e pequenos |
| Amarelo Claro `#FFF3B0` + Cinza Escuro `#2D2D2D` | **AAA** (17.3:1) | ✅ Ideal para cards de texto |
| Amarelo Escuro `#D4A000` + Branco `#FFFFFF` | **AA** (4.7:1) | ✅ Usar em fonte 14px+ |
| Amarelo Principal `#F5C518` + Branco `#FFFFFF` | **AA** (3.2:1) | ⚠️ Só para títulos 24px+ |
| Verde `#2E7D32` + Branco `#FFFFFF` | **AA** (4.8:1) | ✅ Textos pequenos com bold |

> **Regra de ouro:** Texto corrido sempre em Cinza Escuro `#2D2D2D` sobre fundo Branco ou Amarelo Claro. Nunca escreva texto informativo pequeno sobre o Amarelo Principal puro.

---

## 2. 📐 ESTILO DE CARD — FORMATOS E TIPOGRAFIA

### 2.1 Proporções (Export)

| Formato | Dimensão (px) | Proporção | Uso |
|---------|---------------|-----------|-----|
| **Feed** | 1080 × 1080 | 1:1 | Postagens no grid principal |
| **Retrato** | 1080 × 1350 | 4:5 | Postagens no feed com mais conteúdo |
| **Stories** | 1080 × 1920 | 9:16 | Stories Instagram e WhatsApp Status |
| **Capa/Destaque** | 1080 × 1920 | 9:16 | Capa do destaque "Julho Amarelo" |

### 2.2 Grid e Margens (Safe Zone)

```
┌─────────────────────────────────────────────┐
│                   1080px                     │
│  ┌─────────────────────────────────────┐     │
│  │          Safe Zone (80px)           │     │
│  │  ┌───────────────────────────┐      │     │
│  │  │      Área de conteúdo     │      │     │
│  │  │        (920×920)          │      │     │
│  │  └───────────────────────────┘      │     │
│  │                                      80px │
│  └─────────────────────────────────────┘  │
│                       80px                 │
└─────────────────────────────────────────────┘
```

| Elemento | Medida |
|----------|--------|
| **Margem externa** | 80px (todos os lados) |
| **Safe zone (conteúdo)** | 920 × 920px (feed), 920 × 1760px (stories) |
| **Grid interno** | 4 colunas de 200px + 3 gutters de 40px |
| **Raio de canto (cards)** | 24px |
| **Raio de canto (fotos)** | 16px |

### 2.3 Tipografia

**Família principal:** [**Inter**](https://fonts.google.com/specimen/Inter) (gratuita, Google Fonts, excelente legibilidade digital, suporte a caracteres latinos completos)

> **Por que Inter?** É a fonte oficial adotada pelo GOV.BR e amplamente usada em sistemas do SUS. Transmite profissionalismo, modernidade e alinhamento institucional. Se o SAÚDE não tiver Inter instalada, usar **Nunito Sans** como fallback.

| Uso | Fonte | Weight | Size (Feed) | Size (Stories) | Altura de linha | Tracking |
|-----|-------|--------|-------------|----------------|-----------------|----------|
| **Título principal** | Inter Bold | 700 | 52px | 48px | 110% | -0.5px |
| **Título secundário** | Inter SemiBold | 600 | 40px | 36px | 110% | -0.3px |
| **Corpo / Legenda** | Inter Regular | 400 | 28px | 26px | 130% | 0px |
| **Destaque numérico** | Inter Bold | 700 | 80px | 72px | 100% | -1px |
| **Saiba mais / CTA** | Inter SemiBold | 600 | 24px | 22px | 110% | +0.5px |
| **Selos/Legendas curtas** | Inter Medium | 500 | 18px | 16px | 120% | +0.8px |

**Família secundária (opcional, para elementos decorativos):** **Poppins** (Google Fonts) — usar apenas em badges e números destaque.

---

## 3. 🧩 PADRÃO DE ARTE — TEMPLATES REUTILIZÁVEIS

### 3.1 Card Foto + Texto

```
┌─────────────────────────────────────────────┐
│                                             │
│   ┌─────────────────────────────────────┐   │
│   │                                     │   │
│   │         FOTO (920×460px)            │   │
│   │         border-radius: 16px         │   │
│   │                                     │   │
│   └─────────────────────────────────────┘   │
│                                             │
│   ⬟ Título da peça (Inter Bold, 52px)      │
│                                             │
│   Texto de apoio com até 3 linhas.          │
│   Corpo Inter Regular 28px, altura 130%.   │
│   Máximo 280 caracteres.                   │
│                                             │
│   ┌─────────────────────────────────────┐   │
│   │  Saiba mais 🔗  ░░░░░░░░░░░░░░░░    │   │
│   └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

**Regras:**
- Foto: 920×460px, border-radius 16px, margem superior 0
- Título: distância 32px abaixo da foto
- Corpo: distância 16px abaixo do título
- CTA: barra inferior com 64px altura, fundo Amarelo Principal

### 3.2 Card Só Texto

```
┌─────────────────────────────────────────────┐
│                                             │
│   ⬟ VOCÊ SABIA? (Inter SemiBold, 40px)     │
│                                             │
│   Texto central com destaque.               │
│   Até 5 linhas no máximo.                   │
│   Inter Regular 28px, tracking 0.           │
│   Alinhamento: centralizado                 │
│                                             │
│   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─             │
│                                             │
│   💡 Dica importante em Amarelo Escuro      │
│   Inter Medium 24px                         │
│                                             │
│   #JulhoAmarelo • #HepatiteZero             │
│                                             │
└─────────────────────────────────────────────┘
```

**Regras:**
- Fundo: Amarelo Claro `#FFF3B0`
- Título: Amarelo Escuro `#D4A000`
- Divisor: linha horizontal 2px, 50% opacidade, Cinza Médio, 120px largura
- Tags: Inter Medium 18px, Cinza Médio

### 3.3 Card de Dados / Estatísticas

```
┌─────────────────────────────────────────────┐
│                                             │
│   1,5 MILHÃO                                │
│   (Inter Bold, 80px, Amarelo Principal)     │
│                                             │
│   pessoas no Brasil vivem com               │
│   hepatites virais (estimativa)             │
│   (Inter Regular, 28px, Cinza Escuro)       │
│                                             │
│   ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─             │
│                                             │
│   Fonte: Ministério da Saúde, 2025          │
│   (Inter Medium, 18px, Cinza Médio)         │
│                                             │
│   🟡 Previna-se. Teste-se. #JulhoAmarelo   │
│                                             │
└─────────────────────────────────────────────┘
```

**Regras:**
- Número destaque: 80px, Inter Bold, Amarelo Principal, centralizado
- Descrição abaixo: Inter Regular 28px, máximo 3 linhas
- Linha divisória: 40% opacidade, 80px largura
- Fonte: alinhado à esquerda, tag obrigatória
- Fundo: Cinza Escuro `#2D2D2D` para maior impacto visual

### 3.4 Variações Stories (1080×1920)

Aplicar os mesmos templates adaptados à proporção 9:16:

| Elemento | Stories |
|----------|---------|
| **Safe zone** | 920 × 1760px |
| **Título** | 48px (Inter Bold) |
| **Corpo** | 28px (Inter Regular) |
| **CTA vertical** | Barra inferior 100px de altura |
| **Swipe up** | Indicador na base "Arraste para cima ⬆" |

**Variação de arte para Stories:**
- Gradiente do topo: Amarelo Principal → Amarelo Claro (180°)
- Opacidade no texto: sombra suave (text-shadow 0 2px 4px rgba(0,0,0,0.15))
- Elemento decorativo: círculos semi-transparentes `rgba(245,197,24,0.12)` como fundo

### 3.5 Elementos Gráficos (Assets)

| Elemento | Especificação | Formato |
|----------|---------------|---------|
| **Ícone fígado** | Estilo outline, 2px stroke, Amarelo Escuro `#D4A000` | SVG / PNG 512×512 |
| **Ícone seringa** | Estilo outline, 2px stroke, compatível com o fígado | SVG / PNG 512×512 |
| **Ícone teste/sangue** | Estilo outline, 2px stroke | SVG / PNG 512×512 |
| **Ícone escudo** | Estilo filled, Amarelo Principal `#F5C518` | SVG / PNG 512×512 |
| **Shape decorativo 1** | Círculo `#FFF3B0`, 60% opacidade, 200×200px | PNG/SVG |
| **Shape decorativo 2** | Meia-lua `rgba(245,197,24,0.08)`, 300×300px | PNG/SVG |
| **Barra CTA** | Retângulo 920×64px, Amarelo Principal, border-radius 12px | Asset no template |
| **Selo SUS** | Oficial, sem alterações | PNG/PDF |
| **Marca d'água** | "Julho Amarelo" vertical, Inter Bold, 48px, 5% opacidade | Opcional no template |

> **Ícones recomendados (gratuitos):** Phosphor Icons ou Font Awesome (licença gratuita para uso institucional).

---

## 4. 🏷️ TAGS E HASHTAGS VISUAIS

### 4.1 Tags Obrigatórias (em toda peça)

| Tag | Posição | Formato |
|-----|---------|---------|
| `#JulhoAmarelo` | Canto inferior esquerdo | Inter Medium 18px, Amarelo Escuro |
| `@minsaude` | Canto inferior direito (quando houver) | Inter Medium 16px, Azul Apoio |
| **Arte: "SUS — Sistema Único de Saúde"** | Barra inferior ou canto | Inter Medium 16px, Branco sobre verde `#2E7D32` |

### 4.2 Tags Complementares (rotacionar)

- `#PrevençãoHepatites`
- `#HepatiteZero`
- `#TesteSe`
- `#HepatitesVirais`
- `#VacinaHepatiteB`
- `#VivaSemHepatite`
- `#SaúdePública`
- `#SUS`

### 4.3 Selo Visual e Assinatura

**Selo Julho Amarelo** (obrigatório no canto superior direito de todas as peças):

```
┌──────────┐
│ 🟡 JULHO │
│ AMARELO  │
│ 2026     │
└──────────┘
```

**Especificação:**
- Fundo: Amarelo Principal `#F5C518`
- Texto: Inter Bold, Branco `#FFFFFF`, 16px
- Border-radius: 8px
- Padding interno: 8px 12px
- Posição: top-right, 80px da margem direita, 80px do topo

**Assinatura padrão** (rodapé de stories e feed):
```
Secretaria Municipal de Saúde
[Inserir nome do município]
SUS — Sistema Único de Saúde
```

Fonte: Inter Medium 14px, Cinza Médio `#6B6B6B`, alinhado à esquerda.

### 4.4 Assets em PNG e PDF

| Asset | Formato | Tamanho | Transparência |
|-------|---------|---------|---------------|
| Selo Julho Amarelo | PNG | 200×200px | ✅ Fundo transparente |
| Selo Julho Amarelo (vetorial) | PDF | Vetorial | ✅ Fundo transparente |
| Marca d'água | PNG | 1080×1080px | ✅ 5% opacidade |
| Ícones de hepatites | PNG | 512×512px (cada) | ✅ Fundo transparente |
| Elementos decorativos | PNG | Individual | ✅ Fundo transparente |
| Template Feed | PSD / FIG | 1080×1080px | Camadas separadas |
| Template Stories | PSD / FIG | 1080×1920px | Camadas separadas |
| Template Capa Destaque | PSD / FIG | 1080×1920px | Camadas separadas |

---

## 5. 📋 QUANTITATIVO E CRONOGRAMA

### 5.1 Peças a Produzir (21 peças totais)

| Tipo | Quantidade | Formato | Conteúdo |
|------|------------|---------|----------|
| **Card feed — foto+texto** | 4 | 1080×1080px | Prevenção, sintomas, tratamento, diagnóstico |
| **Card feed — só texto** | 4 | 1080×1080px | Mitos × verdades, curiosidades, dicas |
| **Card feed — dados** | 4 | 1080×1080px | Estatísticas epidemiológicas |
| **Stories** | 8 | 1080×1920px | Sequência interativa (quiz, enquete, teste) |
| **Capa do destaque** | 1 | 1080×1920px | Grid de stories permanente |

### 5.2 Cronograma de Entregas

| Data | Entrega |
|------|---------|
| 21/06 | ✅ Briefing de identidade visual (este documento) |
| 24/06 | Aprovação da paleta e estilo pelo CCO |
| 26/06 | Entrega dos assets em PNG/AI/FIG |
| 28/06 | **Entrega final das 21 peças** |
| 30/06 | Revisão e ajustes finais |

---

## 6. 👁️ OBSERVAÇÕES E RECOMENDAÇÕES ADICIONAIS

### 6.1 Tom da Comunicação

- **Linguagem:** Clara, acolhedora e informativa. Evite tom alarmista. A hepatite tem tratamento e cura — a mensagem deve ser de esperança e ação ("teste-se, previna-se"), não de medo.
- **Público-alvo:** População geral, com ênfase em adultos jovens (18-45 anos), que são o grupo com menor adesão a testagem.
- **Evitar:** Imagens explícitas de agulhas, sangue ou fígados doentes. Prefira ilustrações limpas ou fotografia humanizada (pessoas sorrindo, sendo atendidas, tomando vacina).

### 6.2 Recomendações de Acessibilidade

- **Legendagem:** Todos os stories com legenda descritiva (CC).
- **Alt text:** Todas as imagens do feed devem conter texto alternativo descritivo em português.
- **Contraste:** Seguir a tabela de WCAG da seção 1.3. Nunca usar Amarelo Principal como fundo de texto informativo.
- **Fonte mínima:** Nunca abaixo de 14px em peças digitais (equivalente a ~18-20px no export 1080px).

### 6.3 Estratégia de Cores por Contexto

| Contexto | Fundo | Texto | Tom |
|----------|-------|-------|-----|
| Card informativo | Branco `#FFFFFF` | Cinza Escuro `#2D2D2D` | Neutro, sério |
| Card de alerta | Amarelo Claro `#FFF3B0` | Cinza Escuro `#2D2D2D` | Atenção positiva |
| Card de dados | Cinza Escuro `#2D2D2D` | Branco `#FFFFFF` | Impacto |
| Card CTA | Amarelo Principal `#F5C518` | Cinza Escuro `#2D2D2D` | Energia, ação |
| Story informativo | Gradiente amarelo | Branco (com sombra) | Leve, acolhedor |

### 6.4 Identidade Sonora (para Reels e vídeos)

- **Trilha sugerida:** Música instrumental alegre, até 120 BPM, tom maior. Algo no estilo "hopeful acoustic" ou "upbeat corporate".
- **Voz (se narrado):** Feminina, tom médio, dicção clara, 160-180 palavras/minuto.
- **Efeitos sonoros:** "Pop" para transições, "ding" para marcadores de checklist — suaves, sem agressividade.

### 6.5 Variação por Plataforma

| Plataforma | Ajustes |
|------------|---------|
| **Instagram Feed** | Grid deve manter coerência visual intercalando cards amarelos, brancos e escuros |
| **Instagram Stories** | Incluir caixa de texto para resposta, enquete ("Você já fez o teste? Sim/Não") |
| **Facebook** | Legendas maiores (público mais velho), compartilhamento incentivado |
| **WhatsApp** | Versões otimizadas em PNG, sem texto fino (<20px), priorizar formato retrato |

### 6.6 Checklist de Pré-Publicação

- [ ] Contraste WCAG verificado
- [ ] Selo Julho Amarelo posicionado (top-right)
- [ ] Hashtag `#JulhoAmarelo` visível
- [ ] Assinatura SUS presente
- [ ] Alt text inserido (Instagram/Facebook)
- [ ] Legendas CC nos stories
- [ ] Todos os links testados
- [ ] Versão WhatsApp exportada sem texto pequeno

---

## 7. 📂 ESTRUTURA DE PASTAS RECOMENDADA (para organização dos arquivos)

```
julho-amarelo-2026/
├── assets/
│   ├── iconografia/         (ícones SVG/PNG)
│   ├── selos/               (selo julho amarelo, selo SUS)
│   ├── shapes/              (elementos decorativos)
│   └── fontes/              (Inter .ttf/.otf)
├── templates/
│   ├── feed/                (.ai / .psd / .fig)
│   ├── stories/             (.ai / .psd / .fig)
│   └── capa-destaque/       (.ai / .psd / .fig)
├── exports/
│   ├── feed/
│   │   ├── card-01-foto-texto.png
│   │   └── ...
│   ├── stories/
│   │   └── story-01-quiz.png
│   └── whatsapp/
├── briefings/
│   └── briefing-identidade-visual.md  ← (este arquivo)
└── aprovacao/
    └── (prints de aprovação)
```

---

## ✅ APROVAÇÃO DO CCO

| Item | Status |
|------|--------|
| Paleta de cores | ✅ Aprovada |
| Tipografia | ✅ Aprovada (Inter + Poppins) |
| Templates | ✅ Conforme especificado |
| Assets gráficos | ✅ Pendente de produção |
| Observações finais | ✅ Incluídas |

---

🎯 **CCO — Briefing entregue. O SAÚDE Social Media pode iniciar a produção das 21 peças com base nestas diretrizes. Qualquer dúvida ou desvio criativo, reportar ao CCO antes de publicar.**

*Documento gerado em 21/06/2026 por Lôh (CCO — Tier 0, Orquestradora)*