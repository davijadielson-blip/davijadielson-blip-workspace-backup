#!/usr/bin/env python3
"""Importa arquivos Markdown do Cofre para o Notion Cofre Index em lotes."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import time
from pathlib import Path
from urllib import error, request


WORKSPACE = Path(__file__).resolve().parents[2]
COFRE_INDEX_DS = os.environ.get("NOTION_COFRE_INDEX_DS", "a3803ed8-abf8-47da-9a52-ae8bf889b865")
NOTION_VERSION = os.environ.get("NOTION_API_VERSION", "2026-03-11")


def headers() -> dict[str, str]:
    token = os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        raise SystemExit("NOTION_API_TOKEN/NOTION_TOKEN ausente. Rode: source scripts/notion-env.sh")
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion(method: str, path: str, payload: dict | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = request.Request(f"https://api.notion.com/v1{path}", data=body, headers=headers(), method=method)
    try:
        with request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8")
        raise RuntimeError(f"{method} {path} failed {exc.code}: {detail}") from exc


def prop_rich_text(item: dict, name: str) -> str:
    prop = item.get("properties", {}).get(name, {})
    return "".join(part.get("plain_text", "") for part in prop.get("rich_text", []))


def existing_paths() -> set[str]:
    paths: set[str] = set()
    cursor = None
    while True:
        payload: dict = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        response = notion("POST", f"/data_sources/{COFRE_INDEX_DS}/query", payload)
        for item in response.get("results", []):
            path = prop_rich_text(item, "Caminho Cofre").strip()
            if path:
                paths.add(path)
        if not response.get("has_more"):
            return paths
        cursor = response.get("next_cursor")


def all_markdown() -> list[str]:
    output = subprocess.check_output(["rg", "--files", "-g", "*.md"], cwd=WORKSPACE, text=True)
    return [line.strip() for line in output.splitlines() if line.strip()]


def priority(path: str) -> tuple[int, str]:
    if path in {
        "CONSTITUICAO.md",
        "AGENTS.md",
        "MAPA.md",
        "MEMORY.md",
        "SOUL.md",
        "IDENTITY.md",
        "USER.md",
        "TOOLS.md",
        "HEARTBEAT.md",
    }:
        return (0, path)
    prefixes = [
        ("00-central/", 1),
        ("memory/context/", 1),
        ("10-pessoal/", 2),
        ("memory/projects/logika-solucoes-digitais/", 2),
        ("20-profissional/", 3),
        ("memory/decisoes/", 3),
        ("30-estudos/", 4),
        ("memory/daily-briefs/", 4),
        ("40-projetos/", 5),
        ("memory/logika/", 5),
        ("50-clientes/", 6),
        ("memory/projects/", 6),
        ("60-processos/", 7),
        ("[F3] PROJETOS/", 7),
        ("70-agentes/", 8),
        ("[F1] 5-Frentes/", 8),
        ("80-handoffs/", 9),
        ("[F1] 4-Pessoal/", 9),
        ("90-arquivo/", 90),
        ("[F1]", 10),
        ("skills/", 20),
        ("scripts/", 21),
    ]
    for prefix, rank in prefixes:
        if path.startswith(prefix):
            return (rank, path)
    return (30, path)


def classify(path: str) -> tuple[str, bool]:
    if path.startswith("00-central/"):
        return "Central", False
    if path.startswith("10-pessoal/"):
        return "Pessoal", True
    if path.startswith("20-profissional/"):
        return "Profissional", False
    if path.startswith("30-estudos/"):
        return "Estudos", False
    if path.startswith("40-projetos/"):
        return "Projetos", False
    if path.startswith("50-clientes/"):
        return "Clientes", False
    if path.startswith("60-processos/"):
        return "Processos", False
    if path.startswith("70-agentes/"):
        return "Agentes", False
    if path.startswith("80-handoffs/"):
        return "Handoffs", False
    if path.startswith("90-arquivo/"):
        return "Arquivo", False
    if path.startswith("[F1]"):
        return "Legado F1", True
    if path.startswith("[F0]"):
        return "Legado F0", True
    if path.startswith("[F3]"):
        return "Legado F3 Projetos", False
    if path.startswith("memory/"):
        return "Memoria Operacional", False
    if path.startswith("scripts/"):
        return "Scripts", False
    if path.startswith("skills/"):
        return "Skills", False
    return "Raiz", path == "PIN.md"


def doc_type(path: str) -> str:
    low = path.lower()
    name = Path(path).name.lower()
    if name in {"constituicao.md", "agents.md"}:
        return "Constituicao"
    if name in {"soul.md", "identity.md", "user.md", "pin.md"}:
        return "Identidade"
    if name == "memory.md":
        return "Memoria"
    if name == "mapa.md":
        return "Mapa"
    if "projeto" in low or "projects" in low:
        return "Projeto"
    if "context" in low or "decisoes" in low:
        return "Contexto"
    if "output" in low or "briefing" in low:
        return "Output"
    if path.startswith("skills/") or path.startswith("60-processos/skills/") or name == "skill.md":
        return "Skill"
    return "Outro"


def front(path: str) -> str:
    low = path.lower()
    if "logika" in low:
        return "LOGIKA"
    if "saude" in low or "saúde" in low:
        return "Saude"
    if "camara" in low or "câmara" in low:
        return "Camara"
    if "sindss" in low:
        return "SINDSS"
    if "alem-da-foto" in low or "além" in low:
        return "Alem da Foto"
    if "pessoal" in low or path.startswith("10-pessoal/") or path.startswith("[F1] 4-Pessoal/"):
        return "Pessoal"
    if path in {"AGENTS.md", "MAPA.md", "MEMORY.md", "SOUL.md", "IDENTITY.md", "USER.md", "CONSTITUICAO.md"}:
        return "Sistema Loh"
    return "Geral"


def summary(path: str) -> str:
    text = (WORKSPACE / path).read_text(encoding="utf-8", errors="ignore")
    lines = [line.strip("#- *\t ") for line in text.splitlines() if line.strip() and line.strip() != "---"]
    return " ".join(lines[:4])[:900]


def title(value: str) -> dict:
    return {"title": [{"type": "text", "text": {"content": value[:2000]}}]}


def rich(value: str) -> dict:
    return {"rich_text": [{"type": "text", "text": {"content": value[:2000]}}]} if value else {"rich_text": []}


def select(value: str) -> dict:
    return {"select": {"name": value}}


def checkbox(value: bool) -> dict:
    return {"checkbox": value}


def date_today() -> dict:
    return {"date": {"start": os.environ.get("IMPORT_DATE", "2026-08-07")}}


def number(value: int) -> dict:
    return {"number": value}


def create_index_item(path: str) -> None:
    fluxo, protected = classify(path)
    digest = hashlib.sha256((WORKSPACE / path).read_bytes()).hexdigest()[:16]
    props = {
        "Nome": title(Path(path).name),
        "Caminho Cofre": rich(path),
        "Fluxo": select(fluxo),
        "Tipo": select(doc_type(path)),
        "Frente": select(front(path)),
        "Status Sync": select("Protegido" if protected else "Indexado"),
        "Direcao Sync": select("Somente leitura" if protected else "Bidirecional governado"),
        "Atualizar Cofre": checkbox(not protected),
        "Protegido": checkbox(protected),
        "Ultima Sync": date_today(),
        "Hash": rich(digest),
        "Resumo": rich(summary(path)),
    }
    notion("POST", "/pages", {"parent": {"data_source_id": COFRE_INDEX_DS}, "properties": props})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=250)
    parser.add_argument("--sleep", type=float, default=0.22)
    args = parser.parse_args()

    existing = existing_paths()
    candidates = [path for path in sorted(all_markdown(), key=priority) if path not in existing]
    imported: list[str] = []
    errors: list[dict[str, str]] = []

    for path in candidates[: args.limit]:
        try:
            create_index_item(path)
            imported.append(path)
            time.sleep(args.sleep)
        except Exception as exc:  # noqa: BLE001
            errors.append({"path": path, "error": str(exc)})

    print(
        json.dumps(
            {
                "existing_before": len(existing),
                "remaining_before": len(candidates),
                "imported": len(imported),
                "errors": errors,
                "first_imported": imported[:5],
                "last_imported": imported[-5:],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
