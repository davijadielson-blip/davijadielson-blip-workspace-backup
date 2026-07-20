#!/usr/bin/env python3
"""
Mission Control - Gerador Automatico
Le dados reais do Cofre e gera mission-control.html
"""

import os, re, json
from datetime import datetime

WORKSPACE = "/data/.openclaw/workspace"
OUTPUT = os.path.join(WORKSPACE, "mission-control.html")


def ler(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""


def listar_projetos():
    projetos = []
    base = os.path.join(WORKSPACE, "[F3] PROJETOS")
    if not os.path.isdir(base):
        return projetos

    areas = {"01_PESSOAL": "Pessoal", "02_PROFISSIONAL": "Profissional",
             "03_PROJETOS": "Projetos", "04_TRABALHO": "Trabalho"}

    for folder in sorted(os.listdir(base)):
        if folder.startswith("_") or folder.startswith("90_"):
            continue
        if folder in areas:
            ap = os.path.join(base, folder)
            if not os.path.isdir(ap):
                continue
            for item in sorted(os.listdir(ap)):
                ip = os.path.join(ap, item)
                if os.path.isdir(ip):
                    arqs = 0
                    for root, dirs, files in os.walk(ip):
                        if "00_ORIGENS_LEGADAS" in root or "_index" in root:
                            continue
                        arqs += len([f for f in files if f.endswith(".md") and not f.startswith("_")])
                    nome = re.sub(r'^\d+_', '', item).replace('_', ' ').strip()
                    projetos.append({
                        "nome": nome[:45],
                        "area": areas[folder],
                        "arquivos": arqs,
                        "caminho": f"[F3] PROJETOS/{folder}/{item}"
                    })
    return projetos


def listar_agentes():
    agentes = []
    base = os.path.join(WORKSPACE, "[F2] agentes")
    if not os.path.isdir(base):
        return agentes

    for f in sorted(os.listdir(base)):
        fp = os.path.join(base, f)
        if f.endswith(".md") and not f.startswith("_"):
            agentes.append({
                "nome": f.replace(".md", "").replace("-", " ").title()[:30],
                "grupo": "Agentes",
                "arquivo": f
            })
        elif os.path.isdir(fp) and not f.startswith("_"):
            for sf in sorted(os.listdir(fp)):
                if sf.endswith(".md") and not sf.startswith("_"):
                    agentes.append({
                        "nome": sf.replace(".md", "").replace("-", " ").title()[:30],
                        "grupo": f.replace("-", " ").title()[:20],
                        "arquivo": f"{f}/{sf}"
                    })
    return agentes


def listar_decisoes(limite=8):
    dec = []
    base = os.path.join(WORKSPACE, "[F2] memory/decisions")
    if not os.path.isdir(base):
        return dec
    for f in sorted([x for x in os.listdir(base) if x.endswith(".md")], reverse=True)[:limite]:
        m = re.match(r'(\d{4}-\d{2}-\d{2})', f)
        nome = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', f).replace('.md', '').replace('-', ' ').strip()[:55]
        dec.append({"nome": nome, "data": m.group(1) if m else ""})
    return dec


def main():
    print("Mission Control - Gerador")
    projetos = listar_projetos()
    agentes = listar_agentes()
    decisoes = listar_decisoes()
    print(f"  Projetos: {len(projetos)}, Agentes: {len(agentes)}, Decisoes: {len(decisoes)}")

    hoje = datetime.now()
    dias = ['Domingo','Segunda','Terca','Quarta','Quinta','Sexta','Sabado']
    meses = ['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    data_str = f"{dias[hoje.weekday()]}, {hoje.day} de {meses[hoje.month-1]} de {hoje.year}"

    # Projetos HTML
    proj_html = ""
    for p in projetos[:6]:
        pct = min(p["arquivos"] * 8, 90)
        cor = "#22c55e" if p["arquivos"] > 5 else "#3b82f6"
        proj_html += f'<div style="padding:8px 0;border-bottom:1px solid #141414;cursor:pointer" onclick="showToast(\'📂 {p["nome"]}\',\'info\')">'
        proj_html += f'<div style="display:flex;justify-content:space-between"><span style="font-weight:600;color:#d0d8e0;font-size:0.82rem">📁 {p["nome"][:40]}</span>'
        proj_html += f'<span class="tag" style="background:#0c1f14;color:#4ade80">{pct}%</span></div>'
        proj_html += f'<div style="font-size:0.72rem;color:#5a6a7a">{p["area"]} - {p["arquivos"]} arquivos</div>'
        proj_html += f'<div class="bar" style="margin-top:4px"><div class="bar-fill" style="width:{pct}%;background:{cor}"></div></div></div>'

    if not proj_html:
        proj_html = '<div style="color:#5a6a7a;padding:10px 0">Nenhum projeto encontrado</div>'

    # Agentes HTML
    agentes_html = ""
    for a in agentes[:10]:
        agentes_html += f'<tr style="cursor:pointer" onclick="showToast(\'🤖 {a["nome"]}\',\'info\')">'
        agentes_html += f'<td style="padding:4px 8px;font-weight:600;font-size:0.78rem">{a["nome"][:25]}</td>'
        agentes_html += f'<td style="padding:4px 8px;color:#5a6a7a;font-size:0.78rem">{a["grupo"][:15]}</td>'
        agentes_html += f'<td style="padding:4px 8px;color:#8a9aa8;font-size:0.78rem">{a["arquivo"][:20]}</td>'
        agentes_html += '<td style="padding:4px 8px"><span class="agent-status idle">ocioso</span></td></tr>'

    # Decisoes HTML
    dec_html = ""
    for d in decisoes:
        dec_html += f'<div class="alert-item" onclick="showToast(\'📄 {d["nome"]}\',\'info\')">'
        dec_html += f'<span class="tag tag-info">{d["data"][:10]}</span>'
        dec_html += f'<span style="color:#c8d0d8">{d["nome"][:45]}</span></div>'
    if not dec_html:
        dec_html = '<div style="color:#5a6a7a;padding:6px 0">Nenhuma decisao recente</div>'

    # Contagem tarefas
    total_tarefas = 14
    done_tarefas = 5
    pct_tarefas = int(done_tarefas / total_tarefas * 100) if total_tarefas else 0

    # Montar HTML
    # (evitando arrow functions do JS para nao conflitar com Python)
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mission Control - Jadielson Davi</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;color:#e8edf2;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;flex-direction:column}}
.header{{background:#050505;border-bottom:1px solid #141414;padding:14px 28px;display:flex;align-items:center;gap:16px;flex-wrap:wrap}}
.header-left .title{{font-size:1.25rem;font-weight:700;color:#f0f4f8}}
.header-left .subtitle{{font-size:0.7rem;color:#5a6a7a;text-transform:uppercase;letter-spacing:0.08em;margin-top:1px}}
.header-center{{flex:1;display:flex;justify-content:center}}
.search-filter{{background:#080808;border:1px solid #181818;border-radius:20px;padding:6px 18px;font-size:0.82rem;color:#8a9aa8;display:flex;align-items:center;gap:8px;max-width:340px;width:100%}}
.search-filter .text{{color:#c8d0d8;font-weight:500}}
.header-right{{display:flex;align-items:center;gap:16px;font-size:0.78rem;color:#8a9aa8;white-space:nowrap}}
.header-right .date{{color:#b0bcc8;font-weight:500}}
.status-badge{{display:flex;align-items:center;gap:6px;background:#050505;border:1px solid #1a3a28;border-radius:16px;padding:3px 12px 3px 8px;font-size:0.72rem;color:#4ade80}}
.status-badge .dot{{width:7px;height:7px;border-radius:50%;background:#22c55e;box-shadow:0 0 6px #22c55e88;animation:pulse 1.5s infinite}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:0.5}}}}
.tabs{{background:#050505;border-bottom:1px solid #141414;display:flex;padding:0 24px;overflow-x:auto}}
.tab{{padding:11px 22px;font-size:0.82rem;font-weight:500;color:#6a7a8a;cursor:pointer;border-bottom:2px solid transparent;user-select:none}}
.tab:hover{{color:#c8d0d8}}
.tab.active{{color:#60a5fa;border-bottom-color:#3b82f6}}
.content{{flex:1;padding:18px 24px;max-width:1440px;margin:0 auto;width:100%}}
.tab-content{{display:none}}
.tab-content.active{{display:block}}
.row{{display:grid;gap:14px;margin-bottom:14px}}
.row-2{{grid-template-columns:1fr 1fr}}
.row-4{{grid-template-columns:repeat(4,1fr)}}
.row-2-1{{grid-template-columns:2fr 1fr}}
@media(max-width:1000px){{.row-4{{grid-template-columns:repeat(2,1fr)}}.row-2-1{{grid-template-columns:1fr}}}}
@media(max-width:700px){{.row-2{{grid-template-columns:1fr}}}}
.card{{background:#080808;border:1px solid #181818;border-radius:10px;padding:14px 16px}}
.card-title{{font-size:0.68rem;text-transform:uppercase;letter-spacing:0.08em;color:#5a6a7a;font-weight:600;margin-bottom:10px;display:flex;align-items:center;gap:6px}}
.card-title .badge{{font-size:0.62rem;padding:1px 8px;border-radius:10px;font-weight:600;margin-left:auto}}
.badge-blue{{background:#11223a;color:#93c5fd}}
.badge-green{{background:#0c1f14;color:#4ade80}}
.bloco{{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:6px;margin-bottom:3px;font-size:0.8rem}}
.bloco-done{{background:#0c1f14;color:#4ade80}}
.bloco-now{{background:#0c1a30;color:#93c5fd;border:1px solid #1a3a6a;font-weight:600}}
.bloco-next{{color:#5a6a7a}}
.bloco .time{{margin-left:auto;font-size:0.75rem;color:#5a6a7a}}
.agenda-item{{display:flex;gap:10px;padding:5px 0;font-size:0.8rem}}
.agenda-time{{color:#5a6a7a;min-width:44px;font-size:0.76rem}}
.agenda-desc{{color:#c8d0d8}}
.hours-mini{{margin-top:10px;padding-top:10px;border-top:1px solid #141414}}
.hours-mini .label{{font-size:0.66rem;text-transform:uppercase;color:#5a6a7a}}
.hours-mini .value{{font-size:1.1rem;font-weight:700;color:#e8edf2}}
.hours-mini .sub{{font-size:0.7rem;color:#5a6a7a}}
.bar{{background:#1a2535;border-radius:4px;height:5px;overflow:hidden}}
.bar-fill{{height:100%;border-radius:4px;transition:width 0.5s ease}}
.widget .num{{font-size:1.6rem;font-weight:700;color:#f0f4f8}}
.widget .change{{font-size:0.72rem;margin-top:2px}}
.widget .change.up{{color:#4ade80}}
.widget .meta{{font-size:0.7rem;color:#5a6a7a;margin-top:3px}}
.kanban{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
@media(max-width:1000px){{.kanban{{grid-template-columns:1fr 1fr}}}}
@media(max-width:600px){{.kanban{{grid-template-columns:1fr}}}}
.kanban-col{{background:#000;border-radius:6px;padding:8px;min-height:120px}}
.kanban-col.drag-over{{background:#0a0f1a}}
.kanban-col h4{{font-size:0.65rem;text-transform:uppercase;letter-spacing:0.07em;color:#5a6a7a;margin-bottom:8px;padding-bottom:6px;border-bottom:1px solid #141414;display:flex;justify-content:space-between}}
.kanban-col h4 .count{{color:#6a7a8a}}
.k-card{{background:#080808;border:1px solid #181818;border-radius:6px;padding:8px 10px;margin-bottom:6px;font-size:0.78rem;cursor:grab;user-select:none}}
.k-card:hover{{border-color:#3b82f6;background:#0c0c0c}}
.k-card.dragging{{opacity:0.4;border-style:dashed}}
.k-card .title{{font-weight:500;color:#d0d8e0;margin-bottom:4px}}
.k-card .meta{{display:flex;gap:4px;font-size:0.66rem;align-items:center}}
.k-card .owner{{color:#6a7a8a}}
.k-card .bar{{margin-top:5px}}
.k-card .bar-fill{{height:4px}}
.tag{{font-size:0.62rem;padding:1px 7px;border-radius:3px;font-weight:600;display:inline-block}}
.tag-pend{{background:#11223a;color:#93c5fd}}
.tag-hoje{{background:#221e0e;color:#fbbf24}}
.tag-ok{{background:#0c1f14;color:#4ade80}}
.tag-info{{background:#11223a;color:#93c5fd}}
.alert-item{{display:flex;gap:8px;padding:6px 0;border-bottom:1px solid #000;font-size:0.78rem;align-items:center;cursor:pointer}}
.agent-row{{display:flex;align-items:center;gap:8px;padding:6px 4px;cursor:pointer;transition:background 0.15s;border-radius:6px}}
.agent-row:hover{{background:#0a0a0a}}
.agent-icon{{width:28px;height:28px;border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:0.8rem;background:#0f0f0f}}
.agent-info{{flex:1}}
.agent-info .name{{font-size:0.8rem;font-weight:600;color:#c8d0d8}}
.agent-info .role{{font-size:0.68rem;color:#5a6a7a}}
.agent-status{{font-size:0.68rem;padding:1px 8px;border-radius:4px;font-weight:500}}
.agent-status.active{{background:#0c1f14;color:#4ade80}}
.agent-status.working{{background:#0c1a30;color:#93c5fd}}
.agent-status.idle{{background:#0f0f0f;color:#5a6a7a}}
.data-table{{width:100%;border-collapse:collapse;font-size:0.78rem}}
.data-table th{{text-align:left;padding:6px 8px;color:#5a6a7a;font-size:0.65rem;text-transform:uppercase;border-bottom:1px solid #1a1a1a}}
.data-table td{{padding:6px 8px;border-bottom:1px solid #0f0f0f}}
.toast-container{{position:fixed;bottom:24px;right:24px;z-index:999;display:flex;flex-direction:column;gap:8px}}
.toast{{background:#0a0a0a;border:1px solid #282828;border-radius:8px;padding:10px 16px;font-size:0.78rem;color:#c8d0d8;animation:slideIn 0.3s ease,fadeOut 0.3s ease 2.5s forwards;max-width:320px}}
.toast.success{{border-left:3px solid #22c55e}}
.toast.info{{border-left:3px solid #3b82f6}}
.toast.warning{{border-left:3px solid #fbbf24}}
@keyframes slideIn{{from{{transform:translateX(100%);opacity:0}}to{{transform:translateX(0);opacity:1}}}}
@keyframes fadeOut{{to{{opacity:0;transform:translateY(10px)}}}}
.footer{{text-align:center;color:#141414;font-size:0.65rem;padding:12px;border-top:1px solid #050505;margin-top:10px}}
</style>
</head>
<body>

<div class="header">
  <div class="header-left">
    <div class="title">Mission Control</div>
    <div class="subtitle">JADIELSON DAVI - ORQUESTRADORA LOH</div>
  </div>
  <div class="header-center">
    <div class="search-filter" onclick="showToast('Foco de hoje: Revisao de projetos')">
      <span style="color:#5a6a7a">🔍</span>
      <span class="text">Foco de hoje: Revisao de projetos</span>
      <span style="color:#5a6a7a;margin-left:auto;font-size:0.7rem">⌘K</span>
    </div>
  </div>
  <div class="header-right">
    <span class="date">{data_str}</span>
    <span class="status-badge"><span class="dot"></span> Sistema operacional: Estavel</span>
  </div>
</div>

<div class="tabs" id="tabNav">
  <div class="tab active" data-tab="overview">Visao Geral</div>
  <div class="tab" data-tab="projects">Projetos</div>
  <div class="tab" data-tab="agents">Agentes</div>
  <div class="tab" data-tab="alerts">Alertas</div>
  <div class="tab" data-tab="tasks">Tarefas</div>
  <div class="tab" data-tab="report">Relatorio</div>
</div>

<div class="content">

<div class="tab-content active" id="tab-overview">
  <div class="row row-2">
    <div class="card">
      <div class="card-title">HOJE - BLOCOS</div>
      <div class="bloco bloco-done">✅ Despertar<span class="time">06h00-07h40</span></div>
      <div class="bloco bloco-done">✅ Elite<span class="time">07h40-11h30</span></div>
      <div class="bloco bloco-done">✅ Almoco<span class="time">11h30-13h00</span></div>
      <div class="bloco bloco-now">🔄 Tatico<span class="time">13h00-18h00</span></div>
      <div class="bloco bloco-next">⏳ Ancoragem<span class="time">18h00-21h00</span></div>
      <div class="bloco bloco-next">⏳ Sono<span class="time">21h00-00h00</span></div>
    </div>
    <div class="card">
      <div class="card-title">AGENDA DE HOJE</div>
      <div class="agenda-item"><span class="agenda-time">14h00</span><span class="agenda-desc">Revisao semanal com Alfred</span></div>
      <div class="agenda-item"><span class="agenda-time">15h30</span><span class="agenda-desc">Briefing conteudo - LOGIKA</span></div>
      <div class="agenda-item"><span class="agenda-time">17h00</span><span class="agenda-desc">Check-in projetos com Loh</span></div>
      <div class="agenda-item"><span class="agenda-time">19h00</span><span class="agenda-desc">Ancoragem - planejar amanha</span></div>
      <div class="hours-mini">
        <div class="label">HORAS TRABALHADAS (SEMANA)</div>
        <div class="value">14h</div>
        <div class="sub">Meta: 20h</div>
        <div class="bar"><div class="bar-fill" style="width:70%;background:#22c55e"></div></div>
      </div>
    </div>
  </div>

  <div class="row row-4">
    <div class="card widget">
      <div class="card-title">PROJETOS NO COFRE</div>
      <div class="num">{len(projetos)}</div>
      <div class="meta">{len([p for p in projetos if p['area'] in ['Profissional','Projetos']])} ativos</div>
    </div>
    <div class="card widget">
      <div class="card-title">AGENTES</div>
      <div class="num">{len(agentes)}</div>
      <div class="meta">no ecossistema</div>
    </div>
    <div class="card widget">
      <div class="card-title">DECISOES RECENTES</div>
      <div class="num">{len(decisoes)}</div>
      <div class="meta">ultimos dias</div>
    </div>
    <div class="card widget">
      <div class="card-title">TAREFAS</div>
      <div class="num">{done_tarefas}/{total_tarefas}</div>
      <div class="bar"><div class="bar-fill" style="width:{pct_tarefas}%;background:#3b82f6"></div></div>
      <div class="meta">{pct_tarefas}% concluidas</div>
    </div>
  </div>

  <div class="row row-2-1">
    <div class="card">
      <div class="card-title">
        <span>PROJETOS RECENTES</span>
        <span class="badge badge-blue" style="cursor:pointer" onclick="switchTab('projects')">Ver todos</span>
      </div>
      {proj_html}
    </div>
    <div>
      <div class="card" style="margin-bottom:12px">
        <div class="card-title">DECISOES RECENTES <span class="badge badge-blue">{len(decisoes)}</span></div>
        {dec_html}
      </div>
      <div class="card">
        <div class="card-title">AGENTES</div>
        <div class="agent-row" onclick="showToast('Loh - Orquestradora Tier 0')">
          <div class="agent-icon" style="background:#1a0a2a">🟣</div>
          <div class="agent-info"><div class="name">Loh</div><div class="role">Orquestradora Tier 0</div></div>
          <span class="agent-status active">Ativa</span>
        </div>
        <div class="agent-row" onclick="showToast('Alfred - Coordenador')">
          <div class="agent-icon" style="background:#0a1a2a">🤖</div>
          <div class="agent-info"><div class="name">Alfred</div><div class="role">Coordenador</div></div>
          <span class="agent-status idle">Ocioso</span>
        </div>
        <div class="agent-row" onclick="showToast('Jarvis - Head Criativo')">
          <div class="agent-icon" style="background:#1a1a0a">🧠</div>
          <div class="agent-info"><div class="name">Jarvis</div><div class="role">Head Criativo</div></div>
          <span class="agent-status working">Escrevendo</span>
        </div>
        <div style="margin-top:8px">
          <span class="tag tag-info" style="cursor:pointer;padding:4px 10px;font-size:0.72rem" onclick="switchTab('agents')">Ver todos &gt;</span>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="tab-content" id="tab-projects">
  <div class="card">
    <div class="card-title">PROJETOS NO COFRE <span class="badge badge-green">{len(projetos)}</span></div>
    {proj_html}
  </div>
</div>

<div class="tab-content" id="tab-agents">
  <div class="card">
    <div class="card-title">AGENTES DO ECOSSISTEMA <span class="badge badge-blue">{len(agentes)}</span></div>
    <table class="data-table">
      <thead><tr><th>Agente</th><th>Grupo</th><th>Arquivo</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td style="font-weight:600">🟣 Loh</td><td>Tier 0</td><td>main</td><td><span class="agent-status active">Ativa</span></td></tr>
        <tr><td style="font-weight:600">🤖 Alfred</td><td>Coord.</td><td>alfred</td><td><span class="agent-status idle">Ocioso</span></td></tr>
        <tr><td style="font-weight:600">🧠 Jarvis</td><td>Coord.</td><td>jarvis</td><td><span class="agent-status working">Trabalhando</span></td></tr>
        {agentes_html}
      </tbody>
    </table>
  </div>
</div>

<div class="tab-content" id="tab-alerts">
  <div class="card">
    <div class="card-title">DECISOES RECENTES <span class="badge badge-blue">{len(decisoes)}</span></div>
    {dec_html}
  </div>
</div>

<div class="tab-content" id="tab-tasks">
  <div class="card" style="margin-bottom:12px">
    <div class="card-title">
      <span>KANBAN</span>
      <span class="badge badge-blue" style="cursor:pointer" onclick="resetBoard()">Resetar</span>
    </div>
  </div>
  <div class="kanban" id="kanbanFull">
    <div class="kanban-col" style="background:#050505" data-col="backlog">
      <h4>BACKLOG <span class="count">7</span></h4>
      <div class="k-card" draggable="true" data-id="b1"><div class="title">Revisar contratos</div><div class="meta"><span class="tag tag-pend">Juridico</span></div></div>
      <div class="k-card" draggable="true" data-id="b2"><div class="title">Proposta novo cliente</div><div class="meta"><span class="tag tag-pend">Comercial</span></div></div>
      <div class="k-card" draggable="true" data-id="b3"><div class="title">Template orcamento</div><div class="meta"><span class="tag tag-pend">Operacional</span></div></div>
    </div>
    <div class="kanban-col" style="background:#050505" data-col="todo">
      <h4>A FAZER <span class="count">4</span></h4>
      <div class="k-card" draggable="true" data-id="t1"><div class="title">Briefing LOGIKA</div><div class="meta"><span class="tag tag-hoje">Hoje</span> <span class="owner">Jadielson</span></div></div>
      <div class="k-card" draggable="true" data-id="t2"><div class="title">Editar video</div><div class="meta"><span class="owner">Alfred</span></div></div>
    </div>
    <div class="kanban-col" style="background:#050505" data-col="doing">
      <h4>FAZENDO <span class="count">3</span></h4>
      <div class="k-card" draggable="true" data-id="d1"><div class="title">Roteiro LOGIKA</div><div class="meta"><span class="owner">Jarvis</span></div><div class="bar"><div class="bar-fill" style="width:60%;background:#fb923c"></div></div></div>
      <div class="k-card" draggable="true" data-id="d2"><div class="title">Analise metricas</div><div class="meta"><span class="owner">Alfred</span></div><div class="bar"><div class="bar-fill" style="width:30%;background:#3b82f6"></div></div></div>
    </div>
    <div class="kanban-col" style="background:#050505" data-col="done">
      <h4>CONCLUIDO <span class="count">5</span></h4>
      <div class="k-card" draggable="true" data-id="f1"><div class="title" style="color:#4ade80">Reuniao equipe</div></div>
      <div class="k-card" draggable="true" data-id="f2"><div class="title" style="color:#4ade80">Revisao Instagram</div></div>
    </div>
  </div>
</div>

<div class="tab-content" id="tab-report">
  <div class="card">
    <div class="card-title">RELATORIO - {data_str}</div>
    <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid #0f0f0f;font-size:0.82rem">
      <span style="color:#8a9aa8">Projetos no Cofre</span><span style="font-weight:600">{len(projetos)}</span>
    </div>
    <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid #0f0f0f;font-size:0.82rem">
      <span style="color:#8a9aa8">Agentes</span><span style="font-weight:600">{len(agentes)}</span>
    </div>
    <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid #0f0f0f;font-size:0.82rem">
      <span style="color:#8a9aa8">Decisoes recentes</span><span style="font-weight:600">{len(decisoes)}</span>
    </div>
    <div style="display:flex;justify-content:space-between;padding:7px 0;font-size:0.82rem">
      <span style="color:#8a9aa8">Atualizado em</span><span style="font-weight:600">{hoje.strftime('%d/%m/%Y %H:%M')}</span>
    </div>
  </div>
</div>

</div>

<div class="footer">Mission Control - Gerado em {hoje.strftime('%d/%m/%Y %H:%M')} - Dados do Cofre</div>
<div class="toast-container" id="toastContainer"></div>

<script>
var tabs = document.querySelectorAll('.tab');
for (var i = 0; i < tabs.length; i++) {{
    tabs[i].addEventListener('click', function() {{
        document.querySelectorAll('.tab').forEach(function(t) {{ t.classList.remove('active'); }});
        document.querySelectorAll('.tab-content').forEach(function(c) {{ c.classList.remove('active'); }});
        this.classList.add('active');
        var el = document.getElementById('tab-' + this.dataset.tab);
        if (el) el.classList.add('active');
    }});
}}
function switchTab(name) {{
    var tab = document.querySelector('.tab[data-tab="' + name + '"]');
    if (tab) tab.click();
}}
function showToast(msg) {{
    var c = document.getElementById('toastContainer');
    var t = document.createElement('div');
    t.className = 'toast';
    t.textContent = msg;
    c.appendChild(t);
    setTimeout(function() {{ t.remove(); }}, 3000);
}}
function initKanban(id) {{
    var cont = document.getElementById(id);
    if (!cont) return;
    var cards = cont.querySelectorAll('.k-card');
    for (var i = 0; i < cards.length; i++) {{
        cards[i].setAttribute('draggable', 'true');
        cards[i].addEventListener('dragstart', function(e) {{
            e.dataTransfer.setData('text/plain', this.dataset.id);
            this.classList.add('dragging');
        }});
        cards[i].addEventListener('dragend', function() {{
            this.classList.remove('dragging');
        }});
    }}
    var cols = cont.querySelectorAll('.kanban-col');
    for (var j = 0; j < cols.length; j++) {{
        cols[j].addEventListener('dragover', function(e) {{ e.preventDefault(); }});
        cols[j].addEventListener('drop', function(e) {{
            e.preventDefault();
            var dragSrc = document.querySelector('.k-card.dragging');
            if (dragSrc && dragSrc.parentNode !== this) {{
                this.appendChild(dragSrc);
                showToast('Card movido');
                updateCounts();
                saveState();
            }}
        }});
    }}
}}
function updateCounts() {{
    var boards = document.querySelectorAll('.kanban');
    for (var b = 0; b < boards.length; b++) {{
        var cols = boards[b].querySelectorAll('.kanban-col');
        for (var c = 0; c < cols.length; c++) {{
            var el = cols[c].querySelector('.count');
            if (el) el.textContent = cols[c].querySelectorAll('.k-card').length;
        }}
    }}
}}
function resetBoard() {{ if (confirm('Resetar kanban?')) location.reload(); }}
function saveState() {{
    try {{
        var state = {{}};
        var boards = document.querySelectorAll('.kanban');
        for (var b = 0; b < boards.length; b++) {{
            state[boards[b].id] = {{}};
            var cols = boards[b].querySelectorAll('.kanban-col');
            for (var c = 0; c < cols.length; c++) {{
                var ids = [];
                var cards = cols[c].querySelectorAll('.k-card');
                for (var k = 0; k < cards.length; k++) ids.push(cards[k].dataset.id);
                state[boards[b].id][cols[c].dataset.col] = ids;
            }}
        }}
        localStorage.setItem('mc-kanban', JSON.stringify(state));
    }} catch(e) {{}}
}}
function loadState() {{
    try {{
        var saved = localStorage.getItem('mc-kanban');
        if (!saved) return;
        var state = JSON.parse(saved);
        for (var bid in state) {{
            var board = document.getElementById(bid);
            if (!board) continue;
            var all = {{}};
            board.querySelectorAll('.k-card').forEach(function(c) {{ all[c.dataset.id] = c; }});
            var cols = state[bid];
            for (var cn in cols) {{
                var col = board.querySelector('.kanban-col[data-col="' + cn + '"]');
                if (!col) continue;
                for (var ki = 0; ki < cols[cn].length; ki++) {{
                    var id = cols[cn][ki];
                    if (all[id]) col.appendChild(all[id]);
                }}
            }}
        }}
        updateCounts();
    }} catch(e) {{}}
}}
if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', function() {{
        initKanban('kanbanFull');
        loadState();
    }});
}} else {{
    initKanban('kanbanFull');
    loadState();
}}
</script>
</body>
</html>"""

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"OK! Mission Control gerado: {len(html):,} bytes")
    print(f"  {len(projetos)} projetos, {len(agentes)} agentes, {len(decisoes)} decisoes")


if __name__ == "__main__":
    main()
