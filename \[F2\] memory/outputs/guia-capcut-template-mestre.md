# 📱 CAPCUT — Template Mestre para Reels
## Template B — Personagem + Serviço (30s)

---

## 📱 PLATAFORMA

Este guia funciona para **CapCut Desktop** (PC/Mac) — é onde monta o template. Depois de salvo, dá pra abrir e editar no **CapCut Mobile** também.

---

## PASSO 1 — Criar Projeto

### No CapCut Desktop:

1. Abra o **CapCut**
2. Clique em **+ Novo Projeto**
3. Configure:

| Parâmetro | Valor |
|-----------|-------|
| Proporção | **9:16** (vertical) |
| Resolução | **1080×1920** |
| Quadros por segundo | **30fps** |
| Duração | **30 segundos** |

4. Nomeie: `TEMPLATE-B-30s`
5. Clique **Criar**

---

## PASSO 2 — Montar a Linha do Tempo

A timeline do CapCut tem **track principal (V1)** + tracks adicionais.

### Track V1 — Takes
### Track V2 — Tela final / textos
### Track A1 — Voz
### Track A2 — Música

```
V2:                                [TEXTO FINAL]
V1:  [ABERTURA] [SERVIÇO] [PACIENTE] [CTA]
A1:  [GRV.AUDIO] [GRV.AUDIO] [GRV.AUDIO]
A2:  [________________TRILHA_________________]
     0s         5s         14s      22s    30s
```

### Criar os Placeholders (antes de ter os takes)

Como ainda não gravou os takes, use clipes de **cor sólida** como marcadores:

1. Clique em **Media** → aba **Solid Color**
2. Escolha **preto**
3. Arraste pra timeline:

| Slot | Cor | Posição | Duração |
|------|-----|---------|---------|
| ABERTURA | Azul Claro (#0099CC) | 00:00 → 00:05 | 5s |
| TAKE 1 (Serviço) | Cinza (#666666) | 00:05 → 00:14 | 9s |
| TAKE 2 (Paciente) | Cinza (#999999) | 00:14 → 00:22 | 8s |
| CTA | Azul Claro (#0099CC) | 00:22 → 00:30 | 8s |

---

## PASSO 3 — Adicionar Textos de Orientação

Pra não esquecer o que cada slot significa, adicione textos:

1. Clique em **Text → Add Text**
2. Digite: `🎬 ABERTURA — Servidor chegando`
3. Posicione sobre o primeiro slot (00:00 → 00:05)
4. Fonte: **Montserrat Bold**, 40pt, cor **branca**
5. Fundo: preto 50% transparência pra legibilidade

Repita:

| Slot | Texto |
|------|-------|
| 00:05 → 00:14 | `📋 TAKE 1 — Servidor explica serviço` |
| 00:14 → 00:22 | `👤 TAKE 2 — Paciente recebe caneta` |
| 00:22 → 00:30 | `📍 CTA — Tela final com endereço` |

> 💡 **Dica:** Esses textos são só orientação. Na hora de editar com takes reais, é só apagar ou desativar a visibilidade.

---

## PASSO 4 — Aplicar Transições

No CapCut, as transições ficam na aba **Transitions**.

### Como aplicar:

1. Clique na aba **Transitions** no painel esquerdo
2. Escolha a transição
3. Arraste para **entre** os dois clipes na timeline

### Transições do Template B:

| Entre | Transição | Duração | Onde encontrar |
|-------|-----------|---------|----------------|
| Abertura → Take 1 | **Fade** | 0.3s (10 frames) | Aba Transitions → Basic → Fade |
| Take 1 → Take 2 | **Slide Right** | 0.4s (12 frames) | Aba Transitions → Slide → Slide Right |
| Take 2 → Take 3 | **Fade** | 0.3s (10 frames) | Aba Transitions → Basic → Fade |
| Final | **Fade Out** | 0.5s (15 frames) | Aba Transitions → Basic → Fade Out |

### Para ajustar a duração:

1. Clique **duas vezes** na transição na timeline
2. No painel direito, ajuste **Duration** para o valor acima
3. ✅

---

## PASSO 5 — Criar a Tela Final (CTA)

A tela final é uma **imagem** ou **texto** com fundo Azul Claro.

### Opção 1: Imagem PNG (recomendado)

Crie uma imagem 1080×1920 no Photoshop/Canva com:

```
Fundo: Azul Claro (#0099CC)

📍 Povoado Serra
✅ Entrega concluída


[Logo Secretaria]

#SaúdeSãoSebastião
```

Importe e arraste pra timeline (00:22 → 00:30).

### Opção 2: Texto no CapCut

1. Clique em **Text → Add Text**
2. Escreva o conteúdo conforme acima
3. Fundo: clique em **Background** → cor sólida → **Azul Claro (#0099CC)**
4. Fonte: **Montserrat Bold**, cor **branca**
5. Alinhe tudo no centro
6. Duração: 00:22 → 00:30

**Animação do texto:**

1. Selecione o texto
2. Aba **Animation**
3. Escolha **Fade In** (0.5s) na entrada
4. ✅

---

## PASSO 6 — Áudio

### Track de Voz (A1)

A voz virá dos takes gravados — o áudio já vem junto com o vídeo.

**Ajuste de volume da voz:**

1. Selecione o clipe de vídeo na timeline
2. No painel direito, aba **Audio**
3. Volume: **100%** (ou 0dB)
4. Marque **Remove Background Noise** se o ambiente estiver com ruído

### Track de Música (A2)

1. Clique em **Audio → Music**
2. Pesquise: "acoustic calm" ou "hopeful"
3. Selecione uma faixa (80-90 BPM, instrumental, sem vocal)
4. Arraste pra track A2

**Ajuste de volume:**

1. Selecione a faixa na timeline
2. Volume: **40%** (ou -8dB aproximadamente)
3. Marque **Fade In** (0.5s) e **Fade Out** (1s)

---

## PASSO 7 — Salvar como Template

### No CapCut Desktop:

1. **File → Save Project As...**
2. Nome: `TEMPLATE-B-30s`
3. Salve em: `producao/templates-capcut/`

### No CapCut Mobile:

O projeto do CapCut Desktop **sincroniza com a nuvem CapCut**. Se você tiver conta:

1. No Desktop: **File → Export → Save to Cloud**
2. No Mobile: Abra CapCut → **Cloud Projects** → Baixe o projeto
3. Pronto pra editar no celular

---

## PASSO 8 — Como Usar na Próxima Produção

### Fluxo rápido (Desktop):

1. Abra `TEMPLATE-B-30s` (File → Open Project)
2. Selecione o placeholder preto na timeline
3. **Clique com botão direito → Replace**
4. Escolha o take novo do arquivo
5. O CapCut mantém a duração e transições automaticamente
6. Atualize a tela final (endereço, data)
7. Troque a música se quiser

### Fluxo rápido (Mobile):

1. Abra o projeto na nuvem
2. Toque no placeholder → **Replace**
3. Selecione o vídeo novo da galeria
4. Edite texto do CTA
5. Exporte

> ⏱️ **Tempo com template:** 10 minutos no Desktop, 15 no Mobile

---

## PASSO 9 — Renderizar (Exportar)

### No Desktop:

1. **File → Export** (ou Ctrl+E)
2. Configure:

| Parâmetro | Valor |
|-----------|-------|
| Resolution | **1080×1920** |
| Frame Rate | **30fps** |
| Bitrate | **Higher** (ou 10Mbps) |
| Format | **MP4** |
| Codec | **H.264** |

3. Clique **Export**

### No Mobile:

1. Toque no ícone de **seta pra cima** (canto superior direito)
2. Resolução: **1080p**
3. Frame Rate: **30fps**
4. Bitrate: **Recomendado** (ou Mais Alto)
5. Exporte

---

## 🗂️ Estrutura de Pastas no CapCut

Dentro do CapCut, organize seus templates assim:

```
Meus Projetos/
├── TEMPLATE-B-30s            ← Template Personagem
├── TEMPLATE-C-30s            ← Template Dados
├── TEMPLATE-D-45s            ← Template Bastidores
├── canetas-insulina-serra    ← Projeto real (cópia do template)
└── proximo-reel              ← Próximo projeto
```

**Regra:** Nunca edite o template original. Sempre **Salvar Como** antes de começar.

---

## ✅ CHECKLIST — Configuração Inicial

- [ ] Projeto criado (9:16, 1080×1920, 30fps, 30s)
- [ ] Placeholders coloridos em cada slot
- [ ] Textos de orientação em cada slot
- [ ] Transições aplicadas entre todos os slots
- [ ] Tela final criada (CTA)
- [ ] Áudio configurado (voz 100% / música 40%)
- [ ] Projeto salvo como `TEMPLATE-B-30s`
- [ ] Backup no cloud (para mobile) — opcional

---

*Criado em 17/06/2026 por Lôh para Jadielson*
*CapCut Desktop — Template B (30s)*