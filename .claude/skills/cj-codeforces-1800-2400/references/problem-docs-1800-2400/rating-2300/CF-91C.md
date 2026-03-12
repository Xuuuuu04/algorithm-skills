# CF-91C Ski Base

## 题面快照

## Description

A ski base is planned to be built in Walrusland. Recently, however, the project is still in the constructing phase. A large land lot was chosen for the construction. It contains n ski junctions, numbered from 1 to n. Initially the junctions aren't connected in any way.

In the constructing process m bidirectional ski roads will be built. The roads are built one after another: first the road number 1 will be built, then the road number 2, and so on. The i-th road connects the junctions with numbers ai and bi.

Track is the route with the following properties:

-  The route is closed, that is, it begins and ends in one and the same junction.

-  The route contains at least one road.

-  The route doesn't go on one road more than once, however it can visit any junction any number of times.

Let's consider the ski base as a non-empty set of roads that can be divided into one or more tracks so that exactly one track went along each road of the chosen set. Besides, each track can consist only of roads from the chosen set. Ski base doesn't have to be connected.

Two ski bases are considered different if they consist of different road sets.

After building each new road the Walrusland government wants to know the number of variants of choosing a ski base based on some subset of the already built roads. The government asks you to help them solve the given problem.

The first line contains two integers n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105). They represent the number of junctions and the number of roads correspondingly. Then on m lines follows the description of the roads in the order in which they were built. Each road is described by a pair of integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi) — the numbers of the connected junctions. There could be more than one road between a pair of junctions.

Print m lines: the i-th line should represent the number of ways to build a ski base after the end of construction of the road number i. The numbers should be printed modulo 1000000009 (109 + 9).

## Input

The first line contains two integers n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ 105). They represent the number of junctions and the number of roads correspondingly. Then on m lines follows the description of the roads in the order in which they were built. Each road is described by a pair of integers ai and bi (1 ≤ ai, bi ≤ n, ai ≠ bi) — the numbers of the connected junctions. There could be more than one road between a pair of junctions.

## Output

Print m lines: the i-th line should represent the number of ways to build a ski base after the end of construction of the road number i. The numbers should be printed modulo 1000000009 (109 + 9).

## Samples

```
3 4
1 3
2 3
1 2
1 2

```

```
0
0
1
3

```

## Note

Let us have 3 junctions and 4 roads between the junctions have already been built (as after building all the roads in the sample): 1 and 3, 2 and 3, 2 roads between junctions 1 and 2. The land lot for the construction will look like this:

The land lot for the construction will look in the following way:

We can choose a subset of roads in three ways:

In the first and the second ways you can choose one path, for example, 1 - 2 - 3 - 1. In the first case you can choose one path 1 - 2 - 1.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-91C |
| Contest | 91 |
| Index | C |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `combinatorics`、`dsu`、`graphs` |
| 镜像标签 | `combinatorics`、`dsu`、`graphs`、`*2300` |
| Codeforces 通过次数 | 998 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/91/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/91/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P91C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

