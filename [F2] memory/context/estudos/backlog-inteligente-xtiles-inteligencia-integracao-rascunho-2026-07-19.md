# Backlog Inteligente — xTiles e integração com a inteligência

**Data:** 2026-07-19  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Contexto:** Jadielson comentou que achou o xTiles muito interessante, parecido com Notion, porém mais personalizável e inclusivo, mas ainda não sabe como integrá-lo à inteligência da Central.

## Leitura inicial

O xTiles pode ser útil como **interface visual humana** do Backlog Inteligente, enquanto o Cofre continua sendo a fonte de verdade e a Central continua sendo a camada de inteligência.

A ideia não deve ser “trocar o Cofre pelo xTiles”. A ideia mais segura é:

```text
Cofre = memória e método
Central/Agentes = inteligência, análise e síntese
xTiles = painel visual e manipulação humana
Google Calendar = tempo real, compromissos e blocos
```

## Modelo recomendado

### 1. xTiles como espelho visual

O xTiles pode representar visualmente:

- Inbox;
- Mapa 360;
- Áreas da vida;
- Projetos/listas;
- Ordem do Dia;
- Revisão Semanal;
- Cursos e estudos;
- Backlog de ideias e pendências.

### 2. Cofre como fonte de verdade

Tudo que for decisão, método, contexto, síntese, plano, checklist e continuidade deve continuar salvo em `.md` no Cofre.

### 3. Integração inicial sem API

Mesmo sem API oficial, é possível integrar por processo:

1. A Central gera estruturas em Markdown/CSV.
2. Jadielson importa ou replica no xTiles.
3. xTiles vira painel visual de uso diário.
4. A Central registra decisões e revisões no Cofre.

### 4. Integração por Google Calendar

Como xTiles integra com Google Calendar, a Central pode usar `gog` para criar/ler eventos e blocos no Google Calendar. O xTiles pode refletir esses compromissos e blocos por sincronização.

### 5. Integração profunda

Se a conta/plano de Jadielson tiver API ou MCP do xTiles, Lôh deve avaliar arquitetura, autenticação, segurança e limites antes de tornar oficial.

## Prova de conceito sugerida

Criar um painel piloto no xTiles chamado `Backlog Inteligente` com:

1. Inbox;
2. Ordem do Dia;
3. Mapa 360;
4. Projetos/Listas;
5. Estudos/Cursos;
6. Revisão Semanal;
7. Incubação.

Depois testar por 7 dias:

- captura rápida;
- mover cartões;
- agendar tarefas;
- sincronizar com Google Calendar;
- revisar pendências;
- comparar atrito contra TickTick/Notion.

## Ponto de arquitetura

Integração oficial com xTiles envolve arquitetura, autenticação, segurança e possível API/MCP. Portanto, deve ser encaminhada para Lôh antes de implementação definitiva.

## Decisão provisória

xTiles é candidato forte para ser a **camada visual inclusiva** do Backlog Inteligente, mas não deve substituir Cofre nem Central. O papel ideal é ser interface de planejamento e execução visual.
