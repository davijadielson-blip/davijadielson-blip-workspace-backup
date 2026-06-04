# Diagnóstico Notion — LÓGIKA / Operação Empresarial

Data: 2026-06-04
Responsável: Lôh
Escopo: somente páginas/databases compartilhadas com a integração `Loh-bot`.

## Princípios de segurança

- Não excluir nada nesta fase.
- Não mover conteúdo antigo sem revisão.
- Preferir centralizar por navegação, links e views antes de fundir databases.
- Usar o Notion aqui para a área empresarial/LÓGIKA, mantendo a parte pessoal separada.
- Agentes futuros devem ler este mapa antes de operar.

## Databases acessíveis hoje

### 1. Calendário Editorial
- ID: `1d8207e6-f145-8153-99c1-f5ae2b4e4e23`
- URL: https://app.notion.com/p/1d8207e6f145815399c1f5ae2b4e4e23
- Uso provável: calendário editorial principal, com campos também relacionados a eventos, setor, roteiro, criativo e publicação.
- Observação: há muitos registros sem título na amostra; isso reduz clareza operacional.
- Status encontrados na amostra: A INICIAR, PUBLICADO, ABORTADO.
- Recomendação: manter como base principal ou transformar em calendário editorial mestre, mas corrigir nomes/títulos futuramente.

### 2. 📥 Captura Geral
- ID: `242f2506-a972-451d-8020-9bd593bdb006`
- URL: https://app.notion.com/p/242f2506a972451d80209bd593bdb006
- Uso provável: entrada rápida de tarefas, compromissos, capturas e ideias vindas de Telegram/Claude.
- Pontos fortes: tem Frente, Tipo, Status, Data e Origem.
- Recomendação: manter como inbox operacional. Tudo que chegar sem destino claro entra aqui e depois é triado.

### 3. Agenda de Eventos — Secretaria Municipal de Saúde
- ID: `30d207e6-f145-809d-838a-cdf7bb477adf`
- URL: https://app.notion.com/p/30d207e6f145809d838acdf7bb477adf
- Uso provável: agenda específica de eventos/coberturas da Saúde.
- Pontos fortes: campos de prioridade, setor, presença de prefeito/secretário, materiais, coordenador e status.
- Recomendação: manter especializada; não fundir agora com calendário editorial.

### 4. 📆 Calendário Editorial SINDSS
- ID: `5ca1a34c-342b-406a-8c71-4b8b63e0a1f5`
- URL: https://app.notion.com/p/5ca1a34c342b406a8c714b8b63e0a1f5
- Uso provável: calendário por cliente/frente.
- Amostra atual: 0 registros retornados.
- Recomendação: manter como frente específica ou avaliar se deve virar view filtrada de um calendário mestre.

### 5. 📆 Calendário Editorial Câmara
- ID: `52a83dbb-9d10-40b6-87c3-687013d92138`
- URL: https://app.notion.com/p/52a83dbb9d1040b687c3687013d92138
- Uso provável: calendário por cliente/frente.
- Amostra atual: 0 registros retornados.
- Recomendação: manter como frente específica ou avaliar se deve virar view filtrada de um calendário mestre.

### 6. 🚀 Cockpit Diretor
- ID: `e6d0b774-ebe0-4761-a61b-1a30e16db091`
- URL: https://app.notion.com/p/e6d0b774ebe04761a61b1a30e16db091
- Uso provável: gestão pessoal/produtiva do diretor dentro da operação.
- Amostra atual: 0 registros retornados.
- Recomendação: usar como painel de foco semanal ou migrar a função para a Central LÓGIKA.

### 7. Ideias
- ID: `312207e6-f145-8126-9ed5-d5c4cbce1b7f`
- URL: https://app.notion.com/p/312207e6f14581269ed5d5c4cbce1b7f
- Uso provável: banco de ideias, pautas e temas.
- Recomendação: manter como banco de ideias; relacionar ou referenciar com calendário editorial futuramente.

## Diagnóstico geral

O Notion empresarial já tem boas bases, mas está dividido por uso/frente de forma parcialmente redundante.

Há três problemas principais:

1. **Fragmentação**
   - Existem calendários por frente e um calendário geral.
   - Ainda não está claro se cada cliente deve ter database própria ou se todos devem virar views de uma base mestre.

2. **Entrada e triagem**
   - A Captura Geral é uma boa inbox, mas precisa de rotina: capturar → triar → virar projeto/evento/post/tarefa.

3. **Navegação para agentes**
   - Os agentes futuros precisam de um mapa simples: onde olhar, o que podem tocar, o que não devem alterar.

## Arquitetura recomendada — versão leve

Criar uma página central chamada:

> Central LÓGIKA — Mapa Operacional

Ela deve funcionar como índice e instrução operacional para humanos e agentes.

### Seções da Central

1. **Entrada rápida / Inbox**
   - Link: 📥 Captura Geral
   - Regra: tudo que chega bruto entra aqui.

2. **Produção editorial**
   - Link: Calendário Editorial
   - Links auxiliares: SINDSS e Câmara
   - Regra: posts, roteiros, criativos, publicação e avaliação.

3. **Eventos e coberturas**
   - Link: Agenda de Eventos — Saúde
   - Regra: eventos, datas, local, necessidade de cobertura e materiais.

4. **Ideias e pautas**
   - Link: Ideias
   - Regra: ideias ainda não compromissadas.

5. **Gestão / foco do diretor**
   - Link: Cockpit Diretor
   - Regra: tarefas estratégicas, foco semanal, blocos de trabalho.

6. **Instruções para agentes**
   - Lôh: coordenação macro, memória, segurança, integração entre canais e arquitetura.
   - Jarvis: coordenador local da LÓGIKA; triagem empresarial, clientes, projetos, produção, prioridades e encaminhamento para especialistas.
   - Subagentes: executar tarefas específicas conforme permissão.

## Decisão recomendada agora

Não consolidar tudo em uma única database ainda.

Fazer em 3 fases:

### Fase 1 — Central de navegação
- Criar a Central LÓGIKA.
- Linkar as bases existentes.
- Documentar regra de uso de cada base.

### Fase 2 — Padronização
- Padronizar nomes de propriedades principais.
- Definir campos mínimos por tipo de trabalho:
  - Cliente/Frente
  - Status
  - Prazo/Data
  - Responsável
  - Tipo de entrega
  - Link de arquivos
  - Observações/briefing

### Fase 3 — Consolidação futura
- Decidir se SINDSS e Câmara continuam como databases separadas ou viram views filtradas de uma base mestre.
- Arquivar bases vazias se ficarem sem uso.
- Nunca deletar sem backup e revisão.

## Próxima ação sugerida

Criar no Notion uma página-rascunho da Central LÓGIKA com os links principais e instruções para agentes.

