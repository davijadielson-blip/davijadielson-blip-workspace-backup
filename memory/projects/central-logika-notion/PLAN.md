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

- [x] **T4.6** — Adicionar campo `Link de origem`.
  - Verificação: propriedade URL criada para rastrear item/página original.
  - Estimativa: 10min.
  - Depende de: revisão de Jadielson.

- [x] **T4.3** — Planejar migração por amostra e executar amostra inicial.
  - Verificação: 4 registros-teste criados e verificados na base mestre antes de qualquer migração em massa.
  - Estimativa: 45min.
  - Depende de: T4.2.

- [x] **T4.7** — Consolidar regra de entrada única pela Inbox.
  - Verificação: Central LÓGIKA atualizada com decisão v0.4; regra `Inbox / Captura Geral → triagem → destino adequado` documentada.
  - Estimativa: 10min.
  - Depende de: decisão de Jadielson.

### Fase 5: Inbox oficial e rotina Jarvis

- [x] **T5.1** — Criar nova database `Inbox / Captura Geral — LÓGIKA`.
  - Verificação: database criada e lida pela API.
  - Estimativa: 20min.
  - Depende de: decisão de Jadielson.

- [x] **T5.2** — Arquivar antiga Captura Geral de teste.
  - Verificação: database antiga marcada como `archived: true` via API.
  - Estimativa: 10min.
  - Depende de: T5.1 e autorização de Jadielson.

- [x] **T5.3** — Atualizar Central LÓGIKA com Inbox oficial.
  - Verificação: Central recebeu seção v0.5 com link da nova Inbox e rotina Jarvis.
  - Estimativa: 10min.
  - Depende de: T5.2.

- [x] **T5.4** — Agendar revisão diária da Inbox.
  - Verificação: cron `jarvis-revisao-inbox-logika-seg-sab` ajustado para segunda a sábado às 17:00 America/Maceio.
  - Estimativa: 10min.
  - Depende de: T5.3.

- [x] **T5.5** — Ajustar rotina Jarvis para 17h.
  - Verificação: cron atualizado para `0 17 * * 1-6` em `America/Maceio`.
  - Estimativa: 5min.
  - Depende de: decisão de Jadielson.

### Fase 6: Teste de Inbox e views

- [x] **T6.1** — Criar entradas de teste na Inbox.
  - Verificação: 3 páginas `[TESTE]` criadas na Inbox e retornadas por query da rotina.
  - Estimativa: 15min.
  - Depende de: Inbox oficial.

- [x] **T6.2** — Criar views operacionais.
  - Verificação: 6 views criadas via Notion API: 4 na Inbox e 2 na Produção & Agenda.
  - Estimativa: 20min.
  - Depende de: databases oficiais.

- [x] **T6.3** — Atualizar Central LÓGIKA com views/teste.
  - Verificação: Central recebeu seção v0.6 com lista de views e resultado do teste.
  - Estimativa: 10min.
  - Depende de: T6.1 e T6.2.

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
- Central LÓGIKA v0.3 atualizada; database mestre Produção & Agenda — LÓGIKA criada e schema simplificado. Migração por amostra executada com 4 registros. Regra de entrada definida: tudo novo entra primeiro na nova Inbox / Captura Geral — LÓGIKA e depois é triado. Antiga Captura Geral foi arquivada. Rotina Jarvis ajustada para segunda a sábado às 17:00. Inbox testada com 3 entradas; views operacionais criadas. Definição completa da Secretária — Agenda e Execução ficará para depois das próximas integrações.

---

*Atualizar este arquivo conforme execução. Não criar arquivo novo — versionar este.*

## Nota arquitetural — Secretária Agenda e Execução

Jadielson corrigiu que a “Secretária — Agenda e Execução” não deve ser entendida como pessoa/agente que apenas alimenta a Inbox do Notion. Ela será uma camada operacional diária mais ampla, responsável por organizar o que Jadielson terá naquele dia ou nos próximos dias, usando várias integrações futuras: Google Agenda, Trello, e-mail, WhatsApp, Notion etc.

Neste plano, a Inbox / Captura Geral — LÓGIKA permanece como entrada do Notion, mas não representa todo o escopo da Secretária.
