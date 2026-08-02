---
tema: protocolo do tópico Telegram da Saúde São Sebastião
conteudo: regra operacional para demandas diárias de social media da Secretaria Municipal de Saúde no tópico 3672, com escopo profissional de fontes
setor: comunicação institucional e social media
cliente: Saúde São Sebastião
tipo: protocolo operacional
prioridade: máxima
atualizado_em: 2026-07-31
usar_quando: produzir legenda, headline, roteiro, Stories, WhatsApp, release, pauta, carrossel educativo ou planejamento editorial da Saúde São Sebastião
nao_usar_quando: publicar automaticamente, prometer serviço sem confirmação ou consultar arquivos pessoais
---

# Protocolo do tópico Telegram 3672 - Social Media Saúde

Este tópico da LÓGIKA é a frente diária de trabalho da comunicação da Secretaria Municipal de Saúde de São Sebastião.

## Regra central

Cofre organiza, Drive comprova, skill dá o padrão editorial, e Jadielson valida o que for sensível.

## Regra de armazenamento

No Cofre, guardar somente arquivos `.md`.

Arquivos não Markdown — como ZIP, imagem, vídeo, áudio, arte, PDF, planilha, pacote de skill, mídia bruta ou arquivo binário — não devem ser armazenados no Cofre como destino permanente. Quando precisarem ser preservados, encaminhar para o Drive profissional da frente ou manter apenas como anexo transitório até a organização correta.

## Quando aplicar

Aplicar em toda demanda que envolva:

- legenda;
- headline;
- roteiro;
- Stories;
- WhatsApp;
- release;
- pauta;
- carrossel educativo;
- planejamento editorial;
- revisão de texto institucional da Secretaria Municipal de Saúde.

## Ordem de operação

1. Consultar primeiro o Cofre:
   `/data/.openclaw/workspace/50-clientes/10-saude-sao-sebastiao/`
2. Para produção diária, começar pela entrada operacional:
   `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/`
3. Usar também:
   - `00-indice/indice-editorial.md`
   - `00-indice/indice-unidades-setores.md`
   - `10-contexto/resumo-consolidado-fatos-validados.md`
   - `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/SKILL.md`
   - `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/references/STYLE_GUIDE.md`
   - `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/references/SOURCE_POLICY.md`
   - `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/references/GOOGLE_DRIVE_SOURCES.md`
   - `/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/references/ACCESS_SCOPE.md`
4. Quando a demanda depender de arquivo-fonte, relatório, roteiro, planilha, peça, versão de produção ou documento original, consultar primeiro o Drive profissional:
   `gog --account logikacreative.mkt@gmail.com --readonly ...`
5. Não consultar, listar, abrir, exportar, baixar, editar, compartilhar, mover ou excluir arquivos do Drive pessoal `davijadielson@gmail.com` nesta frente.
6. Antes de operações Google, quando necessário, carregar:
   `cd /data/.openclaw/workspace && source scripts/gog-auth.sh`
7. Se Cofre + Drive profissional forem insuficientes, marcar a lacuna como `[A CONFIRMAR]` e pedir o arquivo ou validação de Jadielson.

## Ordem de confiança

1. Instrução atual de Jadielson.
2. Cofre e contexto operacional da Saúde.
3. Drive profissional, quando houver arquivo-fonte mais recente ou aprovado.
4. Exemplos e padrões da skill.
5. Fontes oficiais externas para orientação técnica de saúde.

## Regras editoriais

- Nunca inventar nomes, datas, números, locais, cargos, horários, especialidades, quantidade de atendimentos ou promessa de serviço.
- Quando faltar dado essencial, marcar `[A CONFIRMAR]`.
- Não publicar automaticamente nem escrever externamente sem ordem explícita de Jadielson.
- Produzir, revisar e sinalizar o que precisa de confirmação.
- Evitar texto genérico.
- Toda peça deve mostrar:
  - serviço real acontecendo;
  - benefício prático para a população;
  - orientação clara de acesso ou continuidade;
  - tom institucional, humano e simples.

## Observação operacional

A skill `saude-sao-sebastiao-comunicacao` está instalada no caminho canônico:

`/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao/`
