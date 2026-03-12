# algorithm-skills

这是一个比赛优先的仓颉 Skill 仓库，面向 Claude、OpenCode、Copilot 等 AI 编程助手。

仓库当前包含 68 个 Skill，但主体系已经收敛为三层。第一层是 8 个算法解题核心 Skill，负责题型识别、算法选型、仓颉实现、作答协议和证据引用。第二层是 2 个维护与回归 Skill，负责文档索引重建和题解质量评测。第三层是 58 个 `cangjie-*` 通用开发参考 Skill，保留为显式调用的参考书架。

所有 Skill 统一位于 `.claude/skills/`。当前仓库已经是完整落盘的 Skill 项目，不依赖外部软链接。`cangjie-*` 现在默认不参与算法题自动路由，只在用户显式点名或算法核心层确有需要时手动调用。

项目级路由约束见 [AGENTS.md](./AGENTS.md)。技能分层见 [docs/skill-map.md](./docs/skill-map.md)，治理规则见 [docs/skill-governance.md](./docs/skill-governance.md)。

## 技能治理命令

```bash
# 生成 catalog、检索索引与 skill map
python3 scripts/skills/build_catalog.py

# 运行健康检查（严格模式）
python3 scripts/skills/check_health.py --strict

# 一键执行
make skills-all
```

## 高难数据集构建命令

```bash
# Codeforces 1800-2400 高难题库
python3 .claude/skills/cj-codeforces-1800-2400/scripts/fetch_codeforces_bank.py \
  --min-rating 1800 --max-rating 2400

# Codeforces 单题单文档实体题库
python3 .claude/skills/cj-codeforces-1800-2400/scripts/materialize_codeforces_collection.py \
  --source-jsonl ../references/problems_all_full.jsonl \
  --out-dir ../references/problem-docs-1800-2400 \
  --min-rating 1800 --max-rating 2400 --clean

# Codeforces 真实题面快照（按 Hydro -> Luogu -> Codeforces 官方镜像 三源回退，把单题文档从“题目卡片”升级成“题面正文”）
python3 .claude/skills/cj-codeforces-1800-2400/scripts/hydrate_codeforces_statements.py \
  --source-jsonl ../references/problems_1800_2400.jsonl \
  --out-dir ../references/problem-docs-1800-2400 \
  --workers 32 --timeout 12 --skip-existing

# Codeforces 全量题目 + 答案入口超大索引（推荐）
python3 .claude/skills/cj-codeforces-1800-2400/scripts/build_codeforces_full_index.py

# CangjieSIG 活跃仓库（cjc >= 1.0.0）
python3 .claude/skills/cj-cangjiesig-active-repos/scripts/fetch_cangjiesig_repos.py \
  --org cangjielanguage-sig --min-version 1.0.0 --active-days 540

# CangjieSIG 一项目一个目录实体集合
python3 .claude/skills/cj-cangjiesig-active-repos/scripts/materialize_repo_collection.py --clean

# 黄大年高难题（自动抓取；若源站受限则使用 CSV 模板导入）
python3 .claude/skills/cj-hdn-hard-problem-bank/scripts/fetch_hdn_bank.py --max-pages 80

# 黄大年一题一文档实体集合
python3 .claude/skills/cj-hdn-hard-problem-bank/scripts/materialize_hdn_collection.py --clean
```
