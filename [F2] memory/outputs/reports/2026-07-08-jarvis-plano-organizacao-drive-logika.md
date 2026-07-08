---
tipo: plano-operacional
data: 2026-07-08
gerado-por: jarvis
status: aguardando-aprovacao-humana
conta-drive: logikacreative.mkt@gmail.com
escopo: auditoria readonly + plano de organização
---

# Plano inicial — Organização do Drive da LÓGIKA

## Pedido de Jadielson
Organizar e otimizar o Drive da empresa de forma simples, comunicativa e clara para humanos e agentes. Categorizar clientes, contratos, propostas, produção de vídeos, artes, banco de dados de logos/assinaturas, estratégias, empresa e materiais duplicados/escondidos.

## Auditoria executada
- Ferramenta: `gog` via terminal, conta `logikacreative.mkt@gmail.com`, modo leitura.
- Inventário parcial salvo em: `F2-memory/inbox-externa/drive/logika-2026-07-08/inventory-my-drive.json`.
- Árvore parcial salva em: `F2-memory/inbox-externa/drive/logika-2026-07-08/tree-depth4.txt`.
- Resultado lido: 3.000 itens; inventário truncado (`truncated: true`).
- Distribuição inicial detectada:
  - `OUTROS`: 2.210 itens.
  - `01_CLIENTES`: 620 itens.
  - `03_EMPRESA`: 121 itens.
  - `PORTIFÓLIO`: 32 itens.
  - `02_PROJETOS`: 17 itens.
- Tipos principais: vídeos MP4, imagens Sony ARW/JPEG/DNG, documentos Office e alguns arquivos compactados.

## Achados principais
1. A estrutura nova já começou a existir: `01_CLIENTES`, `02_PROJETOS`, `03_EMPRESA`, `PORTIFÓLIO`.
2. O maior volume ainda está em `OUTROS`, provavelmente contendo material antigo, misturado ou não classificado.
3. Há clientes já padronizados com subpastas: `00_ADMIN_BRIEFINGS`, `01_IDENTIDADE_VISUAL`, `02_PLANEJAMENTO`, `03_PRODUCAO_BRUTA`, `04_PROJETOS_EDICAO`, `05_ENTREGAS_FINAIS`, `06_PUBLICADOS_ARQUIVO`, `99_REVISAR_DUPLICADOS`.
4. Existem materiais que parecem duplicados entre `01_CLIENTES/.../05_ENTREGAS_FINAIS` e `PORTIFÓLIO/VIDEOS/RENDERs FINAIS`.
5. Duplicidades por nome existem, mas várias podem ser legítimas por câmera/dia de gravação (`C0001.MP4`, etc.); não devem ser apagadas automaticamente.
6. Existe pasta `99_REVISAR_CLIENTES_NAO_CADASTRADOS`, útil para triagem de clientes antigos/avulsos.

## Estrutura recomendada

```text
DRIVE LÓGIKA/
├── 00_LEIA-ME_E_MAPA_DO_DRIVE
├── 01_CLIENTES
│   ├── CLIENTE_NOME
│   │   ├── 00_ADMIN_BRIEFINGS
│   │   │   ├── briefing.md/doc
│   │   │   ├── contatos_e_acessos
│   │   │   └── reunioes_e_alinhamentos
│   │   ├── 01_CONTRATOS_E_PROPOSTAS
│   │   │   ├── propostas
│   │   │   ├── contratos_assinados
│   │   │   ├── notas_fiscais_recibos
│   │   │   └── pendencias_comerciais
│   │   ├── 02_ESTRATEGIA_E_PLANEJAMENTO
│   │   │   ├── calendario_editorial
│   │   │   ├── campanhas
│   │   │   ├── personas_tom_de_voz
│   │   │   └── referencias
│   │   ├── 03_BANCO_DE_DADOS_DO_CLIENTE
│   │   │   ├── logos
│   │   │   ├── assinaturas
│   │   │   ├── identidade_visual
│   │   │   ├── fotos_oficiais
│   │   │   └── acessos_permitidos
│   │   ├── 04_PRODUCAO_BRUTA
│   │   │   ├── videos_brutos
│   │   │   ├── fotos_brutas
│   │   │   ├── audios
│   │   │   └── por_data_evento
│   │   ├── 05_PROJETOS_DE_EDICAO_E_ARTES
│   │   │   ├── premiere_davinci_capcut
│   │   │   ├── photoshop_illustrator_canva
│   │   │   └── arquivos_de_trabalho
│   │   ├── 06_ENTREGAS_FINAIS
│   │   │   ├── videos
│   │   │   ├── artes
│   │   │   ├── legendas_textos
│   │   │   └── aprovados_cliente
│   │   ├── 07_PUBLICADOS_E_ARQUIVO
│   │   └── 99_REVISAR_DUPLICADOS_OU_MIGRAR
│   └── 99_REVISAR_CLIENTES_NAO_CADASTRADOS
├── 02_PROJETOS_PROPRIOS
│   ├── ALÉM_DA_FOTO
│   ├── O_FIO_DA_MEMORIA
│   └── VIDEOCLIPES_E_PROJETOS_AUTORAIS
├── 03_EMPRESA_LOGIKA
│   ├── 01_ADMINISTRATIVO
│   ├── 02_CONTRATOS_MODELOS_E_JURIDICO
│   ├── 03_FINANCEIRO_EMPRESA
│   ├── 04_COMERCIAL_PROPOSTAS_MODELOS
│   ├── 05_MARKETING_DA_LOGIKA
│   ├── 06_IDENTIDADE_VISUAL_LOGIKA
│   ├── 07_PROCESSOS_TEMPLATES_CHECKLISTS
│   └── 99_REVISAR_DUPLICADOS
├── 04_PORTFOLIO_E_CASES
│   ├── videos_aprovados_para_mostrar
│   ├── artes_aprovadas_para_mostrar
│   └── cases_por_segmento
├── 05_ACERVO_E_REFERENCIAS
│   ├── trilhas_sons_fontes
│   ├── referencias_criativas
│   └── assets_reutilizaveis
└── 99_TRIAGEM_E_QUARENTENA
    ├── arquivos_sem_dono_identificado
    ├── possiveis_duplicados_nao_apagar
    └── revisar_com_jadielson
```

## Regras de segurança
- Não deletar nada.
- Não mover material sensível sem aprovação humana.
- Duplicado vai para pasta de revisão/quarentena, não para exclusão.
- Contratos, propostas, documentos financeiros e dados de acesso devem ficar em pastas com permissão restrita.
- Portfólio deve conter apenas material aprovado para mostrar/publicar.

## Próximas fases propostas
1. Validar estrutura com Jadielson.
2. Completar inventário em lotes menores se o inventário total travar.
3. Criar/ajustar apenas pastas-base aprovadas.
4. Gerar planilha de triagem: item atual → destino sugerido → confiança → precisa revisar? → observação.
5. Mover em lotes pequenos: primeiro `OUTROS`, depois duplicados aparentes, depois clientes não cadastrados.
6. Criar `00_LEIA-ME_E_MAPA_DO_DRIVE` com explicação simples para humanos e agentes.

## Status
Plano concluído como proposta. Nenhuma movimentação, exclusão, renomeação ou alteração externa foi executada.
