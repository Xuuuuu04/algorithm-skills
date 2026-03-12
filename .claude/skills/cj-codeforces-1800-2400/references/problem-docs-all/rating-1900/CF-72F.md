# CF-72F Oil

## 题面快照

## Description

After the nationalization of the oil industry, Dr. Mosaddegh wants to dig some oil wells to extract all the oil in Persian Gulf. But Persian Gulf is huge and has an infinite amount of oil. So Dr. Mosaddegh works only on a rectangular plane of size n × m of the Persian Gulf. Each of the cells in this rectangle either contains an infinite amount of oil or nothing.

Two cells are considered adjacent if and only if they have a common edge, a path is a sequence c1, c2, ..., cx of cells so that all of them contain oil and for each i, ci is adjacent to ci - 1 and ci + 1 (if they exist). Two cells are considered connected to each other if and only if there exists a path between them. If we dig a well in a certain cell, we can extract oil from all the cells that are connected to it by oil paths. It is not allowed to dig wells on empty cells.

Dr. Mosaddegh also knows that in Persian Gulf, the empty cells form rows and columns. I. e. if some cell is empty, then it's column is completely empty or it's row is completely empty, or both.

Help Dr. Mosaddegh find out how many wells he has to dig to access all the oil in that region.

In the first line there are two positive integers n and m (1 ≤ n, m ≤ 100).

In the second line there is an integer t (0 ≤ t ≤ n), the number of empty rows. t distinct positive integers follow, these are the numbers of empty rows and are in range [1, n].

In the second line there is an integer s (0 ≤ s ≤ m) that shows the number of columns not having any oil. s distinct positive integers follow, these are the numbers of empty columns and are in range of [1, m].

Note that rows are numbered from 1 to n (from top to bottom) and columns are numbered from 1 to m (from left to right).

A single integer, the minimum number of wells that Dr. Mossadegh has to dig.

This is actually finding how many regions are made by removing the given rows and columns.

## Input

In the first line there are two positive integers n and m (1 ≤ n, m ≤ 100).

In the second line there is an integer t (0 ≤ t ≤ n), the number of empty rows. t distinct positive integers follow, these are the numbers of empty rows and are in range [1, n].

In the second line there is an integer s (0 ≤ s ≤ m) that shows the number of columns not having any oil. s distinct positive integers follow, these are the numbers of empty columns and are in range of [1, m].

Note that rows are numbered from 1 to n (from top to bottom) and columns are numbered from 1 to m (from left to right).

## Output

A single integer, the minimum number of wells that Dr. Mossadegh has to dig.

This is actually finding how many regions are made by removing the given rows and columns.

## Samples

```
2 3
1 2
1 2

```

```
2

```

```
4 4
2 2 3
3 2 3 1

```

```
2

```

```
2 3
1 1
0

```

```
1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-72F |
| Contest | 72 |
| Index | F |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `*special`、`greedy`、`math` |
| 镜像标签 | `*special problem`、`greedy`、`math`、`*1900` |
| Codeforces 通过次数 | 143 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/72/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/72/problem/F)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P72F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

