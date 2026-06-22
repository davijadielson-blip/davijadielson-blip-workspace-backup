---
tipo: ritual
frente: vault
ultimo-update: 2026-05-10
agente-compatibilidade: [claude, openclaw, gpt, hermes]
---

# Ritual de Importação — Fontes Externas

> Rotina de domingo para manter o vault alimentado com o que aconteceu na semana real.
> Estimativa: 15–20 minutos. Não é obrigatório cada passo toda semana — use o bom senso.

---

## Quando fazer

**Domingo de manhã** — antes ou depois do planejamento semanal (`/planejar-semana`).

O cron `sunday-planning.sh` já gera a nota semanal às 8h com o checklist. Você abre e executa.

---

## Sequência recomendada

### 1. Gmail — `/inbox` *(~3 min)*

```
/inbox
```

- Revisa e-mails das últimas 24–48h agrupados por frente
- Se houver e-mail relevante, o comando pergunta se salva em `[F2] memory/inbox-externa/email/`
- Spam e promoções são ignorados automaticamente

**Quando usar `/inbox-cliente`:**
- Se você sabe que tem algo específico pendente de um cliente
- Exemplo: `/inbox-cliente camara` antes de uma reunião

---

### 2. Google Drive — `/drive-recente` *(~2 min)*

```
/drive-recente
```

- Lista arquivos modificados nas últimas 48h classificados por frente
- Se houver material novo de cliente, salve a referência:
  ```
  /drive-arquivo [ID do arquivo]
  ```

---

### 3. WhatsApp — `/whats-importar` *(~5 min — quando tiver material)*

**Frequência:** quando acumular mensagens relevantes nos grupos (semanal ou quinzenal).

**Como exportar:**
1. Abra o grupo no WhatsApp
2. Toque nos 3 pontos → Mais → Exportar conversa → Sem mídia
3. Compartilhe o `.txt` para o Mac (AirDrop, iCloud Drive, etc.)
4. Mova para `[F2] memory/inbox-externa/whatsapp/whatsapp-raw/`

**Depois:**
```
/whats-importar [F2] memory/inbox-externa/whatsapp/whatsapp-raw/nome-do-grupo.txt
```

**Grupos prioritários para exportar:**
- Câmara Municipal (combinados de pauta, sessões)
- SINDSS (Ceiça e equipe)
- Logika (clientes, equipe)
- Família / pessoal (se relevante para agenda)

---

### 4. Áudio — `/audio-importar` *(~10 min — quando tiver gravações)*

**Frequência:** quando necessário (reuniões gravadas, voicenotes importantes, entrevistas).

**Como transcrever:**
```bash
bash scripts/transcrever.sh /caminho/do/audio.mp3
```

**Pré-requisito (instalar uma vez):**
```bash
pip install openai-whisper
```

**Depois:**
```
/audio-importar [F2] memory/inbox-externa/audio/audio-transcricoes/YYYY-MM-DD-nome.md
```

**Dica:** Whisper usa o modelo `base` por padrão (mais rápido). Para áudios longos ou com sotaque local, use `medium`:
```bash
whisper audio.mp3 --language Portuguese --model medium
```

---

### 5. Cruzar tudo — `/prioridades` *(~2 min)*

```
/prioridades
```

- Cruza Gmail + Drive + Calendar + pendências
- Entrega Top 3 real do dia baseado em dados reais, não suposição
- Aponta prazos novos que não estão em `pendencias.md`

---

### 6. Financeiro — `/financeiro` *(mensal)*

**Frequência:** uma vez por mês, quando fechar o mês ou receber pagamentos.

**Como usar:**
- Se tiver planilha: exporte como CSV e rode `/financeiro caminho/arquivo.csv`
- Se quiser digitar direto: rode `/financeiro` e cole os valores quando pedido

---

## Regra de ouro

> **A IA sugere — você decide.**
> Nada sai de `[F2] memory/inbox-externa/` sem você aprovar.
> Se não quiser salvar: ignore. O ritual não obriga.

---

## Sinais de que o ritual está funcionando

- `/prioridades` retorna itens que você não tinha visto
- Você para de perder e-mails de cliente na semana
- Reuniões gravadas viram ações no vault, não ficam esquecidas no celular
- O financeiro fica atualizado sem esforço mental

---

## Referências

- Comandos disponíveis: `[F2] memory/visualizations/comandos.md`
- Estrutura da inbox: `[F2] memory/inbox-externa/_MAP.md`
- Pendências: `[F2] memory/context/pendencias.md`
