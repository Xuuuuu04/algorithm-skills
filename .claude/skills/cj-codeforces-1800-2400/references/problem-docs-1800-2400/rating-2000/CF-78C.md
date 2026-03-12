# CF-78C Beaver Game

## 题面快照

## Description

Two beavers, Timur and Marsel, play the following game.

There are n logs, each of exactly m meters in length. The beavers move in turns. For each move a beaver chooses a log and gnaws it into some number (more than one) of equal parts, the length of each one is expressed by an integer and is no less than k meters. Each resulting part is also a log which can be gnawed in future by any beaver. The beaver that can't make a move loses. Thus, the other beaver wins.

Timur makes the first move. The players play in the optimal way. Determine the winner.

The first line contains three integers n, m, k (1 ≤ n, m, k ≤ 109).

Print "Timur", if Timur wins, or "Marsel", if Marsel wins. You should print everything without the quotes.

## Input

The first line contains three integers n, m, k (1 ≤ n, m, k ≤ 109).

## Output

Print "Timur", if Timur wins, or "Marsel", if Marsel wins. You should print everything without the quotes.

## Samples

```
1 15 4

```

```
Timur

```

```
4 9 5

```

```
Marsel

```

## Note

In the first sample the beavers only have one log, of 15 meters in length. Timur moves first. The only move he can do is to split the log into 3 parts each 5 meters in length. Then Marsel moves but he can't split any of the resulting logs, as k = 4. Thus, the winner is Timur.

In the second example the beavers have 4 logs 9 meters in length. Timur can't split any of them, so that the resulting parts possessed the length of not less than 5 meters, that's why he loses instantly.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-78C |
| Contest | 78 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dp`、`games`、`number theory` |
| 镜像标签 | `dp`、`games`、`number theory`、`*2000` |
| Codeforces 通过次数 | 2152 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/78/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/78/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P78C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

