#!/usr/bin/env bash
# Reorganização do workspace: elimina diretórios duplicados/paralelos,
# consolidando conteúdo nos locais canônicos.
# Uso: bash scripts/reorganizar-workspace.sh  (roda em dry-run com -n)
set -euo pipefail
DRY="${1:--x}"
if [ "$DRY" = "-n" ]; then DRY=echo; else DRY=""; fi

cd /data/.openclaw/workspace

echo "=== Reorganização do workspace ==="
echo ""

move_merge() {
  local src="$1" dst="$2"
  if [ ! -e "$src" ]; then echo "  [skip] $src não existe"; return 0; fi
  if [ ! -d "$src" ]; then echo "  [skip] $src não é diretório"; return 0; fi
  # Cria destino
  $DRY mkdir -p "$dst"
  # Conta arquivos antes
  local count_src
  count_src=$(find "$src" -maxdepth 3 -type f | wc -l)
  if [ "$count_src" -eq 0 ]; then
    echo "  [vazio] $src está vazio -> removendo"
    $DRY git rm -rf "$src" 2>/dev/null || $DRY rm -rf "$src"
    return 0
  fi
  # Move conteúdo com rsync para preservar estrutura e sobrescrever conflitos
  echo "  [merge] $src ($count_src arquivos) -> $dst"
  if [ "$count_src" -gt 0 ]; then
    # git mv cada arquivo individualmente
    find "$src" -type f | while read -r f; do
      rel="${f#$src/}"
      target="$dst/$rel"
      mkdir -p "$(dirname "$target")"
      if [ -f "$target" ]; then
        # Se já existe no destino, verifica se é diferente
        if ! diff -q "$f" "$target" >/dev/null 2>&1; then
          # Conflito: preserva ambos
          base="${rel%.*}"
          ext="${rel##*.}"
          if [ "$ext" = "$rel" ]; then ext=""; else ext=".$ext"; fi
          echo "    conflito: $rel -> preservando como ${base}-do-overlap${ext}"
          $DRY cp "$f" "$(dirname "$target")/${base}-do-overlap${ext}"
        fi
      else
        $DRY cp "$f" "$target"
      fi
      $DRY git rm -f "$f" 2>/dev/null || $DRY rm -f "$f"
    done
  fi
  # Remove diretório fonte se vazio
  if [ -d "$src" ]; then
    local remaining
    remaining=$(find "$src" -maxdepth 3 -type f 2>/dev/null | wc -l)
    if [ "$remaining" -eq 0 ]; then
      $DRY rm -rf "$src" 2>/dev/null || true
    fi
  fi
}

# ============================================================
# MERGE 1: memory/ (raiz) → [F2] memory/ (canônico)
# ============================================================
echo ""
echo "--- 1. memory/ → [F2] memory/ ---"
move_merge "memory" "F2 memory"

# ============================================================
# MERGE 2: entregaveis/ → [F2] memory/outputs/
# ============================================================
echo ""
echo "--- 2. entregaveis/ → [F2] memory/outputs/ ---"
move_merge "entregaveis" "F2 memory/outputs"

# ============================================================
# MERGE 3: reports/ → [F2] memory/outputs/reports/
# ============================================================
echo ""
echo "--- 3. reports/ → [F2] memory/outputs/reports/ ---"
move_merge "reports" "F2 memory/outputs/reports"

# ============================================================
# MERGE 4: templates/ (raiz) → [F2] memory/templates/
# ============================================================
echo ""
echo "--- 4. templates/ → [F2] memory/templates/ ---"
move_merge "templates" "F2 memory/templates"

# ============================================================
# MERGE 5: contextos/ → [F2] memory/context/
# ============================================================
echo ""
echo "--- 5. contextos/ → [F2] memory/context/ ---"
move_merge "contextos" "F2 memory/context"

# ============================================================
# MERGE 6: calendarios/ → [F2] memory/context/calendarios/
# ============================================================
echo ""
echo "--- 6. calendarios/ → [F2] memory/context/calendarios/ ---"
move_merge "calendarios" "F2 memory/context/calendarios"

# ============================================================
# MERGE 7: content/drafts/ → [F2] memory/outputs/drafts/
# ============================================================
echo ""
echo "--- 7. content/ → [F2] memory/outputs/ ---"
move_merge "content" "F2 memory/outputs"

# ============================================================
# MERGE 8: pesquisa/ → [F2] memory/projects/pesquisa/
# ============================================================
echo ""
echo "--- 8. pesquisa/ → [F2] memory/projects/pesquisa/ ---"
move_merge "pesquisa" "F2 memory/projects/pesquisa"

# ============================================================
# MERGE 9: projetos/ (raiz) → [F1] PROJETOS/
# ============================================================
echo ""
echo "--- 9. projetos/ → [F1] PROJETOS/ ---"
move_merge "projetos" "F1 PROJETOS"

# ============================================================
# MERGE 10: producao/ → [F1] 5-Frentes/Logika-Creative/producao/
# ============================================================
echo ""
echo "--- 10. producao/ → [F1] 5-Frentes/Logika-Creative/producao/ ---"
# producao pode estar vazia, verificar
move_merge "producao" "F1 5-Frentes/Logika-Creative/producao"

# ============================================================
# MERGE 11: notion-configs/ → scripts/notion/configs/
# ============================================================
echo ""
echo "--- 11. notion-configs/ → scripts/notion/configs/ ---"
move_merge "notion-configs" "scripts/notion/configs"

# ============================================================
# MERGE 12: config-patches/ → scripts/patches/
# ============================================================
echo ""
echo "--- 12. config-patches/ → scripts/patches/ ---"
move_merge "config-patches" "scripts/patches"

# ============================================================
# MERGE 13: Anexos/ → [F1] 1-Permanentes/Anexos/
# ============================================================
echo ""
echo "--- 13. Anexos/ → [F1] 1-Permanentes/Anexos/ ---"
move_merge "Anexos" "F1 1-Permanentes/Anexos"

# ============================================================
# MERGE 14: exemplos/ → archive/exemplos/
# ============================================================
echo ""
echo "--- 14. exemplos/ → archive/exemplos/ ---"
move_merge "exemplos" "archive/exemplos"

# ============================================================
# MERGE 15: _curso/ → archive/_curso/
# ============================================================
echo ""
echo "--- 15. _curso/ → archive/_curso/ ---"
move_merge "_curso" "archive/_curso"

# ============================================================
# MERGE 16: backups/ → archive/backups/
# ============================================================
echo ""
echo "--- 16. backups/ → archive/backups/ ---"
move_merge "backups" "archive/backups"

# ============================================================
# MERGE 17: agentes/entregaveis/ → [F2] memory/outputs/
# ============================================================
echo ""
echo "--- 17. agentes/entregaveis/ → [F2] memory/outputs/ ---"
move_merge "agentes/entregaveis" "F2 memory/outputs"

echo ""
echo "=== Reorganização concluída ==="
