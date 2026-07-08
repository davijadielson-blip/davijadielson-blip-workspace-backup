#!/bin/bash
# serve-cockpit.sh — Inicia o cockpit interativo em localhost:8765
# Use este quando quiser EDITAR dados. Para só visualizar, use generate-cockpit.sh

VAULT="$(cd "$(dirname "$0")/../.." && pwd)"
python3 "$VAULT/scripts/cockpit/cockpit-server.py"
