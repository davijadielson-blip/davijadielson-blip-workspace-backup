# INTEGRACOES-MCP-REDES.md — Auditoria e regras de uso

Data: 2026-06-05
Responsável operacional: Tópico `871 — Redes Sociais & Métricas`
Coordenação: Jarvis
Supervisão técnica/segurança: Lôh

## Decisão operacional

As integrações sociais via Zapier/MCP ficam sob responsabilidade operacional do tópico **Redes Sociais & Métricas**.

Esse tópico atua em modo padrão de **leitura, análise e monitoramento**. Qualquer ação de publicação, edição, resposta, alteração de perfil/campanha ou requisição mutável exige autorização explícita de Jadielson e, se envolver configuração/segurança, validação da Lôh.

## Auditoria de acessos disponíveis

### MCP dedicado YouTube — `zapier-youtube`

App disponível:
- YouTube

Ações de leitura/análise:
- Find Video — buscar vídeos por termo, canal, ordem, região, idioma, duração etc.
- Get Report — gerar relatórios analíticos por período, métricas e tipo de relatório.
- Make API GET Request — chamada GET para endpoints conhecidos do YouTube via Zapier.

Ações sensíveis / não usar sem autorização explícita:
- Add Video to Playlist.
- Upload Video.
- Update Video Thumbnail.
- Make API Mutating Request.

### MCP social — `zapier-3`

Apps disponíveis:
- Facebook Pages
- Instagram for Business

#### Instagram for Business

Ações disponíveis:
- Publish Photo(s) — escrita/publicação.
- Publish Video — escrita/publicação.
- Make API GET Request — leitura/API GET.
- Make API Mutating Request — escrita/mutação.

Regra: usar apenas leitura/API GET quando solicitado. Publicação e mutação exigem autorização explícita.

#### Facebook Pages

Ações disponíveis:
- Change Page Profile Photo — sensível/escrita.
- Create Page Photo — publicação.
- Page Post Insights — métricas de post; no Zapier aparece como write_action, então tratar como sensível e executar só com comando claro.
- Create Page Post — publicação.
- Create Page Video — publicação.

Métricas possíveis em Page Post Insights incluem engajamento, feedback negativo, reações, impressões, alcance, cliques, views de vídeo, tempo de visualização e métricas pagas/orgânicas quando disponíveis.

## Outros MCPs fora da responsabilidade principal do tópico

### `zapier-1`

App disponível:
- Google AI Studio (Gemini)

Uso: análise/geração multimodal via Gemini. Não é responsabilidade principal de Redes Sociais & Métricas, mas pode apoiar estudos de vídeo/áudio/documento quando autorizado.

### `zapier-2`

Apps disponíveis:
- Trello
- Miro

Uso: gestão visual/projetos. Não é responsabilidade principal de Redes Sociais & Métricas.

## Regra de atuação do agente 871

1. Receber pedido de monitoramento/análise.
2. Identificar plataforma e fonte: YouTube, Instagram, Facebook Pages ou outro.
3. Preferir ações de leitura/GET/relatórios.
4. Apresentar resultado em formato:
   - fonte;
   - período;
   - dados observados;
   - interpretação;
   - recomendação;
   - riscos/limitações;
   - próximos passos.
5. Encaminhar à Clara quando o resultado precisar virar planilha/relatório no Drive.
6. Encaminhar à Lôh quando envolver novo MCP, credencial, permissão, erro técnico ou ação sensível.

## Limites explícitos

Sem autorização explícita, o tópico/agente não deve:

- publicar post, foto ou vídeo;
- fazer upload no YouTube;
- alterar thumbnail;
- adicionar vídeo a playlist;
- trocar foto de perfil;
- responder comentários;
- criar/alterar campanhas;
- fazer API mutating request;
- alterar permissões ou contas conectadas.

## Primeira missão recomendada

Levantar inventário de contas/canais/perfis acessíveis:

| Plataforma | Nome | ID/URL | Tipo de acesso | Métricas disponíveis | Riscos | Próximo passo |
|---|---|---|---|---|---|---|

Começar pelo YouTube quando Jadielson autorizar o teste funcional/readonly.
