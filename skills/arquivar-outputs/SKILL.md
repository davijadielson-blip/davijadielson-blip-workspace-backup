---
tipo: skill
nome: arquivar-outputs
trigger: "usuário digita 'arquivar outputs' ou '/arquivar-outputs' ou 'arquivar mês'"
agente-compatibilidade: [claude, openclaw, gpt]
ultimo-update: 2026-05-23
---

# SKILL — arquivar-outputs

> Move os arquivos de output do mês anterior de `[F2] memory/outputs/<frente>/` para `[F2] memory/outputs/_arquivo/YYYY-MM/<frente>/`, mantendo a estrutura por frente.
> Usar no início de cada mês ou quando os outputs estiverem acumulando.

---

## Trigger

O usuário digita: `arquivar outputs`, `/arquivar-outputs`, `arquivar mês`, `limpar outputs`.

---

## Estrutura de outputs (frente → tipo)

```
[F2] memory/outputs/
  <frente>/
    roteiros/
    legendas/
    headlines/
    drafts/
    resumos-whatsapp/
    briefings/
    _arquivo/
      YYYY-MM/
        roteiros/
        legendas/
        drafts/
        ...
```

Frentes ativas: `saude-sao-sebastiao` · `camara` · `sindss` · `logika` · `rogerio` · `alem-da-foto` · `vereadores` · `lives-louvor`

---

## Procedimento

### Fase 1 — Identificar o mês a arquivar

1. Verificar a data atual.
2. O mês a arquivar é **sempre o mês anterior** ao atual.
   - Ex.: se hoje é junho, arquiva os arquivos de maio (prefixo `2026-05-`).
3. Confirmar com o usuário: _"Vou arquivar todos os outputs de [MÊS/ANO]. Confirma?"_
4. Aguardar confirmação antes de mover qualquer arquivo.

---

### Fase 2 — Verificar arquivos elegíveis

Percorrer:

```
[F2] memory/outputs/<frente>/<tipo>/
```

Critério: arquivo cujo nome começa com `YYYY-MM-` do mês a arquivar.

Listar os arquivos encontrados e exibir antes de mover.

---

### Fase 3 — Criar estrutura de destino

Destino: `[F2] memory/outputs/<frente>/_arquivo/YYYY-MM/<tipo>/`

Exemplo para maio de 2026:
```
[F2] memory/outputs/saude-sao-sebastiao/_arquivo/2026-05/roteiros/
[F2] memory/outputs/saude-sao-sebastiao/_arquivo/2026-05/drafts/
[F2] memory/outputs/sindss/_arquivo/2026-05/legendas/
[F2] memory/outputs/camara/_arquivo/2026-05/resumos-whatsapp/
```

---

### Fase 4 — Mover os arquivos

Mover cada arquivo elegível para o caminho correspondente. Manter estrutura `<frente>/_arquivo/YYYY-MM/<tipo>/<arquivo>`.

---

### Fase 5 — Relatório final

```
✅ Arquivamento de [MÊS/ANO] concluído.

Movidos:
- saude-sao-sebastiao/roteiros: X arquivo(s)
- saude-sao-sebastiao/drafts: X arquivo(s)
- sindss/legendas: X arquivo(s)
- ...

Total: X arquivo(s) arquivados.
Destino: [F2] memory/outputs/<frente>/_arquivo/YYYY-MM/
```

---

## Regras

- **Nunca arquivar o mês atual** — apenas mês anterior ou anteriores.
- **Nunca deletar** — apenas mover.
- **Sempre confirmar** antes de executar a fase 4.
- Arquivos sem prefixo de data são ignorados.
- A pasta `_arquivo/` nunca é varrida por `/revisar`.

---

## Variação: arquivar mês específico

Se o usuário disser _"arquivar outputs de março"_ ou _"arquivar 2026-03"_, usar o mês indicado. Confirmar igualmente antes de executar.
