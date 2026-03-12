# CF-57A Square Earth?

## 题面快照

## Description

Meg the Rabbit decided to do something nice, specifically — to determine the shortest distance between two points on the surface of our planet. But Meg... what can you say, she wants everything simple. So, she already regards our planet as a two-dimensional circle. No, wait, it's even worse — as a square of side n. Thus, the task has been reduced to finding the shortest path between two dots on a square (the path should go through the square sides). To simplify the task let us consider the vertices of the square to lie at points whose coordinates are: (0, 0), (n, 0), (0, n) and (n, n).

The single line contains 5 space-separated integers: n, x1, y1, x2, y2 (1 ≤ n ≤ 1000, 0 ≤ x1, y1, x2, y2 ≤ n) which correspondingly represent a side of the square, the coordinates of the first point and the coordinates of the second point. It is guaranteed that the points lie on the sides of the square.

You must print on a single line the shortest distance between the points.

## Input

The single line contains 5 space-separated integers: n, x1, y1, x2, y2 (1 ≤ n ≤ 1000, 0 ≤ x1, y1, x2, y2 ≤ n) which correspondingly represent a side of the square, the coordinates of the first point and the coordinates of the second point. It is guaranteed that the points lie on the sides of the square.

## Output

You must print on a single line the shortest distance between the points.

## Samples

```
2 0 0 1 0

```

```
1

```

```
2 0 1 2 1

```

```
4

```

```
100 0 0 100 100

```

```
200

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-57A |
| Contest | 57 |
| Index | A |
| Rating | 1300 |
| Points | 500.0 |
| Codeforces 标签 | `dfs and similar`、`greedy`、`implementation` |
| 镜像标签 | `dfs and similar`、`greedy`、`implementation`、`*1300` |
| Codeforces 通过次数 | 3215 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/57/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/57/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P57A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

