# Mission Control v2 — App editável

## Decisão
Jadielson aprovou a Opção 3: transformar o Mission Control em app web editável, elegante e otimizável.

## Arquitetura aprovada
- App fora do Cofre: `/data/.openclaw/mission-control-next/`.
- Fonte persistente dentro do Cofre em Markdown: `[F2] memory/visualizacoes/mission-control-data.md`.
- O app lê e salva os dados por API local.
- O Cofre continua recebendo apenas `.md`.
- Alterações visuais passam por tokens CSS.
- Conteúdo operacional deve vir do objeto de dados persistido, não hardcoded na interface.

## Regras
- Não apagar nada.
- Não criar workspace paralelo.
- Salvar continuidade no Cofre em Markdown.
- Manter painel elegante, otimizável e responsivo.

## Próximo passo
Implementar v2 em Next.js já existente, com modo Visualizar/Editar, salvamento em Markdown e changelog.
