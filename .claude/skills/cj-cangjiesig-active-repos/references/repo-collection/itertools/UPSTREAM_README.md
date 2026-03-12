[English](./README_EN.md) | 中文

<div align="center">
<h1>itertools</h1>
</div>

<p align="center">
<img alt="" src="https://img.shields.io/badge/release-v2.0.0-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/cjc-v1.0.4-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/state-孵化-brightgreen" style="display: inline-block;" />
<img alt="" src="https://img.shields.io/badge/domain-Demo-brightgreen" style="display: inline-block;" />
</p>

## 介绍

Cangjie 语言下的惰性迭代器工具库，灵感来自 Rust `itertools`。提供标准库 `Iterator<T>` 没有的高级迭代器功能，包括生成器、索引、预览、组合学、去重、条件处理等惰性适配器，以及折叠、查找、聚合、分组、排序、比较等终止操作。

### 项目特性

- **生成器适配器**：`iterate`、`repeatN`、`unfold` 等无限/有限序列生成
- **索引与位置**：`enumerate`、`positions`、`withPosition` 等位置标记功能
- **预览与回退**：`multipeek`、`putBack`、`putBackN` 等灵活的迭代控制
- **组合学适配器**：笛卡尔积、组合、排列、幂集等
- **去重与条件**：全局去重、连续去重、条件终止等
- **丰富的终止操作**：折叠、查找、聚合、分组、排序、比较等
- **并行迭代器**（v2.0）：利用协程实现高效并行处理
- **类型安全迭代器**（v2.0）：NonEmptyIterator、SortedIterator、UniqueIterator
- **高级统计功能**（v2.0）：中位数、百分位数、众数、协方差、相关系数、直方图
- **时间序列操作**（v2.0）：移动平均、指数移动平均、滞后、超前
- **调试工具**（v2.0）：性能分析、跟踪

### v2.0.0 新增功能

#### 标准库生态集成

**收集器模块 (stdlib/collectors.cj)**
提供将迭代器收集到标准库集合类型的功能：
- **toHashSet**：收集到 HashSet，自动去重
- **toHashMap**：收集键值对到 HashMap
- **toHashMapBy**：使用键/值函数收集到 HashMap
- **toLinkedList**：收集到 LinkedList（保持顺序）
- **collectToString**：收集字符迭代器为字符串
- **fromArrayList/fromHashSet/fromHashMap**：集合转迭代器

**集合扩展方法 (stdlib/collection_ext.cj)**
为标准库集合类型添加 itertools 风格的扩展方法：
- ArrayList：`iter()`, `iterChunks()`, `iterWindows()`, `iterEnumerate()`, `iterReverse()`
- HashMap：`iterKeys()`, `iterValues()`, `iterEntries()`
- HashSet：`iter()`, `iterDifference()`

**Comparable 接口集成 (stdlib/comparable_ext.cj)**
为实现 Comparable 接口的类型提供便捷操作：
- **sorted**：自然排序
- **minValue/maxValue**：获取最小/最大值
- **minmaxValue**：同时获取最小和最大值

**Option/Result 迭代器 (stdlib/option_iter.cj, result_iter.cj)**
将 Option 和 Result 类型视为迭代器：
- **optionIter**：Option 转 0/1 元素迭代器
- **resultOkIter/resultErrIter**：Result 的 Ok/Err 值迭代器

**字符串迭代器 (stdlib/string_iter.cj)**
字符串的惰性迭代操作：
- **stringChars**：字符迭代器
- **stringLines**：行迭代器
- **stringWords**：单词迭代器
- **stringSplit**：分割迭代器

**切片和反向迭代器 (stdlib/slice_iter.cj, collection_ext.cj)**
- **sliceIter**：数组切片迭代器，支持负索引
- **reverseIter/reversed**：反向迭代器

**惰性字符串构建器 (stdlib/lazy_string.cj)**
- **LazyJoiner**：惰性字符串连接器
- **lazyJoin/lazyFormat**：惰性字符串构建函数

**并行收集器 (parallel/par_collectors.cj)**
- **parCollectToArrayList**：并行收集到 ArrayList
- **parCollectToHashSet**：并行收集到 HashSet
- **parCollectToHashMap**：并行收集到 HashMap

#### 惰性求值优化

**融合适配器 (adapters/fusion.cj)**
提供迭代器融合操作，将多个连续操作合并为单一遍历，减少中间分配：
- **filterMap**：map+filter 融合，对每个元素应用函数 f，保留 Some 值，过滤 None 值
- **mapFilter**：filter+map 融合，先应用 map，再应用 filter
- **composeMap**：map+map 融合，将两个变换组合为单一变换 g(f(x))
- **andFilter**：filter+filter 融合，将两个谓词合并为单一测试 p1(x) && p2(x)
- **slice**：skip+take 融合，高效获取序列的 [start, end) 范围

**短路计数操作 (terminals/short_circuit.cj)**
提供带计数的短路操作，返回结果和实际检查的元素数量：
- **anyWithCount**：带计数的 any 操作，返回 (Bool, Int64)
- **allWithCount**：带计数的 all 操作，返回 (Bool, Int64)
- **findWithCount**：带计数的 find 操作，返回 (Option<T>, Int64)
- **containsWithCount**：带计数的 contains 操作，返回 (Bool, Int64)

**惰性验证工具 (adapters/lazy_debug.cj)**
提供用于验证和调试惰性求值行为的工具：
- **countingIterator**：计数迭代器，跟踪 next() 调用次数
- **assertLazy**：断言惰性迭代器，检测过度消费

#### 高级统计功能
- **中位数和百分位数**：`median`、`medianFloat`、`percentile`、`percentileFloat`
- **众数**：`mode` - 返回出现频率最高的元素
- **协方差和相关系数**：`covariance`、`correlation` - 分析两个序列的关系
- **直方图**：`histogram`、`histogramBy` - 数据分布可视化

#### 时间序列操作
- **移动平均**：`movingAverage`、`movingAverageInt` - 简单移动平均
- **指数移动平均**：`exponentialMovingAverage` - 给予近期数据更高权重
- **滞后/超前**：`lag`、`lead` - 访问前/后 n 个元素

#### 并行迭代器
- **parMap**：并行映射，保持输出顺序
- **parFilter**：并行过滤，保持输出顺序
- **parReduce**：并行归约，使用分治策略
- **ParallelConfig**：并行执行配置

#### 类型安全迭代器
- **NonEmptyIterator**：编译时保证至少有一个元素
  - `firstValue()`、`reduceValue()`、`lastValue()` 总是成功
- **SortedIterator**：编译时保证元素已排序
  - `merge()`、`union()`、`intersection()`、`binarySearch()` 优化操作
- **UniqueIterator**：编译时保证没有重复元素
  - `containsValue()` O(1) 查找

#### 函数式编程增强
- **scan1**：无初始值的扫描适配器
- **unfoldN**：有限展开生成器，产生恰好 n 个元素
- **converge**：收敛迭代生成器
- **fixpoint**、**fixpointFloat**：查找不动点

#### 调试工具
- **profile**：性能分析适配器，测量迭代器操作的性能
- **trace**：跟踪适配器，记录每个元素的流动

#### 其他增强

### v1.5.0 功能

- **步进迭代器**：`stepBy(xs, step)` - 每隔 n 个元素产出一个，支持数据降采样
- **惰性分组**：`lazyGroupBy(xs, keyFn)` - 惰性分组迭代器，不预先消费整个序列
- **多路分叉**：`teeN(xs, n)` - 将迭代器分叉为 N 个独立副本
- **Try 系列操作**：`tryForEach`、`tryFold`、`tryFind`、`tryAll`、`tryAny` - 可中断的迭代操作
- **数值统计终止操作**：`average`、`variance`、`stddev` - 算术平均值、方差、标准差
- **数值统计适配器**：`runningSum`、`runningAverage`、`differences` - 累计和、累计平均、差分
- **有序集合操作**：`unionBy`、`intersectionBy`、`differenceBy`、`symmetricDifferenceBy` - 并集、交集、差集、对称差集
- **排序算法优化**：`sortedBy` 使用归并排序（O(n log n) 稳定排序），小数组使用插入排序优化
- **窗口操作增强**：`slidingWindow(xs, size, step)` - 带步长的滑动窗口，`mapWindows(xs, size, f)` - 映射窗口
- **调试辅助工具**：`inspectWithIndex(xs, f)` - 带索引的检查，`tap(xs, f)` - 每次迭代前执行动作

### v1.4.0 新增功能

- **性能优化**：`kSmallest`/`kLargest`/`kmerge` 使用堆优化，从 O(n log n) 或 O(n*k) 降至 O(n log k)
- **内部堆实现**：`BinaryHeap` - 内部二叉堆数据结构，支持 max-heap 和 min-heap
- **Top-K 增强**：`kSmallestByKey`、`kLargestByKey` - 按键函数返回 k 个最小/最大元素
- **Relaxed Top-K**：`kSmallestRelaxed`、`kLargestRelaxed`、`kSmallestRelaxedByKey`、`kLargestRelaxedByKey` - O(n + k log k) 时间 O(2k) 空间
- **尾部获取**：`tail(xs, n)` - 返回迭代器的最后 n 个元素（环形缓冲区实现）
- **Result 归约**：`tryReduce` - 对 Result 流归约，归约函数返回 Result，遇 Err 提前终止
- **展平适配器**：`flattenOk` - 展平 Result 流中 Ok 值的内部可迭代对象
- **条件获取**：`peekingTakeWhile` - 使用 peek 的条件获取，不消费边界元素
- **更新适配器**：`update` - 对每个元素应用更新函数
- **分组映射**：`intoGroupingMap`、`intoGroupingMapBy` - 灵活的分组 API，支持 fold/reduce/minBy/maxBy 等聚合
- **元组拆分**：`multiunzip2`、`multiunzip3` - 将元组迭代器拆分为多个 ArrayList
- **格式化**：`formatWith` - 使用分隔符和格式化函数生成字符串
- **位置查找**：`positionMinmaxByKey` - 按键同时查找最小和最大元素位置

### v1.3.0 新增功能

- **Result 流映射适配器**：`mapOk`、`mapErr` - 映射 Result 流中的 Ok/Err 值
- **Result 流过滤适配器**：`filterOkBy`、`filterMapOk` - 按谓词过滤 Ok 值，保留 Err
- **Result 流终止操作**：`foldOk`、`reduceOk`、`tryCollect` - 折叠和收集 Result 流
- **Option 流终止操作**：`foldOptions` - 折叠 Option 流，遇到 None 时停止
- **条件终止适配器**：`takeWhileInclusive` - 包含边界的条件终止
- **聚合增强**：`minmax`、`minmaxByKey` - 一次遍历同时获取最小和最大值
- **范围索引操作**：`getRange`、`getNth` - 获取指定范围或位置的元素

### v1.2.0 新增功能

- **去重增强**：`dedupWithCount`、`dedupByWithCount`、`duplicates`、`duplicatesBy`
- **位置查找**：`positionMinBy`、`positionMaxBy`、`positionMinByKey`、`positionMaxByKey`、`positionMinmaxBy`
- **排序增强**：`sortedByCachedKey`、`kSmallest`、`kSmallestBy`、`kLargest`
- **聚合增强**：`minSet`、`maxSet`、`treeFold1`、`sum1`、`product1`
- **窗口和元组**：`circularTupleWindows2/3`、`tuples2/3`、`nextTuple2/3`
- **实用工具**：`interleaveShortest`、`intersperseWith`、`zipEq`、`contains`、`allEqual`、`allUnique`、`findOrFirst`、`findOrLast`、`dropping`、`droppingBack`
- **分组增强**：`groupMapFirst`、`groupMapLast`、`countsByKey`、`partitionResult`

## 使用方式

```cangjie
// 基础类型和收集操作
import itertools.*

// 惰性适配器
import itertools.adapters.*

// 终止操作
import itertools.terminals.*

// 并行迭代器 (v2.0 新增)
import itertools.parallel.*

// 类型安全迭代器 (v2.0 新增)
import itertools.typed.*

// 标准库集成 (v2.0 新增)
import itertools.stdlib.*
```

## 功能列表

### 惰性适配器 (itertools.adapters)

| 模块 | 函数 | 说明 |
|------|------|------|
| generators | `iterate(init, f)` | 从初始值和函数生成无限序列 |
| generators | `repeatN(val, n)` | 重复值 n 次 |
| generators | `unfold(init, f)` | 从状态函数展开序列 |
| indexing | `enumerate(xs)` | 为每个元素添加索引 |
| indexing | `positions(xs, pred)` | 返回满足谓词的所有位置 |
| indexing | `withPosition(xs)` | 标记元素位置 (Only/First/Middle/Last) |
| peeking | `multipeek(xs)` | 多步预览迭代器 |
| peeking | `peekNth(xs, n)` | 预览第 n 个元素 |
| peeking | `putBack(xs)` | 单元素回退迭代器 |
| peeking | `putBackN(xs)` | 多元素回退迭代器 (LIFO) |
| grouping | `chunks(xs, size)` | 按固定大小分块 |
| grouping | `windows(xs, size)` | 滑动窗口 |
| grouping | `tuples2(xs)` | 连续元素分组为不重叠的二元组 |
| grouping | `tuples3(xs)` | 连续元素分组为不重叠的三元组 |
| grouping | `nextTuple2(xs)` | 消费并返回下一个二元组 |
| grouping | `nextTuple3(xs)` | 消费并返回下一个三元组 |
| combining | `multizip(xss)` | 多序列 zip |
| combining | `tupleWindows2(xs)` | 二元组滑动窗口 |
| combining | `tupleWindows3(xs)` | 三元组滑动窗口 |
| combining | `circularTupleWindows2(xs)` | 环形二元组滑动窗口 |
| combining | `circularTupleWindows3(xs)` | 环形三元组滑动窗口 |
| combining | `interleaveShortest(xs, ys)` | 交替合并（较短序列结束时停止）|
| combining | `intersperseWith(xs, sepGen)` | 使用生成函数插入分隔符 |
| combining | `zipEq(xs, ys)` | 等长序列 zip（长度不等返回 Err）|
| padding | `padUsing(xs, minLen, f)` | 序列填充到最小长度 |
| combinatorics | `combinations(xs, k)` | k-组合 |
| combinatorics | `permutations(xs, k)` | k-排列 |
| combinatorics | `powerset(xs)` | 幂集 |
| dedup | `distinct(xs)` | 全局去重 |
| dedup | `dedupWithCount(xs)` | 连续去重并计数 |
| dedup | `dedupByWithCount(xs, eq)` | 自定义相等函数的连续去重并计数 |
| dedup | `duplicates(xs)` | 返回重复元素 |
| dedup | `duplicatesBy(xs, key)` | 按键返回重复元素 |
| conditional | `whileSome(xs)` | 直到遇到 None |
| conditional | `mapOk(xs, f)` | 映射 Result 流中的 Ok 值 |
| conditional | `mapErr(xs, f)` | 映射 Result 流中的 Err 值 |
| conditional | `filterOkBy(xs, pred)` | 按谓词过滤 Ok 值，保留 Err |
| conditional | `filterMapOk(xs, f)` | 对 Ok 值应用返回 Option 的函数并展平 |
| conditional | `takeWhileInclusive(xs, pred)` | 包含边界的条件终止 |
| conditional | `flattenOk(xs)` | 展平 Result 流中 Ok 值的内部可迭代对象 |
| conditional | `peekingTakeWhile(peekable, pred)` | 使用 peek 的条件获取，不消费边界元素 |
| conditional | `update(xs, f)` | 对每个元素应用更新函数 |
| conditional | `inspectWithIndex(xs, f)` | 带索引的检查，调用 f(index, element) |
| conditional | `tap(xs, f)` | 每次迭代前执行动作 |
| stepping | `stepBy(xs, step)` | 步进迭代器，每隔 step 个元素产出一个 |
| lazy_grouping | `lazyGroupBy(xs, keyFn)` | 惰性分组迭代器，产出 (key, group_iterator) 对 |
| forking | `teeN(xs, n)` | 将迭代器分叉为 N 个独立副本 |
| statistics | `runningSum(xs)` | 累计和迭代器 |
| statistics | `runningAverage(xs)` | 累计平均值迭代器 |
| statistics | `differences(xs)` | 相邻差分迭代器 |
| set_ops | `unionBy(xs, ys, less)` | 有序序列并集 |
| set_ops | `intersectionBy(xs, ys, less)` | 有序序列交集 |
| set_ops | `differenceBy(xs, ys, less)` | 有序序列差集 |
| set_ops | `symmetricDifferenceBy(xs, ys, less)` | 有序序列对称差集 |
| windows_ext | `slidingWindow(xs, size, step)` | 带步长的滑动窗口 |
| windows_ext | `mapWindows(xs, size, f)` | 映射窗口 |
| batching | `batchingPeekable(xs, batchFn)` | 使用 PeekableIterator 的自定义批处理 |
| functional | `scan1(xs, f)` | 无初始值的扫描适配器 |
| functional | `unfoldN(init, n, f)` | 有限展开生成器 |
| functional | `converge(init, f, eq, maxIterations)` | 收敛迭代生成器 |
| debug | `profile(xs, name)` | 性能分析适配器 |
| debug | `trace(xs, name)` | 跟踪适配器 |
| debug | `traceWith(xs, name, config)` | 带配置的跟踪适配器 |
| statistics_ext | `movingAverage(xs, window)` | 简单移动平均 |
| statistics_ext | `movingAverageInt(xs, window)` | Int64 简单移动平均 |
| statistics_ext | `exponentialMovingAverage(xs, alpha)` | 指数移动平均 |
| statistics_ext | `lag(xs, n)` | 滞后适配器 |
| statistics_ext | `lead(xs, n)` | 超前适配器 |
| fusion | `filterMap(xs, f)` | map+filter 融合 |
| fusion | `mapFilter(xs, mapper, pred)` | filter+map 融合 |
| fusion | `composeMap(xs, f, g)` | map+map 融合 |
| fusion | `andFilter(xs, p1, p2)` | filter+filter 融合 |
| fusion | `slice(xs, start, end)` | skip+take 融合 |
| lazy_debug | `countingIterator(xs)` | 计数迭代器 |
| lazy_debug | `assertLazy(xs, maxCalls)` | 断言惰性迭代器 |
| windows_partial | `windowsWithPartial(xs, size)` | 包含部分窗口的滑动窗口 |
| grouping_ext | `groupByConsecutiveCount(xs)` | 连续计数分组（RLE）|

### 终止操作 (itertools.terminals)

| 模块 | 函数 | 说明 |
|------|------|------|
| search | `exactlyOne(xs)` | 断言恰好一个元素 |
| search | `atMostOne(xs)` | 断言最多一个元素 |
| search | `contains(xs, elem)` | 检查元素是否存在 |
| search | `allEqual(xs)` | 检查所有元素是否相等 |
| search | `allUnique(xs)` | 检查所有元素是否唯一 |
| search | `findOrFirst(xs, pred)` | 查找匹配元素或返回第一个 |
| search | `findOrLast(xs, pred)` | 查找匹配元素或返回最后一个 |
| search | `dropping(xs, n)` | 跳过前 n 个元素 |
| search | `droppingBack(xs, n)` | 跳过后 n 个元素 |
| search | `getRange(xs, start, end)` | 获取指定范围的元素 |
| search | `getNth(xs, n)` | 获取第 n 个元素 |
| aggregate | `counts(xs)` | 元素频率统计 |
| aggregate | `minmax(xs, less)` | 一次遍历同时获取最小和最大值 |
| aggregate | `minmaxByKey(xs, key, less)` | 按键同时查找最小和最大元素 |
| aggregate | `minSet(xs, less)` | 返回所有等于最小值的元素 |
| aggregate | `maxSet(xs, less)` | 返回所有等于最大值的元素 |
| aggregate | `treeFold1(xs, f)` | 树形折叠（平衡二叉树方式）|
| aggregate | `sum1(xs)` | 求和（空序列返回 None）|
| aggregate | `product1(xs)` | 求积（空序列返回 None）|
| aggregate | `tail(xs, n)` | 返回迭代器的最后 n 个元素 |
| position | `positionMinBy(xs, less)` | 使用自定义比较器查找最小值位置 |
| position | `positionMaxBy(xs, less)` | 使用自定义比较器查找最大值位置 |
| position | `positionMinByKey(xs, key)` | 按键值查找最小元素位置 |
| position | `positionMaxByKey(xs, key)` | 按键值查找最大元素位置 |
| position | `positionMinmaxBy(xs, less)` | 同时查找最小和最大值位置 |
| position | `positionMinmaxByKey(xs, key)` | 按键同时查找最小和最大元素位置 |
| sort_merge | `sortedUnstableBy(xs, less)` | 不稳定排序（快速排序）|
| sort_merge | `sortedUnstableByKey(xs, key)` | 按键不稳定排序 |
| sort_merge | `sortedByCachedKey(xs, key, less)` | 缓存键值的排序 |
| sort_merge | `kSmallest(xs, k, less)` | 返回 k 个最小元素（堆优化 O(n log k)）|
| sort_merge | `kSmallestBy(xs, k, less)` | 使用自定义比较器返回 k 个最小元素 |
| sort_merge | `kSmallestByKey(xs, k, key)` | 按键函数返回 k 个最小元素 |
| sort_merge | `kLargest(xs, k, less)` | 返回 k 个最大元素（堆优化 O(n log k)）|
| sort_merge | `kLargestByKey(xs, k, key)` | 按键函数返回 k 个最大元素 |
| sort_merge | `kSmallestRelaxed(xs, k, less)` | Relaxed 版本 kSmallest（O(n + k log k)）|
| sort_merge | `kLargestRelaxed(xs, k, less)` | Relaxed 版本 kLargest |
| sort_merge | `kSmallestRelaxedByKey(xs, k, key)` | 按键的 Relaxed 版本 kSmallest |
| sort_merge | `kLargestRelaxedByKey(xs, k, key)` | 按键的 Relaxed 版本 kLargest |
| grouping | `groupMapFirst(xs, key, val)` | 按键分组，只保留第一个值 |
| grouping | `groupMapLast(xs, key, val)` | 按键分组，只保留最后一个值 |
| grouping | `countsByKey(xs, key)` | 按键计数 |
| grouping | `partitionResult(xs)` | 分离 Result 的 Ok 和 Err 值 |
| grouping | `multiunzip2(xs)` | 将 2-元组迭代器拆分为两个 ArrayList |
| grouping | `multiunzip3(xs)` | 将 3-元组迭代器拆分为三个 ArrayList |
| grouping | `formatWith(xs, sep, fmt)` | 使用分隔符和格式化函数生成字符串 |
| grouping_map | `intoGroupingMap(xs, keyFn, valueFn)` | 灵活的分组 API，支持多种聚合 |
| grouping_map | `intoGroupingMapBy(xs, keyFn)` | 分组 API，值为元素本身 |
| comparison | `diffWith(xs, ys, eq)` | 比较两个序列的差异 |
| comparison | `consTuples2(xs)` | 展平左嵌套元组 |
| comparison | `consTuples2R(xs)` | 展平右嵌套元组 |
| result_ops | `processResults(xs, f)` | 处理 Result 迭代器 |
| result_ops | `foldOk(xs, init, f)` | 折叠 Result 流的 Ok 值 |
| result_ops | `reduceOk(xs, f)` | 无初始值的 Result 流折叠 |
| result_ops | `tryCollect(xs)` | 收集 Result 流为 Result<ArrayList<T>, E> |
| result_ops | `foldOptions(xs, init, f)` | 折叠 Option 流的 Some 值 |
| result_ops | `tryReduce(xs, f)` | 对 Result 流归约，遇 Err 提前终止 |
| short_circuit | `anyWithCount(xs, pred)` | 带计数的 any 操作 |
| short_circuit | `allWithCount(xs, pred)` | 带计数的 all 操作 |
| short_circuit | `findWithCount(xs, pred)` | 带计数的 find 操作 |
| short_circuit | `containsWithCount(xs, elem)` | 带计数的 contains 操作 |
| try_ops | `tryForEach(xs, f)` | 对每个元素应用函数，遇 Err 停止 |
| try_ops | `tryFold(xs, init, f)` | 可中断的折叠操作 |
| try_ops | `tryFind(xs, pred)` | 查找满足条件的元素，谓词可能失败 |
| try_ops | `tryAll(xs, pred)` | 检查所有元素是否满足条件 |
| try_ops | `tryAny(xs, pred)` | 检查是否存在满足条件的元素 |
| statistics | `average(xs)` | 计算算术平均值 |
| statistics | `variance(xs)` | 计算总体方差（Welford 算法）|
| statistics | `stddev(xs)` | 计算总体标准差 |
| statistics_ext | `median(xs)` | 计算 Int64 中位数 |
| statistics_ext | `medianFloat(xs)` | 计算 Float64 中位数 |
| statistics_ext | `percentile(xs, p)` | 计算 Int64 百分位数 |
| statistics_ext | `percentileFloat(xs, p)` | 计算 Float64 百分位数 |
| statistics_ext | `mode(xs)` | 计算众数 |
| statistics_ext | `covariance(xs, ys)` | 计算样本协方差 |
| statistics_ext | `correlation(xs, ys)` | 计算 Pearson 相关系数 |
| statistics_ext | `histogram(xs, bins)` | 创建等宽直方图 |
| statistics_ext | `histogramBy(xs, binFn)` | 自定义 bin 函数直方图 |
| search_ext | `exactlyOneOrErr(xs)` | 断言恰好一个元素（返回 Result）|
| search_ext | `atMostOneOrErr(xs)` | 断言最多一个元素（返回 Result）|
| functional_ext | `fixpoint(init, f, eq, maxIterations)` | 查找不动点 |
| functional_ext | `fixpointFloat(init, f, tolerance, maxIterations)` | 浮点数不动点 |

### 并行迭代器 (itertools.parallel) - v2.0 新增

| 模块 | 函数 | 说明 |
|------|------|------|
| parallel_iter | `ParallelConfig` | 并行执行配置 |
| parallel_iter | `splitIntoChunks(xs, chunkSize)` | 分割成数据块 |
| par_map | `parMap(xs, f, config)` | 并行映射 |
| par_filter | `parFilter(xs, pred, config)` | 并行过滤 |
| par_reduce | `parReduce(xs, f, config)` | 并行归约 |

### 类型安全迭代器 (itertools.typed) - v2.0 新增

| 模块 | 函数/类型 | 说明 |
|------|------|------|
| non_empty | `NonEmptyIterator<T>` | 非空迭代器类型 |
| non_empty | `nonEmpty(xs)` | 创建非空迭代器 |
| sorted | `SortedIterator<T>` | 有序迭代器类型 |
| sorted | `assertSorted(xs, less)` | 断言迭代器已排序 |
| unique | `UniqueIterator<T>` | 唯一元素迭代器类型 |
| unique | `assertUnique(xs)` | 断言迭代器元素唯一 |

### 标准库集成 (itertools.stdlib) - v2.0 新增

| 模块 | 函数/类型 | 说明 |
|------|------|------|
| collectors | `toHashSet(xs)` | 收集到 HashSet |
| collectors | `toHashMap(xs)` | 收集键值对到 HashMap |
| collectors | `toHashMapBy(xs, keyFn, valueFn)` | 使用函数收集到 HashMap |
| collectors | `toLinkedList(xs)` | 收集到 LinkedList |
| collectors | `collectToString(xs)` | 收集字符到字符串 |
| collectors | `fromArrayList(list)` | ArrayList 转迭代器 |
| collectors | `fromHashSet(set)` | HashSet 转迭代器 |
| collectors | `fromHashMap(map)` | HashMap 转迭代器 |
| collection_ext | `ArrayList.iter()` | ArrayList 迭代器 |
| collection_ext | `ArrayList.iterChunks(size)` | 分块迭代器 |
| collection_ext | `ArrayList.iterWindows(size)` | 滑动窗口迭代器 |
| collection_ext | `ArrayList.iterEnumerate()` | 带索引迭代器 |
| collection_ext | `ArrayList.iterReverse()` | 反向迭代器 |
| collection_ext | `HashMap.iterKeys()` | 键迭代器 |
| collection_ext | `HashMap.iterValues()` | 值迭代器 |
| collection_ext | `HashMap.iterEntries()` | 键值对迭代器 |
| collection_ext | `HashSet.iter()` | HashSet 迭代器 |
| collection_ext | `HashSet.iterDifference(other)` | 差集迭代器 |
| comparable_ext | `sorted(xs)` | Comparable 自然排序 |
| comparable_ext | `minValue(xs)` | 获取最小值 |
| comparable_ext | `maxValue(xs)` | 获取最大值 |
| comparable_ext | `minmaxValue(xs)` | 获取最小和最大值 |
| option_iter | `optionIter(opt)` | Option 转迭代器 |
| option_iter | `OptionIterator<T>` | Option 迭代器类型 |
| result_iter | `resultOkIter(result)` | Result Ok 值迭代器 |
| result_iter | `resultErrIter(result)` | Result Err 值迭代器 |
| string_iter | `stringChars(s)` | 字符迭代器 |
| string_iter | `stringLines(s)` | 行迭代器 |
| string_iter | `stringWords(s)` | 单词迭代器 |
| string_iter | `stringSplit(s, delimiter)` | 分割迭代器 |
| slice_iter | `sliceIter(array, start, end)` | 切片迭代器 |
| lazy_string | `LazyJoiner<T>` | 惰性字符串连接器 |
| lazy_string | `lazyJoin(xs, sep, fmt)` | 惰性连接 |
| lazy_string | `lazyFormat(xs, fmt)` | 惰性格式化 |

### 基础类型 (itertools)

| 类型 | 说明 |
|------|------|
| `Position` | 元素位置标记：Only, First, Middle, Last |
| `Diff<T>` | 序列差异：Equal, Longer, Shorter, FirstMismatch |
| `Result<T, E>` | 成功或失败的结果 |
| `Either<L, R>` | 两种可能类型之一 |

## 示例

```cangjie
import itertools.*
import itertools.adapters.*
import itertools.terminals.*

main() {
    // 生成斐波那契数列
    let fib = iterate((0, 1), {(a, b) => (b, a + b)})
        .map({(a, _) => a})
        .take(10)
        |> toArrayList
    // fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    // 带索引的过滤
    let indexed = enumerate([10, 20, 30, 40, 50].iterator())
        |> toArrayList
    // indexed = [(0, 10), (1, 20), (2, 30), (3, 40), (4, 50)]
    
    // 元素频率统计
    let freq = counts([1, 2, 1, 3, 1, 2].iterator())
    // freq = {1: 3, 2: 2, 3: 1}
    
    // 序列差异比较
    let diff = diffWith([1, 2, 3].iterator(), [1, 2, 4].iterator(), {a, b => a == b})
    // diff = FirstMismatch(2, ...)
    
    // === v1.2.0 新增功能示例 ===
    
    // 连续去重并计数
    let counted = dedupWithCount([1, 1, 2, 2, 2, 3].iterator()) |> toArrayList
    // counted = [(2, 1), (3, 2), (1, 3)]
    
    // 查找重复元素
    let dups = duplicates([1, 2, 1, 3, 2, 4].iterator()) |> toArrayList
    // dups = [1, 2]
    
    // 使用自定义比较器查找最小值位置
    let minPos = positionMinBy([3, 1, 4, 1, 5].iterator(), {a, b => a < b})
    // minPos = Some(1)
    
    // 返回 k 个最小元素
    let smallest3 = kSmallest([5, 2, 8, 1, 9, 3].iterator(), 3, {a, b => a < b})
    // smallest3 = [1, 2, 3]
    
    // 返回所有等于最小值的元素
    let mins = minSet([3, 1, 4, 1, 5].iterator(), {a, b => a < b})
    // mins = [1, 1]
    
    // 环形二元组滑动窗口
    let circular = circularTupleWindows2([1, 2, 3].iterator()) |> toArrayList
    // circular = [(1, 2), (2, 3), (3, 1)]
    
    // 检查所有元素是否相等
    let allSame = allEqual([1, 1, 1, 1].iterator())
    // allSame = true
    
    // 按键计数
    let keyCounts = countsByKey([1, 2, 3, 4, 5, 6].iterator(), {x => x % 2})
    // keyCounts = {0: 3, 1: 3}
    
    // === v1.3.0 新增 Result/Option 操作示例 ===
    
    // 映射 Result 流中的 Ok 值
    let results = [Ok(1), Err("e1"), Ok(2)].iterator()
    let mapped = mapOk(results, {x => x * 2}) |> toArrayList
    // mapped = [Ok(2), Err("e1"), Ok(4)]
    
    // 按谓词过滤 Ok 值，保留 Err
    let filtered = filterOkBy([Ok(1), Err("e"), Ok(3)].iterator(), {x => x > 1}) |> toArrayList
    // filtered = [Err("e"), Ok(3)]
    
    // 折叠 Result 流，遇到 Err 时停止
    let sum = foldOk([Ok(1), Ok(2), Ok(3)].iterator(), 0, {acc, x => acc + x})
    // sum = Ok(6)
    
    // 收集 Result 流为单个 Result
    let collected = tryCollect([Ok(1), Ok(2), Ok(3)].iterator())
    // collected = Ok([1, 2, 3])
    
    // 包含边界的条件终止
    let inclusive = takeWhileInclusive([1, 2, 3, 4, 5].iterator(), {x => x < 4}) |> toArrayList
    // inclusive = [1, 2, 3, 4]  // 包含第一个不满足条件的元素
    
    // 一次遍历同时获取最小和最大值
    let (min, max) = minmax([3, 1, 4, 1, 5].iterator(), {a, b => a < b})
    // min = Some(1), max = Some(5)
    
    // 获取指定范围的元素
    let range = getRange([1, 2, 3, 4, 5].iterator(), 1, 4)
    // range = [2, 3, 4]
    
    // === v1.4.0 新增功能示例 ===
    
    // 堆优化的 kSmallest/kLargest (O(n log k) 复杂度)
    let smallest3 = kSmallest([5, 2, 8, 1, 9, 3].iterator(), 3, {a, b => a < b})
    // smallest3 = [1, 2, 3]
    
    // 按键函数返回 k 个最小元素
    let smallestByKey = kSmallestByKey(["apple", "pie", "a", "banana"].iterator(), 2, {s => s.size})
    // smallestByKey = ["a", "pie"]
    
    // tail - 获取最后 n 个元素
    let last3 = tail([1, 2, 3, 4, 5].iterator(), 3)
    // last3 = [3, 4, 5]
    
    // tryReduce - 对 Result 流归约
    let reduceResult = tryReduce([Ok(1), Ok(2), Ok(3)].iterator(), {a, b => Ok(a + b)})
    // reduceResult = Ok(Some(6))
    
    // flattenOk - 展平 Result 流中 Ok 值的内部可迭代对象
    let flattened = flattenOk([Ok([1, 2]), Err("e1"), Ok([3, 4])].iterator()) |> toArrayList
    // flattened = [Ok(1), Ok(2), Err("e1"), Ok(3), Ok(4)]
    
    // update - 对每个元素应用更新函数
    let updated = update([1, 2, 3].iterator(), {x => x + 10}) |> toArrayList
    // updated = [11, 12, 13]
    
    // intoGroupingMap - 灵活的分组 API
    let gm = intoGroupingMap([1, 2, 3, 4, 5, 6].iterator(), {x => x % 2}, {x => x})
    let sums = gm.fold({=> 0}, {acc, x => acc + x})
    // sums[0] = 12, sums[1] = 9
    
    // multiunzip - 拆分元组迭代器
    let (nums, strs) = multiunzip2([(1, "a"), (2, "b"), (3, "c")].iterator())
    // nums = [1, 2, 3], strs = ["a", "b", "c"]
    
    // formatWith - 自定义格式化
    let formatted = formatWith([1, 2, 3].iterator(), ", ", {x => x.toString()})
    // formatted = "1, 2, 3"
    
    // === v1.5.0 新增功能示例 ===
    
    // stepBy - 步进迭代器
    let stepped = stepBy([1, 2, 3, 4, 5, 6, 7, 8, 9].iterator(), 3) |> toArrayList
    // stepped = [1, 4, 7]  // 每隔 3 个元素取一个
    
    // lazyGroupBy - 惰性分组
    let groups = lazyGroupBy([1, 1, 2, 2, 2, 3].iterator(), {x => x})
    // 产出 (1, [1, 1]), (2, [2, 2, 2]), (3, [3])
    
    // teeN - 多路分叉
    let forks = teeN([1, 2, 3].iterator(), 3)
    // forks[0], forks[1], forks[2] 都可以独立遍历 [1, 2, 3]
    
    // tryForEach - 可中断的遍历
    let result = tryForEach([1, 2, 3].iterator(), {x => 
        if (x > 2) { Err("too large") } else { Ok(()) }
    })
    // result = Err("too large")
    
    // average - 算术平均值
    let avg = average([1, 2, 3, 4, 5].iterator())
    // avg = Some(3.0)
    
    // runningSum - 累计和
    let sums = runningSum([1, 2, 3, 4, 5].iterator()) |> toArrayList
    // sums = [1, 3, 6, 10, 15]
    
    // differences - 差分
    let diffs = differences([1, 3, 6, 10, 15].iterator()) |> toArrayList
    // diffs = [2, 3, 4, 5]
    
    // unionBy - 有序序列并集
    let union = unionBy([1, 3, 5].iterator(), [2, 3, 4].iterator(), {a, b => a < b}) |> toArrayList
    // union = [1, 2, 3, 4, 5]
    
    // slidingWindow - 带步长的滑动窗口
    let windows = slidingWindow([1, 2, 3, 4, 5, 6].iterator(), 2, 2) |> toArrayList
    // windows = [[1, 2], [3, 4], [5, 6]]  // 不重叠窗口
    
    // mapWindows - 映射窗口
    let windowSums = mapWindows([1, 2, 3, 4, 5].iterator(), 3, {w =>
        var sum: Int64 = 0
        for (x in w) { sum += x }
        sum
    }) |> toArrayList
    // windowSums = [6, 9, 12]
    
    // inspectWithIndex - 带索引的检查
    let result = inspectWithIndex([10, 20, 30].iterator(), {idx, x => 
        println("Index ${idx}: ${x}")
    }) |> toArrayList
    // 输出: Index 0: 10, Index 1: 20, Index 2: 30
    
    // === v2.0 新增功能示例 ===
    
    // 高级统计 - 中位数
    let med = median([1, 3, 5, 7, 9].iterator())
    // med = Some(5.0)
    
    // 高级统计 - 百分位数
    let p75 = percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10].iterator(), 75.0)
    // p75 = Some(7.75)
    
    // 高级统计 - 众数
    let m = mode([1, 2, 2, 3, 3, 3].iterator())
    // m = [3]  // 3 出现 3 次
    
    // 高级统计 - 相关系数
    let corr = correlation([1.0, 2.0, 3.0, 4.0, 5.0].iterator(), 
                           [2.0, 4.0, 6.0, 8.0, 10.0].iterator())
    // corr = Some(1.0)  // 完全正相关
    
    // 时间序列 - 移动平均
    let ma = movingAverage([1.0, 2.0, 3.0, 4.0, 5.0].iterator(), 3) |> toArrayList
    // ma = [2.0, 3.0, 4.0]
    
    // 时间序列 - 指数移动平均
    let ema = exponentialMovingAverage([10.0, 20.0, 30.0, 40.0].iterator(), 0.5)
    // ema = Ok([10.0, 15.0, 22.5, 31.25])
    
    // 时间序列 - lag
    let lagged = lag([1, 2, 3, 4, 5].iterator(), 2) |> toArrayList
    // lagged = [(1, None), (2, None), (3, Some(1)), (4, Some(2)), (5, Some(3))]
    
    // 函数式编程 - scan1
    let sums = scan1([1, 2, 3, 4, 5].iterator(), {a, b => a + b}) |> toArrayList
    // sums = [1, 3, 6, 10, 15]
    
    // 函数式编程 - unfoldN
    let fibs = unfoldN((0, 1), 5, {state =>
        let (a, b) = state
        Some((a, (b, a + b)))
    }) |> toArrayList
    // fibs = [0, 1, 1, 2, 3]
    
    // 函数式编程 - fixpoint
    let sqrt2 = fixpointFloat(1.0, {x => (x + 2.0 / x) / 2.0}, 1e-10, 100)
    // sqrt2 ≈ Some(1.4142135623730951)
    
    // 并行迭代器 - parMap
    let doubled = parMap([1, 2, 3, 4, 5].iterator(), {x => x * 2}, ParallelConfig.default())
    // doubled = [2, 4, 6, 8, 10]
    
    // 并行迭代器 - parReduce
    let sum = parReduce([1, 2, 3, 4, 5].iterator(), {a, b => a + b}, ParallelConfig.default())
    // sum = Some(15)
    
    // 类型安全迭代器 - NonEmptyIterator
    let ne = nonEmpty([1, 2, 3].iterator())
    match (ne) {
        case Some(iter) =>
            let first = iter.firstValue()  // 1，不是 Option
        case None => ()
    }
    
    // 类型安全迭代器 - SortedIterator
    let sorted = assertSorted([1, 2, 3, 4, 5].iterator(), {a, b => a < b})
    match (sorted) {
        case Ok(si) =>
            let pos = si.binarySearch(3)  // Some(2)，O(log n)
        case Err(_) => ()
    }
    
    // 调试工具 - profile
    let profiled = profile([1, 2, 3, 4, 5].iterator(), "my_iterator")
    while (let Some(x) <- profiled.next()) { /* 处理 */ }
    let data = profiled.getProfileData()
    println(data.report())
    
    // 窗口增强 - windowsWithPartial
    let withPartial = windowsWithPartial([1, 2, 3, 4, 5].iterator(), 3) |> toArrayList
    // withPartial = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5], [5]]
    
    // 分组增强 - groupByConsecutiveCount
    let rle = groupByConsecutiveCount([1, 1, 2, 2, 2, 3].iterator()) |> toArrayList
    // rle = [(1, 2), (2, 3), (3, 1)]
    
    // === v2.0 标准库集成示例 ===
    
    // 收集到 HashSet（自动去重）
    let set = toHashSet([1, 2, 2, 3, 3, 3].iterator())
    // set = {1, 2, 3}
    
    // 收集键值对到 HashMap
    let map = toHashMap([(1, "a"), (2, "b"), (3, "c")].iterator())
    // map = {1: "a", 2: "b", 3: "c"}
    
    // 使用键/值函数收集到 HashMap
    let wordLengths = toHashMapBy(["apple", "pie", "banana"].iterator(), 
        {s => s}, {s => s.size})
    // wordLengths = {"apple": 5, "pie": 3, "banana": 6}
    
    // ArrayList 扩展方法
    let arr = ArrayList<Int64>([1, 2, 3, 4, 5])
    let chunks = arr.iterChunks(2) |> toArrayList
    // chunks = [[1, 2], [3, 4], [5]]
    
    let reversed = arr.iterReverse() |> toArrayList
    // reversed = [5, 4, 3, 2, 1]
    
    // HashMap 扩展方法
    let hm = HashMap<String, Int64>()
    hm["a"] = 1
    hm["b"] = 2
    let keys = hm.iterKeys() |> toArrayList
    // keys = ["a", "b"] (顺序可能不同)
    
    // HashSet 差集
    let set1 = HashSet<Int64>([1, 2, 3, 4, 5])
    let set2 = HashSet<Int64>([3, 4, 5, 6, 7])
    let diff = set1.iterDifference(set2) |> toArrayList
    // diff = [1, 2]
    
    // Comparable 自然排序
    let sortedNums = sorted([3, 1, 4, 1, 5, 9, 2, 6].iterator())
    // sortedNums = [1, 1, 2, 3, 4, 5, 6, 9]
    
    // 获取最小/最大值
    let minVal = minValue([3, 1, 4, 1, 5].iterator())
    // minVal = Some(1)
    
    // Option 迭代器
    let someIter = optionIter(Some(42)) |> toArrayList
    // someIter = [42]
    let noneIter = optionIter(None) |> toArrayList
    // noneIter = []
    
    // 字符串行迭代器
    let lines = stringLines("hello\nworld\nfoo") |> toArrayList
    // lines = ["hello", "world", "foo"]
    
    // 字符串单词迭代器
    let words = stringWords("  hello   world  ") |> toArrayList
    // words = ["hello", "world"]
    
    // 字符串分割迭代器
    let parts = stringSplit("a,b,c,d", ",") |> toArrayList
    // parts = ["a", "b", "c", "d"]
    
    // 切片迭代器（支持负索引）
    let slice = sliceIter(ArrayList<Int64>([1, 2, 3, 4, 5]), 1, -1) |> toArrayList
    // slice = [2, 3, 4]
    
    // 惰性字符串构建
    let joined = lazyJoin([1, 2, 3].iterator(), ", ", {x => x.toString()}).build()
    // joined = "1, 2, 3"
}
```

## 项目架构

```
src/
├── lib.cj                      # 库入口和文档
├── types.cj                    # 基础类型定义
├── collect.cj                  # 收集操作
├── internal/
│   └── heap.cj                 # 内部堆实现（BinaryHeap，不对外导出）
├── adapters/
│   ├── generators.cj           # 生成器：iterate, repeatN, unfold
│   ├── indexing.cj             # 索引：enumerate, positions, withPosition
│   ├── peeking.cj              # 预览：multipeek, putBack, putBackN
│   ├── grouping.cj             # 分组：chunks, windows, chunkBy, tuples2/3
│   ├── combining.cj            # 组合：multizip, tupleWindows, circularTupleWindows, zipEq
│   ├── padding.cj              # 填充：padUsing
│   ├── combinatorics.cj        # 组合学：combinations, permutations
│   ├── dedup.cj                # 去重：distinct, dedupConsecutive, dedupWithCount, duplicates
│   ├── conditional.cj          # 条件：whileSome, whileOk, mapOk, mapErr, filterOkBy, filterMapOk, takeWhileInclusive, flattenOk, peekingTakeWhile, update, inspectWithIndex, tap
│   ├── stepping.cj             # 步进：stepBy
│   ├── lazy_grouping.cj        # 惰性分组：lazyGroupBy
│   ├── forking.cj              # 分叉：teeN
│   ├── statistics.cj           # 数值统计适配器：runningSum, runningAverage, differences
│   ├── set_ops.cj              # 有序集合操作：unionBy, intersectionBy, differenceBy, symmetricDifferenceBy
│   ├── windows_ext.cj          # 窗口增强：slidingWindow, mapWindows
│   ├── batching.cj             # 批处理增强：batchingPeekable (v2.0)
│   ├── functional.cj           # 函数式编程：scan1, unfoldN, converge (v2.0)
│   ├── debug.cj                # 调试工具：profile, trace (v2.0)
│   ├── statistics_ext.cj       # 时间序列：movingAverage, exponentialMovingAverage, lag, lead (v2.0)
│   ├── windows_partial.cj      # 窗口增强：windowsWithPartial (v2.0)
│   └── grouping_ext.cj         # 分组增强：groupByConsecutiveCount (v2.0)
├── terminals/
│   ├── fold.cj                 # 折叠：fold, foldWhile, reduce
│   ├── search.cj               # 查找：find, exactlyOne, contains, allEqual, allUnique, getRange, getNth
│   ├── aggregate.cj            # 聚合：count, counts, minBy, maxBy, minmax, minmaxByKey, minSet, maxSet, treeFold1, tail
│   ├── position.cj             # 位置：positionMinBy, positionMaxBy, positionMinmaxBy, positionMinmaxByKey
│   ├── grouping.cj             # 分组：groupBy, partition, groupMapFirst/Last, countsByKey, multiunzip2/3, formatWith
│   ├── grouping_map.cj         # 分组映射：intoGroupingMap, GroupingMap (fold, reduce, minBy, maxBy, aggregate)
│   ├── sort_merge.cj           # 排序：sortedBy（归并排序）, sortedByCachedKey, kSmallest, kLargest, kSmallestRelaxed, kLargestRelaxed, merge, kmerge
│   ├── comparison.cj           # 比较：diffWith, consTuples
│   ├── result_ops.cj           # Result：processResults, foldOk, reduceOk, tryCollect, foldOptions, tryReduce
│   ├── try_ops.cj              # Try 系列：tryForEach, tryFold, tryFind, tryAll, tryAny
│   ├── statistics.cj           # 数值统计：average, variance, stddev
│   ├── statistics_ext.cj       # 高级统计：median, percentile, mode, covariance, correlation, histogram (v2.0)
│   ├── search_ext.cj           # 扩展查找：exactlyOneOrErr, atMostOneOrErr, IteratorError (v2.0)
│   └── functional_ext.cj       # 函数式扩展：fixpoint, fixpointFloat (v2.0)
├── parallel/                   # 并行迭代器 (v2.0)
│   ├── parallel_iter.cj        # 并行配置：ParallelConfig, IndexedChunk
│   ├── par_map.cj              # 并行映射：parMap
│   ├── par_filter.cj           # 并行过滤：parFilter
│   ├── par_reduce.cj           # 并行归约：parReduce
│   └── par_collectors.cj       # 并行收集器：parCollectToArrayList, parCollectToHashSet, parCollectToHashMap (v2.0)
├── stdlib/                     # 标准库集成 (v2.0)
│   ├── collectors.cj           # 收集器：toHashSet, toHashMap, toLinkedList, collectToString
│   ├── collection_ext.cj       # 集合扩展：ArrayList/HashMap/HashSet 扩展方法
│   ├── comparable_ext.cj       # Comparable 集成：sorted, minValue, maxValue
│   ├── option_iter.cj          # Option 迭代器：optionIter, OptionIterator
│   ├── result_iter.cj          # Result 迭代器：resultOkIter, resultErrIter
│   ├── string_iter.cj          # 字符串迭代器：stringChars, stringLines, stringWords, stringSplit
│   ├── slice_iter.cj           # 切片迭代器：sliceIter, SliceIterator
│   └── lazy_string.cj          # 惰性字符串：LazyJoiner, lazyJoin, lazyFormat
└── typed/                      # 类型安全迭代器 (v2.0)
    ├── non_empty.cj            # 非空迭代器：NonEmptyIterator, nonEmpty
    ├── sorted.cj               # 有序迭代器：SortedIterator, assertSorted
    └── unique.cj               # 唯一元素迭代器：UniqueIterator, assertUnique
```

## 编译与测试

```shell
# 编译
cjpm build

# 运行测试
cjpm test
```

## 性能优化

itertools 库实现了多项性能优化，确保高效处理大规模数据：

### 堆操作优化
- **O(1) 空间 pop 操作**：`BinaryHeap.pop()` 使用逻辑大小跟踪，避免每次 pop 创建新数组
- **单次赋值 siftDown**：堆下沉操作使用单次赋值替代多次交换，减少内存写入
- **高效 Top-K**：`kSmallest`/`kLargest` 使用堆优化，时间复杂度 O(n log k)

### 滑动窗口优化
- **RingBuffer 实现**：`slidingWindow` 和 `mapWindows` 使用环形缓冲区
- **O(step) 窗口滑动**：窗口滑动从 O(windowSize) 优化到 O(step)

### 组合学优化
- **缓冲区复用**：`CombinationsIterator` 和 `PermutationsIterator` 复用内部输出缓冲区
- **减少内存分配**：内部计算使用复用缓冲区，仅在输出时创建新数组

### 并行迭代器优化
- **自适应分块**：根据数据量自动调整分块大小
- **顺序处理回退**：小数据集自动回退到顺序处理，避免并行开销
- **可配置阈值**：`ParallelConfig` 支持 `minChunkSize`、`adaptiveChunking`、`sequentialThreshold`

### 数值计算优化
- **Kahan 求和**：`sumFloat` 和 `averageFloat` 使用 Kahan 求和算法，减少浮点累积误差
- **Welford 算法**：`variance` 和 `stddev` 使用 Welford 在线算法，数值稳定

### 排序优化
- **小数组插入排序**：数组大小 ≤16 时使用插入排序，减少递归开销
- **稳定归并排序**：`sortedBy` 使用 O(n log n) 稳定归并排序

## 约束与限制

- 依赖 Cangjie 1.0.4（cjnative runtime）
- 组合学操作在大输入时会占用更多内存
- 无限迭代器（如 `iterate`、`cycle`）需配合 `take` 使用

## 开源协议

[LICENSE](./LICENSE)

## 参与贡献

欢迎提交 Issue / PR，一起完善惰性迭代器生态。
