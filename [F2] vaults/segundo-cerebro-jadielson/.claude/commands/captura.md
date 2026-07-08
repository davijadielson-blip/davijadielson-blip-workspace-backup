---
description: Captura rápida — anexa texto na seção Captura da daily de hoje
argument-hint: <texto a capturar>
---

Captura rápida. Sem perguntas, sem ritual, sem reformulação.

**Texto capturado:** $ARGUMENTS

**Execute agora:**

1. Obtenha data e hora atual:
```bash
date +"%Y-%m-%d|%H:%M"
```

2. Localize `[F1] 3-Daily/YYYY-MM-DD.md`.
   - Se não existir: crie um arquivo mínimo com frontmatter básico e as seções `## 📝 Captura` e `## 🌙 Revisão (17h–18h)` vazias.

3. Encontre a seção `## 📝 Captura` no arquivo.

4. Insira esta linha imediatamente após o cabeçalho da seção (antes de qualquer conteúdo existente):
```
- **HH:MM** — TEXTO_DO_ARGUMENTS
```

5. Salve o arquivo.

6. Responda em uma única linha: "✓ Capturado às HH:MM."

Nada mais. Não expanda, não comente, não pergunte.
