# CF-51F Caterpillar

## 题面快照

## Description

An undirected graph is called a caterpillar if it is a connected graph without cycles and it has such a path p that any vertex is located at a distance of at most 1 from the path p. The caterpillar can contain loops (edges from a vertex to itself) but cannot contain multiple (parallel) edges.

The picture contains an example of a caterpillar:

You are given an undirected graph G. You are allowed to do a merging operations, each such operation merges two vertices into one vertex. For that two any vertices a and b (a ≠ b) are chosen. These verteces are deleted together with their edges (which are incident to at least one of the vertices a or b) but a new vertex w is added together with edges (x, w) for each edge (a, w) and/or (b, w). If there was the edge (a, b) it transforms to the loop (w, w). The resulting graph (after the merging operation) may contain multiple (parallel) edges between pairs of vertices and loops. Let us note that this operation decreases the number of vertices of graph by 1 but leaves the number of edges in the graph unchanged.

The merging operation can be informally described as a unity of two vertices of the graph into one with the natural transformation of the graph edges.

You may apply this operation consecutively and make the given graph to be a caterpillar. Write a program that will print the minimal number of merging operations required to make the given graph a caterpillar.

The first line contains a pair of integers n, m (1 ≤ n ≤ 2000;0 ≤ m ≤ 105), where n represents the number of vertices in the graph and m is the number of edges in it. Then the following m lines contain edge descriptions, one edge description per line. Every line contains a pair of integers ai, bi (1 ≤ ai, bi ≤ n;ai ≠ bi), ai, bi which represent the indices of the vertices connected by the edge. The vertices are numbered from 1 to n. In the given graph it will be no more than one edge between any pair of vertices. The given graph is not necessarily connected.

Print the minimal required number of operations.

## Input

The first line contains a pair of integers n, m (1 ≤ n ≤ 2000;0 ≤ m ≤ 105), where n represents the number of vertices in the graph and m is the number of edges in it. Then the following m lines contain edge descriptions, one edge description per line. Every line contains a pair of integers ai, bi (1 ≤ ai, bi ≤ n;ai ≠ bi), ai, bi which represent the indices of the vertices connected by the edge. The vertices are numbered from 1 to n. In the given graph it will be no more than one edge between any pair of vertices. The given graph is not necessarily connected.

## Output

Print the minimal required number of operations.

## Samples

```
4 4
1 2
2 3
3 4
4 2

```

```
2

```

```
6 3
1 2
3 4
5 6

```

```
2

```

```
7 6
1 2
2 3
1 4
4 5
1 6
6 7

```

```
1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-51F |
| Contest | 51 |
| Index | F |
| Rating | 2800 |
| Points | 3000.0 |
| Codeforces 标签 | `dfs and similar`、`dp`、`graphs`、`trees` |
| 镜像标签 | `dfs and similar`、`dp`、`graphs`、`trees`、`*2800` |
| Codeforces 通过次数 | 800 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/51/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/51/problem/F)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P51F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

