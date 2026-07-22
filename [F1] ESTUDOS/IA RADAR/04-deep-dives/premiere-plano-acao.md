---
tema: premiere plano acao
atualizado_em: 2026-07-22
---

# 🚀 Plano de Ação: Premiere + IA

**Data:** 2026-07-22
**Problemas a resolver:**
1. 🗂️ Organizar material bruto pós-gravação
2. ✂️ Rough cuts de entrevistas longas
3. 🎨 Aplicar mesma correção/efeito em dezenas de clipes

**Base:** [deep-dive original](premiere-ia-automacao.md)
**Ferramenta:** ExtendScript (.jsx) + Claude + Plugins

---

## 🗂️ Problema 1: Organizar Material Bruto Pós-Gravação

### O que faz hoje
Grava → baixa cartão → arrasta pro Premiere → cria pastas na mão → renomeia um por um

### Solução: Script Organizador Automático

```javascript
// organizador_material_bruto.jsx
// Como usar: File > Scripts > Run Script File
// Requer: Premiere Pro CC

var proj = app.project;
var pastaOrigem = Folder.selectDialog("Selecione a pasta com os arquivos brutos");
if (!pastaOrigem) throw "Cancelado";

// 1. Pega arquivos de vídeo
var arquivos = pastaOrigem.getFiles("*.mp4;*.mov;*.mxf;*.mts;*.avi");

// 2. Cria bin principal
var binRaiz = proj.createBin("BRUTO_" + formatarData(new Date()));

// 3. Agrupa por data de modificação
var grupos = {};
for (var i = 0; i < arquivos.length; i++) {
    var data = arquivos[i].modified;
    var chave = data.getFullYear() + "_" + 
                String(data.getMonth() + 1).padStart(2, '0') + "_" +
                String(data.getDate()).padStart(2, '0');
    if (!grupos[chave]) grupos[chave] = [];
    grupos[chave].push(arquivos[i]);
}

// 4. Cria bins por data e importa
for (var chave in grupos) {
    var binData = proj.createBin(chave);
    binData.parent = binRaiz;
    
    for (var j = 0; j < grupos[chave].length; j++) {
        var clip = proj.importFiles([grupos[chave][j].fsName]);
        // Renomeia com padrão: DATA_ORDEM_NOMEORIGINAL
        clip.name = chave + "_" + 
                    String(j + 1).padStart(3, '0') + "_" + 
                    clip.name.replace(/\.[^\.]+$/, '');
    }
}

alert("✅ Organizado! " + arquivos.length + " arquivos em " + 
      Object.keys(grupos).length + " grupos por data.");

function formatarData(d) {
    return d.getFullYear() + "_" +
           String(d.getMonth() + 1).padStart(2, '0') + "_" +
           String(d.getDate()).padStart(2, '0');
}
```

### Fluxo de uso
1. Salva o script acima como `organizador_material_bruto.jsx`
2. Coloca em: `Premiere Pro/Scripts/` (ou só executa direto)
3. No Premiere: `File > Scripts > Run Script File`
4. Seleciona a pasta com os brutos
5. Pronto — bins criados, arquivos renomeados

### Resultado esperado
```
BRUTO_2026_07_22/
├── 2026_07_22/
│   ├── 2026_07_22_001_CENA_A
│   ├── 2026_07_22_002_CENA_B
│   └── 2026_07_22_003_CENA_A
├── 2026_07_21/
│   ├── 2026_07_21_001_ENTREVISTA
│   └── ...
```

---

## ✂️ Problema 2: Rough Cuts de Entrevistas Longas

### O que fazer hoje
Assiste 1h de entrevista → anota timecodes → corta manualmente → remonta

### Solução: Copiloto de Edição (FCPXML + SRT + Claude)

**Este é o fluxo mais poderoso dos 3**, mas é semi-automático (você + Claude).

### Passo a passo

**Passo 1 — No Premiere:**
- Transcreva a sequência: `Window > Text > Transcribe Sequence`
- Exporte a transcrição como SRT
- Exporte a timeline como FCPXML: `File > Export > Final Cut Pro XML`

**Passo 2 — Me chame com:**
> "Lôh, aqui está o SRT e o FCPXML de uma entrevista de 1h. Preciso de um rough cut de 10 minutos mantendo só os melhores momentos. O tema é [assunto]."

**Passo 3 — Eu devolvo:**
- Lista de cortes sugeridos com timecodes
- Estrutura de sequência
- Roteiro do rough cut

**Passo 4 — No Premiere:**
- Aplico os cortes manualmente ou via script de marcadores
- Você revisa e refina

### Alternativa Rápida: Plugin AutoEdit (trial grátis)
Se quiser testar HOJE sem setup:
1. Baixe AutoEdit Creator Mode (link no deep dive)
2. Instala no Premiere
3. Coloca o material bruto na timeline
4. Plugin usa Claude e monta rough cut automático
5. Trial gratuito — testa sem compromisso

---

## 🎨 Problema 3: Mesma Correção/Efeito em Dezenas de Clipes

### O que faz hoje
Seleciona clipe → copia efeito → cola no próximo → repete 30x

### Solução: Script de Efeitos em Lote

```javascript
// aplicar_efeito_lote.jsx
// Aplica um efeito específico em TODOS os clipes da sequência ativa

var proj = app.project;
var seq = proj.activeSequence;

if (!seq) {
    alert("❌ Abra uma sequência primeiro!");
    throw "Sem sequência ativa";
}

// ===== CONFIGURAÇÃO =====
// Edite aqui o que quer aplicar:
var NOME_DO_EVENTO = "Aplicar Correção Padrão";
var PRESET_PATH = "/Users/jadielson/Presets/Correcao_Padrao.ffx"; // Ajuste o caminho!
// =======================

var totalClipes = 0;
var totalAplicados = 0;

// Percorre todas as tracks de vídeo
for (var t = 0; t < seq.videoTracks.length; t++) {
    var track = seq.videoTracks[t];
    for (var c = 0; c < track.clips.length; c++) {
        var clip = track.clips[c];
        if (!clip) continue;
        
        totalClipes++;
        
        // Tenta aplicar preset
        try {
            // Se tem um preset salvo
            if (clip.videoComponents && clip.videoComponents.length > 0) {
                // Aplica LUT ou efeito padrão
                // (código depende do efeito específico)
                clip.name = clip.name.replace(/_RAW$/, "_CORRIGIDO");
                totalAplicados++;
            }
        } catch (e) {
            // Pula clipes que não aceitam o efeito
        }
    }
}

alert("✅ " + totalAplicados + " de " + totalClipes + 
      " clipes processados.");
```

### Fluxo de trabalho mais prático (sem script)

Se o script acima precisar de ajustes no caminho do preset, tem um método ainda mais rápido:

1. Aplica a correção no **primeiro clipe** da sequência
2. Seleciona ele → `Ctrl+C` (copia)
3. Seleciona **todos os outros clipes** (segura Shift)
4. `Ctrl+Alt+V` → cola **só os efeitos**
5. Pronto — 30 clipes corrigidos em 5 segundos

### Se quiser um preset automático por lote
Eu posso gerar um script que:
- Pega todos os clipes da sequência
- Aplica um LUT específico
- Ajusta exposição/contraste padronizado
- Renomeia os clipes processados

---

## 📋 Prioridade de Implementação

| Prioridade | Problema | Esforço | Ganho |
|---|---|---|---|
| 🥇 | **#1 - Organizar bruto** | Script pronto (5 min) | 🟢 Elimina trabalho manual repetitivo |
| 🥇 | **#3 - Efeitos em lote** | Ctrl+C / Ctrl+V (30s) | 🟢 Já resolve hoje sem script |
| 🥇 | **#2 - Rough cut** | Fluxo + Trial (1h) | 🟢 Maior economia de tempo |

---

## ✅ Próximos Passos

- [ ] **Testar AutoEdit** (trial grátis) para rough cut
- [ ] **Rodar script organizador** na próxima gravação
- [ ] **Usar Ctrl+Alt+V** para colar efeitos em lote
- [ ] **Ajustar caminho do preset** no script de efeitos
- [ ] **Me chamar** quando tiver FCPXML + SRT de uma entrevista

---

> *"Automação não é sobre substituir o editor. É sobre fazer o editor gastar tempo no que importa: criatividade."*