---
description: Lista aniversariantes da SMS no mês e sugere template de homenagem por servidor
argument-hint: <mes> (1-12, padrão: mês atual)
---

Liste os aniversariantes e sugira homenagens. Siga cada passo.

**Argumento recebido:** $ARGUMENTS
(Se vazio, use o mês atual. Se for número de 1 a 12, use esse mês.)

---

**PASSO 1 — Determinar o mês**

```bash
date +"%m"   # mês atual se argumento vazio
```

Converta o número para o nome do mês em português.

**PASSO 2 — Varrer aniversariantes**

Leia todos os arquivos em `[F2] memory/databases/aniversariantes/`.

Para cada arquivo, extraia: `nome`, `aniversario`, `cargo`, `frente`.

Filtre os que têm `month(aniversario) == mês_alvo`. Ordene por dia crescente.

**PASSO 3 — Exibir a lista**

```
## Aniversariantes — Mês de <Nome do Mês>

| Dia | Nome | Cargo |
|-----|------|-------|
| DD  | Nome | Cargo |
...

Total: X aniversariantes
```

**PASSO 4 — Sugerir template de homenagem**

Para cada aniversariante, gere um template de post de homenagem:

```
---
### Homenagem — <Nome> (DD/<mês>)

[Nome], que neste dia completa mais um ano de vida, é [cargo] da Secretaria de Saúde de São Sebastião.

Sua dedicação ao [área de atuação] é parte fundamental do atendimento de qualidade que a nossa população merece.

A Secretaria de Saúde parabeniza [Nome] e deseja saúde, realizações e muito sucesso nessa nova etapa!

#aniversario #saude #servidores #saude #saoebastiao
---
```

Ajuste o template para o cargo e área de cada pessoa. Se o cargo envolver área específica (EMULTI, CEO, APS etc.), mencione.

**PASSO 5 — Perguntar**

Ao final pergunte: "Quer que eu gere o post completo de homenagem para algum deles? Se sim, me diz o nome."
