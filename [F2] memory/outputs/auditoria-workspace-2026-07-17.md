# Auditoria do Workspace — 17/07/2026

## Status Geral

| Item | Valor |
|---|---|
| **Workspace total** | **167 MB** |
| `.git/` (histórico essencial) | 83 MB |
| Sem `.git` | **84 MB** |
| Partição `/data` | **10 GB — 91% usado (9.1G / 1.0G livre)** |

⚠️ A partição `/data` está em 91% — o alerta procede. O workspace em si são 167 MB, mas o disco tem outros arquivos além do workspace.

---

## O que foi concluído na auditoria anterior (16/07)

**Antes: 272 MB → Depois: 166 MB (106 MB limpos ✅)**

### Removidos com segurança:
- ✅ 30+ JSONs de Notion (logs de processo)
- ✅ Duplicatas de [F2] vaults/ (PDFs, imagens, HTML, DOCX, XLSX, ZIPs) — ~55 MB
- ✅ Duplicata `F2-memory/` antiga — ~21 MB
- ✅ JSONs de auditoria do Drive — ~5 MB
- ✅ Comprovantes financeiros (imagens) — ~5 MB
- ✅ Outputs de texto de pesquisa do Documentário
- ✅ Backups antigos do archive
- ✅ Arquivo LLM grande (openclaw-llms-full.txt — 6 MB)

### Enviados para o Google Drive (9 PDFs via Zapier 3):
- Plano alimentar, OMEGA 3, PRÉ-TREINO, FRAPPUCINO, SHAKE PROTEICO, SMOOTHIE DE MORANGO
- Planejamento Alimentar Semanal
- Dados Laboratório São Sebastião
- SINDSS ID Visual

### ⚠️ Pendente da auditoria anterior (limite Zapier):
- 4 PDFs ainda no workspace: 300 GANCHOS, PACK PREMIERE PRO, SINDSS ID VISUAL, Estrutura base da secretaria

---

## Auditoria de hoje — O que ainda não é .md e deve ir para o Drive

### 🖼️ IMAGENS (25 MB no total — maior peso)

| Arquivo | Tamanho | Localização |
|---|---|---|
| image.jpg | 3.6 MB | Logika/LIVES |
| image 3.jpg | 3.3 MB | Saúde/Mídias |
| image 4.jpg | 2.9 MB | Saúde/Mídias |
| image.jpg | 2.9 MB | Saúde/Mídias |
| image 1.jpg | 2.5 MB | Saúde/Mídias |
| image 1.jpg | 2.5 MB | Logika/LIVES |
| Pasted image 20241108093800.jpg | 2.5 MB | Logika/LIVES |
| image 2.jpg | 2.5 MB | Logika/LIVES |
| image 2.jpg | 2.4 MB | Saúde/Mídias |
| recargapay_escola_eloah.jpg | 159 KB | Financeiro/tmp |
| 5 PNGs de screenshots (skills) | ~1 MB | skills/starter/ |

**Total imagens: ~25 MB → Mover para Drive**

### 📄 DOCUMENTOS BINÁRIOS (4 MB)

| Arquivo | Tamanho | Localização |
|---|---|---|
| Av360-Planilha-de-Custo-e-Orcamento.xlsx | 190 KB | Central Pessoal |
| MAPEAMENTO_E_CURADORIA_DAS_PERSONAGENS.xlsx | 10 KB | Documentário |
| Nome para meu Produto Digital.xlsx (2x) | 10 KB cada | Logika |
| BASE PADRÃO DE CTA/HEADLINE/GANCHOS.docx (3x) | ~22 KB cada | Saúde/Templates |
| O_FIO_DA_MEMORIA_PROPOSTA.docx | 22 KB | Documentário |
| CRONOGRAMA_DE_EXECUCAO.docx | 15 KB | Documentário |
| CHECKLIST_EXECUCAO_SEGURA.docx | 17 KB | Documentário |
| TERMO_AUTORIZACAO_IMAGEM.docx | 15 KB | Documentário |

**Total documentos: ~4 MB → Mover para Drive**

### 📦 ARQUIVOS COMPACTADOS (1.4 MB)

| Arquivo | Tamanho | Localização |
|---|---|---|
| starter-kit-openclaw-v2.5.7-2026-06-04.zip | 1.4 MB | archive/starter-kit-zips |

**→ Mover para Drive (já tem no GitHub)**

### 📝 ARQUIVOS .TXT QUE PODEM VIRAR .MD (89 KB)

| Arquivo | Tamanho | Localização |
|---|---|---|
| 03_ESTRATEGIA_E_SCRIPTS_ENTRE_TEMPOS.txt | 26 KB | Entre Tempos |
| habilidades-gestao-rotina-energia-alfred.txt | 13 KB | Central Pessoal |
| arvore-logika-*.txt (4 arquivos) | ~57 KB | logika-c-level-squad |

**→ Renomear para .md ou mover para Drive**

### 🎨 .CANVAS (Obsidian — 12 KB, pode ficar ou ir)

### ⚙️ ARQUIVOS OPERACIONAIS (FICAM)

| Categoria | Justificativa |
|---|---|
| `.py` (scripts) | Infraestrutura do agente |
| `.sh` (hooks) | Infraestrutura do agente |
| `.json` / `.json5` (configs) | Configuração operacional |
| `.toml` (codex agents) | Configuração de agentes |
| `.html` / `.css` (cockpit) | Dashboard do agente |
| `.env` | Variáveis de ambiente (secreto, fica) |
| `.gitkeep` | Placeholders de diretório |
| `.pyc` (cache) | Cache do Python |

---

## Resumo do que deve sair do workspace

| Categoria | Tamanho |
|---|---|
| 🖼️ Imagens (Logika + Saúde + skills) | ~25 MB |
| 📄 Documentos (xlsx, docx) | ~4 MB |
| 📦 ZIP (starter-kit) | ~1.4 MB |
| 📝 TXT → .md | ~89 KB |
| **Total movível para Drive** | **~31 MB** |

> Após mover, o workspace sem `.git` cai de **84 MB → ~53 MB**.
> O `.git` (83 MB) deve permanecer — é histórico essencial do versionamento.

---

## Próximos passos recomendados

1. **Mover imagens** (Logika LIVES + Saúde Mídias) para o Google Drive
2. **Mover documentos** (xlsx, docx) para o Google Drive
3. **Converter .txt relevantes** para .md ou mover para Drive
4. **Remover ZIP** do starter-kit (já está no GitHub)
5. **Limpar .git** com `git gc --aggressive` para reduzir 83 MB
6. **Verificar** outros diretórios fora do workspace na partição `/data` (pode ter mais lixo)

Fonte: Cofre (auditoria-workspace-2026-07-17.md), exec (find, du, df, stat)