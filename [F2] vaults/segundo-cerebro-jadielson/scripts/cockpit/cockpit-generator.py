#!/usr/bin/env python3
"""
cockpit-generator.py — Gera cockpit.html para o Sistema Operacional Pessoal
Lê: rotina.md, pendencias.md, deadlines.md, Google Calendar (via get-calendar-events.py)
Gera: cockpit.html na raiz do vault
"""

import sys
import os
import datetime
import subprocess
import re

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# ── Blocos da Inversão Biológica ─────────────────────────────────────────────

BLOCOS = [
    {"nome": "Sono",        "inicio": (0,  0), "fim": (6,  0), "cor": "#1a1a2e", "emoji": "😴"},
    {"nome": "Despertar",   "inicio": (6,  0), "fim": (7, 40), "cor": "#16213e", "emoji": "🌅"},
    {"nome": "Elite",       "inicio": (7, 40), "fim": (11,30), "cor": "#0f3460", "emoji": "🟦"},
    {"nome": "Almoço",      "inicio": (11,30), "fim": (13, 0), "cor": "#533483", "emoji": "🍽️"},
    {"nome": "Tático",      "inicio": (13, 0), "fim": (18, 0), "cor": "#6b2d8b", "emoji": "🟥"},
    {"nome": "Ancoragem",   "inicio": (18, 0), "fim": (21, 0), "cor": "#1b4332", "emoji": "🌙"},
    {"nome": "Sono",        "inicio": (21, 0), "fim": (24, 0), "cor": "#1a1a2e", "emoji": "😴"},
]

TETOS = {"SMS": 15*60, "SINDSS": 90, "Câmara": 210}  # em minutos/semana

def minutos_do_dia(h, m):
    return h * 60 + m

def bloco_atual():
    agora = datetime.datetime.now()
    total = minutos_do_dia(agora.hour, agora.minute)
    for b in BLOCOS:
        ini = minutos_do_dia(*b["inicio"])
        fim = minutos_do_dia(*b["fim"])
        if ini <= total < fim:
            restante = fim - total
            return b, restante
    return BLOCOS[-1], 0

def formatar_tempo(minutos):
    h, m = divmod(abs(minutos), 60)
    if h > 0:
        return f"{h}h{m:02d}min"
    return f"{m}min"

def ler_pendencias():
    path = os.path.join(VAULT, "memory/context/pendencias.md")
    criticas = []
    try:
        with open(path, encoding="utf-8") as f:
            capturando = False
            for linha in f:
                if "## 🔴 Críticas" in linha:
                    capturando = True
                    continue
                if capturando and linha.startswith("## "):
                    break
                if capturando and linha.startswith("- [ ]"):
                    criticas.append(linha.strip().replace("- [ ] ", ""))
                    if len(criticas) >= 5:
                        break
    except FileNotFoundError:
        pass
    return criticas

def ler_deadlines():
    path = os.path.join(VAULT, "memory/context/deadlines.md")
    linhas = []
    try:
        with open(path, encoding="utf-8") as f:
            capturando = False
            for linha in f:
                if "## 📅 Próximos" in linha:
                    capturando = True
                    continue
                if capturando and linha.startswith("## "):
                    break
                if capturando and linha.startswith("|") and not linha.startswith("| Data") and "---" not in linha:
                    partes = [p.strip() for p in linha.split("|") if p.strip()]
                    if len(partes) >= 2:
                        linhas.append({"data": partes[0], "desc": partes[1], "frente": partes[2] if len(partes) > 2 else ""})
                    if len(linhas) >= 5:
                        break
    except FileNotFoundError:
        pass
    return linhas

def ler_estudos():
    pasta = os.path.join(VAULT, "ESTUDOS/EM ANDAMENTO")
    estudos = []
    if not os.path.isdir(pasta):
        return estudos
    for arq in sorted(os.listdir(pasta)):
        if not arq.endswith(".md"):
            continue
        path = os.path.join(pasta, arq)
        nome = os.path.splitext(arq)[0]
        subtipo = "curso"
        aulas_c, total_a = 0, 0
        try:
            with open(path, encoding="utf-8") as f:
                conteudo = f.read()
            for linha in conteudo.splitlines():
                if linha.startswith("subtipo:"):
                    subtipo = linha.split(":", 1)[1].strip()
                if linha.startswith("aulas-concluidas:"):
                    try: aulas_c = int(linha.split(":", 1)[1].strip())
                    except: pass
                if linha.startswith("total-aulas:"):
                    try: total_a = int(linha.split(":", 1)[1].strip())
                    except: pass
        except Exception:
            pass
        pct = round((aulas_c / total_a) * 100) if total_a > 0 else 0
        estudos.append({"nome": nome, "subtipo": subtipo, "aulas_c": aulas_c, "total_a": total_a, "pct": pct})
    return estudos

def ler_projetos_por_destino():
    """Lê projetos de EM ANDAMENTO e A INICIAR agrupados por destino-matriz."""
    grupos = {"FOCO": [], "BLOCO": [], "SISTEMA": [], "DELEGAR": [], "CORTAR": []}
    em_andamento = []

    for status_dir in ["EM ANDAMENTO", "A INICIAR"]:
        pasta = os.path.join(VAULT, "PROJETOS", status_dir)
        if not os.path.isdir(pasta):
            continue
        for proj_dir in sorted(os.listdir(pasta)):
            proj_path = os.path.join(pasta, proj_dir)
            if not os.path.isdir(proj_path):
                continue
            main_file = os.path.join(proj_path, f"{proj_dir}.md")
            if not os.path.exists(main_file):
                continue
            try:
                with open(main_file, encoding="utf-8") as f:
                    content = f.read()
                destino_match = re.search(r'^destino-matriz:\s*(\S+)', content, re.MULTILINE)
                destino = destino_match.group(1).strip() if destino_match else "FOCO"
                if destino in grupos:
                    grupos[destino].append(proj_dir)
                if status_dir == "EM ANDAMENTO":
                    em_andamento.append(proj_dir)
            except Exception:
                continue

    return grupos, em_andamento


def captura_recente():
    try:
        result = subprocess.run(
            ["python3", os.path.join(VAULT, "scripts/lib/get-calendar-events.py"), "--format", "html"],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip() if result.returncode == 0 else "<i>⚠️ Erro ao buscar agenda</i>"
    except Exception:
        return "<i>⚠️ Script de agenda não disponível</i>"

def calcular_ancoragem():
    agora = datetime.datetime.now()
    ancoragem = agora.replace(hour=18, minute=0, second=0, microsecond=0)
    diff = int((ancoragem - agora).total_seconds() / 60)
    if diff < 0:
        return f"<span style='color:#4ade80'>Em ancoragem há {formatar_tempo(-diff)}</span>"
    elif diff <= 30:
        return f"<span style='color:#fbbf24'>⚠️ Ancoragem em {formatar_tempo(diff)}</span>"
    else:
        return f"<span style='color:#94a3b8'>Ancoragem em {formatar_tempo(diff)}</span>"

def grade_blocos():
    agora = datetime.datetime.now()
    total_agora = minutos_do_dia(agora.hour, agora.minute)
    itens = []
    blocos_unicos = [
        {"nome": "Despertar",  "inicio": (6,  0), "fim": (7, 40), "emoji": "🌅"},
        {"nome": "Elite",      "inicio": (7, 40), "fim": (11,30), "emoji": "🟦"},
        {"nome": "Almoço",     "inicio": (11,30), "fim": (13, 0), "emoji": "🍽️"},
        {"nome": "Tático",     "inicio": (13, 0), "fim": (18, 0), "emoji": "🟥"},
        {"nome": "Ancoragem",  "inicio": (18, 0), "fim": (21, 0), "emoji": "🌙"},
        {"nome": "Sono",       "inicio": (21, 0), "fim": (24, 0), "emoji": "😴"},
    ]
    for b in blocos_unicos:
        ini = minutos_do_dia(*b["inicio"])
        fim = minutos_do_dia(*b["fim"])
        if total_agora >= fim:
            estado = "✅"
            cls = "bloco-done"
        elif total_agora >= ini:
            estado = "🔄"
            cls = "bloco-atual"
        else:
            estado = "⏳"
            cls = "bloco-futuro"
        itens.append(f'<div class="bloco-item {cls}">{estado} {b["emoji"]} <strong>{b["nome"]}</strong> <span class="bloco-hora">{b["inicio"][0]:02d}h{b["inicio"][1]:02d}–{b["fim"][0]:02d}h{b["fim"][1]:02d}</span></div>')
    return "\n".join(itens)

def gerar_html():
    bloco, restante = bloco_atual()
    agora = datetime.datetime.now()
    criticas = ler_pendencias()
    deadlines = ler_deadlines()
    estudos = ler_estudos()
    grupos_proj, em_andamento = ler_projetos_por_destino()
    agenda_html = captura_recente()
    ancoragem_html = calcular_ancoragem()
    grade_html = grade_blocos()

    criticas_html = "".join(f'<li>{c}</li>' for c in criticas) if criticas else "<li><i>Nenhuma pendência crítica</i></li>"
    deadlines_html = "".join(f'<li><strong>{d["data"]}</strong> — {d["desc"]} <small>({d["frente"]})</small></li>' for d in deadlines) if deadlines else "<li><i>Nenhum deadline próximo</i></li>"

    def barra_estudo(e):
        pct = e["pct"]
        cor = "#22c55e" if pct >= 80 else "#3b82f6"
        prog = f'<div style="font-size:0.75rem;color:#64748b;margin-top:3px">{e["aulas_c"]}/{e["total_a"]} aulas · {pct}%</div><div style="background:#334155;border-radius:3px;height:4px;margin-top:4px;overflow:hidden"><div style="height:100%;border-radius:3px;background:{cor};width:{pct}%"></div></div>' if e["total_a"] > 0 else ""
        return f'<div style="padding:6px 0;border-bottom:1px solid #1e293b"><span style="font-size:0.88rem;color:#e2e8f0">📚 {e["nome"]}</span>{prog}</div>'

    estudos_html = "".join(barra_estudo(e) for e in estudos) if estudos else '<div style="font-size:0.85rem;color:#64748b;font-style:italic">Nenhum estudo em andamento</div>'

    # Card projetos
    _destino_labels = [
        ("FOCO",    "🎯", "#3b82f6"),
        ("BLOCO",   "📦", "#8b5cf6"),
        ("SISTEMA", "⚙️", "#f59e0b"),
        ("DELEGAR", "🤝", "#10b981"),
        ("CORTAR",  "🗑️", "#ef4444"),
    ]
    em_and_html = "".join(
        f'<div style="padding:5px 0;border-bottom:1px solid #1e293b;font-size:0.85rem;color:#4ade80">🚀 {p}</div>'
        for p in em_andamento
    ) if em_andamento else '<div style="font-size:0.82rem;color:#64748b;font-style:italic">Nenhum em andamento — mova um projeto no COCKPIT</div>'
    destinos_badges = "".join(
        f'<span style="background:#1e3a5f;color:{cor};border-radius:6px;padding:3px 8px;font-size:0.78rem;font-weight:600">{emoji} {d} ({len(grupos_proj[d])})</span>'
        for d, emoji, cor in _destino_labels if grupos_proj[d]
    )
    projetos_card_html = f"""
      <div style="margin-bottom:10px">
        <div style="font-size:0.72rem;color:#64748b;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:6px">Em andamento</div>
        {em_and_html}
      </div>
      <div style="font-size:0.72rem;color:#64748b;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:6px">A iniciar — por destino</div>
      <div style="display:flex;flex-wrap:wrap;gap:6px">{destinos_badges}</div>
    """

    hora_formatada = agora.strftime("%H:%M")
    data_formatada = agora.strftime("%A, %d/%m/%Y").capitalize()
    gerado_em = agora.strftime("%H:%M:%S")

    restante_str = formatar_tempo(restante) if restante > 0 else "encerrado"

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🧠 Cockpit Diretor — {agora.strftime('%d/%m/%Y')}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #0f172a; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; min-height: 100vh; }}
    .header {{ background: #1e293b; border-bottom: 1px solid #334155; padding: 16px 24px; display: flex; align-items: center; gap: 24px; }}
    .header-title {{ font-size: 1.1rem; font-weight: 700; color: #f8fafc; }}
    .header-date {{ color: #94a3b8; font-size: 0.9rem; }}
    .bloco-destaque {{ background: {bloco["cor"]}; border: 2px solid #475569; border-radius: 10px; padding: 12px 20px; display: flex; flex-direction: column; margin-left: auto; text-align: right; }}
    .bloco-destaque .nome {{ font-size: 1.3rem; font-weight: 800; color: #f8fafc; }}
    .bloco-destaque .restante {{ font-size: 0.85rem; color: #cbd5e1; }}
    .grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; padding: 20px; }}
    @media (max-width: 900px) {{ .grid {{ grid-template-columns: 1fr 1fr; }} }}
    @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
    .card {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 16px; }}
    .card h3 {{ font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; margin-bottom: 12px; }}
    .bloco-item {{ padding: 6px 8px; border-radius: 6px; margin-bottom: 4px; font-size: 0.88rem; display: flex; align-items: center; gap: 8px; }}
    .bloco-hora {{ color: #64748b; font-size: 0.78rem; margin-left: auto; }}
    .bloco-done {{ background: #0f2417; color: #4ade80; }}
    .bloco-atual {{ background: #1d3a6e; color: #93c5fd; font-weight: 700; border: 1px solid #3b82f6; }}
    .bloco-futuro {{ background: #1e293b; color: #94a3b8; }}
    ul {{ list-style: none; padding: 0; }}
    ul li {{ padding: 6px 0; border-bottom: 1px solid #1e293b; font-size: 0.88rem; color: #cbd5e1; }}
    ul li:last-child {{ border-bottom: none; }}
    .footer {{ display: flex; gap: 16px; padding: 0 20px 20px; }}
    .indicator {{ flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 14px 16px; }}
    .indicator h4 {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; margin-bottom: 6px; }}
    .indicator .valor {{ font-size: 1.1rem; font-weight: 700; color: #f8fafc; }}
    .indicator .sub {{ font-size: 0.8rem; color: #94a3b8; margin-top: 4px; }}
    .prog-bar {{ background: #334155; border-radius: 4px; height: 6px; margin-top: 8px; overflow: hidden; }}
    .prog-fill {{ height: 100%; border-radius: 4px; background: #3b82f6; }}
    .prog-fill.danger {{ background: #ef4444; }}
    .gerado {{ text-align: center; color: #334155; font-size: 0.75rem; padding: 8px; }}
    .agenda-html {{ font-size: 0.88rem; line-height: 1.6; color: #cbd5e1; }}
  </style>
</head>
<body>

<div class="header">
  <div>
    <div class="header-title">🧠 Cockpit Diretor — Jadielson Davi</div>
    <div class="header-date">{data_formatada} · {hora_formatada}</div>
  </div>
  <div class="bloco-destaque">
    <div class="nome">{bloco["emoji"]} {bloco["nome"]}</div>
    <div class="restante">Restante: {restante_str}</div>
  </div>
</div>

<div class="grid">

  <div class="card">
    <h3>🕐 Hoje — Blocos</h3>
    {grade_html}
  </div>

  <div class="card">
    <h3>📅 Agenda</h3>
    <div class="agenda-html">{agenda_html}</div>
  </div>

  <div class="card">
    <h3>🔴 Pendências críticas</h3>
    <ul>{criticas_html}</ul>
  </div>

  <div class="card">
    <h3>📌 Deadlines próximos</h3>
    <ul>{deadlines_html}</ul>
  </div>

  <div class="card" style="grid-column: span 2">
    <h3>📚 Estudos em andamento</h3>
    {estudos_html}
  </div>

  <div class="card" style="grid-column: span 2">
    <h3>🎯 Projetos</h3>
    {projetos_card_html}
  </div>

</div>

<div class="footer">

  <div class="indicator">
    <h4>⏱️ Horas institucionais (semana)</h4>
    <div class="valor">— / 20h</div>
    <div class="sub">SMS —h · SINDSS —h · Câmara —h</div>
    <div class="prog-bar"><div class="prog-fill" style="width: 0%"></div></div>
  </div>

  <div class="indicator">
    <h4>💰 Receita potencial Lógika</h4>
    <div class="valor">R$ —</div>
    <div class="sub">— horas × R$ 96/h</div>
  </div>

  <div class="indicator">
    <h4>🌙 Ancoragem</h4>
    <div class="valor">{ancoragem_html}</div>
    <div class="sub">Meta: 18h00 · Sono: 21h00</div>
  </div>

</div>

<div class="gerado">Gerado em {gerado_em} · atualizar: rodar generate-cockpit.sh novamente</div>

</body>
</html>"""

if __name__ == "__main__":
    html = gerar_html()
    output = os.path.join(VAULT, "cockpit.html")
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ cockpit.html gerado em {output}")
