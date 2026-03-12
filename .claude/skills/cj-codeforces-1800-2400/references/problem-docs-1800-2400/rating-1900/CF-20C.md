# CF-20C Dijkstra?

## 题面快照

## Description

You are given a weighted undirected graph. The vertices are enumerated from 1 to n. Your task is to find the shortest path between the vertex 1 and the vertex n.

The first line contains two integers n and m (2 ≤ n ≤ 105, 0 ≤ m ≤ 105), where n is the number of vertices and m is the number of edges. Following m lines contain one edge each in form ai, bi and wi (1 ≤ ai, bi ≤ n, 1 ≤ wi ≤ 106), where ai, bi are edge endpoints and wi is the length of the edge.

It is possible that the graph has loops and multiple edges between pair of vertices.

Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many solutions, print any of them.

## Input

The first line contains two integers n and m (2 ≤ n ≤ 105, 0 ≤ m ≤ 105), where n is the number of vertices and m is the number of edges. Following m lines contain one edge each in form ai, bi and wi (1 ≤ ai, bi ≤ n, 1 ≤ wi ≤ 106), where ai, bi are edge endpoints and wi is the length of the edge.

It is possible that the graph has loops and multiple edges between pair of vertices.

## Output

Write the only integer -1 in case of no path. Write the shortest path in opposite case. If there are many solutions, print any of them.

## Samples

```
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1

```

```
1 4 3 5

```

```
5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1

```

```
1 4 3 5

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-20C |
| Contest | 20 |
| Index | C |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `graphs`、`shortest paths` |
| 镜像标签 | `graphs`、`shortest paths`、`*1900` |
| Codeforces 通过次数 | 44348 |
| 镜像尝试 / 通过 | 11 / 1 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/20/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/20/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P20C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

