---
tema: pendencias centrais do Cofre
conteudo: lista atual de pendencias estruturais, revisoes humanas e proximas etapas de limpeza do Cofre
nicho: ecossistema agentico Loh/Jadielson
setor: governanca do Cofre
cliente: Jadielson Davi
tipo: pendencias
prioridade: alta
atualizado_em: 2026-08-10
usar_quando: acompanhar o que falta decidir, revisar ou executar na organizacao do Cofre
nao_usar_quando: registrar decisoes finais; use 00-central/decisoes.md
---

# Pendencias centrais

## Revisao humana

- [ ] Decidir se materiais do Starter Kit/OpenClaw que ainda vivem na raiz ativa (`README.md`, `CHANGELOG.md`, `FAQ.md`) devem permanecer como referencia de curso ou ir para `90-arquivo/`.
- [ ] Decidir destino formal dos papeis antigos associados a "bibliotecaria": renomear, arquivar como historico ou manter apenas como referencia.
- [ ] Revisar arquivos de `70-agentes/runtime/*/openclaw-workspace-state.json` antes de versionar, por serem estado operacional nao rastreado.
- [ ] Revisar `memory/2026-08-10.md` e demais arquivos nao rastreados antes de incluir em commit amplo, preservando sigilo e pertinencia.

## Limpeza estrutural restante

- [ ] Atualizar gradualmente `_MAP.md` legados dentro de bases migradas de clientes, sem apagar a origem historica.
- [ ] Separar, por lote, duplicidades internas da Saude em `50-clientes/10-saude-sao-sebastiao/10-contexto/operacional/03-fichas-setores/`.
- [ ] Decidir destino de arquivos nao Markdown que ainda aparecem dentro do Cofre: manter tecnico, referenciar Drive ou mover para quarentena de revisao.
- [ ] Consolidar indices por area onde a navegacao ainda depender de nomes legados longos.

## Compatibilidade

- [ ] Manter referencias historicas F0/F1/F2/F3 em logs e registros de migracao, mas evitar que aparecam como rota ativa em READMEs, mapas e protocolos.
- [ ] Antes de mover qualquer script, skill, agente, cron ou runtime, verificar referencias com `rg` e registrar origem/destino no relatorio do lote.
