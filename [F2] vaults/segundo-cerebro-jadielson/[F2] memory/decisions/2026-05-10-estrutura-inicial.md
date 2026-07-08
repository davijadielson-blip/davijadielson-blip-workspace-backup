# Decisão Arquitetural — Estrutura Inicial do Vault

**Data:** 2026-05-10
**Decidido por:** Jadielson Davi dos Santos
**Registrado por:** IA (Claude)

---

## Decisão

Adotar o método **3 Fluxos + 4 Camadas** como estrutura permanente do vault.

## Estrutura aprovada

```
0-Inbox/
1-Permanentes/
2-Literatura/
3-Daily/
4-Pessoal/
5-Frentes/
    ├── [frentes ativas]
    └── Inativos/        ← clientes/projetos pausados
claude/
```

## Justificativa

O vault anterior misturava notas autorais, outputs de IA, todos e referências sem separação clara de camadas. O novo método separa explicitamente:
- O que é meu (Fluxo 1)
- O que é da IA (Fluxo 2)
- Como os dois se integram (Fluxo 3)

## Decisões específicas tomadas nesta sessão

| Questão | Decisão |
|---|---|
| CLAUDE_OBSIDIAN.md vs CLAUDE.md | Criar CLAUDE.md único e definitivo na raiz; arquivar original em `claude/decisions/` |
| Autoajuda (Paulo Vieira e similares) | Vai para `2-Literatura/` |
| Rogério Rocha | Cliente **inativo** — pasta em `5-Frentes/Inativos/Rogerio-Rocha/` |
| Pastas vazias | Deletar; títulos preservados no Inbox para revisão futura |

## O que NÃO muda

- Estrutura interna de `5-Frentes/Saude-Sao-Sebastiao/` — preservada integralmente
- Conteúdo de qualquer nota autoral — IA não edita, só move (com aprovação)
