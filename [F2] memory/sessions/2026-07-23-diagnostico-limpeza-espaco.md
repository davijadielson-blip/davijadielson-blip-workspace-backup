---
tema: sessão de diagnóstico e limpeza de disco
data: 2026-07-23
horario: 12:48 - 14:02 UTC
participantes: Lôh, Jadielson Davi
canal: openclaw-control-ui (webchat)
status: concluido
---

# Sessão — Diagnóstico e Limpeza de Disco (ENOSPC)

## Resumo

Jadielson reportou erro ENOSPC (no space left on device) no OpenClaw Managed. 
Diagnóstico revelou volume `/dev/sda1` de 10G em 100% de uso.

## Causa Raiz

Crescimento de <5G para 10G causado principalmente por:
- ~709 MB de vídeos da edição bastidores adicionados em 22/07
- ~700 MB no git history (vídeos commitados)
- Crescimento natural de sessões (~2G) e memória SQLite (~500 MB)
- Caches acumulados (Homebrew, NPM, Browser)

## Ações Realizadas

### 1. Limpeza de Caches (13:09 UTC)
- Homebrew cache antigo: 1.1G → 169M (-940 MB)
- NPM cache: 499M → 15M (-484 MB)
- Browser cache: 186M → 16M (-170 MB)
- Pip cache: 13M → 0
- Temp files

### 2. Limpeza de Não-.md (13:14 UTC)
- `edicao-bastidores/`: 709 MB (vídeos MP4, JPG, MP3) — deletado
- `.kit-import/`: 3 MB (starter kit duplicado) — deletado
- `__pycache__` / `.pyc` — deletado
- `evals.json` / screenshots — deletado

### 3. Remoção de Duplicatas [F2] (13:42 UTC)
- `[F2] vaults/`: 30 MB (mirror do workspace) — deletado
- `[F2] agentes/jarvis-workspace/`: 2.9 MB — deletado

### 4. Upload para Google Drive via GOG (13:49 UTC)
- 34 arquivos não-.md (27 MB) enviados para `OpenClaw-Cofre/` no Drive da empresa
- Subpastas: F1-5Frentes, F1-2-Literatura, F3-Projetos, F2-outputs
- Drive: https://drive.google.com/drive/folders/11B247NyZsKF5ctodbwM0iC9crCCWsw8q

### 5. Pendências do Doctor (13:26 UTC)
- 2 orphan transcripts arquivados em main/sessions
- Agente Clara movido para `_revisao_agentes/`

### 6. Reinicialização (13:23 UTC)
- Gateway reiniciado com sucesso (SIGUSR1)

### 7. Cron de Limpeza Diária (13:55 UTC)
- Job `limpeza-diaria-cache` configurado para 00:00 (America/Maceio)
- ID: eac72b16-9b61-4d5c-bd3c-d02e488fab2e

## Resultado

| Métrica | Antes | Depois |
|---|---|---|
| Uso do disco | 100% (8 MB livre) | 79% (2.2 GB livre) |
| Gateway | Falhando (ENOSPC) | Reiniciado e operacional |
| Zapier | Descontinuado | Removido |
| GOG Drive | — | Configurado com 3 contas |

## Decisões Registradas
- `[F2] memory/decisions/2026-07-23-diagnostico-espaco.md`
- `[F2] memory/decisions/2026-07-23-cron-limpeza-cache.md`

---

*Fonte: Cofre (sessão completa)*