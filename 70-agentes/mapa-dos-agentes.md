---
tema: mapa dos agentes do ecossistema
conteudo: funções, escopos, permissões de acesso, limites e protocolo de handoff dos agentes
nicho: ecossistema agêntico Lôh/Jadielson
setor: governança agentiva
cliente: Jadielson Davi
tipo: mapa de agentes
prioridade: máxima
atualizado_em: 2026-07-26
usar_quando: rotear tarefas, limitar contexto por agente e registrar passagem entre agentes
nao_usar_quando: como prompt completo de cada agente; usar arquivos específicos em [F2] memory/agents quando existirem
---

# Mapa dos agentes

## Regra geral de acesso
A regra não é bloquear escrita por pasta; é limitar contexto por necessidade. Cada agente pode criar/editar arquivos quando sua função exigir, mas só deve acessar o necessário, citar fontes, registrar decisões/pêndencias e preservar segurança.

Cada agente deve receber apenas o contexto necessário para sua função. `MEMORY.md`, `USER.md`, áreas pessoais, financeiro, saúde e dados sensíveis só devem ser consultados quando indispensáveis e em sessão apropriada.

| Agente | Função | Escopo | Pode acessar | Não pode acessar | Quando deve chamar LÔH | Handoff |
|---|---|---|---|---|---|---|
| LÔH / main | Orquestradora Tier 0 | Estratégia, roteamento, síntese, governança | Todo o Cofre conforme necessidade e segurança | Não expor segredos/contexto sensível | Decisões finais são com Jadielson; LÔH coordena | Registra em `80-handoffs/` |
| Jarvis | Coordenador operacional | Execução e organização transversal | Regras, mapas, projetos necessários | Dados íntimos sem necessidade | Decisão estratégica, conflito ou risco | Usar template |
| Alfred | Coordenador pessoal | Rotina, estudos, projetos pessoais | Contexto pessoal necessário | Clientes/profissional não relacionado | Impacto em empresa/ecossistema | Usar template |
| Central Pessoal | Agentes pessoais | Vida, estudos, rotina | Contexto pessoal mínimo necessário | Frentes/clientes profissionais sem relação | Tema sensível ou priorização | Usar template |
| C-Levels Lógika | Estratégia empresarial | Lógika e áreas C-level | Contextos Lógika/clientes pertinentes | Dados pessoais fora do escopo | Orçamento, cliente sensível, decisão transversal | Usar template |
| Operacionais | Execução especializada | Copy, design, dados, social, automação | Briefing e arquivos do projeto | Memória ampla/dados sensíveis | Ambiguidade, risco ou falta de briefing | Usar template |
| Especializados LÓGIKA | Apoio técnico | Análises e entregáveis | Materiais autorizados do projeto | Outros clientes/dados internos sensíveis | Decisão ou conflito de prioridade | Usar template |

## Protocolo de handoff
1. Criar arquivo em `80-handoffs/AAAA-MM-DD--assunto--agente-origem-para-destino.md`.
2. Usar `80-handoffs/template-handoff.md`.
3. Separar fatos, decisões, pendências e riscos.
4. Preencher `Pode compartilhar com` e `Não compartilhar com`.
5. Citar arquivos consultados.
