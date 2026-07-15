---
tipo: consulta_cron_financeiro
data: 2026-07-15
agente: Warren
escopo: finanças pessoais
origem: Telegram Central Pessoal / My Finance
---

# Consulta — cron de relatório mensal de contas a pagar

Jadielson perguntou se existe cron para rodar relatório das contas que devem ser pagas do mês corrente, com entrega no último dia do mês, respeitando meses com 28, 30 ou 31 dias.

Verificação realizada em 2026-07-15:
- Lista de cron jobs ativos/inativos consultada via ferramenta `cron list`.
- Busca no Cofre por registros de cron/relatório/contas a pagar.

Resultado:
- Não foi encontrado cron específico do Warren/My Finance para relatório mensal de contas a pagar no último dia do mês.
- Existem crons gerais e de outras frentes, mas nenhum dedicado a esse fechamento financeiro pessoal.

Proposta técnica segura:
- Criar cron recorrente em `America/Maceio`, rodando nos dias 28 a 31, com checagem interna de data local para só entregar relatório quando o dia atual for o último dia real do mês.
- Alternativa se o scheduler aceitar sintaxe de último dia (`L`): usar `0 8 L * *`; porém a abordagem mais compatível é 28-31 + checagem.
- Relatório deve ler a planilha `Warren — Controle Financeiro Pessoal 2026`, aba `Contas a pagar`, filtrar mês corrente, separar PAGO/PENDENTE/PARCIAL/ADIADO/A LEVANTAR, e entregar no tópico My Finance.

Pendente de decisão:
- Confirmar horário de envio. Sugestão conservadora: 08h de Maceió no último dia do mês.
