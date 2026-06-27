# Arquitetura — Leads no Notion + Make.com

> Decisão de Jadielson: os leads devem ir para uma database no Notion já existente. Make.com será usado como camada de automação.

## Recomendação da Lôh

Usar **uma database principal de Leads/Clientes** no Notion como fonte operacional única para o comercial.

O Make.com não deve criar bases paralelas sem necessidade. Ele deve funcionar como **ponte/integrador**, levando dados para a database oficial e atualizando status conforme o funil avança.

## Por que evitar várias databases no início

Várias bases logo no começo tendem a gerar:

- lead duplicado;
- perda de histórico;
- confusão sobre onde atualizar status;
- automações mais frágeis;
- relatórios inconsistentes;
- dificuldade para a Lôh/CRO acompanharem o funil.

## Arquitetura recomendada — versão simples

### Database principal
**Leads/Clientes — LÓGIKA**

### Make.com
Função: capturar, transformar, enviar e atualizar informações.

### OpenClaw / Lôh / CRO
Função: analisar, sugerir resposta, preparar follow-up, orientar proposta e registrar decisões no Cofre.

## Fluxo sugerido

1. Lead chega por WhatsApp, Instagram, formulário, indicação ou captura manual.
2. Make.com recebe ou é acionado.
3. Make.com cria/atualiza item na database de Leads/Clientes no Notion.
4. Lôh/CRO recebem contexto e ajudam na triagem.
5. Status do lead avança no Notion.
6. Proposta é criada com base no tipo de serviço.
7. Follow-up é controlado por status/data.

## Campos mínimos recomendados para a database de leads

- **Nome**
- **Empresa/Instituição**
- **Contato**
- **Canal de origem**: WhatsApp, Instagram, indicação, site, evento, manual
- **Tipo de cliente**: comércio local, instituição pública, profissional liberal, empresa privada, outro
- **Interesse principal**: social media, vídeo, site, tráfego, automação, IA, pacote 360, outro
- **Status comercial**: novo, qualificar, contato feito, reunião marcada, proposta enviada, follow-up, fechado, perdido, stand-by
- **Temperatura**: frio, morno, quente
- **Responsável**
- **Data de entrada**
- **Próximo follow-up**
- **Valor estimado**
- **Observações**
- **Link da proposta**
- **Origem Make/OpenClaw/manual**

## Quando criar mais de uma database

Criar bases separadas apenas quando houver necessidade clara:

### Base principal
- Leads/Clientes

### Bases auxiliares possíveis no futuro
- Propostas
- Projetos/Produção
- Contratos
- Financeiro
- Conteúdos/Calendário editorial

A regra é: **lead começa em Leads/Clientes; depois se relaciona com proposta/projeto se avançar.**

## Database Notion já mapeada no Cofre

Foi encontrado no Cofre o registro de uma database:

- **Produção & Agenda — LÓGIKA**
- ID: `375207e6-f145-8111-bba0-e132fd820542`
- Uso descrito: agenda operacional, eventos e produção de conteúdo.

Também há uma base:

- **📥 Captura Geral**
- ID: `242f2506-a972-451d-8020-9bd593bdb006`
- Uso provável: entrada rápida de tarefas, compromissos, capturas e ideias.

## Recomendação sobre a base atual

Não recomendo misturar leads comerciais dentro da database **Produção & Agenda — LÓGIKA**, porque ela parece voltada a produção/editorial/eventos.

Opções:

1. **Se já existe uma database específica de leads/clientes:** usar essa como oficial.
2. **Se não existe:** criar uma database nova chamada **Leads & Clientes — LÓGIKA**.
3. **Se quiser começar sem criar nova:** usar temporariamente a **📥 Captura Geral**, mas apenas como inbox, não como CRM definitivo.

## Próxima decisão necessária

Jadielson precisa confirmar qual é a database atual de leads/clientes no Notion ou enviar o link/nome dela.

Com isso, a Lôh pode mapear os campos e preparar o desenho do primeiro cenário Make.com.
