#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import ssl
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path
from typing import Dict, List, Set

PROBLEM_KEYWORDS = ["problem", "challenge", "contest", "题", "算法", "解题"]


def md_cell(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").replace("\n", " ").strip()


def fetch_html(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "algorithm-skills/1.0"})
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def extract_links(base_url: str, html: str) -> List[str]:
    links = re.findall(r'href=["\']([^"\']+)["\']', html, flags=re.I)
    out: List[str] = []
    for link in links:
        u = urllib.parse.urljoin(base_url, link)
        out.append(u)
    return out


def looks_like_problem(url: str, title: str) -> bool:
    text = (url + " " + title).lower()
    return any(k in text for k in PROBLEM_KEYWORDS)


def host_allowed(url: str, allowed_hosts: Set[str]) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    if not host:
        return False
    for h in allowed_hosts:
        if host == h or host.endswith("." + h):
            return True
    return False


def to_markdown(rows: List[Dict]) -> str:
    lines: List[str] = []
    lines.append("# 黄大年高难题参考库")
    lines.append("")
    lines.append(f"总条目：{len(rows)}")
    lines.append("")
    lines.append("| Title | Source | Difficulty | URL |")
    lines.append("|---|---|---|---|")
    for r in rows:
        title = md_cell(r.get("title", ""))
        source = md_cell(r.get("source", ""))
        difficulty = md_cell(r.get("difficulty", ""))
        url = md_cell(r.get("url", ""))
        lines.append(
            f"| {title} | {source} | {difficulty} | [link]({url}) |"
        )
    return "\n".join(lines) + "\n"


def fetch_json_with_headers(url: str, headers: Dict[str, str], timeout: int = 20) -> Dict:
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def normalize_api_rows(items: List[Dict], source_name: str) -> List[Dict]:
    out: List[Dict] = []
    for it in items:
        title = (
            it.get("title")
            or it.get("name")
            or it.get("questionTitle")
            or it.get("puzzleTitle")
            or "unknown-title"
        )
        pid = it.get("id") or it.get("questionId") or it.get("puzzleId") or ""
        url = it.get("detailUrl") or it.get("url") or ""
        if not url and pid:
            url = f"https://www.chaspark.com/#/puzzle/{pid}"
        out.append(
            {
                "source": source_name,
                "title": str(title),
                "url": str(url),
                "difficulty": str(it.get("difficulty") or it.get("level") or "Hard"),
                "tags": it.get("tags") if isinstance(it.get("tags"), list) else [],
                "core_idea": "待补充",
                "pitfalls": "待补充",
                "raw": it,
            }
        )
    return out


def normalize_public_slot_rows(payload_data: List[Dict]) -> List[Dict]:
    rows: List[Dict] = []
    for slot in payload_data:
        slot_name = str(slot.get("slot", ""))
        contents = slot.get("contents")
        if not isinstance(contents, list):
            continue
        for it in contents:
            if not isinstance(it, dict):
                continue
            title = str(
                it.get("title")
                or it.get("name")
                or it.get("contentTitle")
                or it.get("summary")
                or "unknown-title"
            )
            url = str(it.get("linkAddress") or it.get("url") or it.get("detailUrl") or "")
            if url.startswith("#/"):
                url = "https://www.chaspark.com/" + url
            text = (title + " " + url).lower()
            if not any(k in text for k in ("挑战", "难题", "challenge", "contest", "/races", "/question")):
                continue
            rows.append(
                {
                    "source": "public_slot_api",
                    "title": title,
                    "url": url,
                    "difficulty": "Hard",
                    "tags": [slot_name] if slot_name else [],
                    "core_idea": "待补充",
                    "pitfalls": "待补充",
                    "raw": it,
                }
            )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch HDN hard problem bank with crawler + CSV import fallback")
    parser.add_argument("--seed-url", action="append", default=[])
    parser.add_argument("--max-pages", type=int, default=200)
    parser.add_argument("--use-api", action="store_true", help="Try official API endpoints first.")
    parser.add_argument("--api-token", default="", help="Optional X-CSRF-TOKEN value.")
    parser.add_argument("--cookie", default="", help="Optional Cookie header string.")
    parser.add_argument("--import-csv", default="")
    parser.add_argument("--out-jsonl", default="../references/hdn_hard_problems.jsonl")
    parser.add_argument("--out-md", default="../references/hdn_hard_problems.md")
    parser.add_argument("--out-log", default="../references/hdn_fetch_log.json")
    parser.add_argument("--template-csv", default="../references/hdn_manual_import_template.csv")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    out_jsonl = (base / args.out_jsonl).resolve()
    out_md = (base / args.out_md).resolve()
    out_log = (base / args.out_log).resolve()
    template_csv = (base / args.template_csv).resolve()

    seed_urls = args.seed_url or ["https://chaspark.com", "https://www.chaspark.com"]
    allowed_hosts = {urllib.parse.urlparse(u).netloc.lower() for u in seed_urls if urllib.parse.urlparse(u).netloc}

    rows: List[Dict] = []
    fetch_log: Dict[str, object] = {"seed_urls": seed_urls, "visited": 0, "errors": []}

    if args.import_csv:
        csv_path = (base / args.import_csv).resolve()
        if csv_path.exists():
            with csv_path.open("r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for item in reader:
                    rows.append(
                        {
                            "source": item.get("source", "manual"),
                            "title": item.get("title", ""),
                            "url": item.get("url", ""),
                            "difficulty": item.get("difficulty", "Hard"),
                            "tags": [t.strip() for t in item.get("tags", "").split(",") if t.strip()],
                            "core_idea": item.get("core_idea", ""),
                            "pitfalls": item.get("pitfalls", ""),
                        }
                    )

    if args.use_api and not rows:
        api_candidates = [
            "https://www.chaspark.com/chasiwu/v1/content/puzzle/list?current=1&size=200",
            "https://www.chaspark.com/chasiwu/v1/question/challenge-list?current=1&size=200",
            "https://www.chaspark.com/chasiwu/v1/content/races/question/list?current=1&size=200",
        ]
        headers = {
            "User-Agent": "algorithm-skills/1.0",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.chaspark.com/",
            "Origin": "https://www.chaspark.com",
        }
        if args.api_token:
            headers["X-CSRF-TOKEN"] = args.api_token
        if args.cookie:
            headers["Cookie"] = args.cookie

        for api in api_candidates:
            try:
                payload = fetch_json_with_headers(api, headers=headers, timeout=20)
            except Exception as exc:
                fetch_log["errors"].append({"url": api, "error": str(exc)})
                continue

            code = str(payload.get("code", ""))
            if code not in {"0", "200", "OK"}:
                fetch_log["errors"].append({"url": api, "error": f"api_code={code}"})
                continue

            data = payload.get("data")
            items: List[Dict] = []
            if isinstance(data, dict):
                if isinstance(data.get("list"), list):
                    items = data.get("list")
                elif isinstance(data.get("records"), list):
                    items = data.get("records")
            elif isinstance(data, list):
                items = data

            if items:
                rows.extend(normalize_api_rows(items, source_name="api"))

        # Fallback for unauthenticated mode: public home recommendation slots.
        if not rows:
            public_api = (
                "https://www.chaspark.com/chasiwu/v1/content/recommend/slot"
                "?slot=homeRaces,homePuzzle,homeActivity&size=200&current=1&lang=zh"
            )
            try:
                payload = fetch_json_with_headers(public_api, headers=headers, timeout=20)
                if str(payload.get("code", "")) == "0" and isinstance(payload.get("data"), list):
                    rows.extend(normalize_public_slot_rows(payload.get("data")))
                else:
                    fetch_log["errors"].append({"url": public_api, "error": f"api_code={payload.get('code', '')}"})
            except Exception as exc:
                fetch_log["errors"].append({"url": public_api, "error": str(exc)})

    visited: Set[str] = set()
    q = deque(seed_urls)

    while q and len(visited) < args.max_pages and not rows:
        url = q.popleft()
        if url in visited:
            continue
        visited.add(url)
        try:
            html = fetch_html(url)
        except Exception as exc:
            fetch_log["errors"].append({"url": url, "error": str(exc)})
            continue

        title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
        title = title_match.group(1).strip() if title_match else ""
        if looks_like_problem(url, title):
            rows.append(
                {
                    "source": "crawler",
                    "title": title or "unknown-title",
                    "url": url,
                    "difficulty": "Hard",
                    "tags": [],
                    "core_idea": "待补充",
                    "pitfalls": "待补充",
                }
            )
            break

        for nxt in extract_links(url, html):
            if nxt.startswith("http") and host_allowed(nxt, allowed_hosts) and nxt not in visited:
                q.append(nxt)

    fetch_log["visited"] = len(visited)
    # Deduplicate by URL or title for mixed API/crawler sources.
    uniq: Dict[str, Dict] = {}
    for row in rows:
        key = row.get("url") or row.get("title") or json.dumps(row, ensure_ascii=False)
        uniq[str(key)] = row
    rows = list(uniq.values())
    fetch_log["items"] = len(rows)

    if not template_csv.exists():
        template_csv.parent.mkdir(parents=True, exist_ok=True)
        with template_csv.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["source", "title", "url", "difficulty", "tags", "core_idea", "pitfalls"])
            writer.writerow(["manual", "示例题目", "https://example.com/problem", "Hard", "dp,graphs", "状态压缩+最短路", "边界和溢出"])

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    out_md.write_text(to_markdown(rows), encoding="utf-8")
    out_log.write_text(json.dumps(fetch_log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {len(rows)} entries -> {out_jsonl}")
    print(f"template csv -> {template_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
