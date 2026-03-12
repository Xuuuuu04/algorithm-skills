# CF-24D Broken robot

## 题面快照

## Description

You received as a gift a very clever robot walking on a rectangular board. Unfortunately, you understood that it is broken and behaves rather strangely (randomly). The board consists of N rows and M columns of cells. The robot is initially at some cell on the i-th row and the j-th column. Then at every step the robot could go to some another cell. The aim is to go to the bottommost (N-th) row. The robot can stay at it's current cell, move to the left, move to the right, or move to the cell below the current. If the robot is in the leftmost column it cannot move to the left, and if it is in the rightmost column it cannot move to the right. At every step all possible moves are equally probable. Return the expected number of step to reach the bottommost row.

On the first line you will be given two space separated integers N and M (1 ≤ N, M ≤ 1000). On the second line you will be given another two space separated integers i and j (1 ≤ i ≤ N, 1 ≤ j ≤ M) — the number of the initial row and the number of the initial column. Note that, (1, 1) is the upper left corner of the board and (N, M) is the bottom right corner.

Output the expected number of steps on a line of itself with at least 4 digits after the decimal point.

## Input

On the first line you will be given two space separated integers N and M (1 ≤ N, M ≤ 1000). On the second line you will be given another two space separated integers i and j (1 ≤ i ≤ N, 1 ≤ j ≤ M) — the number of the initial row and the number of the initial column. Note that, (1, 1) is the upper left corner of the board and (N, M) is the bottom right corner.

## Output

Output the expected number of steps on a line of itself with at least 4 digits after the decimal point.

## Samples

```
10 10
10 4

```

```
0.0000000000

```

```
10 14
5 14

```

```
18.0038068653

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-24D |
| Contest | 24 |
| Index | D |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `dp`、`math`、`probabilities` |
| 镜像标签 | `dp`、`math`、`probabilities`、`*2400` |
| Codeforces 通过次数 | 2598 |
| 镜像尝试 / 通过 | 4 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/24/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/24/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P24D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

