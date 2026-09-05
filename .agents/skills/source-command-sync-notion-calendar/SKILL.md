---
name: "source-command-sync-notion-calendar"
description: "Sincroniza Notion (Calendário Editorial Saúde) → Google Calendar manualmente"
tema: sincronizacao notion calendar
conteudo: instrucoes para agentes rodarem sync Notion para Google Calendar usando MAPA 360 e Producao LOGIKA com tokens separados
setor: operacoes tecnicas e produtividade
cliente: Jadielson Davi
tipo: skill
prioridade: alta
atualizado_em: 2026-08-11
usar_quando: rodar ou validar sincronizacao manual Notion para Google Calendar
nao_usar_quando: publicar conteudo, enviar mensagens ou alterar Notion sem validacao do escopo
---

# source-command-sync-notion-calendar

Use this skill when the user asks to run the migrated source command `sync-notion-calendar`.

## Integracoes Notion

O ambiente tem duas conexoes Notion separadas:

- `MAPA 360`: painel pessoal/estrategico e camada visual do Cofre. Carregado por `scripts/.secrets/notion.env`.
- `Loh-bot`: producao/editorial da LOGIKA. Carregado por `scripts/.secrets/notion-logika-producao.env`.

Sempre carregue o ambiente antes de validar ou rodar scripts Notion:

```bash
source scripts/notion-env.sh
```

Nao exponha tokens em respostas, logs Markdown ou relatorios. Registre apenas caminho seguro, status, workspace/bot, database consultada e resultado dos testes.

## Base de Producao

Base oficial para producao/editorial:

- Nome: `Producao & Agenda - LOGIKA`
- ID: `375207e6-f145-8111-bba0-e132fd820542`
- Integracao: `Loh-bot`
- Workspace: `LOGIKA CREATIVE`
- Variaveis: `NOTION_LOGIKA_TOKEN`, `NOTION_PRODUCAO_DATABASE_ID`, `NOTION_API_VERSION`

## Command Template

Antes de rodar sync completo, faca uma validacao seca de leitura quando houver mudanca recente de token, database, campos ou regra de status:

```bash
source scripts/notion-env.sh
python3 - <<'PY'
import importlib.util
from pathlib import Path
script = Path('scripts/sync/notion-to-calendar.py')
spec = importlib.util.spec_from_file_location('notion_to_calendar', script)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
items = mod.fetch_notion_items()
print(f"itens_elegiveis={len(items)}")
PY
```

Se a leitura estiver correta e o usuario tiver confirmado que pode atualizar o Calendar, rode o script de sync e mostre o relatorio.

```bash
source scripts/notion-env.sh
python3 scripts/sync/notion-to-calendar.py
```

Depois leia o log gerado em `[F2] memory/sessions/sync/YYYY-MM-DD.md` e mostre:
- Quantos eventos criados
- Quantos atualizados
- Erros (se houver)
- Lista dos itens sincronizados

O sync é **unidirecional**: Notion → Calendar. Mudanças feitas diretamente no Google Calendar não voltam para o Notion.
