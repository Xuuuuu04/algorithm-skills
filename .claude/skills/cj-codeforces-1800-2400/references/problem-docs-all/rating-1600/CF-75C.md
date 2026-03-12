# CF-75C Modified GCD

## 题面快照

## Description

Well, here is another math class task. In mathematics, GCD is the greatest common divisor, and it's an easy task to calculate the GCD between two positive integers.

A common divisor for two positive numbers is a number which both numbers are divisible by.

But your teacher wants to give you a harder task, in this task you have to find the greatest common divisor d between two integers a and b that is in a given range from low to high (inclusive), i.e. low ≤ d ≤ high. It is possible that there is no common divisor in the given range.

You will be given the two integers a and b, then n queries. Each query is a range from low to high and you have to answer each query.

The first line contains two integers a and b, the two integers as described above (1 ≤ a, b ≤ 109). The second line contains one integer n, the number of queries (1 ≤ n ≤ 104). Then n lines follow, each line contains one query consisting of two integers, low and high (1 ≤ low ≤ high ≤ 109).

Print n lines. The i-th of them should contain the result of the i-th query in the input. If there is no common divisor in the given range for any query, you should print -1 as a result for this query.

## Input

The first line contains two integers a and b, the two integers as described above (1 ≤ a, b ≤ 109). The second line contains one integer n, the number of queries (1 ≤ n ≤ 104). Then n lines follow, each line contains one query consisting of two integers, low and high (1 ≤ low ≤ high ≤ 109).

## Output

Print n lines. The i-th of them should contain the result of the i-th query in the input. If there is no common divisor in the given range for any query, you should print -1 as a result for this query.

## Samples

```
9 27
3
1 5
10 11
9 11

```

```
3
-1
9

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-75C |
| Contest | 75 |
| Index | C |
| Rating | 1600 |
| Points | 1500.0 |
| Codeforces 标签 | `binary search`、`number theory` |
| 镜像标签 | `binary search`、`number theory`、`*1600` |
| Codeforces 通过次数 | 15386 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/75/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/75/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P75C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

