---
name: cj-std-algo-toolkit
description: 仓颉标准库竞赛热路径技能。用于高频算法题中的标准库 API 精准选型与实现，重点覆盖 collection、sort、math、math_numeric、random、overflow；不承担通用标准库百科职责。
---

# Standard Library Toolkit

## 必读参考
- **标准库速查**: `references/std-hotpaths.md` — 完整 API 表 + 复杂度 + 示例

本 Skill 只保留比赛最常用、最容易写错、最影响复杂度判断的标准库热路径。更广的标准库说明留在手动参考层 `cangjie-std-*` 和 `cangjie-std-libs`。

## 首选模块

### std.collection — 容器
| 类型 | 用途 | 关键操作复杂度 |
|------|------|---------------|
| `ArrayList<T>` | 动态数组 | append O(1)摊, get/set O(1), insert O(n) |
| `HashMap<K,V>` | 哈希表 | get/put/remove O(1)期望 |
| `HashSet<T>` | 哈希集 | add/contains/remove O(1)期望 |
| `TreeMap<K,V>` | 有序映射 (红黑树) | get/put/remove O(log n), forward/backward |
| `TreeSet<T>` | 有序集 | add/contains/remove O(log n) |
| `ArrayDeque<T>` | 双端队列 | pushFirst/pushLast/popFirst/popLast O(1)摊 |
| `LinkedList<T>` | 链表 | insertAfter O(1), search O(n) |

**竞赛重点**:
- TreeMap.forward(k) = lower_bound (>= k)
- TreeMap.backward(k) = 反向迭代 (<= k)
- 用 `TreeMap<(priority, id), V>` 模拟优先队列
- 用 `TreeMap<T, Int64>` (计数值) 模拟 multiset

### std.sort — 排序
```cangjie
import std.sort.*
sort(arr)                              // 默认升序 (需 Comparable)
sort(arr) { a, b => a > b }           // 自定义比较 (降序)
sort(arr, start, len)                  // 子区间排序
sort(arr, start, len) { a, b => ... } // 子区间 + 自定义
```
- `stableSort` 同样 4 个重载，保证稳定性

### std.math — 数学
| 函数 | 说明 |
|------|------|
| `abs(x)` | 绝对值 |
| `max(a,b)` / `min(a,b)` | 最大/最小 |
| `gcd(a,b)` / `lcm(a,b)` | 最大公约数/最小公倍数 |
| `sqrt(x: Float64)` | 平方根 |
| `log(x)` / `log2(x)` | 对数 |
| `countOnes(x)` | popcount |
| `countLeadingZeros(x)` / `countTrailingZeros(x)` | 前/后导零 |
| `INF` (Float64) | 正无穷 |

### std.overflow — 溢出处理
```cangjie
import std.overflow.*
let (sum, overflow) = addWithOverflow(a, b)     // 返回 (结果, 是否溢出)
let (prod, overflow) = mulWithOverflow(a, b)
let safe = saturatingAdd(a, b)                  // 饱和加 (夹到范围)
let wrapped = wrappingAdd(a, b)                 // 回绕 (类似 C)
```

### std.convert — 类型转换
```cangjie
import std.convert.*
Int64.parse("123")         // String → Int64 (失败抛异常)
Float64.parse("3.14")      // String → Float64
x.toString()               // 数字 → String
```

## 使用原则
1. 先在 std-hotpaths.md 确认 API 语义和复杂度
2. 优先用标准库能力，避免造轮子
3. 溢出风险用 std.overflow 显式处理
4. 稳定性要求用 stableSort 而非 sort

## 必做检查
- [ ] 容器操作复杂度满足上界
- [ ] 排序稳定性与题目一致
- [ ] 数值 API 精度/范围无风险
- [ ] 都加了对应 import
