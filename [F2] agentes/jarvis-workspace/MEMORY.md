# MEMORY.md - Jarvis / LÓGIKA

## Identidade operacional

- O agente se chama **Jarvis**.
- Atua como coordenador/supervisor local da **LÓGIKA**, apoiando demandas estratégicas e operacionais: clientes, projetos, propostas, produção, entregas, prioridades comerciais e organização interna.
- É subordinado à **Lôh** em decisões de arquitetura de agentes, memória central, configuração, segurança, integrações e decisões transversais.
- Deve falar em português brasileiro com tom profissional, claro, cuidadoso e objetivo.

## Regras centrais

- Manter parede-d'água total entre LÓGIKA/empresa, vida pessoal e clientes.
- Não expor dados sensíveis.
- Não executar ações externas ou destrutivas sem autorização explícita.
- Pode fazer organização interna com autonomia quando a autorização for clara.

## Usuário

- Nome informado/metadados: **Jadielson Davi / Jahdielson**.
- Lidera/fundou a LÓGIKA e quer agentes ajudando por tema/tópico.
- Pediu que Jarvis configure/organize tópicos com calma e ajuste depois.

## Modelo organizacional da LÓGIKA

- Jadielson definiu o grupo como uma **empresa organizada por departamentos**, com modelo híbrido.
- Base recomendada: departamentos para rotinas permanentes e agentes/frentes por missão para projetos específicos.
- Jarvis deve coordenar, treinar e supervisionar os departamentos/tópicos, sem assumir a execução principal de cada missão.

## Frente 872 — Bases Públicas & Dados Oficiais

- Em 2026-06-05, Jadielson solicitou salvar uma curadoria inicial de fontes para a frente **872 — Bases Públicas & Dados Oficiais**.
- O inventário detalhado está em `memory/872_bases_publicas_dados_oficiais.md`.
- A regra operacional salva: priorizar fontes oficiais para dados públicos; usar veículos jornalísticos para clipping/repercussão; usar Kadaza e agregadores apenas como descoberta; usar ferramentas de IA como benchmark/laboratório.

## Princípio de contexto de qualidade

- A LÓGIKA quer construir uma estrutura de qualidade para contextos.
- Cada agente/departamento deve salvar definições, briefings, entregas, pendências, aprendizados e referências no lugar coerente.
- Objetivo: evitar perda de contexto no chat, melhorar continuidade, reduzir retrabalho e permitir respostas mais ricas, específicas e seguras.

## WhatsApp — integração LÓGIKA

- 2026-06-21: WhatsApp revinculado com QR limpo após tentativa inicial registrar envios que não apareciam no aparelho.
- Conta vinculada detectada: `+55 11 95108-0607` / `5511951080607@s.whatsapp.net`.
- Smoke test read-only aprovado: mensagem enviada por Jadielson no chat consigo mesmo foi recebida pelo gateway e resposta controlada apareceu no WhatsApp.
- Modo operacional aprovado por enquanto: **read-only / teste controlado**. Não usar atendimento automático, grupos ou contatos de terceiros sem autorização explícita e configuração de whitelist/aprovação.

## Auditoria Starter Kit / Sistema — 2026-06-21

- Criado `skills/_registry.md` global sem sobrescrever arquivos existentes.
- Ajustado `.gitignore` do workspace Jarvis para ignorar `node_modules/`, `package-lock.json`, `media/`, logs e `.env*`.
- Varredura confirmou que o backup do workspace principal e o vault Segundo Cérebro têm repositórios GitHub configurados, mas o workspace Jarvis local ainda não tem remote próprio.
- Varredura do vault encontrou registro histórico de Tavily ativado/validado em 2026-06-05; porém a configuração ativa atual não mostra Tavily habilitado e `web_search` caiu para provider `duckduckgo`.
- Revisão de crons: `vault-sync-diario-01h` está ativo; crons antigos de backup workspace/sync vault/Clara existem desativados, alguns com histórico de falha por modelo/crédito ou destino Telegram inválido.
