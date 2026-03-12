# CF-43E Race

## 题面快照

## Description

Today s kilometer long auto race takes place in Berland. The track is represented by a straight line as long as s kilometers. There are n cars taking part in the race, all of them start simultaneously at the very beginning of the track. For every car is known its behavior — the system of segments on each of which the speed of the car is constant. The j-th segment of the i-th car is pair (vi, j, ti, j), where vi, j is the car's speed on the whole segment in kilometers per hour and ti, j is for how many hours the car had been driving at that speed. The segments are given in the order in which they are "being driven on" by the cars.

Your task is to find out how many times during the race some car managed to have a lead over another car. A lead is considered a situation when one car appears in front of another car. It is known, that all the leads happen instantly, i. e. there are no such time segment of positive length, during which some two cars drive "together". At one moment of time on one and the same point several leads may appear. In this case all of them should be taken individually. Meetings of cars at the start and finish are not considered to be counted as leads.

The first line contains two integers n and s (2 ≤ n ≤ 100, 1 ≤ s ≤ 106) — the number of cars and the length of the track in kilometers. Then follow n lines — the description of the system of segments for each car. Every description starts with integer k (1 ≤ k ≤ 100) — the number of segments in the system. Then k space-separated pairs of integers are written. Each pair is the speed and time of the segment. These integers are positive and don't exceed 1000. It is guaranteed, that the sum of lengths of all segments (in kilometers) for each car equals to s; and all the leads happen instantly.

Print the single number — the number of times some car managed to take the lead over another car during the race.

## Input

The first line contains two integers n and s (2 ≤ n ≤ 100, 1 ≤ s ≤ 106) — the number of cars and the length of the track in kilometers. Then follow n lines — the description of the system of segments for each car. Every description starts with integer k (1 ≤ k ≤ 100) — the number of segments in the system. Then k space-separated pairs of integers are written. Each pair is the speed and time of the segment. These integers are positive and don't exceed 1000. It is guaranteed, that the sum of lengths of all segments (in kilometers) for each car equals to s; and all the leads happen instantly.

## Output

Print the single number — the number of times some car managed to take the lead over another car during the race.

## Samples

```
2 33
2 5 1 2 14
1 3 11

```

```
1

```

```
2 33
2 1 3 10 3
1 11 3

```

```
0

```

```
5 33
2 1 3 3 10
1 11 3
2 5 3 3 6
2 3 1 10 3
2 6 3 3 5

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-43E |
| Contest | 43 |
| Index | E |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `brute force`、`implementation`、`two pointers` |
| 镜像标签 | `brute force`、`implementation`、`two pointers`、`*2300` |
| Codeforces 通过次数 | 435 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/43/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/43/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P43E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

