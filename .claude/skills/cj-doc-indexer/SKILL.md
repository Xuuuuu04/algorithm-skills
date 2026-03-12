---
name: cj-doc-indexer
description: 仓颉文档资产维护与索引重建技能。仅在需要全量扫描本地文档、重建 doc/symbol 索引、修复引用基础设施或生成质量报告时使用；默认不参与普通算法题自动路由。
disable-model-invocation: true
---

# Doc Indexer

本 Skill 属于维护层，不进入普通解题上下文。

## 目标
建立并维护仓颉文档的可搜索索引，支持证据引用的实时验证。

## 输出产物
| 文件 | 路径 | 说明 |
|------|------|------|
| 文档索引 | `references/generated/doc_index.jsonl` | 文档记录（条目数以最新重建结果为准） |
| 符号索引 | `references/generated/symbol_index.jsonl` | API 符号（条目数以最新重建结果为准） |
| 质量报告 | `references/generated/quality_report.json` | 覆盖率 100% |

## 脚本

### 一键重建
```bash
bash scripts/rebuild_all.sh
```

### 单独构建索引
```bash
python3 scripts/build_index.py \
  --docs-root references/docs \
  --out-dir references/generated \
  --include-raw --include-clean
```

### 补缺抓取
```bash
python3 scripts/fetch_missing_pages.py
```

## 文档结构 (已迁入本技能)
```
references/docs/
├── std/              — 非竞赛核心标准库模块 (27 模块)
├── recovered/        — 补缺恢复的文档
├── libs_index.md     — 标准库总索引
├── CLAUDE.md         — 文档说明
└── *.json            — 爬取元数据
```

> **竞赛核心文档分布于其他技能:**
> - 用户手册 → `cj-language-core/references/docs/user_manual/`
> - 竞赛标准库 (collection/sort/math等) → `cj-std-algo-toolkit/references/docs/std/`
> - 扩展库 → `cj-stdx-reference/references/docs/libs_stdx/`

## 索引格式
### doc_index.jsonl — 每行一个文档
```json
{"path": "cj-std-algo-toolkit/references/docs/std/collection/...", "title": "ArrayList", "headings": [...]}
```

### symbol_index.jsonl — 每行一个符号
```json
{"symbol": "ArrayList.append", "type": "method", "doc_path": "..."}
```

## 维护
- 文档更新后重新运行 `rebuild_all.sh`
- 质量报告中 `coverage < 100%` 时运行补缺抓取
- 新增文档目录时需更新 `_structure.json`
