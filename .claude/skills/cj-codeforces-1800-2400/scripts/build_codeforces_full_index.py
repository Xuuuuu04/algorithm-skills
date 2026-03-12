#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import ssl
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, List

API_URL = "https://codeforces.com/api/problemset.problems"


def fetch_json(url: str) -> Dict:
    req = urllib.request.Request(url, headers={"User-Agent": "algorithm-skills/1.0"})
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def to_key(contest_id: int, index: str) -> str:
    return f"{contest_id}-{index}"


def tutorial_search_url(contest_id: int, index: str, name: str) -> str:
    q = f"{contest_id}{index} {name} tutorial"
    return "https://codeforces.com/search?query=" + urllib.parse.quote(q)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build full Codeforces problem + answer-entry index.")
    parser.add_argument(
        "--out-jsonl",
        default="../references/problems_all_full.jsonl",
        help="Output JSONL path relative to this script.",
    )
    parser.add_argument(
        "--out-md",
        default="../references/problems_all_answer_index.md",
        help="Output markdown index path relative to this script.",
    )
    parser.add_argument(
        "--out-summary-md",
        default="../references/problems_all_summary.md",
        help="Output summary markdown path relative to this script.",
    )
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    out_jsonl = (base / args.out_jsonl).resolve()
    out_md = (base / args.out_md).resolve()
    out_summary_md = (base / args.out_summary_md).resolve()

    payload = fetch_json(API_URL)
    if payload.get("status") != "OK":
        raise RuntimeError(f"Codeforces API failed: {payload.get('comment', 'unknown')}")

    problems = payload["result"]["problems"]
    stats = payload["result"]["problemStatistics"]
    solved_map: Dict[str, int] = {
        to_key(item.get("contestId"), item.get("index", "")): item.get("solvedCount", 0)
        for item in stats
        if item.get("contestId") is not None and item.get("index") is not None
    }

    rows: List[Dict] = []
    for p in problems:
        contest_id = p.get("contestId")
        index = p.get("index")
        name = p.get("name", "")
        if contest_id is None or index is None:
            continue
        key = to_key(contest_id, index)
        rating = p.get("rating")
        row = {
            "id": f"CF-{contest_id}{index}",
            "contest_id": contest_id,
            "index": index,
            "name": name,
            "rating": rating,
            "type": p.get("type", ""),
            "points": p.get("points"),
            "tags": p.get("tags", []),
            "solved_count": solved_map.get(key, 0),
            "problem_url": f"https://codeforces.com/problemset/problem/{contest_id}/{index}",
            "answer_index_url": f"https://codeforces.com/problemset/status/{contest_id}/problem/{index}",
            "ok_submissions_url": f"https://codeforces.com/problemset/status/{contest_id}/problem/{index}?order=BY_PROGRAM_LENGTH_ASC&status=OK",
            "tutorial_search_url": tutorial_search_url(contest_id, index, name),
        }
        rows.append(row)

    rows.sort(
        key=lambda x: (
            x["rating"] if x["rating"] is not None else 10**9,
            -x["solved_count"],
            x["contest_id"],
            x["index"],
        )
    )

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    rating_count: Dict[str, int] = {}
    tag_count: Dict[str, int] = {}
    for r in rows:
        rk = str(r["rating"]) if r["rating"] is not None else "Unrated"
        rating_count[rk] = rating_count.get(rk, 0) + 1
        for t in r["tags"]:
            tag_count[t] = tag_count.get(t, 0) + 1

    lines: List[str] = []
    lines.append("# Codeforces 全量题目 + 答案入口索引")
    lines.append("")
    lines.append(f"总题量：{len(rows)}")
    lines.append("")
    lines.append("说明：`题目` 链接跳转原题，`答案入口` 链接跳转提交列表，`OK提交` 链接按最短代码排序且状态为 OK，`题解检索` 链接用于快速检索教程。")
    lines.append("")
    lines.append("| ID | Rating | Name | Tags | 题目 | 答案入口 | OK提交 | 题解检索 |")
    lines.append("|---|---:|---|---|---|---|---|---|")
    for r in rows:
        tags = ", ".join(r["tags"][:5])
        rating = r["rating"] if r["rating"] is not None else "-"
        lines.append(
            f"| {r['id']} | {rating} | {r['name']} | {tags} | [题目]({r['problem_url']}) | "
            f"[答案入口]({r['answer_index_url']}) | [OK提交]({r['ok_submissions_url']}) | [检索]({r['tutorial_search_url']}) |"
        )
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    top_tags = sorted(tag_count.items(), key=lambda x: (-x[1], x[0]))[:80]
    summary: List[str] = []
    summary.append("# Codeforces 全量题目摘要")
    summary.append("")
    summary.append(f"总题量：{len(rows)}")
    summary.append("")
    summary.append("## 评分分布")
    summary.append("")
    summary.append("| Rating | Count |")
    summary.append("|---:|---:|")
    for k in sorted(rating_count, key=lambda x: (10**9 if x == "Unrated" else int(x))):
        summary.append(f"| {k} | {rating_count[k]} |")
    summary.append("")
    summary.append("## 高频标签 Top 80")
    summary.append("")
    summary.append("| Tag | Count |")
    summary.append("|---|---:|")
    for t, c in top_tags:
        summary.append(f"| {t} | {c} |")
    summary.append("")
    summary.append(f"详见：[{out_md.name}]({out_md.name})")
    out_summary_md.write_text("\n".join(summary) + "\n", encoding="utf-8")

    print(f"wrote {len(rows)} rows -> {out_jsonl}")
    print(f"wrote full index -> {out_md}")
    print(f"wrote summary -> {out_summary_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
