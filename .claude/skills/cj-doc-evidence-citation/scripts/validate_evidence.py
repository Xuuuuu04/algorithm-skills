#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Set

REQUIRED_SECTIONS = [
    "思路",
    "复杂度",
    "正确性要点",
    "仓颉实现",
    "边界测试",
    "风险项",
    "证据引用",
]

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
CITATION_RE = re.compile(r"\|")


def normalize_path(value: str) -> str:
    value = value.strip()
    m = re.search(r"\]\(([^)]+)\)", value)
    if m:
        value = m.group(1).strip()
    return value


def parse_sections(text: str) -> Set[str]:
    found: Set[str] = set()
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if not m:
            continue
        title = m.group(1).strip()
        for sec in REQUIRED_SECTIONS:
            if sec in title:
                found.add(sec)
    return found


def load_doc_index(index_path: Path) -> Dict[str, Dict]:
    docs: Dict[str, Dict] = {}
    for line in index_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        path = item.get("path", "")
        if path:
            docs[path] = item
    return docs


def validate_citation_line(line: str, docs: Dict[str, Dict], strict: bool) -> Dict:
    parts = [p.strip() for p in line.split("|", 2)]
    result = {
        "line": line,
        "valid": False,
        "path": "",
        "anchor": "",
        "quote": "",
        "error": "",
    }

    if len(parts) < 3:
        result["error"] = "citation_requires_3_parts"
        return result

    path = normalize_path(parts[0])
    anchor = parts[1].strip().lstrip("#")
    quote = parts[2].strip().strip('"“”')

    result["path"] = path
    result["anchor"] = anchor
    result["quote"] = quote

    match_doc = None
    for doc_path, doc in docs.items():
        if path == doc_path or path.endswith(doc_path):
            match_doc = doc
            break

    if match_doc is None:
        result["error"] = "path_not_found_in_index"
        return result

    if strict:
        anchors = set(match_doc.get("anchors", []))
        headings = set(match_doc.get("headings", []))
        # Some crawled txt/noisy pages do not preserve heading anchors reliably.
        # In strict mode, enforce anchor matching only when the index has heading data.
        if (anchors or headings) and anchor and anchor not in anchors and anchor not in headings:
            result["error"] = "anchor_not_found"
            return result

    if strict and len(quote) < 4:
        result["error"] = "quote_too_short"
        return result

    result["valid"] = True
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate three-part evidence citations")
    parser.add_argument("--index", required=True, help="Path to doc_index.jsonl")
    parser.add_argument("--answer-file", required=True, help="Markdown answer file")
    parser.add_argument("--strict", action="store_true", help="Strict validation mode")
    args = parser.parse_args()

    index_path = Path(args.index).resolve()
    answer_path = Path(args.answer_file).resolve()

    docs = load_doc_index(index_path)
    answer_text = answer_path.read_text(encoding="utf-8", errors="ignore")

    section_found = parse_sections(answer_text)
    missing_sections = [sec for sec in REQUIRED_SECTIONS if sec not in section_found]

    citation_lines = [
        line.strip()
        for line in answer_text.splitlines()
        if line.strip() and CITATION_RE.search(line)
    ]
    citation_results = [validate_citation_line(line, docs, args.strict) for line in citation_lines]

    valid_count = sum(1 for r in citation_results if r["valid"])
    invalid_count = len(citation_results) - valid_count

    report = {
        "answer_file": str(answer_path),
        "index_file": str(index_path),
        "strict": args.strict,
        "required_sections": REQUIRED_SECTIONS,
        "found_sections": sorted(section_found),
        "missing_sections": missing_sections,
        "citation_total": len(citation_results),
        "citation_valid": valid_count,
        "citation_invalid": invalid_count,
        "citations": citation_results,
        "pass": not missing_sections and invalid_count == 0 and len(citation_results) > 0,
    }

    report_path = answer_path.with_suffix(answer_path.suffix + ".evidence_report.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report, ensure_ascii=False, indent=2))

    if report["pass"]:
        return 0
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
