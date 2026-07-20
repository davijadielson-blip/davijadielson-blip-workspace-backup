# 🛡️ Matriz de Riscos de Dados Pessoais — Lógika Creative

**Data de criação:** 2026-07-20  
**Responsável:** CIO (Governança & Compliance)  
**Status:** 🟡 Preliminar — revisar trimestralmente

---

## 1. Riscos Identificados

### R1 — Exposição indevida de imagem de terceiros
| Campo | Detalhe |
|---|---|
| **Probabilidade** | 🟡 Média |
| **Impacto** | 🔴 Alto |
| **Risco** | 🔴 **Alto** |
| **Cenário** | Publicar conteúdo com imagem de terceiro sem autorização assinada |
| **Fonte** | Produção de conteúdo (vídeos, fotos, depoimentos) |
| **Controles atuais** | ❌ Nenhum |
| **Ação recomendada** | ✅ Implementar coleta de autorização de imagem prévia |
| **Prazo** | Imediato |
| **Responsável** | CIO / Produção |

### R2 — Vazamento de dados de clientes
| Campo | Detalhe |
|---|---|
| **Probabilidade** | 🟢 Baixa |
| **Impacto** | 🔴 Alto |
| **Risco** | 🟡 **Médio** |
| **Cenário** | Acesso não autorizado a dados contratuais de clientes |
| **Fonte** | Drive compartilhado, e-mail |
| **Controles atuais** | 🟡 Autenticação 2FA no Google |
| **Ação recomendada** | ✅ Segregação de pastas por nível de acesso, revisão de permissões |
| **Prazo** | 30 dias |

### R3 — Tratamento inadequado de dados de saúde
| Campo | Detalhe |
|---|---|
| **Probabilidade** | 🟢 Baixa |
| **Impacto** | 🔴 Alto |
| **Risco** | 🟡 **Médio** |
| **Cenário** | Capturar/armazenar dado de paciente identificado sem base legal |
| **Fonte** | Frente São Sebastião (Saúde) |
| **Controles atuais** | 🟡 Diretriz de usar apenas fontes públicas oficiais |
| **Ação recomendada** | ✅ Incluir cláusula de compliance nos briefings de conteúdo da Saúde |
| **Prazo** | 30 dias |

### R4 — Ausência de canal para direitos do titular
| Campo | Detalhe |
|---|---|
| **Probabilidade** | 🟡 Média |
| **Impacto** | 🟡 Médio |
| **Risco** | 🟡 **Médio** |
| **Cenário** | Titular solicita exclusão/correção de dados e não há resposta em 15 dias |
| **Fonte** | Processo geral |
| **Controles atuais** | ❌ Nenhum |
| **Ação recomendada** | ✅ Definir canal (e-mail) e procedimento de resposta |
| **Prazo** | 15 dias |

### R5 — Retenção excessiva de dados
| Campo | Detalhe |
|---|---|
| **Probabilidade** | 🟡 Média |
| **Impacto** | 🟢 Baixo |
| **Risco** | 🟢 **Baixo** |
| **Cenário** | Manter dados de prospecção/clientes por período superior ao necessário |
| **Fonte** | Processo geral |
| **Controles atuais** | ❌ Nenhum |
| **Ação recomendada** | ✅ Implementar revisão semestral de dados armazenados |
| **Prazo** | 90 dias |

---

## 2. Mapa de Calor de Riscos

```
Impacto
  Alto    | R1          | 
  Médio   |             | R4
  Baixo   |             | R5
          ------------------
          Baixa   Médio   Alta
                  Probabilidade
```

---

## 3. Plano de Ação Prioritário

| Prioridade | Ação | Responsável | Prazo |
|---|---|---|---|
| 🔴 P0 | Criar e exigir autorização de uso de imagem em todo conteúdo com terceiros | CIO / Produção | **Imediato** |
| 🟡 P1 | Revisar permissões de acesso ao Google Drive | CIO | 15 dias |
| 🟡 P2 | Definir canal oficial para direitos do titular | CIO | 15 dias |
| 🟡 P3 | Incluir compliance nos briefings da Frente Saúde | CIO / CCO | 30 dias |
| 🟢 P4 | Implementar revisão semestral de dados retidos | CIO | 90 dias |
| 🟢 P5 | Criar Relatório de Impacto (RIPD) para frentes sensíveis | CIO | 120 dias |

---

## Revisões

| Versão | Data | Responsável | Alterações |
|---|---|---|---|
| 1.0 | 2026-07-20 | CIO | Criação inicial |

---

*Fonte: Cofre (`[F2] memory/context/governanca/MATRIZ-RISCOS-DADOS-LOGIKA.md`)*