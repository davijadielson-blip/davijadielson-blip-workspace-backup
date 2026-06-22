---
tipo: skill
nome: colheita
trigger: "usuário digita 'colheita', '/colheita', 'fiz a colheita', 'sintetizei', 'criei nota de'"
agente-compatibilidade: [claude, openclaw, gpt, hermes]
ultimo-update: 2026-05-28
---

# SKILL — colheita (Fechamento do Fluxo 3)

> Fecha o ciclo de integração: Jadielson processou um output da IA e criou uma nota autoral no Fluxo 1.
> A IA atualiza os metadados do output e registra o evento. Sem isso, o Fluxo 3 não aconteceu.

---

## Trigger

O usuário digita: `colheita`, `/colheita`, `fiz a colheita`, `sintetizei`, `criei nota de`.

Pode vir com argumentos diretos:
- `colheita output: [nome] nota: [caminho]`
- `fiz a colheita do output sobre X, criei a nota Y`

---

## Procedimento

### Fase 1 — Identificar o output colhido

**Se o usuário já informou o output:** pular para a Fase 2.

**Se não informou:** buscar outputs pendentes.

1. Chamar `GET /search?q=aguardando-colheita` na API do vault.
2. Filtrar resultados que estejam dentro de `[F2] memory/outputs/`.
3. Listar os outputs pendentes com nome e frente:

```
📦 Outputs aguardando colheita:

1. [F2] memory/outputs/logika/drafts/2026-05-20-posicionamento.md
2. [F2] memory/outputs/camara/legendas/2026-05-22-sessao-plenaria.md
3. ...

Qual você colheu? (pode informar o número ou o nome)
```

4. Aguardar Jadielson indicar qual output foi colhido.

---

### Fase 2 — Identificar a nota do Fluxo 1

**Se o usuário já informou o caminho da nota:** usar esse caminho.

**Se não informou:** perguntar:

```
Qual é o caminho (ou nome) da nota que você criou no Fluxo 1?
Exemplo: 1-Permanentes/posicionamento-logika.md
```

Aguardar resposta antes de prosseguir.

---

### Fase 3 — Atualizar o output (Fluxo 2)

1. Ler o arquivo do output via `GET /file?path=MAPA OBSIDIAN/[F2] memory/outputs/[caminho]`.
2. Localizar o bloco YAML frontmatter (entre os primeiros `---`).
3. Substituir:
   - `status: aguardando-colheita` → `status: sintetizado`
   - `sintetizado-em: ` → `sintetizado-em: "[[F1] 1-Permanentes/[nome-da-nota]]"` (ou o caminho real informado)
4. Escrever o arquivo atualizado via `PUT /file?path=MAPA OBSIDIAN/[F2] memory/outputs/[caminho]`.
5. Confirmar o sucesso da escrita.

---

### Fase 4 — Oferecer atualização da nota do Fluxo 1 (opcional)

Perguntar:

```
Quer que eu adicione o campo `colhido-de` na sua nota do Fluxo 1?
Isso marca a origem da ideia sem alterar o conteúdo autoral.

[S] Sim, adicionar  [N] Não, já está bom
```

**Se sim (e apenas se sim):**
1. Ler a nota em `[F1]/[caminho-da-nota]` via `GET /file`.
2. Verificar se já existe `colhido-de:` no frontmatter.
   - Se já existe: informar e não sobrescrever.
   - Se não existe: adicionar `colhido-de: "[[[F2] memory/outputs/[caminho-do-output]]]"` no frontmatter.
3. Escrever via `PUT /file?path=MAPA OBSIDIAN/[F1]/[caminho-da-nota]`.

**Se não:** pular. A nota do Fluxo 1 é território de Jadielson.

---

### Fase 5 — Registrar na sessão

1. Abrir ou criar `[F2] memory/sessions/YYYY-MM-DD.md`.
2. Acrescentar ao final:

```markdown
### Colheita — HH:MM
- Output sintetizado: `[F2] memory/outputs/[caminho]`
- Nota autoral criada: `[F1]/[caminho-nota]`
- Fluxo 3 fechado ✅
```

---

### Fase 6 — Relatório final

```
🌾 Colheita registrada.

Output atualizado:
  [F2] memory/outputs/[caminho]
  status: sintetizado
  sintetizado-em: [[nome-da-nota]]

Nota autoral: [F1]/[caminho] (criada por você)
colhido-de: [adicionado / não solicitado]

Fluxo 3 fechado. O ciclo se multiplicou. ✅
```

---

## Regras

- **Nunca criar a nota do Fluxo 1** — só Jadielson escreve lá.
- **Nunca sobrescrever conteúdo autoral** — só modificar frontmatter YAML.
- **A Fase 4 requer "sim" explícito** antes de tocar em qualquer arquivo `[F1]`.
- Se o output não tiver frontmatter YAML, alertar Jadielson em vez de tentar editar.
- Se a busca não retornar outputs, informar: _"Nenhum output com status aguardando-colheita encontrado. Você pode informar o caminho diretamente."_

---

## Notas

A Colheita é o evento que valida o Fluxo 3. Sem ela, a IA operou mas o sistema não se multiplicou.
Cada Colheita é um commit intelectual de Jadielson — a IA apenas registra o que ele decidiu.