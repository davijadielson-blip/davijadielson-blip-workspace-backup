#!/usr/bin/env python3
"""
Resumo semanal de projetos.
Lê:
  - Git log da última semana (projetos com commits).
  - Frontmatter ultimo_update de cada <NOME>.md em PROJETOS/EM ANDAMENTO e A INICIAR.
Gera:
  - Projetos que avançaram (com contagem de commits).
  - Projetos parados 7-13 dias (alerta amarelo).
  - Projetos parados 14+ dias (alerta vermelho).
  - Top 3 sugerido pra semana seguinte.
Envia: arquivo markdown em memory/sessions/weekly-projects/YYYY-MM-DD.md
"""

import argparse
import os
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path

HOJE = datetime.now()
SEMANA_INICIO = HOJE - timedelta(days=7)


def projetos_avancaram_via_git(vault: Path) -> list[tuple[str, int]]:
    """Quais pastas em PROJETOS/ tiveram commits na última semana."""
    result = subprocess.run(
        ["git", "log",
         f"--since={SEMANA_INICIO.strftime('%Y-%m-%d')}",
         "--name-only", "--pretty=format:"],
        cwd=vault, capture_output=True, text=True
    )
    contagem: dict[str, int] = {}
    for linha in result.stdout.splitlines():
        if not linha.startswith("PROJETOS/"):
            continue
        partes = linha.split("/")
        if len(partes) >= 3:
            nome = partes[2]
            contagem[nome] = contagem.get(nome, 0) + 1
    return sorted(contagem.items(), key=lambda x: -x[1])


def projetos_parados(vault: Path) -> tuple[list, list]:
    """Projetos com ultimo_update ≥ 7 dias."""
    amarelos = []
    vermelhos = []

    for status_dir in ["EM ANDAMENTO", "A INICIAR"]:
        pasta = vault / "PROJETOS" / status_dir
        if not pasta.exists():
            continue
        for proj_dir in sorted(pasta.iterdir()):
            if not proj_dir.is_dir():
                continue
            # Arquivo principal tem mesmo nome que a pasta
            main_file = proj_dir / f"{proj_dir.name}.md"
            if not main_file.exists():
                # fallback: qualquer .md que não seja 1-briefing ou proximas-etapas
                candidates = [f for f in proj_dir.glob("*.md")
                              if f.name not in ("1-briefing.md", "proximas-etapas.md")]
                if not candidates:
                    continue
                main_file = candidates[0]

            try:
                content = main_file.read_text(encoding="utf-8")
                match = re.search(r'ultimo_update:\s*(\S+)', content)
                if not match:
                    continue
                data_str = match.group(1).strip().strip("'\"")
                try:
                    data = datetime.strptime(data_str, "%Y-%m-%d")
                except ValueError:
                    continue
                dias = (HOJE - data).days
                info = (proj_dir.name, status_dir, dias)
                if dias >= 14:
                    vermelhos.append(info)
                elif dias >= 7:
                    amarelos.append(info)
            except Exception:
                continue

    return amarelos, vermelhos


def gerar_markdown(vault: Path) -> str:
    avancados = projetos_avancaram_via_git(vault)
    amarelos, vermelhos = projetos_parados(vault)

    total_em_andamento = sum(1 for _ in (vault / "PROJETOS" / "EM ANDAMENTO").iterdir()
                             if (vault / "PROJETOS" / "EM ANDAMENTO" / _).is_dir()) \
        if (vault / "PROJETOS" / "EM ANDAMENTO").exists() else 0
    total_a_iniciar = sum(1 for _ in (vault / "PROJETOS" / "A INICIAR").iterdir()
                          if (vault / "PROJETOS" / "A INICIAR" / _).is_dir()) \
        if (vault / "PROJETOS" / "A INICIAR").exists() else 0

    linhas = [
        f"---",
        f"tipo: weekly-projects-summary",
        f"data: {HOJE.strftime('%Y-%m-%d')}",
        f"gerado-por: cron-weekly-projects-summary",
        f"---",
        f"",
        f"# 🗓️ Resumo Semanal de Projetos — {HOJE.strftime('%d/%m/%Y')}",
        f"_{SEMANA_INICIO.strftime('%d/%m')} → {HOJE.strftime('%d/%m')}_",
        f"",
        f"## 📊 Inventário",
        f"- EM ANDAMENTO: {total_em_andamento}",
        f"- A INICIAR: {total_a_iniciar}",
        f"",
        f"---",
        f"",
        f"## 📈 Avançaram esta semana ({len(avancados)})",
    ]

    if avancados:
        for proj, commits in avancados[:10]:
            linhas.append(f"- {proj} ({commits} updates)")
    else:
        linhas.append("_Nenhum projeto avançou esta semana._")

    linhas += ["", "---", ""]

    if vermelhos:
        linhas.append(f"## 🔴 Parados 14+ dias — considerar PAUSAR ou DESCARTAR ({len(vermelhos)})")
        for proj, status, dias in sorted(vermelhos, key=lambda x: -x[2])[:10]:
            linhas.append(f"- {proj} ({status}) — {dias}d parado")
        linhas.append("")

    if amarelos:
        linhas.append(f"## 🟡 Parados 7-13 dias — atenção ({len(amarelos)})")
        for proj, status, dias in sorted(amarelos, key=lambda x: -x[2])[:10]:
            linhas.append(f"- {proj} ({status}) — {dias}d parado")
        linhas.append("")

    if not vermelhos and not amarelos:
        linhas += ["## ✅ Nenhum projeto parado", ""]

    linhas += [
        "---",
        "",
        f"## 🎯 Top 3 sugerido — próxima semana",
    ]

    if avancados:
        for proj, _ in avancados[:3]:
            linhas.append(f"- [ ] {proj}")
    else:
        linhas.append("_(sem dados de atividade — escolha manualmente)_")

    linhas += [
        "",
        "---",
        f"_Gerado em {HOJE.strftime('%H:%M')} · Abra PROJETOS/COCKPIT.md pra revisar status completo._",
    ]

    return "\n".join(linhas)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    vault = Path(args.vault)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    conteudo = gerar_markdown(vault)
    output.write_text(conteudo, encoding="utf-8")

    print(conteudo)


if __name__ == "__main__":
    main()
