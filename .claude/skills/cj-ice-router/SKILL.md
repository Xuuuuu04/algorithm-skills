---
name: cj-ice-router
description: 仓颉ICE算法题路由技能。用于识别题型、判断复杂度上界、选择技能组合与最小上下文加载路径，并给出推荐的速度模式与回答模式；不负责最终输出格式。
---

# CJ ICE Router

## 目标
在 30 秒内完成“题型识别 → 技能调用 → 回答模式建议”。

## 必读参考
- **路由矩阵**: `references/route-matrix.md` — 30 题型映射表 + 约束→复杂度表 + 决策树

## 路由三步法

### Step 1: 约束分析 (最重要)
```
n 范围 → 确定 O(?) 上界 (查 route-matrix.md §二)
```

### Step 2: 题型识别
查 route-matrix.md §一 的 30 行表，匹配题目特征。

题型大类:
- **图论**: 最短路/连通性/拓扑/MST/SCC/LCA/网络流
- **DP**: 线性/树形/区间/数位/状压/背包/LIS/LCS
- **数据结构**: 线段树/BIT/单调栈/单调队列/Trie
- **字符串**: KMP/Hash/SAM/SA/AC自动机
- **数论**: 快速幂/逆元/组合数/筛/矩阵快速幂/CRT
- **搜索**: 二分/二分答案/DFS/BFS
- **几何**: 凸包/旋转卡壳
- **博弈**: SG函数/Nim
- **贪心**: 排序+贪心/前缀和/差分
- **构造**: 贪心构造/归纳构造

### Step 3: 技能组合
| 所有题 | 算法类题 | 语法复杂题 | 集合排序密集 | 需要stdx | strict 模式 |
|--------|---------|-----------|-------------|---------|-----------|
| cj-ice-contest-protocol | cj-algo-patterns | cj-language-core | cj-std-algo-toolkit | cj-stdx-reference | cj-doc-evidence-citation |

### Step 4: 回答模式建议
- `lite`: 现场求解、代码修复、快速验证、用户只要代码
- `strict`: 题解审查、正式讲解、教学、复盘、评测

## 仓颉特有路由注意
| 需求 | 路由到 | 说明 |
|------|--------|------|
| 优先队列 | cj-std-algo-toolkit | TreeMap 模拟 |
| lower_bound | cj-std-algo-toolkit | TreeMap.forward() |
| 大整数 | cj-language-core | 自行实现 |
| 位操作 | cj-std-algo-toolkit | std.math.countOnes 等 |
| 整数溢出 | cj-std-algo-toolkit | std.overflow |
| readln 解析 | cj-language-core | Int64.parse + split |

## 输出格式
```
## 路由结果
- 题型: [具体题型]
- 约束: n=[?], 复杂度上界 O([?])
- 主算法: [算法名]
- 调用技能: [清单 + 原因]
- 速度模式: ⚡闪电 / 🎯标准 / 🔬深度
- 回答模式: lite / strict
```
