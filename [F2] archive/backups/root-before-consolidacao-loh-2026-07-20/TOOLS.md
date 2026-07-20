---
summary: "Workspace template for TOOLS.md"
read_when:
  - Bootstrapping a workspace manually
---

# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
## Google — acesso oficial via `gog`

Decisão de Jadielson/Lôh: Google não deve ser acessado via Zapier MCP.

Use `gog` e scripts diretos para:

- Google Drive: `gog_drive`
- Gmail: `gog_gmail`
- Google Calendar: `gog_calendar` ou scripts do Cofre
- Google Sheets: `gog`/scripts diretos com OAuth

Antes de qualquer operação Google, carregar ambiente quando necessário:

```bash
cd /data/.openclaw/workspace
source scripts/gog-auth.sh
```

Proibido reabilitar Google no Zapier sem autorização explícita de Jadielson/Lôh.

Decisão: `[F2] memory/decisions/2026-07-14-google-zapier-removido-gog-oficial.md`
