---
tema: lições aprendidas e falhas operacionais
conteudo: registro de falhas onde o Cofre não foi consultado primeiro, com causa e correção
nicho: ecossistema agêntico Lôh/Jadielson
setor: operações agentivas
cliente: Jadielson Davi
tipo: log
prioridade: alta
atualizado_em: 2026-07-22
usar_quando: revisão de falhas, aprendizado contínuo, melhoria de procedimentos
nao_usar_quando: informação operacional normal
---

# 📓 Lições Aprendidas — Falhas Operacionais

> Registro de incidentes onde o Cofre não foi consultado primeiro.
> Cada entrada = 1 falha, com causa, consequência e correção.

## 2026-07-22 — Criação do protocolo LOCAL-FIRST

- **Incidente:** N/A (protocolo criado preventivamente)
- **Causa:** Respostas genéricas sem lastro no Cofre em sessões anteriores
- **Correção:** Protocolo LOCAL-FIRST documentado em `AGENTS.md`, `MAPA.md` e `checklists/local-first.md`
- **Ação preventiva:** Todo agente deve consultar o Cofre primeiro; falha = registro aqui

---

*Criado em 2026-07-22 · Adicionar novas entradas no topo.*