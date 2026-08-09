#!/usr/bin/env python3
"""
Sincronizacao governada Notion -> Cofre.

Por padrao roda em dry-run. Use --apply para gravar arquivos operacionais.
Notas autorais/protegidas geram proposta em memory/inbox-externa/notion/revisao/.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib import error, request


WORKSPACE = Path(__file__).resolve().parents[2]
COFRE_INDEX_DS = os.environ.get("NOTION_COFRE_INDEX_DS", "a3803ed8-abf8-47da-9a52-ae8bf889b865")
NOTION_VERSION = os.environ.get("NOTION_API_VERSION", "2026-03-11")
REVIEW_DIR = WORKSPACE / "memory" / "inbox-externa" / "notion" / "revisao"


def ntn_bin() -> str:
    candidates = [
        os.environ.get("NTN_BIN"),
        shutil.which("ntn"),
        "/data/.npm-global/bin/ntn",
        "/usr/local/bin/ntn",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise RuntimeError("ntn nao encontrado. Instale o CLI ou defina NTN_BIN.")


def notion_headers() -> dict[str, str]:
    token = os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        raise SystemExit("NOTION_API_TOKEN/NOTION_TOKEN ausente. Rode: source scripts/notion-env.sh")
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def notion_api(method: str, path: str, payload: dict | None = None) -> dict:
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    req = request.Request(f"https://api.notion.com/v1{path}", data=body, headers=notion_headers(), method=method)
    try:
        with request.urlopen(req, timeout=45) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8")
        raise RuntimeError(f"{method} {path} failed {exc.code}: {detail}") from exc


def prop_text(props: dict, name: str) -> str:
    prop = props.get(name) or {}
    ptype = prop.get("type")
    if ptype == "title":
        return "".join(part.get("plain_text", "") for part in prop.get("title", []))
    if ptype == "rich_text":
        return "".join(part.get("plain_text", "") for part in prop.get("rich_text", []))
    if ptype == "select":
        selected = prop.get("select")
        return selected.get("name", "") if selected else ""
    if ptype == "checkbox":
        return "true" if prop.get("checkbox") else "false"
    return ""


def query_index() -> list[dict]:
    items: list[dict] = []
    cursor = None
    while True:
        payload: dict = {"page_size": 100}
        if cursor:
            payload["start_cursor"] = cursor
        response = notion_api("POST", f"/data_sources/{COFRE_INDEX_DS}/query", payload)
        items.extend(response.get("results", []))
        if not response.get("has_more"):
            return items
        cursor = response.get("next_cursor")


def page_markdown(page_id: str) -> str:
    result = subprocess.run(
        [ntn_bin(), "pages", "get", page_id],
        cwd=WORKSPACE,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def body_without_frontmatter(markdown: str) -> str:
    lines = markdown.splitlines()
    if lines[:1] == ["---"]:
        for idx in range(1, len(lines)):
            if lines[idx] == "---":
                return "\n".join(lines[idx + 1 :]).strip()
    return markdown.strip()


def is_protected(path: str, protected_flag: bool) -> bool:
    sensitive_prefixes = ("10-pessoal/",)
    legacy_sensitive_prefixes = ("[F1]", "[F0]")
    return (
        protected_flag
        or path.startswith(sensitive_prefixes)
        or path.startswith(legacy_sensitive_prefixes)
        or path == "PIN.md"
    )


def review_path(cofre_path: str) -> Path:
    safe = cofre_path.replace("/", "__").replace("[", "").replace("]", "").replace(" ", "-")
    stamp = dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")
    return REVIEW_DIR / f"{stamp}-{safe}.md"


def write_review(cofre_path: str, content: str) -> Path:
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)
    out = review_path(cofre_path)
    out.write_text(
        "\n".join(
            [
                "---",
                "tema: revisao de alteracao notion para cofre",
                "conteudo: proposta de alteracao vinda do Notion para arquivo protegido ou pendente de revisao",
                "setor: governanca documental",
                "cliente: Jadielson Davi",
                "tipo: revisao",
                "prioridade: alta",
                f"atualizado_em: {dt.date.today().isoformat()}",
                "usar_quando: revisar alteracoes vindas do Notion antes de aplicar no Cofre",
                "nao_usar_quando: buscar versao canonica ja aprovada",
                "---",
                "",
                f"# Revisao Notion -> Cofre - {cofre_path}",
                "",
                f"Arquivo-alvo: `{cofre_path}`",
                "",
                "## Conteudo proposto",
                "",
                content,
                "",
            ]
        ),
        encoding="utf-8",
    )
    return out


def sync(apply: bool, max_items: int | None = None) -> dict:
    stats = {"checked": 0, "skipped": 0, "would_write": 0, "written": 0, "review": 0, "errors": []}
    for item in query_index():
        if max_items is not None and stats["checked"] >= max_items:
            break
        stats["checked"] += 1
        props = item.get("properties", {})
        cofre_path = prop_text(props, "Caminho Cofre").strip()
        update_allowed = prop_text(props, "Atualizar Cofre") == "true"
        protected = prop_text(props, "Protegido") == "true"
        direction = prop_text(props, "Direcao Sync")

        if not cofre_path or not update_allowed or direction not in {"Notion -> Cofre", "Bidirecional governado"}:
            stats["skipped"] += 1
            continue

        try:
            markdown = page_markdown(item["id"])
            content = body_without_frontmatter(markdown)
            if not content:
                stats["skipped"] += 1
                continue
            target = (WORKSPACE / cofre_path).resolve()
            if WORKSPACE not in target.parents and target != WORKSPACE:
                raise RuntimeError(f"caminho fora do Cofre: {cofre_path}")
            if is_protected(cofre_path, protected):
                if apply:
                    write_review(cofre_path, content)
                    stats["review"] += 1
                else:
                    stats["would_write"] += 1
                continue
            if apply:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content + "\n", encoding="utf-8")
                stats["written"] += 1
            else:
                stats["would_write"] += 1
        except Exception as exc:  # noqa: BLE001
            stats["errors"].append({"page_id": item.get("id"), "path": cofre_path, "error": str(exc)})
    return stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="grava alteracoes permitidas no Cofre")
    parser.add_argument("--max-items", type=int, help="limita a quantidade de itens verificados")
    args = parser.parse_args()
    print(json.dumps(sync(apply=args.apply, max_items=args.max_items), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
