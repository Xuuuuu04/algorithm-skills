# CF-13D Triangles

## 题面快照

## Description

Little Petya likes to draw. He drew N red and M blue points on the plane in such a way that no three points lie on the same line. Now he wonders what is the number of distinct triangles with vertices in red points which do not contain any blue point inside.

The first line contains two non-negative integer numbers N and M (0 ≤ N ≤ 500, 0 ≤ M ≤ 500) — the number of red and blue points respectively. The following N lines contain two integer numbers each — coordinates of red points. The following M lines contain two integer numbers each — coordinates of blue points. All coordinates do not exceed 109 by absolute value.

Output one integer — the number of distinct triangles with vertices in red points which do not contain any blue point inside.

## Input

The first line contains two non-negative integer numbers N and M (0 ≤ N ≤ 500, 0 ≤ M ≤ 500) — the number of red and blue points respectively. The following N lines contain two integer numbers each — coordinates of red points. The following M lines contain two integer numbers each — coordinates of blue points. All coordinates do not exceed 109 by absolute value.

## Output

Output one integer — the number of distinct triangles with vertices in red points which do not contain any blue point inside.

## Samples

```
4 1
0 0
10 0
10 10
5 4
2 1

```

```
2

```

```
5 5
5 10
6 1
8 6
-6 -7
7 -1
5 -1
10 -4
-10 -8
-10 5
-2 -8

```

```
7

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-13D |
| Contest | 13 |
| Index | D |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | `dp`、`geometry` |
| 镜像标签 | `dp`、`geometry`、`*2600` |
| Codeforces 通过次数 | 726 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/13/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/13/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P13D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

