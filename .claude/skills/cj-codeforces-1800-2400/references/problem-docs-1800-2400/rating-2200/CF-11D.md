# CF-11D A Simple Task

## 题面快照

## Description

Given a simple graph, output the number of simple cycles in it. A simple cycle is a cycle with no repeated vertices or edges.

The first line of input contains two integers n and m (1 ≤ n ≤ 19, 0 ≤ m) – respectively the number of vertices and edges of the graph. Each of the subsequent m lines contains two integers a and b, (1 ≤ a, b ≤ n, a ≠ b) indicating that vertices a and b are connected by an undirected edge. There is no more than one edge connecting any pair of vertices.

Output the number of cycles in the given graph.

## Input

The first line of input contains two integers n and m (1 ≤ n ≤ 19, 0 ≤ m) – respectively the number of vertices and edges of the graph. Each of the subsequent m lines contains two integers a and b, (1 ≤ a, b ≤ n, a ≠ b) indicating that vertices a and b are connected by an undirected edge. There is no more than one edge connecting any pair of vertices.

## Output

Output the number of cycles in the given graph.

## Samples

```
4 6
1 2
1 3
1 4
2 3
2 4
3 4

```

```
7

```

## Note

The example graph is a clique and contains four cycles of length 3 and three cycles of length 4.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-11D |
| Contest | 11 |
| Index | D |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `bitmasks`、`dp`、`graphs` |
| 镜像标签 | `bitmasks`、`dp`、`graphs`、`*2200` |
| Codeforces 通过次数 | 6207 |
| 镜像尝试 / 通过 | 5 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/11/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/11/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P11D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

