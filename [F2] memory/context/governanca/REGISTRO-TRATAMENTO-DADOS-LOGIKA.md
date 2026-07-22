---
tema: REGISTRO TRATAMENTO DADOS LOGIKA
atualizado_em: 2026-07-22
---

# 📋 Registro das Operações de Tratamento de Dados Pessoais — Lógika Creative

**Art. 37 LGPD — Obrigação de manutenção de registro**
**Data de criação:** 2026-07-20  
**Responsável:** CIO (Governança & Compliance)  
**Status:** 🟡 Preliminar — expandir conforme novas operações forem mapeadas

---

## 1. Identificação do Controlador

| Campo | Valor |
|---|---|
| Nome empresarial | Lógika Creative |
| Natureza jurídica | MEI |
| Representante | Jadielson Davi |
| Contato | via LÔH / Telegram |
| Canais de comunicação | WhatsApp comercial, e-mail (a definir) |

---

## 2. Mapeamento das Operações

### 2.1 OPERAÇÃO: Atendimento e Orçamento
| Campo | Detalhe |
|---|---|
| **Finalidade** | Responder a solicitações de orçamento, tirar dúvidas, prospectar |
| **Base legal** | Legítimo interesse (Art. 7º, IX) / Execução de contrato (Art. 7º, V) |
| **Dados tratados** | Nome, telefone, e-mail, descrição do projeto |
| **Categoria** | Dados pessoais comuns |
| **Fonte** | Próprio titular (WhatsApp, formulário, Instagram DM) |
| **Titulares** | Clientes potenciais |
| **Compartilhamento** | Nenhum |
| **Prazo de retenção** | 6 meses sem contrato; vigência + 5 anos se contratado |

### 2.2 OPERAÇÃO: Execução de Contrato (Pessoa Física)
| Campo | Detalhe |
|---|---|
| **Finalidade** | Prestação de serviços contratados (foto, vídeo, conteúdo) |
| **Base legal** | Execução de contrato (Art. 7º, V) / Obrigação legal (Art. 7º, II) |
| **Dados tratados** | Nome completo, CPF, endereço, telefone, e-mail |
| **Categoria** | Dados pessoais comuns |
| **Fonte** | Próprio titular |
| **Titulares** | Clientes |
| **Compartilhamento** | Contador (NF), plataformas de entrega |
| **Prazo de retenção** | 5 anos após encerramento do contrato (prazo fiscal) |

### 2.3 OPERAÇÃO: Execução de Contrato (Pessoa Jurídica)
| Campo | Detalhe |
|---|---|
| **Finalidade** | Prestação de serviços contratados |
| **Base legal** | Execução de contrato (Art. 7º, V) / Obrigação legal (Art. 7º, II) |
| **Dados tratados** | Razão Social, CNPJ, dados de contato do representante |
| **Categoria** | Dados pessoais comuns (contato) |
| **Fonte** | Próprio titular |
| **Titulares** | Representantes de PJ |
| **Compartilhamento** | Contador |
| **Prazo de retenção** | 5 anos após encerramento |

### 2.4 OPERAÇÃO: Produção de Conteúdo com Terceiros
| Campo | Detalhe |
|---|---|
| **Finalidade** | Gravação, fotografia, depoimentos para conteúdo editorial/audiovisual |
| **Base legal** | **Consentimento (Art. 7º, I)** |
| **Dados tratados** | Nome, imagem, voz, depoimentos, dados biográficos |
| **Categoria** | Dados pessoais comuns + imagem |
| **Fonte** | Próprio titular |
| **Titulares** | Entrevistados, participantes, modelos |
| **Compartilhamento** | Plataformas de veiculação (YouTube, Instagram, site) |
| **Prazo de retenção** | Vigência da obra + 2 anos |
| **Exigência** | **Autorização de uso de imagem assinada** |

### 2.5 OPERAÇÃO: Pesquisa em Bases Públicas (Frente 872)
| Campo | Detalhe |
|---|---|
| **Finalidade** | Pesquisa para produção de conteúdo informativo |
| **Base legal** | Dados públicos (Art. 7º, §3º / Art. 11, II, "a") |
| **Dados tratados** | Dados de fontes oficiais governamentais |
| **Categoria** | Dados pessoais de fontes públicas |
| **Fonte** | Portais oficiais (Câmara, Prefeitura, Gov.br, DATASUS) |
| **Titulares** | Agentes públicos, profissionais de saúde |
| **Compartilhamento** | Conteúdo publicado (com crédito) |
| **Prazo de retenção** | Enquanto durar a pertinência do conteúdo |

### 2.6 OPERAÇÃO: Conteúdo de Saúde (Frente São Sebastião)
| Campo | Detalhe |
|---|---|
| **Finalidade** | Conteúdo informativo sobre saúde pública municipal |
| **Base legal** | Dados públicos oficiais (Art. 7º, §3º / Art. 11, II, "a") |
| **Dados tratados** | Dados epidemiológicos, serviços, estrutura, profissionais |
| **Categoria** | Dados pessoais + dados de saúde (Art. 11) — **aproveitamento de fontes públicas** |
| **Fonte** | Fontes oficiais governamentais (Prefeitura, DATASUS, Ministério da Saúde) |
| **Titulares** | Profissionais de saúde (dados funcionais públicos) |
| **Compartilhamento** | Conteúdo publicado (com crédito às fontes) |
| **🚫 Restrição** | **Nenhum dado de paciente identificado é tratado ou armazenado.** Apenas dados macro (estatísticos/epidemiológicos) ou de profissionais em exercício público. |

---

## 3. Mapa de Fluxo de Dados

```
Titular → Canal de Captura (WhatsApp/Formulário/Contato direto)
    ↓
Registro no Drive/Workspace (controlado)
    ↓
Processamento (edição, produção de conteúdo)
    ↓
Armazenamento (Google Drive - pastas segregadas)
    ↓
Compartilhamento (contador, plataformas) / Publicação
    ↓
Descarte (após prazo de retenção)
```

---

## 4. Base Legal por Tipo de Titular

| Titular | Base Legal Principal | Consentimento Exigido? |
|---|---|---|
| Cliente PF | Execução de contrato + Obrigação legal | Não (contrato já é base) |
| Cliente PJ (representante) | Legítimo interesse | Não |
| Participante de conteúdo | **Consentimento** | ✅ Sim (autorização de imagem) |
| Entrevistado | **Consentimento** | ✅ Sim (autorização de imagem) |
| Seguidor/visitante (site) | Legítimo interesse | Não (dados de navegação anônimos) |
| Profissional em fonte pública | Dados públicos | Não (dados públicos) |

---

## 5. Revisões

| Versão | Data | Responsável | Alterações |
|---|---|---|---|
| 1.0 | 2026-07-20 | CIO | Criação inicial |

---

*Fonte: Cofre (`[F2] memory/context/governanca/REGISTRO-TRATAMENTO-DADOS-LOGIKA.md`)*