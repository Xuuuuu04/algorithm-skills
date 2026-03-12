#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import shutil
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional


def read_jsonl(path: Path) -> List[Dict]:
    rows: List[Dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def get_text(url: str, headers: Dict[str, str], timeout: int = 20) -> Optional[str]:
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 404, 429}:
            return None
        raise
    except Exception:
        return None


def get_json(url: str, headers: Dict[str, str], timeout: int = 20) -> Optional[object]:
    text = get_text(url, headers=headers, timeout=timeout)
    if text is None:
        return None
    try:
        return json.loads(text)
    except Exception:
        return None


def sanitize_name(name: str) -> str:
    return "".join(ch if ch.isalnum() or ch in {"-", "_", "."} else "-" for ch in name)


def md_cell(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").strip()


def render_repo_readme(row: Dict, root_listing: List[str], has_cjpm: bool, has_remote_readme: bool) -> str:
    description = row.get("description") or "仓库未提供描述。"
    listing = "、".join(f"`{name}`" for name in root_listing[:20]) if root_listing else "未抓到根目录清单。"
    return "\n".join(
        [
            f"# {md_cell(row.get('name', ''))}",
            "",
            "## 仓库概况",
            "",
            f"{description}",
            "",
            "## 基本信息",
            "",
            "| 字段 | 内容 |",
            "|---|---|",
            f"| 仓库 | {md_cell(row.get('full_name', ''))} |",
            f"| cjc-version | {md_cell(row.get('cjc_version', ''))} |",
            f"| Stars | {row.get('stars', 0)} |",
            f"| Forks | {row.get('forks', 0)} |",
            f"| 语言 | {md_cell(row.get('language', ''))} |",
            f"| 默认分支 | {md_cell(row.get('default_branch', ''))} |",
            f"| 最近提交 | {md_cell(row.get('pushed_at', ''))} |",
            f"| 仓库链接 | [repo]({row.get('html_url', '')}) |",
            "",
            "## 本地快照内容",
            "",
            f"当前目录已经落地了仓库元信息、根目录清单，以及 {'`cjpm.toml`' if has_cjpm else '未抓到 `cjpm.toml`'}。"
            f"{' 同时补了远端 README 快照。' if has_remote_readme else ' 远端 README 未抓到时，保留为生成说明。'}",
            "",
            "## 根目录观察",
            "",
            listing,
            "",
            "## 使用建议",
            "",
            "优先从这个目录判断仓库是否能作为比赛参考，再决定是否进一步克隆全仓或抽取模板文件。",
            "",
        ]
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize CangjieSIG repos into one-folder-per-project collection.")
    parser.add_argument("--source-jsonl", default="../references/active_repos_1_0_0_plus.jsonl")
    parser.add_argument("--out-dir", default="../references/repo-collection")
    parser.add_argument("--clean", action="store_true")
    parser.add_argument("--github-token", default=os.environ.get("GITHUB_TOKEN", ""))
    parser.add_argument("--workers", type=int, default=12)
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    source_jsonl = (base / args.source_jsonl).resolve()
    out_dir = (base / args.out_dir).resolve()

    rows = read_jsonl(source_jsonl)
    if args.clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    headers = {
        "User-Agent": "algorithm-skills/1.0",
        "Accept": "application/vnd.github+json",
    }
    raw_headers = {"User-Agent": "algorithm-skills/1.0"}
    if args.github_token:
        headers["Authorization"] = f"Bearer {args.github_token}"
        raw_headers["Authorization"] = f"Bearer {args.github_token}"

    index_lines: List[str] = []
    index_lines.append("# CangjieSIG 实体仓库集合")
    index_lines.append("")
    index_lines.append(f"总目录数：{len(rows)}")
    index_lines.append("")
    index_lines.append("| 仓库 | cjc-version | Stars | 本地目录 |")
    index_lines.append("|---|---|---:|---|")

    def materialize_one(row: Dict) -> Dict:
        repo_name = str(row.get("name", "unknown"))
        folder_name = sanitize_name(repo_name)
        repo_dir = out_dir / folder_name
        repo_dir.mkdir(parents=True, exist_ok=True)

        metadata_path = repo_dir / "metadata.json"
        metadata_path.write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        full_name = row.get("full_name", "")
        default_branch = row.get("default_branch", "main")
        root_api = f"https://api.github.com/repos/{full_name}/contents?ref={default_branch}"
        root_payload = get_json(root_api, headers=headers, timeout=12)
        root_listing: List[str] = []
        if isinstance(root_payload, list):
            root_listing = [str(item.get("name", "")) for item in root_payload if isinstance(item, dict)]
            (repo_dir / "root-tree.json").write_text(
                json.dumps(root_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

        cjpm_url = row.get("raw_cjpm", "")
        cjpm_text = get_text(cjpm_url, headers=raw_headers, timeout=10) if cjpm_url else None
        has_cjpm = cjpm_text is not None
        if cjpm_text is not None:
            (repo_dir / "cjpm.toml").write_text(cjpm_text, encoding="utf-8")

        readme_candidates = [
            f"https://raw.githubusercontent.com/{full_name}/{default_branch}/README.md",
            f"https://raw.githubusercontent.com/{full_name}/{default_branch}/readme.md",
            f"https://raw.githubusercontent.com/{full_name}/{default_branch}/README_CN.md",
        ]
        remote_readme = None
        for candidate in readme_candidates:
            remote_readme = get_text(candidate, headers=raw_headers, timeout=10)
            if remote_readme:
                break
        has_remote_readme = remote_readme is not None
        if remote_readme is not None:
            (repo_dir / "UPSTREAM_README.md").write_text(remote_readme, encoding="utf-8")

        repo_readme = render_repo_readme(row, root_listing, has_cjpm, has_remote_readme)
        (repo_dir / "README.md").write_text(repo_readme, encoding="utf-8")

        return {
            "repo_name": repo_name,
            "folder_name": folder_name,
            "cjc_version": row.get("cjc_version", ""),
            "stars": row.get("stars", 0),
        }

    done_rows: List[Dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(materialize_one, row) for row in rows]
        for future in concurrent.futures.as_completed(futures):
            done_rows.append(future.result())

    done_rows.sort(key=lambda item: item["repo_name"].lower())
    for item in done_rows:
        index_lines.append(
            f"| {md_cell(item['repo_name'])} | {md_cell(item['cjc_version'])} | {item['stars']} | `{item['folder_name']}` |"
        )

    (out_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"materialized {len(rows)} repos -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
