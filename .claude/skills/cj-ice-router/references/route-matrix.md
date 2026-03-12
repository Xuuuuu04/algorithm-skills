# 路由矩阵 (Route Matrix)

> **用途**: 题型识别后快速选定技能组合，避免无关上下文干扰。

---

## 一、题型 → 技能路由

| # | 题型特征 | 主要技能 | 追加技能 | 首选模板 |
|---|---------|----------|----------|----------|
| 1 | 最短路 (Dijkstra/SPFA/Floyd) | cj-algo-patterns | cj-std-algo-toolkit | Dijkstra/BellmanFord/Floyd |
| 2 | 连通性 / 并查集 | cj-algo-patterns | cj-std-algo-toolkit | UnionFind |
| 3 | 拓扑排序 / DAG | cj-algo-patterns | cj-std-algo-toolkit | TopoSort |
| 4 | 最小生成树 | cj-algo-patterns | cj-std-algo-toolkit | Kruskal |
| 5 | 强连通分量 / 缩点 | cj-algo-patterns | — | Tarjan SCC |
| 6 | LCA / 树上查询 | cj-algo-patterns | — | LCA倍增 |
| 7 | 树形 DP | cj-algo-patterns | cj-language-core | 树形DP框架 |
| 8 | 线性 DP / 背包 | cj-algo-patterns | — | 01背包/完全背包 |
| 9 | 区间 DP | cj-algo-patterns | — | 区间DP框架 |
| 10 | 数位 DP | cj-algo-patterns | cj-language-core | 数位DP框架 |
| 11 | 状态压缩 DP | cj-algo-patterns | — | 状压DP框架 |
| 12 | LIS / LCS | cj-algo-patterns | cj-std-algo-toolkit | LIS O(nlogn) |
| 13 | 线段树 / 树状数组 | cj-algo-patterns | cj-language-core | SegTree/BIT |
| 14 | 单调栈 / 单调队列 | cj-algo-patterns | cj-std-algo-toolkit | 模板 |
| 15 | 字典树 (Trie) | cj-algo-patterns | cj-language-core | Trie |
| 16 | KMP / 字符串哈希 | cj-algo-patterns | — | KMP/StringHash |
| 17 | 后缀自动机 / 后缀数组 | cj-algo-patterns | cj-language-core | 自行实现 |
| 18 | 数论 (GCD/快速幂/素数筛) | cj-algo-patterns | cj-std-algo-toolkit | 数论模板集 |
| 19 | 组合数学 / 逆元 | cj-algo-patterns | cj-std-algo-toolkit | Comb类 |
| 20 | 矩阵快速幂 | cj-algo-patterns | — | matPow |
| 21 | 二分答案 / 二分搜索 | cj-algo-patterns | — | 二分框架 |
| 22 | 贪心 + 排序 | cj-algo-patterns | cj-std-algo-toolkit | sort + 贪心 |
| 23 | 前缀和 / 差分 | cj-algo-patterns | — | prefixSum/diff |
| 24 | 计算几何 (凸包等) | cj-algo-patterns | — | convexHull |
| 25 | 博弈论 (SG函数) | cj-algo-patterns | — | SG模板 |
| 26 | 网络流 / 最小割 | cj-algo-patterns | cj-language-core | 自行实现 |
| 27 | 大量集合/排序操作 | cj-std-algo-toolkit | cj-algo-patterns | std API |
| 28 | 泛型/约束/Option 问题 | cj-language-core | cj-doc-evidence-citation | 语法速查 |
| 29 | HTTP/TLS/JSON/编码 | cj-stdx-reference | cj-language-core | 按需 |
| 30 | 复杂实现/调试 | cj-language-core | cj-algo-patterns | 分步调试 |

**所有题型最终提交阶段永远追加**: `cj-ice-contest-protocol` + `cj-doc-evidence-citation`

---

## 二、输入规模 → 复杂度判断

| n 范围 | 可接受复杂度 | 典型算法 |
|--------|-------------|----------|
| n ≤ 10 | O(n!) | 全排列、暴搜 |
| n ≤ 20 | O(2^n * n) | 状态压缩 DP、折半搜索 |
| n ≤ 500 | O(n³) | Floyd、区间 DP |
| n ≤ 5000 | O(n²) | 朴素 DP、O(n²) 排序 |
| n ≤ 10^5 | O(n log n) | 排序、线段树、二分 |
| n ≤ 10^6 | O(n) 或 O(n log n) | 线性扫描、桶排序 |
| n ≤ 10^7 | O(n) | 线性筛、前缀和 |
| n ≤ 10^9 | O(√n) 或 O(log n) | 数论分块、二分、矩阵快速幂 |
| n ≤ 10^18 | O(log n) | 快速幂、矩阵快速幂 |

---

## 三、算法选型决策树

```
输入题目
│
├─ 约束分析 → 确定 O(?) 上界
│
├─ 目标类型?
│  ├─ 最值 → DP / 贪心 / 二分答案
│  ├─ 计数 → DP / 组合数学 / 容斥
│  ├─ 判定 → 二分 / 图连通 / 博弈SG
│  └─ 构造 → 贪心 / 构造性证明
│
├─ 数据关系?
│  ├─ 线性序列 → 前缀和 / 单调栈 / DP
│  ├─ 树 → 树形DP / LCA / DFS序 + 线段树
│  ├─ 一般图 → BFS/DFS / 最短路 / SCC / 网络流
│  ├─ 区间 → 线段树 / 树状数组 / 莫队
│  └─ 字符串 → KMP / Trie / SAM / 哈希
│
├─ 优化手段?
│  ├─ 可离线? → 莫队 / 离线并查集
│  ├─ 单调性? → 单调栈/队列 / 二分
│  ├─ 可分治? → CDQ分治 / 点分治
│  └─ 可数据结构优化? → 线段树 / BIT / 平衡树
│
└─ 输出方案
   ├─ 主方案 + 复杂度论证
   └─ 备选方案 (主方案超时/错误时)
```

---

## 四、仓颉语言特有选型注意

| 场景 | 仓颉方案 | 说明 |
|------|----------|------|
| 优先队列 | TreeMap<(priority, id), V> | 仓颉无原生 PQ，用 TreeMap 模拟 |
| lower_bound | TreeMap.forward(k) | 返回 >= k 的迭代器 |
| upper_bound | TreeMap.forward(k, inclusive: false) | 返回 > k 的迭代器 |
| multiset | TreeMap<T, Int64> (值为计数) | 用 TreeMap 模拟多重集 |
| 大整数 | 自行实现或字符串模拟 | 标准库无 BigInteger |
| 位操作 | `& \| ^ ! << >>` + std.math countOnes 等 | 同 C++ |
| 快读 | `readln()` + `split` + `Int64.parse` | 核心方式 |
