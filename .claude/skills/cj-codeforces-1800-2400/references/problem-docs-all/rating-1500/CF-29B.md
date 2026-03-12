# CF-29B Traffic Lights

## 题面快照

## Description

A car moves from point A to point B at speed v meters per second. The action takes place on the X-axis. At the distance d meters from A there are traffic lights. Starting from time 0, for the first g seconds the green light is on, then for the following r seconds the red light is on, then again the green light is on for the g seconds, and so on.

The car can be instantly accelerated from 0 to v and vice versa, can instantly slow down from the v to 0. Consider that it passes the traffic lights at the green light instantly. If the car approaches the traffic lights at the moment when the red light has just turned on, it doesn't have time to pass it. But if it approaches the traffic lights at the moment when the green light has just turned on, it can move. The car leaves point A at the time 0.

What is the minimum time for the car to get from point A to point B without breaking the traffic rules?

The first line contains integers l, d, v, g, r (1 ≤ l, d, v, g, r ≤ 1000, d < l) — the distance between A and B (in meters), the distance from A to the traffic lights, car's speed, the duration of green light and the duration of red light.

Output a single number — the minimum time that the car needs to get from point A to point B. Your output must have relative or absolute error less than 10 - 6.

## Input

The first line contains integers l, d, v, g, r (1 ≤ l, d, v, g, r ≤ 1000, d < l) — the distance between A and B (in meters), the distance from A to the traffic lights, car's speed, the duration of green light and the duration of red light.

## Output

Output a single number — the minimum time that the car needs to get from point A to point B. Your output must have relative or absolute error less than 10 - 6.

## Samples

```
2 1 3 4 5

```

```
0.66666667

```

```
5 4 3 1 1

```

```
2.33333333

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-29B |
| Contest | 29 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1500` |
| Codeforces 通过次数 | 3318 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/29/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/29/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P29B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

