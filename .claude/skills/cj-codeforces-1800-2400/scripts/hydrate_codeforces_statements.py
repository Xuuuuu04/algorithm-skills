#!/usr/bin/env python3
from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import shutil
import ssl
import subprocess
import urllib.error
import urllib.request
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Tuple


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


def fetch_text(url: str, timeout: int = 30) -> Optional[str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 404, 429, 500, 502, 503, 504}:
            return None
        raise
    except Exception:
        return None


def fetch_text_via_curl(url: str, timeout: int = 30) -> Optional[str]:
    try:
        proc = subprocess.run(
            ["curl", "-L", "-sS", "--max-time", str(timeout), url],
            check=False,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    if proc.returncode != 0 or not proc.stdout:
        return None
    return proc.stdout


class ProblemContentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.capture = False
        self.capture_depth = 0
        self.found = False
        self.in_pre = False
        self.in_h2 = False
        self.in_li = False
        self.parts: List[str] = []

    def _append(self, text: str) -> None:
        if not text:
            return
        self.parts.append(text)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attr_map = dict(attrs)
        if not self.capture and tag == "div" and attr_map.get("data-fragment-id") == "problem-description":
            self.capture = True
            self.capture_depth = 1
            self.found = True
            return
        if not self.capture:
            return
        self.capture_depth += 1
        if tag == "h2":
            self.in_h2 = True
            self._append("\n## ")
        elif tag == "p":
            self._append("\n")
        elif tag == "pre":
            self.in_pre = True
            self._append("\n```\n")
        elif tag == "br":
            self._append("\n")
        elif tag == "li":
            self.in_li = True
            self._append("\n- ")

    def handle_endtag(self, tag: str) -> None:
        if not self.capture:
            return
        if tag == "pre" and self.in_pre:
            self._append("\n```\n")
            self.in_pre = False
        elif tag == "h2" and self.in_h2:
            self._append("\n")
            self.in_h2 = False
        elif tag == "li" and self.in_li:
            self._append("\n")
            self.in_li = False
        elif tag in {"p", "div"} and not self.in_pre:
            self._append("\n")
        self.capture_depth -= 1
        if self.capture_depth <= 0:
            self.capture = False

    def handle_data(self, data: str) -> None:
        if not self.capture:
            return
        text = unescape(data)
        if self.in_pre:
            self._append(text)
            return
        cleaned = re.sub(r"\s+", " ", text)
        if cleaned.strip():
            self._append(cleaned)

    def result(self) -> str:
        text = "".join(self.parts)
        text = text.replace("\xa0", " ")
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n +", "\n", text)
        return text.strip() + "\n"


def extract_description(html: str) -> Optional[str]:
    parser = ProblemContentParser()
    parser.feed(html)
    if not parser.found:
        return None
    return parser.result()


def extract_hydro_meta(html: str) -> Dict[str, object]:
    title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
    page_title = unescape(title_match.group(1).strip()) if title_match else ""

    tags: List[str] = []
    for item in re.findall(r'<span class="problem__tag-item tags hasjs--hide">(.*?)</span>', html, flags=re.S):
        tag = re.sub(r"<.*?>", "", unescape(item)).strip()
        if tag:
            tags.append(tag)

    accepted = None
    accepted_match = re.search(r"已通过:\s*(\d+)", html)
    if accepted_match:
        accepted = int(accepted_match.group(1))

    attempt = None
    attempt_match = re.search(r"尝试:\s*(\d+)", html)
    if attempt_match:
        attempt = int(attempt_match.group(1))

    time_limit = None
    memory_limit = None
    tl_match = re.search(r'problem__tag-item icon icon-stopwatch">([^<]+)</span>', html)
    ml_match = re.search(r'problem__tag-item icon icon-comparison">([^<]+)</span>', html)
    if tl_match:
        time_limit = unescape(tl_match.group(1).strip())
    if ml_match:
        memory_limit = unescape(ml_match.group(1).strip())

    return {
        "page_title": page_title,
        "hydro_tags": tags,
        "hydro_accepted": accepted,
        "hydro_attempt": attempt,
        "time_limit": time_limit,
        "memory_limit": memory_limit,
    }


class HtmlSnippetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: List[str] = []
        self.in_pre = False
        self.in_li = False

    def _append(self, text: str) -> None:
        if text:
            self.parts.append(text)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if tag == "p":
            self._append("\n")
        elif tag == "br":
            self._append("\n")
        elif tag == "li":
            self.in_li = True
            self._append("\n- ")
        elif tag == "pre":
            self.in_pre = True
            self._append("\n```\n")
        elif tag == "div":
            cls = dict(attrs).get("class", "")
            if cls and "title" in cls.split():
                self._append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self.in_pre:
            self._append("\n```\n")
            self.in_pre = False
        elif tag == "li" and self.in_li:
            self._append("\n")
            self.in_li = False
        elif tag in {"p", "div"} and not self.in_pre:
            self._append("\n")

    def handle_data(self, data: str) -> None:
        text = unescape(data).replace("\xa0", " ")
        if self.in_pre:
            self._append(text)
            return
        cleaned = re.sub(r"\s+", " ", text)
        if cleaned.strip():
            self._append(cleaned)

    def result(self) -> str:
        text = "".join(self.parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n +", "\n", text)
        return text.strip()


def html_snippet_to_markdown(html: str) -> str:
    parser = HtmlSnippetParser()
    parser.feed(html)
    return parser.result()


def extract_div_by_class(html: str, class_name: str) -> Optional[str]:
    pattern = re.compile(rf'<div\b[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*>', flags=re.I)
    match = pattern.search(html)
    if not match:
        return None
    tags = re.finditer(r"</?div\b[^>]*>", html[match.start() :], flags=re.I)
    depth = 0
    end_index = None
    for tag_match in tags:
        token = tag_match.group(0)
        if token.startswith("</"):
            depth -= 1
            if depth == 0:
                end_index = match.start() + tag_match.end()
                break
        else:
            depth += 1
    if end_index is None:
        return None
    return html[match.start() : end_index]


def extract_all_divs_by_class(html: str, class_name: str) -> List[str]:
    pattern = re.compile(rf'<div\b[^>]*class="[^"]*\b{re.escape(class_name)}\b[^"]*"[^>]*>', flags=re.I)
    blocks: List[str] = []
    offset = 0
    while True:
        match = pattern.search(html, offset)
        if not match:
            break
        block = extract_div_by_class(html[match.start() :], class_name)
        if not block:
            break
        blocks.append(block)
        offset = match.start() + len(block)
    return blocks


def extract_codeforces_mirror_statement(html: str) -> Optional[str]:
    root = extract_div_by_class(html, "problem-statement")
    if not root:
        return None

    desc_match = re.search(r"</div></div><div>(.*?)</div><div class=\"input-specification\">", root, flags=re.S)
    input_block = extract_div_by_class(root, "input-specification")
    output_block = extract_div_by_class(root, "output-specification")
    samples_block = extract_div_by_class(root, "sample-tests")
    note_block = extract_div_by_class(root, "note")

    parts: List[str] = []
    if desc_match:
        desc = html_snippet_to_markdown(desc_match.group(1))
        if desc:
            parts.extend(["## Description", "", desc, ""])
    if input_block:
        input_text = html_snippet_to_markdown(input_block)
        input_text = re.sub(r"^Входные данные\s*", "", input_text)
        if input_text:
            parts.extend(["## Input", "", input_text, ""])
    if output_block:
        output_text = html_snippet_to_markdown(output_block)
        output_text = re.sub(r"^Выходные данные\s*", "", output_text)
        if output_text:
            parts.extend(["## Output", "", output_text, ""])
    if samples_block:
        parts.extend(["## Samples", ""])
        inputs = extract_all_divs_by_class(samples_block, "input")
        outputs = extract_all_divs_by_class(samples_block, "output")
        sample_count = min(len(inputs), len(outputs))
        for idx in range(sample_count):
            in_match = re.search(r"<pre>(.*?)</pre>", inputs[idx], flags=re.S | re.I)
            out_match = re.search(r"<pre>(.*?)</pre>", outputs[idx], flags=re.S | re.I)
            if not in_match or not out_match:
                continue
            sample_in = html_snippet_to_markdown(in_match.group(1))
            sample_out = html_snippet_to_markdown(out_match.group(1))
            parts.extend(
                [
                    f"### Sample {idx + 1}",
                    "",
                    "Input",
                    "```",
                    sample_in,
                    "```",
                    "",
                    "Output",
                    "```",
                    sample_out,
                    "```",
                    "",
                ]
            )
    if note_block:
        note_text = html_snippet_to_markdown(note_block)
        note_text = re.sub(r"^Примечание\s*", "", note_text)
        if note_text:
            parts.extend(["## Note", "", note_text, ""])

    if not parts:
        return None
    return "\n".join(parts).strip() + "\n"


def extract_codeforces_mirror_meta(html: str) -> Dict[str, object]:
    title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
    page_title = unescape(title_match.group(1).strip()) if title_match else ""
    time_match = re.search(r'<div class="time-limit"><div class="property-title">.*?</div>(.*?)</div>', html, flags=re.S)
    memory_match = re.search(r'<div class="memory-limit"><div class="property-title">.*?</div>(.*?)</div>', html, flags=re.S)
    return {
        "page_title": page_title,
        "mirror_tags": [],
        "mirror_accepted": None,
        "mirror_attempt": None,
        "time_limit": html_snippet_to_markdown(time_match.group(1)) if time_match else None,
        "memory_limit": html_snippet_to_markdown(memory_match.group(1)) if memory_match else None,
    }


def extract_luogu_context(html: str) -> Optional[Dict[str, object]]:
    match = re.search(
        r'<script id="lentille-context" type="application/json">(.*?)</script>',
        html,
        flags=re.I | re.S,
    )
    if not match:
        return None
    try:
        return json.loads(unescape(match.group(1)))
    except Exception:
        return None


def normalize_block(text: Optional[str]) -> str:
    if not text:
        return ""
    value = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    return value


def render_luogu_statement(problem: Dict[str, object]) -> Optional[str]:
    translations = problem.get("translations") or {}
    preferred = None
    if isinstance(translations, dict):
        preferred = translations.get("zh-CN") or translations.get("en")
    content = preferred or problem.get("contenu") or problem.get("content") or {}
    if not isinstance(content, dict):
        return None

    description = normalize_block(content.get("description"))
    format_i = normalize_block(content.get("formatI"))
    format_o = normalize_block(content.get("formatO"))
    hint = normalize_block(content.get("hint"))
    samples = problem.get("samples") or []

    if not any([description, format_i, format_o, hint, samples]):
        return None

    parts: List[str] = []
    if description:
        parts.extend(["## Description", "", description, ""])
    if format_i:
        parts.extend(["## Input", "", format_i, ""])
    if format_o:
        parts.extend(["## Output", "", format_o, ""])
    if samples:
        parts.extend(["## Samples", ""])
        for idx, sample in enumerate(samples, start=1):
            if not isinstance(sample, list) or len(sample) < 2:
                continue
            sample_in = normalize_block(sample[0])
            sample_out = normalize_block(sample[1])
            parts.extend(
                [
                    f"### Sample {idx}",
                    "",
                    "Input",
                    "```",
                    sample_in,
                    "```",
                    "",
                    "Output",
                    "```",
                    sample_out,
                    "```",
                    "",
                ]
            )
    if hint:
        parts.extend(["## Note", "", hint, ""])
    return "\n".join(parts).strip() + "\n"


def extract_luogu_meta(html: str, problem: Dict[str, object]) -> Dict[str, object]:
    title_match = re.search(r"<title>(.*?)</title>", html, flags=re.I | re.S)
    page_title = unescape(title_match.group(1).strip()) if title_match else ""

    limits = problem.get("limits") or {}
    time_limit = None
    memory_limit = None
    if isinstance(limits, dict):
        time_list = limits.get("time") or []
        memory_list = limits.get("memory") or []
        if isinstance(time_list, list) and time_list:
            time_limit = f"{time_list[0]} ms"
        if isinstance(memory_list, list) and memory_list:
            memory_limit = f"{memory_list[0]} KB"

    return {
        "page_title": page_title,
        "mirror_tags": [],
        "mirror_accepted": problem.get("totalAccepted"),
        "mirror_attempt": problem.get("totalSubmit"),
        "time_limit": time_limit,
        "memory_limit": memory_limit,
    }


def md_cell(value: object) -> str:
    text = str(value) if value is not None else ""
    return text.replace("|", "\\|").strip()


def dash_if_missing(value: object) -> object:
    if value is None:
        return "-"
    return value


def render_doc(
    row: Dict,
    statement: str,
    mirror_meta: Dict[str, object],
    mirror_name: str,
    mirror_url: str,
) -> str:
    rating = row.get("rating")
    rating_text = str(rating) if rating is not None else "Unrated"
    points = row.get("points")
    points_text = "-" if points is None else str(points)
    tags = row.get("tags") or []
    tags_text = "、".join(f"`{md_cell(tag)}`" for tag in tags) if tags else "无"
    mirror_tags = mirror_meta.get("mirror_tags") or []
    mirror_tags_text = "、".join(f"`{md_cell(tag)}`" for tag in mirror_tags) if mirror_tags else "无"
    problem_url = row.get("problem_url") or row.get("url") or ""
    answer_url = row.get("answer_index_url") or ""
    return "\n".join(
        [
            f"# {md_cell(row.get('id', ''))} {md_cell(row.get('name', ''))}",
            "",
            "## 题面快照",
            "",
            statement.strip(),
            "",
            "## 元信息",
            "",
            "| 字段 | 内容 |",
            "|---|---|",
            f"| 来源 | Codeforces / {md_cell(mirror_name)} |",
            f"| 编号 | {md_cell(row.get('id', ''))} |",
            f"| Contest | {row.get('contest_id', '')} |",
            f"| Index | {md_cell(row.get('index', ''))} |",
            f"| Rating | {rating_text} |",
            f"| Points | {md_cell(points_text)} |",
            f"| Codeforces 标签 | {tags_text} |",
            f"| 镜像标签 | {mirror_tags_text} |",
            f"| Codeforces 通过次数 | {row.get('solved_count', 0)} |",
            f"| 镜像尝试 / 通过 | {md_cell(dash_if_missing(mirror_meta.get('mirror_attempt'))) } / {md_cell(dash_if_missing(mirror_meta.get('mirror_accepted')))} |",
            f"| 时限 | {md_cell(dash_if_missing(mirror_meta.get('time_limit'))) } |",
            f"| 内存限制 | {md_cell(dash_if_missing(mirror_meta.get('memory_limit')))} |",
            "",
            "## 远端入口",
            "",
            f"- Codeforces 题面：[problem]({problem_url})",
            f"- Codeforces 提交列表：[status]({answer_url})",
            f"- {mirror_name}：[mirror]({mirror_url})",
            "",
            "## 本地补充位",
            "",
            "这里继续补写解题思路、仓颉实现、边界样例和错题复盘。",
            "",
        ]
    ) + "\n"


def hydrate_from_hydro(row: Dict, timeout: int) -> Optional[Tuple[str, str, Dict[str, object], str, str]]:
    hydro_url = f"https://hydro.ac/p/codeforces-P{row.get('contest_id')}{row.get('index')}"
    html = fetch_text(hydro_url, timeout=timeout)
    if not html:
        return None
    statement = extract_description(html)
    if not statement:
        return None
    hydro_meta = extract_hydro_meta(html)
    mirror_meta = {
        "page_title": hydro_meta.get("page_title", ""),
        "mirror_tags": hydro_meta.get("hydro_tags", []),
        "mirror_accepted": hydro_meta.get("hydro_accepted"),
        "mirror_attempt": hydro_meta.get("hydro_attempt"),
        "time_limit": hydro_meta.get("time_limit"),
        "memory_limit": hydro_meta.get("memory_limit"),
    }
    return statement, html, mirror_meta, "Hydro 镜像", hydro_url


def hydrate_from_luogu(row: Dict, timeout: int) -> Optional[Tuple[str, str, Dict[str, object], str, str]]:
    luogu_url = f"https://www.luogu.com.cn/problem/CF{row.get('contest_id')}{row.get('index')}"
    html = fetch_text_via_curl(luogu_url, timeout=timeout)
    if not html:
        return None
    context = extract_luogu_context(html)
    if not context:
        return None
    data = context.get("data") or {}
    if not isinstance(data, dict):
        return None
    problem = data.get("problem") or {}
    if not isinstance(problem, dict):
        return None
    statement = render_luogu_statement(problem)
    if not statement:
        return None
    mirror_meta = extract_luogu_meta(html, problem)
    return statement, html, mirror_meta, "Luogu 镜像", luogu_url


def hydrate_from_codeforces_mirror(row: Dict, timeout: int) -> Optional[Tuple[str, str, Dict[str, object], str, str]]:
    mirror_url = f"https://mirror.codeforces.com/problemset/problem/{row.get('contest_id')}/{row.get('index')}"
    html = fetch_text_via_curl(mirror_url, timeout=timeout)
    if not html:
        return None
    statement = extract_codeforces_mirror_statement(html)
    if not statement:
        return None
    mirror_meta = extract_codeforces_mirror_meta(html)
    return statement, html, mirror_meta, "Codeforces 官方镜像", mirror_url


def hydrate_one(row: Dict, out_dir: Path, timeout: int) -> Tuple[str, bool, str]:
    bucket_dir = out_dir / rating_bucket(row.get("rating"))
    bucket_dir.mkdir(parents=True, exist_ok=True)
    doc_path = bucket_dir / f"{row.get('id', 'unknown')}.md"
    raw_path = bucket_dir / f"{row.get('id', 'unknown')}.source.html"
    meta_path = bucket_dir / f"{row.get('id', 'unknown')}.snapshot.json"

    payload = hydrate_from_hydro(row, timeout)
    status = "ok_hydro"
    if payload is None:
        payload = hydrate_from_luogu(row, timeout)
        status = "ok_luogu"
    if payload is None:
        payload = hydrate_from_codeforces_mirror(row, timeout)
        status = "ok_cf_mirror"
    if payload is None:
        return str(doc_path), False, "fetch_failed_all_sources"

    statement, html, mirror_meta, mirror_name, mirror_url = payload
    doc_path.write_text(render_doc(row, statement, mirror_meta, mirror_name, mirror_url), encoding="utf-8")
    raw_path.write_text(html, encoding="utf-8")
    meta = dict(row)
    meta["mirror_url"] = mirror_url
    meta["mirror_name"] = mirror_name
    meta["mirror_meta"] = mirror_meta
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return str(doc_path), True, status


def main() -> int:
    parser = argparse.ArgumentParser(description="Hydrate Codeforces docs with actual statement snapshots from HydroOJ.")
    parser.add_argument("--source-jsonl", default="../references/problems_all_full.jsonl")
    parser.add_argument("--out-dir", default="../references/problem-docs-all")
    parser.add_argument("--min-rating", type=int, default=-1)
    parser.add_argument("--max-rating", type=int, default=10**9)
    parser.add_argument("--only-id", action="append", default=[])
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--clean-raw", action="store_true")
    parser.add_argument("--skip-existing", action="store_true")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent
    source_jsonl = (base / args.source_jsonl).resolve()
    out_dir = (base / args.out_dir).resolve()
    rows = read_jsonl(source_jsonl)

    if args.clean_raw and out_dir.exists():
        for path in out_dir.rglob("*.source.html"):
            path.unlink()
        for path in out_dir.rglob("*.snapshot.json"):
            path.unlink()

    only_ids = set(args.only_id or [])
    filtered: List[Dict] = []
    for row in rows:
        rating = row.get("rating")
        effective = rating if rating is not None else -1
        bucket_dir = out_dir / rating_bucket(row.get("rating"))
        doc_path = bucket_dir / f"{row.get('id', 'unknown')}.md"
        raw_path = bucket_dir / f"{row.get('id', 'unknown')}.source.html"
        if only_ids and row.get("id") not in only_ids:
            continue
        if effective < args.min_rating or effective > args.max_rating:
            continue
        if args.skip_existing and doc_path.exists() and raw_path.exists():
            continue
        filtered.append(row)
        if args.limit > 0 and len(filtered) >= args.limit:
            break

    ok_count = 0
    fail_count = 0
    status_counter: Dict[str, int] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [executor.submit(hydrate_one, row, out_dir, args.timeout) for row in filtered]
        for future in concurrent.futures.as_completed(futures):
            _, ok, status = future.result()
            status_counter[status] = status_counter.get(status, 0) + 1
            if ok:
                ok_count += 1
            else:
                fail_count += 1

    print(f"hydrated={ok_count} failed={fail_count} out_dir={out_dir}")
    print(json.dumps(status_counter, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
