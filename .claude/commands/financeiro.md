---
description: Importa planilha financeira e atualiza contexto de receitas no vault
---

Você é a bibliotecária do vault. Importe dados financeiros e atualize o contexto de negócio.

O arquivo ou dados a importar são: `$ARGUMENTS`

**PASSO 1 — Obter os dados**

Se `$ARGUMENTS` for um caminho de arquivo (`.xlsx`, `.csv`, `.txt`):
- Para `.csv` ou `.txt`: leia o arquivo diretamente
- Para `.xlsx`: instrua o usuário a exportar como CSV primeiro:
  ```
  No Excel/Sheets: Arquivo → Baixar → CSV
  Depois: /financeiro caminho/do/arquivo.csv
  ```

Se `$ARGUMENTS` estiver vazio:
- Peça ao usuário que cole os dados ou informe o caminho:
  ```
  Cole os dados financeiros (formato livre) ou informe o caminho do arquivo.
  Exemplo aceito:
    Câmara: R$ 1.200
    SINDSS: R$ 500
    Ewander: -R$ 300
    ...
  ```

**PASSO 2 — Identificar estrutura**

Detecte as colunas disponíveis. Estrutura esperada (mas não obrigatória):
- Frente / Cliente
- Receita ou Despesa
- Status (pago, pendente, em atraso)
- Mês de referência

**PASSO 3 — Resumo financeiro**

Calcule e apresente:

```
## 💰 Resumo Financeiro — [Mês/Período]

### Receitas
| Frente | Valor | Status |
|---|---|---|
| Câmara Municipal | R$ 1.200 | ✅ Pago |
| SINDSS | R$ 500 | ✅ Pago |
| **Total receitas** | **R$ 1.700** | |

### Despesas
| Item | Valor | Status |
|---|---|---|
| Ewander (designer) | R$ 300 | ✅ Pago |
| **Total despesas** | **R$ 300** | |

### Resultado
**Lucro líquido: R$ 1.400**

### Alertas
- ⚠️ [frente] com pagamento pendente há X dias
- ℹ️ [observação relevante]
```

**PASSO 4 — Comparar com contexto atual**

Leia `[F2] memory/context/business-context.md` e verifique se os valores mudaram em relação ao que está registrado.

Se houver diferença, mostre:
```
Diferenças detectadas vs. business-context.md:
- [Frente X]: era R$ Y → agora R$ Z
Quer atualizar o business-context.md?
```

**PASSO 5 — Perguntar antes de salvar**

```
Dados processados. Quer que eu:
1. Atualize [F2] memory/context/business-context.md com os novos valores?
2. Salve um snapshot mensal em [F2] memory/inbox-externa/ (histórico)?
3. Apenas exiba o resumo sem salvar?
```

Não salva nem atualiza nada sem aprovação explícita.
