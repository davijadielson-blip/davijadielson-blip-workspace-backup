## Miro — Exclusivo para Projetos (Jack) — 18/07/2026

### Decisão
O Miro é **exclusivo** para o **Grupo PROJETOS** ([F3]). Apenas o **Jack Lemley** (coordenador de projetos) e seus tópicos devem usar a integração.

### Configuração
- **Board:** "MAPA MENTAL GERAL" (ID: `uXjVJI0-H6E=`)
- **Responsável:** Jack Lemley
- **Escopo:** Projetos em [F3] PROJETOS/
- **Script:** `scripts/miro.py` — uso restrito ao Jack

### Instruções para o Jack
1. Usar o board do Miro como canvas visual para planejamento de projetos
2. Criar cards com decisões, marcos, entregas e cronogramas dos projetos
3. Manter os mapas mentais organizados por projeto
4. Sincronizar com o Cofre ([F3] PROJETOS/) quando houver mudanças visuais relevantes
5. Não compartilhar o token de acesso fora do escopo de projetos

### Uso pelo Jack
```bash
# Adicionar card de decisão de projeto
python3 scripts/miro.py add-decision "Projeto X" "Decisão" "Descrição"

# Adicionar card de sistema/marco
python3 scripts/miro.py add-system "Projeto X" "Marco" "Descrição"
```

Fonte: Cofre (memory/2026-07-18.md), decisão de Jadielson