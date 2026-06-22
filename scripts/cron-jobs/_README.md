# Cron-Jobs — Segundo Cérebro

Três rotinas autônomas ativadas via **launchd** (macOS).

---

## Rotinas

| Script | Horário | Output |
|---|---|---|
| `daily-brief.sh` | Todo dia 7h | `[F2] memory/sessions/daily-briefs/YYYY-MM-DD.md` |
| `sunday-planning.sh` | Domingo 8h | `[F2] memory/sessions/weekly/YYYY-Www.md` |
| `friday-maintenance.sh` | Sexta 16h45 | `[F2] memory/sessions/maintenance/YYYY-MM-DD.md` |

---

## Como pausar um cron

```bash
launchctl unload ~/Library/LaunchAgents/com.jadielson.daily-brief.plist
launchctl unload ~/Library/LaunchAgents/com.jadielson.sunday-planning.plist
launchctl unload ~/Library/LaunchAgents/com.jadielson.friday-maintenance.plist
```

## Como reativar

```bash
launchctl load ~/Library/LaunchAgents/com.jadielson.daily-brief.plist
```

## Como editar o horário

1. Edite o `.plist` em `~/Library/LaunchAgents/com.jadielson.<nome>.plist`
2. Altere `<key>Hour</key>` e/ou `<key>Minute</key>`
3. Recarregue: `launchctl unload <plist> && launchctl load <plist>`

## Ver logs de execução

```bash
cat scripts/cron-jobs/.logs/daily-brief.log
cat scripts/cron-jobs/.logs/daily-brief.err
```

## Forçar execução manual

```bash
launchctl start com.jadielson.daily-brief
launchctl start com.jadielson.sunday-planning
launchctl start com.jadielson.friday-maintenance
```

Ou direto:
```bash
bash scripts/cron-jobs/daily-brief.sh
```

## Verificar status

```bash
launchctl list | grep jadielson
```

## Adicionar novo cron

1. Criar o script em `scripts/cron-jobs/nome.sh`
2. `chmod +x scripts/cron-jobs/nome.sh`
3. Criar `.plist` em `~/Library/LaunchAgents/com.jadielson.nome.plist` (copiar modelo de um existente)
4. `launchctl load ~/Library/LaunchAgents/com.jadielson.nome.plist`
5. Documentar aqui e em `scripts/_MAP.md`
