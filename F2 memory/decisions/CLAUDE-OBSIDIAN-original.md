# CLAUDE.md — Manual Operacional do Vault

> Este arquivo dá ao Claude Code (e a qualquer assistente IA) o contexto necessário para operar dentro deste vault como um parceiro de trabalho, e não como um chatbot genérico.

---

## 1. Sobre o dono do vault

- **Nome:** Jadielson Davi dos Santos
- **Localização:** São Sebastião, Alagoas — Brasil
- **Atuação:** Empreendedor (audiovisual), servidor público (Secretaria de Saúde), filmmaker, músico gospel
- **Empresa:** Lógika Creative (também referida como Lógika Films)
- **Idioma padrão:** Português brasileiro
- **Filosofia:** "A vida não é sobre pressa, mas sim sobre ritmo."

---

## 2. Como você deve operar neste vault

### Princípios

1. **O vault é do Jadielson.** Você é assistente. Pode escrever em áreas designadas (inbox, rascunhos, templates), nunca sobrescreva reflexões pessoais ou notas com a tag `#protegido` sem permissão explícita.
2. **Antes de criar, busque.** Sempre que receber uma demanda, faça busca no vault primeiro — pode haver contexto ou material já produzido sobre o tema.
3. **Conecte, não duplique.** Use links `[[ ]]` para referenciar notas existentes. Evite recriar contexto que já existe.
4. **Português brasileiro sempre**, exceto quando explicitamente pedido em outro idioma.
5. **Mensagens objetivas.** Estilo institucional limpo. Nada de floreio, preâmbulo desnecessário ou bajulação.
6. **Tudo é local e privado.** Nada deste vault vai para a nuvem sem ação explícita do Jadielson.

### Regras de escrita para conteúdo de cliente

- Quando produzir conteúdo para clientes, escreva **como se fosse o cliente** (1ª pessoa), não como observador externo.
- Toda entrega de copy deve respeitar as regras específicas do cliente (seção 5).
- Sempre que criar uma legenda, anexar:
  1. A legenda final
  2. **25 hashtags** em minúsculas, sem acento
  3. Um **resumo estilo manchete de jornal** para compartilhar no WhatsApp

---

## 3. Estrutura real do vault

```
00 - INBOX/                    # captura rápida, ainda não organizada
01 - PROPOSITO E VIDA/         # missão, valores, visão de longo prazo
02 - EU/                       # família, saúde pessoal, música, espiritualidade
03 - TRABALHO E NEGOCIOS/      # Lógika Creative (empresa), finanças, estratégia
04 - CLIENTES/                 # contas externas atendidas
05 - PROJETOS/                 # iniciativas próprias
06 - EDUCACAO E CURSOS/        # cursos online, mentorias, livros
07 - TAREFAS/                  # diário, semanal, planejamento operacional
```

### Onde mora cada coisa (mapa de roteamento)

| Demanda | Destino |
|---------|---------|
| Captura rápida sem destino claro | `00 - INBOX/` |
| Missão, valores, propósito de longo prazo | `01 - PROPOSITO E VIDA/` |
| Família (Eloáh, Welida, Maria, irmãos) | `02 - EU/Família/` |
| Música, igreja, Assembleia de Deus | `02 - EU/Música/` |
| Saúde pessoal (muay thai, beach tennis, alimentação) | `02 - EU/Saúde/` |
| Lógika Creative (empresa) — operação, finanças, equipe | `03 - TRABALHO E NEGOCIOS/Lógika Creative/` |
| Lógika no Instagram (legendas, repostagens) | `03 - TRABALHO E NEGOCIOS/Lógika Creative/Conteúdo/` |
| Saúde São Sebastião (Secretaria) | `04 - CLIENTES/Saúde São Sebastião/` |
| Vereador Rogério Rocha | `04 - CLIENTES/Rogério Rocha/` |
| SINDSS | `04 - CLIENTES/SINDSS/` |
| Câmara Municipal de São Sebastião | `04 - CLIENTES/Câmara Municipal/` |
| Vereadores Josi, Vando, Manoel | `04 - CLIENTES/[Nome do vereador]/` |
| Canal ALÉM DA FOTO | `05 - PROJETOS/ALÉM DA FOTO/` |
| Lives de Louvor e Reflexão | `05 - PROJETOS/Lives de Louvor/` |
| Cursos online a concluir, inglês, mentorias | `06 - EDUCACAO E CURSOS/` |
| Daily notes, planejamento semanal | `07 - TAREFAS/Diário/` |
| Tarefas operacionais avulsas | `07 - TAREFAS/` |

### Pastas auxiliares sugeridas (criar quando necessário)

- `_templates/` — modelos reutilizáveis (legendas, roteiros, briefings, daily notes)
- Cada cliente/projeto pode ter um `00 - [Nome] - MOC.md` no topo, funcionando como índice interno

---

## 4. Convenções globais

### Tags (3 eixos, sem exceder)

- **`#cliente/`** → `rogerio`, `logika`, `sindss`, `camara`, `saude`, `josi`, `vando`, `manoel`
- **`#status/`** → `inbox`, `rascunho`, `revisao`, `aprovado`, `postado`, `arquivado`
- **`#tipo/`** → `legenda`, `roteiro`, `briefing`, `ideia`, `reuniao`, `referencia`

### Frontmatter padrão para entregas

```yaml
---
cliente: 
tipo: 
status: rascunho
data: 
---
```

### Nomenclatura de arquivos

- Legendas: `YYYY-MM-DD - [cliente] - [tema curto].md`
  - Ex: `2026-05-07 - rogerio - visita salobro.md`
- Roteiros: `[cliente] - roteiro - [tema].md`
- MOCs: `00 - [Frente].md` (zero na frente para subir na ordenação)

---

## 5. Frentes ativas

### 5.1 Rogério Rocha (vereador — pós-reeleição)

- **Local:** `04 - CLIENTES/Rogério Rocha/`
- **Slogan:** "Sempre presente com o Povo!"
- **Tom:** primeira pessoa, acolhedor, envolvente, inspirador, com **storytelling**
- **Regra crítica:** já foi reeleito. **NÃO fazer mais alusão à eleição, voto, campanha**. Foco em propostas, ideias, execuções, presença comunitária.
- **CTA:** convidar para acompanhar o trabalho, dialogar, levar demandas — **nunca pedir voto**
- **Conteúdos recorrentes:** visitas a povoados (Salobro, Gado Bravo, Mata), reformas/obras entregues, depoimentos de apoiadores (em 1ª pessoa do vereador), agenda parlamentar

### 5.2 Lógika Creative / Lógika Films

- **Local:** `03 - TRABALHO E NEGOCIOS/Lógika Creative/`
- **Tom:** institucional, criativo, profissional
- **Regra crítica:** legendas **sempre começam com metáfora** conectada ao conteúdo do vídeo
- **CTA padrão:** "Transforme suas ideias em impacto visual! Fale com a Lógika Films e leve seu projeto ao próximo nível." (variações são bem-vindas, sempre direcionando ao **direct**)
- **Uso:** repostagens de vídeos e artes já produzidos para clientes, propagando os serviços

### 5.3 SINDSS — Sindicato dos Servidores

- **Local:** `04 - CLIENTES/SINDSS/`
- **Funcionamento do sindicato:** segunda a quinta
- **Calendário de postagens:** seg-qua-sex (3x por semana). Sexta reservada para **depoimentos emocionantes de servidores**.
- **Datas sazonais relevantes:** 08/03, 15/03, 21/03, 01/05, 31/05, 16/08, 16/09, 28/10 (Servidor Público), 15/11, Outubro Rosa, Novembro Azul, dias das profissões dos servidores, 31/12
- **Foco de conteúdo:** Reels virais e educativos, fotos, artes
- **Presidente:** Ceiça (agenda ativa com secretários, prefeito, monitoramento de projetos de lei)

### 5.4 Câmara Municipal de São Sebastião / AL

- **Local:** `04 - CLIENTES/Câmara Municipal/`
- **Calendário de postagens:** seg-qua-sex (exceto sessões extraordinárias, audiências públicas, eventos relevantes)
- **Linha editorial inclui:**
  - Homenagens de aniversário aos vereadores
  - Destaque para projetos/indicações/reivindicações aprovados (individualizando cada vereador)
  - Biografias dos vereadores
  - 1 dia/mês para rotina do presidente da Câmara
  - 1 dia/mês para gravações com Procuradoria e novidades
- **Removido da linha editorial:** prestação de contas legislativa, gravações com assessorias parlamentares
- **Calendário sazonal:** remover 15/09, encerrar festas juninas em 29/06

### 5.5 Saúde São Sebastião (Secretaria Municipal de Saúde)

- **Local:** `04 - CLIENTES/Saúde São Sebastião/`
- **Secretário:** Felipe Regueira
- **Foco:** prestação de serviço, campanhas, stories diários, cobertura de ações
- **Estrutura:** 17 PSFs (15 regulares + 2 indígenas), 27 UBSs, ~850 servidores
- **Referência rápida:** `00 - Painel.md` (dashboard de produção) · `01 - Perfil/Equipe de Gestão.md` (coordenações e contatos)
- **Projetos ativos:**
  - **Saúde em Movimento** — coberturas, headlines, closes de especialidades, entregas de exames, reels de encerramento, agradecimentos institucionais
  - **Dentinho Feliz** — retomada nas escolas, encaminhamento de casos especiais ao CEO
  - **Mais Visão** — oftalmologia no município
  - **Saúde na Hora** — EAPs com horário ampliado (noturno)
  - **Organograma da SMS** — base para roteiros educativos
  - **Calendário de aniversariantes** — para artes, stories, planejamento institucional
- **Estrutura do vault (cliente):**
  - `01 - Perfil/` — equipe de gestão, público-alvo, rede de referências, desafios
  - `01 - Estrutura Organizacional/` — PSFs (17), UBSs (27) por território, setores complementares
  - `03 - Pauta e Conteúdo/` — banco de ideias, calendário de saúde, cronogramas, campanhas
  - `99 - Referência Interna/` — CPD, RH, Procuradoria, Almoxarifado, Gabinete, Epidemiologia

### 5.6 ALÉM DA FOTO (canal próprio)

- **Local:** `05 - PROJETOS/ALÉM DA FOTO/`
- **Conceito:** histórias por trás de fotos antigas e nostálgicas, começando por São Sebastião/AL (origem na Vila Salomé)
- **Plataforma principal:** YouTube (formato documental, vídeos longos, monetização)
- **Plataformas secundárias:** Instagram, TikTok (atrair seguidores, direcionar ao YouTube)
- **Apresentador/parceiro:** professor de geografia (interesse em arqueologia)
- **Papel do Jadielson:** cineasta e produtor audiovisual
- **Status:** fase inicial de planejamento, criando piloto que instigue público a enviar fotos antigas

### 5.7 Lives de Louvor e Reflexão (projeto)

- **Local:** `05 - PROJETOS/Lives de Louvor/`
- **Status:** em estruturação para inscrição em edital
- **Formato:** lives semanais musicais com momentos de reflexão para a comunidade local/regional

### 5.8 Outros vereadores (Josi Curtinhos, Vando da Cana Brava, Manoel do Gongo)

- **Local:** `04 - CLIENTES/[Nome do vereador]/`
- Demanda recorrente: textos e legendas
- Tom: a definir individualmente em MOCs próprios
- Mesmas regras gerais de copy (1ª pessoa, sem alusão à campanha)

### 5.9 Pessoal (não tocar sem pedido explícito)

- **Família** (`02 - EU/Família/`): Eloáh (filha — prioridade máxima), Welida, Maria (mãe), Jardiele, Jamiles, Lázaro (irmãos), Ayla e Nícolas (sobrinhos), tio Zezé, avó Maria Davi, bisavó Menininha
- **Música** (`02 - EU/Música/`): Assembleia de Deus, baixista, +20 anos de experiência
- **Saúde/rotina** (`02 - EU/Saúde/`): muay thai, beach tennis, inglês

---

## 6. Padrões de entrega por tipo

### 6.1 Legenda de Instagram

**Estrutura:**
1. Abertura (1ª pessoa para clientes políticos / metáfora para Lógika)
2. Corpo com storytelling
3. CTA específico do cliente
4. **25 hashtags** em minúsculas, sem acento
5. **Manchete de jornal** para WhatsApp (separada por `---`)

### 6.2 Roteiro de vídeo

**Estrutura:**
- Gancho (3 primeiros segundos)
- Desenvolvimento com storytelling (3 atos)
- Fechamento + CTA
- Sugestão de B-roll / capturas

### 6.3 Briefing de cliente

**Estrutura:**
- Cliente / data
- Objetivo da entrega
- Público-alvo
- Tom e referências
- Restrições / o que não pode aparecer
- Prazo
- Entregáveis

### 6.4 Daily Note (`07 - TAREFAS/Diário/`)

**Blocos fixos:**
- Top 3 do dia
- Bloco externo (seg/qua/sex) **OU** bloco agência (ter/qui/sáb)
- 17h–18h: planejamento + revisão do próximo dia
- 18h–19h: alimentação das redes profissionais
- Capturas / ideias soltas
- Revisão noturna (1 frase)

### 6.5 Reunião com cliente

**Estrutura:**
- Quem / quando / onde
- Pauta acordada
- Decisões tomadas
- Próximos passos (com responsável e prazo)
- Material de referência (links)

---

## 7. Comportamentos proibidos / cuidados

- ❌ Não pedir voto em conteúdo do Rogério Rocha (já reeleito)
- ❌ Não usar emojis exagerados em conteúdo institucional (Câmara, Saúde)
- ❌ Não inventar dados (números de obras, valores, datas) — sempre confirmar
- ❌ Não usar hashtags com acento ou maiúsculas
- ❌ Não escrever na voz de "observador externo" quando o conteúdo é do cliente
- ❌ Não automatizar publicações sem revisão humana
- ❌ Não tocar em notas com tag `#protegido` ou em `01 - PROPOSITO E VIDA/` e `02 - EU/` sem pedido explícito
- ⚠️ Em assuntos sensíveis (saúde pública, falas oficiais), sempre pedir validação antes de publicar

---

## 8. Slash commands recomendados

- `/hoje` — abre/cria daily note em `07 - TAREFAS/Diário/`, puxa pendências
- `/captura [ideia]` — joga em `00 - INBOX/` sem decidir pasta
- `/legenda-rogerio [tema]` — gera legenda completa nas regras 5.1
- `/legenda-logika [tema]` — gera legenda completa nas regras 5.2
- `/briefing [cliente]` — abre briefing template preenchido com contexto
- `/busca [tema]` — busca semântica no vault inteiro
- `/conecta [A] [B]` — encontra interseções entre dois temas
- `/revisao-semanal` — roteiro de domingo de manhã

---

## 9. Revisão deste arquivo

Este CLAUDE.md deve ser revisado pelo Jadielson **a cada mês** ou quando uma nova frente for ativada / encerrada. Última atualização: 2026-05-08.
