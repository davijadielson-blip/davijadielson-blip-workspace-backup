---
tema: prompts para calendarios editoriais de setembro 2026
conteudo: comandos para subagentes de Saude Sao Sebastiao, Camara Municipal e SINDSS criarem calendarios editoriais de setembro considerando limites de rotina, captacao seletiva e equilibrio vida-familia-empresa
setor: processos editoriais e planejamento mensal
cliente: Jadielson Davi
tipo: template de prompt
prioridade: alta
atualizado_em: 2026-08-30
usar_quando: solicitar aos subagentes de clientes institucionais a criacao de calendarios editoriais mensais
nao_usar_quando: publicar calendarios sem validacao humana ou ignorar compromissos reais do mes
---

# Prompts - Calendarios Editoriais de Setembro 2026

## Contexto comum para todos os subagentes

Setembro de 2026 começa em uma terça-feira e termina em uma quarta-feira.

Diretriz de rotina:

- Jadielson se considera matutino; a manhã e o melhor período para clareza, criatividade, estudo, estratégia e decisões.
- Ainda assim, algumas demandas institucionais acontecem pela manhã e devem ser respeitadas quando forem realmente inadiáveis.
- A rotina precisa equilibrar: eu, família, LÓGIKA/empresa e clientes.
- Cliente pago tem direito a entrega consistente, mas não a disponibilidade 100 por cento.
- Captações devem ser seletivas, em lote quando possível, e alinhadas ao calendário editorial.
- Não transformar toda demanda em urgência.
- Separar:
  - o que precisa ser captado pela manhã;
  - o que pode ser captado à tarde;
  - o que pode ser captado em lote;
  - o que pode ser produzido com banco de imagens, material já existente ou peça educativa.

## Prompt para subagente da Saúde

Preciso que você monte o calendário editorial de setembro de 2026 para a Secretaria Municipal de Saúde de São Sebastião/AL.

Antes de montar, consulte obrigatoriamente o Cofre da frente Saúde:

- `50-clientes/10-saude-sao-sebastiao/contexto.md`
- `50-clientes/10-saude-sao-sebastiao/00-indice/indice-editorial.md`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/`
- `50-clientes/10-saude-sao-sebastiao/10-contexto/memoria-operacional-f2/03-editorial/estrategia-v3-completa-feed-stories-lives.md`
- `50-clientes/10-saude-sao-sebastiao/pendencias.md`
- skill `saude-sao-sebastiao-comunicacao`

Leve em consideração:

- Setembro Amarelo deve entrar como eixo transversal, com linguagem responsável, sem sensacionalismo e sem prometer atendimento sem fonte.
- Seguir os pilares editoriais da Saúde:
  1. Atenção Básica / Território
  2. Serviços Especializados / Diagnóstico
  3. Vigilância / Prevenção
  4. Rede de Apoio / Humanização
  5. Urgência / Serviço
  6. Bastidores / Prestação de Contas
  7. Campanhas Mensais / Datas de Saúde
- Manter rotação de segunda a sexta, alternando Urgência/Serviço e Bastidores/Prestação de Contas para não prender sempre o mesmo pilar ao mesmo dia.
- Stories devem variar dentro do pilar do dia, sem repetir o mesmo setor/personagem em todas as telas.
- Boa parte das ações e eventos da Saúde acontece pela manhã, mas Jadielson não deve ficar 100 por cento disponível para a Secretaria.
- Diferenciar no calendário:
  - captação obrigatória pela manhã;
  - captação possível à tarde;
  - captação em lote;
  - conteúdo que pode ser feito com banco/material existente;
  - conteúdo educativo sem captação.
- O calendário editorial deve conduzir a produção, não ser refém de evento aleatório.
- Quando houver necessidade de dado local, agenda, serviço, horário, número, profissional, paciente ou local, marcar `[A CONFIRMAR]`.
- Respeitar LGPD, imagem de pacientes, dados sensíveis e validação humana antes de publicação.

Entregue:

1. Visão estratégica de setembro.
2. Calendário por semana e por dia útil, de 01/09 a 30/09.
3. Para cada dia: pilar, formato principal, pauta, objetivo, necessidade de captação e observações.
4. Lista de captações em lote recomendadas para o mês.
5. Lista de pautas que precisam obrigatoriamente de manhã.
6. Lista de pautas que podem ser captadas à tarde.
7. Checklist de validação humana antes da publicação.
8. Caminho sugerido para salvar o calendário no Cofre, com YAML frontmatter.

## Prompt para subagente do SINDSS

Preciso que você monte o calendário editorial de setembro de 2026 para o SINDSS.

Antes de montar, consulte obrigatoriamente o Cofre da frente SINDSS:

- `50-clientes/30-sindss/contexto.md`
- `50-clientes/30-sindss/00-indice/indice-editorial.md`
- `50-clientes/30-sindss/30-entregas/outputs/2026-08-27-calendario-sazonal-anual-sindss.md`
- `50-clientes/30-sindss/pendencias.md`
- base editorial legada quando necessário: `50-clientes/30-sindss/20-fontes/base-legada-f1-frente/`

Leve em consideração:

- O SINDSS funciona de segunda a quinta até 14h, mas a rotina depende muito dos horários da presidente Ceiça.
- Jadielson não pode ficar em plantão permanente para o sindicato.
- O calendário deve prever produção leve, objetiva e possível de cumprir.
- Priorizar comunicação sindical, valorização do servidor, direitos, cidadania, serviço público, saúde do trabalhador e atuação institucional.
- Setembro tem datas fortes para SINDSS:
  - 07/09 - Independência do Brasil
  - 08/09 - Nossa Senhora da Penha, se for tratada como tradição/cultura local
  - 09/09 - Dia do Administrador
  - 16/09 - Emancipação Política de Alagoas
  - 21/09 - Dia Nacional de Luta da Pessoa com Deficiência
  - 23/09 - Dia do Agente de Trânsito
  - 25/09 - Dia Nacional do Trânsito, opcional
  - 30/09 - Dia da Secretária
  - Setembro Amarelo
- Datas de categoria só devem virar homenagem se fizerem sentido para servidores representados no município ou se houver gancho local.
- Se houver assembleia, campanha salarial, pauta jurídica, negociação, conflito ou reunião importante, isso tem prioridade sobre data sazonal.
- Usar a presidente Ceiça como representante institucional, não como personalismo excessivo.

Entregue:

1. Visão estratégica de setembro para o SINDSS.
2. Calendário recomendado com frequência realista.
3. Classificação das pautas em obrigatórias, recomendadas e opcionais.
4. Sugestão de janelas de produção para Jadielson, sem exigir disponibilidade total.
5. Lista do que depende da presidente Ceiça.
6. Lista de peças que podem ser produzidas em lote.
7. Checklist de validação humana antes da publicação.
8. Caminho sugerido para salvar o calendário no Cofre, com YAML frontmatter.

## Prompt para subagente da Câmara

Preciso que você monte o calendário editorial de setembro de 2026 para a Câmara Municipal de São Sebastião/AL.

Antes de montar, consulte obrigatoriamente o Cofre da frente Câmara:

- `50-clientes/20-camara-municipal/contexto.md`
- `50-clientes/20-camara-municipal/00-indice/indice-editorial.md`
- `50-clientes/20-camara-municipal/30-entregas/outputs/2026-08-26-calendario-sazonal-anual-camara.md`
- `50-clientes/20-camara-municipal/pendencias.md`
- base editorial legada quando necessário: `50-clientes/20-camara-municipal/20-fontes/base-legada-f1-frente/`

Leve em consideração:

- O maior compromisso operacional da Câmara é na sexta à tarde, quando há sessão ordinária.
- Fora da sexta, a Câmara deve exigir apenas preparação curta, pauta, checagem, artes sazonais e demandas pontuais.
- Em stories de sessão ordinária, manter abordagem neutra quando a pauta não estiver confirmada.
- Não afirmar previamente projetos, votações, requerimentos ou deliberações sem validação.
- Setembro tem datas fortes para Câmara:
  - 07/09 - Independência do Brasil, obrigatória
  - 08/09 - Nossa Senhora da Penha, com cuidado cultural/institucional
  - 16/09 - Emancipação Política de Alagoas, obrigatória
  - 16/09 - aniversário de José Denivaldo Rodrigues Oliveira, Dé do Campo
  - 27/09 - aniversário de Francisco Euzébio dos Santos
  - 27/09 - aniversário de Rosival Antônio dos Santos
  - Setembro Amarelo, recomendada com linguagem responsável
- Datas religiosas devem ser tratadas como tradição, cultura, identidade local e respeito, sem texto devocional.
- Campanhas mensais entram como apoio, sem transformar o perfil da Câmara em calendário genérico.

Entregue:

1. Visão estratégica de setembro para a Câmara.
2. Calendário por semana, incluindo sessões ordinárias quando houver.
3. Peças sazonais obrigatórias e recomendadas.
4. Pautas de sessão: pré-sessão, cobertura, pós-sessão e reaproveitamento.
5. Lista do que depende de confirmação da Câmara.
6. Lista de peças que podem ser produzidas em lote.
7. Sugestão de rotina para Jadielson não deixar a Câmara invadir a semana inteira.
8. Checklist de validação humana antes da publicação.
9. Caminho sugerido para salvar o calendário no Cofre, com YAML frontmatter.
