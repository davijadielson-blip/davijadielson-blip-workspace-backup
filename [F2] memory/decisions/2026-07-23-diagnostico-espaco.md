---
tema: diagnóstico e limpeza de disco ENOSPC
data: 2026-07-23
decisao: limpeza de caches, temp files e não-.md do workspace
autor: Lôh
aprovado_por: Jadielson Davi
status: concluido
---

# Diagnóstico de Disco — ENOSPC (23/07/2026)

## Problema
OpenClaw Managed falhando com ENOSPC (no space left on device).

## Causa Raiz
Volume `/dev/sda1` (XFS de **10G**) em 100% de uso.  
O volume abriga `/data/`, `/tmp/`, `/home/linuxbrew/` — todos compartilhando os mesmos 10G.

## Crescimento Atípico — Investigação
Jadielson reportou que "até alguns dias atrás tava com menos de 5GB ocupados".

### Principais responsáveis pelo crescimento:

| Item | Tamanho | Quando | Natureza |
|---|---|---|---|
| **Edição bastidores (vídeos)** | ~709 MB | 22/07/2026 | Arquivos .mp4, .jpg, .mp3 commitados no workspace |
| **Git objects (vídeos)** | ~815 MB | 22/07/2026 | Histórico do git com os mesmos vídeos |
| **Sessões de agentes** | ~2.0 GB | Acumulativo | Crescimento normal (~50 MB/agente × 20+ agentes) |
| **Memory SQLite** | ~500 MB | Acumulativo | Indexação normal do sistema |
| **Homebrew cache** | ~1.1 GB | Acumulativo | Caches de download |
| **NPM cache** | ~499 MB | Acumulativo | Cache de pacotes |

**Conclusão:** O salto de <5G para 10G foi causado principalmente pelos **~1.4 GB de vídeos** da edição bastidores adicionados em 22/07 (709 MB em arquivos + ~700 MB no git), que somados ao crescimento natural do sistema (sessões + memória + caches) saturaram o volume de 10G.

## Limpeza Realizada (23/07/2026 — 13:09 UTC)

### 1ª rodada — Caches e temporários (autorizado "pode limpar")

| Item | Antes | Depois | Liberado |
|---|---|---|---|
| Homebrew cache antigo (+30d) | 1.1 GB | 169 MB | ~940 MB |
| NPM cache | 499 MB | 15 MB | ~484 MB |
| Browser cache | 186 MB | 16 MB | ~170 MB |
| Pip cache | 13 MB | 0 | ~13 MB |
| Temp files | — | limpos | ~0 |

### 2ª rodada — Não-.md do workspace (autorizado "pode teletar")

| Item | Tamanho | Status |
|---|---|---|
| edicao-bastidores/ (MP4, JPG, MP3, scripts) | 709 MB | ✅ Deletado |
| .kit-import/ (starter kit duplicado) | 3 MB | ✅ Deletado |
| __pycache__ / .pyc | 92 KB | ✅ Deletado |
| evals.json / screenshots duplicados | ~1 MB | ✅ Deletado |
| .trash/ | 4 KB | ✅ Deletado |

## Liberação Total

| Estado | Uso | Livre |
|---|---|---|
| Antes (100%) | 10.0 GB | ~8 MB |
| Após limpeza (79%) | 7.9 GB | ~2.2 GB |

## Pendências

1. **Git objects grandes (815 MB):** O histórico do git (/data/.openclaw/workspace/.git/objects/) contém os vídeos commitados. Para recuperar esse espaço, precisa de `git filter-branch` ou BFG Repo-Cleaner + `git gc --prune=now`. Requer análise de risco.
2. **Agente Clara:** Diretório existe em disco sem entry no agents.list — pode ser removido ou registrado.
3. **Orphan transcript:** 1 arquivo .jsonl órfão no main/sessions — doctor pode arquivar.

## Próximos Passos
- [ ] Rodar doctor e verificar alertas
- [ ] Reiniciar gateway OpenClaw
- [ ] Analisar se vale a pena limpar git history
- [ ] Monitorar crescimento do volume de 10G

---

*Fonte: Cofre (diagnóstico via exec, df, du, find)*