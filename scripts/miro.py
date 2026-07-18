#!/usr/bin/env python3
"""
Integração Miro via API REST — EXCLUSIVO PARA PROJETOS (JACK)
Uso: python3 scripts/miro.py [acao] [args]

ATENÇÃO: Uso restrito ao Jack Lemley e tópicos do GRUPO PROJETOS.
Não utilizar para outros fins sem autorização de Jadielson.

Ações:
  list-boards                             Lista boards
  create-card <board_id> <titulo> [desc]  Cria card
  create-frame <board_id> <tit> [desc]    Cria frame
  add-decision <area> <titulo> <desc>     Card no Mapa Mental Geral
"""

import sys, json, time
import requests

TOKEN = "eyJtaXJvLm9yaWdpbiI6ImV1MDEifQ_wXerP0PpAGBo_XN7JBfR9ml5mqs"
BASE = "https://api.miro.com/v2"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "Accept": "application/json"}
BOARD_ID = "uXjVJI0-H6E="  # "MAPA MENTAL GERAL"

def list_boards():
    r = requests.get(f"{BASE}/boards", headers=HEADERS)
    for b in r.json().get("data", []): print(f"📋 {b['name']}  ({b['id']})")

def create_card(board_id, title, desc=""):
    r = requests.post(f"{BASE}/boards/{board_id}/cards", headers=HEADERS,
                      json={"data": {"title": title, "description": desc}})
    return r.status_code in [200, 201]

def create_frame(board_id, title, desc="", color="#2399F3"):
    r = requests.post(f"{BASE}/boards/{board_id}/frames", headers=HEADERS,
                      json={"data": {"title": title, "description": desc},
                            "style": {"fillColor": color}})
    return r.status_code in [200, 201]

def add_decision(area, title, desc):
    """Adiciona decisão no board Mapa Mental Geral"""
    return create_card(BOARD_ID, f"✅ {title}", desc)

def add_system(area, title, desc):
    """Adiciona card de sistema no board"""
    return create_card(BOARD_ID, f"⚙️ {title}", desc)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    a = sys.argv[1]
    if a == "list-boards": list_boards()
    elif a == "create-card" and len(sys.argv) >= 4:
        ok = create_card(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
        print("✅ OK" if ok else "❌ Falha")
    elif a == "create-frame" and len(sys.argv) >= 4:
        ok = create_frame(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
        print("✅ OK" if ok else "❌ Falha")
    elif a == "add-decision" and len(sys.argv) >= 5:
        ok = add_decision(sys.argv[2], sys.argv[3], sys.argv[4])
        print("✅ OK" if ok else "❌ Falha")
    elif a == "add-system" and len(sys.argv) >= 5:
        ok = add_system(sys.argv[2], sys.argv[3], sys.argv[4])
        print("✅ OK" if ok else "❌ Falha")
    else:
        print("Comando inválido.")
        print(__doc__)
