# Mission Control v1.8 — Proteção de acesso para deploy privado

**Data:** 2026-07-20 02:43 UTC  
**Dono:** Jadielson Davi  
**Orquestração:** Lôh  
**Status:** implementado e testado

## Contexto

Após a preparação de deploy v1.7, a próxima etapa foi adicionar uma camada simples de proteção de acesso para permitir publicação controlada do Mission Control.

## Entrega

Foi implementado um proxy/middleware de Basic Auth opcional no app Next.js.

## Arquivo criado

No app:

`/data/.openclaw/mission-control-next/proxy.js`

## Variáveis adicionadas ao `.env.example`

```env
MISSION_CONTROL_BASIC_AUTH=false
MISSION_CONTROL_USER=jadielson
MISSION_CONTROL_PASSWORD=troque-esta-senha
```

## Como funciona

- Se `MISSION_CONTROL_BASIC_AUTH=false`, o app abre sem senha.
- Se `MISSION_CONTROL_BASIC_AUTH=true`, toda rota exige usuário e senha.
- A senha fica apenas no ambiente do deploy.
- Não há segredo salvo no Cofre.

## Documentação atualizada

`/data/.openclaw/mission-control-next/DEPLOY.md`

Inclui agora:

- instrução de ativação da proteção por senha;
- healthcheck manual;
- reforço de não expor `.env.local`.

## Testes

`npm run build`: OK.

Rotas detectadas:

- `/`
- `/api/logika-crm`
- Proxy/Middleware ativo.

## Observação técnica

No Next.js atual, `middleware.js` está depreciado para esta convenção. A implementação foi ajustada para `proxy.js` com export `proxy`, compatível com o aviso do build.

## Próximo passo recomendado

Escolher o destino do deploy privado/controlado e configurar as variáveis no provedor/servidor.
