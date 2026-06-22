---
tipo: visualizacao
frente: vault
gerado-por: claude
revisado: false
data-criacao: 2026-05-10
---

← [[Hub]]

# Cheat Sheet — Slash Commands

> Referência rápida. Para ver o prompt completo de cada comando, abra `.claude/commands/<nome>.md`.

---

## Tier 1 — Uso diário

| Comando | Quando usar | Exemplo |
|---------|-------------|---------|
| `/hoje` | Ao abrir o Claude de manhã — puxa eventos reais do Google Calendar | `/hoje` |
| `/captura <texto>` | Anotar algo rápido sem interromper o fluxo | `/captura ligar pra Ceiça sobre reunião SINDSS` |
| `/legenda <frente> <desc>` | Gerar legenda Instagram + hashtags + WhatsApp | `/legenda saude "campanha outubro rosa no CEO"` |
| `/resumo-whats` | Gerar manchete de uma legenda já existente | `/resumo-whats` |
| `/revisar` | Ver o que está na fila de revisão | `/revisar` |

---

## Tier 2 — Por frente

| Comando | Quando usar | Exemplo |
|---------|-------------|---------|
| `/roteiro-rogerio <tema>` | Produzir roteiro de vídeo do Rogério | `/roteiro-rogerio "visita ao Povoado Mata"` |
| `/post-camara <tipo>` | Gerar post da Câmara (pergunta detalhes) | `/post-camara sessao` |
| `/post-sindss <tipo>` | Gerar conteúdo SINDSS conforme dia da semana | `/post-sindss depoimento-sexta` |
| `/post-rogerio <tipo>` | Post do Rogério em 1ª pessoa | `/post-rogerio presenca` |
| `/post-logika <desc>` | Legenda Lógika com metáfora + mini-case | `/post-logika "vídeo institucional do hospital"` |
| `/post-saude <campanha>` | Post institucional da SMS | `/post-saude outubro-rosa` |

### Tipos válidos por comando

| Comando | Tipos aceitos |
|---------|--------------|
| `/post-camara` | `aniversario` · `projeto-aprovado` · `biografia` · `sessao` · `rotina-presidente` · `procuradoria` |
| `/post-sindss` | `feed` · `reel-viral` · `reel-educativo` · `depoimento-sexta` |
| `/post-rogerio` | `proposta` · `execucao` · `presenca` · `depoimento-apoiador` |

---

## Google Calendar

| Comando | Quando usar | Exemplo |
|---------|-------------|---------|
| `/agenda <N>` | Ver compromissos dos próximos N dias com ícone de frente | `/agenda 14` |
| `/agendar <desc>` | Criar evento no Calendar (sempre confirma antes) | `/agendar reunião com cliente logika quinta 14h` |
| `/sincronizar-sazonais` | Criar lembretes de planejamento/produção/publicação para datas sazonais | `/sincronizar-sazonais` |
| `/bloquear-rotina` | Criar blocos recorrentes de rotina (Externo, Agência, Revisão...) | `/bloquear-rotina` |

> **Regra:** `/agendar`, `/sincronizar-sazonais` e `/bloquear-rotina` nunca criam eventos sem confirmação explícita.

---

## Tier 3 — Estratégicos

| Comando | Quando usar | Exemplo |
|---------|-------------|---------|
| `/planejar-semana` | Domingo de manhã | `/planejar-semana` |
| `/manutencao` | Sexta-feira, 15 min | `/manutencao` |
| `/sazonal <dias>` | Checar o que vem pela frente | `/sazonal 14` |
| `/aniversariante <mes>` | Ver aniversariantes do mês | `/aniversariante 7` |
| `/busca <tema>` | Encontrar algo no vault | `/busca EMULTI` |
| `/conecta <A> <B>` | Explorar cruzamento de temas | `/conecta saude comunicacao` |
| `/ideia <frente> <texto>` | Guardar ideia na frente certa | `/ideia camara "fazer série sobre projetos aprovados"` |
| `/prioridades` | Top 3 enriquecido cruzando Gmail + Drive + Calendar + pendências | `/prioridades` |
| `/financeiro [arquivo]` | Importar planilha financeira e atualizar business-context | `/financeiro relatorio-maio.csv` |
| `/conflitos-agenda [N]` | Detectar sobreposições e margens apertadas na agenda | `/conflitos-agenda 7` |
| `/agenda-frente <frente>` | Ver agenda de uma frente específica (14 dias) | `/agenda-frente camara` |

---

## 📥 Fontes Externas — Tier 1 (MCP nativo)

| Comando | Fonte | Quando usar | Exemplo |
|---------|-------|-------------|---------|
| `/inbox` | Gmail | Manhã — ver e-mails das últimas 24h | `/inbox` |
| `/inbox-cliente <nome>` | Gmail | Filtrar e-mails de um cliente específico | `/inbox-cliente camara` |
| `/agenda-email` | Gmail + Calendar | Detectar convites e follow-ups pendentes | `/agenda-email` |
| `/drive-recente` | Google Drive | Ver arquivos novos/atualizados (48h) | `/drive-recente` |
| `/drive-buscar <termo>` | Google Drive | Buscar arquivo específico no Drive | `/drive-buscar "proposta câmara"` |
| `/drive-arquivo <ID>` | Google Drive | Arquivar link de referência no vault | `/drive-arquivo 1abc...` |

## 📥 Fontes Externas — Tier 2 (importação manual)

| Comando | Fonte | Como usar |
|---------|-------|-----------|
| `/whats-importar [arquivo]` | WhatsApp | Exportar grupo como .txt → rodar comando |
| `/audio-importar <arquivo>` | Áudio | `bash scripts/transcrever.sh audio.mp3` → `/audio-importar transcricao.md` |

> **Pré-requisito do áudio:** `pip install openai-whisper` (instalar uma vez)

---

## Regras de ouro dos comandos

- **Nenhum comando publica.** Eles geram, organizam, listam.
- **Todo output nasce em `[F2] claude/outputs/`** — exceto `/ideia` (vai direto pra frente).
- **Todo arquivo gerado tem `revisado: false`** até você aprovar.
- **Em caso de dúvida, o comando pergunta** — nunca presume.
- **`/manutencao` nunca deleta** sem confirmação explícita sua.

---

## Onde ficam os arquivos

| Tipo | Destino |
|------|---------|
| Legendas | `[F2] memory/outputs/legendas/` |
| Roteiros | `[F2] memory/outputs/roteiros/` |
| Posts / Drafts | `[F2] memory/outputs/drafts/` |
| Resumos WhatsApp | `[F2] memory/outputs/resumos-whatsapp/` |
| Daily notes | `[F1] 3-Daily/YYYY-MM-DD.md` |
| Semanais | `[F2] memory/sessions/weekly/YYYY-Www.md` |
| Ideias | `[F1] 5-Frentes/<frente>/Ideias/` |
| Log de sessões | `[F2] memory/sessions/` |
| Inbox externa | `[F2] memory/inbox-externa/` |
| Referências Drive | `[F2] memory/inbox-externa/drive/` |
| WhatsApp processado | `[F2] memory/inbox-externa/whatsapp/processados/` |
| Transcrições de áudio | `[F2] memory/inbox-externa/audio/audio-transcricoes/` |
| Cruzamentos de fontes | `[F2] memory/inbox-externa/cruzados/` |
| Regras de classificação agenda | `[F2] memory/databases/regras-classificacao-agenda.md` |
