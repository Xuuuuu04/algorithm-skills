# CF-85D Sum of Medians

## 题面快照

## Description

In one well-known algorithm of finding the k-th order statistics we should divide all elements into groups of five consecutive elements and find the median of each five. A median is called the middle element of a sorted array (it's the third largest element for a group of five). To increase the algorithm's performance speed on a modern video card, you should be able to find a sum of medians in each five of the array.

A sum of medians of a sorted k-element set S = {a1, a2, ..., ak}, where a1 < a2 < a3 < ... < ak, will be understood by as

The  operator stands for taking the remainder, that is  stands for the remainder of dividing x by y.

To organize exercise testing quickly calculating the sum of medians for a changing set was needed.

The first line contains number n (1 ≤ n ≤ 105), the number of operations performed.

Then each of n lines contains the description of one of the three operations:

- add x — add the element x to the set;

- del x — delete the element x from the set;

- sum — find the sum of medians of the set.

For any add x operation it is true that the element x is not included in the set directly before the operation.

For any del x operation it is true that the element x is included in the set directly before the operation.

All the numbers in the input are positive integers, not exceeding 109.

For each operation sum print on the single line the sum of medians of the current set. If the set is empty, print 0.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams (also you may use the %I64d specificator).

## Input

The first line contains number n (1 ≤ n ≤ 105), the number of operations performed.

Then each of n lines contains the description of one of the three operations:

- add x — add the element x to the set;

- del x — delete the element x from the set;

- sum — find the sum of medians of the set.

For any add x operation it is true that the element x is not included in the set directly before the operation.

For any del x operation it is true that the element x is included in the set directly before the operation.

All the numbers in the input are positive integers, not exceeding 109.

## Output

For each operation sum print on the single line the sum of medians of the current set. If the set is empty, print 0.

Please, do not use the %lld specificator to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams (also you may use the %I64d specificator).

## Samples

```
6
add 4
add 5
add 1
add 2
add 3
sum

```

```
3

```

```
14
add 1
add 7
add 2
add 5
sum
add 6
add 8
add 9
add 3
add 4
add 10
sum
del 1
sum

```

```
5
11
13

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-85D |
| Contest | 85 |
| Index | D |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `binary search`、`brute force`、`data structures`、`implementation` |
| 镜像标签 | `binary search`、`brute force`、`data structures`、`implementation`、`*2300` |
| Codeforces 通过次数 | 2409 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/85/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/85/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P85D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

