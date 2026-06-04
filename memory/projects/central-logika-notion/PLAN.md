# Plano: Central LÓGIKA no Notion

> Criado em 2026-06-04. Status: execução.

## Objetivo

Transformar o Notion empresarial da LÓGIKA em uma estrutura operacional clara para Jadielson, Lôh, Jarvis e futuros subagentes, começando por uma central de navegação e protocolo de uso, sem excluir ou mover bases existentes nesta fase.

## Sucesso = critérios verificáveis

- [ ] Central LÓGIKA contém regra clara de uso para cada database acessível.
- [ ] Existe um Protocolo Jarvis v0.1 documentado.
- [ ] Existe rotina de triagem para Captura Geral.
- [ ] Campos mínimos empresariais estão definidos para padronização futura.
- [ ] Nenhuma database antiga foi excluída, arquivada ou movida sem revisão.
- [ ] Documento local e página Notion estão sincronizados em nível de decisão.

## Tarefas

### Fase 1: Fundação segura

- [x] **T1.1** — Conectar Notion via API e validar token.
  - Verificação: API respondeu como bot `Loh-bot`.
  - Estimativa: 15min.
  - Depende de: token Notion.

- [x] **T1.2** — Inventariar databases empresariais acessíveis.
  - Verificação: arquivo `notion-logika-inventory.json` criado com 7 databases.
  - Estimativa: 20min.
  - Depende de: T1.1.

- [x] **T1.3** — Criar diagnóstico inicial.
  - Verificação: arquivo `notion-logika-diagnostico.md` criado.
  - Estimativa: 20min.
  - Depende de: T1.2.

- [x] **T1.4** — Criar página rascunho da Central LÓGIKA no Notion.
  - Verificação: página criada e lida pela API.
  - Estimativa: 20min.
  - Depende de: T1.3.

### Fase 2: Protocolo operacional

- [x] **T2.1** — Criar Plano Executivo da Central LÓGIKA.
  - Verificação: este `PLAN.md` salvo em `memory/projects/central-logika-notion/PLAN.md`.
  - Estimativa: 20min.
  - Depende de: T1.4.

- [x] **T2.2** — Atualizar a Central LÓGIKA no Notion com versão 0.2.
  - Verificação: página contém seções “Regra de uso das databases”, “Protocolo Jarvis” e “Rotina de triagem”.
  - Estimativa: 30min.
  - Depende de: T2.1.

- [x] **T2.3** — Definir campos mínimos empresariais.
  - Verificação: campos mínimos documentados na Central e no workspace.
  - Estimativa: 20min.
  - Depende de: T2.2.

### Fase 3: Padronização futura

- [ ] **T3.1** — Auditar divergências entre calendários editoriais.
  - Verificação: relatório indicando diferenças entre Calendário Editorial, SINDSS e Câmara.
  - Estimativa: 45min.
  - Depende de: aprovação após Fase 2.

- [ ] **T3.2** — Propor modelo de Cliente/Frente.
  - Verificação: proposta dizendo se clientes devem ser propriedade, database separada ou página por frente.
  - Estimativa: 45min.
  - Depende de: T3.1.

- [ ] **T3.3** — Criar plano de consolidação sem perda.
  - Verificação: plano com “manter”, “fundir”, “arquivar futuramente”, “revisar com Jadielson”.
  - Estimativa: 1h.
  - Depende de: T3.2.

### Fase 4: Base mestre Produção & Agenda

- [x] **T4.1** — Criar database mestre “Produção & Agenda — LÓGIKA”.
  - Verificação: database criada e lida pela API.
  - Estimativa: 30min.
  - Depende de: decisão de Jadielson sobre unificação.

- [x] **T4.2** — Atualizar Central LÓGIKA com decisão v0.3.
  - Verificação: blocos de decisão v0.3 adicionados na Central.
  - Estimativa: 15min.
  - Depende de: T4.1.

- [x] **T4.4** — Simplificar schema da base mestre.
  - Verificação: `Data principal` e `Status produção` removidos; `Status geral` renomeado para `Status`.
  - Estimativa: 15min.
  - Depende de: revisão de Jadielson.

- [x] **T4.5** — Adicionar campo `Tipo de conteúdo`.
  - Verificação: propriedade multi_select criada com formatos como Reels, Stories, vídeo institucional e vídeo comercial.
  - Estimativa: 10min.
  - Depende de: revisão de Jadielson.

- [ ] **T4.3** — Planejar migração por amostra.
  - Verificação: plano de migração com 3 a 5 registros-teste antes de qualquer migração em massa.
  - Estimativa: 45min.
  - Depende de: T4.2.

## Dependências externas

- Permissão de escrita da integração Notion quando for necessário criar/editar páginas.
- Revisão de Jadielson antes de qualquer exclusão, arquivamento ou migração.
- Configuração futura do Jarvis e subagentes da LÓGIKA.

## Riscos

- **Bagunça estrutural aumentar se consolidar cedo demais** — mitigação: começar com central de navegação e protocolo, não migração.
- **Misturar pessoal e empresarial** — mitigação: Central LÓGIKA só para operação empresarial.
- **Agente acessar conteúdo sensível** — mitigação: só compartilhar com `Loh-bot` o que for operacional; páginas restritas ficam fora.
- **Campos duplicados ou inconsistentes** — mitigação: padronizar aos poucos, começando por campos mínimos.

## Estado atual

- Fundação Notion validada.
- Central LÓGIKA rascunho criada.
- Plano executivo criado e em execução.
- Central LÓGIKA v0.3 atualizada; database mestre Produção & Agenda — LÓGIKA criada e schema simplificado conforme revisão de Jadielson. Próximo: planejar migração por amostra antes de qualquer migração em massa.

---

*Atualizar este arquivo conforme execução. Não criar arquivo novo — versionar este.*
