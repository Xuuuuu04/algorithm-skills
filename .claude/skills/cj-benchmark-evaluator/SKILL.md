---
name: cj-benchmark-evaluator
description: 仓颉算法答案回归与评分技能。仅在批量评估答案模板合规、引用覆盖、复杂度表达和正确性说明，并生成量化回归报告时使用；默认不参与普通算法题自动路由。
disable-model-invocation: true
---

# Benchmark Evaluator

本 Skill 属于维护与回归层，不用于现场解题。

## 输入
| 文件 | 路径 | 说明 |
|------|------|------|
| 测试用例 | `references/cases.json` | 20 种题型 (ice-001 ~ ice-020) |
| 评分标准 | `references/rubric.json` | 评分维度与权重 |

## 输出
| 文件 | 路径 | 说明 |
|------|------|------|
| 评测报告 | `references/generated/benchmark_report.json` | 量化评分 |

## 运行
```bash
python3 scripts/run_benchmark.py \
  --cases references/cases.json \
  --rubric references/rubric.json \
  --report-out references/generated/benchmark_report.json
```

## 评估维度 (6 项)

### 1. 章节完整度 (25%)
- 7 个章节是否全部存在
- 每章是否有实质内容 (非占位符)

### 2. 复杂度表达 (20%)
- 时间复杂度是否准确
- 空间复杂度是否标注
- 变量定义是否清晰
- 论证是否与代码一致

### 3. 正确性要点 (20%)
- 是否有形式化论证 (不变量/归纳/反证)
- 是否仅为直觉描述 (扣分)

### 4. 代码质量 (15%)
- 可编译性 (含所有 import)
- 命名清晰度
- 是否使用正确的仓颉语法
- I/O 格式是否正确

### 5. 边界测试 (10%)
- 测试用例数量 ≥ 5
- 是否覆盖: 最小/最大/全同/负数/退化

### 6. 证据引用 (10%)
- 引用数量 ≥ 2
- 格式正确: `path | anchor | "quote"`
- 路径可验证

## 20 题型覆盖 (cases.json)

| ID | 题型 | 核心算法 |
|----|------|---------|
| ice-001 | 最短路 | Dijkstra |
| ice-002 | 树形 DP | 换根/子树统计 |
| ice-003 | 区间 DP | 石子合并类 |
| ice-004 | 字符串自动机 | AC自动机/SAM |
| ice-005 | 可持久化数据结构 | 主席树 |
| ice-006 | 二分答案 | 二分 + check |
| ice-007 | DSU 离线 | 并查集 + 离线 |
| ice-008 | 数位 DP | 数字位处理 |
| ice-009 | 最小割 | 最大流=最小割 |
| ice-010 | 树链剖分 | HLD + 线段树 |
| ice-011 | 莫队 | 离线区间查询 |
| ice-012 | 凸包 | 计算几何 |
| ice-013 | 矩阵快速幂 | 线性递推加速 |
| ice-014 | 大整数 | 高精度运算 |
| ice-015 | 状压 DP | n≤20 |
| ice-016 | SAM/SA | 后缀结构 |
| ice-017 | 博弈 SG | 游戏论 |
| ice-018 | 网络流 | Dinic |
| ice-019 | 随机化 | 随机算法 |
| ice-020 | 复杂实现 | 多模块组合 |

## 评测流程
1. 对每个 case 生成答案 (按 cj-ice-contest-protocol)
2. 按 6 维度打分
3. 输出加权总分
4. 标记不合格项
5. 回归对比历史分数
