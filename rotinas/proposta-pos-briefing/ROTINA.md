# Rotina: proposta-pos-briefing

## Objetivo
Transformar briefing comercial em proposta versionada sem desalinhamento com produção/entrega.

## Gatilho
Após briefing com lead/prospect ou cliente ativo.

## Passos
1. Registrar resumo do briefing em `areas/vendas/contexto/`.
2. Rodar a skill `montar-proposta-logika`.
3. Validar riscos com COO/produção quando houver operação sensível.
4. Validar promessa criativa com CCO/CMO quando houver conteúdo/campanha.
5. Gerar versão da proposta e registrar pendências.
6. Enviar para aprovação de Jadielson antes de envio externo.

## Indicadores
- Tempo entre briefing e proposta
- Número de propostas versionadas
- Pendências por proposta
- Gargalos de entrega identificados antes da venda
