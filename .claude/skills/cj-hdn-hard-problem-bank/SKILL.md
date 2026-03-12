---
name: cj-hdn-hard-problem-bank
description: 黄大年系列高难算法题参考库。用于汇聚高难题题目链接、推理思路、易错点与仓颉实现提示；默认不参与普通自动路由，需显式调用。
disable-model-invocation: true
---

# 黄大年高难题题库 Skill

这个 Skill 用于建设黄大年系列高难题参考库。考虑到源站可能存在登录、反爬或网络限制，采用“自动抓取优先 + CSV 导入兜底”的双轨模式。

## 更新命令

```bash
python3 scripts/fetch_hdn_bank.py \
  --seed-url https://chaspark.com \
  --max-pages 200

# 若已登录并可提供 Cookie / X-CSRF-TOKEN，可直接调官方接口批量抓取
python3 scripts/fetch_hdn_bank.py \
  --use-api \
  --api-token '<X-CSRF-TOKEN>' \
  --cookie '<浏览器请求中的 Cookie>'
```

如果自动抓取不可用，先填写 `references/hdn_manual_import_template.csv`，再执行：

```bash
python3 scripts/fetch_hdn_bank.py \
  --import-csv ../references/hdn_manual_import_template.csv

# 一题一文档实体集合
python3 scripts/materialize_hdn_collection.py --clean
```

## 输出

- `references/hdn_hard_problems.jsonl`
- `references/hdn_hard_problems.md`
- `references/hdn_fetch_log.json`
- `references/problem-collection/`：一题一文档集合，并保存对应原始 JSON 快照

## 使用方式

优先自动抓取，再把条目实体化成单题文档；后续围绕“核心思路 + 易错点 + 复杂度边界”继续补写参考内容，再回到 `cj-algo-patterns` 组合仓颉模板实现。
