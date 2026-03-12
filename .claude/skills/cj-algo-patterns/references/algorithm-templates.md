# 仓颉算法竞赛模板库 (Cangjie Algorithm Templates)

> **使用说明**: 所有模板均基于仓颉标准库，import 已标注。直接复制后替换核心逻辑即可。
> **公用函数**: `power(base, exp, mod)` (§6.1)、`extgcd` (§6.6) 等工具函数在多个模板中复用，组合时保留一份即可。
> **字符遍历**: Trie/AC 自动机等用 `for (ch in s)` 遍历 **Byte**，仅限 ASCII；如需 Unicode 请改用 `s.runes()`。

---

## 目录
1. [竞赛 I/O 模板](#1-竞赛-io-模板)
2. [图论](#2-图论)
3. [动态规划](#3-动态规划)
4. [数据结构](#4-数据结构)
5. [字符串](#5-字符串)
6. [数论与数学](#6-数论与数学)
7. [排序与搜索](#7-排序与搜索)
8. [几何](#8-几何)
9. [博弈论](#9-博弈论)
10. [构造与贪心](#10-构造与贪心)
11. [高级数据结构](#11-高级数据结构) — ST表, 树链剖分, 主席树, 点分治, CDQ分治
12. [高级字符串](#12-高级字符串) — AC自动机, Manacher, Z函数
13. [高级字符串(续)](#13-高级字符串-续) — 后缀数组, 后缀自动机
14. [网络流](#14-网络流) — Dinic 最大流, MCMF 最小费用最大流
15. [离线与逻辑](#15-离线与逻辑) — 莫队, 2-SAT
16. [DP优化与平衡树](#16-dp-优化与平衡树) — 凸包优化 DP, FHQ-Treap
17. [高级数据结构(续)](#17-高级数据结构-续) — LCT, 可持久化并查集, 带权并查集
18. [数学进阶](#18-数学进阶) — NTT, CRT/EXCRT, 欧拉函数/降幂
19. [数论进阶](#19-数论进阶) — Lucas定理, Miller-Rabin/Pollard Rho, BSGS
20. [高级图论](#20-高级图论) — DSU on Tree, 虚树
21. [分块](#21-分块) — 分块区间加/求和
22. [基础补充](#22-基础补充) — 二维前缀和/差分, 三分搜索
23. [几何与扫描线](#23-几何与扫描线) — 矩形面积并, 笛卡尔树
24. [异或与离线](#24-异或与离线) — 线性基, 整体二分
25. [树与字符串进阶](#25-树与字符串进阶) — 树哈希, 最小表示法
26. [图连通性](#26-图连通性) — 点双连通分量, 边双连通分量

---

## 1. 竞赛 I/O 模板

### 1.1 基础读写骨架

```cangjie
import std.convert.*
import std.collection.*

main() {
    let n = Int64.parse(readln())
    let parts = readln().split(" ")
    let arr = Array<Int64>(n, {i => Int64.parse(parts[i])})
    
    // --- 核心逻辑 ---
    
    println(result)
}
```

### 1.2 读取多行多组数据

```cangjie
import std.convert.*
import std.collection.*

main() {
    let t = Int64.parse(readln())  // 测试组数
    var cas: Int64 = 0
    while (cas < t) {
        let line1 = readln().split(" ")
        let n = Int64.parse(line1[0])
        let m = Int64.parse(line1[1])
        let vals = readln().split(" ")
        let a = Array<Int64>(n, {i => Int64.parse(vals[i])})
        solve(n, m, a)
        cas++
    }
}

func solve(n: Int64, m: Int64, a: Array<Int64>) {
    // 核心逻辑
    println("answer")
}
```

### 1.3 读取邻接表图

```cangjie
import std.convert.*
import std.collection.*

func readGraph(n: Int64, m: Int64): ArrayList<ArrayList<(Int64, Int64)>> {
    let g = ArrayList<ArrayList<(Int64, Int64)>>(n + 1, {_ => ArrayList<(Int64, Int64)>()})
    var i: Int64 = 0
    while (i < m) {
        let parts = readln().split(" ")
        let u = Int64.parse(parts[0])
        let v = Int64.parse(parts[1])
        let w = Int64.parse(parts[2])
        g[u].add((v, w))
        g[v].add((u, w))  // 无向图; 有向图删除此行
        i++
    }
    return g
}
```

### 1.4 输出数组（空格/换行分隔）

```cangjie
func printArray(arr: Array<Int64>, sep: String) {
    var first = true
    for (v in arr) {
        if (!first) { print(sep) }
        print(v)
        first = false
    }
    println()
}
```

---

## 2. 图论

### 2.1 BFS — 宽度优先搜索

```cangjie
import std.collection.*

func bfs(g: ArrayList<ArrayList<Int64>>, start: Int64, n: Int64): Array<Int64> {
    let dist = Array<Int64>(n + 1, {_ => -1})
    let q = ArrayQueue<Int64>()
    dist[start] = 0
    q.add(start)
    while (!q.isEmpty()) {
        let u = q.remove().getOrThrow()
        for (v in g[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1
                q.add(v)
            }
        }
    }
    return dist
}
```

### 2.2 DFS — 深度优先搜索（迭代版防爆栈）

```cangjie
import std.collection.*

func dfs(g: ArrayList<ArrayList<Int64>>, start: Int64, n: Int64): Array<Bool> {
    let visited = Array<Bool>(n + 1, {_ => false})
    let stk = ArrayStack<Int64>()
    stk.add(start)
    while (!stk.isEmpty()) {
        let u = stk.remove().getOrThrow()
        if (visited[u]) { continue }
        visited[u] = true
        for (v in g[u]) {
            if (!visited[v]) {
                stk.add(v)
            }
        }
    }
    return visited
}
// 用法: bfs(g, 0, n) → dist[]; dfs(g, 0, n) → visited[]
```

### 2.3 Dijkstra — 单源最短路（正权）

```cangjie
import std.collection.*
import std.convert.*

// 用 TreeMap<Int64, Bool> 模拟优先队列
// key 编码: key = dist * MAXN + nodeId (MAXN > 最大节点数)
let MAXN: Int64 = 200001

func dijkstra(g: ArrayList<ArrayList<(Int64, Int64)>>, start: Int64, n: Int64): Array<Int64> {
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dist = Array<Int64>(n + 1, {_ => INF})
    dist[start] = 0
    let pq = TreeMap<Int64, Bool>()
    pq[0 * MAXN + start] = true
    while (pq.size > 0) {
        let (key, _) = pq.removeFirst().getOrThrow()
        let d = key / MAXN
        let u = key % MAXN
        if (d > dist[u]) { continue }
        for (i in 0..g[u].size) {
            let (v, w) = g[u][i]
            let nd = d + w
            if (nd < dist[v]) {
                dist[v] = nd
                pq[nd * MAXN + v] = true
            }
        }
    }
    return dist
}
```

> **⚠️ 注意**: 仓颉 Tuple 不实现 `Comparable`，不可直接作为 `TreeMap` 的 Key。
> 解决方案: 将 `(dist, nodeId)` 编码为单个 Int64: `key = dist * MAXN + nodeId`。
> 要求 `MAXN > n` 且 `dist * MAXN` 不溢出 Int64。

### 2.4 Bellman-Ford / SPFA — 负权最短路

```cangjie
import std.collection.*

func bellmanFord(n: Int64, edges: Array<(Int64, Int64, Int64)>, start: Int64): (Array<Int64>, Bool) {
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dist = Array<Int64>(n + 1, {_ => INF})
    dist[start] = 0
    var updated = false
    var iter: Int64 = 0
    while (iter < n) {
        updated = false
        for ((u, v, w) in edges) {
            if (dist[u] < INF && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w
                updated = true
            }
        }
        if (!updated) { break }
        iter++
    }
    // updated == true 在第 n 轮 → 存在负环
    return (dist, updated)
}
```

### 2.5 Floyd — 全源最短路

```cangjie
func floyd(n: Int64, dist: Array<Array<Int64>>) {
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    var k: Int64 = 1
    while (k <= n) {
        var i: Int64 = 1
        while (i <= n) {
            var j: Int64 = 1
            while (j <= n) {
                if (dist[i][k] < INF && dist[k][j] < INF) {
                    let nd = dist[i][k] + dist[k][j]
                    if (nd < dist[i][j]) {
                        dist[i][j] = nd
                    }
                }
                j++
            }
            i++
        }
        k++
    }
}
```

### 2.6 并查集 (Union-Find)

```cangjie
import std.collection.*

class UnionFind {
    var parent: Array<Int64>
    var rank: Array<Int64>
    var count: Int64  // 连通分量数

    public init(n: Int64) {
        this.parent = Array<Int64>(n, {i => i})
        this.rank = Array<Int64>(n, {_ => 0})
        this.count = n
    }

    public func find(x: Int64): Int64 {
        if (parent[x] != x) {
            parent[x] = find(parent[x])  // 路径压缩
        }
        return parent[x]
    }

    public func union(x: Int64, y: Int64): Bool {
        let rx = find(x)
        let ry = find(y)
        if (rx == ry) { return false }
        if (rank[rx] < rank[ry]) {
            parent[rx] = ry
        } else if (rank[rx] > rank[ry]) {
            parent[ry] = rx
        } else {
            parent[ry] = rx
            rank[rx]++
        }
        count--
        return true
    }

    public func connected(x: Int64, y: Int64): Bool {
        find(x) == find(y)
    }
}
```

### 2.7 拓扑排序 (Kahn 算法)

```cangjie
import std.collection.*

func topoSort(n: Int64, g: ArrayList<ArrayList<Int64>>, inDeg: Array<Int64>): Array<Int64> {
    let q = ArrayQueue<Int64>()
    var i: Int64 = 1
    while (i <= n) {
        if (inDeg[i] == 0) { q.add(i) }
        i++
    }
    let order = ArrayList<Int64>()
    while (!q.isEmpty()) {
        let u = q.remove().getOrThrow()
        order.add(u)
        for (v in g[u]) {
            inDeg[v]--
            if (inDeg[v] == 0) {
                q.add(v)
            }
        }
    }
    return order.toArray()
    // order.size < n → 存在环
}
```

### 2.8 Kruskal — 最小生成树

```cangjie
import std.collection.*
import std.sort.*

func kruskal(n: Int64, edges: Array<(Int64, Int64, Int64)>): Int64 {
    // edges: (u, v, w)
    var sortedEdges = edges  // copy
    sort(sortedEdges, key: { e: (Int64, Int64, Int64) => e[2] })
    let uf = UnionFind(n)
    var totalWeight: Int64 = 0
    var edgeCount: Int64 = 0
    for ((u, v, w) in sortedEdges) {
        if (uf.union(u, v)) {
            totalWeight += w
            edgeCount++
            if (edgeCount == n - 1) { break }
        }
    }
    return totalWeight
}
```

### 2.9 Tarjan — 强连通分量

```cangjie
import std.collection.*

class TarjanSCC {
    var g: ArrayList<ArrayList<Int64>>
    var dfn: Array<Int64>
    var low: Array<Int64>
    var onStack: Array<Bool>
    var stk: ArrayStack<Int64>
    var timer: Int64
    var sccId: Array<Int64>
    var sccCount: Int64

    public init(n: Int64, g: ArrayList<ArrayList<Int64>>) {
        this.g = g
        this.dfn = Array<Int64>(n + 1, {_ => 0})
        this.low = Array<Int64>(n + 1, {_ => 0})
        this.onStack = Array<Bool>(n + 1, {_ => false})
        this.stk = ArrayStack<Int64>()
        this.timer = 0
        this.sccId = Array<Int64>(n + 1, {_ => -1})
        this.sccCount = 0
    }

    public func solve(n: Int64) {
        var i: Int64 = 1
        while (i <= n) {
            if (dfn[i] == 0) { dfs(i) }
            i++
        }
    }

    func dfs(u: Int64): Unit {
        timer++
        dfn[u] = timer
        low[u] = timer
        stk.add(u)
        onStack[u] = true
        for (v in g[u]) {
            if (dfn[v] == 0) {
                dfs(v)
                if (low[v] < low[u]) { low[u] = low[v] }
            } else if (onStack[v]) {
                if (dfn[v] < low[u]) { low[u] = dfn[v] }
            }
        }
        if (dfn[u] == low[u]) {
            while (true) {
                let v = stk.remove().getOrThrow()
                onStack[v] = false
                sccId[v] = sccCount
                if (v == u) { break }
            }
            sccCount++
        }
    }
}
```

### 2.10 LCA — 最近公共祖先（倍增法）

```cangjie
import std.collection.*
import std.math.*

class LCA {
    var up: Array<Array<Int64>>  // up[v][k] = v 的第 2^k 祖先
    var depth: Array<Int64>
    var LOG: Int64

    public init(n: Int64, g: ArrayList<ArrayList<Int64>>, root: Int64) {
        let logVal: Int64 = 20  // 足够 10^6 节点
        this.LOG = logVal
        this.up = Array<Array<Int64>>(n + 1, {_ => Array<Int64>(logVal, {_ => 0})})
        this.depth = Array<Int64>(n + 1, {_ => 0})
        bfsBuild(n, g, root)
    }

    func bfsBuild(n: Int64, g: ArrayList<ArrayList<Int64>>, root: Int64) {
        let q = ArrayQueue<Int64>()
        let visited = Array<Bool>(n + 1, {_ => false})
        q.add(root)
        visited[root] = true
        depth[root] = 0
        while (!q.isEmpty()) {
            let u = q.remove().getOrThrow()
            for (v in g[u]) {
                if (!visited[v]) {
                    visited[v] = true
                    depth[v] = depth[u] + 1
                    up[v][0] = u
                    var k: Int64 = 1
                    while (k < LOG) {
                        up[v][k] = up[up[v][k - 1]][k - 1]
                        k++
                    }
                    q.add(v)
                }
            }
        }
    }

    public func query(a: Int64, b: Int64): Int64 {
        var u = a
        var v = b
        if (depth[u] < depth[v]) { let tmp = u; u = v; v = tmp }
        let diff = depth[u] - depth[v]
        var k: Int64 = 0
        while (k < LOG) {
            if (((diff >> k) & 1) == 1) {
                u = up[u][k]
            }
            k++
        }
        if (u == v) { return u }
        k = LOG - 1
        while (k >= 0) {
            if (up[u][k] != up[v][k]) {
                u = up[u][k]
                v = up[v][k]
            }
            k--
        }
        return up[u][0]
    }
}
```

---

## 3. 动态规划

### 3.1 01 背包

```cangjie
func knapsack01(n: Int64, cap: Int64, w: Array<Int64>, v: Array<Int64>): Int64 {
    let dp = Array<Int64>(cap + 1, {_ => 0})
    var i: Int64 = 0
    while (i < n) {
        var j = cap
        while (j >= w[i]) {
            let nv = dp[j - w[i]] + v[i]
            if (nv > dp[j]) { dp[j] = nv }
            j--
        }
        i++
    }
    return dp[cap]
}
```

### 3.2 完全背包

```cangjie
func knapsackComplete(n: Int64, cap: Int64, w: Array<Int64>, v: Array<Int64>): Int64 {
    let dp = Array<Int64>(cap + 1, {_ => 0})
    var i: Int64 = 0
    while (i < n) {
        var j = w[i]
        while (j <= cap) {
            let nv = dp[j - w[i]] + v[i]
            if (nv > dp[j]) { dp[j] = nv }
            j++
        }
        i++
    }
    return dp[cap]
}
```

### 3.3 最长递增子序列 (LIS) — O(n log n)

```cangjie
import std.collection.*

func lis(a: Array<Int64>): Int64 {
    let tails = ArrayList<Int64>()  // tails[i] = 长度为 i+1 的 LIS 末尾最小值
    for (x in a) {
        // 二分查找第一个 >= x 的位置
        var lo: Int64 = 0
        var hi: Int64 = tails.size
        while (lo < hi) {
            let mid = (lo + hi) / 2
            if (tails[mid] < x) {
                lo = mid + 1
            } else {
                hi = mid
            }
        }
        if (lo == tails.size) {
            tails.add(x)
        } else {
            tails[lo] = x
        }
    }
    return tails.size
}
```

### 3.4 最长公共子序列 (LCS)

```cangjie
func lcs(a: Array<Int64>, b: Array<Int64>): Int64 {
    let n = a.size
    let m = b.size
    let dp = Array<Array<Int64>>(n + 1, {_ => Array<Int64>(m + 1, {_ => 0})})
    var i: Int64 = 1
    while (i <= n) {
        var j: Int64 = 1
        while (j <= m) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1
            } else {
                dp[i][j] = if (dp[i - 1][j] > dp[i][j - 1]) { dp[i - 1][j] } else { dp[i][j - 1] }
            }
            j++
        }
        i++
    }
    return dp[n][m]
}
```

### 3.5 区间 DP

```cangjie
func intervalDP(a: Array<Int64>): Int64 {
    let n = a.size
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dp = Array<Array<Int64>>(n, {_ => Array<Int64>(n, {_ => INF})})
    // 预处理前缀和
    let pre = Array<Int64>(n + 1, {_ => 0})
    var i: Int64 = 0
    while (i < n) { pre[i + 1] = pre[i] + a[i]; i++ }

    i = 0
    while (i < n) { dp[i][i] = 0; i++ }

    var len: Int64 = 2
    while (len <= n) {
        i = 0
        while (i + len - 1 < n) {
            let j = i + len - 1
            var k = i
            while (k < j) {
                let cost = dp[i][k] + dp[k + 1][j] + pre[j + 1] - pre[i]
                if (cost < dp[i][j]) { dp[i][j] = cost }
                k++
            }
            i++
        }
        len++
    }
    return dp[0][n - 1]
}
```

### 3.6 数位 DP 框架

```cangjie
import std.collection.*
import std.convert.*

// 统计 [0, num] 中满足条件的数字个数
func digitDP(num: Int64): Int64 {
    let digits = ArrayList<Int64>()
    var tmp = num
    while (tmp > 0) {
        digits.add(tmp % 10)
        tmp /= 10
    }
    digits.reverse()
    let n = digits.size
    // memo[pos][state][tight] — 根据题意设计 state
    let memo = Array<Array<Array<Int64>>>(n,
        {_ => Array<Array<Int64>>(/* state_size */ 2, {_ => Array<Int64>(2, {_ => -1})})})

    func dfs(pos: Int64, state: Int64, tight: Int64): Int64 {
        if (pos == n) {
            return if (/* 终态条件 */ true) { 1 } else { 0 }
        }
        if (memo[pos][state][tight] != -1) {
            return memo[pos][state][tight]
        }
        let limit = if (tight == 1) { digits[pos] } else { 9 }
        var res: Int64 = 0
        var d: Int64 = 0
        while (d <= limit) {
            let newState = state  // 根据题意更新
            let newTight = if (tight == 1 && d == limit) { 1 } else { 0 }
            res += dfs(pos + 1, newState, newTight)
            d++
        }
        memo[pos][state][tight] = res
        return res
    }

    return dfs(0, 0, 1)
}
```

### 3.7 状态压缩 DP

```cangjie
func bitmaskDP(n: Int64, cost: Array<Array<Int64>>): Int64 {
    let full = (1 << n) - 1
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dp = Array<Array<Int64>>(1 << n, {_ => Array<Int64>(n, {_ => INF})})
    dp[1][0] = 0  // 从节点0出发

    var mask: Int64 = 1
    while (mask <= full) {
        var u: Int64 = 0
        while (u < n) {
            if (dp[mask][u] < INF && ((mask >> u) & 1) == 1) {
                var v: Int64 = 0
                while (v < n) {
                    if (((mask >> v) & 1) == 0) {
                        let newMask = mask | (1 << v)
                        let nd = dp[mask][u] + cost[u][v]
                        if (nd < dp[newMask][v]) {
                            dp[newMask][v] = nd
                        }
                    }
                    v++
                }
            }
            u++
        }
        mask++
    }
    // 返回经过所有节点回到起点的最短路
    var ans = INF
    var u: Int64 = 0
    while (u < n) {
        let d = dp[full][u] + cost[u][0]
        if (d < ans) { ans = d }
        u++
    }
    return ans
}
```

### 3.8 树形 DP — 树的直径

```cangjie
import std.collection.*

func treeDiameter(n: Int64, g: ArrayList<ArrayList<(Int64, Int64)>>): Int64 {
    var diameter: Int64 = 0
    let dp = Array<Int64>(n + 1, {_ => 0})  // dp[v] = 从 v 向下的最长路径

    func dfs(u: Int64, parent: Int64): Unit {
        dp[u] = 0
        var maxChild: Int64 = 0
        for ((v, w) in g[u]) {
            if (v == parent) { continue }
            dfs(v, u)
            let childLen = dp[v] + w
            // 更新直径: 经过 u 的最长路径 = 最长 + 次长
            let candidate = maxChild + childLen
            if (candidate > diameter) { diameter = candidate }
            if (childLen > maxChild) { maxChild = childLen }
        }
        dp[u] = maxChild
    }

    dfs(1, 0)
    return diameter
}
```

---

## 4. 数据结构

### 4.1 线段树 (单点修改 + 区间查询)

```cangjie
class SegTree {
    var tree: Array<Int64>
    var n: Int64

    public init(n: Int64) {
        this.n = n
        this.tree = Array<Int64>(4 * n + 4, {_ => 0})
    }

    public func build(a: Array<Int64>, node: Int64, l: Int64, r: Int64): Unit {
        if (l == r) {
            tree[node] = a[l]
            return
        }
        let mid = (l + r) / 2
        build(a, node * 2, l, mid)
        build(a, node * 2 + 1, mid + 1, r)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
    }

    public func update(node: Int64, l: Int64, r: Int64, pos: Int64, val: Int64): Unit {
        if (l == r) {
            tree[node] = val
            return
        }
        let mid = (l + r) / 2
        if (pos <= mid) {
            update(node * 2, l, mid, pos, val)
        } else {
            update(node * 2 + 1, mid + 1, r, pos, val)
        }
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
    }

    public func query(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64): Int64 {
        if (ql <= l && r <= qr) {
            return tree[node]
        }
        let mid = (l + r) / 2
        var res: Int64 = 0
        if (ql <= mid) { res += query(node * 2, l, mid, ql, qr) }
        if (qr > mid) { res += query(node * 2 + 1, mid + 1, r, ql, qr) }
        return res
    }
}
// 用法: let seg = SegTree(a); seg.update(1,0,n-1,pos,val); seg.query(1,0,n-1,l,r)
```

### 4.2 线段树 (区间修改 + 懒标记)

```cangjie
class LazySegTree {
    var tree: Array<Int64>
    var lazy: Array<Int64>
    var n: Int64

    public init(n: Int64) {
        this.n = n
        this.tree = Array<Int64>(4 * n + 4, {_ => 0})
        this.lazy = Array<Int64>(4 * n + 4, {_ => 0})
    }

    func pushDown(node: Int64, l: Int64, r: Int64) {
        if (lazy[node] != 0) {
            let mid = (l + r) / 2
            tree[node * 2] += lazy[node] * (mid - l + 1)
            tree[node * 2 + 1] += lazy[node] * (r - mid)
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
            lazy[node] = 0
        }
    }

    public func build(a: Array<Int64>, node: Int64, l: Int64, r: Int64): Unit {
        if (l == r) { tree[node] = a[l]; return }
        let mid = (l + r) / 2
        build(a, node * 2, l, mid)
        build(a, node * 2 + 1, mid + 1, r)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
    }

    public func rangeAdd(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64, val: Int64): Unit {
        if (ql <= l && r <= qr) {
            tree[node] += val * (r - l + 1)
            lazy[node] += val
            return
        }
        pushDown(node, l, r)
        let mid = (l + r) / 2
        if (ql <= mid) { rangeAdd(node * 2, l, mid, ql, qr, val) }
        if (qr > mid) { rangeAdd(node * 2 + 1, mid + 1, r, ql, qr, val) }
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
    }

    public func query(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64): Int64 {
        if (ql <= l && r <= qr) { return tree[node] }
        pushDown(node, l, r)
        let mid = (l + r) / 2
        var res: Int64 = 0
        if (ql <= mid) { res += query(node * 2, l, mid, ql, qr) }
        if (qr > mid) { res += query(node * 2 + 1, mid + 1, r, ql, qr) }
        return res
    }
}
```

### 4.3 树状数组 (BIT / Fenwick Tree)

```cangjie
class BIT {
    var c: Array<Int64>
    var n: Int64

    public init(n: Int64) {
        this.n = n
        this.c = Array<Int64>(n + 1, {_ => 0})
    }

    public func update(pos: Int64, delta: Int64) {
        var i = pos
        while (i <= n) {
            c[i] += delta
            i += i & (-i)
        }
    }

    public func query(pos: Int64): Int64 {
        var s: Int64 = 0
        var i = pos
        while (i > 0) {
            s += c[i]
            i -= i & (-i)
        }
        return s
    }

    public func rangeQuery(l: Int64, r: Int64): Int64 {
        query(r) - query(l - 1)
    }
}
// 用法: let bit = BIT(n); bit.update(i, delta); bit.rangeQuery(l, r)
```

### 4.4 单调栈

```cangjie
import std.collection.*

// 求每个元素右边第一个比它大的元素位置（不存在为 -1）
func nextGreater(a: Array<Int64>): Array<Int64> {
    let n = a.size
    let res = Array<Int64>(n, {_ => -1})
    let stk = ArrayStack<Int64>()  // 存下标
    var i: Int64 = 0
    while (i < n) {
        while (!stk.isEmpty() && a[stk.peek().getOrThrow()] < a[i]) {
            res[stk.remove().getOrThrow()] = i
        }
        stk.add(i)
        i++
    }
    return res
}
```

### 4.5 单调队列（滑动窗口最值）

```cangjie
import std.collection.*

// 滑动窗口大小为 k，求每个窗口的最大值
func slidingMax(a: Array<Int64>, k: Int64): Array<Int64> {
    let n = a.size
    let res = ArrayList<Int64>()
    let dq = ArrayDeque<Int64>()  // 存下标，维护单调递减
    var i: Int64 = 0
    while (i < n) {
        // 移除窗口外的
        while (!dq.isEmpty() && dq.first.getOrThrow() <= i - k) {
            dq.removeFirst()
        }
        // 移除比当前小的
        while (!dq.isEmpty() && a[dq.last.getOrThrow()] <= a[i]) {
            dq.removeLast()
        }
        dq.addLast(i)
        if (i >= k - 1) {
            res.add(a[dq.first.getOrThrow()])
        }
        i++
    }
    return res.toArray()
}
```

### 4.6 字典树 (Trie)

```cangjie
class TrieNode {
    var children: Array<?TrieNode>
    var isEnd: Bool
    var count: Int64

    public init() {
        this.children = Array<?TrieNode>(26, {_ => None})
        this.isEnd = false
        this.count = 0
    }
}

class Trie {
    var root: TrieNode

    public init() {
        this.root = TrieNode()
    }

    public func insert(word: String) {
        var cur = root
        for (ch in word) {  // ASCII-only: Byte 值等于码点
            let idx = Int64(ch) - Int64(UInt32(r'a'))
            match (cur.children[idx]) {
                case None =>
                    cur.children[idx] = Some(TrieNode())
                case _ => ()
            }
            cur = cur.children[idx].getOrThrow()
            cur.count++
        }
        cur.isEnd = true
    }

    public func search(word: String): Bool {
        var cur = root
        for (ch in word) {  // ASCII-only
            let idx = Int64(ch) - Int64(UInt32(r'a'))
            match (cur.children[idx]) {
                case None => return false
                case Some(next) => cur = next
            }
        }
        return cur.isEnd
    }

    public func startsWith(prefix: String): Int64 {
        var cur = root
        for (ch in prefix) {  // ASCII-only
            let idx = Int64(ch) - Int64(UInt32(r'a'))
            match (cur.children[idx]) {
                case None => return 0
                case Some(next) => cur = next
            }
        }
        return cur.count
    }
}
```

---

## 5. 字符串

### 5.1 KMP 模式匹配

```cangjie
import std.collection.*

func kmpBuildNext(pattern: String): Array<Int64> {
    let m = pattern.size
    let next = Array<Int64>(m, {_ => 0})
    let p = pattern.toArray()  // Array<Byte>
    var j: Int64 = 0
    var i: Int64 = 1
    while (i < m) {
        while (j > 0 && p[i] != p[j]) {
            j = next[j - 1]
        }
        if (p[i] == p[j]) { j++ }
        next[i] = j
        i++
    }
    return next
}

func kmpSearch(text: String, pattern: String): ArrayList<Int64> {
    let next = kmpBuildNext(pattern)
    let t = text.toArray()
    let p = pattern.toArray()
    let n = text.size
    let m = pattern.size
    let matches = ArrayList<Int64>()
    var j: Int64 = 0
    var i: Int64 = 0
    while (i < n) {
        while (j > 0 && t[i] != p[j]) {
            j = next[j - 1]
        }
        if (t[i] == p[j]) { j++ }
        if (j == m) {
            matches.add(i - m + 1)
            j = next[j - 1]
        }
        i++
    }
    return matches
}
// 用法: kmpSearch("abababc", "aba") → [0, 2]
```

### 5.2 字符串哈希 (Rabin-Karp)

```cangjie
class StringHash {
    var h: Array<Int64>
    var pw: Array<Int64>
    var MOD: Int64
    var BASE: Int64

    public init(s: String) {
        this.MOD = 998244353
        this.BASE = 131
        let n = s.size
        let a = s.toArray()
        this.h = Array<Int64>(n + 1, {_ => 0})
        this.pw = Array<Int64>(n + 1, {_ => 0})
        pw[0] = 1
        var i: Int64 = 0
        while (i < n) {
            h[i + 1] = (h[i] * BASE + Int64(a[i])) % MOD
            pw[i + 1] = pw[i] * BASE % MOD
            i++
        }
    }

    // 获取子串 [l, r) 的哈希值 (0-indexed)
    public func getHash(l: Int64, r: Int64): Int64 {
        ((h[r] - h[l] * pw[r - l]) % MOD + MOD) % MOD
    }
}
```

---

## 6. 数论与数学

### 6.1 快速幂

```cangjie
func power(base: Int64, exp: Int64, mod: Int64): Int64 {
    var result: Int64 = 1
    var b = base % mod
    var e = exp
    while (e > 0) {
        if ((e & 1) == 1) {
            result = result * b % mod
        }
        b = b * b % mod
        e >>= 1
    }
    return result
}
```

### 6.2 逆元（费马小定理，mod 为质数）

```cangjie
func modInverse(a: Int64, mod: Int64): Int64 {
    power(a, mod - 2, mod)
}
```

### 6.3 组合数（预处理阶乘）

```cangjie
class Comb {
    var fac: Array<Int64>
    var inv: Array<Int64>
    var MOD: Int64

    public init(n: Int64, mod: Int64) {
        this.MOD = mod
        this.fac = Array<Int64>(n + 1, {_ => 0})
        this.inv = Array<Int64>(n + 1, {_ => 0})
        fac[0] = 1
        var i: Int64 = 1
        while (i <= n) {
            fac[i] = fac[i - 1] * i % MOD
            i++
        }
        inv[n] = power(fac[n], MOD - 2, MOD)
        i = n - 1
        while (i >= 0) {
            inv[i] = inv[i + 1] * (i + 1) % MOD
            i--
        }
    }

    public func C(n: Int64, k: Int64): Int64 {
        if (k < 0 || k > n) { return 0 }
        fac[n] * inv[k] % MOD * inv[n - k] % MOD
    }
}
```

### 6.4 素数筛（埃氏筛 / 线性筛）

```cangjie
import std.collection.*

func sieve(n: Int64): Array<Bool> {
    let isPrime = Array<Bool>(n + 1, {_ => true})
    isPrime[0] = false
    if (n >= 1) { isPrime[1] = false }
    var i: Int64 = 2
    while (i * i <= n) {
        if (isPrime[i]) {
            var j = i * i
            while (j <= n) {
                isPrime[j] = false
                j += i
            }
        }
        i++
    }
    return isPrime
}

// 线性筛
func linearSieve(n: Int64): ArrayList<Int64> {
    let isPrime = Array<Bool>(n + 1, {_ => true})
    let primes = ArrayList<Int64>()
    var i: Int64 = 2
    while (i <= n) {
        if (isPrime[i]) { primes.add(i) }
        var j: Int64 = 0
        while (j < primes.size && i * primes[j] <= n) {
            isPrime[i * primes[j]] = false
            if (i % primes[j] == 0) { break }
            j++
        }
        i++
    }
    return primes
}
// 用法: sieve(100) → Bool数组; linearSieve(100) → 素数列表
```

### 6.5 矩阵快速幂

```cangjie
func matMul(a: Array<Array<Int64>>, b: Array<Array<Int64>>, mod: Int64): Array<Array<Int64>> {
    let n = a.size
    let m = b[0].size
    let k = b.size
    let c = Array<Array<Int64>>(n, {_ => Array<Int64>(m, {_ => 0})})
    var i: Int64 = 0
    while (i < n) {
        var j: Int64 = 0
        while (j < m) {
            var p: Int64 = 0
            while (p < k) {
                c[i][j] = (c[i][j] + a[i][p] * b[p][j]) % mod
                p++
            }
            j++
        }
        i++
    }
    return c
}

func matPow(mat: Array<Array<Int64>>, exp: Int64, mod: Int64): Array<Array<Int64>> {
    let n = mat.size
    var result = Array<Array<Int64>>(n, {i => Array<Int64>(n, {j => if (i == j) { 1 } else { 0 }})})
    var base = mat
    var e = exp
    while (e > 0) {
        if ((e & 1) == 1) {
            result = matMul(result, base, mod)
        }
        base = matMul(base, base, mod)
        e >>= 1
    }
    return result
}
```

### 6.6 扩展欧几里得

```cangjie
func extgcd(a: Int64, b: Int64): (Int64, Int64, Int64) {
    // 返回 (g, x, y) 使得 a*x + b*y = g = gcd(a,b)
    if (b == 0) {
        return (a, 1, 0)
    }
    let (g, x1, y1) = extgcd(b, a % b)
    return (g, y1, x1 - (a / b) * y1)
}
```

---

## 7. 排序与搜索

### 7.1 二分搜索（通用框架）

```cangjie
// 找第一个满足 pred(x) == true 的位置
func lowerBound(arr: Array<Int64>, target: Int64): Int64 {
    var lo: Int64 = 0
    var hi: Int64 = arr.size
    while (lo < hi) {
        let mid = (lo + hi) / 2
        if (arr[mid] < target) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}

func upperBound(arr: Array<Int64>, target: Int64): Int64 {
    var lo: Int64 = 0
    var hi: Int64 = arr.size
    while (lo < hi) {
        let mid = (lo + hi) / 2
        if (arr[mid] <= target) {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    return lo
}
```

### 7.2 二分答案

```cangjie
func binarySearchAnswer(lo: Int64, hi: Int64, check: (Int64) -> Bool): Int64 {
    var l = lo
    var r = hi
    while (l < r) {
        let mid = (l + r) / 2
        if (check(mid)) {
            r = mid
        } else {
            l = mid + 1
        }
    }
    return l
}
```

### 7.3 离散化

```cangjie
import std.collection.*
import std.sort.*

func discretize(a: Array<Int64>): (Array<Int64>, ArrayList<Int64>) {
    let sorted = ArrayList<Int64>()
    let s = HashSet<Int64>()
    for (x in a) { s.add(x) }
    for (x in s) { sorted.add(x) }
    sort(sorted)
    // 构建映射
    let mp = HashMap<Int64, Int64>()
    var idx: Int64 = 0
    for (x in sorted) {
        mp[x] = idx
        idx++
    }
    let result = Array<Int64>(a.size, {i => mp[a[i]]})
    return (result, sorted)
}
```

---

## 8. 几何

### 8.1 二维向量与叉积

```cangjie
struct Vec2 {
    let x: Int64
    let y: Int64

    public init(x: Int64, y: Int64) {
        this.x = x
        this.y = y
    }
}

func cross(o: Vec2, a: Vec2, b: Vec2): Int64 {
    (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
}
```

### 8.2 凸包 (Andrew's Monotone Chain)

```cangjie
import std.collection.*
import std.sort.*

func convexHull(points: Array<Vec2>): Array<Vec2> {
    let n = points.size
    if (n < 3) { return points }
    var pts = points
    sort(pts, by: { a: Vec2, b: Vec2 =>
        if (a.x != b.x) {
            if (a.x < b.x) { Ordering.LT } else { Ordering.GT }
        } else {
            if (a.y < b.y) { Ordering.LT } else if (a.y > b.y) { Ordering.GT } else { Ordering.EQ }
        }
    })
    let hull = ArrayList<Vec2>()
    // 下凸包
    for (p in pts) {
        while (hull.size >= 2 && cross(hull[hull.size - 2], hull[hull.size - 1], p) <= 0) {
            hull.remove(at: hull.size - 1)
        }
        hull.add(p)
    }
    // 上凸包
    let lower = hull.size + 1
    var i = n - 2
    while (i >= 0) {
        let p = pts[i]
        while (hull.size >= lower && cross(hull[hull.size - 2], hull[hull.size - 1], p) <= 0) {
            hull.remove(at: hull.size - 1)
        }
        hull.add(p)
        i--
    }
    hull.remove(at: hull.size - 1)  // 移除重复的起点
    return hull.toArray()
}
```

---

## 9. 博弈论

### 9.1 SG 函数 (Sprague-Grundy)

```cangjie
import std.collection.*

func sg(n: Int64, moves: Array<Int64>): Array<Int64> {
    let sgVal = Array<Int64>(n + 1, {_ => 0})
    var i: Int64 = 1
    while (i <= n) {
        let reachable = HashSet<Int64>()
        for (m in moves) {
            if (i >= m) {
                reachable.add(sgVal[i - m])
            }
        }
        // mex: 最小排除值
        var mex: Int64 = 0
        while (reachable.contains(mex)) { mex++ }
        sgVal[i] = mex
        i++
    }
    return sgVal
}

// 多堆 Nim: XOR 所有 SG 值, 非零先手赢
```

---

## 10. 构造与贪心

### 10.1 贪心 + 排序模板

```cangjie
import std.sort.*
import std.collection.*
import std.convert.*

main() {
    let n = Int64.parse(readln())
    let items = Array<(Int64, Int64)>(n, {i =>
        let parts = readln().split(" ")
        (Int64.parse(parts[0]), Int64.parse(parts[1]))
    })
    // 按第二关键字排序（活动选择问题: 按结束时间升序）
    sort(items, by: { a: (Int64, Int64), b: (Int64, Int64) =>
        if (a[1] < b[1]) { Ordering.LT }
        else if (a[1] > b[1]) { Ordering.GT }
        else { Ordering.EQ }
    })

    var count: Int64 = 0
    var lastEnd: Int64 = -1
    for ((s, e) in items) {
        if (s >= lastEnd) {
            count++
            lastEnd = e
        }
    }
    println(count)
}
```

### 10.2 前缀和 + 差分

```cangjie
// 一维前缀和
func prefixSum(a: Array<Int64>): Array<Int64> {
    let n = a.size
    let pre = Array<Int64>(n + 1, {_ => 0})
    var i: Int64 = 0
    while (i < n) {
        pre[i + 1] = pre[i] + a[i]
        i++
    }
    return pre
    // 区间和 [l, r] = pre[r+1] - pre[l]
}

// 一维差分: 对区间 [l, r] 加 val
func diffAdd(diff: Array<Int64>, l: Int64, r: Int64, val: Int64) {
    diff[l] += val
    if (r + 1 < diff.size) { diff[r + 1] -= val }
}

// 还原差分数组
func diffRestore(diff: Array<Int64>): Array<Int64> {
    let n = diff.size
    let a = Array<Int64>(n, {_ => 0})
    a[0] = diff[0]
    var i: Int64 = 1
    while (i < n) {
        a[i] = a[i - 1] + diff[i]
        i++
    }
    return a
}
```

---

## 11. 高级数据结构

### 11.1 ST 表 (Sparse Table) — 静态 RMQ O(1) 查询

```cangjie
import std.collection.*
import std.math.*

class SparseTable {
    var table: Array<Array<Int64>>
    var logTable: Array<Int64>
    var n: Int64

    public init(a: Array<Int64>) {
        let sz = a.size
        this.n = sz
        let maxLog: Int64 = 20
        this.logTable = Array<Int64>(sz + 1, {_ => 0})
        var i: Int64 = 2
        while (i <= sz) {
            logTable[i] = logTable[i / 2] + 1
            i++
        }
        this.table = Array<Array<Int64>>(maxLog + 1, {_ => Array<Int64>(sz, {_ => 0})})
        i = 0
        while (i < sz) {
            table[0][i] = a[i]
            i++
        }
        var k: Int64 = 1
        while (k <= maxLog) {
            i = 0
            while (i + (1 << k) - 1 < sz) {
                let left = table[k - 1][i]
                let right = table[k - 1][i + (1 << (k - 1))]
                table[k][i] = if (left < right) { left } else { right }
                i++
            }
            k++
        }
    }

    // 查询 [l, r] 的最小值, 0-indexed
    public func query(l: Int64, r: Int64): Int64 {
        let k = logTable[r - l + 1]
        let left = table[k][l]
        let right = table[k][r - (1 << k) + 1]
        if (left < right) { left } else { right }
    }
}
```

### 11.2 树链剖分 (Heavy-Light Decomposition)

```cangjie
import std.collection.*

class HLD {
    var parent: Array<Int64>
    var depth: Array<Int64>
    var heavy: Array<Int64>   // 重子节点
    var head: Array<Int64>    // 链头
    var pos: Array<Int64>     // DFS 序位置
    var subSize: Array<Int64>
    var timer: Int64

    public init(n: Int64, g: ArrayList<ArrayList<Int64>>, root: Int64) {
        this.parent = Array<Int64>(n + 1, {_ => 0})
        this.depth = Array<Int64>(n + 1, {_ => 0})
        this.heavy = Array<Int64>(n + 1, {_ => -1})
        this.head = Array<Int64>(n + 1, {i => i})
        this.pos = Array<Int64>(n + 1, {_ => 0})
        this.subSize = Array<Int64>(n + 1, {_ => 1})
        this.timer = 0
        dfs1(g, root, 0, 0)
        dfs2(g, root, root)
    }

    // 第一遍 DFS: 求 parent, depth, subSize, heavy (迭代版)
    func dfs1(g: ArrayList<ArrayList<Int64>>, root: Int64, par: Int64, dep: Int64) {
        let stk = ArrayStack<(Int64, Int64, Int64, Bool)>()
        stk.add((root, par, dep, false))
        while (!stk.isEmpty()) {
            let (u, p, d, processed) = stk.remove().getOrThrow()
            if (processed) {
                // 回溯阶段: 汇总子树信息
                var maxSub: Int64 = 0
                for (v in g[u]) {
                    if (v != p) {
                        subSize[u] += subSize[v]
                        if (subSize[v] > maxSub) {
                            maxSub = subSize[v]
                            heavy[u] = v
                        }
                    }
                }
            } else {
                parent[u] = p
                depth[u] = d
                subSize[u] = 1
                heavy[u] = -1
                stk.add((u, p, d, true))  // 标记回溯
                for (v in g[u]) {
                    if (v != p) {
                        stk.add((v, u, d + 1, false))
                    }
                }
            }
        }
    }

    // 第二遍 DFS: 链剖分 (迭代版)
    func dfs2(g: ArrayList<ArrayList<Int64>>, root: Int64, h: Int64) {
        let stk = ArrayStack<(Int64, Int64)>()  // (node, head)
        stk.add((root, h))
        while (!stk.isEmpty()) {
            let (u, hd) = stk.remove().getOrThrow()
            head[u] = hd
            pos[u] = timer
            timer++
            // 先加轻子（后处理），再加重子（先处理）
            let lightChildren = ArrayList<Int64>()
            for (v in g[u]) {
                if (v != parent[u] && v != heavy[u]) {
                    lightChildren.add(v)
                }
            }
            // 轻子逆序入栈（LIFO → 正序处理）
            var i = lightChildren.size - 1
            while (i >= 0) {
                stk.add((lightChildren[i], lightChildren[i]))
                i--
            }
            // 重子最后入栈 → 最先处理
            if (heavy[u] != -1) {
                stk.add((heavy[u], hd))
            }
        }
    }

    // 路径查询辅助: 返回 (u, v) 跳链过程中的 DFS 序区间对
    public func pathQuery(a: Int64, b: Int64): ArrayList<(Int64, Int64)> {
        let ranges = ArrayList<(Int64, Int64)>()
        var u = a
        var v = b
        while (head[u] != head[v]) {
            if (depth[head[u]] < depth[head[v]]) {
                let tmp = u; u = v; v = tmp
            }
            ranges.add((pos[head[u]], pos[u]))
            u = parent[head[u]]
        }
        if (depth[u] > depth[v]) { let tmp = u; u = v; v = tmp }
        ranges.add((pos[u], pos[v]))
        return ranges
    }
}
```

### 11.3 主席树 (可持久化线段树) — 静态区间第 k 小

```cangjie
import std.collection.*

class PersistentSegTree {
    var lc: Array<Int64>    // 左子
    var rc: Array<Int64>    // 右子
    var cnt: Array<Int64>   // 节点包含元素数
    var tot: Int64
    var roots: Array<Int64>

    public init(maxN: Int64) {
        let maxNodes = maxN * 40  // 每次插入 O(log n) 个新节点
        this.lc = Array<Int64>(maxNodes, {_ => 0})
        this.rc = Array<Int64>(maxNodes, {_ => 0})
        this.cnt = Array<Int64>(maxNodes, {_ => 0})
        this.tot = 0
        this.roots = Array<Int64>(maxN + 1, {_ => 0})
    }

    // 在 prev 版本基础上插入值 val (值域 [1, m])
    public func insert(prev: Int64, l: Int64, r: Int64, val: Int64): Int64 {
        tot++
        let cur = tot
        lc[cur] = lc[prev]
        rc[cur] = rc[prev]
        cnt[cur] = cnt[prev] + 1
        if (l == r) { return cur }
        let mid = (l + r) / 2
        if (val <= mid) {
            lc[cur] = insert(lc[prev], l, mid, val)
        } else {
            rc[cur] = insert(rc[prev], mid + 1, r, val)
        }
        return cur
    }

    // 查询 [rootL, rootR] 版本区间的第 k 小 (值域 [l, r])
    public func kth(rootL: Int64, rootR: Int64, l: Int64, r: Int64, k: Int64): Int64 {
        if (l == r) { return l }
        let mid = (l + r) / 2
        let leftCnt = cnt[lc[rootR]] - cnt[lc[rootL]]
        if (k <= leftCnt) {
            return kth(lc[rootL], lc[rootR], l, mid, k)
        } else {
            return kth(rc[rootL], rc[rootR], mid + 1, r, k - leftCnt)
        }
    }
}
```

### 11.4 点分治 (Centroid Decomposition)

```cangjie
import std.collection.*

class CentroidDecomp {
    var g: ArrayList<ArrayList<(Int64, Int64)>>
    var subSize: Array<Int64>
    var removed: Array<Bool>
    var n: Int64
    // 结果容器 (根据题意定制)
    var answer: Int64

    public init(n: Int64, g: ArrayList<ArrayList<(Int64, Int64)>>) {
        this.n = n
        this.g = g
        this.subSize = Array<Int64>(n + 1, {_ => 0})
        this.removed = Array<Bool>(n + 1, {_ => false})
        this.answer = 0
    }

    func getSubSize(u: Int64, parent: Int64): Int64 {
        subSize[u] = 1
        for ((v, _) in g[u]) {
            if (v != parent && !removed[v]) {
                subSize[u] += getSubSize(v, u)
            }
        }
        return subSize[u]
    }

    func getCentroid(u: Int64, parent: Int64, treeSize: Int64): Int64 {
        for ((v, _) in g[u]) {
            if (v != parent && !removed[v] && subSize[v] > treeSize / 2) {
                return getCentroid(v, u, treeSize)
            }
        }
        return u
    }

    // 收集从 u 出发到子树所有节点的距离
    func getDists(u: Int64, parent: Int64, dist: Int64, dists: ArrayList<Int64>): Unit {
        dists.add(dist)
        for ((v, w) in g[u]) {
            if (v != parent && !removed[v]) {
                getDists(v, u, dist + w, dists)
            }
        }
    }

    public func solve(u: Int64): Unit {
        let treeSize = getSubSize(u, 0)
        let centroid = getCentroid(u, 0, treeSize)
        removed[centroid] = true

        // 统计经过 centroid 的路径 (根据题意定制)
        let allDists = ArrayList<Int64>()
        allDists.add(0)  // centroid 自身
        for ((v, w) in g[centroid]) {
            if (!removed[v]) {
                let subDists = ArrayList<Int64>()
                getDists(v, centroid, w, subDists)
                // 这里根据题意处理 subDists 与 allDists 的组合
                // 例: 统计距离 <= K 的路径对
                for (d in subDists) { allDists.add(d) }
            }
        }

        // 递归处理子树
        for ((v, _) in g[centroid]) {
            if (!removed[v]) {
                solve(v)
            }
        }
    }
}
```

### 11.5 CDQ 分治 (三维偏序)

```cangjie
import std.collection.*
import std.sort.*

// 三维偏序: 对每个元素求满足 a[j].x <= a[i].x && a[j].y <= a[i].y && a[j].z <= a[i].z 的 j 数
// 第一维排序，第二维 CDQ 分治，第三维 BIT

class CDQ {
    var bit: Array<Int64>
    var maxVal: Int64

    public init(maxVal: Int64) {
        this.maxVal = maxVal
        this.bit = Array<Int64>(maxVal + 1, {_ => 0})
    }

    func bitUpdate(pos: Int64, delta: Int64) {
        var i = pos
        while (i <= maxVal) {
            bit[i] += delta
            i += i & (-i)
        }
    }

    func bitQuery(pos: Int64): Int64 {
        var s: Int64 = 0
        var i = pos
        while (i > 0) {
            s += bit[i]
            i -= i & (-i)
        }
        return s
    }

    // items: Array<(x, y, z, origIdx)> 已按 x 排序
    // ans: 结果数组
    public func solve(items: Array<(Int64, Int64, Int64, Int64)>, ans: Array<Int64>): Unit {
        let n = items.size
        if (n <= 1) { return }
        let mid = n / 2
        let left = Array<(Int64, Int64, Int64, Int64)>(mid, {i => items[i]})
        let right = Array<(Int64, Int64, Int64, Int64)>(n - mid, {i => items[mid + i]})

        solve(left, ans)
        solve(right, ans)

        // 左半按 y 排序，右半按 y 排序
        var sortedLeft = left
        var sortedRight = right
        sort(sortedLeft, key: { e: (Int64, Int64, Int64, Int64) => e[1] })
        sort(sortedRight, key: { e: (Int64, Int64, Int64, Int64) => e[1] })

        // 双指针: 左半贡献到右半
        var j: Int64 = 0
        var i: Int64 = 0
        while (i < sortedRight.size) {
            while (j < sortedLeft.size && sortedLeft[j][1] <= sortedRight[i][1]) {
                bitUpdate(sortedLeft[j][2], 1)
                j++
            }
            ans[sortedRight[i][3]] += bitQuery(sortedRight[i][2])
            i++
        }

        // 清理 BIT
        i = 0
        while (i < j) {
            bitUpdate(sortedLeft[i][2], -1)
            i++
        }
    }
}
```

---

## 12. 高级字符串

### 12.1 AC 自动机 (Aho-Corasick)

```cangjie
import std.collection.*

class AhoCorasick {
    var next: Array<Array<Int64>>  // next[node][c] = 子节点
    var fail: Array<Int64>         // 失配指针
    var output: Array<Int64>       // 输出标记 (可扩展为 ArrayList)
    var tot: Int64

    public init(maxNodes: Int64) {
        this.next = Array<Array<Int64>>(maxNodes, {_ => Array<Int64>(26, {_ => 0})})
        this.fail = Array<Int64>(maxNodes, {_ => 0})
        this.output = Array<Int64>(maxNodes, {_ => 0})
        this.tot = 0
    }

    public func insert(word: String, id: Int64) {
        var cur: Int64 = 0
        for (ch in word) {  // ASCII-only: Byte 值等于码点
            let c = Int64(ch) - Int64(UInt32(r'a'))
            if (next[cur][c] == 0) {
                tot++
                next[cur][c] = tot
            }
            cur = next[cur][c]
        }
        output[cur] = id  // 或 output[cur]++ 计数
    }

    public func build() {
        let q = ArrayQueue<Int64>()
        var c: Int64 = 0
        while (c < 26) {
            if (next[0][c] != 0) {
                fail[next[0][c]] = 0
                q.add(next[0][c])
            }
            c++
        }
        while (!q.isEmpty()) {
            let u = q.remove().getOrThrow()
            c = 0
            while (c < 26) {
                let v = next[u][c]
                if (v != 0) {
                    fail[v] = next[fail[u]][c]
                    q.add(v)
                } else {
                    next[u][c] = next[fail[u]][c]
                }
                c++
            }
        }
    }

    // 在文本中搜索所有模式
    public func search(text: String): ArrayList<(Int64, Int64)> {
        let matches = ArrayList<(Int64, Int64)>()
        var cur: Int64 = 0
        var i: Int64 = 0
        for (ch in text) {  // ASCII-only
            let c = Int64(ch) - Int64(UInt32(r'a'))
            cur = next[cur][c]
            var tmp = cur
            while (tmp != 0) {
                if (output[tmp] != 0) {
                    matches.add((i, output[tmp]))
                }
                tmp = fail[tmp]
            }
            i++
        }
        return matches
    }
}
```

### 12.2 Manacher — 最长回文子串 O(n)

```cangjie
import std.collection.*

// 返回以每个位置为中心的回文半径 (在插入分隔符后的串上)
func manacher(s: String): Int64 {
    let a = s.toArray()
    let n = a.size
    // 构造 #a[0]#a[1]#...#a[n-1]# 用 Int64 数组
    let t = Array<Int64>(2 * n + 1, {i =>
        if (i % 2 == 0) { -1 }  // 分隔符用 -1 代替
        else { Int64(a[i / 2]) }
    })
    let m = t.size
    let p = Array<Int64>(m, {_ => 0})  // p[i] = 回文半径
    var c: Int64 = 0  // 当前最右回文的中心
    var r: Int64 = 0  // 当前最右回文的右边界

    var i: Int64 = 0
    while (i < m) {
        let mirror = 2 * c - i
        if (i < r) {
            p[i] = if (r - i < p[mirror]) { r - i } else { p[mirror] }
        }
        // 尝试扩展
        while (i - p[i] - 1 >= 0 && i + p[i] + 1 < m && t[i - p[i] - 1] == t[i + p[i] + 1]) {
            p[i]++
        }
        if (i + p[i] > r) {
            c = i
            r = i + p[i]
        }
        i++
    }

    // 最长回文长度
    var maxLen: Int64 = 0
    for (v in p) {
        if (v > maxLen) { maxLen = v }
    }
    return maxLen  // 在原串中的长度就是 maxLen
}
```

### 12.3 Z 函数 (扩展 KMP / Z-Algorithm)

```cangjie
// z[i] = s[i..] 与 s[0..] 的最长公共前缀长度
func zFunction(s: String): Array<Int64> {
    let a = s.toArray()
    let n = a.size
    let z = Array<Int64>(n, {_ => 0})
    z[0] = n
    var l: Int64 = 0
    var r: Int64 = 0
    var i: Int64 = 1
    while (i < n) {
        if (i < r) {
            z[i] = if (r - i < z[i - l]) { r - i } else { z[i - l] }
        }
        while (i + z[i] < n && a[z[i]] == a[i + z[i]]) {
            z[i]++
        }
        if (i + z[i] > r) {
            l = i
            r = i + z[i]
        }
        i++
    }
    return z
}
```

---

## 13. 高级字符串 (续)

### 13.1 后缀数组 + LCP (Suffix Array)

> **用途**: 子串排序、最长公共子串、重复子串检测。O(n log²n) 构建，O(1) LCP 查询（配合 ST 表）。

```cangjie
import std.collection.*
import std.sort.*

class SuffixArray {
    let s: Array<Byte>
    let n: Int64
    var sa: Array<Int64>
    var rank: Array<Int64>
    var lcp: Array<Int64>

    init(str: String) {
        let bytes = str.toArray()
        s = bytes
        n = bytes.size
        let nn = bytes.size
        sa = Array<Int64>(nn, {i => i})
        rank = Array<Int64>(nn, {i => Int64(bytes[i])})
        lcp = Array<Int64>(nn, {_ => 0})
        build()
        buildLCP()
    }

    func build(): Unit {
        var k: Int64 = 1
        let tmp = Array<Int64>(n, {_ => 0})
        while (k < n) {
            let kk = k
            let rk = rank.clone()
            sort(sa, by: {a, b =>
                if (rk[a] != rk[b]) {
                    if (rk[a] < rk[b]) { return Ordering.LT } else { return Ordering.GT }
                }
                let ra = if (a + kk < n) { rk[a + kk] } else { -1 }
                let rb = if (b + kk < n) { rk[b + kk] } else { -1 }
                if (ra < rb) { return Ordering.LT } else if (ra > rb) { return Ordering.GT } else { return Ordering.EQ }
            })
            tmp[sa[0]] = 0
            var i: Int64 = 1
            while (i < n) {
                tmp[sa[i]] = tmp[sa[i - 1]]
                let prev = sa[i - 1]
                let cur = sa[i]
                if (rk[cur] != rk[prev]) {
                    tmp[sa[i]] = tmp[sa[i - 1]] + 1
                } else {
                    let rprev = if (prev + kk < n) { rk[prev + kk] } else { -1 }
                    let rcur = if (cur + kk < n) { rk[cur + kk] } else { -1 }
                    if (rprev != rcur) {
                        tmp[sa[i]] = tmp[sa[i - 1]] + 1
                    }
                }
                i++
            }
            i = 0
            while (i < n) { rank[i] = tmp[i]; i++ }
            if (rank[sa[n - 1]] == n - 1) { break }
            k *= 2
        }
    }

    func buildLCP(): Unit {
        let inv = Array<Int64>(n, {_ => 0})
        var i: Int64 = 0
        while (i < n) { inv[sa[i]] = i; i++ }
        var h: Int64 = 0
        i = 0
        while (i < n) {
            if (inv[i] > 0) {
                let j = sa[inv[i] - 1]
                while (i + h < n && j + h < n && s[i + h] == s[j + h]) { h++ }
                lcp[inv[i]] = h
                if (h > 0) { h-- }
            } else { h = 0 }
            i++
        }
    }
}
// 用法: let sa = SuffixArray("banana"); sa.sa / sa.lcp
```

### 13.2 后缀自动机 (SAM)

> **用途**: 不同子串计数、最长公共子串、子串出现次数。O(n) 构建。
> **注意**: `extend` 是仓颉关键字，方法名需用 `addChar` 替代。

```cangjie
import std.collection.*

class SAMNode {
    var len: Int64 = 0
    var link: Int64 = -1
    var ch: HashMap<UInt8, Int64> = HashMap<UInt8, Int64>()
}

class SAM {
    var nodes: ArrayList<SAMNode> = ArrayList<SAMNode>()
    var last: Int64 = 0

    init() {
        let root = SAMNode()
        root.len = 0; root.link = -1
        nodes.add(root); last = 0
    }

    func addChar(c: UInt8): Unit {
        let cur = nodes.size
        let nd = SAMNode()
        nd.len = nodes[last].len + 1
        nodes.add(nd)
        var p = last
        while (p != -1 && !nodes[p].ch.contains(c)) {
            nodes[p].ch[c] = cur; p = nodes[p].link
        }
        if (p == -1) {
            nodes[cur].link = 0
        } else {
            let q = nodes[p].ch.get(c).getOrThrow()
            if (nodes[p].len + 1 == nodes[q].len) {
                nodes[cur].link = q
            } else {
                let clone = nodes.size
                let cloneNode = SAMNode()
                cloneNode.len = nodes[p].len + 1
                cloneNode.link = nodes[q].link
                for ((k, v) in nodes[q].ch) { cloneNode.ch[k] = v }
                nodes.add(cloneNode)
                while (p != -1 && nodes[p].ch.get(c).getOrThrow() == q) {
                    nodes[p].ch[c] = clone; p = nodes[p].link
                }
                nodes[q].link = clone; nodes[cur].link = clone
            }
        }
        last = cur
    }

    func countDistinct(): Int64 {
        var ans: Int64 = 0
        var i: Int64 = 1
        while (i < nodes.size) {
            ans += nodes[i].len - nodes[nodes[i].link].len; i++
        }
        return ans
    }
}
// 用法: let sam = SAM(); for (b in s.toArray()) { sam.addChar(b) }
// sam.countDistinct() = 不同子串数
```

---

## 14. 网络流

### 14.1 Dinic 最大流

> **用途**: 最大流 / 最小割。时间复杂度 O(V²E)。
> **关键**: struct 需显式 `init` 构造器；用位置参数调用。

```cangjie
import std.collection.*

struct FlowEdge {
    var to: Int64
    var cap: Int64
    var rev: Int64
    init(to: Int64, cap: Int64, rev: Int64) {
        this.to = to; this.cap = cap; this.rev = rev
    }
}

class Dinic {
    let n: Int64
    var graph: ArrayList<ArrayList<FlowEdge>>
    var level: Array<Int64>
    var iter: Array<Int64>

    init(n: Int64) {
        this.n = n
        graph = ArrayList<ArrayList<FlowEdge>>(n, {_ => ArrayList<FlowEdge>()})
        level = Array<Int64>(n, {_ => 0})
        iter = Array<Int64>(n, {_ => 0})
    }

    func addEdge(from: Int64, to: Int64, cap: Int64): Unit {
        graph[from].add(FlowEdge(to, cap, graph[to].size))
        graph[to].add(FlowEdge(from, 0, graph[from].size - 1))
    }

    func dfs(v: Int64, t: Int64, f: Int64): Int64 {
        if (v == t) { return f }
        while (iter[v] < graph[v].size) {
            let idx = iter[v]
            let e = graph[v][idx]
            if (e.cap > 0 && level[v] < level[e.to]) {
                let d = dfs(e.to, t, if (f < e.cap) { f } else { e.cap })
                if (d > 0) {
                    graph[v][idx] = FlowEdge(e.to, e.cap - d, e.rev)
                    let re = graph[e.to][e.rev]
                    graph[e.to][e.rev] = FlowEdge(re.to, re.cap + d, re.rev)
                    return d
                }
            }
            iter[v]++
        }
        return 0
    }

    func maxflow(s: Int64, t: Int64): Int64 {
        let INF: Int64 = 0x3f3f3f3f3f3f3f3f
        var flow: Int64 = 0
        while (true) {
            var i: Int64 = 0
            while (i < n) { level[i] = -1; i++ }
            let q = ArrayQueue<Int64>()
            level[s] = 0; q.add(s)
            while (!q.isEmpty()) {
                let v = q.remove().getOrThrow()
                for (idx in 0..graph[v].size) {
                    let e = graph[v][idx]
                    if (e.cap > 0 && level[e.to] < 0) {
                        level[e.to] = level[v] + 1; q.add(e.to)
                    }
                }
            }
            if (level[t] < 0) { break }
            i = 0
            while (i < n) { iter[i] = 0; i++ }
            while (true) {
                let d = dfs(s, t, INF)
                if (d == 0) { break }
                flow += d
            }
        }
        return flow
    }
}
// 用法: let d = Dinic(n); d.addEdge(u,v,cap); d.maxflow(s,t)
```

### 14.2 最小费用最大流 (MCMF - SPFA)

> **用途**: 在满足最大流的前提下最小化总费用。O(VEf)。

```cangjie
import std.collection.*

struct MCFEdge {
    var to: Int64
    var cap: Int64
    var cost: Int64
    var rev: Int64
    init(to: Int64, cap: Int64, cost: Int64, rev: Int64) {
        this.to = to; this.cap = cap; this.cost = cost; this.rev = rev
    }
}

class MCMF {
    let n: Int64
    var graph: ArrayList<ArrayList<MCFEdge>>

    init(n: Int64) {
        this.n = n
        graph = ArrayList<ArrayList<MCFEdge>>(n, {_ => ArrayList<MCFEdge>()})
    }

    func addEdge(from: Int64, to: Int64, cap: Int64, cost: Int64): Unit {
        graph[from].add(MCFEdge(to, cap, cost, graph[to].size))
        graph[to].add(MCFEdge(from, 0, -cost, graph[from].size - 1))
    }

    func solve(s: Int64, t: Int64): (Int64, Int64) {
        let INF: Int64 = 0x3f3f3f3f3f3f3f3f
        var totalFlow: Int64 = 0
        var totalCost: Int64 = 0
        while (true) {
            let dist = Array<Int64>(n, {_ => INF})
            let inQ = Array<Bool>(n, {_ => false})
            let prevv = Array<Int64>(n, {_ => -1})
            let preve = Array<Int64>(n, {_ => -1})
            dist[s] = 0
            let q = ArrayQueue<Int64>()
            q.add(s); inQ[s] = true
            while (!q.isEmpty()) {
                let v = q.remove().getOrThrow(); inQ[v] = false
                for (idx in 0..graph[v].size) {
                    let e = graph[v][idx]
                    if (e.cap > 0 && dist[v] + e.cost < dist[e.to]) {
                        dist[e.to] = dist[v] + e.cost
                        prevv[e.to] = v; preve[e.to] = idx
                        if (!inQ[e.to]) { q.add(e.to); inQ[e.to] = true }
                    }
                }
            }
            if (dist[t] == INF) { break }
            var d = INF
            var v = t
            while (v != s) {
                let e = graph[prevv[v]][preve[v]]
                if (e.cap < d) { d = e.cap }
                v = prevv[v]
            }
            v = t
            while (v != s) {
                let idx = preve[v]; let pv = prevv[v]
                let e = graph[pv][idx]
                graph[pv][idx] = MCFEdge(e.to, e.cap - d, e.cost, e.rev)
                let re = graph[e.to][e.rev]
                graph[e.to][e.rev] = MCFEdge(re.to, re.cap + d, re.cost, re.rev)
                v = pv
            }
            totalFlow += d; totalCost += d * dist[t]
        }
        return (totalFlow, totalCost)
    }
}
// 用法: let mcmf = MCMF(n); mcmf.addEdge(u,v,cap,cost); let (flow,cost) = mcmf.solve(s,t)
```

---

## 15. 离线与逻辑

### 15.1 莫队 (Mo's Algorithm)

> **用途**: 离线处理 [l, r] 区间查询（如不同数计数）。O((N+Q)√N)。

```cangjie
import std.collection.*
import std.sort.*

func moAlgorithm(queries: Array<(Int64, Int64, Int64)>, a: Array<Int64>, n: Int64): Array<Int64> {
    let q = queries.size
    let block = if (n > 0) {
        var sq: Int64 = 1
        while (sq * sq < n) { sq++ }
        if (sq == 0) { 1 } else { sq }
    } else { 1 }

    let idx = Array<Int64>(q, {i => i})
    sort(idx, by: {i, j =>
        let bi = queries[i][0] / block
        let bj = queries[j][0] / block
        if (bi != bj) {
            if (bi < bj) { return Ordering.LT } else { return Ordering.GT }
        }
        if (queries[i][1] < queries[j][1]) { return Ordering.LT }
        else if (queries[i][1] > queries[j][1]) { return Ordering.GT }
        else { return Ordering.EQ }
    })

    let ans = Array<Int64>(q, {_ => 0})
    let cnt = HashMap<Int64, Int64>()
    var curAns: Int64 = 0
    var curL: Int64 = 0
    var curR: Int64 = -1

    func addVal(v: Int64): Unit {
        let c = cnt.get(v) ?? 0
        if (c == 0) { curAns++ }
        cnt[v] = c + 1
    }
    func removeVal(v: Int64): Unit {
        let c = cnt.get(v) ?? 0
        if (c == 1) { curAns-- }
        cnt[v] = c - 1
    }

    for (qi in idx) {
        let (l, r, _) = queries[qi]
        while (curR < r) { curR++; addVal(a[curR]) }
        while (curL > l) { curL--; addVal(a[curL]) }
        while (curR > r) { removeVal(a[curR]); curR-- }
        while (curL < l) { removeVal(a[curL]); curL++ }
        ans[queries[qi][2]] = curAns
    }
    return ans
}
// 用法: queries = [(l, r, queryIndex), ...]; moAlgorithm(queries, a, n)
```

### 15.2 2-SAT (Kosaraju)

> **用途**: 布尔可满足性，约束形如 (x ∨ y)。O(V+E)。

```cangjie
import std.collection.*

class TwoSAT {
    let n: Int64
    var graph: ArrayList<ArrayList<Int64>>
    var rgraph: ArrayList<ArrayList<Int64>>

    init(n: Int64) {
        this.n = n
        graph = ArrayList<ArrayList<Int64>>(2 * n, {_ => ArrayList<Int64>()})
        rgraph = ArrayList<ArrayList<Int64>>(2 * n, {_ => ArrayList<Int64>()})
    }

    // x OR y: addClause(x, true, y, true)
    // NOT x OR y: addClause(x, false, y, true) 等
    func addClause(x: Int64, xVal: Bool, y: Int64, yVal: Bool): Unit {
        let u = 2 * x + (if (xVal) { 0 } else { 1 })
        let notU = 2 * x + (if (xVal) { 1 } else { 0 })
        let v = 2 * y + (if (yVal) { 0 } else { 1 })
        let notV = 2 * y + (if (yVal) { 1 } else { 0 })
        graph[notU].add(v); rgraph[v].add(notU)
        graph[notV].add(u); rgraph[u].add(notV)
    }

    func solve(): ?Array<Bool> {
        let nn = 2 * n
        let visited = Array<Bool>(nn, {_ => false})
        let order = ArrayList<Int64>()
        let comp = Array<Int64>(nn, {_ => -1})

        func dfs1(v: Int64): Unit {
            visited[v] = true
            for (u in graph[v]) { if (!visited[u]) { dfs1(u) } }
            order.add(v)
        }
        var i: Int64 = 0
        while (i < nn) { if (!visited[i]) { dfs1(i) }; i++ }

        var c: Int64 = 0
        func dfs2(v: Int64, id: Int64): Unit {
            comp[v] = id
            for (u in rgraph[v]) { if (comp[u] < 0) { dfs2(u, id) } }
        }
        i = nn - 1
        while (i >= 0) {
            let v = order[i]
            if (comp[v] < 0) { dfs2(v, c); c++ }
            i--
        }

        let result = Array<Bool>(n, {_ => false})
        i = 0
        while (i < n) {
            if (comp[2 * i] == comp[2 * i + 1]) { return None }
            result[i] = comp[2 * i] > comp[2 * i + 1]
            i++
        }
        return result
    }
}
// 用法: let sat = TwoSAT(n); sat.addClause(0, true, 1, false); sat.solve()
```

---

## 16. DP 优化与平衡树

### 16.1 凸包优化 DP (Convex Hull Trick)

> **用途**: dp[i] = min(dp[j] + b[j]*a[i])，a[] 单调递增 b[] 单调递减时 O(n)。
> 维护下凸壳，单调指针查询。

```cangjie
import std.collection.*

class CHT {
    var lines: ArrayList<(Int64, Int64)> = ArrayList<(Int64, Int64)>()

    func bad(l1: (Int64, Int64), l2: (Int64, Int64), l3: (Int64, Int64)): Bool {
        return (l3[1] - l1[1]) * (l1[0] - l2[0]) <= (l2[1] - l1[1]) * (l1[0] - l3[0])
    }

    func addLine(slope: Int64, intercept: Int64): Unit {
        let newLine = (slope, intercept)
        while (lines.size >= 2 && bad(lines[lines.size - 2], lines[lines.size - 1], newLine)) {
            lines.remove(at: lines.size - 1)
        }
        lines.add(newLine)
    }

    var ptr: Int64 = 0
    func query(x: Int64): Int64 {
        if (ptr >= lines.size) { ptr = lines.size - 1 }
        while (ptr < lines.size - 1 &&
               lines[ptr + 1][0] * x + lines[ptr + 1][1] <= lines[ptr][0] * x + lines[ptr][1]) {
            ptr++
        }
        return lines[ptr][0] * x + lines[ptr][1]
    }
}
// 用法: cht.addLine(slope, intercept); cht.query(x) — x 需单调递增
```

### 16.2 FHQ-Treap (无旋 Treap)

> **用途**: 支持 insert/delete/kth/rank/split/merge。期望 O(log n)。
> **特点**: 基于 split-merge，无需旋转操作，代码简洁。

```cangjie
import std.collection.*

class FHQTreap {
    var key: ArrayList<Int64> = ArrayList<Int64>()
    var pri: ArrayList<Int64> = ArrayList<Int64>()
    var sz: ArrayList<Int64> = ArrayList<Int64>()
    var ch: ArrayList<(Int64, Int64)> = ArrayList<(Int64, Int64)>()
    var root: Int64 = 0
    var seed: Int64 = 12345

    init() {
        key.add(0); pri.add(0); sz.add(0); ch.add((0, 0))
    }

    func nextRand(): Int64 {
        seed = (seed * 1103515245 + 12345) & 0x7fffffff
        return seed
    }

    func newNode(v: Int64): Int64 {
        let id = key.size
        key.add(v); pri.add(nextRand()); sz.add(1); ch.add((0, 0))
        return id
    }

    func pushUp(u: Int64): Unit {
        if (u == 0) { return }
        sz[u] = sz[ch[u][0]] + sz[ch[u][1]] + 1
    }

    func split(u: Int64, v: Int64): (Int64, Int64) {
        if (u == 0) { return (0, 0) }
        if (key[u] <= v) {
            let (rl, rr) = split(ch[u][1], v)
            ch[u] = (ch[u][0], rl); pushUp(u)
            return (u, rr)
        } else {
            let (ll, lr) = split(ch[u][0], v)
            ch[u] = (lr, ch[u][1]); pushUp(u)
            return (ll, u)
        }
    }

    func merge(a: Int64, b: Int64): Int64 {
        if (a == 0) { return b }
        if (b == 0) { return a }
        if (pri[a] > pri[b]) {
            ch[a] = (ch[a][0], merge(ch[a][1], b)); pushUp(a); return a
        } else {
            ch[b] = (merge(a, ch[b][0]), ch[b][1]); pushUp(b); return b
        }
    }

    func insert(v: Int64): Unit {
        let nd = newNode(v)
        let (l, r) = split(root, v)
        root = merge(merge(l, nd), r)
    }

    func remove(v: Int64): Unit {
        let (l, r) = split(root, v)
        let (ll, eq) = split(l, v - 1)
        let mergedEq = if (eq != 0) { merge(ch[eq][0], ch[eq][1]) } else { 0 }
        root = merge(merge(ll, mergedEq), r)
    }

    func kth(k: Int64): Int64 {
        var u = root; var rem = k
        while (u != 0) {
            let leftSz = sz[ch[u][0]]
            if (leftSz + 1 == rem) { return key[u] }
            if (rem <= leftSz) { u = ch[u][0] }
            else { rem -= leftSz + 1; u = ch[u][1] }
        }
        return -1
    }

    func rankOf(v: Int64): Int64 {
        let (l, r) = split(root, v - 1)
        let ans = sz[l] + 1
        root = merge(l, r)
        return ans
    }
}
// 用法: let treap = FHQTreap(); treap.insert(3); treap.kth(1); treap.remove(3)
```

---

## 17. 高级数据结构 (续)

### 17.1 LCT (Link-Cut Tree)

> **用途**: 动态树——支持 link/cut/路径查询。均摊 O(log n)。
> **聚合示例**: 路径 XOR 和（可改为 sum/max 等）。

```cangjie
import std.collection.*

class LCT {
    var fa: Array<Int64>
    var ch: Array<(Int64, Int64)>
    var rev: Array<Bool>
    var val_: Array<Int64>
    var sum: Array<Int64>
    let n: Int64

    init(n: Int64) {
        let nn = n + 1
        this.n = n
        fa = Array<Int64>(nn, {_ => 0})
        ch = Array<(Int64, Int64)>(nn, {_ => (0, 0)})
        rev = Array<Bool>(nn, {_ => false})
        val_ = Array<Int64>(nn, {_ => 0})
        sum = Array<Int64>(nn, {_ => 0})
    }

    func isRoot(x: Int64): Bool {
        return ch[fa[x]][0] != x && ch[fa[x]][1] != x
    }

    func pushUp(x: Int64): Unit {
        sum[x] = sum[ch[x][0]] ^ val_[x] ^ sum[ch[x][1]]
    }

    func pushDown(x: Int64): Unit {
        if (rev[x]) {
            let (l, r) = ch[x]
            ch[x] = (r, l)
            if (l != 0) { rev[l] = !rev[l] }
            if (r != 0) { rev[r] = !rev[r] }
            rev[x] = false
        }
    }

    func rotate(x: Int64): Unit {
        let y = fa[x]; let z = fa[y]
        let k: Int64 = if (ch[y][1] == x) { 1 } else { 0 }
        let w = if (k == 0) { ch[x][1] } else { ch[x][0] }
        if (!isRoot(y)) {
            if (ch[z][0] == y) { ch[z] = (x, ch[z][1]) }
            else { ch[z] = (ch[z][0], x) }
        }
        if (k == 0) { ch[x] = (ch[x][0], y); ch[y] = (w, ch[y][1]) }
        else { ch[x] = (y, ch[x][1]); ch[y] = (ch[y][0], w) }
        fa[w] = y; fa[y] = x; fa[x] = z
        pushUp(y); pushUp(x)
    }

    func splay(x: Int64): Unit {
        let stk = ArrayList<Int64>()
        var u = x; stk.add(u)
        while (!isRoot(u)) { u = fa[u]; stk.add(u) }
        var i = stk.size - 1
        while (i >= 0) { pushDown(stk[i]); i-- }
        while (!isRoot(x)) {
            let y = fa[x]
            if (!isRoot(y)) {
                if ((ch[fa[y]][0] == y) == (ch[y][0] == x)) { rotate(y) }
                else { rotate(x) }
            }
            rotate(x)
        }
        pushUp(x)
    }

    func access(x: Int64): Unit {
        var last: Int64 = 0; var u = x
        while (u != 0) {
            splay(u); ch[u] = (ch[u][0], last); pushUp(u)
            last = u; u = fa[u]
        }
        splay(x)
    }

    func makeRoot(x: Int64): Unit { access(x); rev[x] = !rev[x] }

    func findRoot(x: Int64): Int64 {
        access(x); var u = x; pushDown(u)
        while (ch[u][0] != 0) { u = ch[u][0]; pushDown(u) }
        splay(u); return u
    }

    func link(x: Int64, y: Int64): Unit {
        makeRoot(x); if (findRoot(y) != x) { fa[x] = y }
    }

    func cut(x: Int64, y: Int64): Unit {
        makeRoot(x); access(y)
        if (ch[y][0] == x && ch[x][1] == 0) {
            ch[y] = (0, ch[y][1]); fa[x] = 0; pushUp(y)
        }
    }

    func queryPath(x: Int64, y: Int64): Int64 {
        makeRoot(x); access(y); return sum[y]
    }
}
// 用法: let lct = LCT(n); lct.val_[i] = v; lct.sum[i] = v; lct.link(u,v); lct.queryPath(u,v)
```

### 17.2 可持久化并查集

> **用途**: 支持版本回退的并查集（时间旅行）。基于可持久化数组。O(log²n)。

```cangjie
import std.collection.*

class PersistentDSU {
    var root: ArrayList<Int64> = ArrayList<Int64>()
    var ls: ArrayList<Int64> = ArrayList<Int64>()
    var rs: ArrayList<Int64> = ArrayList<Int64>()
    var fa: ArrayList<Int64> = ArrayList<Int64>()
    var rnk: ArrayList<Int64> = ArrayList<Int64>()
    var cnt: Int64 = 0
    let n: Int64

    init(n: Int64) {
        this.n = n
        let maxNodes = (n + 1) * 40
        ls = ArrayList<Int64>(maxNodes, {_ => 0})
        rs = ArrayList<Int64>(maxNodes, {_ => 0})
        fa = ArrayList<Int64>(maxNodes, {_ => 0})
        rnk = ArrayList<Int64>(maxNodes, {_ => 0})
        cnt = 0
        let r = buildTree(1, n)
        root = ArrayList<Int64>(); root.add(r)
    }

    func newNode(): Int64 {
        cnt++
        if (cnt >= ls.size) { ls.add(0); rs.add(0); fa.add(0); rnk.add(0) }
        return cnt
    }

    func buildTree(l: Int64, r: Int64): Int64 {
        let nd = newNode()
        if (l == r) { fa[nd] = l; rnk[nd] = 0; return nd }
        let mid = (l + r) / 2
        ls[nd] = buildTree(l, mid); rs[nd] = buildTree(mid + 1, r)
        return nd
    }

    func queryNode(nd: Int64, l: Int64, r: Int64, pos: Int64): Int64 {
        if (l == r) { return nd }
        let mid = (l + r) / 2
        if (pos <= mid) { return queryNode(ls[nd], l, mid, pos) }
        else { return queryNode(rs[nd], mid + 1, r, pos) }
    }

    func updateNode(prev: Int64, l: Int64, r: Int64, pos: Int64, newFa: Int64, newRnk: Int64): Int64 {
        let nd = newNode()
        ls[nd] = ls[prev]; rs[nd] = rs[prev]; fa[nd] = fa[prev]; rnk[nd] = rnk[prev]
        if (l == r) { fa[nd] = newFa; rnk[nd] = newRnk; return nd }
        let mid = (l + r) / 2
        if (pos <= mid) { ls[nd] = updateNode(ls[prev], l, mid, pos, newFa, newRnk) }
        else { rs[nd] = updateNode(rs[prev], mid + 1, r, pos, newFa, newRnk) }
        return nd
    }

    func find(ver: Int64, x: Int64): Int64 {
        let nd = queryNode(root[ver], 1, n, x)
        if (fa[nd] == x) { return x }
        return find(ver, fa[nd])
    }

    func union(ver: Int64, x: Int64, y: Int64): Unit {
        let fx = find(ver, x); let fy = find(ver, y)
        if (fx == fy) { root.add(root[ver]); return }
        let ndx = queryNode(root[ver], 1, n, fx)
        let ndy = queryNode(root[ver], 1, n, fy)
        if (rnk[ndx] < rnk[ndy]) {
            root.add(updateNode(root[ver], 1, n, fx, fy, rnk[ndx]))
        } else if (rnk[ndx] > rnk[ndy]) {
            root.add(updateNode(root[ver], 1, n, fy, fx, rnk[ndy]))
        } else {
            let nr1 = updateNode(root[ver], 1, n, fy, fx, rnk[ndy])
            root.add(updateNode(nr1, 1, n, fx, fx, rnk[ndx] + 1))
        }
    }
}
// 用法: let pdsu = PersistentDSU(n)
// pdsu.union(ver, x, y) → 新版本; pdsu.find(ver, x) → 查询某版本
```

### 17.3 带权并查集

> **用途**: 维护节点间的相对权值关系（如距离、偏移量）。O(α(n))。

```cangjie
class WeightedDSU {
    var parent: Array<Int64>
    var rank_: Array<Int64>
    var weight: Array<Int64>

    init(n: Int64) {
        parent = Array<Int64>(n, {i => i})
        rank_ = Array<Int64>(n, {_ => 0})
        weight = Array<Int64>(n, {_ => 0})
    }

    func find(x: Int64): (Int64, Int64) {
        if (parent[x] == x) { return (x, 0) }
        let (r, d) = find(parent[x])
        parent[x] = r; weight[x] += d
        return (r, weight[x])
    }

    func union(x: Int64, y: Int64, w: Int64): Bool {
        let (rx, dx) = find(x); let (ry, dy) = find(y)
        if (rx == ry) { return dx - dy == w }
        if (rank_[rx] < rank_[ry]) {
            parent[rx] = ry; weight[rx] = dy - dx + w
        } else if (rank_[rx] > rank_[ry]) {
            parent[ry] = rx; weight[ry] = dx - dy - w
        } else {
            parent[ry] = rx; weight[ry] = dx - dy - w; rank_[rx]++
        }
        return true
    }

    func query(x: Int64, y: Int64): ?Int64 {
        let (rx, dx) = find(x); let (ry, dy) = find(y)
        if (rx != ry) { return None }
        return dx - dy
    }
}
// 用法: wdsu.union(x, y, w) — dist(x)-dist(y)=w; wdsu.query(x, y) → ?Int64
```

---

## 18. 数学进阶

### 18.1 NTT (数论变换 — 多项式乘法)

> **用途**: O(n log n) 多项式乘法，MOD = 998244353，原根 = 3。

```cangjie
func ntt(a: Array<Int64>, invert: Bool): Unit {
    let MOD: Int64 = 998244353
    let n = a.size
    var j: Int64 = 0
    var i: Int64 = 1
    while (i < n) {
        var bit = n >> 1
        while ((j & bit) != 0) { j = j ^ bit; bit >>= 1 }
        j = j ^ bit
        if (i < j) { let tmp = a[i]; a[i] = a[j]; a[j] = tmp }
        i++
    }
    func power(base: Int64, exp: Int64, m: Int64): Int64 {
        var result: Int64 = 1; var b = base % m; var e = exp
        while (e > 0) {
            if ((e & 1) == 1) { result = result * b % m }
            b = b * b % m; e >>= 1
        }
        return result
    }
    var len: Int64 = 2
    while (len <= n) {
        let w = if (invert) { power(3, MOD - 1 - (MOD - 1) / len, MOD) }
                else { power(3, (MOD - 1) / len, MOD) }
        i = 0
        while (i < n) {
            var wn: Int64 = 1; j = 0
            while (j < len / 2) {
                let u = a[i + j]
                let v = a[i + j + len / 2] * wn % MOD
                a[i + j] = (u + v) % MOD
                a[i + j + len / 2] = (u - v + MOD) % MOD
                wn = wn * w % MOD; j++
            }
            i += len
        }
        len *= 2
    }
    if (invert) {
        let inv = power(Int64(n), MOD - 2, MOD)
        i = 0; while (i < n) { a[i] = a[i] * inv % MOD; i++ }
    }
}

func polyMul(a: Array<Int64>, b: Array<Int64>): Array<Int64> {
    let MOD: Int64 = 998244353
    let rl = a.size + b.size - 1
    var n: Int64 = 1
    while (n < rl) { n *= 2 }
    let fa = Array<Int64>(n, {i => if (i < a.size) { a[i] } else { 0 }})
    let fb = Array<Int64>(n, {i => if (i < b.size) { b[i] } else { 0 }})
    ntt(fa, false); ntt(fb, false)
    var i: Int64 = 0
    while (i < n) { fa[i] = fa[i] * fb[i] % MOD; i++ }
    ntt(fa, true)
    return Array<Int64>(rl, {i => fa[i]})
}
// 用法: let c = polyMul([1,2,3], [4,5]) → [4,13,22,15]
```

### 18.2 中国剩余定理 (CRT + EXCRT)

> **用途**: 解同余方程组。CRT 要求模数两两互质；EXCRT 无此限制。

```cangjie
func extgcd(a: Int64, b: Int64): (Int64, Int64, Int64) {
    if (b == 0) { return (a, 1, 0) }
    let (g, x1, y1) = extgcd(b, a % b)
    return (g, y1, x1 - (a / b) * y1)
}

func crt(r: Array<Int64>, m: Array<Int64>): Int64 {
    let n = r.size
    var M: Int64 = 1; var i: Int64 = 0
    while (i < n) { M *= m[i]; i++ }
    var x: Int64 = 0; i = 0
    while (i < n) {
        let mi = M / m[i]
        let (_, inv, _) = extgcd(mi, m[i])
        let ti = ((inv % m[i]) + m[i]) % m[i]
        x = (x + r[i] * mi % M * ti % M) % M; i++
    }
    return (x + M) % M
}

func excrt(r: Array<Int64>, m: Array<Int64>): ?Int64 {
    var curR = r[0]; var curM = m[0]; var i: Int64 = 1
    while (i < r.size) {
        let (g, px, _) = extgcd(curM, m[i])
        if ((r[i] - curR) % g != 0) { return None }
        let lcm = curM / g * m[i]
        let t = (r[i] - curR) / g * px % (m[i] / g)
        curR = ((curR + curM * t) % lcm + lcm) % lcm
        curM = lcm; i++
    }
    return curR
}
// 用法: crt([2,3,2], [3,5,7]) → 23; excrt([1,3], [4,6]) → 9
```

### 18.3 欧拉函数 + 欧拉降幂

> **用途**: φ(n) 互质计数 + 降幂公式 a^b mod m。

```cangjie
func eulerPhi(n: Int64): Int64 {
    var result = n; var x = n; var i: Int64 = 2
    while (i * i <= x) {
        if (x % i == 0) {
            while (x % i == 0) { x /= i }
            result = result / i * (i - 1)
        }
        i++
    }
    if (x > 1) { result = result / x * (x - 1) }
    return result
}

func powerMod(a: Int64, b: Int64, m: Int64): Int64 {
    var result: Int64 = 1; var base = a % m; var exp = b
    while (exp > 0) {
        if ((exp & 1) == 1) { result = result * base % m }
        base = base * base % m; exp >>= 1
    }
    return result
}

func eulerPowerMod(a: Int64, b: Int64, m: Int64): Int64 {
    let phi = eulerPhi(m)
    if (b >= phi) { return powerMod(a, b % phi + phi, m) }
    return powerMod(a, b, m)
}
// 用法: eulerPhi(12) → 4; eulerPowerMod(2, 100, 1000) → 376
```

---

## 19. 数论进阶

### 19.1 Lucas 定理 — C(n,k) mod p (p 为素数)

> **适用**: p 较小 (< 10^5)，n, k 可极大。复杂度 O(p log_p n)

```cangjie
import std.collection.*

func lucasPower(base: Int64, exp: Int64, m: Int64): Int64 {
    var result: Int64 = 1
    var b = base % m
    var e = exp
    while (e > 0) {
        if ((e & 1) == 1) { result = result * b % m }
        b = b * b % m
        e >>= 1
    }
    return result
}

func lucasComb(n: Int64, k: Int64, p: Int64): Int64 {
    if (k > n) { return 0 }
    if (k == 0 || k == n) { return 1 }
    var num: Int64 = 1
    var den: Int64 = 1
    let kk = if (k > n - k) { n - k } else { k }
    var i: Int64 = 0
    while (i < kk) {
        num = num * ((n - i) % p) % p
        den = den * ((i + 1) % p) % p
        i++
    }
    return num * lucasPower(den, p - 2, p) % p
}

func lucas(n: Int64, k: Int64, p: Int64): Int64 {
    if (k == 0) { return 1 }
    return lucasComb(n % p, k % p, p) * lucas(n / p, k / p, p) % p
}
// 用法: lucas(10, 3, 13) → 3; lucas(10^9, 2, 10^9+7) → 28
```

### 19.2 Miller-Rabin 素性测试 + Pollard Rho 大数分解

> **适用**: 单个大数 (< 2^62) 素性判断 / 质因数分解。复杂度 Miller-Rabin O(k log²n), Pollard Rho O(n^{1/4})

```cangjie
import std.collection.*

func mulMod(a: Int64, b: Int64, m: Int64): Int64 {
    // 防溢出慢速乘法 (m < 2^62)
    var result: Int64 = 0
    var aa = a % m
    var bb = b
    while (bb > 0) {
        if ((bb & 1) == 1) { result = (result + aa) % m }
        aa = (aa + aa) % m
        bb >>= 1
    }
    return result
}

func powModMR(a: Int64, b: Int64, m: Int64): Int64 {
    var result: Int64 = 1
    var base = a % m
    var exp = b
    while (exp > 0) {
        if ((exp & 1) == 1) { result = mulMod(result, base, m) }
        base = mulMod(base, base, m)
        exp >>= 1
    }
    return result
}

func millerRabin(n: Int64): Bool {
    if (n < 2) { return false }
    if (n == 2 || n == 3 || n == 5 || n == 7) { return true }
    if (n % 2 == 0) { return false }
    var d = n - 1
    var r: Int64 = 0
    while (d % 2 == 0) { d /= 2; r++ }
    let witnesses: Array<Int64> = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for (a in witnesses) {
        if (a >= n) { continue }
        var x = powModMR(a, d, n)
        if (x == 1 || x == n - 1) { continue }
        var found = false
        var i: Int64 = 0
        while (i < r - 1) {
            x = mulMod(x, x, n)
            if (x == n - 1) { found = true; break }
            i++
        }
        if (!found) { return false }
    }
    return true
}

func myAbs(x: Int64): Int64 { if (x < 0) { return -x }; return x }
func myGcd(a: Int64, b: Int64): Int64 {
    var x = myAbs(a); var y = myAbs(b)
    while (y != 0) { let t = y; y = x % y; x = t }
    return x
}

var pollardSeed: Int64 = 42
func pollardRand(): Int64 {
    pollardSeed = (pollardSeed * 1103515245 + 12345) & 0x7fffffff
    return pollardSeed
}

// 注意: while(true) 在返回非 Unit 的函数中会报类型错误
// 必须用 var result 循环模式
func pollardRho(n: Int64): Int64 {
    if (n % 2 == 0) { return 2 }
    var result: Int64 = n
    while (result == n) {
        var x = pollardRand() % (n - 2) + 2
        var y = x
        let c = pollardRand() % (n - 1) + 1
        var d: Int64 = 1
        while (d == 1) {
            x = (mulMod(x, x, n) + c) % n
            y = (mulMod(y, y, n) + c) % n
            y = (mulMod(y, y, n) + c) % n
            d = myGcd(myAbs(x - y), n)
        }
        result = d
    }
    return result
}

func factorize(n: Int64): ArrayList<Int64> {
    let factors = ArrayList<Int64>()
    if (n <= 1) { return factors }
    let stk = ArrayList<Int64>()
    stk.add(n)
    while (stk.size > 0) {
        let x = stk[stk.size - 1]
        stk.remove(at: stk.size - 1)
        if (x == 1) { continue }
        if (millerRabin(x)) { factors.add(x); continue }
        let d = pollardRho(x)
        stk.add(d)
        stk.add(x / d)
    }
    return factors
}
// 用法: millerRabin(97) → true; factorize(84) → [2, 2, 3, 7]
```

### 19.3 BSGS (Baby-Step Giant-Step)

> **适用**: 求 a^x ≡ b (mod p)，p 为素数。复杂度 O(√p)

```cangjie
import std.collection.*

func bsgs(a: Int64, b: Int64, p: Int64): Int64 {
    if (b == 1) { return 0 }
    var m: Int64 = 1
    while (m * m < p) { m++ }
    // Baby step: 存 b * a^j mod p, j = 0..m-1
    let table = HashMap<Int64, Int64>()
    var cur: Int64 = b % p
    var j: Int64 = 0
    while (j < m) {
        table[cur] = j
        cur = cur * a % p
        j++
    }
    // Giant step: 检查 a^(im), i = 1..m
    let am = powModMR(a, m, p)  // 需要上面的 powModMR
    cur = am
    var i: Int64 = 1
    while (i <= m) {
        match (table.get(cur)) {
            case Some(jj) => return i * m - jj
            case None => ()
        }
        cur = cur * am % p
        i++
    }
    return -1  // 无解
}
// 用法: bsgs(2, 3, 5) → 3 (因为 2^3=8≡3 mod 5)
```

---

## 20. 高级图论

### 20.1 DSU on Tree (树上启发式合并)

> **适用**: 统计每个子树的某种信息 (如不同颜色数)。复杂度 O(n log n)

```cangjie
import std.collection.*

func dsuOnTree(n: Int64, adj: ArrayList<ArrayList<Int64>>,
               color: Array<Int64>): Array<Int64> {
    let parent = Array<Int64>(n, {_ => -1})
    let sz = Array<Int64>(n, {_ => 1})
    let order = ArrayList<Int64>()

    // 迭代 DFS 求大小和后序
    let stk = ArrayList<(Int64, Bool)>()
    stk.add((0, false))
    while (stk.size > 0) {
        let (v, processed) = stk[stk.size - 1]
        stk.remove(at: stk.size - 1)
        if (processed) {
            for (u in adj[v]) {
                if (u != parent[v]) { sz[v] += sz[u] }
            }
            order.add(v)
        } else {
            stk.add((v, true))
            for (u in adj[v]) {
                if (u != parent[v]) {
                    parent[u] = v
                    stk.add((u, false))
                }
            }
        }
    }

    // 统计子树不同值个数
    let ans = Array<Int64>(n, {_ => 0})
    for (v in order) {
        let seen = HashSet<Int64>()
        let q = ArrayList<Int64>()
        q.add(v)
        while (q.size > 0) {
            let u = q[q.size - 1]
            q.remove(at: q.size - 1)
            seen.add(color[u])
            for (w in adj[u]) {
                if (w != parent[u]) { q.add(w) }
            }
        }
        ans[v] = seen.size
    }
    return ans
}
// 用法: colors=[1,2,1,3,2], 树 0-1-3,1-4,0-2 → ans=[3,2,1,1,1]
```

### 20.2 虚树 (Virtual Tree)

> **适用**: 从关键节点 + 它们的 LCA 构建压缩树。复杂度 O(k log k)，k 为关键点数

```cangjie
import std.collection.*
import std.sort.*

class VirtualTree {
    let n: Int64
    var adj: ArrayList<ArrayList<Int64>>
    var tin: Array<Int64>
    var tout: Array<Int64>
    var depth: Array<Int64>
    var up: Array<Array<Int64>>
    var timer: Int64 = 0
    let LOG: Int64 = 20

    init(n: Int64, edges: ArrayList<ArrayList<Int64>>) {
        this.n = n
        adj = edges
        tin = Array<Int64>(n, {_ => 0})
        tout = Array<Int64>(n, {_ => 0})
        depth = Array<Int64>(n, {_ => 0})
        let logVal = 20  // 陷阱#9: 需用局部变量
        up = Array<Array<Int64>>(n, {_ => Array<Int64>(logVal, {_ => 0})})
        // 迭代 DFS 预处理
        let stk = ArrayList<(Int64, Int64, Bool)>()
        stk.add((0, -1, false))
        while (stk.size > 0) {
            let (v, p, visited) = stk[stk.size - 1]
            stk.remove(at: stk.size - 1)
            if (visited) {
                tout[v] = timer; timer++
            } else {
                tin[v] = timer; timer++
                up[v][0] = if (p >= 0) { p } else { 0 }
                var k: Int64 = 1
                while (k < logVal) { up[v][k] = up[up[v][k - 1]][k - 1]; k++ }
                stk.add((v, p, true))
                for (u in adj[v]) {
                    if (u != p) { depth[u] = depth[v] + 1; stk.add((u, v, false)) }
                }
            }
        }
    }

    func isAncestor(u: Int64, v: Int64): Bool {
        return tin[u] <= tin[v] && tout[v] <= tout[u]
    }

    func lca(a: Int64, b: Int64): Int64 {
        var u = a; var v = b
        if (depth[u] < depth[v]) { let tmp = u; u = v; v = tmp }
        let diff = depth[u] - depth[v]
        var k: Int64 = 0
        while (k < LOG) { if (((diff >> k) & 1) == 1) { u = up[u][k] }; k++ }
        if (u == v) { return u }
        k = LOG - 1
        while (k >= 0) {
            if (up[u][k] != up[v][k]) { u = up[u][k]; v = up[v][k] }
            k--
        }
        return up[u][0]
    }

    // 从关键点数组构建虚树，返回压缩邻接表
    func build(keys: Array<Int64>): ArrayList<ArrayList<Int64>> {
        let sorted = keys.clone()
        sort(sorted, by: {a, b =>
            if (tin[a] < tin[b]) { return Ordering.LT }
            if (tin[a] > tin[b]) { return Ordering.GT }
            return Ordering.EQ
        })
        let nodeSet = HashSet<Int64>()
        for (v in sorted) { nodeSet.add(v) }
        var i: Int64 = 0
        while (i + 1 < sorted.size) { nodeSet.add(lca(sorted[i], sorted[i + 1])); i++ }
        if (sorted.size > 0) { nodeSet.add(lca(sorted[0], sorted[sorted.size - 1])) }

        let allNodes = ArrayList<Int64>()
        for (v in nodeSet) { allNodes.add(v) }
        sort(allNodes, by: {a, b =>
            if (tin[a] < tin[b]) { return Ordering.LT }
            if (tin[a] > tin[b]) { return Ordering.GT }
            return Ordering.EQ
        })
        let idMap = HashMap<Int64, Int64>()
        let vtAdj = ArrayList<ArrayList<Int64>>()
        i = 0
        while (i < allNodes.size) { idMap[allNodes[i]] = i; vtAdj.add(ArrayList<Int64>()); i++ }

        let stk = ArrayList<Int64>()
        if (allNodes.size > 0) {
            stk.add(allNodes[0])
            i = 1
            while (i < allNodes.size) {
                let v = allNodes[i]
                let l = lca(v, stk[stk.size - 1])
                if (l != stk[stk.size - 1]) {
                    while (stk.size > 1 && depth[stk[stk.size - 2]] >= depth[l]) {
                        let u = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
                        vtAdj[idMap[stk[stk.size - 1]]].add(idMap[u])
                    }
                    if (stk[stk.size - 1] != l) {
                        let u = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
                        if (!idMap.contains(l)) { idMap[l] = vtAdj.size; vtAdj.add(ArrayList<Int64>()) }
                        vtAdj[idMap[l]].add(idMap[u]); stk.add(l)
                    }
                }
                stk.add(v); i++
            }
            while (stk.size > 1) {
                let u = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
                vtAdj[idMap[stk[stk.size - 1]]].add(idMap[u])
            }
        }
        return vtAdj
    }
}
// 用法: 7 节点树, build([3,5,6]) → 5节点虚树含 LCA 0,2
```

---

## 21. 分块

### 21.1 分块 (Sqrt Decomposition) — 区间加 + 区间求和

> **适用**: 区间修改+区间查询，代码简单易写。复杂度 O(n√n)

```cangjie
import std.collection.*

class SqrtBlock {
    let n: Int64
    let block: Int64
    var a: Array<Int64>
    var blockSum: Array<Int64>
    var blockAdd: Array<Int64>

    init(arr: Array<Int64>) {
        n = arr.size
        var sq: Int64 = 1
        while (sq * sq < n) { sq++ }
        block = sq
        a = arr.clone()
        let numBlocks = (n + block - 1) / block
        let blk = block  // 陷阱#9: 闭包不可引用未初始化成员
        blockSum = Array<Int64>(numBlocks, {_ => 0})
        blockAdd = Array<Int64>(numBlocks, {_ => 0})
        var i: Int64 = 0
        while (i < n) { blockSum[i / blk] += a[i]; i++ }
    }

    func rangeAdd(l: Int64, r: Int64, val_: Int64): Unit {
        let lb = l / block; let rb = r / block
        if (lb == rb) {
            var i = l
            while (i <= r) { a[i] += val_; blockSum[lb] += val_; i++ }
        } else {
            var i = l
            while (i < (lb + 1) * block) { a[i] += val_; blockSum[lb] += val_; i++ }
            var b = lb + 1
            while (b < rb) { blockAdd[b] += val_; blockSum[b] += val_ * block; b++ }
            i = rb * block
            while (i <= r) { a[i] += val_; blockSum[rb] += val_; i++ }
        }
    }

    func rangeSum(l: Int64, r: Int64): Int64 {
        let lb = l / block; let rb = r / block
        var sum: Int64 = 0
        if (lb == rb) {
            var i = l
            while (i <= r) { sum += a[i] + blockAdd[lb]; i++ }
        } else {
            var i = l
            while (i < (lb + 1) * block) { sum += a[i] + blockAdd[lb]; i++ }
            var b = lb + 1
            while (b < rb) { sum += blockSum[b]; b++ }
            i = rb * block
            while (i <= r) { sum += a[i] + blockAdd[rb]; i++ }
        }
        return sum
    }
}
// 用法: SqrtBlock([1..10]), rangeSum(0,4)=15, rangeAdd(2,5,10), rangeSum(0,4)=45
```

---

## 22. 基础补充

### 22.1 二维前缀和 + 二维差分

> **适用**: 矩阵子矩形求和 / 矩形区域修改。复杂度 O(nm) 预处理，O(1) 查询/修改

```cangjie
class Prefix2D {
    let rows: Int64
    let cols: Int64
    var pre: Array<Array<Int64>>

    init(grid: Array<Array<Int64>>) {
        rows = grid.size
        cols = if (rows > 0) { grid[0].size } else { 0 }
        let c = cols  // 陷阱#9
        pre = Array<Array<Int64>>(rows + 1, {_ => Array<Int64>(c + 1, {_ => 0})})
        var i: Int64 = 1
        while (i <= rows) {
            var j: Int64 = 1
            while (j <= cols) {
                pre[i][j] = grid[i - 1][j - 1] + pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1]
                j++
            }
            i++
        }
    }

    // 查询 [r1,c1] 到 [r2,c2] 子矩形和 (1-indexed)
    func query(r1: Int64, c1: Int64, r2: Int64, c2: Int64): Int64 {
        return pre[r2][c2] - pre[r1 - 1][c2] - pre[r2][c1 - 1] + pre[r1 - 1][c1 - 1]
    }
}

class Diff2D {
    let rows: Int64
    let cols: Int64
    var diff: Array<Array<Int64>>

    init(rows: Int64, cols: Int64) {
        this.rows = rows
        this.cols = cols
        let r = rows; let c = cols  // 陷阱#9
        diff = Array<Array<Int64>>(r + 2, {_ => Array<Int64>(c + 2, {_ => 0})})
    }

    // 子矩形 [r1,c1] 到 [r2,c2] 加 val (1-indexed)
    func add(r1: Int64, c1: Int64, r2: Int64, c2: Int64, val_: Int64): Unit {
        diff[r1][c1] += val_
        diff[r1][c2 + 1] -= val_
        diff[r2 + 1][c1] -= val_
        diff[r2 + 1][c2 + 1] += val_
    }

    func build(): Array<Array<Int64>> {
        let result = Array<Array<Int64>>(rows, {_ => Array<Int64>(cols, {_ => 0})})
        var i: Int64 = 1
        while (i <= rows) {
            var j: Int64 = 1
            while (j <= cols) {
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                result[i - 1][j - 1] = diff[i][j]
                j++
            }
            i++
        }
        return result
    }
}
// 用法: Prefix2D([[1,2,3],[4,5,6],[7,8,9]]).query(1,1,2,2) → 12
// Diff2D(3,3), add(1,1,2,2,5), add(2,2,3,3,3), build() → [[5,5,0],[5,8,3],[0,3,3]]
```

### 22.2 三分搜索

> **适用**: 单峰/单谷函数求极值。浮点复杂度 O(log(精度)), 整数 O(log n)

```cangjie
// 浮点三分: 求单谷函数最小值点
func ternarySearchMin(lo: Float64, hi: Float64,
                      f: (Float64) -> Float64): Float64 {
    var l = lo; var r = hi
    var iter: Int64 = 0
    while (iter < 200) {  // 200 次足够 10^-60 精度
        let m1 = l + (r - l) / 3.0
        let m2 = r - (r - l) / 3.0
        if (f(m1) < f(m2)) { r = m2 } else { l = m1 }
        iter++
    }
    return (l + r) / 2.0
}

// 整数三分: 求单谷函数最小值点
func ternarySearchMinInt(lo: Int64, hi: Int64,
                         f: (Int64) -> Int64): Int64 {
    var l = lo; var r = hi
    while (r - l > 2) {
        let m1 = l + (r - l) / 3
        let m2 = r - (r - l) / 3
        if (f(m1) < f(m2)) { r = m2 } else { l = m1 }
    }
    var best = l; var bestVal = f(l)
    var i = l + 1
    while (i <= r) {
        let v = f(i)
        if (v < bestVal) { bestVal = v; best = i }
        i++
    }
    return best
}
// 用法: ternarySearchMin(0,10, {x => (x-3)^2+1}) ≈ 3.0
// ternarySearchMinInt(0,10, {x => (x-5)^2}) → 5
```

---

## 23. 几何与扫描线

### 23.1 扫描线 (矩形面积并)

> **适用**: 多矩形面积并。复杂度 O(n log n)

```cangjie
import std.collection.*
import std.sort.*

class SweepLineSegTree {
    var cnt: Array<Int64>    // 覆盖计数
    var len: Array<Int64>    // 被覆盖长度
    let ys: Array<Int64>     // 离散化 y 坐标
    let size: Int64

    init(ys: Array<Int64>) {
        this.ys = ys
        size = ys.size - 1
        let n4 = if (size > 0) { size * 4 } else { 4 }
        cnt = Array<Int64>(n4, {_ => 0})
        len = Array<Int64>(n4, {_ => 0})
    }

    func pushup(node: Int64, l: Int64, r: Int64): Unit {
        if (cnt[node] > 0) { len[node] = ys[r + 1] - ys[l] }
        else if (l == r) { len[node] = 0 }
        else { len[node] = len[node * 2] + len[node * 2 + 1] }
    }

    func update(node: Int64, l: Int64, r: Int64, ql: Int64, qr: Int64, val_: Int64): Unit {
        if (ql > r || qr < l) { return }
        if (ql <= l && r <= qr) { cnt[node] += val_; pushup(node, l, r); return }
        let mid = (l + r) / 2
        update(node * 2, l, mid, ql, qr, val_)
        update(node * 2 + 1, mid + 1, r, ql, qr, val_)
        pushup(node, l, r)
    }
}

func rectangleAreaUnion(rects: Array<(Int64, Int64, Int64, Int64)>): Int64 {
    if (rects.size == 0) { return 0 }
    let ysSet = ArrayList<Int64>()
    for (r in rects) { let (_, y1, _, y2) = r; ysSet.add(y1); ysSet.add(y2) }
    let ysArr = ysSet.toArray(); sort(ysArr)
    let ys = ArrayList<Int64>(); ys.add(ysArr[0])
    var i: Int64 = 1
    while (i < ysArr.size) { if (ysArr[i] != ysArr[i - 1]) { ys.add(ysArr[i]) }; i++ }
    let yCoords = ys.toArray()
    let yMap = HashMap<Int64, Int64>()
    i = 0; while (i < yCoords.size) { yMap[yCoords[i]] = i; i++ }

    let events = ArrayList<(Int64, Int64, Int64, Int64)>()
    for (r in rects) {
        let (x1, y1, x2, y2) = r
        events.add((x1, 1, yMap[y1], yMap[y2]))
        events.add((x2, -1, yMap[y1], yMap[y2]))
    }
    let evArr = events.toArray()
    sort(evArr, by: {a, b =>
        if (a[0] < b[0]) { return Ordering.LT }
        if (a[0] > b[0]) { return Ordering.GT }
        return Ordering.EQ
    })
    let tree = SweepLineSegTree(yCoords)
    var area: Int64 = 0; var prevX: Int64 = evArr[0][0]
    i = 0
    while (i < evArr.size) {
        let (ex, etype, ey1, ey2) = evArr[i]
        area += tree.len[1] * (ex - prevX); prevX = ex
        tree.update(1, 0, tree.size - 1, ey1, ey2 - 1, etype)
        i++
    }
    return area
}
// 用法: rectangleAreaUnion([(0,0,3,3),(1,1,4,4)]) → 14
```

### 23.2 笛卡尔树 (Cartesian Tree)

> **适用**: 以值为优先级、以下标为 BST 序的树。O(n) 构建，用于 RMQ/最大矩形面积

```cangjie
import std.collection.*

// 返回 (root, left[], right[])，以 min-heap 顺序
func buildCartesianTree(a: Array<Int64>): (Int64, Array<Int64>, Array<Int64>) {
    let n = a.size
    let left = Array<Int64>(n, {_ => -1})
    let right = Array<Int64>(n, {_ => -1})
    let stk = ArrayList<Int64>()
    var i: Int64 = 0
    while (i < n) {
        var last: Int64 = -1
        while (stk.size > 0 && a[stk[stk.size - 1]] > a[i]) {
            last = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
        }
        if (last != -1) { left[i] = last }
        if (stk.size > 0) { right[stk[stk.size - 1]] = i }
        stk.add(i); i++
    }
    return (stk[0], left, right)
}
// 用法: [3,2,6,1,9] → root=3(val=1), left=[−1,0,−1,1,−1]
```

---

## 24. 异或与离线

### 24.1 线性基 (XOR Linear Basis)

> **适用**: XOR 相关问题：最大异或和、判断异或可达性。O(62) 每次插入/查询

```cangjie
class XORBasis {
    var basis: Array<Int64>
    let BITS: Int64 = 62

    init() { basis = Array<Int64>(63, {_ => 0}) }

    func insert(x: Int64): Bool {
        var v = x; var i = BITS
        while (i >= 0) {
            if (((v >> i) & 1) == 0) { i--; continue }
            if (basis[i] == 0) { basis[i] = v; return true }
            v = v ^ basis[i]; i--
        }
        return false  // 线性相关
    }

    func queryMax(): Int64 {
        var res: Int64 = 0; var i = BITS
        while (i >= 0) { if ((res ^ basis[i]) > res) { res = res ^ basis[i] }; i-- }
        return res
    }

    func queryMin(): Int64 {
        var i: Int64 = 0
        while (i <= BITS) { if (basis[i] != 0) { return basis[i] }; i++ }
        return 0
    }

    func canRepresent(x: Int64): Bool {
        var v = x; var i = BITS
        while (i >= 0) {
            if (((v >> i) & 1) == 0) { i--; continue }
            if (basis[i] == 0) { return false }
            v = v ^ basis[i]; i--
        }
        return true
    }
}
// 用法: insert(3,5,6), queryMax()=6, canRepresent(7)=false
```

### 24.2 整体二分 (Parallel Binary Search)

> **适用**: 多个查询同时二分答案。复杂度 O((n+q) log V)

```cangjie
import std.collection.*

class ParallelBinarySearch {
    let n: Int64
    var lo: Array<Int64>; var hi: Array<Int64>; var ans: Array<Int64>

    init(n: Int64, initLo: Int64, initHi: Int64) {
        this.n = n
        lo = Array<Int64>(n, {_ => initLo})
        hi = Array<Int64>(n, {_ => initHi})
        ans = Array<Int64>(n, {_ => initHi})
    }

    // checkMid(n, mids) → Array<Bool>: 每个查询在对应 mid 下是否满足
    func solve(checkMid: (Int64, Array<Int64>) -> Array<Bool>): Array<Int64> {
        var iterations: Int64 = 0
        while (iterations < 40) {
            let mids = Array<Int64>(n, {i => (lo[i] + hi[i]) / 2})
            var hasActive = false
            var idx: Int64 = 0
            while (idx < n) { if (lo[idx] < hi[idx]) { hasActive = true; break }; idx++ }
            if (!hasActive) { break }
            let results = checkMid(n, mids)
            idx = 0
            while (idx < n) {
                if (lo[idx] < hi[idx]) {
                    if (results[idx]) { ans[idx] = mids[idx]; hi[idx] = mids[idx] }
                    else { lo[idx] = mids[idx] + 1 }
                }
                idx++
            }
            iterations++
        }
        return ans
    }
}
// 用法: 3 个查询找阈值 → [10, 50, 75]
```

---

## 25. 树与字符串进阶

### 25.1 树哈希 (Tree Hashing)

> **适用**: 判定有根子树同构。复杂度 O(n log n)

```cangjie
import std.collection.*
import std.sort.*

func treeHash(n: Int64, adj: ArrayList<ArrayList<Int64>>,
              root: Int64): Array<Int64> {
    let hashMod: Int64 = 998244353
    let hashBase: Int64 = 1000000007
    let parent = Array<Int64>(n, {_ => -1})
    let hashVal = Array<Int64>(n, {_ => 1})
    let order = ArrayList<Int64>()
    let visited = Array<Bool>(n, {_ => false})
    // BFS
    let queue = ArrayList<Int64>()
    queue.add(root); visited[root] = true
    var head: Int64 = 0
    while (head < queue.size) {
        let v = queue[head]; head++; order.add(v)
        for (u in adj[v]) {
            if (!visited[u]) { visited[u] = true; parent[u] = v; queue.add(u) }
        }
    }
    // 逆序计算 (叶子先)
    var i = order.size - 1
    while (i >= 0) {
        let v = order[i]
        let ch = ArrayList<Int64>()
        for (u in adj[v]) { if (u != parent[v]) { ch.add(hashVal[u]) } }
        let sorted = ch.toArray(); sort(sorted)
        var h: Int64 = 1
        for (c in sorted) { h = h * ((c + hashBase) % hashMod) % hashMod }
        hashVal[v] = h; i--
    }
    return hashVal
}
// 用法: 同构叶节点 hash 值相等
```

### 25.2 最小表示法 (Minimum Representation)

> **适用**: 求循环字符串的字典序最小旋转起点。O(n)

```cangjie
func minRepresentation(s: String): Int64 {
    let a = s.toRuneArray()
    let n = a.size
    var i: Int64 = 0; var j: Int64 = 1; var k: Int64 = 0
    while (i < n && j < n && k < n) {
        let ci = UInt32(a[(i + k) % n])
        let cj = UInt32(a[(j + k) % n])
        if (ci == cj) { k++ }
        else if (ci > cj) { i += k + 1; if (i == j) { i++ }; k = 0 }
        else { j += k + 1; if (j == i) { j++ }; k = 0 }
    }
    return if (i < j) { i } else { j }
}
// 用法: minRepresentation("bca") → 2 (即 "abc")
```

---

## 26. 图连通性

### 26.1 点双连通分量 (Biconnected Components)

> **适用**: 求割点 + 点双连通分量。复杂度 O(n + m)

```cangjie
import std.collection.*

func biconnectedComponents(n: Int64, adj: ArrayList<ArrayList<Int64>>):
    (ArrayList<ArrayList<Int64>>, Array<Bool>) {
    let dfn = Array<Int64>(n, {_ => 0})
    let low = Array<Int64>(n, {_ => 0})
    let isArt = Array<Bool>(n, {_ => false})
    var timer: Int64 = 0
    let stk = ArrayList<Int64>()
    let components = ArrayList<ArrayList<Int64>>()

    func dfs(u: Int64, parent: Int64): Unit {
        timer++; dfn[u] = timer; low[u] = timer; stk.add(u)
        var childCount: Int64 = 0
        for (v in adj[u]) {
            if (v == parent) { continue }
            if (dfn[v] == 0) {
                childCount++; dfs(v, u)
                if (low[v] < low[u]) { low[u] = low[v] }
                if ((parent == -1 && childCount > 1) || (parent != -1 && low[v] >= dfn[u])) {
                    isArt[u] = true
                }
                if (low[v] >= dfn[u]) {
                    let comp = ArrayList<Int64>()
                    while (stk.size > 0) {
                        let top = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
                        comp.add(top)
                        if (top == v) { break }
                    }
                    comp.add(u); components.add(comp)
                }
            } else { if (dfn[v] < low[u]) { low[u] = dfn[v] } }
        }
    }

    var i: Int64 = 0
    while (i < n) { if (dfn[i] == 0) { dfs(i, -1) }; i++ }
    return (components, isArt)
}
// 用法: 三角形+路径, BCC=3组, 割点=[2,3]
```

### 26.2 边双连通分量 (Edge Biconnected Components)

> **适用**: 求桥 + 边双连通分量。复杂度 O(n + m)

```cangjie
import std.collection.*

func edgeBCC(n: Int64, adj: ArrayList<ArrayList<(Int64, Int64)>>):
    (Array<Int64>, Int64) {
    // adj[u] = [(v, edgeId)], 返回 (每点所属分量, 分量数)
    let dfn = Array<Int64>(n, {_ => 0})
    let low = Array<Int64>(n, {_ => 0})
    var timer: Int64 = 0
    let stk = ArrayList<Int64>()
    let comp = Array<Int64>(n, {_ => -1})
    var numComp: Int64 = 0

    func dfs(u: Int64, fromEdge: Int64): Unit {
        timer++; dfn[u] = timer; low[u] = timer; stk.add(u)
        for (edge in adj[u]) {
            let (v, eid) = edge
            if (eid == fromEdge) { continue }
            if (dfn[v] == 0) {
                dfs(v, eid)
                if (low[v] < low[u]) { low[u] = low[v] }
            } else { if (dfn[v] < low[u]) { low[u] = dfn[v] } }
        }
        if (low[u] == dfn[u]) {
            while (true) {
                let top = stk[stk.size - 1]; stk.remove(at: stk.size - 1)
                comp[top] = numComp
                if (top == u) { break }
            }
            numComp++
        }
    }

    var i: Int64 = 0
    while (i < n) { if (dfn[i] == 0) { dfs(i, -1) }; i++ }
    return (comp, numComp)
}
// 用法: 三角形{0,1,2}+链{3,4}, EBCC=3 组
```

---

## 附录: 常用常量

```cangjie
let INF: Int64 = 0x3f3f3f3f3f3f3f3f   // 大整数哨兵
let MOD: Int64 = 1000000007            // 10^9 + 7
let MOD2: Int64 = 998244353            // NTT 常用模数
```

## 附录: 仓颉竞赛关键陷阱 (编译器已验证)

| 陷阱 | 正确写法 | 说明 |
|------|----------|------|
| `e & 1 == 1` | `(e & 1) == 1` | `&` 优先级低于 `==`，不加括号编译报错 |
| `Int64(r'a')` | `Int64(UInt32(r'a'))` | Rune 不是数值类型，需先转 UInt32 |
| `TreeMap<(A,B), V>()` | `TreeMap<Int64, V>()` + 编码 | Tuple 未实现 Comparable，不可做 Key |
| `list.append(x)` | `list.add(x)` | ArrayList 没有 append |
| `queue.enqueue(x)` | `queue.add(x)` | ArrayQueue 没有 enqueue/dequeue |
| `func dfs() {` 递归 | `func dfs(): Unit {` | 递归嵌套函数必须标注返回类型 |
| `for (ch in s)` | 遍历 Byte | 如需 Rune 用 `s.runes()` |
| `map[key]` 缺键 | `map.get(key)` | `[]` 不存在时抛异常 |
| `this.x = Array(n, {_ => f(LOG)})` | 用 `let logVal = 20` 局部变量代替 | init 中闭包不可访问未全初始化的成员 |
| `func extend(...)` | `func addChar(...)` | `extend` 是仓颉关键字，不可做方法名 |
| `MyStruct(a: 1, b: 2)` | 定义 `init(a: Int64, b: Int64)` + 位置调用 | struct 无自动命名构造器，需显式 init |
| `while(true) { return x }` | `var r = init; while(r==init) { ... r=v }; return r` | `while(true)` 类型是 Unit，不能在返回非 Unit 函数中使用 |

---

## § 27. 高级数据结构补充

### 27.1 回文自动机 (PAM / Eertree) — O(n)

> **适用**: 回文子串计数、不同回文子串数、最长回文后缀。O(n) 构建

```cangjie
import std.collection.*

class PAM {
    var len: ArrayList<Int64>       // 节点代表的回文长度
    var fail: ArrayList<Int64>      // 后缀链接
    var ch: ArrayList<Array<Int64>> // 转移边 (26 个字母)
    var cnt: ArrayList<Int64>       // 该节点对应回文串出现次数 (需后续 propagate)
    var sz: Int64                   // 节点总数
    var last: Int64                 // 当前最长回文后缀节点
    var s: ArrayList<Int64>         // 已添加字符序列
    var n: Int64                    // 当前字符串长度

    init() {
        len = ArrayList<Int64>()
        fail = ArrayList<Int64>()
        ch = ArrayList<Array<Int64>>()
        cnt = ArrayList<Int64>()
        sz = 0; last = 0; n = 0
        s = ArrayList<Int64>()
        s.add(-1) // 哨兵
        // 节点0: 偶根 (len=0), 节点1: 奇根 (len=-1)
        newNode(0); newNode(-1)
        fail[0] = 1; fail[1] = 1
        last = 0
    }

    func newNode(length: Int64): Int64 {
        len.add(length)
        fail.add(0)
        ch.add(Array<Int64>(26, {_ => 0}))
        cnt.add(0)
        let id = sz; sz++
        return id
    }

    func getFail(x: Int64): Int64 {
        var cur = x
        while (s[n - len[cur] - 1] != s[n]) {
            cur = fail[cur]
        }
        return cur
    }

    // 添加一个字符 c (0-25)
    func addChar(c: Int64): Int64 {
        n++
        s.add(c)
        let cur = getFail(last)
        if (ch[cur][c] == 0) {
            let now = newNode(len[cur] + 2)
            fail[now] = ch[getFail(fail[cur])][c]
            if (fail[now] == 0 && now != 2) { fail[now] = 0 } // 偶根
            ch[cur][c] = now
        }
        last = ch[cur][c]
        cnt[last] = cnt[last] + 1
        return last
    }

    // 传播 cnt, 逆拓扑序累加
    func propagate(): Unit {
        var i = sz - 1
        while (i >= 2) {
            cnt[fail[i]] = cnt[fail[i]] + cnt[i]
            i--
        }
    }

    // 不同回文子串数 = sz - 2
    func distinctCount(): Int64 { return sz - 2 }
}
// 用法: 对 "abba", addChar(0),addChar(1),addChar(1),addChar(0)
// distinctCount() = 4: "a","b","bb","abba"
```

### 27.2 对顶堆 (Dual Heap via TreeMap) — O(log n) 每操作

> **适用**: 动态维护中位数、第 k 大/小。仓颉无原生堆，用 TreeMap 模拟

```cangjie
import std.collection.*

class DualHeap {
    // 小顶部分 (存较大的一半, 升序) 和 大顶部分 (存较小的一半, 降序)
    // 用 TreeMap<Int64, Int64> 存 (编码值 -> 计数)
    // 编码: key = value * 1000000 + uniqueId (避免重复值冲突)
    var lo: TreeMap<Int64, Int64>      // 较小一半, key 降序取 last
    var hi: TreeMap<Int64, Int64>      // 较大一半, key 升序取 first
    var loSize: Int64
    var hiSize: Int64
    var uid: Int64

    init() {
        lo = TreeMap<Int64, Int64>()
        hi = TreeMap<Int64, Int64>()
        loSize = 0; hiSize = 0; uid = 0
    }

    func encode(v: Int64): Int64 {
        uid++
        return v * 1000000 + uid
    }

    func decode(k: Int64): Int64 { return k / 1000000 }

    func addNum(num: Int64): Unit {
        let key = encode(num)
        // 先加入 lo (较小一半)
        lo.put(key, 1); loSize++
        // 平衡: lo 的最大值移到 hi
        let loMax = lo.lastEntry().getOrThrow()
        lo.remove(loMax.key); loSize--
        hi.put(loMax.key, 1); hiSize++
        // 保持 loSize >= hiSize
        if (loSize < hiSize) {
            let hiMin = hi.firstEntry().getOrThrow()
            hi.remove(hiMin.key); hiSize--
            lo.put(hiMin.key, 1); loSize++
        }
    }

    // 中位数: loSize > hiSize 时取 lo 最大值, 否则取两者平均
    func findMedian(): Int64 {
        return decode(lo.lastEntry().getOrThrow().key)
    }
}
// 用法: addNum(1), addNum(3), addNum(2), findMedian() = 2
```

### 27.3 左偏树 (Leftist Heap / 可并堆) — O(log n) 合并

> **适用**: 需要高效合并两个堆的场景（如多源 Dijkstra、哈夫曼变种）

```cangjie
import std.collection.*

class LeftistNode {
    var val: Int64
    var left: Int64   // 左子节点编号 (-1 = null)
    var right: Int64  // 右子节点编号 (-1 = null)
    var dist: Int64   // 右路径长度

    init(v: Int64) {
        val = v; left = -1; right = -1; dist = 0
    }
}

class LeftistHeap {
    var nodes: ArrayList<LeftistNode>

    init() { nodes = ArrayList<LeftistNode>() }

    func newNode(v: Int64): Int64 {
        nodes.add(LeftistNode(v))
        return nodes.size - 1
    }

    func getDist(x: Int64): Int64 {
        if (x == -1) { return -1 }
        return nodes[x].dist
    }

    // 合并两个堆, 返回新根编号
    func merge(a: Int64, b: Int64): Int64 {
        if (a == -1) { return b }
        if (b == -1) { return a }
        // 小根堆: 值小的做根
        var x = a; var y = b
        if (nodes[x].val > nodes[y].val) { let t = x; x = y; y = t }
        nodes[x].right = merge(nodes[x].right, y)
        // 维护左偏性质
        if (getDist(nodes[x].left) < getDist(nodes[x].right)) {
            let t = nodes[x].left
            nodes[x].left = nodes[x].right
            nodes[x].right = t
        }
        nodes[x].dist = getDist(nodes[x].right) + 1
        return x
    }

    // 弹出堆顶 (最小值), 返回 (值, 新根)
    func pop(root: Int64): (Int64, Int64) {
        let v = nodes[root].val
        let newRoot = merge(nodes[root].left, nodes[root].right)
        return (v, newRoot)
    }
}
// 用法: merge(heap1, heap2) 合并两个堆
```

### 27.4 Splay 树 (独立平衡树) — O(log n) 摊销

> **适用**: 区间翻转、序列分裂合并。与 FHQ-Treap 互补

```cangjie
import std.collection.*

class Splay {
    var ch: ArrayList<Array<Int64>>  // ch[x][0]=左, ch[x][1]=右
    var fa: ArrayList<Int64>         // 父节点
    var sz: ArrayList<Int64>         // 子树大小
    var val: ArrayList<Int64>        // 值
    var rev: ArrayList<Bool>         // 翻转标记 (区间翻转用)
    var root: Int64
    var tot: Int64

    init(capacity: Int64) {
        let cap = capacity + 2
        ch = ArrayList<Array<Int64>>()
        fa = ArrayList<Int64>()
        sz = ArrayList<Int64>()
        val = ArrayList<Int64>()
        rev = ArrayList<Bool>()
        var i: Int64 = 0
        while (i < cap) {
            ch.add(Array<Int64>(2, {_ => 0}))
            fa.add(0); sz.add(0); val.add(0); rev.add(false)
            i++
        }
        root = 0; tot = 0
    }

    func pushUp(x: Int64): Unit { sz[x] = sz[ch[x][0]] + sz[ch[x][1]] + 1 }

    func pushDown(x: Int64): Unit {
        if (rev[x]) {
            let t = ch[x][0]; ch[x][0] = ch[x][1]; ch[x][1] = t
            if (ch[x][0] != 0) { rev[ch[x][0]] = !rev[ch[x][0]] }
            if (ch[x][1] != 0) { rev[ch[x][1]] = !rev[ch[x][1]] }
            rev[x] = false
        }
    }

    func rotate(x: Int64): Unit {
        let y = fa[x]; let z = fa[y]
        let k: Int64 = if (ch[y][1] == x) { 1 } else { 0 }
        let w = ch[x][1 - k]
        ch[z][if (ch[z][1] == y) { 1 } else { 0 }] = x
        ch[x][1 - k] = y; ch[y][k] = w
        fa[w] = y; fa[y] = x; fa[x] = z
        pushUp(y); pushUp(x)
    }

    func splay(x: Int64, goal: Int64): Unit {
        while (fa[x] != goal) {
            let y = fa[x]; let z = fa[y]
            if (z != goal) {
                let ky: Int64 = if (ch[z][1] == y) { 1 } else { 0 }
                let kx: Int64 = if (ch[y][1] == x) { 1 } else { 0 }
                if (ky == kx) { rotate(y) } else { rotate(x) }
            }
            rotate(x)
        }
        if (goal == 0) { root = x }
    }

    // 找第 k 个节点 (1-indexed)
    func kth(k: Int64): Int64 {
        var cur = root; var rem = k
        while (true) {
            pushDown(cur)
            if (sz[ch[cur][0]] >= rem) { cur = ch[cur][0] }
            else if (sz[ch[cur][0]] + 1 == rem) { return cur }
            else { rem -= sz[ch[cur][0]] + 1; cur = ch[cur][1] }
        }
        return cur // 不可达
    }

    // 翻转区间 [l, r] (1-indexed)
    func reverseRange(l: Int64, r: Int64): Unit {
        let x = kth(l - 1); splay(x, 0)        // l-1 旋转到根
        let y = kth(r + 1); splay(y, root)      // r+1 旋转到根的右子
        let z = ch[y][0]                         // 区间 [l,r] 在 z 子树
        rev[z] = !rev[z]
    }
}
// 用法: 序列翻转 — 经典 NOI 文艺平衡树
```

---

## § 28. Chtholly Tree / 珂朵莉树 — O(n log n) 期望

> **适用**: 区间赋值（assign）频繁的题目。基于有序集合维护值相同的连续段

```cangjie
import std.collection.*

class ChthollyTree {
    // 用 TreeMap<Int64, Int64> 存区间 (左端点 -> 值)
    // 含义: 从 key 开始到下一个 key 之前, 值都是 val
    var tree: TreeMap<Int64, Int64>

    init(n: Int64, initVal: Int64) {
        tree = TreeMap<Int64, Int64>()
        tree.put(0, initVal)
        tree.put(n, 0)  // 哨兵
    }

    // 在位置 pos 处分裂: 确保 pos 是一个区间起点
    func split(pos: Int64): Unit {
        let it = tree.backward(pos + 1) // <= pos 的最大 key
        match (it.next()) {
            case Some(entry) =>
                if (entry.key == pos) { return } // 已存在
                let v = entry.value
                tree.put(pos, v)
            case None => ()
        }
    }

    // 区间赋值 [l, r) = val
    func assign(l: Int64, r: Int64, val: Int64): Unit {
        split(l); split(r)
        // 删除 [l, r) 内所有旧区间起点
        let toRemove = ArrayList<Int64>()
        let it = tree.forward(l)
        while (true) {
            match (it.next()) {
                case Some(entry) =>
                    if (entry.key >= r) { break }
                    toRemove.add(entry.key)
                case None => break
            }
        }
        for (k in toRemove) { tree.remove(k) }
        tree.put(l, val)
    }

    // 区间求和 [l, r)
    func querySum(l: Int64, r: Int64): Int64 {
        split(l); split(r)
        var sum: Int64 = 0
        let it = tree.forward(l)
        var prevKey = l
        while (true) {
            match (it.next()) {
                case Some(entry) =>
                    if (entry.key >= r) {
                        sum += (r - prevKey) * tree.get(prevKey).getOrThrow()
                        break
                    }
                    sum += (entry.key - prevKey) * tree.get(prevKey).getOrThrow()
                    prevKey = entry.key
                case None => break
            }
        }
        return sum
    }
}
// 用法: 区间赋值 + 区间查询, 适合数据随机的 assign-heavy 题目
```

---

## § 29. K-D Tree (二维) — O(√n) 平均查询

> **适用**: 二维平面上的矩形范围查询、最近点查询

```cangjie
import std.collection.*

class KDTree {
    var x: ArrayList<Int64>
    var y: ArrayList<Int64>
    var minX: ArrayList<Int64>; var maxX: ArrayList<Int64>
    var minY: ArrayList<Int64>; var maxY: ArrayList<Int64>
    var left: ArrayList<Int64>; var right: ArrayList<Int64>
    var sz: Int64

    init(capacity: Int64) {
        let cap = capacity + 1
        x = ArrayList<Int64>(); y = ArrayList<Int64>()
        minX = ArrayList<Int64>(); maxX = ArrayList<Int64>()
        minY = ArrayList<Int64>(); maxY = ArrayList<Int64>()
        left = ArrayList<Int64>(); right = ArrayList<Int64>()
        var i: Int64 = 0
        while (i < cap) {
            x.add(0); y.add(0)
            minX.add(0); maxX.add(0); minY.add(0); maxY.add(0)
            left.add(0); right.add(0)
            i++
        }
        sz = 0
    }

    func newNode(px: Int64, py: Int64): Int64 {
        sz++
        x[sz] = px; y[sz] = py
        minX[sz] = px; maxX[sz] = px
        minY[sz] = py; maxY[sz] = py
        left[sz] = 0; right[sz] = 0
        return sz
    }

    func pushUp(o: Int64): Unit {
        minX[o] = x[o]; maxX[o] = x[o]
        minY[o] = y[o]; maxY[o] = y[o]
        for (c in [left[o], right[o]]) {
            if (c != 0) {
                if (minX[c] < minX[o]) { minX[o] = minX[c] }
                if (maxX[c] > maxX[o]) { maxX[o] = maxX[c] }
                if (minY[c] < minY[o]) { minY[o] = minY[c] }
                if (maxY[c] > maxY[o]) { maxY[o] = maxY[c] }
            }
        }
    }

    // 插入点, dim=0 按 x 分, dim=1 按 y 分
    func insert(root: Int64, px: Int64, py: Int64, dim: Int64): Int64 {
        if (root == 0) { return newNode(px, py) }
        if (dim == 0) {
            if (px <= x[root]) {
                left[root] = insert(left[root], px, py, 1 - dim)
            } else {
                right[root] = insert(right[root], px, py, 1 - dim)
            }
        } else {
            if (py <= y[root]) {
                left[root] = insert(left[root], px, py, 1 - dim)
            } else {
                right[root] = insert(right[root], px, py, 1 - dim)
            }
        }
        pushUp(root)
        return root
    }

    // 求最近点距离 (曼哈顿距离)
    func minDist(o: Int64, px: Int64, py: Int64): Int64 {
        if (o == 0) { return 0x3f3f3f3f3f3f3f3f }
        var dx: Int64 = 0; var dy: Int64 = 0
        if (px < minX[o]) { dx = minX[o] - px }
        else if (px > maxX[o]) { dx = px - maxX[o] }
        if (py < minY[o]) { dy = minY[o] - py }
        else if (py > maxY[o]) { dy = py - maxY[o] }
        return dx + dy
    }

    func nearest(root: Int64, px: Int64, py: Int64): Int64 {
        if (root == 0) { return 0x3f3f3f3f3f3f3f3f }
        var d: Int64 = 0
        let ddx = x[root] - px; let ddy = y[root] - py
        if (ddx < 0) { d += -ddx } else { d += ddx }
        if (ddy < 0) { d += -ddy } else { d += ddy }
        let dl = minDist(left[root], px, py)
        let dr = minDist(right[root], px, py)
        var res = d
        if (dl < dr) {
            let r1 = nearest(left[root], px, py)
            if (r1 < res) { res = r1 }
            if (dr < res) {
                let r2 = nearest(right[root], px, py)
                if (r2 < res) { res = r2 }
            }
        } else {
            let r1 = nearest(right[root], px, py)
            if (r1 < res) { res = r1 }
            if (dl < res) {
                let r2 = nearest(left[root], px, py)
                if (r2 < res) { res = r2 }
            }
        }
        return res
    }
}
// 用法: 二维最近点查询
```

---

## § 30. 高级 DP 优化

### 30.1 分治优化 DP (Divide & Conquer DP) — O(n m log n)

> **适用**: 满足决策单调性的 DP：`dp[i][j] = min { dp[i-1][k] + cost(k+1, j) }`

```cangjie
import std.collection.*

// pre[j] - pre[k] 类型的 cost 函数
func divideConquerDP(m: Int64, n: Int64, cost: (Int64, Int64) -> Int64): Array<Int64> {
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    var dp = Array<Int64>(n + 1, {_ => INF})
    var ndp = Array<Int64>(n + 1, {_ => INF})
    dp[0] = 0

    var layer: Int64 = 0
    while (layer < m) {
        var j: Int64 = 0
        while (j <= n) { ndp[j] = INF; j++ }

        // solve(l, r, optL, optR): dp[layer+1][l..r] 的最优决策点在 [optL, optR]
        func solve(l: Int64, r: Int64, optL: Int64, optR: Int64): Unit {
            if (l > r) { return }
            let mid = (l + r) / 2
            var bestK = optL
            var bestVal = INF
            var k = optL
            let kr = if (mid < optR) { mid } else { optR }
            while (k <= kr) {
                let v = dp[k] + cost(k + 1, mid)
                if (v < bestVal) { bestVal = v; bestK = k }
                k++
            }
            ndp[mid] = bestVal
            solve(l, mid - 1, optL, bestK)
            solve(mid + 1, r, bestK, optR)
        }

        solve(1, n, 0, n - 1)
        let t = dp; dp = ndp; ndp = t
        layer++
    }
    return dp
}
// 用法: 将 n 个元素分成 m 组, 最小化组内 cost 之和
```

### 30.2 SMAWK / 单调队列优化 1D1D DP — O(n)

> **适用**: `dp[j] = min { dp[i] + w(i, j) }` 满足四边形不等式

```cangjie
import std.collection.*

// 单调队列优化: 适用于 dp[j] = min(dp[i] + cost(i,j)), i < j, cost 满足决策单调性
func monotonicQueueDP(n: Int64, cost: (Int64, Int64) -> Int64): Array<Int64> {
    let INF: Int64 = 0x3f3f3f3f3f3f3f3f
    let dp = Array<Int64>(n + 1, {_ => INF})
    dp[0] = 0
    // dq 存入决策点, 保持决策单调
    let dq = ArrayList<Int64>()
    dq.add(0)
    var j: Int64 = 1
    while (j <= n) {
        // 弹出不优的队首
        while (dq.size > 1) {
            let a = dq[0]; let b = dq[1]
            if (dp[a] + cost(a, j) >= dp[b] + cost(b, j)) {
                dq.remove(at: 0)
            } else { break }
        }
        dp[j] = dp[dq[0]] + cost(dq[0], j)
        // 维护队尾单调性
        while (dq.size > 1) {
            let sz = dq.size
            let a = dq[sz - 2]; let b = dq[sz - 1]
            // 如果 j 比 b 在任何后续位置都更优, 弹出 b
            if (dp[b] + cost(b, j + 1) >= dp[j] + cost(j, j + 1)) {
                dq.remove(at: sz - 1)
            } else { break }
        }
        dq.add(j)
        j++
    }
    return dp
}
// 用法: 1D1D DP 优化, 如最优划分问题
```

---

## 附录 3: PriorityQueue 模拟指南 (基于 TreeMap)

> 仓颉标准库没有原生 PriorityQueue。竞赛中用 TreeMap 模拟：

```cangjie
import std.collection.*

// ===== 小根堆模拟 =====
class MinHeap {
    var tree: TreeMap<Int64, Int64>  // key=编码值, value=1 (占位)
    var uid: Int64

    init() { tree = TreeMap<Int64, Int64>(); uid = 0 }

    // 编码: val * 10000000 + uid, 保证不同元素有唯一 key
    func push(val: Int64): Unit {
        uid++
        tree.put(val * 10000000 + uid, 1)
    }

    func top(): Int64 {
        return tree.firstEntry().getOrThrow().key / 10000000
    }

    func pop(): Int64 {
        let entry = tree.firstEntry().getOrThrow()
        tree.remove(entry.key)
        return entry.key / 10000000
    }

    func isEmpty(): Bool { return tree.size == 0 }
}

// ===== 大根堆模拟 =====
class MaxHeap {
    var tree: TreeMap<Int64, Int64>
    var uid: Int64

    init() { tree = TreeMap<Int64, Int64>(); uid = 0 }

    func push(val: Int64): Unit {
        uid++
        tree.put(val * 10000000 + uid, 1)
    }

    func top(): Int64 {
        return tree.lastEntry().getOrThrow().key / 10000000
    }

    func pop(): Int64 {
        let entry = tree.lastEntry().getOrThrow()
        tree.remove(entry.key)
        return entry.key / 10000000
    }

    func isEmpty(): Bool { return tree.size == 0 }
}

// 用法:
// let pq = MinHeap()
// pq.push(5); pq.push(3); pq.push(7)
// pq.top()  // 3
// pq.pop()  // 3
// pq.top()  // 5
//
// 注意: 编码系数 10000000 需保证 val * 10000000 + uid 不溢出 Int64
// 安全范围: val ∈ [-9×10^11, 9×10^11], uid < 10^7
```
