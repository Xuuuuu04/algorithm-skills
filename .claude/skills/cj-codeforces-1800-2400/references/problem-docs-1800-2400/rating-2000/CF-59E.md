# CF-59E Shortest Path

## 题面快照

## Description

In Ancient Berland there were n cities and m two-way roads of equal length. The cities are numbered with integers from 1 to n inclusively. According to an ancient superstition, if a traveller visits three cities ai, bi, ci in row, without visiting other cities between them, a great disaster awaits him. Overall there are k such city triplets. Each triplet is ordered, which means that, for example, you are allowed to visit the cities in the following order: ai, ci, bi. Vasya wants to get from the city 1 to the city n and not fulfil the superstition. Find out which minimal number of roads he should take. Also you are required to find one of his possible path routes.

The first line contains three integers n, m, k (2 ≤ n ≤ 3000, 1 ≤ m ≤ 20000, 0 ≤ k ≤ 105) which are the number of cities, the number of roads and the number of the forbidden triplets correspondingly.

Then follow m lines each containing two integers xi, yi (1 ≤ xi, yi ≤ n) which are the road descriptions. The road is described by the numbers of the cities it joins. No road joins a city with itself, there cannot be more than one road between a pair of cities.

Then follow k lines each containing three integers ai, bi, ci (1 ≤ ai, bi, ci ≤ n) which are the forbidden triplets. Each ordered triplet is listed mo more than one time. All three cities in each triplet are distinct.

City n can be unreachable from city 1 by roads.

If there are no path from 1 to n print -1. Otherwise on the first line print the number of roads d along the shortest path from the city 1 to the city n. On the second line print d + 1 numbers — any of the possible shortest paths for Vasya. The path should start in the city 1 and end in the city n.

## Input

The first line contains three integers n, m, k (2 ≤ n ≤ 3000, 1 ≤ m ≤ 20000, 0 ≤ k ≤ 105) which are the number of cities, the number of roads and the number of the forbidden triplets correspondingly.

Then follow m lines each containing two integers xi, yi (1 ≤ xi, yi ≤ n) which are the road descriptions. The road is described by the numbers of the cities it joins. No road joins a city with itself, there cannot be more than one road between a pair of cities.

Then follow k lines each containing three integers ai, bi, ci (1 ≤ ai, bi, ci ≤ n) which are the forbidden triplets. Each ordered triplet is listed mo more than one time. All three cities in each triplet are distinct.

City n can be unreachable from city 1 by roads.

## Output

If there are no path from 1 to n print -1. Otherwise on the first line print the number of roads d along the shortest path from the city 1 to the city n. On the second line print d + 1 numbers — any of the possible shortest paths for Vasya. The path should start in the city 1 and end in the city n.

## Samples

```
4 4 1
1 2
2 3
3 4
1 3
1 4 3

```

```
2
1 3 4

```

```
3 1 0
1 2

```

```
-1

```

```
4 4 2
1 2
2 3
3 4
1 3
1 2 3
1 3 4

```

```
4
1 3 2 3 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-59E |
| Contest | 59 |
| Index | E |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `graphs`、`shortest paths` |
| 镜像标签 | `graphs`、`shortest paths`、`*2000` |
| Codeforces 通过次数 | 4661 |
| 镜像尝试 / 通过 | 1 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/59/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/59/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P59E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

