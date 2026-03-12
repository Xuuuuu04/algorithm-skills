# CF-6B President's Office

## 题面快照

## Description

President of Berland has a very vast office-room, where, apart from him, work his subordinates. Each subordinate, as well as President himself, has his own desk of a unique colour. Each desk is rectangular, and its sides are parallel to the office walls. One day President decided to establish an assembly, of which all his deputies will be members. Unfortunately, he does not remember the exact amount of his deputies, but he remembers that the desk of each his deputy is adjacent to his own desk, that is to say, the two desks (President's and each deputy's) have a common side of a positive length.

The office-room plan can be viewed as a matrix with n rows and m columns. Each cell of this matrix is either empty, or contains a part of a desk. An uppercase Latin letter stands for each desk colour. The «period» character («.») stands for an empty cell.

The first line contains two separated by a space integer numbers n, m (1 ≤ n, m ≤ 100) — the length and the width of the office-room, and c character — the President's desk colour. The following n lines contain m characters each — the office-room description. It is guaranteed that the colour of each desk is unique, and each desk represents a continuous subrectangle of the given matrix. All colours are marked by uppercase Latin letters.

Print the only number — the amount of President's deputies.

## Input

The first line contains two separated by a space integer numbers n, m (1 ≤ n, m ≤ 100) — the length and the width of the office-room, and c character — the President's desk colour. The following n lines contain m characters each — the office-room description. It is guaranteed that the colour of each desk is unique, and each desk represents a continuous subrectangle of the given matrix. All colours are marked by uppercase Latin letters.

## Output

Print the only number — the amount of President's deputies.

## Samples

```
3 4 R
G.B.
.RR.
TTT.

```

```
2

```

```
3 3 Z
...
.H.
..Z

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-6B |
| Contest | 6 |
| Index | B |
| Rating | 1100 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1100` |
| Codeforces 通过次数 | 14657 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/6/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/6/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P6B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

