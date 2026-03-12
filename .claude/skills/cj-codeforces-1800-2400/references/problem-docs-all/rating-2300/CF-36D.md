# CF-36D New Game with a Chess Piece

## 题面快照

## Description

Petya and Vasya are inventing a new game that requires a rectangular board and one chess piece. At the beginning of the game the piece stands in the upper-left corner of the board. Two players move the piece in turns. Each turn the chess piece can be moved either one square to the right or one square down or jump k squares diagonally down and to the right. The player who can’t move the piece loses.

The guys haven’t yet thought what to call the game or the best size of the board for it. Your task is to write a program that can determine the outcome of the game depending on the board size.

The first input line contains two integers t and k (1 ≤ t ≤ 20, 1 ≤ k ≤ 109). Each of the following t lines contains two numbers n, m — the board’s length and width (1 ≤ n, m ≤ 109).

Output t lines that can determine the outcomes of the game on every board. Write «+» if the first player is a winner, and «-» otherwise.

## Input

The first input line contains two integers t and k (1 ≤ t ≤ 20, 1 ≤ k ≤ 109). Each of the following t lines contains two numbers n, m — the board’s length and width (1 ≤ n, m ≤ 109).

## Output

Output t lines that can determine the outcomes of the game on every board. Write «+» if the first player is a winner, and «-» otherwise.

## Samples

```
10 2
1 1
1 2
2 1
2 2
1 3
2 3
3 1
3 2
3 3
4 3

```

```
-
+
+
-
-
+
-
+
+
+

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-36D |
| Contest | 36 |
| Index | D |
| Rating | 2300 |
| Points | 2000.0 |
| Codeforces 标签 | `games` |
| 镜像标签 | `games`、`*2300` |
| Codeforces 通过次数 | 764 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/36/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/36/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P36D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

