---
name: algo-grandmaster
description: 华为ICE仓颉算法比赛总控技能。用于高难算法题、代码优化、题解审查和复杂度优化请求，负责选择速度模式与回答模式，并编排路由到算法策略、仓颉实现、标准库、协议与证据技能；不直接承担最终答案格式或证据校验。
---

# Algo Grandmaster (ICE 总控)

## 总控职责
作为比赛入口，只负责编排，不直接堆叠细节，也不重复承担路由、协议和证据 Skill 的职责。

### 核心参考文件 (必读)
- **算法模板库**: `cj-algo-patterns/references/algorithm-templates.md` — 30+ 仓颉完整算法实现
- **路由矩阵**: `cj-ice-router/references/route-matrix.md` — 30 题型 → 技能映射
- **语法速查**: `cj-language-core/references/core-map.md` — 仓颉语法全景
- **标准库速查**: `cj-std-algo-toolkit/references/std-hotpaths.md` — API + 复杂度表
- **诊断清单**: `cj-algo-patterns/references/pattern-checklist.md` — 六步系统诊断
- **扩展库速查**: `cj-stdx-reference/references/stdx-map.md` — stdx API (按需)

## 速度模式

### ⚡ 闪电模式 (≤3 min) — 经典题、约束清晰
1. 约束 → route-matrix.md 匹配题型行
2. algorithm-templates.md 取模板
3. 微调 I/O → 提交
4. 默认配 `lite` 回答模式

### 🎯 标准模式 (3-10 min) — 大部分题目
1. cj-ice-router 题型路由
2. cj-algo-patterns 算法选型 (参考 pattern-checklist.md)
3. algorithm-templates.md 取基础实现 + 修改
4. 默认配 `strict` 回答模式

### 🔬 深度模式 (>10 min) — 非标或创新题
1. 完整走 pattern-checklist.md 六步诊断
2. 暴力基线 → 优化路径 → 最终方案
3. 详细正确性证明
4. 默认配 `strict` 回答模式

## 回答模式

### `lite`
- 用于比赛现场、代码修复、快速验证
- 只要求：思路、复杂度、仓颉实现、必要边界提示
- 证据引用按需，仅在出现非显然语法或 API 结论时启用

### `strict`
- 用于正式题解、教学、复盘、回归评测
- 调用 `cj-ice-contest-protocol` 的完整七章节协议
- 调用 `cj-doc-evidence-citation` 做最小引用集和校验

## 执行流程
```
收到题目
 ├─ 1. cj-ice-router → 题型 + 技能清单
 ├─ 2. cj-algo-patterns → 选型 + 复杂度论证
 │     (参考 pattern-checklist.md + algorithm-templates.md)
 ├─ 3. cj-language-core → 语法正确 (参考 core-map.md)
 ├─ 4. cj-std-algo-toolkit → API 确认 (参考 std-hotpaths.md)
 ├─ 5. (可选) cj-stdx-reference → 仅限需要时
 ├─ 6. cj-ice-contest-protocol → 根据 lite/strict 选择回答契约
 └─ 7. cj-doc-evidence-citation → 仅处理证据最小集和校验
```

## 质量门禁
- strict 模式缺任一章节 → 不合格
- strict 模式下无最小证据集 → 不合格
- 复杂度与代码不一致 → 不合格
- 代码含未定义符号或缺 import → 不合格
- 引用无法定位 → 标注"不确定"

## 索引依赖
- 文档索引: `cj-doc-indexer/references/generated/doc_index.jsonl`（条目数以最新重建结果为准）
- 符号索引: `cj-doc-indexer/references/generated/symbol_index.jsonl`（符号数以最新重建结果为准）
