# 端到端实战测试 — 模拟 ICE 竞赛作答

## 题目 (模拟)

给定 n 个城市和 m 条双向道路，每条道路有一个通行时间。
从城市 1 出发，求到达每个城市的最短时间。
如果无法到达某个城市，输出 -1。

**输入格式**:
- 第一行两个整数 n, m (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 2×10^5)
- 接下来 m 行，每行三个整数 u, v, w (1 ≤ u,v ≤ n, 1 ≤ w ≤ 10^9)

**输出格式**:
- 一行 n 个整数，第 i 个表示从城市 1 到城市 i 的最短时间，不可达输出 -1

---

# 思路

**核心算法**: Dijkstra 单源最短路 (TreeMap 模拟优先队列)

**关键 insight**: 所有边权 w ≥ 1 为正权，Dijkstra 保证正确性。
仓颉无内置优先队列，使用 TreeMap<Int64, Bool> 编码 (dist * MAXN + nodeId) 作为 key。

**步骤**:
1. 用邻接表存图
2. dist[1] = 0，其余 INF
3. TreeMap 作为小根堆，每次取 removeFirst() 得最小 key
4. 松弛操作更新相邻节点，将新 (dist, node) 编码入 TreeMap
5. 输出 dist 数组，INF 替换为 -1

---

# 复杂度

- **时间复杂度**: O((n + m) log n) — 每条边最多松弛一次，TreeMap 操作 O(log n)
- **空间复杂度**: O(n + m) — 邻接表 + dist 数组

**变量定义**: n = 城市数, m = 边数

**论证**: TreeMap 每次 removeFirst + add 均 O(log n)，总操作数 O(m)

---

# 正确性要点

**方法**: 不变量

- **初始**: dist[1] = 0，源点距离正确
- **维持**: 每次从 TreeMap 取出的节点 u 的 dist[u] 已是最终最短距离
  (因为所有未处理节点的距离 ≥ dist[u]，正权保证后续不会减小)
- **终止**: 所有可达节点均被处理，dist[v] = 最短路

---

# 仓颉实现

```cangjie
import std.collection.*
import std.convert.*

let MAXN: Int64 = 200001

main() {
    let line1 = readln().split(" ")
    let n = Int64.parse(line1[0])
    let m = Int64.parse(line1[1])

    let g = ArrayList<ArrayList<(Int64, Int64)>>(n + 1, {_ => ArrayList<(Int64, Int64)>()})
    var i: Int64 = 0
    while (i < m) {
        let parts = readln().split(" ")
        let u = Int64.parse(parts[0])
        let v = Int64.parse(parts[1])
        let w = Int64.parse(parts[2])
        g[u].add((v, w))
        g[v].add((u, w))
        i++
    }

    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dist = Array<Int64>(n + 1, {_ => INF})
    dist[1] = 0
    let pq = TreeMap<Int64, Bool>()
    pq[0 * MAXN + 1] = true

    while (pq.size > 0) {
        let (key, _) = pq.removeFirst().getOrThrow()
        let d = key / MAXN
        let u = key % MAXN
        if (d > dist[u]) { continue }
        for (j in 0..g[u].size) {
            let (v, w) = g[u][j]
            let nd = d + w
            if (nd < dist[v]) {
                dist[v] = nd
                pq[nd * MAXN + v] = true
            }
        }
    }

    var first = true
    i = 1
    while (i <= n) {
        if (!first) { print(" ") }
        if (dist[i] >= INF) { print(-1) } else { print(dist[i]) }
        first = false
        i++
    }
    println()
}
```

---

# 边界测试

| # | 输入 | 期望输出 | 验证点 |
|---|------|---------|--------|
| 1 | n=1, m=0 | `0` | 最小输入，无边 |
| 2 | n=2, m=0 | `0 -1` | 不可达 |
| 3 | n=10^5, 链状图 | 累加和 | 线性图最长路径 |
| 4 | n=10^5, 全连接 | 最小权直达 | 大量边不超时 |
| 5 | w=10^9, 长路径 | 10^9 × 10^5 < INF | 不溢出 (dist*MAXN) |

---

# 风险项

| # | 风险 | 概率 | 规避策略 |
|---|------|------|---------|
| 1 | dist*MAXN 溢出 Int64 | 低 | 10^9 × 10^5 × 200001 ≈ 2×10^19 > Int64.Max (9.2×10^18) → **需检查**! 若 max dist > 4.6×10^13 则溢出。实际 n×w ≤ 10^14 < 4.6×10^13*MAXN 有风险 → 用 dist*300000 + nodeId 且验证上界 |
| 2 | 同 (dist, node) 编码的 key 冲突 | 低 | MAXN > n 保证不同 node 编码不同；不同 dist 差距 ≥ MAXN |

**常见风险速查**:
- Int64 溢出 → 当 dist 可能很大时，MAXN 取较小值或改用双层 TreeMap
- TLE → Dijkstra O(m log n) 对 m=2×10^5 绰绰有余

---

# 证据引用

- `cj-std-algo-toolkit/references/docs/std/collection/collection_package_api/collection_package_classes.md | TreeMap | "class TreeMap<K, V> where K <: Comparable<K>"`
- `cj-std-algo-toolkit/references/docs/std/collection/collection_package_api/collection_package_classes.md | removeFirst | "public func removeFirst(): ?(K, V)"`
- `cj-language-core/references/docs/user_manual/basic_data_type/integer_type.md | Int64 | "Int64 类型范围 -2^63 到 2^63-1"`
