#!/usr/bin/env python3
"""
estudos-generator.py — Gera cockpit-estudos.html para o Sistema Operacional Pessoal
Lê: notas em [F1] 2-Literatura/ com frontmatter padronizado (subtipo: curso|livro|mentoria|workshop)
Gera: cockpit-estudos.html na raiz do vault
"""

import os
import re
import datetime

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ESTUDOS = os.path.join(VAULT, "ESTUDOS")

CATEGORIAS_EMOJI = {
    "marketing": "📣",
    "audiovisual": "🎬",
    "produtividade": "⚡",
    "negocios": "💼",
    "tecnologia": "🤖",
    "pessoal": "🌱",
    "espiritualidade": "🙏",
    "ficcao": "📖",
}

SUBTIPO_EMOJI = {
    "curso": "🎓",
    "livro": "📚",
    "mentoria": "🤝",
    "workshop": "⚡",
}

STATUS_LABEL = {
    "a-iniciar": "A iniciar",
    "em-andamento": "Em andamento",
    "pausado": "Pausado",
    "concluido": "Concluído",
}

PRIORIDADE_ORDEM = {"alta": 0, "media": 1, "baixa": 2}


def parse_frontmatter(path):
    """Lê o bloco YAML entre --- e retorna dict com os campos."""
    dados = {}
    try:
        with open(path, encoding="utf-8") as f:
            conteudo = f.read()
    except Exception:
        return dados

    match = re.match(r"^---\s*\n(.*?)\n---", conteudo, re.DOTALL)
    if not match:
        return dados

    for linha in match.group(1).splitlines():
        if ":" in linha:
            chave, _, valor = linha.partition(":")
            chave = chave.strip()
            valor = valor.strip()
            # Remove colchetes de campos com opções
            if valor.startswith("[") and "|" in valor:
                valor = ""
            dados[chave] = valor

    dados["_path"] = path
    dados["_conteudo"] = conteudo
    return dados


def extrair_insights(conteudo, limite=3):
    """Extrai primeiros bullets da seção ## 💡 Insights."""
    insights = []
    em_insights = False
    for linha in conteudo.splitlines():
        if re.match(r"##\s+.*[Ii]nsights?", linha):
            em_insights = True
            continue
        if em_insights and linha.startswith("##"):
            break
        if em_insights and re.match(r"^[-*]\s+\S", linha):
            texto = re.sub(r"^[-*]\s+", "", linha).strip()
            if texto:
                insights.append(texto)
        if len(insights) >= limite:
            break
    return insights


STATUS_MAP = {
    "EM ANDAMENTO": "em-andamento",
    "A INICIAR": "a-iniciar",
    "PAUSADO": "pausado",
    "CONCLUÍDO": "concluido",
    "DESCARTADO": "descartado",
}

def varrer_estudos():
    """Varre ESTUDOS/ usando a pasta como fonte de verdade do status."""
    notas = []
    for pasta_status, status_valor in STATUS_MAP.items():
        pasta = os.path.join(ESTUDOS, pasta_status)
        if not os.path.isdir(pasta):
            continue
        # Só arquivos diretos na pasta de status (não recursivo nos subníveis)
        for arq in os.listdir(pasta):
            if not arq.endswith(".md"):
                continue
            path = os.path.join(pasta, arq)
            dados = parse_frontmatter(path)
            dados["_path"] = path
            dados["status"] = status_valor  # pasta é a fonte de verdade
            dados.setdefault("subtipo", "curso")
            notas.append(dados)
    return notas


def calcular_progresso(nota):
    """Retorna (concluidas, total, pct) para cursos."""
    try:
        total = int(nota.get("total-aulas") or nota.get("total-paginas") or nota.get("total-encontros") or 0)
        feitas = int(nota.get("aulas-concluidas") or nota.get("pagina-atual") or nota.get("encontros-realizados") or 0)
        pct = round((feitas / total) * 100) if total > 0 else 0
        return feitas, total, pct
    except Exception:
        return 0, 0, 0


def nome_nota(nota):
    return nota.get("titulo") or os.path.splitext(os.path.basename(nota["_path"]))[0]


def card_em_andamento(nota):
    subtipo = nota.get("subtipo", "curso")
    feitas, total, pct = calcular_progresso(nota)
    cor_barra = "#3b82f6" if pct < 80 else "#22c55e"
    modulo = nota.get("modulo-atual") or nota.get("pagina-atual") or ""
    proxima = nota.get("proxima-aula") or ""
    insights = extrair_insights(nota.get("_conteudo", ""), limite=2)
    insights_html = "".join(f"<li>{i}</li>" for i in insights) if insights else "<li><i>Nenhum insight registrado</i></li>"
    meta = nota.get("meta-horas-semana") or "—"
    instrutor = nota.get("instrutor") or nota.get("autor") or nota.get("mentor") or ""
    emoji = SUBTIPO_EMOJI.get(subtipo, "📖")
    cat = nota.get("categoria", "")
    cat_emoji = CATEGORIAS_EMOJI.get(cat, "")

    modulo_html = f'<div class="em-detalhe">📍 {modulo}</div>' if modulo else ""
    proxima_html = f'<div class="em-detalhe">▶️ Próxima: {proxima}</div>' if proxima else ""

    barra_html = ""
    if total > 0:
        barra_html = f"""
        <div class="prog-label">{feitas}/{total} {'aulas' if subtipo=='curso' else 'páginas' if subtipo=='livro' else 'encontros'} · {pct}%</div>
        <div class="prog-bar"><div class="prog-fill" style="width:{pct}%;background:{cor_barra}"></div></div>
        """

    return f"""
    <div class="card-estudo">
      <div class="estudo-header">
        <span class="subtipo-badge">{emoji} {subtipo.title()}</span>
        {f'<span class="cat-badge">{cat_emoji} {cat}</span>' if cat else ''}
      </div>
      <div class="estudo-titulo">{nome_nota(nota)}</div>
      {f'<div class="estudo-sub">{instrutor}</div>' if instrutor else ''}
      {barra_html}
      {modulo_html}
      {proxima_html}
      <div class="insights-mini">
        <span class="insights-label">💡 Insights</span>
        <ul>{insights_html}</ul>
      </div>
      {f'<div class="meta-tag">⏱️ Meta: {meta}h/sem</div>' if meta and meta != "—" else ''}
    </div>
    """


def card_a_iniciar(nota):
    subtipo = nota.get("subtipo", "curso")
    prioridade = nota.get("prioridade", "media")
    emoji = SUBTIPO_EMOJI.get(subtipo, "📖")
    instrutor = nota.get("instrutor") or nota.get("autor") or nota.get("mentor") or ""
    cat = nota.get("categoria", "")
    cat_emoji = CATEGORIAS_EMOJI.get(cat, "")
    cores_prioridade = {"alta": "#ef4444", "media": "#f59e0b", "baixa": "#64748b"}
    cor = cores_prioridade.get(prioridade, "#64748b")

    return f"""
    <div class="item-fila">
      <div class="fila-left">
        <span class="subtipo-sm">{emoji}</span>
        <div>
          <div class="fila-titulo">{nome_nota(nota)}</div>
          {f'<div class="fila-sub">{instrutor}{f" · {cat_emoji} {cat}" if cat else ""}</div>' if instrutor or cat else ''}
        </div>
      </div>
      <span class="prioridade-dot" style="background:{cor}" title="Prioridade: {prioridade}"></span>
    </div>
    """


def gerar_html(notas):
    agora = datetime.datetime.now()
    data_formatada = agora.strftime("%A, %d/%m/%Y").capitalize()
    hora = agora.strftime("%H:%M")
    gerado_em = agora.strftime("%H:%M:%S")

    em_andamento = [n for n in notas if n.get("status") == "em-andamento"]
    a_iniciar = sorted(
        [n for n in notas if n.get("status") == "a-iniciar"],
        key=lambda n: PRIORIDADE_ORDEM.get(n.get("prioridade", "media"), 1)
    )
    concluidos = [n for n in notas if n.get("status") == "concluido"]

    # Coleta insights recentes de todos os em-andamento
    todos_insights = []
    for n in em_andamento:
        ins = extrair_insights(n.get("_conteudo", ""), limite=3)
        for i in ins:
            todos_insights.append({"texto": i, "fonte": nome_nota(n)})
    insights_html = "".join(
        f'<li><span class="insight-texto">{i["texto"]}</span> <span class="insight-fonte">— {i["fonte"]}</span></li>'
        for i in todos_insights[:6]
    ) if todos_insights else "<li><i>Nenhum insight registrado ainda</i></li>"

    # Blocos em andamento
    em_andamento_html = "".join(card_em_andamento(n) for n in em_andamento) if em_andamento else '<p class="vazio">Nenhum estudo em andamento</p>'

    # Fila
    fila_html = "".join(card_a_iniciar(n) for n in a_iniciar[:8]) if a_iniciar else '<p class="vazio">Fila vazia</p>'

    # Indicadores
    total_geral = len(notas)
    em_and_count = len(em_andamento)
    concluidos_count = len(concluidos)
    fila_count = len(a_iniciar)

    # Meta semanal agregada
    meta_total = sum(int(n.get("meta-horas-semana") or 0) for n in em_andamento)
    meta_str = f"{meta_total}h/sem" if meta_total else "—"

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>📚 Cockpit Estudos — {agora.strftime('%d/%m/%Y')}</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #0f172a; color: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; min-height: 100vh; }}

    .header {{ background: #1e293b; border-bottom: 1px solid #334155; padding: 16px 24px; display: flex; align-items: center; justify-content: space-between; }}
    .header-title {{ font-size: 1.1rem; font-weight: 700; color: #f8fafc; }}
    .header-date {{ color: #94a3b8; font-size: 0.85rem; margin-top: 2px; }}
    .header-badge {{ background: #1d3a6e; border: 1px solid #3b82f6; border-radius: 8px; padding: 8px 16px; text-align: right; }}
    .header-badge .num {{ font-size: 1.4rem; font-weight: 800; color: #93c5fd; }}
    .header-badge .label {{ font-size: 0.75rem; color: #64748b; }}

    .indicadores {{ display: flex; gap: 12px; padding: 16px 20px 0; }}
    .ind {{ flex: 1; background: #1e293b; border: 1px solid #334155; border-radius: 10px; padding: 12px 16px; }}
    .ind h4 {{ font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.07em; color: #64748b; margin-bottom: 4px; }}
    .ind .val {{ font-size: 1.2rem; font-weight: 700; color: #f8fafc; }}
    .ind .sub {{ font-size: 0.78rem; color: #94a3b8; margin-top: 2px; }}

    .main {{ display: grid; grid-template-columns: 2fr 1fr; gap: 16px; padding: 16px 20px; }}
    @media (max-width: 800px) {{ .main {{ grid-template-columns: 1fr; }} }}

    .secao-titulo {{ font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; margin-bottom: 12px; padding-bottom: 6px; border-bottom: 1px solid #1e293b; }}

    .col-left {{ display: flex; flex-direction: column; gap: 12px; }}
    .col-right {{ display: flex; flex-direction: column; gap: 12px; }}

    .bloco {{ background: #1e293b; border: 1px solid #334155; border-radius: 12px; padding: 16px; }}

    /* Cards em andamento */
    .cards-andamento {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px; }}
    .card-estudo {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; padding: 14px; transition: border-color 0.2s; }}
    .card-estudo:hover {{ border-color: #3b82f6; }}
    .estudo-header {{ display: flex; gap: 8px; align-items: center; margin-bottom: 6px; }}
    .subtipo-badge {{ background: #1d3a6e; color: #93c5fd; font-size: 0.72rem; padding: 2px 8px; border-radius: 20px; font-weight: 600; }}
    .cat-badge {{ background: #1e293b; color: #94a3b8; font-size: 0.7rem; padding: 2px 8px; border-radius: 20px; }}
    .estudo-titulo {{ font-size: 0.92rem; font-weight: 700; color: #f1f5f9; margin-bottom: 2px; line-height: 1.3; }}
    .estudo-sub {{ font-size: 0.78rem; color: #64748b; margin-bottom: 8px; }}
    .prog-label {{ font-size: 0.75rem; color: #94a3b8; margin-bottom: 4px; }}
    .prog-bar {{ background: #334155; border-radius: 4px; height: 6px; margin-bottom: 8px; overflow: hidden; }}
    .prog-fill {{ height: 100%; border-radius: 4px; transition: width 0.3s; }}
    .em-detalhe {{ font-size: 0.78rem; color: #94a3b8; margin-bottom: 3px; }}
    .insights-mini {{ margin-top: 10px; }}
    .insights-label {{ font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.06em; color: #64748b; display: block; margin-bottom: 4px; }}
    .insights-mini ul {{ list-style: none; }}
    .insights-mini ul li {{ font-size: 0.78rem; color: #cbd5e1; padding: 3px 0; border-bottom: 1px solid #1e293b; }}
    .insights-mini ul li:last-child {{ border-bottom: none; }}
    .meta-tag {{ font-size: 0.72rem; color: #64748b; margin-top: 8px; }}

    /* Fila */
    .item-fila {{ display: flex; align-items: center; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #1e293b; }}
    .item-fila:last-child {{ border-bottom: none; }}
    .fila-left {{ display: flex; align-items: center; gap: 10px; }}
    .subtipo-sm {{ font-size: 1rem; }}
    .fila-titulo {{ font-size: 0.85rem; font-weight: 600; color: #e2e8f0; }}
    .fila-sub {{ font-size: 0.75rem; color: #64748b; }}
    .prioridade-dot {{ width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }}

    /* Insights globais */
    .insights-globais ul {{ list-style: none; }}
    .insights-globais ul li {{ font-size: 0.83rem; color: #cbd5e1; padding: 7px 0; border-bottom: 1px solid #1e293b; }}
    .insights-globais ul li:last-child {{ border-bottom: none; }}
    .insight-fonte {{ color: #64748b; font-size: 0.75rem; display: block; margin-top: 1px; }}

    .vazio {{ font-size: 0.85rem; color: #64748b; font-style: italic; padding: 8px 0; }}

    .legenda {{ display: flex; gap: 12px; font-size: 0.75rem; color: #64748b; padding: 0 20px 8px; flex-wrap: wrap; }}
    .legenda span {{ display: flex; align-items: center; gap: 4px; }}
    .dot-alta {{ width: 8px; height: 8px; background: #ef4444; border-radius: 50%; }}
    .dot-media {{ width: 8px; height: 8px; background: #f59e0b; border-radius: 50%; }}
    .dot-baixa {{ width: 8px; height: 8px; background: #64748b; border-radius: 50%; }}

    .gerado {{ text-align: center; color: #334155; font-size: 0.72rem; padding: 12px; }}
  </style>
</head>
<body>

<div class="header">
  <div>
    <div class="header-title">📚 Cockpit Estudos — Jadielson Davi</div>
    <div class="header-date">{data_formatada} · {hora}</div>
  </div>
  <div class="header-badge">
    <div class="num">{em_and_count}</div>
    <div class="label">em andamento</div>
  </div>
</div>

<div class="indicadores">
  <div class="ind">
    <h4>🎓 Total mapeados</h4>
    <div class="val">{total_geral}</div>
    <div class="sub">cursos, livros, mentorias, workshops</div>
  </div>
  <div class="ind">
    <h4>🔄 Em andamento</h4>
    <div class="val">{em_and_count}</div>
    <div class="sub">estudos ativos agora</div>
  </div>
  <div class="ind">
    <h4>📋 Fila</h4>
    <div class="val">{fila_count}</div>
    <div class="sub">aguardando início</div>
  </div>
  <div class="ind">
    <h4>✅ Concluídos</h4>
    <div class="val">{concluidos_count}</div>
    <div class="sub">finalizados no vault</div>
  </div>
  <div class="ind">
    <h4>⏱️ Meta semanal</h4>
    <div class="val">{meta_str}</div>
    <div class="sub">total dos estudos ativos</div>
  </div>
</div>

<div class="main">

  <div class="col-left">

    <div class="bloco">
      <div class="secao-titulo">🔄 Em andamento</div>
      <div class="cards-andamento">
        {em_andamento_html}
      </div>
    </div>

    <div class="bloco insights-globais">
      <div class="secao-titulo">💡 Insights recentes (todos os estudos)</div>
      <ul>{insights_html}</ul>
    </div>

  </div>

  <div class="col-right">

    <div class="bloco">
      <div class="secao-titulo">⏳ Fila — A iniciar</div>
      <div class="legenda" style="padding: 0 0 8px; font-size:0.72rem;">
        <span><span class="dot-alta"></span> Alta</span>
        <span><span class="dot-media"></span> Média</span>
        <span><span class="dot-baixa"></span> Baixa</span>
      </div>
      {fila_html}
    </div>

  </div>

</div>

<div class="gerado">Gerado em {gerado_em} · rodar generate-cockpit-estudos.sh para atualizar</div>

</body>
</html>"""


if __name__ == "__main__":
    notas = varrer_estudos()
    html = gerar_html(notas)
    output = os.path.join(VAULT, "cockpit-estudos.html")
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    total = len(notas)
    em_and = sum(1 for n in notas if n.get("status") == "em-andamento")
    print(f"✅ cockpit-estudos.html gerado · {total} notas · {em_and} em andamento")
