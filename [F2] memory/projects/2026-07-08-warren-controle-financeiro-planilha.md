# Warren — Controle Financeiro Pessoal 2026

**Criado em:** 2026-07-08
**Responsável:** Warren (agente My Finance)
**Tipo:** Finanças Pessoais (nada da LÓGIKA)

---

## Arquitetura (3 camadas)

| Camada | Local | Função |
|---|---|---|
| 🗄️ Cofre | `/data/.openclaw/workspace/` | Memória, decisões, scripts |
| 📁 Drive | Pasta `FINANCEIRO` | Armazenamento de documentos |
| 📊 Planilha | Google Sheets | Panorama mensal e lançamentos |

---

## Planilha

**Nome:** Warren — Controle Financeiro Pessoal 2026
**URL:** https://docs.google.com/spreadsheets/d/1HS9w4c04l2tUlggaztNPQuk-2BYIDmaTHTI7Df0QCGs/edit
**ID:** `1HS9w4c04l2tUlggaztNPQuk-2BYIDmaTHTI7Df0QCGs`
**Pasta:** FINANCEIRO (no Drive pessoal `davijadielson@gmail.com`)

### Abas

1. **Resumo** — 10 colunas: Mês, Receitas, Despesas, Saldo, Receitas Fixas, Receitas Variáveis, Despesas Fixas, Despesas Variáveis, Economias, % Economia
2. **Lançamentos** — 11 colunas: Data, Categoria, Subcategoria, Descrição, Valor, Tipo, Conta, Forma de Pagamento, Status, Mês Referência, Observações
3. **Contas a pagar** — 10 colunas: Vencimento, Categoria, Descrição, Valor, Status, Prioridade, Conta Débito, Recorrente, Mês Referência, Pago em
4. **Config** — 4 colunas: Parâmetro, Valor, Tipo, Descrição

### Formatação aplicada
- ✅ Cabeçalhos em negrito com fundo escuro
- ✅ Linha do cabeçalho congelada (freeze)
- ✅ Colunas com auto-resize

---

## Autenticação

**Método:** OAuth2 via Google API com escopos sheets + drive
**Credenciais:** `scripts/.secrets/google-calendar-credentials.json` (cliente OAuth `logika-openclaw-gog`)
**Token salvo em:** `scripts/.secrets/google-sheets-token.json`
**Conta:** `davijadielson@gmail.com`

### Como renovar token
O token tem refresh_token, então renova automaticamente. Se precisar re-autenticar, usar:
```python
python3 scripts/.secrets/financeiro_criar_planilha.py  # ou fluxo OAuth manual
```

---

## Observações

- Criado via Python (API Google Sheets v4 + Drive v3) — gog CLI não funcionou por limite de threads do container
- Zapier removido a pedido do usuário (MCP servers desabilitados)
- Container com load avg ~19 no momento da criação — pode precisar de restart periódico