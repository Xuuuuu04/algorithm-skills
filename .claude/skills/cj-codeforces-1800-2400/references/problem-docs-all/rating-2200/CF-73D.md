# CF-73D FreeDiv

## 题面快照

## Description

Vasya plays FreeDiv. In this game he manages a huge state, which has n cities and m two-way roads between them. Unfortunately, not from every city you can reach any other one moving along these roads. Therefore Vasya decided to divide the state into provinces so that in every province, one could reach from every city all the cities of the province, but there are no roads between provinces.

Unlike other turn-based strategies, in FreeDiv a player has the opportunity to build tunnels between cities. The tunnels are two-way roads along which one can move armies undetected by the enemy. However, no more than one tunnel can be connected to each city. As for Vasya, he wants to build a network of tunnels so that any pair of cities in his state were reachable by some path consisting of roads and a tunnels. But at that no more than k tunnels are connected to each province (otherwise, the province will be difficult to keep in case other provinces are captured by enemy armies).

Vasya discovered that maybe he will not be able to build such a network for the current condition of the state. Maybe he'll have first to build several roads between cities in different provinces to merge the provinces. Your task is to determine the minimum number of roads Vasya needs to build so that it was possible to build the required network of tunnels in the resulting state.

The first line contains three integers n, m and k (1 ≤ n, k ≤ 106, 0 ≤ m ≤ 106). Each of the next m lines contains two integers. They are the numbers of cities connected by a corresponding road. No road connects city to itself and there is at most one road between each pair of cities.

Print a single number, the minimum number of additional roads.

## Input

The first line contains three integers n, m and k (1 ≤ n, k ≤ 106, 0 ≤ m ≤ 106). Each of the next m lines contains two integers. They are the numbers of cities connected by a corresponding road. No road connects city to itself and there is at most one road between each pair of cities.

## Output

Print a single number, the minimum number of additional roads.

## Samples

```
3 3 2
1 2
2 3
3 1

```

```
0

```

```
4 2 2
1 2
3 4

```

```
0

```

```
4 0 2

```

```
1

```

## Note

In the first example only one province exists, so it is not necessary to build any tunnels or roads.

In the second example two provinces exist. It is possible to merge the provinces by building a tunnel between cities 1 and 3.

In the third example at least one additional road is necessary. For example it is possible to build additional road between cities 1 and 2 and build two tunnels between cities 1 and 3, 2 and 4 after that.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-73D |
| Contest | 73 |
| Index | D |
| Rating | 2200 |
| Points | 1500.0 |
| Codeforces 标签 | `dfs and similar`、`graphs`、`greedy` |
| 镜像标签 | `dfs and similar`、`graphs`、`greedy`、`*2200` |
| Codeforces 通过次数 | 742 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/73/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/73/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P73D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

