# CF-47C Crossword

## 题面快照

## Description

Vasya trains to compose crossword puzzles. He can only compose crosswords of a very simplе type so far. All of them consist of exactly six words; the words can be read only from top to bottom vertically and from the left to the right horizontally. The words are arranged in the form of a rectangular "eight" or infinity sign, not necessarily symmetrical.

The top-left corner of the crossword coincides with the top-left corner of the rectangle. The same thing is correct for the right-bottom corners. The crossword can't degrade, i.e. it always has exactly four blank areas, two of which are surrounded by letters. Look into the output for the samples for clarification.

Help Vasya — compose a crossword of the described type using the given six words. It is allowed to use the words in any order.

Six lines contain the given words. Every word consists of no more than 30 and no less than 3 uppercase Latin letters.

If it is impossible to solve the problem, print Impossible. Otherwise, print the sought crossword. All the empty squares should be marked as dots.

If there can be several solutions to that problem, print the lexicographically minimum one. I.e. the solution where the first line is less than the first line of other solutions should be printed. If the two lines are equal, compare the second lines and so on. The lexicographical comparison of lines is realized by the < operator in the modern programming languages.

## Input

Six lines contain the given words. Every word consists of no more than 30 and no less than 3 uppercase Latin letters.

## Output

If it is impossible to solve the problem, print Impossible. Otherwise, print the sought crossword. All the empty squares should be marked as dots.

If there can be several solutions to that problem, print the lexicographically minimum one. I.e. the solution where the first line is less than the first line of other solutions should be printed. If the two lines are equal, compare the second lines and so on. The lexicographical comparison of lines is realized by the < operator in the modern programming languages.

## Samples

```
NOD
BAA
YARD
AIRWAY
NEWTON
BURN

```

```
BAA...
U.I...
R.R...
NEWTON
..A..O
..YARD

```

```
AAA
AAA
AAAAA
AAA
AAA
AAAAA

```

```
AAA..
A.A..
AAAAA
..A.A
..AAA

```

```
PTC
JYNYFDSGI
ZGPPC
IXEJNDOP
JJFS
SSXXQOFGJUZ

```

```
JJFS....
Y..S....
N..X....
Y..X....
F..Q....
D..O....
S..F....
G..G....
IXEJNDOP
...U...T
...ZGPPC

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-47C |
| Contest | 47 |
| Index | C |
| Rating | 2000 |
| Points | 1500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*2000` |
| Codeforces 通过次数 | 856 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/47/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/47/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P47C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

