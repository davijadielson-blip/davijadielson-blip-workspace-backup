---
tema: lições aprendidas e falhas operacionais
conteudo: registro de falhas onde o Cofre não foi consultado primeiro, com causa e correção
nicho: ecossistema agêntico Lôh/Jadielson
setor: operações agentivas
cliente: Jadielson Davi
tipo: log
prioridade: alta
atualizado_em: 2026-07-30
usar_quando: revisão de falhas, aprendizado contínuo, melhoria de procedimentos
nao_usar_quando: informação operacional normal
---

# 📓 Lições Aprendidas — Falhas Operacionais

> Registro de incidentes onde o Cofre não foi consultado primeiro, erros operacionais e aprendizados técnicos para o ecossistema.

## 2026-07-30 — [Operacional] Alucinação por memória técnica contraditória de modelo

- **Incidente:** Jadielson relatou que agentes estavam alucinando e pediu novo checape dos sistemas.
- **Causa provável encontrada:** o Cofre preservava registros históricos conflitantes sobre o modelo primário (`openai-codex/gpt-5.5` antigo vs `openai/gpt-5.5` atual). A configuração ativa estava correta, mas agentes que leem memórias antigas poderiam tratar instruções superadas como vigentes.
- **Correção aplicada:** `MEMORY.md` foi atualizado para marcar a política antiga como histórica e registrar `openai/gpt-5.5` como ID técnico canônico atual.
- **Ação preventiva:** se um agente mostrar `Model Fallback: openrouter/...`, investigar como incidente, pois indica saída do modelo primário atual.

---

## 2026-07-28 — [Troubleshooting] Crache do Premiere com fotos JPG específicas / Alternativa via conversão de mídia

- **Incidente:** Travamento completo do Premiere (normal e beta) e Made in Code durante renderização de projeto contendo duas fotografias específicas.
- **Causa:** Fotos em formato JPG corrompidas ou com espaço de cores ou perfis ICC complexos (ex: RGB de 16/32 bits, perfis proprietários de celulares ou câmeras específicas, compressão progressiva não-padrão) que causam vazamento de memória e travamento no decodificador de imagem nativo do Mercury Render Engine do Adobe Premiere.
- **Tentativas malsucedidas:** Reduzir qualidade no Lightroom e exportar novamente em JPG (permaneceu travando devido à retenção dos metadados/perfis idênticos ou limitação na decodificação de imagem estática do Premiere sob aceleração por GPU).
- **Correção/Workflow de sucesso:** Levar as duas fotos para o CapCut, adicioná-las na timeline, renderizar em formato de vídeo (ex: MP4/H.264), carregar esse arquivo de vídeo gerado na timeline do Premiere e fazer a renderização do projeto principal (que agora funciona perfeitamente, inclusive em 4K).
- **Instruções futuras para o Suporte Técnico (cto):** 
  1. Em caso de travamento de render (crash no Premiere/Media Encoder), desativar aceleração de hardware nas configurações para isolar se é render de GPU.
  2. Isolar elementos de mídia na timeline (especialmente fotos estáticas de altíssima resolução).
  3. Aplicar o workflow de **"Conversão de Imagem Estática para Vídeo"** (via CapCut ou similar) antes de trazer para a timeline do Premiere quando o Lightroom falhar em re-encodar as fotos.

---

## 2026-07-22 — Criação do protocolo LOCAL-FIRST

- **Incidente:** N/A (protocolo criado preventivamente)
- **Causa:** Respostas genéricas sem lastro no Cofre em sessões anteriores
- **Correção:** Protocolo LOCAL-FIRST documentado em `AGENTS.md`, `MAPA.md` e `checklists/local-first.md`
- **Ação preventiva:** Todo agente deve consultar o Cofre primeiro; falha = registro aqui

---

*Criado em 2026-07-22 · Adicionar novas entradas no topo.*
