---
tema: 07 08 auditoria drive pessoal relatorio final
atualizado_em: 2026-07-22
---

# Relatório final — Auditoria do Google Drive pessoal

**Data de fechamento:** 2026-07-08 00:22 UTC  
**Agente:** Alfred / Central Pessoal  
**Conta auditada:** `davijadielson@gmail.com`  
**Método:** `gog` / Google OAuth direto  
**Zapier:** não utilizado  
**Modo:** leitura; nenhuma exclusão, movimentação, renomeação ou alteração foi executada.

## Conclusão objetiva

A auditoria técnica do Drive pessoal foi **concluída**.

Foram concluídas:

- Inventário estrutural do Drive.
- Coleta por pastas raiz.
- Consolidação em CSV.
- Classificação por categorias candidatas.
- Levantamento de duplicatas prováveis.
- Levantamento de arquivos grandes.
- Auditoria completa de permissões dos itens inventariados.
- Consolidação dos achados principais.

## Escopo inventariado

- Itens totais: **3.378**
- Pastas: **610**
- Arquivos: **2.768**
- Tamanho conhecido: **~502,9 GB**
- Permissões processadas: **3.378 / 3.378**
- Restantes: **0**

## Pastas raiz encontradas

1. `01_PROJETOS`
2. `02_FOTOS_SOLTAS`
3. `03_LOGIKA_NEGOCIO`
4. `04_PESSOAL`
5. `05_OUTROS`
6. `CONTADOS CELULAR`
7. `ESTUDOS`
8. `EXCEL  e SHEETS`
9. `FINANCEIRO`
10. `FORMULÁRIOS`
11. `Google Earth`
12. `PDF's`
13. `PERFIL DA EMPRESA LÓGIKA CREATIVE`
14. `POWER POINT`
15. `PRODUTIVIDADE`
16. `PROPOSTAS`

## Concentrações principais

- `ESTUDOS` / cursos: maior massa do Drive.
- `04_PESSOAL`: núcleo principal da vida pessoal.
- `EBOOKs` e cursos: forte presença de duplicatas e arquivos públicos por link.
- Materiais de LÓGIKA/empresa aparecem misturados no Drive pessoal.

## Categorias candidatas

- Materiais LÓGIKA/empresa: **87** candidatos
- Financeiro: **25** candidatos
- Sensível pessoal: **24** candidatos
- Família/casa: **262** candidatos
- Estudos/cursos: **2.875** candidatos
- Fotos/mídias: **1.558** candidatos
- Grupos de duplicatas candidatas: **179**

## Achados de compartilhamento

Arquivo normalizado:

`[F2] memory/outputs/central-pessoal/drive_pessoal_auditoria_completa_2026-07-07/permissoes_todos_achados.csv`

Principais achados:

1. Vários ePUBs em `EBOOKs/` com `anyoneWithLink` como leitor.
2. `PLANILHA DE CÁLCULO VALOR DA HORA DE TRABALHO - LÓGIKA` com `anyoneWithLink` como leitor.
3. `BRIEFING PARA IDENTIDADE VISUAL` compartilhado com `logikacreative.mkt@gmail.com` como editor.
4. `Rapidinho: Me Conta do Seu Negócio!` com `anyoneWithLink` como editor e também compartilhado com `logikacreative.mkt@gmail.com` como editor.
5. `PROPROSTA PRESTAÇÃO DE SERVIÇO 02` com `anyoneWithLink` como leitor.

## Riscos priorizados

### Prioridade alta

- Revisar `Rapidinho: Me Conta do Seu Negócio!`, pois aparece com permissão pública tipo `writer`.
- Revisar materiais de LÓGIKA públicos dentro do Drive pessoal.
- Revisar candidatos sensíveis pessoais antes de qualquer reorganização.

### Prioridade média

- Separar lista de materiais LÓGIKA/empresa para decidir se ficam no Drive pessoal, se migram ou se são espelhados.
- Revisar ePUBs públicos com link.
- Organizar `04_PESSOAL` por subcategorias de vida pessoal.

### Prioridade baixa / operacional

- Deduplicar cursos, zips e materiais repetidos somente após validação humana.
- Organizar `ESTUDOS` como biblioteca de cursos/ebooks/mídias.
- Padronizar nomes e estrutura, sem apagar nada automaticamente.

## Entregáveis gerados

- Inventário da raiz: `drive-pessoal-root-depth1-2026-07-07.json`
- Inventários por pasta: `drive_pessoal_lotes_2026-07-07/`
- CSV consolidado: `drive-pessoal-inventory-consolidado-2026-07-07.csv`
- Resumo: `drive-pessoal-auditoria-summary-2026-07-07.json`
- Relatórios complementares: `drive_pessoal_auditoria_completa_2026-07-07/`
- CSV de duplicatas candidatas: `duplicatas_candidatas.csv`
- CSV de arquivos grandes: `arquivos_grandes_top100.csv`
- CSV de permissões achadas: `permissoes_todos_achados.csv`

## Recomendação de próximo passo

Não executar mudanças automáticas ainda. Próximo passo seguro:

1. Apresentar a lista de compartilhamentos para Jadielson aprovar correções.
2. Fechar/restringir primeiro os itens de prioridade alta, se autorizado.
3. Criar árvore-alvo de organização pessoal.
4. Separar candidatos LÓGIKA para revisão da parede-d’água.
5. Só depois iniciar organização, sem exclusões permanentes.

## Segurança

Nenhum arquivo foi excluído, movido, renomeado ou alterado durante a auditoria.

Fonte: Cofre; Google Drive via `gog` OAuth direto; arquivos de auditoria salvos em `[F2] memory/outputs/central-pessoal/`.
