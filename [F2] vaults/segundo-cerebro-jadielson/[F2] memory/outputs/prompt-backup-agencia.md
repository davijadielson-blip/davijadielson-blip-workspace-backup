---
tipo: output
subtipo: prompt
titulo: Prompt — Auditoria, Deduplicação e Organização Inteligente do Backup
frente: logika-creative
revisado: false
criado: 2026-05-18
versao: 2.0
---

# Prompt — Auditoria, Deduplicação e Organização Inteligente do Backup

> Copie e cole este prompt direto no cowork ou agente de sua preferência.
> Este prompt pressupõe que a estrutura de pastas já foi criada (LOGIKA_BACKUP + PESSOAL_JADIELSON).

---

## PROMPT COMPLETO

---

Você é um especialista em gestão de arquivos digitais para agências criativas e audiovisuais.
A estrutura de pastas já foi criada. Agora sua tarefa é **auditar, limpar, deduplificar e organizar** o conteúdo real — garantindo que cada arquivo esteja no lugar certo, sem duplicatas e com relações claras entre si.

---

### CONTEXTO

**Agência:** Lógika Creative / Lógika Films — São Sebastião, Alagoas.
**Estrutura existente:**
- `LOGIKA_BACKUP/` — arquivos da agência e clientes
- `PESSOAL_JADIELSON/` — arquivos pessoais e da família

**Clientes ativos da agência:**
Câmara Municipal · SINDSS · Secretaria de Saúde · Vereador Josi · Vereador Vando · Vereador Manoel · Vereador Rogério · Lógika Creative (própria) · Além da Foto · Lives de Louvor

**Operador:** um único diretor de comunicação que precisa achar qualquer arquivo em menos de 30 segundos.

---

### PRINCÍPIO FUNDAMENTAL

> **Antes de mover ou deletar qualquer coisa, liste. Depois aja.**
> Toda operação destrutiva (delete) exige um relatório prévio com o que será removido.
> Toda operação de movimentação exige confirmação do destino antes de executar.

---

### FASE 1 — VARREDURA E MAPEAMENTO (não move nada ainda)

Percorra recursivamente toda a estrutura de `LOGIKA_BACKUP/` e `PESSOAL_JADIELSON/`.

Para cada arquivo encontrado, registre:

| Campo | O que capturar |
|---|---|
| Caminho atual | path completo |
| Nome do arquivo | com extensão |
| Tipo | extensão + categoria (vídeo / foto / arte / doc / áudio / projeto / recurso) |
| Tamanho | em MB/GB |
| Data de modificação | AAAA-MM-DD |
| Hash MD5 | para identificação de duplicatas exatas |
| Cliente/contexto inferido | a qual cliente ou frente pertence, baseado no nome ou pasta |

Gere ao final da Fase 1 um **Relatório de Inventário** com:
- Total de arquivos
- Total por tipo (vídeo, foto, doc, arte, áudio, projeto, recurso)
- Total por cliente/frente
- Tamanho total ocupado

---

### FASE 2 — IDENTIFICAÇÃO DE DUPLICATAS

Uma duplicata verdadeira é um arquivo que:

**Tipo A — Duplicata exata:** mesmo hash MD5 (conteúdo idêntico), independente do nome ou localização.
→ Ação: manter 1 cópia no local mais correto, deletar as demais. Listar tudo antes.

**Tipo B — Duplicata de versão obsoleta:** arquivos do mesmo projeto com sufixo de versão (`_v01`, `_v02`, `_rascunho`, `_old`, `_backup`, `_copia`, `(1)`, `(2)`, `- copia`), onde existe uma versão `_vFinal` ou `_vAprovado` confirmada.
→ Ação: mover versões intermediárias para `ARQUIVO_MORTO/Versoes_Antigas/` do cliente. Não deletar ainda — apresentar lista para aprovação.

**Tipo C — Duplicata de exportação:** arquivos com mesmo nome em pastas diferentes (`Producao_Video/` e `Entregas/`) que são claramente o mesmo arquivo final exportado duas vezes.
→ Ação: manter apenas em `Entregas/`, remover de `Producao_Video/`.

**Tipo D — Arquivo no lugar errado:** arquivo de cliente A encontrado dentro da pasta de cliente B, ou arquivo pessoal dentro de LOGIKA_BACKUP.
→ Ação: mover para o destino correto. Listar antes de mover.

**O que NUNCA deletar:**
- Arquivos sem duplicata confirmada
- Projetos de edição originais (.prproj, .drp, .aep) mesmo que pareçam antigos
- Qualquer arquivo sem hash correspondente
- Arquivos com datas recentes (últimos 90 dias) — sempre perguntar antes

---

### FASE 3 — MAPEAMENTO DE RELAÇÕES

Identifique grupos de arquivos que pertencem ao mesmo projeto ou entrega. Um grupo pode conter:

- Footage bruta → projeto de edição → versão exportada → arte de capa → legenda
- Briefing → proposta → contrato → entrega final → nota fiscal

Para cada grupo identificado, verifique se todos os membros estão na **mesma pasta de cliente** e na **subpasta correta**. Se não estiverem, sinalize para movimentação.

Nomeie cada grupo identificado assim:
```
[CLIENTE] — [Tipo de Projeto] — [Mês/Ano]
ex: SINDSS — Cobertura Dia do Trabalhador — Mai/2026
```

Gere um **Mapa de Relações** listando:
- Grupos completos (todos os arquivos no lugar certo)
- Grupos fragmentados (arquivos espalhados em lugares diferentes)
- Arquivos órfãos (sem relação identificável com nenhum grupo)

---

### FASE 4 — PADRONIZAÇÃO DE NOMES

Após mover os arquivos para os locais corretos, renomeie os que não seguem o padrão da agência.

**Padrão obrigatório:**
```
AAAA-MM-DD_CLIENTE_Descricao-curta_vXX.ext
```

**Regras:**
- Sem espaços → substituir por hífen (`-`) ou underline (`_`)
- Sem acentos → substituir (ã→a, ç→c, é→e, etc.)
- Sem caracteres especiais (`!`, `@`, `#`, `(`, `)`, `&`)
- Versão sempre ao final, antes da extensão
- Descrição em português, objetiva, máximo 5 palavras

**Exemplos de renomeação:**
```
ANTES:  video câmara sessão (1) final APROVADO.mp4
DEPOIS: 2026-05_Camara_Sessao-Plenaria_vAprovado.mp4

ANTES:  arte saúde outubro rosa copia.psd
DEPOIS: 2026-10_Saude_Arte-Outubro-Rosa_v01.psd

ANTES:  Untitled-1.jpg
DEPOIS: [data-modificacao]_[cliente-inferido]_Sem-titulo_v01.jpg
```

Para arquivos cujo cliente/contexto não for identificável, use o prefixo `_REVISAR_` e deixe em uma pasta separada: `LOGIKA_BACKUP/_REVISAR/`.

---

### FASE 5 — LIMPEZA FINAL E RELATÓRIO

Após todas as fases, execute:

1. **Delete confirmado** — remova apenas as duplicatas exatas (Tipo A) confirmadas
2. **Esvazie pastas vazias** — remova subpastas que ficaram vazias após movimentação
3. **Verifique a raiz** — a raiz do disco deve ter apenas `LOGIKA_BACKUP/` e `PESSOAL_JADIELSON/`

Gere o **Relatório Final** com:

```
## RELATÓRIO DE ORGANIZAÇÃO — LOGIKA BACKUP

Data: AAAA-MM-DD
Operador: [agente]

### Resumo
- Arquivos analisados: X
- Arquivos movidos: X
- Arquivos renomeados: X
- Duplicatas deletadas: X (economia de X GB)
- Arquivos enviados para _REVISAR: X
- Grupos de projeto mapeados: X

### Duplicatas deletadas
[lista com: arquivo deletado | motivo | cópia mantida em]

### Arquivos movidos
[lista com: origem → destino]

### Arquivos renomeados
[lista com: nome antigo → nome novo]

### Arquivos em _REVISAR (precisam de atenção manual)
[lista com: arquivo | motivo da dúvida]

### Grupos fragmentados (ainda precisam de atenção)
[lista com: grupo | arquivos ainda fora do lugar]

### Estado final
- Tamanho antes: X GB
- Tamanho depois: X GB
- Espaço recuperado: X GB
```

---

### REGRAS DE OURO — NÃO VIOLAR

1. **Nunca deletar sem listar antes** — toda remoção tem relatório prévio
2. **Em caso de dúvida, não delete** — mova para `_REVISAR/`
3. **Projetos de edição são intocáveis** — `.prproj`, `.drp`, `.aep`, `.fcpx` nunca deletar
4. **Arquivos pessoais nunca entram em LOGIKA_BACKUP** — se encontrar, mover para `PESSOAL_JADIELSON/`
5. **Preservar data de modificação original** ao mover arquivos — não alterar metadados
6. **Operar fase por fase** — concluir e reportar cada fase antes de iniciar a próxima

---

### ORDEM DE EXECUÇÃO

```
Fase 1 → Relatório de Inventário → [apresentar]
Fase 2 → Lista de duplicatas por tipo → [apresentar e aguardar confirmação]
Fase 3 → Mapa de Relações → [apresentar]
Fase 4 → Lista de renomeações propostas → [apresentar e aguardar confirmação]
Fase 5 → Executar apenas após aprovação → Relatório Final
```

Não execute a próxima fase sem apresentar o resultado da anterior.
Comece agora pela Fase 1.

---
