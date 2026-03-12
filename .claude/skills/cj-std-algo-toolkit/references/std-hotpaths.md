# 仓颉标准库竞赛 API 速查 (Cangjie Stdlib Quick Reference)

> **用途**: 算法竞赛中快速查阅标准库 API 签名、复杂度与用法示例。

---

## 文档路径
> 文档已复制到本技能目录: `references/docs/std/`

- docs/std/collection/ — 集合
- docs/std/sort/ — 排序
- docs/std/math/ — 数学
- docs/std/math_numeric/ — 数值
- docs/std/overflow/ — 溢出处理
- docs/std/console/ — 控制台I/O
- docs/std/io/ — 流式I/O
- docs/std/convert/ — 类型转换
- docs/std/random/ — 随机数
- docs/std/core/ — 核心类型

---

## 一、集合 (`import std.collection.*`)

### ArrayList<T> — 动态数组

| API | 复杂度 | 说明 |
|-----|--------|------|
| `ArrayList<T>()` | — | 空列表 |
| `ArrayList<T>(n, {i => ...})` | O(n) | 初始化函数构造 |
| `size: Int64` | O(1) | 长度 |
| `[i]` / `[i] = v` | O(1) | 读写 |
| `add(e)` | O(1)均摊 | 尾部添加 |
| `add(e, at: i)` | O(n) | 指定位置插入 |
| `remove(at: i): T` | O(n) | 删除 |
| `first / last` | O(1) | 返回 ?T |
| `contains(e)` | O(n) | 需 Equatable |
| `reverse()` | O(n) | 原地反转 |
| `toArray()` | O(n) | 转 Array |
| `clone()` | O(n) | 浅拷贝 |
| `slice(range)` | O(k) | 子列表 |

```cangjie
let list = ArrayList<Int64>()
list.add(1); list.add(2); list.add(3)
list[0]       // 1
list.size     // 3
list.remove(at: 1)  // 删除索引1的元素
```

### HashMap<K, V> — 哈希表 (K: Hashable & Equatable)

| API | 复杂度 | 说明 |
|-----|--------|------|
| `HashMap<K,V>()` | — | 空表 |
| `[k]` | O(1) | 读取(不存在抛异常!) |
| `get(k): ?V` | O(1) | 安全读取 |
| `[k] = v` | O(1) | 写入/更新 |
| `add(k, v): ?V` | O(1) | 添加 |
| `remove(k): ?V` | O(1) | 删除 |
| `contains(k): Bool` | O(1) | 判存 |
| `keys()` | O(1) | 键集合 |
| `values()` | O(1) | 值集合 |
| `size` | O(1) | 大小 |

```cangjie
let freq = HashMap<Int64, Int64>()
freq[x] = (freq.get(x) ?? 0) + 1   // 计数惯用法
freq.contains(x)                     // 判存
for ((k, v) in freq) { }             // 遍历
```

### HashSet<T> — 哈希集合 (T: Hashable & Equatable)

| API | 复杂度 | 说明 |
|-----|--------|------|
| `add(e): Bool` | O(1) | 添加 |
| `remove(e): Bool` | O(1) | 删除 |
| `contains(e): Bool` | O(1) | 判存 |
| `& \| -` | O(n) | 交/并/差集 |

```cangjie
let s = HashSet<Int64>()
s.add(1); s.add(2)
s.contains(1)     // true
```

### TreeMap<K, V> — 有序映射 (K: Comparable, 红黑树)

| API | 复杂度 | 说明 |
|-----|--------|------|
| 增删查同 HashMap | O(log n) | |
| `first: ?(K,V)` | O(log n) | 最小键 |
| `last: ?(K,V)` | O(log n) | 最大键 |
| `removeFirst() / removeLast()` | O(log n) | 删除最小/最大 |
| `forward(k, inclusive: true)` | O(log n) | **>=k 升序迭代器** |
| `backward(k, inclusive: true)` | O(log n) | **<=k 降序迭代器** |

```cangjie
let tm = TreeMap<Int64, Int64>()
tm.add(3, 30); tm.add(1, 10); tm.add(5, 50)
tm.first   // Some((1, 10))
// lower_bound(x) 等效:
let it = tm.forward(x)  // >= x 的第一个元素开始
```

> **竞赛关键**: TreeMap 的 `forward`/`backward` 可实现 C++ `lower_bound`/`upper_bound` 等效操作。

> **⚠️ 严重警告**: 仓颉 Tuple 未实现 `Comparable`，**不可作为 TreeMap/TreeSet 的 Key**！
> 要模拟 `TreeMap<(dist,node), V>` 的效果，请将多元组编码为单个 Int64: `key = d * MAXN + node`。

### TreeSet<T> — 有序集合 (T: Comparable, 红黑树)

同 TreeMap 但无 Value, API 类似 HashSet + forward/backward。

### ArrayDeque<T> — 双端队列

| API | 复杂度 |
|-----|--------|
| `addFirst(e) / addLast(e)` | O(1)均摊 |
| `removeFirst() / removeLast(): ?T` | O(1) |
| `first / last: ?T` | O(1) |

### ArrayQueue<T> — 队列 (FIFO)

| API | 说明 |
|-----|------|
| `add(e)` | 入队 |
| `remove(): ?T` | 出队 |
| `peek(): ?T` | 查看队头 |

### ArrayStack<T> — 栈 (LIFO)

| API | 说明 |
|-----|------|
| `add(e)` | 压栈 |
| `remove(): ?T` | 出栈 |
| `peek(): ?T` | 查看栈顶 |

### LinkedList<T> — 双向链表

| API | 说明 |
|-----|------|
| `addFirst/addLast` | O(1) |
| `removeFirst/removeLast` | O(1) |
| `nodeAt(i)` | O(n) |
| `splitOff(node)` | 分割 |

---

## 二、函数式集合操作 (`std.collection`)

```cangjie
import std.collection.*

// 管道风格 (|>) 或直接调用
arr |> filter { x: Int64 => x > 0 } |> collectArray
arr |> map { x: Int64 => x * 2 } |> collectArrayList
arr |> fold(0, { acc: Int64, x: Int64 => acc + x })

// 常用函数
map(f)                  // 映射
filter(pred)            // 过滤
fold(init, op)          // 累积
reduce(op)              // 用首元素做初始值
flatMap(f)              // 映射+展平
enumerate(iter)         // (index, value)
zip(iter2)              // 合并两个迭代器
all(pred) / any(pred)   // 全部/任一满足
min(iter) / max(iter)   // 最值 (需 Comparable)
count(iter)             // 计数
collectArray(iter)      // 迭代器 -> Array
collectArrayList(iter)  // 迭代器 -> ArrayList
collectHashMap(iter)    // 迭代器 -> HashMap
collectHashSet(iter)    // 迭代器 -> HashSet
```

---

## 三、排序 (`import std.sort.*`)

```cangjie
import std.sort.*

// 对 Array / ArrayList 排序
sort(arr)                                  // 升序 (T: Comparable)
sort(arr, descending: true)                // 降序
sort(arr, stable: true)                    // 稳定排序
sort(arr, stable: true, descending: true)  // 稳定降序

// 自定义比较 (返回 Ordering: LT/EQ/GT)
sort(arr, by: { a, b =>
    if (a < b) { Ordering.LT }
    else if (a > b) { Ordering.GT }
    else { Ordering.EQ }
})

// 按键排序
sort(arr, key: { x => keyExpr })

// lessThan 风格
sort(arr, lessThan: { a, b => a < b })
```

> **Ordering 枚举**: `Ordering.LT`, `Ordering.EQ`, `Ordering.GT`

---

## 四、数学 (`import std.math.*`)

### 高频函数

| 函数 | 说明 |
|------|------|
| `abs(x)` | 绝对值 (Int64/Float64) |
| `gcd(a, b)` | 最大公约数 |
| `lcm(a, b)` | 最小公倍数 |
| `sqrt(x)` | 平方根 (Float64) |
| `pow(base, exp)` | 幂 (Float64) |
| `log(x) / log2(x) / log10(x)` | 对数 |
| `floor(x) / ceil(x) / round(x)` | 取整 |
| `clamp(x, min, max)` | 夹紧 |
| `countOnes(x)` | popcount |
| `leadingZeros(x)` | 前导零 |
| `trailingZeros(x)` | 尾随零 |

### 数学常数 (`import std.math_numeric.*`)

```cangjie
Float64.getPI()     // π
Float64.getE()      // e
Float64.getInf()    // ∞
Float64.isNaN(x)    // 判断 NaN
```

---

## 五、溢出处理 (`import std.overflow.*`)

| 策略 | 方法示例 | 溢出行为 |
|------|----------|----------|
| Checked | `a.checkedAdd(b): ?Int64` | 返回 None |
| Saturating | `a.saturatingAdd(b): Int64` | 返回 MAX/MIN |
| Wrapping | `a.wrappingAdd(b): Int64` | 截断取模 |
| Carrying | `a.carryingAdd(b): (Bool, Int64)` | (是否溢出, 结果) |
| Throwing | `a.throwingAdd(b): Int64` | 抛异常 |

每种策略均有: Add, Sub, Mul, Div, Mod, Neg, Shl, Shr, Pow

```cangjie
import std.overflow.*
let r = Int64.Max.checkedAdd(1)      // None
let r2 = Int64.Max.saturatingAdd(1)  // Int64.Max
let (ov, r3) = Int64.Max.carryingAdd(1) // (true, Int64.Min)
```

---

## 六、I/O

### 内置全局函数 (无需 import)
```cangjie
print("hello")       // 不换行
println("hello")     // 换行
let line = readln()   // 读一行, 返回 String
```

### Console (`import std.console.*`)
```cangjie
let line: ?String = Console.stdIn.readln()  // 返回 ?String
let ch: ?Rune = Console.stdIn.read()        // 单字符
```

### 竞赛 I/O 模式
```cangjie
import std.convert.*

let n = Int64.parse(readln())
let parts = readln().split(" ")
let a = Array<Int64>(n, {i => Int64.parse(parts[i])})
println(result)
```

---

## 七、集合接口层级

```
Collection<T>
├── Deque<T>         -> ArrayDeque
├── Queue<T>         -> ArrayQueue
├── Stack<T>         -> ArrayStack
├── ReadOnlyList<T>
│   └── List<T>      -> ArrayList
├── ReadOnlyMap<K,V>
│   └── Map<K,V>     -> HashMap
│       └── OrderedMap<K,V> -> TreeMap
├── ReadOnlySet<T>
│   └── Set<T>       -> HashSet
│       └── OrderedSet<T>  -> TreeSet
└── EquatableCollection<T>
```

---

## 八、竞赛高频模式速记

```cangjie
import std.convert.*
import std.collection.*
import std.sort.*
import std.math.*

main() {
    // 读入
    let n = Int64.parse(readln())
    let parts = readln().split(" ")
    let a = Array<Int64>(n, {i => Int64.parse(parts[i])})

    // 排序
    sort(a)                          // 升序
    sort(a, descending: true)        // 降序

    // HashMap 计数
    let freq = HashMap<Int64, Int64>()
    for (x in a) { freq[x] = (freq.get(x) ?? 0) + 1 }

    // TreeMap 有序查询
    let tm = TreeMap<Int64, Int64>()
    tm.add(key, value)
    let it = tm.forward(x)           // >= x 的迭代器

    // GCD/LCM
    let g = gcd(a, b)

    // 栈/队列
    let stk = ArrayStack<Int64>()
    stk.add(1); stk.peek(); stk.remove()
    let q = ArrayQueue<Int64>()
    q.add(1); q.peek(); q.remove()
    let dq = ArrayDeque<Int64>()
    dq.addFirst(1); dq.addLast(2)

    // 输出
    println(ans)
}
```

---

## 九、TreeMap 模拟优先队列

仓颉标准库无 `PriorityQueue`，用 `TreeMap<Int64, Int64>` 模拟。

### 最小堆

```cangjie
let pq = TreeMap<Int64, Int64>()  // key=编码值, value=计数(或占位)
var uid: Int64 = 0  // 全局唯一 ID，防止值相同时覆盖

func pqPush(val0: Int64): Unit {
    let key = val0 * 10000000 + uid  // 高位放值，低位放 uid 保证唯一
    uid++
    pq.add(key, val0)
}

func pqPeek(): Int64 {
    let it = pq.iterator()           // 最小 key 在最前
    let (_, v) = it.next()
    return v
}

func pqPop(): Int64 {
    let it = pq.iterator()
    let (k, v) = it.next()
    pq.remove(k)
    return v
}
```

### 最大堆

```cangjie
// 取反编码: key = -val * 10000000 + uid
func pqPushMax(val0: Int64): Unit {
    let key = -val0 * 10000000 + uid
    uid++
    pq.add(key, val0)
}
// pqPeek / pqPop 同上
```

**⚠️ 编码注意**: `uid` 上限不超过 10⁷（与编码因子匹配），否则会串位。如果 n > 10⁷，改用更大的因子（如 10⁹）。

---

## 十、竞赛高频数学工具

### 10.1 快速幂

```cangjie
func power(base: Int64, exp: Int64, mod: Int64): Int64 {
    var result: Int64 = 1
    var b = base % mod; var e = exp
    while (e > 0) {
        if ((e & 1) == 1) { result = result * b % mod }
        b = b * b % mod
        e >>= 1
    }
    return result
}
```

### 10.2 逆元

```cangjie
// 费马小定理: a^(-1) ≡ a^(p-2) (mod p), p 是质数
func modInv(a: Int64, p: Int64): Int64 { return power(a, p - 2, p) }
```

### 10.3 组合数（预处理阶乘）

```cangjie
let MAXN: Int64 = 200001
let MOD: Int64 = 1000000007
let fac = Array<Int64>(MAXN, {_ => 0})
let inv = Array<Int64>(MAXN, {_ => 0})

func initComb(): Unit {
    fac[0] = 1
    var i: Int64 = 1
    while (i < MAXN) { fac[i] = fac[i - 1] * i % MOD; i++ }
    inv[MAXN - 1] = power(fac[MAXN - 1], MOD - 2, MOD)
    i = MAXN - 2
    while (i >= 0) { inv[i] = inv[i + 1] * (i + 1) % MOD; i-- }
}

func comb(n: Int64, k: Int64): Int64 {
    if (k < 0 || k > n) { return 0 }
    return fac[n] * inv[k] % MOD * inv[n - k] % MOD
}
```

### 10.4 溢出安全乘法

```cangjie
import std.overflow.*

// 当 a * b 可能超 Int64 范围时:
let (hi, lo) = a.carryingMul(b)  // 128 位结果
// 或用 checkedMul 检测溢出:
try { let c = a.checkedMul(b) } catch (e: OverflowException) { /* 溢出 */ }

// 取模场景: 若 a, b < 10^18, a*b 会溢出
// 方案1: 先取模再乘 → (a % mod) * (b % mod) % mod (仍可能溢出如果 mod > 3×10^9)
// 方案2: 使用 Int128 或 __int128 (仓颉暂不支持) → 拆分乘法
// 方案3: 龟速乘(O(log n))
func mulMod(a: Int64, b: Int64, mod: Int64): Int64 {
    var result: Int64 = 0
    var base = a % mod
    var exp = if (b < 0) { -b } else { b }
    while (exp > 0) {
        if ((exp & 1) == 1) { result = (result + base) % mod }
        base = (base + base) % mod
        exp >>= 1
    }
    return if (b < 0) { mod - result } else { result }
}
```
