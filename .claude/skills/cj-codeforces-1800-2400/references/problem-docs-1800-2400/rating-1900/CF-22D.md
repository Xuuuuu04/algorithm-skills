# CF-22D Segments

## 题面快照

## Description

You are given n segments on the Ox-axis. You can drive a nail in any integer point on the Ox-axis line nail so, that all segments containing this point, are considered nailed down. If the nail passes through endpoint of some segment, this segment is considered to be nailed too. What is the smallest number of nails needed to nail all the segments down?

The first line of the input contains single integer number n (1 ≤ n ≤ 1000) — amount of segments. Following n lines contain descriptions of the segments. Each description is a pair of integer numbers — endpoints coordinates. All the coordinates don't exceed 10000 by absolute value. Segments can degenarate to points.

The first line should contain one integer number — the smallest number of nails needed to nail all the segments down. The second line should contain coordinates of driven nails separated by space in any order. If the answer is not unique, output any.

## Input

The first line of the input contains single integer number n (1 ≤ n ≤ 1000) — amount of segments. Following n lines contain descriptions of the segments. Each description is a pair of integer numbers — endpoints coordinates. All the coordinates don't exceed 10000 by absolute value. Segments can degenarate to points.

## Output

The first line should contain one integer number — the smallest number of nails needed to nail all the segments down. The second line should contain coordinates of driven nails separated by space in any order. If the answer is not unique, output any.

## Samples

```
2
0 2
2 5

```

```
1
2

```

```
5
0 3
4 2
4 8
8 10
7 7

```

```
3
7 10 3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-22D |
| Contest | 22 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `greedy`、`sortings` |
| 镜像标签 | `greedy`、`sortings`、`*1900` |
| Codeforces 通过次数 | 3365 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/22/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/22/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P22D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

