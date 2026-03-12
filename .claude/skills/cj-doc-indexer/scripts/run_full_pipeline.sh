#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
INDEX_DIR="${ROOT_DIR}/.claude/skills/cj-doc-indexer/references/generated"
BENCH_DIR="${ROOT_DIR}/.claude/skills/cj-benchmark-evaluator/references"

bash "${ROOT_DIR}/.claude/skills/cj-doc-indexer/scripts/rebuild_all.sh"

python3 "${ROOT_DIR}/.claude/skills/cj-doc-evidence-citation/scripts/validate_evidence.py" \
  --index "${INDEX_DIR}/doc_index.jsonl" \
  --answer-file "${BENCH_DIR}/sample_answers/ice-001.md" \
  --strict

mkdir -p "${BENCH_DIR}/generated"
python3 "${ROOT_DIR}/.claude/skills/cj-benchmark-evaluator/scripts/run_benchmark.py" \
  --cases "${BENCH_DIR}/cases.json" \
  --rubric "${BENCH_DIR}/rubric.json" \
  --report-out "${BENCH_DIR}/generated/benchmark_report.json"

echo "Pipeline complete"
