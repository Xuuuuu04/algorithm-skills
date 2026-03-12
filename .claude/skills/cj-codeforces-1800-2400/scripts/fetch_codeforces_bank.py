#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import ssl
import urllib.request
from pathlib import Path
from typing import Dict, List, Tuple

API_URL = "https://codeforces.com/api/problemset.problems"

TAG_PATTERN_MAP: Dict[str, str] = {
    "dp": "动态规划（状态设计与转移方程）",
    "graphs": "图论（最短路/连通性/拓扑）",
    "data structures": "数据结构（线段树/BIT/平衡树）",
    "greedy": "贪心（排序+局部最优证明）",
    "binary search": "二分答案（单调性判定）",
    "math": "数学（数论/组合计数）",
    "number theory": "数论（质因数/同余/逆元）",
    "trees": "树算法（树形 DP/LCA/重链剖分）",
    "strings": "字符串（KMP/哈希/自动机）",
    "constructive algorithms": "构造（不变量与可行性）",
    "flows": "网络流（最大流/最小割）",
}


def fetch_json(url: str) -> Dict:
    req = urllib.request.Request(url, headers={"User-Agent": "algorithm-skills/1.0"})
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        return json.loads(resp.read().decode("utf-8", errors="ignore"))


def to_key(contest_id: int, index: str) -> str:
    return f"{contest_id}-{index}"


def map_patterns(tags: List[str]) -> List[str]:
    patterns: List[str] = []
    for t in tags:
        if t in TAG_PATTERN_MAP:
            patterns.append(TAG_PATTERN_MAP[t])
    dedup: List[str] = []
    seen = set()
    for p in patterns:
        if p not in seen:
            seen.add(p)
            dedup.append(p)
    return dedup


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch Codeforces 1800-2400 problem bank")
    parser.add_argument("--min-rating", type=int, default=1800)
    parser.add_argument("--max-rating", type=int, default=2400)
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max number of rows to keep. 0 means no limit.",
    )
    parser.add_argument(
        "--out-jsonl",
        default="../references/problems_1800_2400.jsonl",
        help="Output JSONL path relative to this script.",
    )
    parser.add_argument(
        "--out-md",
        default="../references/problems_1800_2400.md",
        help="Output markdown path relative to this script.",
    )
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    out_jsonl = (base / args.out_jsonl).resolve()
    out_md = (base / args.out_md).resolve()

    data = fetch_json(API_URL)
    if data.get("status") != "OK":
        raise RuntimeError(f"Codeforces API failed: {data.get('comment', 'unknown error')}")

    problems = data["result"]["problems"]
    stats = data["result"]["problemStatistics"]
    solved: Dict[str, int] = {
        to_key(item.get("contestId"), item.get("index", "")): item.get("solvedCount", 0)
        for item in stats
        if item.get("contestId") is not None
    }

    rows: List[Dict] = []
    for p in problems:
        rating = p.get("rating")
        contest_id = p.get("contestId")
        index = p.get("index")
        if rating is None or contest_id is None or index is None:
            continue
        if not (args.min_rating <= rating <= args.max_rating):
            continue
        if p.get("type") != "PROGRAMMING":
            continue

        tags = p.get("tags", [])
        key = to_key(contest_id, index)
        rows.append(
            {
                "id": f"CF-{contest_id}{index}",
                "contest_id": contest_id,
                "index": index,
                "name": p.get("name", ""),
                "rating": rating,
                "tags": tags,
                "url": f"https://codeforces.com/problemset/problem/{contest_id}/{index}",
                "answer_index_url": f"https://codeforces.com/problemset/status/{contest_id}/problem/{index}",
                "ok_submissions_url": (
                    f"https://codeforces.com/problemset/status/{contest_id}/problem/{index}"
                    "?order=BY_PROGRAM_LENGTH_ASC&status=OK"
                ),
                "tutorial_search_url": (
                    f"https://codeforces.com/search?query={contest_id}{index}%20{p.get('name', '')}%20tutorial"
                ),
                "solved_count": solved.get(key, 0),
                "suggested_patterns": map_patterns(tags),
                "note": "先按标签定位算法，再回到仓颉模板实现。",
            }
        )

    rows.sort(key=lambda x: (x["rating"], -x["solved_count"], x["contest_id"], x["index"]))
    if args.limit > 0:
        rows = rows[: args.limit]

    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    by_rating: Dict[int, int] = {}
    for r in rows:
        by_rating[r["rating"]] = by_rating.get(r["rating"], 0) + 1

    lines: List[str] = []
    lines.append("# Codeforces 1800-2400 题库")
    lines.append("")
    lines.append(f"总题量：{len(rows)}")
    lines.append("")
    lines.append("## 评分分布")
    lines.append("")
    lines.append("| Rating | Count |")
    lines.append("|---:|---:|")
    for rating in sorted(by_rating):
        lines.append(f"| {rating} | {by_rating[rating]} |")
    lines.append("")
    lines.append("## 全量条目")
    lines.append("")
    lines.append("| ID | Rating | Name | Tags | 题目链接 | 答案入口 | OK提交 | 题解检索 |")
    lines.append("|---|---:|---|---|---|---|---|---|")
    for row in rows:
        tags = ", ".join(row["tags"][:4])
        lines.append(
            f"| {row['id']} | {row['rating']} | {row['name']} | {tags} | "
            f"[题目]({row['url']}) | [答案入口]({row['answer_index_url']}) | "
            f"[OK提交]({row['ok_submissions_url']}) | [检索]({row['tutorial_search_url']}) |"
        )

    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(rows)} problems -> {out_jsonl}")
    print(f"wrote markdown -> {out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
