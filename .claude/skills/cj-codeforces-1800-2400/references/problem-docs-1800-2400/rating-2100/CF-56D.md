# CF-56D Changing a String

## 题面快照

## Description

There is a string s, consisting of capital Latin letters. Let's denote its current length as |s|. During one move it is allowed to apply one of the following operations to it:

- INSERTposch — insert a letter ch in the string s in the position pos (1 ≤ pos ≤ |s| + 1, A ≤ ch ≤ Z). The letter ch becomes the pos-th symbol of the string s, at that the letters shift aside and the length of the string increases by 1.

- DELETEpos — delete a character number pos (1 ≤ pos ≤ |s|) from the string s. At that the letters shift together and the length of the string decreases by 1.

- REPLACEposch — the letter in the position pos of the line s is replaced by ch (1 ≤ pos ≤ |s|, A ≤ ch ≤ Z). At that the length of the string does not change.

Your task is to find in which minimal number of moves one can get a t string from an s string. You should also find the sequence of actions leading to the required results.

The first line contains s, the second line contains t. The lines consist only of capital Latin letters, their lengths are positive numbers from 1 to 1000.

In the first line print the number of moves k in the given sequence of operations. The number should be the minimal possible one. Then print k lines containing one operation each. Print the operations in the format, described above. If there are several solutions, print any of them.

## Input

The first line contains s, the second line contains t. The lines consist only of capital Latin letters, their lengths are positive numbers from 1 to 1000.

## Output

In the first line print the number of moves k in the given sequence of operations. The number should be the minimal possible one. Then print k lines containing one operation each. Print the operations in the format, described above. If there are several solutions, print any of them.

## Samples

```
ABA
ABBBA

```

```
2
INSERT 3 B
INSERT 4 B

```

```
ACCEPTED
WRONGANSWER

```

```
10
REPLACE 1 W
REPLACE 2 R
REPLACE 3 O
REPLACE 4 N
REPLACE 5 G
REPLACE 6 A
INSERT 7 N
INSERT 8 S
INSERT 9 W
REPLACE 11 R

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-56D |
| Contest | 56 |
| Index | D |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*2100` |
| Codeforces 通过次数 | 2049 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/56/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/56/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P56D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

