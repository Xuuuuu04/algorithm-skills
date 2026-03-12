---
name: cj-cangjiesig-active-repos
description: CangjieSIG 活跃仓库参考库。用于筛选活跃且支持仓颉 1.0.0+ 的官方/社区仓库，并形成可检索工程实践索引；默认不参与普通自动路由，需显式调用。
disable-model-invocation: true
---

# CangjieSIG 活跃仓库 Skill

这个 Skill 用于追踪 CangjieSIG 生态里“仍然活跃且支持仓颉 1.0.0+”的仓库，为比赛和项目阶段提供高质量实现参考。

## 更新命令

```bash
python3 scripts/fetch_cangjiesig_repos.py \
  --org cangjielanguage-sig \
  --min-version 1.0.0 \
  --active-days 540

# 全量仓库（不过滤活跃时间）
python3 scripts/fetch_cangjiesig_repos.py \
  --org cangjielanguage-sig \
  --min-version 1.0.0 \
  --active-days 0

# 一项目一个目录实体集合
python3 scripts/materialize_repo_collection.py --clean
```

## 输出

- `references/active_repos_1_0_0_plus.jsonl`
- `references/active_repos_1_0_0_plus.md`
- `references/repo-collection/`：一项目一个目录，内含仓库说明、元信息、配置快照和目录结构快照

## 使用方式

先按领域筛选仓库，再直接进入实体目录检查 README、仓库元信息、`cjpm.toml` 和根目录结构，抽取可复用的工程组织方式。
