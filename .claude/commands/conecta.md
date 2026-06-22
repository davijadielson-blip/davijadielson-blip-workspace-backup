---
description: Encontra conexões entre dois temas no vault e entrega esqueleto de nota para Jadielson escrever
argument-hint: <tema-A> <tema-B>
---

Encontre conexões entre dois temas no vault. Siga cada passo.

**Argumento recebido:** $ARGUMENTS
(Separar os dois temas por espaço. Se houver apenas um tema, pergunte o segundo.)

---

**PASSO 1 — Identificar os dois temas**

Extraia do argumento:
- `<tema-A>` = primeiro elemento
- `<tema-B>` = tudo que vier depois

Se algum estiver faltando, pergunte antes de continuar.

**PASSO 2 — Buscar cada tema individualmente**

Execute grep para cada tema no vault (mesmas pastas do `/busca`):
```bash
grep -ril "<tema-A>" "[F1]" "memory" 2>/dev/null
grep -ril "<tema-B>" "[F1]" "memory" 2>/dev/null
```

**PASSO 3 — Identificar interseções**

Encontre os arquivos que aparecem em **ambas** as buscas — eles são os pontos de conexão já existentes.

Leia esses arquivos e extraia os trechos relevantes.

**PASSO 4 — Mapear as conexões**

Com base nos resultados, identifique:
- O que os dois temas têm em comum no vault atual
- Onde eles se tocam (mesmo arquivo, mesmo projeto, mesma frente)
- O que está em um mas não no outro (lacunas)
- Uma ideia de síntese que poderia emergir da combinação dos dois

**PASSO 5 — Entregar o esqueleto**

Gere um esqueleto de nota para Jadielson escrever. Não preencha o conteúdo — apenas a estrutura:

```
## Esqueleto sugerido: "<Tema-A> × <Tema-B>"

> Esta nota é para você escrever. Eu trouxe a estrutura baseada no que encontrei no vault.

### Por que esses dois temas se conectam
[você escreve aqui]

### O que já existe sobre <Tema-A>
→ Links relevantes encontrados: [[nota-1]], [[nota-2]]

### O que já existe sobre <Tema-B>
→ Links relevantes encontrados: [[nota-3]], [[nota-4]]

### Ponto de cruzamento
[você escreve aqui — o insight que só você pode ter]

### Próximos passos
- [ ] 
- [ ] 
```

**PASSO 6 — Orientar**

Diga: "Esse esqueleto é pra você. Quando quiser transformar em nota permanente, salve em `[F1] 1-Permanentes/`. Posso ajudar a afinar a estrutura, mas o pensamento é seu."
