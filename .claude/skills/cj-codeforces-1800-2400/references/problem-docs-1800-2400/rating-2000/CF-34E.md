# CF-34E Collisions

## 题面快照

## Description

On a number line there are n balls. At time moment 0 for each ball the following data is known: its coordinate xi, speed vi (possibly, negative) and weight mi. The radius of the balls can be ignored.

The balls collide elastically, i.e. if two balls weighing m1 and m2 and with speeds v1 and v2 collide, their new speeds will be:
.
Your task is to find out, where each ball will be t seconds after.

The first line contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 100) — amount of balls and duration of the process. Then follow n lines, each containing three integers: xi, vi, mi (1 ≤ |vi|, mi ≤ 100, |xi| ≤ 100) — coordinate, speed and weight of the ball with index i at time moment 0.

It is guaranteed that no two balls have the same coordinate initially. Also each collision will be a collision of not more than two balls (that is, three or more balls never collide at the same point in all times from segment [0;t]).

Output n numbers — coordinates of the balls t seconds after. Output the numbers accurate to at least 4 digits after the decimal point.

## Input

The first line contains two integers n and t (1 ≤ n ≤ 10, 0 ≤ t ≤ 100) — amount of balls and duration of the process. Then follow n lines, each containing three integers: xi, vi, mi (1 ≤ |vi|, mi ≤ 100, |xi| ≤ 100) — coordinate, speed and weight of the ball with index i at time moment 0.

It is guaranteed that no two balls have the same coordinate initially. Also each collision will be a collision of not more than two balls (that is, three or more balls never collide at the same point in all times from segment [0;t]).

## Output

Output n numbers — coordinates of the balls t seconds after. Output the numbers accurate to at least 4 digits after the decimal point.

## Samples

```
2 9
3 4 5
0 7 8

```

```
68.538461538
44.538461538

```

```
3 10
1 2 3
4 -5 6
7 -8 9

```

```
-93.666666667
-74.666666667
-15.666666667

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-34E |
| Contest | 34 |
| Index | E |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `brute force`、`implementation`、`math` |
| 镜像标签 | `brute force`、`implementation`、`math`、`*2000` |
| Codeforces 通过次数 | 646 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/34/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/34/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P34E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

