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
## Integrações — `gog` oficial; Zapier removido

Decisão de Jadielson/Lôh: **Zapier não deve mais ser usado no ecossistema operacional**.

Para Google, use `gog` e scripts diretos:

- Google Drive: `gog_drive`
- Gmail: `gog_gmail`
- Google Calendar: `gog_calendar` ou scripts do Cofre
- Google Sheets: `gog`/scripts diretos com OAuth

Antes de qualquer operação Google, carregar ambiente quando necessário:

```bash
cd /data/.openclaw/workspace
source scripts/gog-auth.sh
```

Proibido reabilitar, reprovisionar ou sugerir Zapier sem autorização explícita posterior de Jadielson.

Decisão: `[F2] memory/decisions/2026-07-20-remocao-total-zapier-gog-oficial.md`
