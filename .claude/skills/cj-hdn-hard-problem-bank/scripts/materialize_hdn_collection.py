#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Dict, List


def read_jsonl(path: Path) -> List[Dict]:
    rows: List[Dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def md_cell(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def sanitize_name(name: str) -> str:
    raw = "".join(ch if ch.isalnum() or ch in {"-", "_"} else "-" for ch in name.lower())
    while "--" in raw:
        raw = raw.replace("--", "-")
    return raw.strip("-") or "item"


def best_title(row: Dict) -> str:
    raw = row.get("raw")
    if isinstance(raw, dict):
        custom_title = raw.get("customTitle")
        if isinstance(custom_title, dict):
            if custom_title.get("zh"):
                return str(custom_title["zh"])
            if custom_title.get("en"):
                return str(custom_title["en"])
    return str(row.get("title", "unknown"))


def summary_text(row: Dict) -> str:
    raw = row.get("raw")
    if isinstance(raw, dict):
        description = raw.get("description")
        if isinstance(description, dict):
            for key in ("zh", "en"):
                value = description.get(key)
                if value:
                    text = str(value).replace("\n", " ").strip()
                    return text[:220] + ("..." if len(text) > 220 else "")
    tags = row.get("tags") or []
    if tags:
        return f"当前公开信息有限，这条资料来自 `{'、'.join(tags)}` 推荐槽位，建议继续人工补写题意和方案。"
    return "当前公开信息有限，建议后续补入完整题意、样例和解题思路。"


def render_doc(row: Dict) -> str:
    title = md_cell(best_title(row))
    tags = row.get("tags") or []
    tags_text = "、".join(f"`{md_cell(tag)}`" for tag in tags) if tags else "无"
    return "\n".join(
        [
            f"# {title}",
            "",
            "## 基本信息",
            "",
            "| 字段 | 内容 |",
            "|---|---|",
            f"| 来源 | {md_cell(row.get('source', ''))} |",
            f"| 难度 | {md_cell(row.get('difficulty', ''))} |",
            f"| 标签 | {tags_text} |",
            f"| 原始链接 | [source]({row.get('url', '')}) |",
            "",
            "## 公共摘要",
            "",
            summary_text(row),
            "",
            "## 本地补充位",
            "",
            "这里预留给后续补充题面整理、解题思路、参考实现和踩坑记录。",
            "",
        ]
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize HDN entries into one-doc-per-item collection.")
    parser.add_argument("--source-jsonl", default="../references/hdn_hard_problems.jsonl")
    parser.add_argument("--out-dir", default="../references/problem-collection")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    source_jsonl = (base / args.source_jsonl).resolve()
    out_dir = (base / args.out_dir).resolve()
    rows = read_jsonl(source_jsonl)

    if args.clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    index_lines: List[str] = []
    index_lines.append("# 黄大年实体题目集合")
    index_lines.append("")
    index_lines.append(f"总文档数：{len(rows)}")
    index_lines.append("")
    index_lines.append("| 条目 | 来源 | 本地文档 |")
    index_lines.append("|---|---|---|")

    for idx, row in enumerate(rows, start=1):
        title = best_title(row)
        filename = f"{idx:03d}-{sanitize_name(title)[:80]}.md"
        raw_name = f"{idx:03d}-{sanitize_name(title)[:80]}.json"
        (out_dir / filename).write_text(render_doc(row), encoding="utf-8")
        (out_dir / raw_name).write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        index_lines.append(f"| {md_cell(title)} | {md_cell(row.get('source', ''))} | [{filename}]({filename}) |")

    (out_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"materialized {len(rows)} hdn docs -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
