# 思路

**核心算法**: 01背包 DP

**关键 insight**: 经典 01 背包问题——N 个物品各有重量和价值，背包容量 W，每个物品最多选一次，求最大价值。使用一维 DP 滚动数组优化空间。

**步骤**:
1. 读入 N 个物品 (weight, value) 和背包容量 W
2. dp[j] = 容量为 j 时的最大价值，初始全 0
3. 对每个物品 i，从 W 到 w[i] 逆序遍历，dp[j] = max(dp[j], dp[j - w[i]] + v[i])
4. 输出 dp[W]

---

# 复杂度

- **时间复杂度**: O(N × W) — N 个物品各遍历 W 个容量
- **空间复杂度**: O(W) — 一维滚动数组

**变量定义**: N=物品数, W=背包容量

**论证**: 01背包经典复杂度，N,W ≤ 1000 时 O(10^6) 完全可接受

---

# 正确性要点

**方法**: 不变量

- **初始**: dp[0..W] = 0，不选任何物品时价值为 0
- **维持**: 处理完前 i 个物品后，dp[j] = 从前 i 个物品中选取、总重 ≤ j 的最大价值。逆序遍历保证每个物品只选一次
- **终止**: 处理完全部 N 个物品，dp[W] 即为答案

---

# 仓颉实现

```cangjie
import std.collection.*
import std.convert.*
import std.math.*

main() {
    let line1 = readln().split(" ")
    let n = Int64.parse(line1[0])
    let W = Int64.parse(line1[1])

    let weight = Array<Int64>(n, {_ => 0})
    let value = Array<Int64>(n, {_ => 0})
    var i: Int64 = 0
    while (i < n) {
        let parts = readln().split(" ")
        weight[i] = Int64.parse(parts[0])
        value[i] = Int64.parse(parts[1])
        i++
    }

    let dp = Array<Int64>(W + 1, {_ => 0})
    i = 0
    while (i < n) {
        var j = W
        while (j >= weight[i]) {
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
            j--
        }
        i++
    }

    println(dp[W])
}
```

---

# 边界测试

| # | 输入 | 期望输出 | 验证点 |
|---|------|---------|--------|
| 1 | N=1, W=0 | 0 | 容量不足 |
| 2 | N=1, W≥w[0] | v[0] | 单物品放入 |
| 3 | N=4, W=5, items=(2,3)(1,2)(3,4)(2,2) | 7 | 标准测试 |
| 4 | 所有物品重量 > W | 0 | 全不可选 |
| 5 | N=1000, W=1000 | — | 不超时 |

---

# 风险项

| # | 风险 | 概率 | 规避策略 |
|---|------|------|---------|
| 1 | 遍历方向错误（正序变完全背包） | 中 | 逆序 j: W → w[i] |
| 2 | Int64 溢出 | 低 | value ≤ 10^6, N ≤ 10^3, 最大 10^9 < 2^63 |

---

# 证据引用

- `cj-std-algo-toolkit/references/docs/std/math/math_package_api/math_package_funcs | max | "public func max(x: Int64, y: Int64): Int64"`
- `cj-language-core/references/docs/user_manual/basic_data_type/integer_type.md | Int64 | "64 位有符号整数类型"`
