---
description: Cria novo projeto com estrutura padrão em PROJETOS/A INICIAR/
argument-hint: <nome do projeto>
---

Cria um novo projeto com estrutura padrão. Sem perguntas desnecessárias.

**Nome:** $ARGUMENTS

**Execute agora, em ordem:**

1. Obtenha a data atual:
```bash
date +"%Y-%m-%d"
```

2. Sanitize o nome: converta para maiúsculas, remova caracteres proibidos em nomes de pasta (`/ \ : * ? " < > |`). Use esse nome como `NOME_LIMPO`.

3. Crie a estrutura de pastas e arquivos em `PROJETOS/A INICIAR/NOME_LIMPO/`:

   **Arquivo principal** `NOME_LIMPO.md`:
   ```
   ---
   tipo: projeto
   status: a-iniciar
   frente: pessoal
   fase-atual: pesquisa
   criado-em: DATA_HOJE
   proximo-review: (calcule 6 semanas à frente)
   destino-matriz: FOCO
   ultimo_update: DATA_HOJE
   saude: 🟢 ativo
   ---

   # NOME_LIMPO

   ---

   ## 🧭 Por que existe


   ---

   ## 🎯 Resultado esperado


   ---

   ## 📚 Precisa pesquisar antes

   - [ ] 

   ---

   ## 🗺️ Próximas fases

   - [ ] 

   ---

   ## 🔗 Conexões

   -
   ```

   **`1-briefing.md`:**
   ```
   ---
   tipo: briefing
   projeto: NOME_LIMPO
   ---

   # Briefing — NOME_LIMPO

   ## Contexto
   *Por que esse projeto existe? Que problema resolve?*

   ## Objetivo claro
   *Qual o resultado mensurável que define "feito"?*

   ## Critérios de sucesso
   - [ ]
   - [ ]
   - [ ]

   ## Restrições e premissas
   -

   ## Stakeholders
   -

   ---
   *Criado em DATA_HOJE. Atualizar conforme o projeto evolui.*
   ```

   **`proximas-etapas.md`:**
   ```
   ---
   tipo: kanban
   projeto: NOME_LIMPO
   ---

   # 🎯 Próximas Etapas — NOME_LIMPO

   ## 🟡 A FAZER (prioridade decrescente)
   - [ ] Definir objetivo concreto e prazo
   - [ ] Levantar recursos necessários

   ## 🔵 FAZENDO (máx 2 itens)
   - [ ]

   ## 🟢 FEITO (últimos 7 dias)
   - [x]

   ---

   ## ⚡ Próxima ação concreta
   *Qual o menor passo que faz o projeto avançar HOJE?*

   → 

   ---
   *Atualizar pelo menos 1x por semana.*
   ```

   **Subpastas** — crie cada uma com seu `_index.md`:
   - `2-pesquisas/_index.md` → `# Pesquisas & Referências\n\nReferências, editais, orçamentos, inspirações.`
   - `3-dados/_index.md` → `# Dados & Métricas\n\nTabelas, números, cronogramas.`
   - `4-decisoes/_index.md` → `# Decisões\n\nRegistro de decisões importantes do projeto.`
   - `5-resumos-semanais/_index.md` → `# Resumos Semanais\n\nEvolução semana a semana.`
   - `6-entregas/_index.md` → `# Entregas\n\nArquivos finais e entregas do projeto.`
   - `7-arquivo/_index.md` → `# Arquivo\n\nMaterial histórico e arquivado.`

   Cada `_index.md` deve ter frontmatter:
   ```
   ---
   tipo: indice
   secao: NOME_DA_SUBPASTA
   ---
   ```

4. Após criar todos os arquivos, faça commit e push:
```bash
git -C "$(pwd)" add -A && git -C "$(pwd)" commit -m "novo projeto: NOME_LIMPO" && git -C "$(pwd)" push origin main
```

5. Responda em 2 linhas:
   ```
   ✓ Projeto criado: PROJETOS/A INICIAR/NOME_LIMPO/
   Abra o arquivo principal para preencher frente, objetivo e próximas etapas.
   ```

Nada mais. Não explique, não pergunte, não comente.
