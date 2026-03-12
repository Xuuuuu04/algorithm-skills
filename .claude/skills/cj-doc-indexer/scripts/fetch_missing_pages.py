#!/usr/bin/env python3
import argparse
import json
import re
import ssl
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def derive_rel_path(url: str, idx: int) -> str:
    parsed = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed.query)
    source = query.get("url", [""])[0]
    source = urllib.parse.unquote(source)
    source = source.lstrip("/")
    source = source.split("#", 1)[0]
    source = source or f"unknown/{idx:03d}.html"

    if source.endswith("/"):
        source += "index.html"

    # Keep html extension because official docs may not expose markdown endpoint.
    if not re.search(r"\.[A-Za-z0-9]+$", source):
        source += ".html"

    return source


def fetch_url(url: str, timeout: int, insecure: bool) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; CangjieSkillIndexer/1.0)",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    context = ssl._create_unverified_context() if insecure else None
    with urllib.request.urlopen(req, timeout=timeout, context=context) as response:
        return response.read()


def extract_iframe_url(html_text: str) -> str:
    match = re.search(r'<iframe[^>]+id="inlineFrameDocs"[^>]+src="([^"]+)"', html_text)
    if not match:
        return ""
    return match.group(1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch and archive pages listed in *_failed_urls.json")
    parser.add_argument("--failed-urls-file", required=True, help="Path to _failed_urls.json")
    parser.add_argument("--output-root", required=True, help="Directory for recovered pages")
    parser.add_argument("--timeout", type=int, default=20, help="HTTP timeout seconds")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Skip TLS certificate verification for environments without root CAs",
    )
    args = parser.parse_args()

    failed_file = Path(args.failed_urls_file).resolve()
    output_root = Path(args.output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    urls = json.loads(failed_file.read_text(encoding="utf-8"))
    if not isinstance(urls, list):
        raise ValueError("failed_urls_file must be a JSON list")

    try:
        failed_display = str(failed_file.relative_to(output_root.parents[1]))
    except Exception:
        failed_display = failed_file.name

    manifest = {
        "failed_urls_file": failed_display,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "items": [],
    }

    for idx, raw_url in enumerate(urls, start=1):
        url = str(raw_url)
        rel = derive_rel_path(url, idx)
        out_path = output_root / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)

        if out_path.exists() and not args.overwrite:
            manifest["items"].append(
                {
                    "url": url,
                    "path": str(out_path.relative_to(output_root)),
                    "status": "skipped_exists",
                }
            )
            continue

        item = {
            "url": url,
            "path": str(out_path.relative_to(output_root)),
            "status": "unknown",
        }
        try:
            body = fetch_url(url, args.timeout, args.insecure)
            text = body.decode("utf-8", errors="ignore")
            out_path.write_text(text, encoding="utf-8")

            iframe_url = extract_iframe_url(text)
            item["status"] = "ok"
            item["bytes"] = len(body)
            item["iframe_url"] = iframe_url
            item["saved_at"] = datetime.now(timezone.utc).isoformat()
        except Exception as exc:
            item["status"] = "error"
            item["error"] = str(exc)

        manifest["items"].append(item)

    manifest_path = output_root / "fetch_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    ok_count = sum(1 for i in manifest["items"] if i.get("status") == "ok")
    err_count = sum(1 for i in manifest["items"] if i.get("status") == "error")
    skip_count = sum(1 for i in manifest["items"] if i.get("status") == "skipped_exists")

    print(f"Fetched: {ok_count}, errors: {err_count}, skipped: {skip_count}")
    print(f"Manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
