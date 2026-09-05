---
tema: mapa real da skill comunicação câmara municipal
conteudo: inventário inicial dos módulos existentes, classificação de fontes e lacunas para estruturar a skill de comunicação da Câmara Municipal de São Sebastião
nicho: ecossistema agêntico Lôh/Jadielson
setor: clientes e frentes institucionais
cliente: Câmara Municipal
tipo: mapa de skill
prioridade: alta
atualizado_em: 2026-08-14
usar_quando: planejar, revisar ou instalar a skill operacional de comunicação da Câmara Municipal
nao_usar_quando: publicar conteúdo sem validação humana ou substituir a aprovação formal da Lôh/Jadielson
---

# Mapa real da skill Comunicação Câmara

## Status

- Proposta de skill criada no Skill Workshop: `mapear-skill-comunicacao-camara-20260814-f5426daf0b`.
- Status da proposta no momento deste inventário: `pending`.
- Tentativa de aplicação em 2026-08-14: o ciclo de aprovação do Skill Workshop expirou sem decisão, portanto nada foi instalado/aplicado automaticamente.
- Este documento é um inventário preparatório no Cofre, não uma instalação de skill.

## Fontes consultadas

- `50-clientes/20-camara-municipal/README.md`
- `50-clientes/20-camara-municipal/contexto.md`
- `50-clientes/20-camara-municipal/fontes.md`
- `50-clientes/20-camara-municipal/00-indice/indice-editorial.md`
- `50-clientes/20-camara-municipal/00-indice/indice-geral-legado.md`
- `50-clientes/20-camara-municipal/20-fontes/base-legada-f1-frente/`

## Diagnóstico executivo

A frente Câmara já possui material editorial útil, mas ainda concentrado em uma base legada migrada. O conteúdo atual funciona como referência e padrão editorial, porém ainda não está separado em camadas profissionais de skill: governança, identidade, políticas, domínio, contexto, procedimentos, referências, exemplos, memória, ferramentas, validação e auditoria.

O maior risco operacional atual é exemplos antigos ou padrões emergentes serem interpretados como regra vigente. A correção feita em 2026-08-14 sobre stories neutros de sessão ordinária mostra esse risco: o padrão antigo citava projetos e requerimentos em pauta, mas Jadielson corrigiu que a pauta varia e, quando não confirmada, a comunicação deve ser neutra.

## Arquivos existentes e classificação inicial

| Arquivo | Classificação | Uso sugerido | Observação |
|---|---|---|---|
| `contexto.md` | operacional | contexto vivo da frente | contém regra nova de neutralidade em sessão sem pauta confirmada |
| `fontes.md` | operacional | rota de fontes | aponta a base legada migrada |
| `README.md` | operacional | índice da frente | define arquivos canônicos e regra de acesso |
| `00-indice/indice-editorial.md` | operacional | roteamento editorial | lista os arquivos editoriais consultáveis |
| `00-indice/indice-geral-legado.md` | operacional | inventário da base legada | útil para rastreabilidade |
| `11 - CONTEXTO EDITORIAL/TOM DE VOZ.md` | autoritativa candidata | identidade e postura editorial | deve virar módulo `01-identity` e parte de `02-policies` |
| `11 - CONTEXTO EDITORIAL/headlines.md` | procedimento/referência | criação de headlines | deve ser separado entre regra, procedimento e exemplo |
| `11 - CONTEXTO EDITORIAL/Formatos e Padrões Gerais.md` | procedimento/referência | formatos de reels, stories e conteúdos | contém exemplos que precisam de validação temporal |
| `11 - CONTEXTO EDITORIAL/Roteiros de Vídeo.md` | procedimento/referência | roteiros e locuções | deve virar SOP com bloqueios de risco |
| `12 - BANCO DE REFERENCIAS/00 - GUIA CONDENSADO.md` | referência forte | consulta rápida de DNA editorial | bom para context pack, não deve substituir políticas |
| `12 - BANCO DE REFERENCIAS/Melhores Headlines.md` | exemplificativa | calibrar estilo | exemplos não superam regra |
| `12 - BANCO DE REFERENCIAS/Melhores Legendas.md` | exemplificativa | calibrar legendas | contém casos específicos, exigir fonte vigente antes de reutilizar |
| `12 - BANCO DE REFERENCIAS/Padrões que Emergiram.md` | exemplificativa/candidata | padrões recorrentes | precisa separar assinatura editorial de regra obrigatória |
| `Camara-Municipal.md` | lacuna | sem conteúdo útil atual | contém apenas YAML |
| `Projetos de Conteúdo/CONTEXTUALIZAÇÃO DA CAMARA.md` | lacuna | futuro domínio institucional | contém apenas YAML |
| `Projetos de Conteúdo/CRIAR CALENDÁRIO EDITORIAL.md` | lacuna | futuro procedimento/calendário | contém apenas YAML |
| `Projetos de Conteúdo/DEFINIR ESTRATÉGIA DE PUBLICACAO.md` | lacuna | futura política/procedimento | contém apenas YAML |
| `Projetos de Conteúdo/PORTAL/REALIMENTAÇÃO.md` | lacuna | futuro processo do portal | contém apenas YAML |

## Regras vigentes identificadas

- A Câmara deve falar como instituição, não como vereador individual.
- Tom institucional, acessível, prático e representativo.
- Evitar juridiquês, autopromoção, campanha, personalismo e sensacionalismo.
- A Câmara debate, aprova, fiscaliza, acompanha e encaminha; não deve comunicar como se executasse obras diretamente.
- Conteúdo institucional exige validação humana antes de publicação.
- Separar Câmara, Saúde, SINDSS e vereadores individuais.
- Em sessão ordinária sem pauta confirmada, usar stories neutros e flexíveis; não afirmar projetos, requerimentos, votações, aprovações ou deliberações específicas sem confirmação.

## Contextos atuais existentes

- Frente ativa: comunicação/conteúdo da Câmara Municipal de São Sebastião.
- Base atual: `50-clientes/20-camara-municipal`.
- Fonte editorial principal ainda é a base legada migrada de `[F1] 5-Frentes/Camara-Municipal`.
- Não há pauta vigente estruturada da sessão no Cofre no momento deste inventário.

## Procedimentos existentes candidatos

- Stories de sessão.
- Stories pós-sessão.
- Reels de sessão.
- Reels com fala do presidente.
- Reels de homenagem.
- Stories de evento externo.
- Link/chamada para post.
- Legenda institucional.
- Roteiro de vídeo.
- Headline institucional.

## Lacunas para skill operacional

### 00-governance
- Falta constituição específica da skill da Câmara.
- Falta critério formal de escalonamento para temas sensíveis.

### 01-identity
- Existe material forte em `TOM DE VOZ.md`, mas precisa ser condensado em identidade ativa.

### 02-policies
- Falta política separada para fontes, aprovação, neutralidade, client-isolation e uso de exemplos.

### 03-domain
- Faltam módulos estruturados de instituição, mesa diretora, vereadores, legislatura, sessões, projetos, indicações, requerimentos, leis, eventos, calendário cívico e histórico.

### 04-context
- Falta pasta ou arquivo de contexto vigente com validade temporal: sessão de hoje, pauta da semana, campanha atual, status editorial.

### 05-procedures
- Existem procedimentos misturados em arquivos longos. Precisam virar SOPs menores e acionáveis.

### 06-references
- Faltam referências oficiais organizadas: pautas, atas, regimento, documentos e links oficiais.

### 07-examples
- Existem exemplos bons, mas ainda misturados com explicações. Devem ser separados entre aprovados, rejeitados e padrões.

### 08-memory
- Falta fluxo de memória candidata, aprovada, deprecated e archive específico da frente Câmara.

### 09-tools
- Falta registro de ferramentas permitidas e fallbacks para Câmara.

### 10-validation
- Falta quality gate explícito para factualidade, contexto, política, estilo e risco.

### 11-audit
- Falta padrão de auditoria para registrar fontes, limitações, confiança e persistência.

### 12-output
- `30-entregas/` está citado como destino canônico, mas a estrutura ainda não aparece criada no inventário de diretórios lidos.

## Próximo passo recomendado

1. Aplicar formalmente no Skill Workshop a proposta `mapear-skill-comunicacao-camara-20260814-f5426daf0b`.
2. Criar a skill operacional `comunicacao-camara-municipal` somente depois da aprovação do mapa.
3. Na skill operacional, priorizar primeiro estes SOPs:
   - sequência neutra de stories de sessão ordinária;
   - legenda institucional de sessão;
   - chamada de WhatsApp;
   - cobertura de sessão;
   - checagem de pauta antes de afirmar deliberações.
4. Separar exemplos antigos para `07-examples`, sem autoridade normativa.
5. Criar context pack mínimo para `sessao-ordinaria` com: contexto vigente, regras editoriais, pauta confirmada quando houver, restrições e validação final.

## Observação de governança

Este mapa foi criado como preparação e auditoria. Ele não instala nem altera a skill ativa. Mudanças estruturais de skill devem ser aprovadas por Jadielson/Lôh e aplicadas via Skill Workshop.
