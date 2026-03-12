# CF-29D Ant on the Tree

## 题面快照

## Description

Connected undirected graph without cycles is called a tree. Trees is a class of graphs which is interesting not only for people, but for ants too.

An ant stands at the root of some tree. He sees that there are n vertexes in the tree, and they are connected by n - 1 edges so that there is a path between any pair of vertexes. A leaf is a distinct from root vertex, which is connected with exactly one other vertex.

The ant wants to visit every vertex in the tree and return to the root, passing every edge twice. In addition, he wants to visit the leaves in a specific order. You are to find some possible route of the ant.

The first line contains integer n (3 ≤ n ≤ 300) — amount of vertexes in the tree. Next n - 1 lines describe edges. Each edge is described with two integers — indexes of vertexes which it connects. Each edge can be passed in any direction. Vertexes are numbered starting from 1. The root of the tree has number 1. The last line contains k integers, where k is amount of leaves in the tree. These numbers describe the order in which the leaves should be visited. It is guaranteed that each leaf appears in this order exactly once.

If the required route doesn't exist, output -1. Otherwise, output 2n - 1 numbers, describing the route. Every time the ant comes to a vertex, output it's index.

## Input

The first line contains integer n (3 ≤ n ≤ 300) — amount of vertexes in the tree. Next n - 1 lines describe edges. Each edge is described with two integers — indexes of vertexes which it connects. Each edge can be passed in any direction. Vertexes are numbered starting from 1. The root of the tree has number 1. The last line contains k integers, where k is amount of leaves in the tree. These numbers describe the order in which the leaves should be visited. It is guaranteed that each leaf appears in this order exactly once.

## Output

If the required route doesn't exist, output -1. Otherwise, output 2n - 1 numbers, describing the route. Every time the ant comes to a vertex, output it's index.

## Samples

```
3
1 2
2 3
3

```

```
1 2 3 2 1

```

```
6
1 2
1 3
2 4
4 5
4 6
5 6 3

```

```
1 2 4 5 4 6 4 2 1 3 1

```

```
6
1 2
1 3
2 4
4 5
4 6
5 3 6

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-29D |
| Contest | 29 |
| Index | D |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`dfs and similar`、`trees` |
| 镜像标签 | `constructive algorithms`、`dfs and similar`、`trees`、`*2000` |
| Codeforces 通过次数 | 2913 |
| 镜像尝试 / 通过 | 1 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/29/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/29/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P29D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

