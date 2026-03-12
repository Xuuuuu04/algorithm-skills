#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ROOT_DIR="$(cd "${SKILL_DIR}/../../.." && pwd)"
SKILLS_DIR="${ROOT_DIR}/.claude/skills"
OUT_DIR="${SKILL_DIR}/references/generated"
RECOVERED_DIR="${SKILL_DIR}/references/docs/recovered"

# Fetch missing pages for user_manual (docs in cj-language-core)
LANG_CORE="${SKILLS_DIR}/cj-language-core/references/docs/user_manual"
python3 "${SKILL_DIR}/scripts/fetch_missing_pages.py" \
  --failed-urls-file "${LANG_CORE}/_failed_urls.json" \
  --output-root "${RECOVERED_DIR}/user_manual" \
  --timeout 20 --overwrite --insecure

# Fetch missing pages for libs (metadata in cj-doc-indexer)
python3 "${SKILL_DIR}/scripts/fetch_missing_pages.py" \
  --failed-urls-file "${SKILL_DIR}/references/docs/_failed_urls.json" \
  --output-root "${RECOVERED_DIR}/libs" \
  --timeout 20 --overwrite --insecure

# Build index from consolidated docs set owned by cj-doc-indexer
python3 "${SKILL_DIR}/scripts/build_index.py" \
  --docs-root "${SKILL_DIR}/references/docs" \
  --out-dir "${OUT_DIR}" \
  --include-raw --include-clean

echo "Rebuild complete: ${OUT_DIR}"
