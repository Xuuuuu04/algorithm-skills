#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")


def load_json(path: Path) -> Dict:
    return json.loads(path.read_text(encoding="utf-8"))


def has_section(text: str, section: str) -> bool:
    for line in text.splitlines():
        m = HEADING_RE.match(line)
        if m and section in m.group(1):
            return True
    return False


def score_case(text: str, rubric: Dict) -> Dict:
    required_sections: List[str] = rubric["required_sections"]
    weights: Dict[str, float] = rubric["weights"]

    found_sections = [s for s in required_sections if has_section(text, s)]
    section_ratio = len(found_sections) / len(required_sections) if required_sections else 0.0
    section_score = section_ratio * weights.get("sections", 0)

    citation_lines = [line for line in text.splitlines() if "|" in line and (".md" in line or ".txt" in line)]
    citation_target = rubric.get("citation_target", 3)
    citation_ratio = min(len(citation_lines) / citation_target, 1.0) if citation_target > 0 else 1.0
    citation_score = citation_ratio * weights.get("citations", 0)

    complexity_score = 0.0
    if "O(" in text and "复杂度" in text:
        complexity_score = weights.get("complexity", 0)

    correctness_score = 0.0
    if any(token in text for token in ["正确性", "不变量", "归纳", "证明"]):
        correctness_score = weights.get("correctness", 0)

    total = section_score + citation_score + complexity_score + correctness_score
    return {
        "found_sections": found_sections,
        "missing_sections": [s for s in required_sections if s not in found_sections],
        "citation_lines": len(citation_lines),
        "score": round(total, 2),
        "breakdown": {
            "sections": round(section_score, 2),
            "citations": round(citation_score, 2),
            "complexity": round(complexity_score, 2),
            "correctness": round(correctness_score, 2),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run structural benchmark for ICE contest answer quality")
    parser.add_argument("--cases", required=True, help="Path to benchmark cases json")
    parser.add_argument("--rubric", required=True, help="Path to rubric json")
    parser.add_argument("--report-out", required=True, help="Output report json path")
    args = parser.parse_args()

    cases_path = Path(args.cases).resolve()
    rubric_path = Path(args.rubric).resolve()
    report_out = Path(args.report_out).resolve()

    cases_data = load_json(cases_path)
    rubric = load_json(rubric_path)
    workspace_root = Path.cwd().resolve()

    threshold = rubric.get("pass_threshold", 80)
    case_results = []

    for case in cases_data.get("cases", []):
        answer_file = case.get("answer_file", "")
        case_id = case.get("id", "unknown")
        item = {
            "id": case_id,
            "question": case.get("question", ""),
            "answer_file": answer_file,
            "exists": False,
            "score": 0,
            "breakdown": {},
            "missing_sections": rubric.get("required_sections", []),
        }

        if answer_file:
            answer_path = Path(answer_file)
            if not answer_path.is_absolute():
                answer_path = cases_path.parent / answer_file
            if answer_path.exists():
                text = answer_path.read_text(encoding="utf-8", errors="ignore")
                scored = score_case(text, rubric)
                item.update(scored)
                item["exists"] = True

        item["pass"] = item["score"] >= threshold
        case_results.append(item)

    avg_score = round(sum(c["score"] for c in case_results) / len(case_results), 2) if case_results else 0.0
    pass_count = sum(1 for c in case_results if c["pass"])

    def to_rel(path: Path) -> str:
        try:
            return str(path.relative_to(workspace_root))
        except Exception:
            return str(path)

    report = {
        "cases": to_rel(cases_path),
        "rubric": to_rel(rubric_path),
        "threshold": threshold,
        "summary": {
            "total_cases": len(case_results),
            "pass_count": pass_count,
            "pass_rate": round(pass_count / len(case_results), 4) if case_results else 0.0,
            "average_score": avg_score,
        },
        "results": case_results,
    }

    report_out.parent.mkdir(parents=True, exist_ok=True)
    report_out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(report["summary"], ensure_ascii=False, indent=2))
    return 0 if report["summary"]["pass_rate"] >= rubric.get("suite_pass_rate", 0.8) else 1


if __name__ == "__main__":
    raise SystemExit(main())
