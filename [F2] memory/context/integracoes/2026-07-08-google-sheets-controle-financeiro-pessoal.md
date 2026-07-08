---
tipo: plano_operacional
data: 2026-07-08
agente: Warren
escopo: finanças pessoais
origem: Telegram Central Pessoal / My Finance
---

# Google Sheets — Controle Financeiro Pessoal Warren

## Pedido de Jadielson

Jadielson sugeriu que, além de guardar comprovantes e registros no Cofre e na pasta FINANCEIRO do Google Drive, Warren também mantenha uma planilha no Google Sheets para dar um panorama financeiro mais abrangente.

## Decisão operacional

Criar uma planilha Google Sheets de controle financeiro pessoal, mantendo parede d'água total com a LÓGIKA/empresa.

Nome sugerido:

`Warren — Controle Financeiro Pessoal 2026`

Local sugerido no Drive:

`FINANCEIRO/`

## Abas mínimas

1. `Resumo`
   - mês
   - total pago
   - total pendente
   - total a verificar
   - principais categorias
   - observações do mês

2. `Lançamentos`
   - ID
   - data de pagamento/vencimento
   - competência
   - categoria
   - descrição
   - valor
   - status: PAGO / PENDENTE / A VERIFICAR / FUTURO PAGO
   - forma: Pix / boleto / cartão / débito automático / não informado
   - pessoa/beneficiário
   - origem: Telegram / Drive / Cofre / manual
   - link do comprovante no Drive
   - caminho no Cofre
   - observações

3. `Contas a pagar`
   - vencimento
   - categoria
   - descrição
   - valor previsto
   - prioridade
   - status
   - observações

4. `Config`
   - categorias pessoais permitidas
   - regra de parede d'água: não lançar LÓGIKA/empresa na planilha pessoal
   - padrões de status e nomenclatura

## Lançamentos iniciais a migrar

Base inicial: comprovantes pessoais registrados em julho/2026 no arquivo `[F2] memory/context/integracoes/drive_financeiro_lancamentos_2026-07.md` e status provisório em `[F2] memory/context/integracoes/financeiro_status_a_quitar_2026-07-07.md`.

## Estado técnico em 2026-07-08 04:41 UTC

- A ideia foi aprovada por Jadielson no tópico My Finance.
- Tentativa direta via `gog sheets create` falhou por limite temporário de threads/processos do container: `failed to create new OS thread` / `Resource temporarily unavailable`.
- Zapier Google Sheets foi localizado e habilitado, mas exige autenticação própria antes de executar criação/edição de planilhas por esse caminho.
- Próximo passo: criar a planilha via `gog` assim que o limite técnico do container normalizar, ou autenticar Google Sheets no Zapier se Jadielson/Lôh preferirem esse caminho.

## Regra de segurança

Não registrar dados empresariais da LÓGIKA nesta planilha. Se algum comprovante ou despesa empresarial aparecer no My Finance, encaminhar para Alfred/Lôh ou para o tópico financeiro da LÓGIKA.
