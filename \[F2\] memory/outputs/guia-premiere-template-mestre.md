# 🎬 PREMIERE PRO — Template Mestre para Reels
## Template B — Personagem + Serviço (30s)

---

## PASSO 1 — Criar a Sequência

1. **File → New → Sequence**
2. Na janela que abrir, vá em **Settings**
3. Configure:

| Parâmetro | Valor |
|-----------|-------|
| Editing Mode | Custom |
| Timebase | **29.97fps** (ou 30fps se preferir) |
| Frame Size | **1080 horizontal × 1920 vertical** |
| Pixel Aspect Ratio | Square Pixels (1.0) |
| Fields | No Fields (Progressive Scan) |
| Display Format | 30fps Drop-Frame Timecode |
| Sample Rate | **48000 Hz** |

4. **Nomeie a sequência:** `TEMPLATE-B-30s`
5. Clique **OK**

> 💡 **Dica:** Se sua timeline aparecer deitada (1920×1080), é porque o Premiere não tem preset 9:16. Crie manualmente: Frame Size = 1080 × 1920.

---

## PASSO 2 — Criar os Slots na Timeline

Sua timeline terá **3 tracks de vídeo** e **2 tracks de áudio**.

### Track V1 — Takes principais
### Track V2 — Tela final (CTA)
### Track V3 — B-roll opcional
### Track A1 — Voz
### Track A2 — Trilha

```
V3:  [                    ]         [B-ROLL]
V2:                                [TELA FINAL]
V1:  [ABERTURA] [SERVIÇO] [PACIENTE] [CTA]
A1:  [SERVIDOR] [SERVIDOR] [PACIENTE]
A2:  [________________TRILHA_________________]
     0s         5s         14s      22s    30s
```

### Criar Marcadores de Slot

1. Posicione o playhead em **00:00:00**
2. **Marker → Add Marker** (ou `M`)
3. No marcador, escreva: `SLOT 1 — ABERTURA (0-5s)`
4. Repita para:
   - **00:00:05** → `SLOT 2 — SERVIÇO (5-14s)`
   - **00:00:14** → `SLOT 3 — PACIENTE (14-22s)`
   - **00:00:22** → `SLOT 4 — CTA (22-30s)`

---

## PASSO 3 — Criar os Itens do Template

### 3.1 — Tela de Transição (Abertura)

1. **File → New → Color Matte**
2. Escolha **Azul Claro (#0099CC)**
3. Nomeie: `Abertura-TemplateB`
4. Arraste pra V1, posicione em **00:00:00**
5. Corte o final em **00:00:05**

### 3.2 — Slots Vazios (Placeholders)

Como não temos takes ainda, use **Color Matte** preto como placeholder:

1. **File → New → Color Matte** → preto
2. Nomeie: `PLACEHOLDER-TAKE1`
3. Arraste pra V1, posicione **00:00:05 → 00:00:14**
4. Repita:
   - `PLACEHOLDER-TAKE2` → **00:00:14 → 00:00:22**
   - `PLACEHOLDER-TAKE3` → **00:00:22 → 00:00:30**

### 3.3 — Tela Final (CTA)

**Opção 1: Título do Premiere**

1. **File → New → Legacy Title**
2. Configure: 1080×1920
3. Fundo: Azul Claro (#0099CC)
4. Texto central:

```
📍 Povoado Serra
✅ Entrega concluída


[Logo Secretaria]

#SaúdeSãoSebastião
```

5. Fonte: **Montserrat Bold**, cor **branca**
6. Salve o título como `CTA-TemplateB`

**Opção 2: Photoshop**

Se tiver logo em PNG, crie a arte no Photoshop e importe como PNG 1080×1920.

---

## PASSO 4 — Aplicar Transições

Vá na aba **Effects** → procure cada transição:

| Entre Slots | Transição | Duração | Localização |
|------------|-----------|---------|-------------|
| Abertura → Take 1 | **Cross Dissolve** | 0.3s (12 frames) | Effects → Video Transitions → Dissolve |
| Take 1 → Take 2 | **Slide** | 0.4s (16 frames) | Effects → Video Transitions → Slide |
| Take 2 → Take 3 | **Cross Dissolve** | 0.3s (12 frames) | Effects → Video Transitions → Dissolve |
| Take 3 → Fim | **Cross Dissolve** | 0.5s (20 frames) | Effects → Video Transitions → Dissolve |

### Como aplicar:

1. Arraste a transição para a **borda entre dois clipes** na timeline
2. Clique duas vezes na transição aplicada
3. Ajuste a **duração** conforme tabela acima
4. ✅ Feito

---

## PASSO 5 — Configurar Áudio

### 5.1 — Track de Voz (A1)
Padrão, sem ajustes especiais.

### 5.2 — Track de Trilha (A2)

1. Deixe a track A2 vazia (é onde a música entra depois)
2. **Efeito padrão:** Clique com botão direito na track A2 → **Track Volume** → deixe em **-4dB** (cerca de 40% do máximo)
3. Isso garante que a voz (0dB) fique 60% mais alta que a música

---

## PASSO 6 — Salvar como Template Mestre

### Premiere Pro CC:

1. **File → Save As...**
2. Nome: `TEMPLATE-B-30s.prproj`
3. Salve em: `producao/templates-premiere/`

### Como reutilizar:

Na próxima produção:

1. Abra `TEMPLATE-B-30s.prproj`
2. Clique com **botão direito** no placeholder → **Replace Footage**
3. Selecione o take novo
4. Ajuste o corte se necessário
5. Troque a trilha
6. Atualize a tela final (endereço/data)
7. **Renderize**

> ⏱️ **Tempo estimado com template:** 10-15 minutos por reel

---

## PASSO 7 — Renderizar

1. **File → Export → Media** (ou `Ctrl+M`)
2. Configure:

| Parâmetro | Valor |
|-----------|-------|
| Format | **H.264** |
| Preset | **Match Source — Adaptive Bitrate** |
| Frame Size | **1920 × 1080** (ou **1080 × 1920** mantendo 9:16) |
| Bitrate | VBR 1 pass, Target 10Mbps |
| Audio | AAC, 320kbps, 48kHz |

3. Marque **Use Maximum Render Quality**
4. Clique **Export**

---

## 🗂️ Estrutura de Pastas Recomendada

```
producao/
├── templates-premiere/
│   ├── TEMPLATE-B-30s.prproj   ← Template B (Personagem)
│   ├── TEMPLATE-C-30s.prproj   ← Template C (Dados)
│   └── TEMPLATE-D-45s.prproj   ← Template D (Bastidores)
├── takes-brutos/
│   └── canetas-insulina-17jun/
│       ├── servidor-falando.mp4
│       ├── paciente-recebendo.mp4
│       └── b-roll-caixas.mp4
├── assets/
│   ├── trilhas/
│   ├── logos/
│   └── telas-CTA/
└── exportados/
    └── canetas-insulina-povoado-serra.mp4
```

---

*Criado em 17/06/2026 por Lôh para Jadielson*
*Premiere Pro CC — Template B (30s)*