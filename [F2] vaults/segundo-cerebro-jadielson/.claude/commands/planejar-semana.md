---
description: Ritual de domingo — cria a nota semanal com recap, frentes, datas e aniversariantes
---

Crie o planejamento da semana. Execute cada passo na ordem.

**PASSO 1 — Obter referências de data**

```bash
date +"%Y-W%V"      # semana atual ex: 2026-W20
date +"%Y-%m-%d"    # hoje (domingo)
date -v+1d +"%Y-%m-%d"   # segunda-feira
date -v+7d +"%Y-%m-%d"   # próximo domingo
```

(No Linux substitua `-v+Nd` por `-d "+N days"`)

Identifique também o número da semana anterior: `W(N-1)`.

**PASSO 2 — Recap da semana anterior**

Liste os arquivos de daily em `[F1] 3-Daily/` da semana passada (seg a sáb):
```bash
ls "[F1] 3-Daily/" | grep -E "YYYY-MM-DD pattern da semana anterior"
```

Para cada daily encontrada, leia e extraia:
- O que estava no **Foco do dia**
- O que foi registrado na **Revisão (17h–18h)**

Se não houver dailies, registre: "Semana anterior sem dailies registradas."

**PASSO 3 — Frentes com e sem atenção**

Verifique em `[F2] memory/outputs/` os arquivos gerados na última semana (por data de criação). Liste quais frentes tiveram outputs e quais ficaram sem nenhuma produção.

**PASSO 4 — Datas sazonais da semana que vem**

Leia os arquivos em `[F2] memory/databases/datas-sazonais/` e filtre as datas que caem entre segunda e domingo da semana que vem. Liste com frente e tipo.

**PASSO 5 — Aniversariantes da SMS na semana**

Leia os arquivos em `[F2] memory/databases/aniversariantes/` e filtre os que têm aniversário entre segunda e domingo da semana que vem (pelo campo `aniversario`, verificando mês e dia). Liste com nome e cargo.

**PASSO 6 — Criar a nota semanal**

Caminho: `[F1] 3-Daily/Semanais/YYYY-Www.md`

Conteúdo:

```
---
tipo: semanal
semana: YYYY-Www
data-inicio: YYYY-MM-DD (segunda)
data-fim: YYYY-MM-DD (domingo seguinte)
gerado-por: claude
comando: /planejar-semana
---

# Semana YYYY-Www — Planejamento

## 📋 Recap da semana anterior (W anterior)

<resumo extraído das dailies ou "sem registros">

## 🔍 Frentes — balanço

**Tiveram outputs:** <lista>
**Sem atividade:** <lista>

## 📅 Datas sazonais da semana

<lista de datas com frente e tipo — ou "nenhuma data sazonal essa semana">

## 🎂 Aniversariantes da SMS na semana

<lista com nome, cargo e data — ou "nenhum aniversário essa semana">

## 🎯 Foco da semana por frente

| Frente | Foco / Entregável |
|--------|------------------|
| Lógika Creative | |
| Saúde SMS | |
| Câmara Municipal | |
| SINDSS | |
| Além da Foto | |
| Lives | |

## 🗓️ Distribuição da rotina

| Dia | Tipo | Prioridade |
|-----|------|------------|
| Segunda | Externo | |
| Terça | Agência | |
| Quarta | Externo | |
| Quinta | Agência | |
| Sexta | Externo + Manutenção | |
| Sábado | Agência | |
| Domingo | Planejamento | ✅ feito |
```

**PASSO 7 — Log**

Crie `[F2] memory/logs/comandos/YYYY-MM-DD-planejar-semana.md` com referência à nota criada.

Ao finalizar, exiba o resumo das datas e aniversariantes da semana, e confirme: "Planejamento YYYY-Www criado. Preencha o foco por frente quando quiser."
