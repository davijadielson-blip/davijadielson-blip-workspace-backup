# 🛠️ GUIA — Projeto Mestre (Premiere / CapCut / DaVinci)
## Entrega Canetas de Insulina | Povoado Serra

**Template B — Personagem + Serviço (30s)**

---

## 📐 CONFIGURAÇÃO DO PROJETO (qualquer editor)

| Parâmetro | Valor |
|-----------|-------|
| Resolução | 1920 × 1080 (1080p vertical) |
| Taxa de quadros | 30fps |
| Formato | 9:16 (gire 90° ou configure como vertical) |
| Codec áudio | AAC, 44.1kHz, 128kbps |

**⚠️ Importante:** Crie o projeto em **9:16 vertical** (1080×1920) ou filme em paisagem e gire 90° na timeline. Se o editor não tiver preset vertical, crie sequência 1080×1920.

---

## 📦 LINHA DO TEMPO — Slots Prontos

```
─── SEQUÊNCIA: 30 segundos ────────────────────────────

[TRACK V1]  ┌──────┬────────┬──────────┬──────────────┐
            | CENA1| CENA2  | CENA3    | CENA4/CTA    |
            | 0-5s | 5-14s  | 14-22s   | 22-30s       |
            └──────┴────────┴──────────┴──────────────┘

[TRACK V2]                     ┌──────────────────────┐
          (B-roll opcional)    | Imagens de apoio     |
                               | sobrepondo CENA 3    |
                               └──────────────────────┘

[TRACK A1] ┌──────┬────────┬──────────┬──────────────┐
           | VOZ  | VOZ    | VOZ      | VOZ           |
           └──────┴────────┴──────────┴──────────────┘

[TRACK A2] ┌──────────────────────────────────────────┐
           | TRILHA (80-90 BPM, instrumental calmo)    |
           └──────────────────────────────────────────┘

[TRACK T]                     ┌──────────────────────┐
          (Título/CTA)        | TELA FINAL           |
                               | (texto + logo)       |
                               └──────────────────────┘
```

---

## 🎬 SLOT A SLOT — Instruções

### SLOT 1: ABERTURA (0s → 5s)
| Configuração | Valor |
|-------------|-------|
| Duração | 5 segundos (00:00:00 → 00:00:05) |
| Transição entrada | Corte seco |
| Transição saída | Fade 0.3s |
| Efeito | Nenhum |

### SLOT 2: SERVIÇO (5s → 14s)
| Configuração | Valor |
|-------------|-------|
| Duração | 9 segundos (00:00:05 → 00:00:14) |
| Transição entrada | Fade 0.3s (herdado) |
| Transição saída | Slide 0.4s (direita pra esquerda) |
| Efeito | Zoom leve 105% (sutil, movimento lento) |

### SLOT 3: PACIENTE (14s → 22s)
| Configuração | Valor |
|-------------|-------|
| Duração | 8 segundos (00:00:14 → 00:00:22) |
| Transição entrada | Slide 0.4s (herdado) |
| Transição saída | Fade 0.3s |
| Efeito | Nenhum (realismo) |

### SLOT 4: CTA/FECHAMENTO (22s → 30s)
| Configuração | Valor |
|-------------|-------|
| Duração | 8 segundos (00:00:22 → 00:00:30) |
| Transição entrada | Fade 0.3s |
| Transição saída | Fade out 0.5s (fim do vídeo) |
| Efeito | Texto animado (fade in) + logo no canto |

---

## 🎵 TRILHA PADRÃO (Template B)

| Característica | Valor |
|---------------|-------|
| Gênero | Instrumental calmo |
| BPM | 80-90 |
| Volume | 40% (60% voz / 40% música) |
| Fade in | 0.5s no início |
| Fade out | 1s no final |

**Sugestão de busca:** "hopeful acoustic guitar" ou "calm piano background" em bibliotecas como Epidemic Sound, Artlist ou YouTube Audio Library.

---

## 🖼️ TELA FINAL (CTA)

Crie uma imagem PNG 1080×1920 com:

```
Fundo: Azul Claro (#0099CC)
┌────────────────────────────────┐
│                                │
│        📍 Povoado Serra        │
│       ✅ Entrega concluída     │
│                                │
│                                │
│    [ Logo Secretaria ]         │
│                                │
│  #SaúdeSãoSebastião            │
│                                │
└────────────────────────────────┘
```

**Fonte:** Montserrat Bold, branco
**Duração na tela:** 8 segundos (último slot)
**Animação:** Fade in (0.5s), estático até o fade out

---

## 🚀 PASSO A PASSO NO EDITOR

### No Premiere / DaVinci:
1. Crie sequência 1080×1920, 30fps
2. Importe os takes nas tracks de vídeo
3. Posicione cada take no slot correspondente
4. Aplique transições conforme tabela acima
5. Adicione trilha na track de áudio (volume 40%)
6. Ajuste sincronia da voz
7. Crie tela final (texto + logo) como PNG ou título
8. Renderize: H.264, 1080×1920, 30fps, AAC 128kbps

### No CapCut:
1. Novo projeto → 9:16 (1080×1920)
2. Adicione todos os clipes na timeline
3. Corte cada um na duração do slot
4. Transições → Fade / Slide (0.3-0.4s)
5. Áudio → Adicionar música → volume 40%
6. Texto → Adicionar tela final
7. Exportar → 1080p, 30fps

---

## ⚡ ATALHOS DE PRODUÇÃO EM LOTE

Se for produzir mais reels nos próximos dias:

1. **Salve este projeto como "TEMPLATE-MESTRE-B"**
2. Na próxima vez, abra o template, clique com botão direito nos clipes → **Replace Footage** (Premiere) ou substitua manualmente (CapCut)
3. Só troca os takes, ajusta cortes se necessário, renderiza
4. **5 reels em ~20 minutos** de edição

---

*Criado em 17/06/2026 por Lôh para Jadielson*
*Template: B — Personagem + Serviço (30s)*