# CF-15C Industrial Nim

## 题面快照

## Description

There are n stone quarries in Petrograd.

Each quarry owns mi dumpers (1 ≤ i ≤ n). It is known that the first dumper of the i-th quarry has xi stones in it, the second dumper has xi + 1 stones in it, the third has xi + 2, and the mi-th dumper (the last for the i-th quarry) has xi + mi - 1 stones in it.

Two oligarchs play a well-known game Nim. Players take turns removing stones from dumpers. On each turn, a player can select any dumper and remove any non-zero amount of stones from it. The player who cannot take a stone loses.

Your task is to find out which oligarch will win, provided that both of them play optimally. The oligarchs asked you not to reveal their names. So, let's call the one who takes the first stone «tolik» and the other one «bolik».

The first line of the input contains one integer number n (1 ≤ n ≤ 105) — the amount of quarries. Then there follow n lines, each of them contains two space-separated integers xi and mi (1 ≤ xi, mi ≤ 1016) — the amount of stones in the first dumper of the i-th quarry and the number of dumpers at the i-th quarry.

Output «tolik» if the oligarch who takes a stone first wins, and «bolik» otherwise.

## Input

The first line of the input contains one integer number n (1 ≤ n ≤ 105) — the amount of quarries. Then there follow n lines, each of them contains two space-separated integers xi and mi (1 ≤ xi, mi ≤ 1016) — the amount of stones in the first dumper of the i-th quarry and the number of dumpers at the i-th quarry.

## Output

Output «tolik» if the oligarch who takes a stone first wins, and «bolik» otherwise.

## Samples

```
2
2 1
3 2

```

```
tolik

```

```
4
1 1
1 1
1 1
1 1

```

```
bolik

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-15C |
| Contest | 15 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `games` |
| 镜像标签 | `games`、`*2000` |
| Codeforces 通过次数 | 2793 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/15/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/15/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P15C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

