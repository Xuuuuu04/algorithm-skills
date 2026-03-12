#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple

HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$")
SYMBOL_RE = re.compile(
    r"^\s*(?:public\s+|protected\s+|private\s+|open\s+|sealed\s+|abstract\s+|override\s+|static\s+|mut\s+|unsafe\s+|foreign\s+)*"
    r"(class|struct|interface|enum)\s+([A-Za-z_][A-Za-z0-9_]*)"
)
FUNC_RE = re.compile(
    r"^\s*(?:public\s+|private\s+|protected\s+|open\s+|static\s+|operator\s+|foreign\s+|mut\s+|unsafe\s+)*"
    r"func\s+([A-Za-z_][A-Za-z0-9_]*)\s*\("
)
CN_FUNC_RE = re.compile(r"^\s*函数\s+func\s+([^\(\s]+)")
CN_CLASS_RE = re.compile(r"^\s*类\s+class\s+([A-Za-z_][A-Za-z0-9_]*)")
HTML_LINK_RE = re.compile(r"\.html(?:\)|\]|\s|$)")
WORD_RE = re.compile(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]")


def slugify(text: str) -> str:
    value = text.strip().lower()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^\w\u4e00-\u9fff\-\s]", "", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "section"


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def infer_domain_module(rel_path: Path) -> Tuple[str, str]:
    parts = rel_path.parts
    if not parts:
        return "unknown", "unknown"
    domain = parts[0]
    module = parts[1] if len(parts) > 1 else "root"
    return domain, module


def to_rel_display(path: Path, base: Path) -> str:
    try:
        return str(path.resolve().relative_to(base.resolve()))
    except Exception:
        return str(path)


def clean_text(text: str) -> str:
    cleaned_lines: List[str] = []
    for line in text.splitlines():
        if re.match(r"^>{4,}", line):
            continue
        line = line.replace(".html)", ".md)")
        line = line.replace(".html]", ".md]")
        line = line.replace(".html ", ".md ")
        cleaned_lines.append(line.rstrip())
    return "\n".join(cleaned_lines).strip() + "\n"


def extract_headings(text: str) -> Tuple[List[str], List[str]]:
    headings: List[str] = []
    anchors: List[str] = []
    seen: Dict[str, int] = {}
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if not match:
            continue
        heading = match.group(2).strip()
        base = slugify(heading)
        idx = seen.get(base, 0)
        seen[base] = idx + 1
        anchor = base if idx == 0 else f"{base}-{idx}"
        headings.append(heading)
        anchors.append(anchor)
    return headings, anchors


def extract_symbols(text: str, rel_path: Path, domain: str) -> List[Dict[str, str]]:
    symbols: List[Dict[str, str]] = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue

        m_symbol = SYMBOL_RE.match(stripped)
        if m_symbol:
            kind = m_symbol.group(1)
            symbol = m_symbol.group(2)
            symbols.append(
                {
                    "symbol": symbol,
                    "kind": kind,
                    "signature": stripped,
                    "path": str(rel_path),
                    "anchor": slugify(f"{kind}-{symbol}"),
                    "domain": domain,
                    "line": lineno,
                }
            )
            continue

        m_func = FUNC_RE.match(stripped)
        if m_func:
            symbol = m_func.group(1)
            symbols.append(
                {
                    "symbol": symbol,
                    "kind": "func",
                    "signature": stripped,
                    "path": str(rel_path),
                    "anchor": slugify(f"func-{symbol}"),
                    "domain": domain,
                    "line": lineno,
                }
            )
            continue

        m_cn_func = CN_FUNC_RE.match(stripped)
        if m_cn_func:
            symbol = m_cn_func.group(1)
            symbols.append(
                {
                    "symbol": symbol,
                    "kind": "func",
                    "signature": stripped,
                    "path": str(rel_path),
                    "anchor": slugify(f"func-{symbol}"),
                    "domain": domain,
                    "line": lineno,
                }
            )
            continue

        m_cn_class = CN_CLASS_RE.match(stripped)
        if m_cn_class:
            symbol = m_cn_class.group(1)
            symbols.append(
                {
                    "symbol": symbol,
                    "kind": "class",
                    "signature": stripped,
                    "path": str(rel_path),
                    "anchor": slugify(f"class-{symbol}"),
                    "domain": domain,
                    "line": lineno,
                }
            )

    # de-duplicate while preserving order
    unique: Dict[Tuple[str, str, str, int], Dict[str, str]] = {}
    for item in symbols:
        key = (item["symbol"], item["kind"], item["path"], item["line"])
        unique[key] = item
    return list(unique.values())


def normalize_source_key(value: str, docs_root: Path) -> str:
    source = value.strip()
    if not source:
        return source
    p = Path(source)
    if p.is_absolute():
        try:
            return str(p.relative_to(docs_root))
        except Exception:
            pass
    marker = "references/docs/"
    if marker in source:
        return source.split(marker, 1)[1]
    return source


def load_failed_urls(docs_root: Path) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    for failed_file in docs_root.rglob("_failed_urls.json"):
        key = to_rel_display(failed_file, docs_root)
        try:
            data = json.loads(failed_file.read_text(encoding="utf-8"))
            if isinstance(data, list):
                result[key] = [str(i) for i in data]
        except Exception:
            result[key] = []
    return result


def load_recovery_manifests(docs_root: Path) -> Dict[str, Dict]:
    result: Dict[str, Dict] = {}
    recovered_root = docs_root / "recovered"
    if not recovered_root.exists():
        return result
    for manifest in recovered_root.glob("*/fetch_manifest.json"):
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except Exception:
            continue
        source = normalize_source_key(str(data.get("failed_urls_file", "")), docs_root)
        if not source:
            continue
        items = data.get("items", [])
        ok = sum(1 for i in items if i.get("status") == "ok")
        err = sum(1 for i in items if i.get("status") == "error")
        skip = sum(1 for i in items if i.get("status") == "skipped_exists")
        result[source] = {
            "manifest": to_rel_display(manifest, docs_root),
            "fetched_at": data.get("fetched_at", ""),
            "ok": ok,
            "error": err,
            "skipped": skip,
            "total": len(items),
        }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Build searchable doc/symbol indexes for Cangjie docs")
    parser.add_argument("--docs-root", required=True, help="Root directory containing docs (e.g. .claude/skills)")
    parser.add_argument("--out-dir", required=True, help="Output directory")
    parser.add_argument("--include-raw", action="store_true", help="Include raw text hash metadata")
    parser.add_argument("--include-clean", action="store_true", help="Write cleaned copies for retrieval")
    args = parser.parse_args()

    docs_root = Path(args.docs_root).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    clean_root = out_dir / "clean_docs"
    if args.include_clean:
        clean_root.mkdir(parents=True, exist_ok=True)

    doc_files = sorted(
        [
            p
            for p in docs_root.rglob("*")
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}
        ]
    )

    doc_index_path = out_dir / "doc_index.jsonl"
    symbol_index_path = out_dir / "symbol_index.jsonl"

    domain_counts: Dict[str, int] = {}
    noisy_files: List[str] = []
    html_link_files: List[str] = []
    format_issues: List[str] = []
    all_symbols: List[Dict[str, str]] = []

    with doc_index_path.open("w", encoding="utf-8") as doc_out:
        for file_path in doc_files:
            rel_path = file_path.relative_to(docs_root)
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            cleaned = clean_text(text)
            domain, module = infer_domain_module(rel_path)

            headings, anchors = extract_headings(cleaned)
            flags: List[str] = []

            if ">>>>" in text:
                flags.append("noisy_chevrons")
                noisy_files.append(str(rel_path))
            if HTML_LINK_RE.search(text):
                flags.append("contains_html_link")
                html_link_files.append(str(rel_path))
            if file_path.suffix.lower() == ".txt":
                flags.append("txt_format")
            if not headings:
                flags.append("no_markdown_headings")
                format_issues.append(str(rel_path))

            doc_id = hashlib.sha1(str(rel_path).encode("utf-8")).hexdigest()[:16]
            raw_hash = hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()
            clean_hash = hashlib.sha256(cleaned.encode("utf-8", errors="ignore")).hexdigest()

            if args.include_clean:
                output_clean = clean_root / rel_path
                output_clean.parent.mkdir(parents=True, exist_ok=True)
                output_clean.write_text(cleaned, encoding="utf-8")

            entry = {
                "doc_id": doc_id,
                "path": str(rel_path),
                "domain": domain,
                "module": module,
                "headings": headings,
                "anchors": anchors,
                "hash": clean_hash,
                "word_count": count_words(cleaned),
                "flags": flags,
            }
            if args.include_raw:
                entry["raw_hash"] = raw_hash

            doc_out.write(json.dumps(entry, ensure_ascii=False) + "\n")
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

            all_symbols.extend(extract_symbols(cleaned, rel_path, domain))

    with symbol_index_path.open("w", encoding="utf-8") as sym_out:
        for item in all_symbols:
            sym_out.write(json.dumps(item, ensure_ascii=False) + "\n")

    failed_urls = load_failed_urls(docs_root)
    recovered = load_recovery_manifests(docs_root)
    missing_pages = {}
    for failed_file, urls in sorted(failed_urls.items()):
        missing_pages[failed_file] = {
            "urls": urls,
            "count": len(urls),
            "recovery": recovered.get(
                failed_file,
                {"manifest": "", "fetched_at": "", "ok": 0, "error": 0, "skipped": 0, "total": 0},
            ),
        }

    quality_report = {
        "coverage": {
            "expected_docs": len(doc_files),
            "indexed_docs": len(doc_files),
            "coverage_ratio": 1.0 if doc_files else 0.0,
            "by_domain": domain_counts,
        },
        "missing_pages": missing_pages,
        "noisy_files": sorted(set(noisy_files)),
        "link_issues": sorted(set(html_link_files)),
        "format_issues": sorted(set(format_issues)),
        "symbol_count": len(all_symbols),
        "generated_files": {
            "doc_index": doc_index_path.name,
            "symbol_index": symbol_index_path.name,
        },
    }
    (out_dir / "quality_report.json").write_text(
        json.dumps(quality_report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"Indexed docs: {len(doc_files)}")
    print(f"Indexed symbols: {len(all_symbols)}")
    print(f"Output: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
