# CF-30D King's Problem?

## 题面快照

## Description

Every true king during his life must conquer the world, hold the Codeforces world finals, win pink panda in the shooting gallery and travel all over his kingdom.

King Copa has already done the first three things. Now he just needs to travel all over the kingdom. The kingdom is an infinite plane with Cartesian coordinate system on it. Every city is a point on this plane. There are n cities in the kingdom at points with coordinates (x1, 0), (x2, 0), ..., (xn, 0), and there is one city at point (xn + 1, yn + 1).

King starts his journey in the city number k. Your task is to find such route for the king, which visits all cities (in any order) and has minimum possible length. It is allowed to visit a city twice. The king can end his journey in any city. Between any pair of cities there is a direct road with length equal to the distance between the corresponding points. No two cities may be located at the same point.

The first line contains two integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ n + 1) — amount of cities and index of the starting city. The second line contains n + 1 numbers xi. The third line contains yn + 1. All coordinates are integers and do not exceed 106 by absolute value. No two cities coincide.

Output the minimum possible length of the journey. Your answer must have relative or absolute error less than 10 - 6.

## Input

The first line contains two integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ n + 1) — amount of cities and index of the starting city. The second line contains n + 1 numbers xi. The third line contains yn + 1. All coordinates are integers and do not exceed 106 by absolute value. No two cities coincide.

## Output

Output the minimum possible length of the journey. Your answer must have relative or absolute error less than 10 - 6.

## Samples

```
3 1
0 1 2 1
1

```

```
3.41421356237309490000

```

```
3 1
1 0 2 1
1

```

```
3.82842712474619030000

```

```
4 5
0 5 -1 -5 2
3

```

```
14.24264068711928400000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-30D |
| Contest | 30 |
| Index | D |
| Rating | 2600 |
| Points | 2000.0 |
| Codeforces 标签 | `geometry`、`greedy` |
| 镜像标签 | `geometry`、`greedy`、`*2600` |
| Codeforces 通过次数 | 487 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/30/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/30/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P30D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

