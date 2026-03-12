# CF-55C Pie or die

## 题面快照

## Description

Volodya and Vlad play the following game. There are k pies at the cells of n × m board. Each turn Volodya moves one pie to the neighbouring (by side) cell. If the pie lies at the border of the board then Volodya can move it outside the board, get the pie and win. After Volodya's move, Vlad bans some edge at the border of the board of length 1 (between two knots of the board) so that Volodya is not able to move the pie outside the board through this edge anymore. The question is: will Volodya win this game? We suppose both players follow the optimal strategy.

First line contains 3 integers, separated by space: 1 ≤ n, m ≤ 100 — dimensions of the board and 0 ≤ k ≤ 100 — the number of pies. Each of the next k lines contains 2 integers, separated by space: 1 ≤ x ≤ n, 1 ≤ y ≤ m — coordinates of the corresponding pie. There could be more than one pie at a cell.

Output only one word: "YES" — if Volodya wins, "NO" — otherwise.

## Input

First line contains 3 integers, separated by space: 1 ≤ n, m ≤ 100 — dimensions of the board and 0 ≤ k ≤ 100 — the number of pies. Each of the next k lines contains 2 integers, separated by space: 1 ≤ x ≤ n, 1 ≤ y ≤ m — coordinates of the corresponding pie. There could be more than one pie at a cell.

## Output

Output only one word: "YES" — if Volodya wins, "NO" — otherwise.

## Samples

```
2 2 1
1 2

```

```
YES

```

```
3 4 0

```

```
NO

```

```
100 50 2
50 25
50 25

```

```
NO

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-55C |
| Contest | 55 |
| Index | C |
| Rating | 1900 |
| Points | 1500.0 |
| Codeforces 标签 | `games` |
| 镜像标签 | `games`、`*1900` |
| Codeforces 通过次数 | 1801 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/55/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/55/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P55C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

