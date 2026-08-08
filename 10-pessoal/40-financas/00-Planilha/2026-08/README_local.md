---
tema: rito local de comprovantes do My Finance em agosto de 2026
conteudo: contexto operacional do envio de comprovantes financeiros ao Drive pessoal e sincronizacao com Cofre e planilha
setor: financeiro pessoal
cliente: Jadielson Davi
tipo: contexto operacional
prioridade: alta
atualizado_em: 2026-08-08
usar_quando: verificar o fluxo de comprovantes do My Finance, pasta Drive oficial e status do ciclo 2026-08
nao_usar_quando: substituir a planilha financeira ou registrar novos comprovantes sem validacao
---

# Rito de comprovantes — Drive pessoal (via gog + Lôh)

Link oficial: https://drive.google.com/drive/folders/1UfyvuOhV9jMUW47tbxGJ5MB1sNIWB4D7
Ferramenta: gog (Google Workspace CLI — /usr/local/bin/gog, OAuth configurado)
Status: configurado; upload bloqueado apenas por GOG_KEYRING_PASSWORD (keyring file backend, sem TTY para prompt).

Regra (reafirmada por Jadielson 2026-08-07):
- Tudo que entrar no My Finance → cofre + planilha + comprovante no Drive do mês exato.
- Rito de pasta: 2026-08, 2026-09, 2026-10 ... (ano-mês, mesma estrutura).
- Não removo do Drive; apenas adiciono no mês de ocorrência.
- Arquivos locais prontos em 00-Planilha/AAAA-MM/ para upload via gog.

Arquivos deste ciclo (2026-08-07):
- 2026-08-07_troca-oleo-moto_R70.pdf
- 2026-08-07_pastilhas-garganta_R18.pdf

## 2026-08-07 19:21 — Upload pelo usuário (Drive liberado)
- Acesso concedido por Jadielson ao Drive: https://drive.google.com/drive/folders/1UfyvuOhV9jMUW47tbxGJ5MB1sNIWB4D7
- Browser indisponível neste runtime; upload feito pelo usuário diretamente (não via gog, conforme autorização "sem necessariamente o gog").
- Arquivos enviados (nome padronizado): 2026-08-07_troca-oleo-moto_R70.pdf | 2026-08-07_pastilhas-garganta_R18.pdf
- Cofre + planilha já sincronizados (nenhuma duplicação).

## 2026-08-08 — Regularização Cofre somente Markdown
- Upload confirmado via `gog` na conta `davijadielson@gmail.com`, pasta Drive `2026/08-Agosto`.
- `2026-08-07_troca-oleo-moto_R70.pdf`: `1vZIM03NMlcUOkpKp58Zx66eJFhiAGBcO` — https://drive.google.com/file/d/1vZIM03NMlcUOkpKp58Zx66eJFhiAGBcO/view?usp=drivesdk
- `2026-08-07_pastilhas-garganta_R18.pdf`: `1J-LYT6GIfRINBbS9yJHIthGj1kKQJiQ-` — https://drive.google.com/file/d/1J-LYT6GIfRINBbS9yJHIthGj1kKQJiQ-/view?usp=drivesdk
- As copias locais dos PDFs foram retiradas do Cofre e preservadas em quarentena local recuperavel: `/data/.openclaw/quarentena-nao-md-exportado-drive/2026-08-08/my-finance/`.
- O Cofre mantem apenas este registro `.md` com resumo, links, IDs e status.
