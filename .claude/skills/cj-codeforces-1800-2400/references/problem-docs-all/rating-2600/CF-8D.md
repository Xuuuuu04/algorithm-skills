# CF-8D Two Friends

## 题面快照

## Description

Two neighbours, Alan and Bob, live in the city, where there are three buildings only: a cinema, a shop and the house, where they live. The rest is a big asphalt square.

Once they went to the cinema, and the film impressed them so deeply, that when they left the cinema, they did not want to stop discussing it.

Bob wants to get home, but Alan has to go to the shop first, and only then go home. So, they agreed to cover some distance together discussing the film (their common path might pass through the shop, or they might walk circles around the cinema together), and then to part each other's company and go each his own way. After they part, they will start thinking about their daily pursuits; and even if they meet again, they won't be able to go on with the discussion. Thus, Bob's path will be a continuous curve, having the cinema and the house as its ends. Alan's path — a continuous curve, going through the shop, and having the cinema and the house as its ends.

The film ended late, that's why the whole distance covered by Alan should not differ from the shortest one by more than t1, and the distance covered by Bob should not differ from the shortest one by more than t2.

Find the maximum distance that Alan and Bob will cover together, discussing the film.

The first line contains two integers: t1, t2 (0 ≤ t1, t2 ≤ 100). The second line contains the cinema's coordinates, the third one — the house's, and the last line — the shop's.

All the coordinates are given in meters, are integer, and do not exceed 100 in absolute magnitude. No two given places are in the same building.

In the only line output one number — the maximum distance that Alan and Bob will cover together, discussing the film. Output the answer accurate to not less than 4 decimal places.

## Input

The first line contains two integers: t1, t2 (0 ≤ t1, t2 ≤ 100). The second line contains the cinema's coordinates, the third one — the house's, and the last line — the shop's.

All the coordinates are given in meters, are integer, and do not exceed 100 in absolute magnitude. No two given places are in the same building.

## Output

In the only line output one number — the maximum distance that Alan and Bob will cover together, discussing the film. Output the answer accurate to not less than 4 decimal places.

## Samples

```
0 2
0 0
4 0
-3 0

```

```
1.0000000000

```

```
0 0
0 0
2 0
1 0

```

```
2.0000000000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-8D |
| Contest | 8 |
| Index | D |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | `binary search`、`geometry` |
| 镜像标签 | `binary search`、`geometry`、`*2600` |
| Codeforces 通过次数 | 573 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/8/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/8/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P8D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

