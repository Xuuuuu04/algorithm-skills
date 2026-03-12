# CF-37B Computer Game

## 题面快照

## Description

Vasya’s elder brother Petya loves playing computer games. In one of his favourite computer games Petya reached the final level where a fight with the boss take place.

While playing the game Petya found spell scrolls and now he is about to use them. Let’s describe the way fighting goes on this level:

1) The boss has two parameters: max — the initial amount of health and reg — regeneration rate per second.

2) Every scroll also has two parameters: powi — spell power measured in percents — the maximal amount of health counted off the initial one, which allows to use the scroll (i.e. if the boss has more than powi percent of health the scroll cannot be used); and dmgi the damage per second inflicted upon the boss if the scroll is used. As soon as a scroll is used it disappears and another spell is cast upon the boss that inflicts dmgi of damage per second upon him until the end of the game.

During the battle the actions per second are performed in the following order: first the boss gets the damage from all the spells cast upon him, then he regenerates reg of health (at the same time he can’t have more than max of health), then the player may use another scroll (no more than one per second).

The boss is considered to be defeated if at the end of a second he has nonpositive ( ≤ 0) amount of health.

Help Petya to determine whether he can win with the set of scrolls available to him and if he can, determine the minimal number of seconds he needs to do it.

The first line contains three integers N, max and reg (1 ≤ N, max, reg ≤ 1000) –– the amount of scrolls and the parameters of the boss. The next N lines contain two integers powi and dmgi each — the parameters of the i-th scroll (0 ≤ powi ≤ 100, 1 ≤ dmgi ≤ 2000).

In case Petya can’t complete this level, output in the single line NO.

Otherwise, output on the first line YES. On the second line output the minimal time after which the boss can be defeated and the number of used scrolls. In the next lines for each used scroll output space-separated number of seconds passed from the start of the battle to the moment the scroll was used and the number of the scroll. Scrolls are numbered starting from 1 in the input order. The first scroll is considered to be available to be used after 0 seconds.

Output scrolls in the order they were used. It is not allowed to use scrolls after the boss is defeated.

## Input

The first line contains three integers N, max and reg (1 ≤ N, max, reg ≤ 1000) –– the amount of scrolls and the parameters of the boss. The next N lines contain two integers powi and dmgi each — the parameters of the i-th scroll (0 ≤ powi ≤ 100, 1 ≤ dmgi ≤ 2000).

## Output

In case Petya can’t complete this level, output in the single line NO.

Otherwise, output on the first line YES. On the second line output the minimal time after which the boss can be defeated and the number of used scrolls. In the next lines for each used scroll output space-separated number of seconds passed from the start of the battle to the moment the scroll was used and the number of the scroll. Scrolls are numbered starting from 1 in the input order. The first scroll is considered to be available to be used after 0 seconds.

Output scrolls in the order they were used. It is not allowed to use scrolls after the boss is defeated.

## Samples

```
2 10 3
100 3
99 1

```

```
NO

```

```
2 100 10
100 11
90 9

```

```
YES
19 2
0 1
10 2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-37B |
| Contest | 37 |
| Index | B |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `greedy`、`implementation` |
| 镜像标签 | `greedy`、`implementation`、`*1800` |
| Codeforces 通过次数 | 1081 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/37/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/37/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P37B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

