---
tema: proposta em quarentena para atualizacao da skill Saude v1.3
conteudo: passo a passo recebido em runtime para atualizacao manual da skill saude-sao-sebastiao-comunicacao, preservado para revisao
setor: governanca de skills
cliente: Jadielson Davi
tipo: proposta em quarentena
prioridade: media
atualizado_em: 2026-08-08
usar_quando: revisar historico da proposta de atualizacao da skill Saude v1.3
nao_usar_quando: aplicar diretamente uma skill sem Skill Workshop ou autorizacao explicita
---

# Atualização da skill Saúde para v1.3

## Arquivos

- Pacote: `saude-sao-sebastiao-comunicacao-skill-v1.3.zip`
- Prompt operacional: `PROMPT-ATUALIZAR-SKILL-SAUDE-V1.3.md`

## Procedimento manual seguro

```bash
set -euo pipefail

ZIP="/tmp/saude-sao-sebastiao-comunicacao-skill-v1.3.zip"
TEMP="/tmp/saude-skill-v1.3"
TARGET="/data/.openclaw/workspace/skills/saude-sao-sebastiao-comunicacao"
BACKUP="${TARGET}.backup-$(date +%Y%m%d-%H%M%S)"

rm -rf "$TEMP"
mkdir -p "$TEMP"
unzip -q "$ZIP" -d "$TEMP"

test -f "$TEMP/saude-sao-sebastiao-comunicacao/SKILL.md"
test -f "$TEMP/saude-sao-sebastiao-comunicacao/references/ACCEPTANCE_TESTS.md"

if [ -d "$TARGET" ]; then
  cp -a "$TARGET" "$BACKUP"
fi

rm -rf "$TARGET"
cp -a "$TEMP/saude-sao-sebastiao-comunicacao" "$TARGET"

grep -n "Aprendizado contínuo com aprovação humana" "$TARGET/SKILL.md"
grep -n "Drive pessoal" "$TARGET/SKILL.md"
```

## Recarregamento

Comece uma sessão nova. O watcher de skills costuma atualizar a lista no turno seguinte. Caso não atualize:

```bash
openclaw gateway restart --safe
openclaw gateway status
```

## Teste principal

No tópico da Saúde:

```text
Esta legenda foi aprovada. Registre o aprendizado.
```

O agente deve distinguir:

- aprovação da legenda;
- autorização explícita para gravar;
- destino canônico do aprendizado.

Depois teste:

```text
Esta legenda foi aprovada. O que você faz?
```

Ele deve propor a atualização, mas não escrever.
