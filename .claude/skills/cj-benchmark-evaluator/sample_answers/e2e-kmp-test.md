# 思路

**核心算法**: KMP 字符串匹配

**关键 insight**: 给定文本串 T 和模式串 P，找出 P 在 T 中所有出现位置。KMP 利用前缀函数避免重复匹配，保证线性复杂度。

**步骤**:
1. 读入文本串 T 和模式串 P
2. 对 P 计算 next 数组（前缀函数）
3. 用 KMP 主过程扫描 T，输出所有匹配起始位置（0-indexed）

---

# 复杂度

- **时间复杂度**: O(N + M) — N = |T|, M = |P|
- **空间复杂度**: O(M) — next 数组

**变量定义**: N=文本串长度, M=模式串长度

**论证**: KMP 的 j 指针回退总量不超过前进量，均摊 O(1)

---

# 正确性要点

**方法**: 不变量

- **初始**: next[0] = 0，空前缀无真前后缀
- **维持**: next[i] = P[0..next[i]-1] == P[i-next[i]+1..i]，即最长匹配前后缀
- **终止**: 找到 j == M 时，T[i-M..i-1] 完全匹配 P

---

# 仓颉实现

```cangjie
import std.collection.*
import std.convert.*

main() {
    let T = readln().toArray()
    let P = readln().toArray()
    let n = T.size
    let m = P.size

    // Build next (prefix function)
    let next = Array<Int64>(m, {_ => 0})
    var j: Int64 = 0
    var i: Int64 = 1
    while (i < m) {
        while (j > 0 && P[i] != P[j]) { j = next[j - 1] }
        if (P[i] == P[j]) { j++ }
        next[i] = j
        i++
    }

    // KMP search
    j = 0
    i = 0
    let results = ArrayList<Int64>()
    while (i < n) {
        while (j > 0 && T[i] != P[j]) { j = next[j - 1] }
        if (T[i] == P[j]) { j++ }
        if (j == m) {
            results.add(i - m + 1)
            j = next[j - 1]
        }
        i++
    }

    // Output
    if (results.size == 0) {
        println(-1)
    } else {
        var first = true
        for (r in results) {
            if (!first) { print(" ") }
            print(r)
            first = false
        }
        println()
    }
}
```

---

# 边界测试

| # | 输入 | 期望输出 | 验证点 |
|---|------|---------|--------|
| 1 | T="a", P="a" | 0 | 最小匹配 |
| 2 | T="aaaa", P="aa" | 0 1 2 | 重叠匹配 |
| 3 | T="abcdef", P="xyz" | -1 | 无匹配 |
| 4 | T="ababababc", P="ababc" | 4 | 需要回退 |
| 5 | T=P (相同) | 0 | 完全匹配 |

---

# 风险项

| # | 风险 | 概率 | 规避策略 |
|---|------|------|---------|
| 1 | String.toArray() 返回 Byte 非 Rune | 中 | ASCII 场景 Byte 比较即可；中文需 toRuneArray() |
| 2 | 空串 P | 低 | 题目一般保证 |P| ≥ 1 |

---

# 证据引用

- `cj-std-algo-toolkit/references/docs/std/collection/collection_package_api/collection_package_class_ArrayList | add | "public func add(element: T): Unit"`
- `cj-language-core/references/docs/user_manual/basic_data_type/string_type.md | toArray | "func toArray(): Array<Byte>"`
