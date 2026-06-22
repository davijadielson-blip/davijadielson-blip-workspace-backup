#!/usr/bin/env python3
"""
cockpit-server.py — Cockpit Kanban interativo (localhost:8765)
Projetos e Estudos como quadros Kanban com drag-and-drop real.
Arrastar um card move o .md para a pasta correta no vault.
"""

import os, re, json, datetime, subprocess, shutil
from http.server import HTTPServer, BaseHTTPRequestHandler

VAULT    = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
PORT     = 8765

STATUS_COLS = ["A INICIAR", "EM ANDAMENTO", "PAUSADO", "CONCLUÍDO"]

BLOCOS = [
    {"nome": "Sono",      "ini": (0,  0), "fim": (6,  0), "cor": "#1a1a2e", "emoji": "😴"},
    {"nome": "Despertar", "ini": (6,  0), "fim": (7, 40), "cor": "#16213e", "emoji": "🌅"},
    {"nome": "Elite",     "ini": (7, 40), "fim": (11,30), "cor": "#0f3460", "emoji": "🟦"},
    {"nome": "Almoço",    "ini": (11,30), "fim": (13, 0), "cor": "#533483", "emoji": "🍽️"},
    {"nome": "Tático",    "ini": (13, 0), "fim": (18, 0), "cor": "#6b2d8b", "emoji": "🟥"},
    {"nome": "Ancoragem", "ini": (18, 0), "fim": (21, 0), "cor": "#1b4332", "emoji": "🌙"},
    {"nome": "Sono",      "ini": (21, 0), "fim": (24, 0), "cor": "#1a1a2e", "emoji": "😴"},
]

def mins(h, m): return h * 60 + m

def bloco_atual():
    t = mins(datetime.datetime.now().hour, datetime.datetime.now().minute)
    for b in BLOCOS:
        if mins(*b["ini"]) <= t < mins(*b["fim"]):
            return b, mins(*b["fim"]) - t
    return BLOCOS[-1], 0

def fmt_tempo(m):
    h, r = divmod(abs(m), 60)
    return f"{h}h{r:02d}min" if h else f"{r}min"

# ── leitura ───────────────────────────────────────────────────────────────────

def ler_fm(path):
    dados = {"_path": path, "_nome": os.path.splitext(os.path.basename(path))[0]}
    try:
        txt = open(path, encoding="utf-8").read()
        m = re.match(r"^---\s*\n(.*?)\n---", txt, re.DOTALL)
        if m:
            for l in m.group(1).splitlines():
                if ":" in l:
                    k, _, v = l.partition(":")
                    v = v.strip()
                    if not (v.startswith("[") and "|" in v):
                        dados[k.strip()] = v
    except Exception:
        pass
    return dados

def ler_tipo(tipo):
    """Retorna {status: [card, ...]} lendo todas as pastas de status.
    Suporta estrutura nova (subpasta/subpasta.md) e antiga (arquivo.md plano)."""
    result = {}
    base = os.path.join(VAULT, tipo)
    for status in STATUS_COLS:
        pasta = os.path.join(base, status)
        cards = []
        if os.path.isdir(pasta):
            for item in sorted(os.listdir(pasta)):
                item_path = os.path.join(pasta, item)
                if os.path.isdir(item_path):
                    # Estrutura nova: subpasta com arquivo principal de mesmo nome
                    main = os.path.join(item_path, f"{item}.md")
                    if os.path.exists(main):
                        card = ler_fm(main)
                        card["_status"] = status
                        cards.append(card)
                elif item.endswith(".md"):
                    # Estrutura antiga: arquivo .md direto na pasta
                    card = ler_fm(item_path)
                    card["_status"] = status
                    cards.append(card)
        result[status] = cards
    return result

def ler_tarefas(tipo):
    """Lê tarefas de TAREFAS/TPD ou TAREFAS/TPG. Retorna {"pendente": [...], "feito": [...]}."""
    result = {"pendente": [], "feito": []}
    pasta  = os.path.join(VAULT, "TAREFAS", tipo)
    if not os.path.isdir(pasta):
        return result
    for item in sorted(os.listdir(pasta)):
        if not item.endswith(".md") or item.startswith(".") or item.startswith("_"):
            continue
        path = os.path.join(pasta, item)
        card = ler_fm(path)
        card["_tipo_tarefa"] = tipo
        status = card.get("status", "pendente")
        if status in result:
            result[status].append(card)
    return result

def ler_pendencias():
    path = os.path.join(VAULT, "memory/context/pendencias.md")
    criticas, importantes = [], []
    try:
        secao = None
        for l in open(path, encoding="utf-8"):
            if "## 🔴 Críticas"    in l: secao = "c"; continue
            if "## 🟡 Importantes" in l: secao = "i"; continue
            if l.startswith("## "): secao = None
            if secao and l.startswith("- [ ]"):
                item = l.strip().replace("- [ ] ", "")
                if secao == "c" and len(criticas)   < 5: criticas.append(item)
                if secao == "i" and len(importantes) < 5: importantes.append(item)
    except FileNotFoundError:
        pass
    return criticas, importantes

def ler_deadlines():
    path = os.path.join(VAULT, "memory/context/deadlines.md")
    linhas = []
    try:
        cap = False
        for l in open(path, encoding="utf-8"):
            if "## 📅 Próximos" in l: cap = True; continue
            if cap and l.startswith("## "): break
            if cap and l.startswith("|") and "---" not in l and "Data" not in l:
                p = [x.strip() for x in l.split("|") if x.strip()]
                if len(p) >= 2:
                    linhas.append({"data": p[0], "desc": p[1], "frente": p[2] if len(p) > 2 else ""})
                if len(linhas) >= 6: break
    except FileNotFoundError:
        pass
    return linhas

def agenda_html():
    try:
        r = subprocess.run(
            ["python3", os.path.join(VAULT, "scripts/lib/get-calendar-events.py"), "--format", "html"],
            capture_output=True, text=True, timeout=10)
        return r.stdout.strip() if r.returncode == 0 else "<i>⚠️ Agenda indisponível</i>"
    except Exception:
        return "<i>⚠️ Script de agenda não disponível</i>"

# ── escrita ───────────────────────────────────────────────────────────────────

def atualizar_campo(path, campo, valor):
    try:
        txt  = open(path, encoding="utf-8").read()
        novo = re.sub(rf"^{re.escape(campo)}:.*$", f"{campo}: {valor}", txt, flags=re.MULTILINE)
        if novo == txt:
            novo = re.sub(r"(^---\s*\n.*?)(---)",
                          lambda mo: mo.group(1) + f"{campo}: {valor}\n" + mo.group(2),
                          txt, flags=re.DOTALL, count=1)
        open(path, "w", encoding="utf-8").write(novo)
        return True
    except Exception as e:
        print(f"[ERRO update] {e}"); return False

def mover_arquivo(src_path, tipo, novo_status):
    try:
        src_dir    = os.path.dirname(src_path)
        src_parent = os.path.dirname(src_dir)
        dest_base  = os.path.join(VAULT, tipo, novo_status)
        os.makedirs(dest_base, exist_ok=True)

        # Estrutura nova: src_path é PROJETOS/STATUS/PASTA/PASTA.md
        if os.path.basename(src_parent) in STATUS_COLS and os.path.isdir(src_dir):
            proj_name   = os.path.basename(src_dir)
            dest_dir    = os.path.join(dest_base, proj_name)
            shutil.move(src_dir, dest_dir)
            return os.path.join(dest_dir, os.path.basename(src_path))

        # Estrutura antiga: src_path é PROJETOS/STATUS/arquivo.md
        basename  = os.path.basename(src_path)
        dest_path = os.path.join(dest_base, basename)
        shutil.move(src_path, dest_path)
        return dest_path
    except Exception as e:
        print(f"[ERRO mover] {e}"); return None

def toggle_pendencia(item_text):
    path = os.path.join(VAULT, "memory/context/pendencias.md")
    try:
        txt  = open(path, encoding="utf-8").read()
        novo = re.sub(rf"^- \[ \] {re.escape(item_text)}$",
                      f"- [x] {item_text}", txt, flags=re.MULTILINE)
        open(path, "w", encoding="utf-8").write(novo)
        return True
    except Exception as e:
        print(f"[ERRO pend] {e}"); return False

# ── widgets ───────────────────────────────────────────────────────────────────

def _attrs(path, campo):
    return f'data-path="{path.replace(chr(34), chr(39))}" data-campo="{campo}" onchange="salvar(this)"'

def inp_num(path, campo, val, mn=0, mx=9999):
    return f'<input type="number" class="f-num" value="{int(val or 0)}" min="{mn}" max="{mx}" {_attrs(path,campo)}>'

def inp_txt(path, campo, val, ph=""):
    v = (val or "").replace('"', '&quot;')
    return f'<input type="text" class="f-txt" value="{v}" placeholder="{ph}" {_attrs(path,campo)}>'

def inp_sel(path, campo, val, opcoes):
    opts = "".join(f'<option value="{o}" {"selected" if o==val else ""}>{o}</option>' for o in opcoes)
    return f'<select class="f-sel" {_attrs(path,campo)}>{opts}</select>'

# ── cards ─────────────────────────────────────────────────────────────────────

MATRIZES = ["FOCO", "BLOCO", "DELEGAR", "SISTEMA", "CORTAR"]
CORES_M  = {"FOCO": "#3b82f6", "BLOCO": "#f59e0b", "DELEGAR": "#a855f7",
            "SISTEMA": "#22c55e", "CORTAR": "#ef4444"}

def card_projeto(p):
    path   = p["_path"]
    path_s = path.replace("'", "\\'")
    nome   = (p.get("titulo") or p["_nome"]).replace("<","&lt;").replace(">","&gt;")
    frente = (p.get("frente") or "").replace("<","&lt;")
    fase   = p.get("fase-atual")      or ""
    matriz = p.get("destino-matriz")  or "FOCO"
    review = p.get("proximo-review")  or ""
    cor_m  = CORES_M.get(matriz, "#64748b")

    return f"""<div class="kcard kcard-p" draggable="true" data-path='{path_s}' data-tipo="PROJETOS">
  <div class="kc-nome">{nome}</div>
  {f'<div class="kc-sub">{frente}</div>' if frente else ''}
  <label class="lbl">Fase atual
    {inp_txt(path,"fase-atual",fase,"Execução, planejamento...")}
  </label>
  <div class="kc-row">
    <label class="lbl">Matriz
      {inp_sel(path,"destino-matriz",matriz,MATRIZES)}
    </label>
    <label class="lbl">Review
      {inp_txt(path,"proximo-review",review,"YYYY-MM-DD")}
    </label>
  </div>
  <div class="m-badge" style="background:{cor_m}22;color:{cor_m};border-color:{cor_m}44">{matriz}</div>
</div>"""

def card_estudo(e):
    path   = e["_path"]
    path_s = path.replace("'", "\\'")
    nome   = (e.get("titulo") or e["_nome"]).replace("<","&lt;").replace(">","&gt;")
    instr  = (e.get("instrutor") or e.get("autor") or "").replace("<","&lt;")
    total  = int(e.get("total-aulas")      or 0)
    feitas = int(e.get("aulas-concluidas") or 0)
    prox   = e.get("proxima-aula") or ""
    mod    = e.get("modulo-atual") or ""
    pct    = round((feitas / total) * 100) if total else 0
    cor    = "#22c55e" if pct >= 80 else "#3b82f6" if pct else "#475569"

    barra = (f'<div class="p-label">{feitas}/{total} aulas · {pct}%</div>'
             f'<div class="p-bar"><div class="p-fill" style="width:{pct}%;background:{cor}"></div></div>'
             ) if total else '<div class="p-label" style="color:#334155">configure total-aulas</div>'

    return f"""<div class="kcard kcard-e" draggable="true" data-path='{path_s}' data-tipo="ESTUDOS">
  <div class="kc-nome">{nome}</div>
  {f'<div class="kc-sub">{instr}</div>' if instr else ''}
  {barra}
  <div class="kc-row">
    <label class="lbl">Feitas
      {inp_num(path,"aulas-concluidas",feitas)}
    </label>
    <label class="lbl">Total
      {inp_num(path,"total-aulas",total)}
    </label>
  </div>
  <label class="lbl">Módulo atual
    {inp_txt(path,"modulo-atual",mod,"Módulo 2...")}
  </label>
  <label class="lbl">Próxima aula
    {inp_txt(path,"proxima-aula",prox,"Aula 5...")}
  </label>
</div>"""

def html_kanban(tipo, dados, card_fn):
    CLS  = {"A INICIAR":"col-ini","EM ANDAMENTO":"col-em","PAUSADO":"col-pau","CONCLUÍDO":"col-con"}
    cols = ""
    for status in STATUS_COLS:
        cards = dados.get(status, [])
        cards_html = "".join(card_fn(c) for c in cards) or '<div class="empty-col">solte aqui</div>'
        cols += f"""<div class="kcol {CLS.get(status,'')}" data-tipo="{tipo}" data-status="{status}">
  <div class="kcol-h">
    <span class="kcol-t">{status}</span>
    <span class="kcol-n">{len(cards)}</span>
  </div>
  <div class="kcol-cards">{cards_html}</div>
</div>"""
    return f'<div class="kboard">{cols}</div>'

def _prazo_html(prazo_str):
    if not prazo_str:
        return ""
    try:
        prazo_dt = datetime.datetime.strptime(prazo_str, "%Y-%m-%d")
        hoje = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        diff = (prazo_dt - hoje).days
        if diff < 0:
            cor, txt = "#ef4444", f"⚠️ {prazo_dt.strftime('%d/%m')} (atrasada)"
        elif diff == 0:
            cor, txt = "#f59e0b", "📅 Hoje"
        elif diff == 1:
            cor, txt = "#f59e0b", "📅 Amanhã"
        else:
            cor, txt = "#64748b", f"📅 {prazo_dt.strftime('%d/%m')}"
        return f'<div class="tc-prazo" style="color:{cor}">{txt}</div>'
    except Exception:
        return f'<div class="tc-prazo" style="color:#64748b">📅 {prazo_str}</div>'

def card_tarefa(t):
    path    = t["_path"]
    path_s  = path.replace("'", "\\'")
    tipo    = t.get("_tipo_tarefa", "TPD")
    nome    = (t.get("titulo") or t["_nome"]).replace("<","&lt;").replace(">","&gt;")
    frente  = (t.get("frente") or "").replace("<","&lt;")
    projeto = (t.get("projeto") or "").replace("<","&lt;")
    prazo   = t.get("prazo") or ""
    status  = t.get("status", "pendente")
    done    = status == "feito"
    done_cls = " tcard-done" if done else ""
    btn_txt  = "↩️ Reabrir" if done else "✓ Feita"
    cor_tipo = "#ef4444" if tipo == "TPD" else "#22c55e"

    projeto_html = f'<div class="tc-projeto">📁 {projeto}</div>' if projeto else ""
    frente_html  = f'<div class="tc-frente">{frente}</div>' if frente else ""
    prazo_html   = _prazo_html(prazo)

    return (f'<div class="tcard{done_cls}" draggable="true" '
            f'data-path=\'{path_s}\' data-tipo="{tipo}">'
            f'<div class="tc-nome" style="border-left:3px solid {cor_tipo};padding-left:6px">{nome}</div>'
            f'{projeto_html}{frente_html}{prazo_html}'
            f'<button class="tc-btn" onclick="toggleTarefa(this)">{btn_txt}</button>'
            f'</div>')

def html_tarefas_board(tpd, tpg):
    def col(tipo, status, cards, label, cor):
        cards_html = "".join(card_tarefa(c) for c in cards) or '<div class="empty-col">nenhuma</div>'
        n = len(cards)
        return (f'<div class="tcol" data-tipo="{tipo}" data-status="{status}">'
                f'<div class="tcol-h">'
                f'<span class="tcol-t" style="color:{cor}">{label}</span>'
                f'<span class="kcol-n">{n}</span></div>'
                f'<div class="tcol-cards">{cards_html}</div></div>')

    return ('<div class="tboard">'
            + col("TPD", "pendente", tpd["pendente"], "🔴 Prevenção de Dor",  "#ef4444")
            + col("TPD", "feito",    tpd["feito"],    "✅ Feitas (TPD)",       "#4ade80")
            + col("TPG", "pendente", tpg["pendente"], "🟢 Produção de Ganho", "#22c55e")
            + col("TPG", "feito",    tpg["feito"],    "✅ Feitas (TPG)",       "#4ade80")
            + '</div>')

def html_grade_blocos():
    t = mins(datetime.datetime.now().hour, datetime.datetime.now().minute)
    itens = []
    for b in BLOCOS:
        if b["ini"] == (0, 0): continue
        ini, fim = mins(*b["ini"]), mins(*b["fim"])
        if t >= fim:   estado, cls = "✅", "b-done"
        elif t >= ini: estado, cls = "🔄", "b-ativo"
        else:          estado, cls = "⏳", "b-fut"
        itens.append(
            f'<div class="b-item {cls}">{estado} {b["emoji"]} <b>{b["nome"]}</b>'
            f'<span class="b-hora">{b["ini"][0]:02d}h{b["ini"][1]:02d}–{b["fim"][0]:02d}h{b["fim"][1]:02d}</span></div>')
    return "\n".join(itens)

# ── página ────────────────────────────────────────────────────────────────────

def gerar_pagina():
    agora = datetime.datetime.now()
    bloco, rest = bloco_atual()

    proj_dados = ler_tipo("PROJETOS")
    est_dados  = ler_tipo("ESTUDOS")
    tpd_dados  = ler_tarefas("TPD")
    tpg_dados  = ler_tarefas("TPG")
    criticas, importantes = ler_pendencias()
    deadlines = ler_deadlines()
    ag    = agenda_html()
    grade = html_grade_blocos()

    data_fmt = agora.strftime("%A, %d/%m/%Y").capitalize()
    hora_fmt = agora.strftime("%H:%M")
    rest_str = fmt_tempo(rest) if rest else "encerrado"

    anc      = agora.replace(hour=18, minute=0, second=0, microsecond=0)
    diff_anc = int((anc - agora).total_seconds() / 60)
    if diff_anc < 0:
        anc_txt = f'<span style="color:#4ade80">Ancorado há {fmt_tempo(-diff_anc)}</span>'
    elif diff_anc <= 30:
        anc_txt = f'<span style="color:#fbbf24">⚠️ Ancoragem em {fmt_tempo(diff_anc)}</span>'
    else:
        anc_txt = f'<span style="color:#94a3b8">Ancoragem em {fmt_tempo(diff_anc)}</span>'

    n_em_proj = len(proj_dados.get("EM ANDAMENTO", []))
    n_em_est  = len(est_dados.get("EM ANDAMENTO", []))

    def pend_li(txt, extra=""):
        safe = txt.replace("'", "&#39;").replace('"', "&quot;")
        return f'<li data-item="{safe}" onclick="concluirPend(this)">{extra}{txt}</li>'

    crit_html = "".join(pend_li(c, "🔴 ") for c in criticas) or "<li><i>Nenhuma</i></li>"
    imp_html  = "".join(pend_li(i)         for i in importantes) or "<li><i>Nenhuma</i></li>"
    dl_html   = "".join(
        f'<li><b>{d["data"]}</b> — {d["desc"]} <small>({d["frente"]})</small></li>'
        for d in deadlines) or "<li><i>Nenhum</i></li>"

    kanban_proj  = html_kanban("PROJETOS", proj_dados, card_projeto)
    kanban_est   = html_kanban("ESTUDOS",  est_dados,  card_estudo)
    tarefas_html = html_tarefas_board(tpd_dados, tpg_dados)
    n_tpd_pend   = len(tpd_dados["pendente"])
    n_tpg_pend   = len(tpg_dados["pendente"])

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>🧠 Cockpit — {agora.strftime('%d/%m/%Y')}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#080d1a;color:#e2e8f0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;min-height:100vh}}

/* HEADER */
.hd{{background:#0f172a;border-bottom:2px solid #1e293b;padding:12px 18px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100}}
.hd-l h1{{font-size:.92rem;font-weight:800;letter-spacing:.02em}}
.hd-l p{{font-size:.72rem;color:#64748b;margin-top:2px}}
.bloco-b{{background:{bloco["cor"]};border:1px solid #475569;border-radius:8px;padding:7px 14px;text-align:right}}
.bloco-b .bn{{font-size:.95rem;font-weight:800}}
.bloco-b .br{{font-size:.68rem;color:#cbd5e1}}

/* INFO STRIP */
.info{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:12px 14px}}
@media(max-width:900px){{.info{{grid-template-columns:1fr 1fr}}}}
.icard{{background:#0f172a;border:1px solid #1e293b;border-radius:10px;padding:11px 13px}}
.icard h3{{font-size:.62rem;text-transform:uppercase;letter-spacing:.08em;color:#334155;margin-bottom:7px}}
.icard ul{{list-style:none}}
.icard li{{font-size:.76rem;color:#cbd5e1;padding:3px 0;border-bottom:1px solid #080d1a}}
.icard li:last-child{{border-bottom:none}}
.icard li[data-item]{{cursor:pointer;transition:all .2s}}
.icard li[data-item]:hover{{text-decoration:line-through;color:#475569}}
.ag-html{{font-size:.76rem;line-height:1.6;color:#94a3b8}}
.b-item{{display:flex;align-items:center;gap:5px;font-size:.73rem;padding:2px 0}}
.b-hora{{margin-left:auto;color:#334155;font-size:.65rem}}
.b-done{{color:#4ade80}}
.b-ativo{{color:#93c5fd;font-weight:700}}
.b-fut{{color:#334155}}

/* KANBAN */
.ksec{{padding:10px 14px 4px}}
.ksec-h{{font-size:.75rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;color:#475569;margin-bottom:8px;display:flex;align-items:center;gap:6px}}
.ksec-h em{{font-style:normal;font-weight:400;font-size:.65rem;color:#334155;text-transform:none;letter-spacing:0}}
.kboard{{display:flex;gap:10px;overflow-x:auto;padding-bottom:10px}}
.kboard::-webkit-scrollbar{{height:4px}}
.kboard::-webkit-scrollbar-thumb{{background:#1e293b;border-radius:2px}}

.kcol{{min-width:240px;flex:1;background:#0f172a;border:1px solid #1e293b;border-radius:12px;display:flex;flex-direction:column;max-height:68vh;transition:border-color .2s}}
.kcol.drag-over{{border-color:#3b82f6;background:#0c1829}}
.kcol-h{{padding:9px 12px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #1e293b;flex-shrink:0}}
.kcol-t{{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em}}
.kcol-n{{font-size:.68rem;background:#1e293b;color:#64748b;border-radius:20px;padding:1px 8px;min-width:20px;text-align:center}}
.col-ini .kcol-t{{color:#64748b}}
.col-em  .kcol-t{{color:#3b82f6}}
.col-pau .kcol-t{{color:#f59e0b}}
.col-con .kcol-t{{color:#22c55e}}
.kcol-cards{{overflow-y:auto;padding:8px;display:flex;flex-direction:column;gap:6px;flex:1}}
.kcol-cards::-webkit-scrollbar{{width:3px}}
.kcol-cards::-webkit-scrollbar-thumb{{background:#1e293b}}
.empty-col{{text-align:center;color:#1e293b;font-size:.72rem;padding:20px 8px;border:1px dashed #1e293b;border-radius:8px}}
.kcol.drag-over .empty-col{{border-color:#3b82f6;color:#3b82f6}}

/* CARDS */
.kcard{{background:#080d1a;border:1px solid #1e293b;border-radius:8px;padding:10px;cursor:grab;transition:border-color .2s,box-shadow .2s;user-select:none}}
.kcard:hover{{border-color:#334155}}
.kcard:active{{cursor:grabbing}}
.kcard.dragging{{opacity:.45;box-shadow:0 12px 32px rgba(0,0,0,.5)}}
.kcard-p:hover{{border-color:#a855f733}}
.kcard-e:hover{{border-color:#3b82f633}}
.kc-nome{{font-size:.8rem;font-weight:700;color:#f1f5f9;line-height:1.3;margin-bottom:1px}}
.kc-sub{{font-size:.65rem;color:#334155;margin-bottom:6px}}
.kc-row{{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}}
.m-badge{{display:inline-block;font-size:.6rem;font-weight:700;padding:1px 7px;border-radius:20px;border:1px solid;margin-top:5px}}

/* CAMPOS */
.lbl{{font-size:.62rem;color:#334155;display:flex;flex-direction:column;gap:2px;margin-top:4px;width:100%}}
.kc-row .lbl{{width:auto;flex:1;min-width:60px}}
.f-num{{width:56px;background:#0f172a;border:1px solid #1e293b;border-radius:5px;color:#e2e8f0;padding:3px 5px;font-size:.78rem;text-align:center;transition:border-color .2s}}
.f-txt{{width:100%;background:#0f172a;border:1px solid #1e293b;border-radius:5px;color:#e2e8f0;padding:3px 7px;font-size:.73rem;transition:border-color .2s}}
.f-sel{{width:100%;background:#0f172a;border:1px solid #1e293b;border-radius:5px;color:#e2e8f0;padding:3px 5px;font-size:.73rem;transition:border-color .2s}}
.f-num:focus,.f-txt:focus,.f-sel:focus{{outline:none;border-color:#3b82f6}}
.f-num.ok,.f-txt.ok,.f-sel.ok{{border-color:#22c55e!important}}
.f-num.er,.f-txt.er,.f-sel.er{{border-color:#ef4444!important}}

/* BARRA */
.p-label{{font-size:.64rem;color:#475569;margin:4px 0 2px}}
.p-bar{{background:#1e293b;border-radius:3px;height:4px;overflow:hidden;margin-bottom:4px}}
.p-fill{{height:100%;border-radius:3px;transition:width .4s,background .4s}}

/* TAREFAS BOARD */
.tboard{{display:flex;gap:10px;overflow-x:auto;padding-bottom:10px}}
.tboard::-webkit-scrollbar{{height:4px}}
.tboard::-webkit-scrollbar-thumb{{background:#1e293b;border-radius:2px}}
.tcol{{min-width:220px;flex:1;background:#0f172a;border:1px solid #1e293b;border-radius:12px;display:flex;flex-direction:column;max-height:50vh;transition:border-color .2s}}
.tcol.drag-over{{border-color:#3b82f6;background:#0c1829}}
.tcol-h{{padding:9px 12px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #1e293b;flex-shrink:0}}
.tcol-t{{font-size:.65rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em}}
.tcol-cards{{overflow-y:auto;padding:8px;display:flex;flex-direction:column;gap:5px;flex:1}}
.tcol-cards::-webkit-scrollbar{{width:3px}}
.tcol-cards::-webkit-scrollbar-thumb{{background:#1e293b}}
.tcard{{background:#080d1a;border:1px solid #1e293b;border-radius:8px;padding:8px 10px;transition:border-color .2s,opacity .3s;cursor:grab}}
.tcard:hover{{border-color:#334155}}
.tcard:active{{cursor:grabbing}}
.tcard.dragging{{opacity:.45}}
.tcard.drag-over-t{{border-color:#3b82f6}}
.tcard-done{{opacity:.55}}
.tcard-done .tc-nome{{text-decoration:line-through;color:#475569}}
.tc-nome{{font-size:.78rem;font-weight:700;color:#f1f5f9;line-height:1.3;margin-bottom:3px}}
.tc-projeto{{font-size:.64rem;color:#3b82f6;margin-bottom:2px}}
.tc-frente{{font-size:.62rem;color:#334155;margin-bottom:2px}}
.tc-prazo{{font-size:.64rem;margin-bottom:4px}}
.tc-btn{{background:#0f172a;border:1px solid #1e293b;color:#64748b;border-radius:5px;padding:2px 8px;font-size:.62rem;cursor:pointer;margin-top:3px;transition:all .2s;width:100%}}
.tc-btn:hover{{border-color:#22c55e;color:#22c55e}}
.tcard-done .tc-btn{{border-color:#334155;color:#475569}}
.tcard-done .tc-btn:hover{{border-color:#3b82f6;color:#3b82f6}}

/* FOOTER */
.footer{{display:flex;gap:10px;padding:10px 14px 16px;flex-wrap:wrap}}
.ind{{flex:1;min-width:140px;background:#0f172a;border:1px solid #1e293b;border-radius:10px;padding:10px 12px}}
.ind h4{{font-size:.6rem;text-transform:uppercase;letter-spacing:.07em;color:#334155;margin-bottom:3px}}
.ind .val{{font-size:.95rem;font-weight:700}}
.ind .sub{{font-size:.68rem;color:#475569;margin-top:2px}}

/* TOAST */
#toast{{position:fixed;bottom:14px;right:14px;background:#22c55e;color:#fff;padding:6px 14px;border-radius:8px;font-size:.78rem;font-weight:700;opacity:0;transition:opacity .25s;pointer-events:none;z-index:999}}
#toast.show{{opacity:1}}
#toast.er{{background:#ef4444}}

/* utils */
.reload-btn{{background:transparent;border:1px solid #1e293b;color:#334155;border-radius:5px;padding:2px 8px;font-size:.65rem;cursor:pointer;margin-left:8px;vertical-align:middle}}
.reload-btn:hover{{border-color:#3b82f6;color:#e2e8f0}}
.sep{{border:none;border-top:1px solid #1e293b;margin:0 14px}}
.gerado{{text-align:center;color:#1e293b;font-size:.62rem;padding:6px 0 12px}}
</style>
</head>
<body>

<!-- HEADER -->
<div class="hd">
  <div class="hd-l">
    <h1>🧠 Cockpit Diretor — Jadielson Davi</h1>
    <p>{data_fmt} · {hora_fmt}
      <button class="reload-btn" onclick="location.reload()">↺ atualizar</button>
    </p>
  </div>
  <div class="bloco-b">
    <div class="bn">{bloco["emoji"]} {bloco["nome"]}</div>
    <div class="br">Restante: {rest_str}</div>
  </div>
</div>

<!-- INFO STRIP: 4 cards informativos -->
<div class="info">
  <div class="icard">
    <h3>🕐 Blocos do dia</h3>
    {grade}
  </div>
  <div class="icard">
    <h3>📅 Agenda</h3>
    <div class="ag-html">{ag}</div>
  </div>
  <div class="icard">
    <h3>⚠️ Pendências <span style="color:#334155;font-size:.8em;font-weight:400">(clique = concluir)</span></h3>
    <ul>{crit_html}</ul>
    <div style="margin:7px 0 4px;font-size:.6rem;text-transform:uppercase;letter-spacing:.07em;color:#334155">Importantes</div>
    <ul>{imp_html}</ul>
  </div>
  <div class="icard">
    <h3>📌 Deadlines</h3>
    <ul>{dl_html}</ul>
  </div>
</div>

<hr class="sep">

<!-- TAREFAS -->
<div class="ksec">
  <div class="ksec-h">✅ Tarefas
    <em>— {n_tpd_pend} TPD · {n_tpg_pend} TPG pendentes · arraste entre colunas ou clique ✓</em>
  </div>
  {tarefas_html}
</div>

<hr class="sep" style="margin-top:10px">

<!-- KANBAN PROJETOS -->
<div class="ksec">
  <div class="ksec-h">🚀 Projetos <em>— arraste para mudar status · edite campos direto no card</em></div>
  {kanban_proj}
</div>

<hr class="sep" style="margin-top:10px">

<!-- KANBAN ESTUDOS -->
<div class="ksec">
  <div class="ksec-h">📚 Estudos <em>— arraste para mudar status · edite progresso direto no card</em></div>
  {kanban_est}
</div>

<hr class="sep" style="margin-top:10px">

<!-- FOOTER -->
<div class="footer">
  <div class="ind"><h4>🌙 Ancoragem</h4><div class="val">{anc_txt}</div><div class="sub">Meta: 18h · Sono: 21h</div></div>
  <div class="ind"><h4>🚀 Projetos ativos</h4><div class="val" id="cnt-proj">{n_em_proj}</div><div class="sub">máx. recomendado: 3</div></div>
  <div class="ind"><h4>📚 Estudos ativos</h4><div class="val" id="cnt-est">{n_em_est}</div><div class="sub">máx. recomendado: 3</div></div>
  <div class="ind"><h4>⏱️ Horas institucionais</h4><div class="val">— / 20h</div><div class="sub">SMS · SINDSS · Câmara</div></div>
</div>

<div class="gerado">localhost:{PORT} · gerado {agora.strftime('%H:%M:%S')} · drag = move arquivo de pasta · campos salvam direto no .md</div>
<div id="toast"></div>

<script>
// ── Toast ──────────────────────────────────────────────────────────────────────
let _tt;
function toast(msg, er) {{
  const t = document.getElementById('toast');
  t.textContent = msg; t.className = er ? 'show er' : 'show';
  clearTimeout(_tt); _tt = setTimeout(() => t.className = '', 2400);
}}

// ── Salvar campo ───────────────────────────────────────────────────────────────
async function salvar(el) {{
  el.classList.remove('ok','er');
  try {{
    const r = await fetch('/update', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{arquivo: el.dataset.path, campo: el.dataset.campo, valor: el.value}})
    }});
    el.classList.add(r.ok ? 'ok' : 'er');
    setTimeout(() => el.classList.remove('ok','er'), 2000);
    if (r.ok) {{
      if (['aulas-concluidas','total-aulas'].includes(el.dataset.campo))
        atualizarBarra(el.closest('.kcard'));
      if (el.dataset.campo === 'destino-matriz')
        atualizarMatriz(el.closest('.kcard'), el.value);
      toast('✅ Salvo');
    }} else {{ toast('❌ Erro ao salvar', true); }}
  }} catch {{ el.classList.add('er'); toast('❌ Servidor offline', true); }}
}}

function atualizarBarra(card) {{
  const c = parseInt(card.querySelector('[data-campo="aulas-concluidas"]')?.value) || 0;
  const t = parseInt(card.querySelector('[data-campo="total-aulas"]')?.value)      || 0;
  const pct = t ? Math.round(c/t*100) : 0;
  const lbl  = card.querySelector('.p-label');
  const fill = card.querySelector('.p-fill');
  if (lbl)  lbl.textContent = c+'/'+t+' aulas · '+pct+'%';
  if (fill) {{ fill.style.width = pct+'%'; fill.style.background = pct>=80?'#22c55e':pct?'#3b82f6':'#475569'; }}
}}

const COR_M = {{FOCO:'#3b82f6',BLOCO:'#f59e0b',DELEGAR:'#a855f7',SISTEMA:'#22c55e',CORTAR:'#ef4444'}};
function atualizarMatriz(card, val) {{
  const b = card.querySelector('.m-badge');
  if (!b) return;
  b.textContent = val;
  const c = COR_M[val] || '#64748b';
  b.style.color=c; b.style.background=c+'22'; b.style.borderColor=c+'44';
}}

// ── Concluir pendência ─────────────────────────────────────────────────────────
async function concluirPend(el) {{
  const r = await fetch('/toggle-pend', {{
    method:'POST', headers:{{'Content-Type':'application/json'}},
    body: JSON.stringify({{item: el.dataset.item}})
  }});
  if (r.ok) {{
    el.style.textDecoration = 'line-through'; el.style.opacity = '.35';
    setTimeout(() => el.remove(), 700);
    toast('✅ Concluída');
  }} else {{ toast('❌ Erro', true); }}
}}

// ── Toggle Tarefa (botão ✓ / ↩️) ──────────────────────────────────────────────
async function toggleTarefa(btn) {{
  const card     = btn.closest('.tcard');
  const path     = card.dataset.path;
  const tipo     = card.dataset.tipo;
  const isDone   = card.classList.contains('tcard-done');
  const novoStatus = isDone ? 'pendente' : 'feito';
  try {{
    const r = await fetch('/update', {{
      method: 'POST',
      headers: {{'Content-Type': 'application/json'}},
      body: JSON.stringify({{arquivo: path, campo: 'status', valor: novoStatus}})
    }});
    if (r.ok) {{
      const targetCol = document.querySelector(`.tcol[data-tipo="${{tipo}}"][data-status="${{novoStatus}}"]`);
      if (targetCol) {{
        const zone = targetCol.querySelector('.tcol-cards');
        const ph   = zone.querySelector('.empty-col');
        if (ph) ph.remove();
        if (isDone) {{
          card.classList.remove('tcard-done');
          btn.textContent = '✓ Feita';
        }} else {{
          card.classList.add('tcard-done');
          btn.textContent = '↩️ Reabrir';
        }}
        zone.appendChild(card);
        atualizarContadoresTarefas();
        toast(isDone ? '↩️ Reaberta' : '✅ Feita!');
      }}
    }} else {{ toast('❌ Erro', true); }}
  }} catch {{ toast('❌ Servidor offline', true); }}
}}

function atualizarContadoresTarefas() {{
  document.querySelectorAll('.tcol').forEach(col => {{
    const n = col.querySelectorAll('.tcard').length;
    const badge = col.querySelector('.kcol-n');
    if (badge) badge.textContent = n;
  }});
}}

// ── Drag & Drop Kanban + Tarefas ──────────────────────────────────────────────
let dragCard = null;

document.querySelectorAll('.kcard, .tcard').forEach(card => {{
  card.addEventListener('dragstart', e => {{
    dragCard = card;
    card.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
  }});
  card.addEventListener('dragend', () => {{
    if (dragCard) dragCard.classList.remove('dragging');
    document.querySelectorAll('.kcol, .tcol').forEach(c => c.classList.remove('drag-over'));
    dragCard = null;
  }});
}});

document.querySelectorAll('.kcol').forEach(col => {{
  col.addEventListener('dragover', e => {{
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    col.classList.add('drag-over');
  }});
  col.addEventListener('dragleave', e => {{
    if (!col.contains(e.relatedTarget)) col.classList.remove('drag-over');
  }});
  col.addEventListener('drop', async e => {{
    e.preventDefault();
    col.classList.remove('drag-over');
    if (!dragCard || !dragCard.classList.contains('kcard')) return;
    if (col.dataset.tipo !== dragCard.dataset.tipo) {{
      toast('❌ Não misture Projetos com Estudos', true); return;
    }}
    const novoStatus = col.dataset.status;
    const path = dragCard.dataset.path;
    const tipo = dragCard.dataset.tipo;
    try {{
      const r = await fetch('/mover', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{arquivo: path, tipo, status: novoStatus}})
      }});
      if (r.ok) {{
        const data = await r.json();
        dragCard.dataset.path = data.novo_path;
        dragCard.querySelectorAll('[data-path]').forEach(el => el.dataset.path = data.novo_path);
        const zone = col.querySelector('.kcol-cards');
        const ph   = zone.querySelector('.empty-col');
        if (ph) ph.remove();
        zone.appendChild(dragCard);
        atualizarContadores();
        toast('✅ Movido → ' + novoStatus);
      }} else {{ toast('❌ Erro ao mover', true); }}
    }} catch {{ toast('❌ Servidor offline', true); }}
  }});
}});

document.querySelectorAll('.tcol').forEach(col => {{
  col.addEventListener('dragover', e => {{
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    col.classList.add('drag-over');
  }});
  col.addEventListener('dragleave', e => {{
    if (!col.contains(e.relatedTarget)) col.classList.remove('drag-over');
  }});
  col.addEventListener('drop', async e => {{
    e.preventDefault();
    col.classList.remove('drag-over');
    if (!dragCard || !dragCard.classList.contains('tcard')) return;
    if (col.dataset.tipo !== dragCard.dataset.tipo) {{
      toast('❌ Não misture TPD com TPG', true); return;
    }}
    const novoStatus = col.dataset.status;
    const path       = dragCard.dataset.path;
    try {{
      const r = await fetch('/update', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{arquivo: path, campo: 'status', valor: novoStatus}})
      }});
      if (r.ok) {{
        const zone = col.querySelector('.tcol-cards');
        const ph   = zone.querySelector('.empty-col');
        if (ph) ph.remove();
        const btn = dragCard.querySelector('.tc-btn');
        if (novoStatus === 'feito') {{
          dragCard.classList.add('tcard-done');
          if (btn) btn.textContent = '↩️ Reabrir';
        }} else {{
          dragCard.classList.remove('tcard-done');
          if (btn) btn.textContent = '✓ Feita';
        }}
        zone.appendChild(dragCard);
        atualizarContadoresTarefas();
        toast(novoStatus === 'feito' ? '✅ Feita!' : '↩️ Reaberta');
      }} else {{ toast('❌ Erro', true); }}
    }} catch {{ toast('❌ Servidor offline', true); }}
  }});
}});

function atualizarContadores() {{
  document.querySelectorAll('.kcol').forEach(col => {{
    col.querySelector('.kcol-n').textContent = col.querySelectorAll('.kcard').length;
  }});
  const cntProj = document.querySelector('[data-tipo="PROJETOS"][data-status="EM ANDAMENTO"] .kcol-cards')?.querySelectorAll('.kcard').length ?? 0;
  const cntEst  = document.querySelector('[data-tipo="ESTUDOS"][data-status="EM ANDAMENTO"] .kcol-cards')?.querySelectorAll('.kcard').length ?? 0;
  const ep = document.getElementById('cnt-proj'); if (ep) ep.textContent = cntProj;
  const ee = document.getElementById('cnt-est');  if (ee) ee.textContent = cntEst;
}}
</script>
</body>
</html>"""

# ── servidor HTTP ──────────────────────────────────────────────────────────────

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def do_GET(self):
        body = gerar_pagina().encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            data   = json.loads(self.rfile.read(length))
        except Exception:
            self.send_response(400); self.end_headers(); return

        if self.path == "/update":
            ok = atualizar_campo(data["arquivo"], data["campo"], str(data["valor"]))
            self._json(200 if ok else 500, {"ok": ok})

        elif self.path == "/mover":
            novo_path = mover_arquivo(data["arquivo"], data["tipo"], data["status"])
            if novo_path:
                self._json(200, {"ok": True, "novo_path": novo_path})
            else:
                self._json(500, {"ok": False})

        elif self.path == "/toggle-pend":
            ok = toggle_pendencia(data["item"])
            self._json(200 if ok else 500, {"ok": ok})

        else:
            self.send_response(404); self.end_headers()

    def _json(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    srv = HTTPServer(("localhost", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"🧠 Cockpit Kanban → {url}")
    print("   Arraste cards para mudar status (move o .md de pasta)")
    print("   Edite campos — salva direto no frontmatter")
    print("   Pendências: clique para concluir")
    print("   Ctrl+C para encerrar\n")
    try:
        import webbrowser; webbrowser.open(url)
    except Exception:
        pass
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n[cockpit] encerrado.")
