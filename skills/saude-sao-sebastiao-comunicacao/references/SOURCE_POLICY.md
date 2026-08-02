---
tema: politica de fontes da saude
conteudo: referencia operacional da skill saude-sao-sebastiao-comunicacao
setor: saude e comunicacao institucional
cliente: Secretaria Municipal de Saude de Sao Sebastiao
tipo: referencia de skill
prioridade: alta
atualizado_em: 2026-07-31
usar_quando: usar a skill saude-sao-sebastiao-comunicacao em demandas da Saude
nao_usar_quando: demandas fora da frente Saude Sao Sebastiao
---

# Política de fontes, pesquisa e atualização

## Princípio central

O contexto consolidado vem do cofre. Os documentos-fonte desta skill podem estar no cofre ou no Drive profissional. O Drive pessoal não pertence ao escopo da Saúde. Orientação técnica vem de fonte oficial. Benchmarking vem de instituições públicas, mas nunca substitui a voz de São Sebastião.

## Fontes internas autorizadas

### Cofre/workspace

- Função: índice canônico, memória institucional, regras, decisões, sínteses e aprendizados.
- Prioridade: primeira consulta em toda demanda da Saúde.
- Caminho operacional: `/data/.openclaw/workspace/50-clientes/10-saude-sao-sebastiao/10-contexto/operacional`.

### Drive profissional

- Conta: `logikacreative.mkt@gmail.com`.
- Função: documentos profissionais, planilhas, relatórios, roteiros, materiais de produção e arquivos oficiais ou aprovados.
- Prioridade: primeira fonte remota para localizar arquivos de trabalho.

## Reconciliação entre fontes internas

1. Confirme tema, autoria, status e data de modificação.
2. Prefira `final`, `aprovado`, `publicado` e `oficial` a `rascunho`, `teste` ou cópia sem status.
3. Prefira a versão aprovada mais recente, não simplesmente o arquivo modificado por último.
4. Use o cofre para consultar a decisão consolidada após a verificação. Para novo registro durável, proponha o destino canônico e grave apenas com autorização explícita de Jadielson ou rotina canônica já aprovada.
5. Em conflito relevante, não publique por conta própria: apresente a divergência e use `[A CONFIRMAR]`.
6. Não use o Drive pessoal como rota de contingência nesta skill.

## Fontes por tipo de informação

### Fato local

Use:

- agenda;
- relatório;
- briefing;
- mensagem confirmada;
- planilha;
- documento;
- arquivo operacional;
- informação explícita do usuário.

Não use a internet para descobrir número de atendimentos, nome de profissional, data ou local de uma ação municipal.

### Orientação de saúde

Priorize:

1. Ministério da Saúde;
2. Anvisa;
3. Fiocruz;
4. secretaria estadual de Saúde;
5. OPAS/OMS;
6. diretriz clínica ou artigo científico primário.

### Comunicação pública

Priorize:

- Lei nº 15.263/2025, Política Nacional de Linguagem Simples;
- guias oficiais de linguagem simples;
- manuais de comunicação pública;
- guias oficiais de redes sociais;
- materiais de acessibilidade digital;
- portais oficiais de prefeituras e secretarias.

### Benchmarking municipal

Rotacione referências para evitar copiar um único estilo:

- Maceió;
- Fortaleza;
- Recife;
- Aracaju;
- Curitiba;
- secretarias estaduais;
- Ministério da Saúde.

Compare apenas conteúdo recente e oficial.

## Checklist de confiabilidade

- O domínio é oficial?
- A página identifica o órgão responsável?
- Há data de publicação ou atualização?
- A orientação ainda está vigente?
- A fonte fala do mesmo público e contexto?
- O texto distingue recomendação de obrigação?
- Há conflito entre fontes?
- O dado local está confirmado no cofre?

## Pesquisa com Tavily

### Busca técnica

Use consulta específica, incluindo tema, população e órgão.

Exemplo de intenção:

`Ministério da Saúde avaliação do pé diabético periodicidade atenção primária`

Parâmetros preferidos:

- `search_depth: advanced`;
- `max_results: 8`;
- `include_domains` com fontes oficiais;
- `include_answer: false` quando a finalidade for verificação.

Depois, use `tavily_extract` nas melhores páginas.

### Benchmarking

Busque:

- tema;
- tipo de conteúdo;
- secretaria/prefeitura;
- benefício ao cidadão;
- período recente.

Exemplo de intenção:

`secretaria municipal de saúde atendimento especializado amplia acesso prefeitura`

Analise:

- como a manchete começa;
- em que momento aparece o benefício;
- como informa acesso;
- presença ou ausência de autoridade;
- tamanho;
- CTA;
- clareza;
- palavras repetidas.

### Registro da pesquisa

Quando houver autorização explícita de Jadielson, registre no arquivo operacional apropriado:

- data;
- tema;
- pergunta;
- fontes consultadas;
- síntese;
- aplicação local;
- pontos não confirmados.

## Atualização do padrão

O agente pode sugerir atualização quando:

- três ou mais aprovações revelarem um padrão;
- uma rejeição corrigir uma regra importante;
- houver mudança oficial de slogan, hashtag, serviço ou estratégia;
- nova orientação legal ou sanitária afetar a comunicação.

A alteração deve ser proposta, revisada e aprovada. Não reescreva a skill em silêncio.

## Segurança editorial

- Não publique diagnóstico individual.
- Não exponha dados pessoais de pacientes.
- Não use imagem ou relato sensível sem autorização e contexto adequado.
- Não transforme pesquisa externa em prescrição médica.
- Não repita desinformação de forma chamativa.
- Em assunto controverso, explique a evidência e cite o órgão oficial.
