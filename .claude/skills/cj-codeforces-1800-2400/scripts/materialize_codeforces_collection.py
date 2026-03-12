#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional

TAG_HINTS: Dict[str, str] = {
    "dp": "核心通常在状态设计、转移顺序和边界初始化。",
    "graphs": "重点检查建图方式、连通性条件和复杂度上界。",
    "trees": "优先判断是否是树形 DP、换根、LCA 或重链问题。",
    "greedy": "需要证明局部最优能够推出全局最优。",
    "binary search": "先确认单调性，再定义判定函数。",
    "data structures": "一般需要把查询或修改压到对数复杂度。",
    "sortings": "多半要先排序再讨论相对位置或贪心顺序。",
    "math": "需要先化简公式，再决定是否做数论或组合计数。",
    "number theory": "注意质因数分解、欧拉函数、同余和逆元。",
    "strings": "先判断是匹配、回文、哈希还是字典序问题。",
    "constructive algorithms": "先抓住不变量，再安排构造顺序。",
    "bitmasks": "通常适合状态压缩、位运算贪心或拆位讨论。",
    "divide and conquer": "先判断能否拆成独立子问题并合并答案。",
    "dfs and similar": "递归边界、回溯状态和父子关系最容易出错。",
    "shortest paths": "先看边权性质，再选 BFS、Dijkstra 或分层图。",
    "combinatorics": "注意重复计数、容斥和组合数预处理。",
    "two pointers": "关键是维护窗口不变量和指针移动条件。",
    "interactive": "必须把查询策略和输出刷新时机写清楚。",
}

TAG_TO_SKILLS: Dict[str, List[str]] = {
    "dp": ["cj-algo-patterns", "cj-language-core"],
    "graphs": ["cj-algo-patterns", "cangjie-std-arraylist"],
    "trees": ["cj-algo-patterns", "cangjie-std-arraylist"],
    "greedy": ["cj-algo-patterns"],
    "binary search": ["cj-algo-patterns"],
    "data structures": ["cj-algo-patterns", "cj-std-algo-toolkit"],
    "sortings": ["cj-std-algo-toolkit"],
    "math": ["cj-algo-patterns", "cj-std-algo-toolkit"],
    "number theory": ["cj-algo-patterns", "cj-std-algo-toolkit"],
    "strings": ["cj-algo-patterns", "cangjie-std-string"],
    "constructive algorithms": ["cj-algo-patterns"],
    "bitmasks": ["cj-algo-patterns"],
    "shortest paths": ["cj-algo-patterns", "cj-std-algo-toolkit"],
}


def md_cell(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").strip()


def read_jsonl(path: Path) -> List[Dict]:
    rows: List[Dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def rating_bucket(rating: Optional[int]) -> str:
    if rating is None:
        return "unrated"
    return f"rating-{rating}"


def training_position(row: Dict) -> str:
    rating = row.get("rating")
    tags = row.get("tags") or []
    tag_text = "、".join(tags[:3]) if tags else "综合"
    if rating is None:
        return f"这是一道未标定 rating 的 Codeforces 题，标签集中在 {tag_text}，更适合作为补充训练和题型归档。"
    if rating < 1400:
        return f"这题 rating {rating}，属于基础到中低强度训练题，适合做模板熟悉和边界处理演练。"
    if rating < 1800:
        return f"这题 rating {rating}，已经进入典型竞赛题强度，适合做题型识别和标准套路提速。"
    if rating < 2200:
        return f"这题 rating {rating}，属于比赛里的中高难核心题，常用于区分是否真正掌握 {tag_text}。"
    return f"这题 rating {rating}，已经是高强度对抗题，通常需要稳定题型识别、严谨复杂度论证和实现细节控制。"


def algorithm_hint(tags: List[str]) -> str:
    parts: List[str] = []
    for tag in tags[:5]:
        hint = TAG_HINTS.get(tag)
        if hint:
            parts.append(f"`{tag}`: {hint}")
    if not parts:
        return "标签信息不足，建议先回到题目链接判断数据范围、操作类型和是否存在单调性。"
    return "；".join(parts)


def route_skills(tags: List[str]) -> str:
    skills: List[str] = []
    seen = set()
    for tag in tags:
        for skill in TAG_TO_SKILLS.get(tag, []):
            if skill not in seen:
                seen.add(skill)
                skills.append(skill)
    if not skills:
        skills = ["cj-ice-router", "cj-algo-patterns", "cj-language-core"]
    return "、".join(f"`{name}`" for name in skills)


def render_doc(row: Dict) -> str:
    title = md_cell(row.get("name", ""))
    problem_id = md_cell(row.get("id", ""))
    rating = row.get("rating")
    rating_text = str(rating) if rating is not None else "Unrated"
    points = row.get("points")
    points_text = str(points) if points is not None else "-"
    tags = row.get("tags") or []
    tags_text = "、".join(f"`{md_cell(tag)}`" for tag in tags) if tags else "无"
    hint_text = algorithm_hint(tags)
    route_text = route_skills(tags)
    solved_count = row.get("solved_count", 0)
    return "\n".join(
        [
            f"# {problem_id} {title}",
            "",
            "## 基本信息",
            "",
            f"| 字段 | 内容 |",
            f"|---|---|",
            f"| 来源 | Codeforces |",
            f"| 编号 | {problem_id} |",
            f"| Contest | {row.get('contest_id', '')} |",
            f"| Index | {md_cell(row.get('index', ''))} |",
            f"| Rating | {rating_text} |",
            f"| Points | {points_text} |",
            f"| 题型标签 | {tags_text} |",
            f"| 通过次数 | {solved_count} |",
            "",
            "## 训练定位",
            "",
            training_position(row),
            "",
            "## 算法切入提示",
            "",
            hint_text,
            "",
            "## 仓颉实现路由建议",
            "",
            f"实现这题时，优先联动 {route_text}。",
            "",
            "## 参考入口",
            "",
            f"- 官方题面：[problem]({row.get('problem_url', '')})",
            f"- 提交列表：[status]({row.get('answer_index_url', '')})",
            f"- OK 提交：[accepted]({row.get('ok_submissions_url', '')})",
            f"- 题解检索：[tutorial]({row.get('tutorial_search_url', '')})",
            "",
            "## 本地补充位",
            "",
            "这里预留给后续补写的解题思路、仓颉实现、边界样例和错题复盘。",
            "",
        ]
    ) + "\n"


def build_index(rows: List[Dict], out_dir: Path, title: str) -> None:
    rating_count: Dict[str, int] = {}
    for row in rows:
        bucket = rating_bucket(row.get("rating"))
        rating_count[bucket] = rating_count.get(bucket, 0) + 1

    lines: List[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"总文档数：{len(rows)}")
    lines.append("")
    lines.append("| 目录 | 数量 |")
    lines.append("|---|---:|")
    for bucket in sorted(rating_count):
        lines.append(f"| `{bucket}` | {rating_count[bucket]} |")
    lines.append("")
    lines.append("每个题目已经展开为独立文档，可按 rating 目录直接浏览。")
    lines.append("")
    (out_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Materialize Codeforces problems into one-doc-per-problem collection.")
    parser.add_argument("--source-jsonl", default="../references/problems_all_full.jsonl")
    parser.add_argument("--out-dir", default="../references/problem-docs-all")
    parser.add_argument("--min-rating", type=int, default=-1)
    parser.add_argument("--max-rating", type=int, default=10**9)
    parser.add_argument("--title", default="Codeforces 实体题库文档集")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    source_jsonl = (base / args.source_jsonl).resolve()
    out_dir = (base / args.out_dir).resolve()

    rows = read_jsonl(source_jsonl)
    filtered: List[Dict] = []
    for row in rows:
        rating = row.get("rating")
        effective = rating if rating is not None else -1
        if effective < args.min_rating or effective > args.max_rating:
            continue
        filtered.append(row)

    if args.clean and out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for row in filtered:
        bucket = rating_bucket(row.get("rating"))
        bucket_dir = out_dir / bucket
        bucket_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{row.get('id', 'unknown')}.md"
        (bucket_dir / filename).write_text(render_doc(row), encoding="utf-8")

    build_index(filtered, out_dir, args.title)
    print(f"materialized {len(filtered)} docs -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
