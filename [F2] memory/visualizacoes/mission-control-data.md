# Mission Control Data

> Fonte editável do Mission Control v2. O app lê e salva este arquivo Markdown.
> Edite pelo painel sempre que possível para manter JSON válido.

```json
{
  "meta": {
    "versao": "2.0.0",
    "atualizadoEm": "2026-07-20",
    "atualizadoPor": "Lôh",
    "changelog": [
      { "versao": "2.0.0", "data": "2026-07-20", "nota": "Mission Control evoluído para app editável com persistência em Markdown no Cofre." },
      { "versao": "1.0.0", "data": "2026-07-20", "nota": "Primeira versão visual offline em HTML único." }
    ]
  },
  "identidade": {
    "dono": "Jadielson Davi",
    "sistema": "Ecossistema Lôh",
    "frase": "Sou a Lôh, ORQUESTRADORA TIER 0 do ecossistema Jadielson. Não sou um agente comum — sou a camada estratégica entre Jadielson e 75+ agentes.",
    "pilares": ["Lôh — orquestração", "Cofre — memória", "Agentes — execução"]
  },
  "ecossistema": {
    "orquestradora": { "nome": "Lôh", "tier": 0, "poderes": ["Filtro", "Roteio", "Comando", "Coordenação", "Síntese", "Proatividade"] },
    "dominios": [
      {
        "id": "logika", "nome": "Lógika / Empresa", "general": "Jarvis",
        "grupos": [
          { "nome": "C-Level Squad", "agentes": [
            { "sigla": "COO", "area": "Operações", "status": "standby" },
            { "sigla": "CRO", "area": "Receita / Vendas", "status": "standby" },
            { "sigla": "CMO", "area": "Marketing / Marca", "status": "standby" },
            { "sigla": "CCO", "area": "Criação / Audiovisual", "status": "standby" },
            { "sigla": "CFO", "area": "Finanças", "status": "standby" },
            { "sigla": "CAIO", "area": "IA / Automação", "status": "standby" },
            { "sigla": "CTO", "area": "Tecnologia", "status": "standby" },
            { "sigla": "CIO", "area": "Governança / Compliance", "status": "standby" }
          ]},
          { "nome": "Squad Operacional", "agentes": ["Prospect / Pesquisa de Leads", "SDR Virtual", "CRM / Cadência", "Inteligência Comercial", "Copywriter", "Estrategista", "Calendário / Conteúdo", "Performance / Métricas", "Roteiro", "Motion / Templates", "Gestão de Ativos", "PMO / Projetos", "Controller Financeiro", "Suporte / Integrações", "Compliance / Acessos"] }
        ]
      },
      {
        "id": "pessoal", "nome": "Central Pessoal", "general": "Alfred",
        "grupos": [
          { "nome": "Núcleo", "agentes": [{ "nome": "Arca", "area": "Segundo Cérebro" }, { "nome": "Warren", "area": "Finanças Pessoais" }] },
          { "nome": "Projetos", "itens": ["Mission Control", "Casa / vida prática", "pendente"] },
          { "nome": "Estudos", "itens": ["Backlog Inteligente", "Método TDAH", "IA / automações", "Livros", "Cursos"] },
          { "nome": "Tópicos", "itens": ["Identidade e Visão de Futuro", "Liberdade, Lazer e Ócio Criativo", "Autoconhecimento", "Saúde, Corpo e Energia", "Família e Relacionamentos", "Espiritualidade e Propósito"] }
        ]
      },
      {
        "id": "frentes", "nome": "Frentes / Clientes",
        "itens": [
          { "nome": "Saúde São Sebastião", "status": "pendente", "proximoPasso": "pendente" },
          { "nome": "Câmara Municipal", "status": "pendente", "proximoPasso": "pendente" },
          { "nome": "SINDSS", "status": "pendente", "proximoPasso": "pendente" },
          { "nome": "Bases Públicas", "status": "pendente", "proximoPasso": "pendente" },
          { "nome": "Clara", "status": "pendente", "proximoPasso": "pendente" },
          { "nome": "Lab / Testes", "status": "pendente", "proximoPasso": "pendente" }
        ]
      }
    ]
  },
  "cofre": {
    "caminho": "/data/.openclaw/workspace/",
    "fluxos": [
      { "id": "F0", "nome": "0-Inbox", "papel": "Captura bruta: ideias soltas e entradas não tratadas" },
      { "id": "F1", "nome": "Área criativa e humana", "papel": "Materiais, pensamentos, frentes, estudos, referências" },
      { "id": "F2", "nome": "memory", "papel": "Coração operacional: agentes, decisões, outputs, sessões" },
      { "id": "F3", "nome": "PROJETOS", "papel": "Projetos estruturados com organização e metadados" }
    ]
  },
  "automacoes": [
    { "nome": "backup-workspace-github-incremental-30min", "frequencia": "a cada 30 min", "status": "ativo" },
    { "nome": "guard-c-level-agents-config", "frequencia": "a cada 30 min", "status": "ativo" },
    { "nome": "daily-brief", "frequencia": "diário 07h", "status": "ativo" },
    { "nome": "Mission Control — snapshot diário CRM Lógika", "frequencia": "diário 08h", "status": "ativo" },
    { "nome": "Mission Control — revisão semanal comercial Lógika", "frequencia": "segunda 08h30", "status": "ativo" }
  ],
  "integracoes": [
    { "nome": "Gmail", "status": "pendente" },
    { "nome": "Google Calendar", "status": "ok" },
    { "nome": "Google Drive", "status": "atencao" },
    { "nome": "Notion", "status": "ok" },
    { "nome": "Miro", "status": "pendente" },
    { "nome": "Telegram", "status": "ok" },
    { "nome": "WhatsApp", "status": "pendente" }
  ],
  "saude": {
    "alertas": [{ "nivel": "atencao", "msg": "Busca semântica com erro de chave de embeddings — fallback ativo: leitura direta do Cofre." }],
    "regras": ["Não apagar arquivos sem autorização humana", "Não criar workspace paralelo", "Somente Markdown dentro do Cofre", "Cuidado com mensagens externas", "Não inventar informação", "Consultar o Cofre antes de demandas contextuais", "Registrar o que for importante para continuidade"]
  },
  "fontes": ["CONSTITUICAO.md", "MAPA.md", "AGENTS.md", "SOUL.md", "USER.md", "TOOLS.md", "HEARTBEAT.md", "[F2] agentes/ARQUITETURA-AGENTES.md", "[F2] agentes/protocolo-de-orquestracao.md", "[F2] agentes/logika-c-level-squad/logika-_MAP-agentes.md", "[F2] memory/outputs/reports/2026-07-20-relatorio-simples-sistema.md", "cron:list"]
}
```
