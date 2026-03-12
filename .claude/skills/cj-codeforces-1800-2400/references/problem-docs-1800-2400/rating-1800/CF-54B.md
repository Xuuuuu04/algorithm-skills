# CF-54B Cutting Jigsaw Puzzle

## 题面快照

## Description

The Hedgehog recently remembered one of his favorite childhood activities, — solving puzzles, and got into it with new vigor. He would sit day in, day out with his friend buried into thousands of tiny pieces of the picture, looking for the required items one by one.

Soon the Hedgehog came up with a brilliant idea: instead of buying ready-made puzzles, one can take his own large piece of paper with some picture and cut it into many small rectangular pieces, then mix them and solve the resulting puzzle, trying to piece together the picture. The resulting task is even more challenging than the classic puzzle: now all the fragments have the same rectangular shape, and one can assemble the puzzle only relying on the picture drawn on the pieces.

All puzzle pieces turn out to be of the same size X × Y, because the picture is cut first by horizontal cuts with the pitch of X, then with vertical cuts with the pitch of Y. If we denote the initial size of the picture as A × B, then A must be divisible by X and B must be divisible by Y (X and Y are integer numbers).

However, not every such cutting of the picture will result in a good puzzle. The Hedgehog finds a puzzle good if no two pieces in it are the same (It is allowed to rotate the pieces when comparing them, but it is forbidden to turn them over).

Your task is to count for a given picture the number of good puzzles that you can make from it, and also to find the puzzle with the minimal piece size.

The first line contains two numbers A and B which are the sizes of the picture. They are positive integers not exceeding 20.

Then follow A lines containing B symbols each, describing the actual picture. The lines only contain uppercase English letters.

In the first line print the number of possible good puzzles (in other words, the number of pairs (X, Y) such that the puzzle with the corresponding element sizes will be good). This number should always be positive, because the whole picture is a good puzzle itself.

In the second line print two numbers — the sizes X and Y of the smallest possible element among all good puzzles. The comparison is made firstly by the area XY of one element and secondly — by the length X.

## Input

The first line contains two numbers A and B which are the sizes of the picture. They are positive integers not exceeding 20.

Then follow A lines containing B symbols each, describing the actual picture. The lines only contain uppercase English letters.

## Output

In the first line print the number of possible good puzzles (in other words, the number of pairs (X, Y) such that the puzzle with the corresponding element sizes will be good). This number should always be positive, because the whole picture is a good puzzle itself.

In the second line print two numbers — the sizes X and Y of the smallest possible element among all good puzzles. The comparison is made firstly by the area XY of one element and secondly — by the length X.

## Samples

```
2 4
ABDC
ABDC

```

```
3
2 1

```

```
2 6
ABCCBA
ABCCBA

```

```
1
2 6

```

## Note

The picture in the first sample test has the following good puzzles: (2, 1), (2, 2), (2, 4).

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-54B |
| Contest | 54 |
| Index | B |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `hashing`、`implementation` |
| 镜像标签 | `hashing`、`implementation`、`*1800` |
| Codeforces 通过次数 | 870 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/54/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/54/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P54B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

