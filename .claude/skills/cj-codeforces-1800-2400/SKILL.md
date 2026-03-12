---
name: cj-codeforces-1800-2400
description: Codeforces 1800-2400 分段高难题参考库。用于补充高难算法训练数据，提供题目元信息、标签映射、解题思路模板和仓颉实现提示；默认不参与普通自动路由，需显式调用。
disable-model-invocation: true
---

# Codeforces 1800-2400 题库 Skill

这个 Skill 用于维护 Codeforces 中 rating 在 1800-2400 区间的高难题参考库，目标是在比赛前建立稳定的“题型→思路→仓颉实现”映射。

## 更新命令

```bash
python3 scripts/fetch_codeforces_bank.py \
  --min-rating 1800 \
  --max-rating 2400

# 全量题目（推荐）
python3 scripts/build_codeforces_full_index.py

# 单题单文档实体题库
python3 scripts/materialize_codeforces_collection.py \
  --source-jsonl ../references/problems_all_full.jsonl \
  --out-dir ../references/problem-docs-1800-2400 \
  --min-rating 1800 \
  --max-rating 2400 \
  --clean

# 真实题面快照（Hydro -> Luogu -> Codeforces 官方镜像 三源回退）
python3 scripts/hydrate_codeforces_statements.py \
  --source-jsonl ../references/problems_1800_2400.jsonl \
  --out-dir ../references/problem-docs-1800-2400 \
  --workers 32 \
  --timeout 12 \
  --skip-existing
```

## 输出

- `references/problems_1800_2400.jsonl`：结构化题目清单
- `references/problems_1800_2400.md`：可读题目索引
- `references/problems_all_full.jsonl`：Codeforces 全量题库
- `references/problems_all_answer_index.md`：全量题目 + 答案入口超大索引
- `references/problem-docs-all/`：全量单题单文档集合
- `references/problem-docs-1800-2400/`：1800-2400 单题单文档集合
- `references/problem-docs-1800-2400/` 下额外生成题面原始 HTML 侧车文件和结构化快照侧车文件

## 使用方式

先实体化成单题文档，再执行题面快照抓取，把文档升级成真实题面正文；之后再结合 `cj-algo-patterns` 与 `cj-language-core` 完成仓颉实现。
