# Backlog Inteligente — xTiles e autoalimentação entre fontes

**Data:** 2026-07-19  
**Origem:** Telegram `ESTUDOS`, tópico `Backlog Inteligente`.  
**Contexto:** Jadielson disse que já tem muita coisa no xTiles e que o problema é alimentar dois lugares. Desejo: uma forma de as fontes se autoalimentarem.

## Diagnóstico

O risco real é criar dois sistemas paralelos:

- xTiles com painéis visuais e tarefas;
- Cofre com método, decisões e memória.

Se Jadielson precisar alimentar os dois manualmente, o sistema tende a morrer por atrito.

## Princípio de arquitetura

Não deve haver dois lugares igualmente oficiais para a mesma coisa.

É preciso definir papéis:

```text
xTiles = cockpit visual e operacional humano
Cofre = fonte de verdade histórica, método e memória da Central
Google Calendar = camada de tempo: compromissos e blocos
Central/Agentes = inteligência que transforma, classifica, resume e registra
```

## Caminhos possíveis de autoalimentação

### 1. xTiles como entrada principal

Jadielson mexe no xTiles normalmente. A Central tenta ler/exportar periodicamente o que foi alterado e salva sínteses no Cofre.

Vantagem: respeita o hábito atual de Jadielson.  
Risco: depende de API/export/automação confiável do xTiles.

### 2. Central/Telegram como entrada principal

Jadielson manda demandas no Telegram. A Central estrutura no Cofre e depois gera conteúdo para xTiles.

Vantagem: inteligência mais controlada.  
Risco: Jadielson continua tendo que passar informação fora do xTiles.

### 3. Google Calendar como ponte de tempo

Compromissos e blocos são criados/lidos via Google Calendar com `gog`. O xTiles sincroniza com Calendar.

Vantagem: já existe caminho técnico mais estável.  
Limite: resolve agenda/tempo, mas não resolve painéis, notas e projetos visuais.

### 4. Exportação/importação Markdown/CSV

A Central gera `.md`/CSV para importar no xTiles, ou xTiles exporta conteúdo para arquivamento no Cofre.

Vantagem: simples e seguro para começar.  
Limite: pode ser semi-manual, não 100% automático.

### 5. API/MCP oficial do xTiles

Se disponível na conta/plano, seria o melhor caminho para autoalimentação real.

Possibilidades:
- ler páginas/boards;
- criar cartões/tarefas;
- atualizar status;
- espelhar decisões no Cofre;
- puxar mudanças recentes para revisão da Central.

Exige validação com Lôh por envolver arquitetura, autenticação e segurança.

## Recomendação

Fazer uma prova de conceito com baixo risco:

1. Mapear o que Jadielson já tem no xTiles.
2. Escolher uma área piloto: `Backlog Inteligente`.
3. Verificar se há exportação Markdown/CSV ou API/MCP disponível.
4. Conectar Google Calendar ao xTiles para testar camada de tempo.
5. Definir regra de ouro:
   - xTiles para operação visual diária;
   - Cofre para síntese, decisões e memória;
   - não duplicar tudo, apenas sincronizar o que importa.

## Próxima ação sugerida

Encaminhar para Lôh/arquitetura um pedido de estudo técnico: `integração xTiles ↔ Cofre/Central`, com foco em API/MCP/exportações, segurança e fluxo de sincronização.
