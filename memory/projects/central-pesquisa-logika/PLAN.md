# Plano: Central de Pesquisa LÓGIKA

> Criado em 2026-06-05. Status: planejamento.

## Objetivo

Implantar uma Central de Pesquisa LÓGIKA que reúna fontes internas, referências criativas, dados públicos, contexto de clientes, métricas e pesquisa web para tornar as respostas da Lôh/Jarvis/Clara mais ricas, específicas e acionáveis.

## Sucesso =

- [ ] Existe um mapa operacional salvo no workspace.
- [ ] Existe uma database/pasta central definida para capturas de pesquisa.
- [ ] As fontes são classificadas por tipo e destino: Notion, Drive, Vault ou GitHub.
- [ ] Pelo menos 20 referências iniciais foram cadastradas com link, anotação e tags.
- [ ] Tavily teve decisão tomada: ativar agora, ativar depois ou manter desativado.
- [ ] Clara/Jarvis sabem como consultar a central antes de pesquisas estratégicas.

## Tarefas

### Fase 1: Estrutura mínima

- [ ] **T1.1** — Criar database Notion `Central de Pesquisa — LÓGIKA`.
  - Verificação: database acessível pela integração Notion.
  - Estimativa: 30min.
  - Depende de: autorização de criação no Notion.

- [ ] **T1.2** — Criar pasta Google Drive `LÓGIKA / Central de Pesquisa`.
  - Verificação: pasta aparece no inventário Drive da LÓGIKA.
  - Estimativa: 15min.
  - Depende de: confirmação para criar pasta no Drive.

- [ ] **T1.3** — Definir campos/tags padrão.
  - Verificação: campos documentados na database e neste plano.
  - Estimativa: 30min.
  - Depende de: T1.1.

### Fase 2: Migração inicial

- [ ] **T2.1** — Triar pastas vindas do OneDrive por destino.
  - Verificação: lista de pastas com destino recomendado: Drive, Notion, Vault ou GitHub.
  - Estimativa: 1-2h.
  - Depende de: Jadielson disponibilizar pastas/links/arquivos.

- [ ] **T2.2** — Cadastrar 20-50 referências iniciais.
  - Verificação: referências com link, fonte, tipo, tags e nota de uso.
  - Estimativa: 1-2h.
  - Depende de: T1.1.

- [ ] **T2.3** — Organizar dados públicos prioritários.
  - Verificação: lista de fontes oficiais para Saúde, município, Câmara e clientes institucionais.
  - Estimativa: 1h.
  - Depende de: nenhuma.

### Fase 3: Métricas e redes

- [ ] **T3.1** — Criar planilha de performance manual das redes.
  - Verificação: Sheets com colunas de data, plataforma, formato, tema, métricas e observação.
  - Estimativa: 45min.
  - Depende de: autorização para criar Sheet.

- [ ] **T3.2** — Subir/exportar primeiros relatórios de Instagram/Meta/YouTube/TikTok.
  - Verificação: arquivos ou dados cadastrados na central.
  - Estimativa: 1-2h.
  - Depende de: acesso às contas ou exports manuais.

- [ ] **T3.3** — Avaliar APIs oficiais das redes.
  - Verificação: decisão documentada sobre conectar agora ou depois.
  - Estimativa: 1h.
  - Depende de: contas e permissões administrativas.

### Fase 4: Pesquisa web enriquecida

- [ ] **T4.1** — Decidir sobre Tavily.
  - Verificação: Tavily ativado com smoke test ou registrado como adiado.
  - Estimativa: 30min.
  - Depende de: chave Tavily válida, se for ativar.

- [ ] **T4.2** — Criar rotina semanal de pesquisa por cliente/frente.
  - Verificação: checklist semanal ou cron/heartbeat definido.
  - Estimativa: 45min.
  - Depende de: central mínima criada.

## Dependências externas

- Acesso/admin das redes sociais.
- Possível chave Tavily.
- Pastas OneDrive ou arquivos para triagem.
- Permissão para criar database Notion e pasta Drive.

## Riscos

- Misturar dados sensíveis de cliente no GitHub — mitigação: GitHub só para documentação/processos, não mídia bruta sensível.
- Central virar depósito sem triagem — mitigação: usar `00_Inbox` + status + revisão semanal.
- Links quebrarem/sumirem — mitigação: salvar print/download para referências estratégicas.
- APIs de redes consumirem tempo cedo demais — mitigação: começar por fluxo manual/semiautomático.

## Estado atual

- Mapa inicial criado em `pesquisa/CENTRAL-DE-PESQUISA-LOGIKA.md`.
- Tavily verificado como instalado, mas desativado.
- Notion, Drive, Vault, GitHub e web já disponíveis em algum nível.

---

*Atualizar este arquivo conforme execução. Não criar arquivo novo — versionar este.*

## Atualização — decisões de Jadielson em 2026-06-05

- Redes sociais: começar por links/prints/downloads/anotações/exportações; APIs ficam para depois.
- Notion: criar grade/database para links de referência e dados públicos.
- OneDrive: migrar preferencialmente para Google Drive, não GitHub.
- Referências: criar tópico/agente próprio para captar, estudar e encaminhar referências.
- Tavily: Jadielson está disposto a habilitar; próximo passo é gerar API key em https://app.tavily.com/home.

### Nova tarefa

- [ ] **T1.4** — Criar tópico/agente `Radar` ou nome equivalente para Referências & Pesquisa.
  - Verificação: tópico configurado, prompt definido e primeiro teste com link/print executado.
  - Estimativa: 45min.
  - Depende de: Jadielson confirmar nome/tópico ou enviar/criar tópico no Telegram.

- [ ] **T4.3** — Ativar Tavily.
  - Verificação: plugin `tavily` habilitado, chave configurada e busca teste retornando resultado.
  - Estimativa: 30min.
  - Depende de: Jadielson gerar/enviar API key Tavily.
