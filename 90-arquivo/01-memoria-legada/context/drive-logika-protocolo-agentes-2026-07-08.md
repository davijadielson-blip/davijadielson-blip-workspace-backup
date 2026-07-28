---
tipo: protocolo-operacional
data: 2026-07-08
responsavel: jarvis
status: vigente
escopo: LÓGIKA / Google Drive / agentes
---

# Protocolo para agentes — Drive da LÓGIKA

## Status
O Drive da LÓGIKA foi reorganizado em fase inicial e a pasta `01_CLIENTES` foi padronizada usando `SAÚDE - SÃO SEBASTIÃO` como modelo.

## Regra principal
Todo agente que for lidar com arquivos da LÓGIKA deve consultar primeiro:
1. Pasta Drive `00_LEIA-ME_E_MAPA_DO_DRIVE`.
2. Google Doc `MAPA_DO_DRIVE_LOGIKA.md`.
3. Este protocolo no Cofre.

## Estrutura padrão dos clientes

```text
CLIENTE/
├── 00_ADMIN_BRIEFINGS
├── 01_IDENTIDADE_VISUAL
├── 02_PLANEJAMENTO
├── 03_BRUTOS
├── 04_PROJETOS_EDICAO
│   ├── ARTES
│   └── VIDEOS
├── 05_ENTREGAS_FINAIS
│   └── RENDERs FINAIS
├── 06_PUBLICADOS_ARQUIVO
└── 99_REVISAR_DUPLICADOS
```

## Como administrar
- Briefings, informações do cliente, alinhamentos e materiais administrativos: `00_ADMIN_BRIEFINGS`.
- Logos, marcas, identidade visual e arquivos institucionais do cliente: `01_IDENTIDADE_VISUAL`.
- Estratégia, calendário, campanhas e planejamento: `02_PLANEJAMENTO`.
- Fotos/vídeos brutos, gravações originais e material de captação: `03_BRUTOS`.
- Arquivos editáveis, artes em construção e projetos de vídeo: `04_PROJETOS_EDICAO/ARTES` ou `04_PROJETOS_EDICAO/VIDEOS`.
- Renders, vídeos finais e artes aprovadas para entrega: `05_ENTREGAS_FINAIS/RENDERs FINAIS`.
- Materiais já publicados/arquivados: `06_PUBLICADOS_ARQUIVO`.
- Itens repetidos, incertos ou para revisão humana: `99_REVISAR_DUPLICADOS`.

## Regras de segurança
- Não deletar nada.
- Não mover arquivos sensíveis sem validação de Jadielson/Jarvis/Lôh.
- Duplicado aparente não é duplicado confirmado; separar para revisão.
- Arquivos parados continuam em `99_TRIAGEM_ARQUIVOS_PARADOS_ANTIGO_OUTROS` até triagem por lote.
- Em caso de dúvida, registrar no Cofre e pedir decisão.

## Observação para agentes
A estrutura está clara para operação básica. A principal dificuldade esperada é classificar materiais antigos/parados ou arquivos sem nome claro. Nesses casos, o agente deve sugerir destino e aguardar validação humana antes de mover.
