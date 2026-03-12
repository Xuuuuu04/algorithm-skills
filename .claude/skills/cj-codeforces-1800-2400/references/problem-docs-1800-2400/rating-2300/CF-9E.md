# CF-9E Interestring graph and Apples

## 题面快照

## Description

Hexadecimal likes drawing. She has drawn many graphs already, both directed and not. Recently she has started to work on a still-life «interesting graph and apples». An undirected graph is called interesting, if each of its vertices belongs to one cycle only — a funny ring — and does not belong to any other cycles. A funny ring is a cycle that goes through all the vertices just once. Moreover, loops are funny rings too.

She has already drawn the apples and some of the graph edges. But now it is not clear, how to connect the rest of the vertices to get an interesting graph as a result. The answer should contain the minimal amount of added edges. And furthermore, the answer should be the lexicographically smallest one. The set of edges (x1, y1), (x2, y2), ..., (xn, yn), where xi ≤ yi, is lexicographically smaller than the set (u1, v1), (u2, v2), ..., (un, vn), where ui ≤ vi, provided that the sequence of integers x1, y1, x2, y2, ..., xn, yn is lexicographically smaller than the sequence u1, v1, u2, v2, ..., un, vn. If you do not cope, Hexadecimal will eat you. ...eat you alive.

The first line of the input data contains a pair of integers n and m (1 ≤ n ≤ 50, 0 ≤ m ≤ 2500) — the amount of vertices and edges respectively. The following lines contain pairs of numbers xi and yi (1 ≤ xi, yi ≤ n) — the vertices that are already connected by edges. The initial graph may contain multiple edges and loops.

In the first line output «YES» or «NO»: if it is possible or not to construct an interesting graph. If the answer is «YES», in the second line output k — the amount of edges that should be added to the initial graph. Finally, output k lines: pairs of vertices xj and yj, between which edges should be drawn. The result may contain multiple edges and loops. k can be equal to zero.

## Input

The first line of the input data contains a pair of integers n and m (1 ≤ n ≤ 50, 0 ≤ m ≤ 2500) — the amount of vertices and edges respectively. The following lines contain pairs of numbers xi and yi (1 ≤ xi, yi ≤ n) — the vertices that are already connected by edges. The initial graph may contain multiple edges and loops.

## Output

In the first line output «YES» or «NO»: if it is possible or not to construct an interesting graph. If the answer is «YES», in the second line output k — the amount of edges that should be added to the initial graph. Finally, output k lines: pairs of vertices xj and yj, between which edges should be drawn. The result may contain multiple edges and loops. k can be equal to zero.

## Samples

```
3 2
1 2
2 3

```

```
YES
1
1 3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-9E |
| Contest | 9 |
| Index | E |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `dfs and similar`、`dsu`、`graphs` |
| 镜像标签 | `dfs and similar`、`dsu`、`graphs`、`*2300` |
| Codeforces 通过次数 | 1151 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/9/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/9/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P9E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

