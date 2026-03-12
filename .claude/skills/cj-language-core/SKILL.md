---
name: cj-language-core
description: 仓颉算法题实现阶段的语言核心技能。用于语法正确性、常用导入、竞赛常见坑、泛型约束、Option/异常处理和可编译代码组织；不是通用仓颉语言百科。
---

# Cangjie Language Core

## 必读参考
- **语法速查**: `references/core-map.md` — 仓颉语法完整快速参考

## 聚焦范围
竞赛中最常用的仓颉语法特性：

本 Skill 只服务算法题实现阶段。更完整的语言知识放在手动参考层 `cangjie-*` 中，不应在比赛场景自动拉入。

### 程序入口
```cangjie
main() {                     // 不需要 func 关键字
    println("hello")
}
```

### 变量与类型
```cangjie
let x: Int64 = 42           // 不可变
var y = 0                    // 可变，类型推导
let arr = Array<Int64>(n, {i => 0})  // n 个 0
var list = ArrayList<Int64>()
```

### I/O 模式 (竞赛必备)
```cangjie
import std.convert.*         // 必须！否则 Int64.parse 不可用
let n = Int64.parse(readln())
let parts = readln().split(" ")
let a = Int64.parse(parts[0])
println(result)
```

### 关键语法速记
| 特性 | 语法 | 注意 |
|------|------|------|
| Range | `0..n` (左闭右开) `0..=n` (左闭右闭) | for 循环用 |
| 数组创建 | `Array<T>(size, {i => initVal})` | lambda 初始化 |
| Option | `?T`, `Some(v)`, `None`, `getOrThrow()` | HashMap.get 返回 |
| 模式匹配 | `match (x) { case p => ... }` | |
| Lambda | `{x: Int64 => x * 2}` 或 `{x => x * 2}` | |
| 字符串格式化 | `"value = ${expr}"` | 插值 |
| 位操作 | `& \| ^ ! << >>` | 同 C++ |

### 竞赛常见错误
| 错误 | 原因 | 修复 |
|------|------|------|
| `Int64.parse` 编译失败 | 缺 import | `import std.convert.*` |
| 数组越界 panic | 未检查边界 | 先判 `if (i >= 0 && i < arr.size)` |
| HashMap 取值崩溃 | 用了 `[]` 不存在的键 | 用 `get(k)` 返回 Option |
| sort 不识别 | 缺 import | `import std.sort.*` |
| 修改数组元素失败 | Array 是固定大小 | 用 `arr[i] = val` 可修改值，但不能 append |
| 泛型类没有 sort | 需要 Comparable 约束 | `<T> where T <: Comparable<T>` |

### struct vs class
| | struct | class |
|---|--------|-------|
| 类型 | 值类型 | 引用类型 |
| 继承 | 不可继承 | 可继承 |
| 赋值 | 拷贝 | 共享引用 |
| 竞赛建议 | 简单数据 (点/边) | 复杂对象 |

### 包导入速记
```cangjie
import std.collection.*      // ArrayList, HashMap, HashSet, TreeMap...
import std.convert.*          // Int64.parse, Float64.parse
import std.sort.*             // sort(), stableSort(), SortExtension
import std.math.*             // abs, max, min, gcd, lcm, sqrt, countOnes...
import std.overflow.*         // addWithOverflow, mulWithOverflow...
import std.random.*           // Random
import std.console.*          // Console (一般不需要，readln 在 core)
```

## 实现策略
1. **代码优先可编译**，再优化表达
2. 泛型约束必须显式写出
3. Option 分支要处理 None
4. 所有 import 放代码最顶部
5. main() 不加 func 关键字

## 引用策略
涉及语法规则时必须附用户手册证据引用。
文档路径: `references/docs/user_manual/` 下对应章节 (本技能目录内)。
