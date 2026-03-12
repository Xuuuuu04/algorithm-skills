# CF-29E Quarrel

## 题面快照

## Description

Friends Alex and Bob live in Bertown. In this town there are n crossroads, some of them are connected by bidirectional roads of equal length. Bob lives in a house at the crossroads number 1, Alex — in a house at the crossroads number n.

One day Alex and Bob had a big quarrel, and they refused to see each other. It occurred that today Bob needs to get from his house to the crossroads n and Alex needs to get from his house to the crossroads 1. And they don't want to meet at any of the crossroads, but they can meet in the middle of the street, when passing it in opposite directions. Alex and Bob asked you, as their mutual friend, to help them with this difficult task.

Find for Alex and Bob such routes with equal number of streets that the guys can follow these routes and never appear at the same crossroads at the same time. They are allowed to meet in the middle of the street when moving toward each other (see Sample 1). Among all possible routes, select such that the number of streets in it is the least possible. Until both guys reach their destinations, none of them can stay without moving.

The guys are moving simultaneously with equal speeds, i.e. it is possible that when one of them reaches some of the crossroads, the other one leaves it. For example, Alex can move from crossroad 1 to crossroad 2, while Bob moves from crossroad 2 to crossroad 3.

If the required routes don't exist, your program should output -1.

The first line contains two integers n and m (2 ≤ n ≤ 500, 1 ≤ m ≤ 10000) — the amount of crossroads and the amount of roads. Each of the following m lines contains two integers — the numbers of crossroads connected by the road. It is guaranteed that no road connects a crossroads with itself and no two crossroads are connected by more than one road.

If the required routes don't exist, output -1. Otherwise, the first line should contain integer k — the length of shortest routes (the length of the route is the amount of roads in it). The next line should contain k + 1 integers — Bob's route, i.e. the numbers of k + 1 crossroads passed by Bob. The last line should contain Alex's route in the same format. If there are several optimal solutions, output any of them.

## Input

The first line contains two integers n and m (2 ≤ n ≤ 500, 1 ≤ m ≤ 10000) — the amount of crossroads and the amount of roads. Each of the following m lines contains two integers — the numbers of crossroads connected by the road. It is guaranteed that no road connects a crossroads with itself and no two crossroads are connected by more than one road.

## Output

If the required routes don't exist, output -1. Otherwise, the first line should contain integer k — the length of shortest routes (the length of the route is the amount of roads in it). The next line should contain k + 1 integers — Bob's route, i.e. the numbers of k + 1 crossroads passed by Bob. The last line should contain Alex's route in the same format. If there are several optimal solutions, output any of them.

## Samples

```
2 1
1 2

```

```
1
1 2
2 1

```

```
7 5
1 2
2 7
7 6
2 3
3 4

```

```
-1

```

```
7 6
1 2
2 7
7 6
2 3
3 4
1 5

```

```
6
1 2 3 4 3 2 7
7 6 7 2 1 5 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-29E |
| Contest | 29 |
| Index | E |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `graphs`、`shortest paths` |
| 镜像标签 | `graphs`、`shortest paths`、`*2400` |
| Codeforces 通过次数 | 1124 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/29/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/29/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P29E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

