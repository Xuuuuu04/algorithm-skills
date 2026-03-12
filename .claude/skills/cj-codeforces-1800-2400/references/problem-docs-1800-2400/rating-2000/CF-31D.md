# CF-31D Chocolate

## 题面快照

## Description

Bob has a rectangular chocolate bar of the size W × H. He introduced a cartesian coordinate system so that the point (0, 0) corresponds to the lower-left corner of the bar, and the point (W, H) corresponds to the upper-right corner. Bob decided to split the bar into pieces by breaking it. Each break is a segment parallel to one of the coordinate axes, which connects the edges of the bar. More formally, each break goes along the line x = xc or y = yc, where xc and yc are integers. It should divide one part of the bar into two non-empty parts. After Bob breaks some part into two parts, he breaks the resulting parts separately and independently from each other. Also he doesn't move the parts of the bar. Bob made n breaks and wrote them down in his notebook in arbitrary order. At the end he got n + 1 parts. Now he wants to calculate their areas. Bob is lazy, so he asks you to do this task.

The first line contains 3 integers W, H and n (1 ≤ W, H, n ≤ 100) — width of the bar, height of the bar and amount of breaks. Each of the following n lines contains four integers xi, 1, yi, 1, xi, 2, yi, 2 — coordinates of the endpoints of the i-th break (0 ≤ xi, 1 ≤ xi, 2 ≤ W, 0 ≤ yi, 1 ≤ yi, 2 ≤ H, or xi, 1 = xi, 2, or yi, 1 = yi, 2). Breaks are given in arbitrary order.

It is guaranteed that the set of breaks is correct, i.e. there is some order of the given breaks that each next break divides exactly one part of the bar into two non-empty parts.

Output n + 1 numbers — areas of the resulting parts in the increasing order.

## Input

The first line contains 3 integers W, H and n (1 ≤ W, H, n ≤ 100) — width of the bar, height of the bar and amount of breaks. Each of the following n lines contains four integers xi, 1, yi, 1, xi, 2, yi, 2 — coordinates of the endpoints of the i-th break (0 ≤ xi, 1 ≤ xi, 2 ≤ W, 0 ≤ yi, 1 ≤ yi, 2 ≤ H, or xi, 1 = xi, 2, or yi, 1 = yi, 2). Breaks are given in arbitrary order.

It is guaranteed that the set of breaks is correct, i.e. there is some order of the given breaks that each next break divides exactly one part of the bar into two non-empty parts.

## Output

Output n + 1 numbers — areas of the resulting parts in the increasing order.

## Samples

```
2 2 2
1 0 1 2
0 1 1 1

```

```
1 1 2

```

```
2 2 3
1 0 1 2
0 1 1 1
1 1 2 1

```

```
1 1 1 1

```

```
2 4 2
0 1 2 1
0 3 2 3

```

```
2 2 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-31D |
| Contest | 31 |
| Index | D |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dfs and similar`、`implementation` |
| 镜像标签 | `dfs and similar`、`implementation`、`*2000` |
| Codeforces 通过次数 | 1215 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/31/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/31/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P31D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

