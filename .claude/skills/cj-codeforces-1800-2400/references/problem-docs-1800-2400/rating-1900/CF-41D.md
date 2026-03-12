# CF-41D Pawn

## 题面快照

## Description

On some square in the lowest row of a chessboard a stands a pawn. It has only two variants of moving: upwards and leftwards or upwards and rightwards. The pawn can choose from which square of the lowest row it can start its journey. On each square lay from 0 to 9 peas. The pawn wants to reach the uppermost row having collected as many peas as possible. As there it will have to divide the peas between itself and its k brothers, the number of peas must be divisible by k + 1. Find the maximal number of peas it will be able to collect and which moves it should make to do it.

The pawn cannot throw peas away or leave the board. When a pawn appears in some square of the board (including the first and last square of the way), it necessarily takes all the peas.

The first line contains three integers n, m, k (2 ≤ n, m ≤ 100, 0 ≤ k ≤ 10) — the number of rows and columns on the chessboard, the number of the pawn's brothers. Then follow n lines containing each m numbers from 0 to 9 without spaces — the chessboard's description. Each square is described by one number — the number of peas in it. The first line corresponds to the uppermost row and the last line — to the lowest row.

If it is impossible to reach the highest row having collected the number of peas divisible by k + 1, print -1.

Otherwise, the first line must contain a single number — the maximal number of peas the pawn can collect given that the number must be divisible by k + 1. The second line must contain a single number — the number of the square's column in the lowest row, from which the pawn must start its journey. The columns are numbered from the left to the right with integral numbers starting from 1. The third line must contain a line consisting of n - 1 symbols — the description of the pawn's moves. If the pawn must move upwards and leftwards, print L, if it must move upwards and rightwards, print R. If there are several solutions to that problem, print any of them.

## Input

The first line contains three integers n, m, k (2 ≤ n, m ≤ 100, 0 ≤ k ≤ 10) — the number of rows and columns on the chessboard, the number of the pawn's brothers. Then follow n lines containing each m numbers from 0 to 9 without spaces — the chessboard's description. Each square is described by one number — the number of peas in it. The first line corresponds to the uppermost row and the last line — to the lowest row.

## Output

If it is impossible to reach the highest row having collected the number of peas divisible by k + 1, print -1.

Otherwise, the first line must contain a single number — the maximal number of peas the pawn can collect given that the number must be divisible by k + 1. The second line must contain a single number — the number of the square's column in the lowest row, from which the pawn must start its journey. The columns are numbered from the left to the right with integral numbers starting from 1. The third line must contain a line consisting of n - 1 symbols — the description of the pawn's moves. If the pawn must move upwards and leftwards, print L, if it must move upwards and rightwards, print R. If there are several solutions to that problem, print any of them.

## Samples

```
3 3 1
123
456
789

```

```
16
2
RL

```

```
3 3 0
123
456
789

```

```
17
3
LR

```

```
2 2 10
98
75

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-41D |
| Contest | 41 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*1900` |
| Codeforces 通过次数 | 2873 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/41/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/41/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P41D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

