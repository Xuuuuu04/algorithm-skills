#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def get_json(url: str, headers: Dict[str, str], timeout: int) -> Dict:
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def get_text(url: str, headers: Dict[str, str], timeout: int) -> Optional[str]:
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as e:
        if e.code in {403, 404, 429}:
            return None
        raise
    except Exception:
        return None


def parse_version(v: str) -> Tuple[int, ...]:
    parts = re.findall(r"\d+", v)
    return tuple(int(x) for x in parts[:3]) if parts else (0,)


def version_ge(v: str, target: str) -> bool:
    a = parse_version(v)
    b = parse_version(target)
    return a >= b


def extract_cjc_version(cjpm_text: str) -> Optional[str]:
    m = re.search(r'cjc-version\s*=\s*"([^"]+)"', cjpm_text)
    if not m:
        return None
    return m.group(1).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch active cangjielanguage-sig repos supporting cjc>=1.0.0")
    parser.add_argument("--org", default="cangjielanguage-sig")
    parser.add_argument("--min-version", default="1.0.0")
    parser.add_argument("--active-days", type=int, default=0)
    parser.add_argument("--per-page", type=int, default=100)
    parser.add_argument("--workers", type=int, default=24)
    parser.add_argument("--api-timeout", type=int, default=30)
    parser.add_argument("--raw-timeout", type=int, default=8)
    parser.add_argument(
        "--github-token",
        default=os.environ.get("GITHUB_TOKEN", ""),
        help="GitHub token for higher API rate limits. Defaults to $GITHUB_TOKEN.",
    )
    parser.add_argument(
        "--out-jsonl",
        default="../references/active_repos_1_0_0_plus.jsonl",
        help="Output JSONL path relative to this script.",
    )
    parser.add_argument(
        "--out-md",
        default="../references/active_repos_1_0_0_plus.md",
        help="Output markdown path relative to this script.",
    )
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    out_jsonl = (base / args.out_jsonl).resolve()
    out_md = (base / args.out_md).resolve()
    api_headers = {
        "User-Agent": "algorithm-skills/1.0",
        "Accept": "application/vnd.github+json",
    }
    raw_headers = {"User-Agent": "algorithm-skills/1.0"}
    if args.github_token:
        api_headers["Authorization"] = f"Bearer {args.github_token}"
        raw_headers["Authorization"] = f"Bearer {args.github_token}"

    repos: List[Dict] = []
    page = 1
    while True:
        api = (
            f"https://api.github.com/orgs/{args.org}/repos"
            f"?per_page={args.per_page}&type=public&page={page}"
        )
        payload = get_json(api, headers=api_headers, timeout=args.api_timeout)
        if not isinstance(payload, list):
            raise RuntimeError(f"GitHub API returned unexpected payload: {payload}")
        if not payload:
            break
        repos.extend(payload)
        if len(payload) < args.per_page:
            break
        page += 1

    now = dt.datetime.now(dt.timezone.utc)
    active_threshold = now - dt.timedelta(days=args.active_days) if args.active_days > 0 else None

    candidates: List[Dict] = []
    for repo in repos:
        if repo.get("archived") or repo.get("disabled"):
            continue
        pushed_at = repo.get("pushed_at")
        if not pushed_at:
            continue
        pushed = dt.datetime.fromisoformat(pushed_at.replace("Z", "+00:00"))
        is_active = active_threshold is None or pushed >= active_threshold
        if not is_active:
            continue
        candidates.append(repo)

    def process_repo(repo: Dict) -> Optional[Dict]:
        name = repo.get("name", "")
        default_branch = repo.get("default_branch", "main")
        raw_cjpm = f"https://raw.githubusercontent.com/{args.org}/{name}/{default_branch}/cjpm.toml"
        cjpm_text = get_text(raw_cjpm, headers=raw_headers, timeout=args.raw_timeout)
        if not cjpm_text:
            return None

        cjc_version = extract_cjc_version(cjpm_text)
        if not cjc_version:
            return None
        if not version_ge(cjc_version, args.min_version):
            return None

        return {
            "name": name,
            "full_name": repo.get("full_name", ""),
            "html_url": repo.get("html_url", ""),
            "description": repo.get("description") or "",
            "stars": repo.get("stargazers_count", 0),
            "forks": repo.get("forks_count", 0),
            "language": repo.get("language") or "",
            "default_branch": default_branch,
            "pushed_at": pushed_at,
            "is_active": is_active,
            "cjc_version": cjc_version,
            "raw_cjpm": raw_cjpm,
        }

    rows: List[Dict] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(process_repo, repo) for repo in candidates]
        for future in concurrent.futures.as_completed(futures):
            row = future.result()
            if row:
                rows.append(row)

    rows.sort(key=lambda x: (x["pushed_at"], x["stars"]), reverse=True)

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    lines: List[str] = []
    lines.append("# CangjieSIG 活跃仓库（支持 cjc >= 1.0.0）")
    lines.append("")
    lines.append(f"组织：`{args.org}`")
    lines.append(f"总仓库数（筛选后）：{len(rows)}")
    lines.append("")
    lines.append("| Repo | cjc-version | Stars | Last Push | URL |")
    lines.append("|---|---|---:|---|---|")
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['cjc_version']} | {row['stars']} | {row['pushed_at'][:10]} | [link]({row['html_url']}) |"
        )

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {len(rows)} repos -> {out_jsonl}")
    print(f"wrote markdown -> {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
