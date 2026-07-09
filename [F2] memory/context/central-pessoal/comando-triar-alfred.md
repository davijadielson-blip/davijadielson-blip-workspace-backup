# 🚩 `/triar` — Enviar demanda para triagem do Alfred

**O que faz:** Envia uma mensagem para a Inbox de Triagem do Alfred (Central Pessoal, tópico Alfred) de qualquer grupo onde você estiver.

**Como usar:**
```
/triar [conteúdo da demanda]
```

**Exemplos:**
```
/triar Preciso organizar os comprovantes deste mês
/triar Lembrar de pagar a fatura do cartão amanhã
/triar Tem uma demanda de cliente que chegou, mas não sei se é pessoal ou da LÓGIKA
/triar Preciso de ajuda para priorizar os estudos da semana
```

---

## Como funciona

1. Você digita `/triar [mensagem]` em **qualquer grupo** que a Lôh está (LÓGIKA, Central Pessoal, etc).
2. **Lôh** (onipresente em todos os grupos) captura o comando.
3. Lôh encaminha o conteúdo para o tópico **Alfred** na Central Pessoal.
4. **Alfred** recebe, classifica (Produção de Ganho × Prevenção de Dor × Organização) e aplica a Matriz de Roteamento.
5. Se a demanda for interna da Central Pessoal: Alfred resolve ou encaminha para Warren, Arca, Estudos, etc.
6. Se atravessar grupos: Alfred prepara contexto e Lôh executa o roteamento real.

---

## Para que serve

- **Separar o que é seu do que é do grupo** — não precisa poluir o assunto do grupo com demanda pessoal.
- **Capturar ideias rápidas** — manda `/triar` e depois Alfred organiza.
- **Evitar esquecimento** — joga na triagem em vez de confiar na memória.
- **Centralizar** — tudo que precisa de organização pessoal vai para o mesmo lugar.

---

**Criado em:** 2026-07-09 por Lôh
**Documento de referência:** `[F2] memory/agents/central-pessoal/alfred-secretario-pessoal.md`
**Log de rastreabilidade:** `[F2] memory/context/central-pessoal/encaminhamentos-alfred.md`