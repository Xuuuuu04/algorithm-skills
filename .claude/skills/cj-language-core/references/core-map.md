# 仓颉语法竞赛速查表 (Cangjie Syntax Quick Reference)

> **用途**: 算法竞赛中快速查阅仓颉语法，避免语法错误浪费时间。

## 文档路径
> 文档已复制到本技能目录: `references/docs/user_manual/`

- docs/user_manual/basic_data_type/
- docs/user_manual/function/
- docs/user_manual/generic/
- docs/user_manual/error_handle/
- docs/user_manual/struct/
- docs/user_manual/class_and_interface/
- docs/user_manual/enum_and_pattern_match/
- docs/user_manual/collections/
- docs/user_manual/Basic_IO/
- docs/user_manual/basic_programming_concepts/
- docs/user_manual/package/
- docs/user_manual/Appendix/
- docs/user_manual/concurrency/
- docs/user_manual/extension/
- docs/user_manual/Macro/
- docs/user_manual/compile_and_build/
- docs/user_manual/first_understanding/
- docs/user_manual/deploy_and_run/
- docs/user_manual/FFI/
- docs/user_manual/Net/
- docs/user_manual/reflect_and_annotation/

---

## 1. 程序入口

```cangjie
main() {
    // main 前面不加 func
}

main(): Int64 {
    return 0
}
```

---

## 2. 变量与常量

```cangjie
let x: Int64 = 10      // 不可变
var y: Int64 = 20       // 可变
const MOD: Int64 = 1000000007  // 编译期常量

// 类型推断
let a = 100     // Int64
var b = 3.14    // Float64
```

---

## 3. 基础类型

| 类型 | 说明 |
|------|------|
| `Int64` | 默认整数类型, -2^63 ~ 2^63-1 |
| `Float64` | 默认浮点类型, IEEE 754 |
| `Bool` | `true` / `false` |
| `String` | UTF-8 不可变字符串 |
| `Rune` | 单个 Unicode 字符, `UInt32(rune)` 取码点 |
| `Byte` | UInt8 别名 |
| `?T` | Option<T>, Some(v) 或 None |

---

## 4. 类型转换

```cangjie
import std.convert.*

// 数值互转: T(expr)
Float64(a)          // Int64 -> Float64
Int64(3.14)         // Float64 -> Int64 (截断)
UInt32(r'a')        // Rune -> UInt32 (码点 97)
Int64(UInt32(r'a')) // Rune -> Int64

// 字符串 -> 数值
Int64.parse("123")      // 失败抛异常
Float64.parse("-3.14")

// 数值 -> 字符串
42.toString()       // "42"
"${42}"             // "42"
```

---

## 5. 字符串

```cangjie
s.size                          // 字节长度
s.contains("abc")               // Bool
"1 2 3".split(" ")              // ["1", "2", "3"]
"1,,2".split(",", removeEmpty: true)
s.replace("old", "new")
s.trimAscii()                   // 去首尾空白
"abc" + "def"                   // 拼接
"x=${x}"                        // 插值
s.toArray()                     // Array<Byte>
for (ch in s) { }               // 遍历 Byte (UInt8 值)
for (ch in s.runes()) { }       // 遍历 Rune (Unicode 字符)
```

---

## 6. 数组 Array

```cangjie
let a = [1, 2, 3]
let b = Array<Int64>(n, {_ => 0})       // n 个 0
let c = Array<Int64>(n, {i => i + 1})    // 1..n

a[0]        // 访问
a[0] = 99   // 修改
a.size      // 长度
a[1..3]     // 切片 [a[1], a[2]]

// 警告: Array 赋值共享引用
let y = x   // y 和 x 指向同一数据
// 独立副本: Array(a.size, {i => a[i]})
```

---

## 7. 控制流

```cangjie
// if (可作表达式)
let abs = if (x >= 0) { x } else { -x }

// while
while (i < n) { i++ }

// for-in
for (i in 0..n) { }         // [0, n)
for (i in 0..=n) { }        // [0, n]
for (i in 0..n : 2) { }     // 步长 2
for (i in n-1..=0 : -1) { } // 逆序

// match
match (x) {
    case 0 => "zero"
    case n where n > 0 => "positive"
    case _ => "other"
}

// 无匹配值 match
match {
    case x > 0 => "pos"
    case _ => "non-pos"
}
```

---

## 8. 函数 & Lambda

```cangjie
func add(a: Int64, b: Int64): Int64 { a + b }

// Lambda
let f = { a: Int64, b: Int64 => a + b }

// 命名参数 + 默认值
func solve(n!: Int64, mod!: Int64 = 1000000007): Int64 { ... }
// 调用: solve(n: 10, mod: 998244353)

// 函数参数不可变(let 语义)
```

---

## 9. Struct / Class / Enum / Option

```cangjie
// Struct (值类型)
struct Point {
    var x: Int64; var y: Int64
    public init(x: Int64, y: Int64) { this.x = x; this.y = y }
}

// Class (引用类型)
class Node {
    var val: Int64; var next: ?Node
    public init(val: Int64) { this.val = val; this.next = None }
}

// 继承
open class Base { public open func f() { } }
class Derived <: Base { public override func f() { } }

// Interface
interface Printable { func display(): String }
class Item <: Printable { public func display(): String { "item" } }

// Enum
enum Color { | Red | Green | Blue }
enum Expr { | Num(Int64) | Add(Expr, Expr) }

// Option
let a: ?Int64 = Some(42)
a.getOrThrow()    // 42
a ?? 0            // 42, None -> 0
```

---

## 10. 泛型

```cangjie
func maxVal<T>(a: T, b: T): T where T <: Comparable<T> {
    if (a > b) { a } else { b }
}

// 关键约束:
// Comparable<T>               -> TreeMap/TreeSet 键
// Hashable & Equatable<T>    -> HashMap/HashSet 键
```

---

## 11. 异常处理

```cangjie
try {
    Int64.parse("abc")
} catch (e: Exception) {
    println("${e}")
}
throw Exception("error")
```

---

## 12. 操作符重载

```cangjie
class Vec {
    var x: Int64; var y: Int64
    public init(x: Int64, y: Int64) { this.x = x; this.y = y }
    public operator func +(r: Vec): Vec { Vec(x + r.x, y + r.y) }
    public operator func <(r: Vec): Bool { x < r.x || (x == r.x && y < r.y) }
}
```

---

## 13. 常见陷阱速查

| 陷阱 | 解决 |
|------|------|
| Array 共享引用 | `Array(a.size, {i => a[i]})` 拷贝 |
| 整数溢出抛异常 | `import std.overflow.*` |
| Tuple 不可做 TreeMap 键 | Tuple 未实现 Comparable, 编码为 Int64 |
| `map[key]` 不存在抛异常 | 用 `map.get(key)` 返回 `?V` |
| 函数参数不可变 | 赋给 `var` |
| `0..n` 不含 n | 用 `0..=n` |
| `Int64.parse` 需导入 | `import std.convert.*` |
| `&`/`\|` 优先级低于 `==` | `(e & 1) == 1` 而非 `e & 1 == 1` |
| 递归嵌套函数需标注返回类型 | `func dfs(...): Unit {` |
| init 闭包不可引用未初始化成员 | `let v = 20; this.a = Array(n, {_ => f(v)})` |
| Rune 不能直接转 Int64 | `Int64(UInt32(rune))` |
| `extend` 是关键字 | 方法名用 `addChar` 等替代 |
| struct 无自动命名构造器 | 需定义 `init(a: Int64, b: Int64)` + 位置调用 |
| `while(true)` 在非 Unit 函数 | 改用 `var r=init; while(r==init){...}; return r` |

---

## 14. 竞赛常见高级陷阱

### 14.1 递归栈深度

仓颉默认线程栈大小有限（通常数 MB），深度递归（> 10⁴ 层）可能导致栈溢出。

**应对策略**：
- 深度可能达 10⁵ 的 DFS/递归 → 改写为 **BFS** 或 **手动栈**（用 `ArrayStack`）
- 如果递归深度 ≤ 数千层（如 log₂n ≤ 20），递归安全
- 线段树递归深度 = O(log n) ≤ 17 层，安全
- 树的 DFS 若为链状（n=10⁵），必须用非递归

```cangjie
// 手动栈代替递归 DFS
let stk = ArrayStack<Int64>()
stk.add(root)
while (!stk.isEmpty()) {
    let u = stk.remove()  // pop
    for (v in adj[u]) {
        if (!visited[v]) { visited[v] = true; stk.add(v) }
    }
}
```

### 14.2 位运算完整参考

```cangjie
// 基本位运算
let and0 = a & b       // 按位与
let or0 = a | b        // 按位或
let xor0 = a ^ b       // 按位异或
let not0 = ~a           // 按位取反（Int64 补码）
let shl = a << k        // 左移 k 位
let shr = a >> k        // 算术右移（保留符号位）

// ⚠️ 优先级陷阱: & | ^ 优先级低于 ==
let ok = (a & 1) == 1   // ✅ 正确
// let ok = a & 1 == 1   // ❌ 语义等于 a & (1 == 1)

// lowbit: 最低位的 1
let lowbit = x & (-x)

// 判断是否为 2 的幂
let isPow2 = x > 0 && (x & (x - 1)) == 0

// 枚举子集
var sub = mask
while (sub > 0) {
    // 处理子集 sub
    sub = (sub - 1) & mask
}

// 位计数（需要 std.math.*）
let ones = countOnes(x)           // popcount
let lz = x.leadingZeros()         // 前导零
let tz = x.trailingZeros()        // 尾部零
let highBit = 63 - x.leadingZeros()  // 最高位位置
```

### 14.3 Float64 精度警告

```cangjie
// ⚠️ 浮点比较禁止用 ==
let EPS: Float64 = 1e-9
let equal = (a - b).abs() < EPS    // ε 比较

// ⚠️ 大整数转 Float64 丢精度
// Int64 有效位 63, Float64 尾数 52 位 → 超过 2^53 的整数不精确
let big: Int64 = 9007199254740993  // 2^53 + 1
let f = Float64(big)               // 丢失末位 → 不等于 big

// 建议: 竞赛中尽量用 Int64 做整数运算, 只在几何题等必须时用 Float64
// 几何题输出: 使用指定精度格式化
// println("${String.format("%.10f", ans)}")  // 保留10位小数
```

### 14.4 Array vs ArrayList 性能对比

| 操作 | `Array<T>` | `ArrayList<T>` |
|------|-----------|---------------|
| 随机访问 `[i]` | O(1) ★ | O(1) |
| 修改 `[i] = v` | O(1) ★ | O(1) |
| 末尾添加 | 不支持（固定大小） | O(1) 均摊 |
| 头部插入 | 不支持 | O(n) |
| 遍历 | O(n) ★ 缓存友好 | O(n) |
| 内存 | 紧凑，无额外开销 ★ | 有扩容预留空间 |

**竞赛选择原则**：
- **大小固定**（dp 数组、邻接矩阵、BIT）→ 用 `Array`
- **大小动态**（邻接表、结果收集）→ 用 `ArrayList`
- **性能敏感路径**（线段树、BIT 内部数组）→ 必须用 `Array`

### 14.5 快速 I/O

默认 `readln()` + `println()` 对大多数题目足够（n ≤ 10⁵）。当输入/输出量极大时（n ≥ 5×10⁵ 行），考虑批量读取。

```cangjie
// 批量输出: 用 StringBuilder 拼接后一次输出
let sb = StringBuilder()
for (x in results) {
    sb.append(x.toString())
    sb.append("\n")
}
print(sb.toString())
```

**注意**: 仓颉竞赛环境中一般不需要像 C++ 那样关闭同步流，`readln()`/`println()` 已足够快。

---

## 15. 竞赛文件头

```cangjie
import std.convert.*
import std.collection.*
import std.sort.*
import std.math.*

main() {
    let n = Int64.parse(readln())
    // ...
    println(ans)
}
```
