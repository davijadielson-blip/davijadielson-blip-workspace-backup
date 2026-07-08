---
tipo: regras-classificacao
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

# Regras de Classificação de Eventos da Agenda

> Usado pelos comandos `/hoje`, `/agenda` e `/agendar` para classificar eventos do Google Calendar com ícone e cor por frente.
> Primeira regra que casar vence. Edite este arquivo para adicionar palavras-chave sem precisar alterar os comandos.

---

## Como aplicar

1. Pegue o título + descrição do evento (tudo em minúsculas).
2. Percorra as regras de cima para baixo.
3. Se qualquer palavra-chave da regra aparecer no título ou descrição → aplique o ícone e colorId correspondente.
4. Se nenhuma regra casar → aplique o padrão (📅 Graphite).

---

## Regras

### 🎬 Lógika Creative — colorId 7 (Peacock)

Palavras-chave: `logika`, `lógika`, `filmagem`, `gravação`, `gravacao`, `edição`, `edicao`, `cliente`, `captação`, `captacao`, `entrega de vídeo`, `entrega de video`, `produção audiovisual`, `producao audiovisual`, `claquete`

---

### 🏛️ Câmara Municipal — colorId 9 (Blueberry)

Palavras-chave: `câmara`, `camara`, `sessão`, `sessao`, `vereador`, `plenário`, `plenario`, `comissão`, `comissao`, `legislativo`, `câmara municipal`, `camara municipal`, `tribuna`

---

### 🏥 Saúde — colorId 10 (Basil)

Palavras-chave: `secretaria de saúde`, `secretaria de saude`, `sms`, `unidade de saúde`, `unidade de saude`, `ceo`, `ubs`, `vacinação`, `vacinacao`, `vigilância`, `vigilancia`, `saúde pública`, `saude publica`, `campanha de saúde`

---

### 🔴 SINDSS — colorId 6 (Tangerine)

Palavras-chave: `sindss`, `sindicato`, `assembleia sindical`, `servidores municipais`, `presidente ceiça`, `presidente ceica`

---

### 🗳️ Rogério Rocha — colorId 3 (Grape)

Palavras-chave: `rogério`, `rogerio`, `vereador rogério`, `mandato rogério`

---

### 📢 Outros Vereadores — colorId 4 (Flamingo)

Palavras-chave: `josi`, `curtinhos`, `vando`, `cana brava`, `manoel`, `gongo`

---

### 🎙️ Além da Foto — colorId 1 (Lavender)

Palavras-chave: `além da foto`, `alem da foto`, `foto antiga`, `documentário`, `documentario`, `são sebastião histórico`

---

### 🎵 Lives de Louvor — colorId 5 (Banana)

Palavras-chave: `lives de louvor`, `live gospel`, `louvor`, `reflexão bíblica`, `reflexao biblica`, `culto online`, `assembleia de deus`

---

### 👨‍👧 Pessoal / Família — colorId 2 (Sage)

Palavras-chave: `eloáh`, `eloah`, `alícia`, `alicia`, `família`, `familia`, `culto`, `ir ao culto`, `treino`, `vitalidade`, `fundação pessoal`, `fundacao pessoal`, `bloco 1`, `bloco 2`, `igreja`, `oração`, `oracao`, `meditação`, `meditacao`

---

### 📅 Padrão — colorId 8 (Graphite)

Qualquer evento que não case com as regras acima.

---

## Adicionando novas regras

Para adicionar uma nova frente ou palavra-chave, edite este arquivo diretamente. Formato:

```
### [ícone] Nome da frente — colorId X (Nome da cor)

Palavras-chave: `palavra1`, `palavra2`, `frase composta`
```

Cores disponíveis: 1 Lavender · 2 Sage · 3 Grape · 4 Flamingo · 5 Banana · 6 Tangerine · 7 Peacock · 8 Graphite · 9 Blueberry · 10 Basil · 11 Tomato
