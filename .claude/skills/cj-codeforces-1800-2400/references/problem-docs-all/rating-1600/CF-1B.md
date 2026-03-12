# CF-1B Spreadsheet

## 题面快照

## Description

In the popular spreadsheets systems (for example, in Excel) the following numeration of columns is used. The first column has number A, the second — number B, etc. till column 26 that is marked by Z. Then there are two-letter numbers: column 27 has number AA, 28 — AB, column 52 is marked by AZ. After ZZ there follow three-letter numbers, etc.

The rows are marked by integer numbers starting with 1. The cell name is the concatenation of the column and the row numbers. For example, BC23 is the name for the cell that is in column 55, row 23.

Sometimes another numeration system is used: RXCY, where X and Y are integer numbers, showing the column and the row numbers respectfully. For instance, R23C55 is the cell from the previous example.

Your task is to write a program that reads the given sequence of cell coordinates and produce each item written according to the rules of another numeration system.

The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .

Write n lines, each line should contain a cell coordinates in the other numeration system.

## Input

The first line of the input contains integer number n (1 ≤ n ≤ 105), the number of coordinates in the test. Then there follow n lines, each of them contains coordinates. All the coordinates are correct, there are no cells with the column and/or the row numbers larger than 106 .

## Output

Write n lines, each line should contain a cell coordinates in the other numeration system.

## Samples

```
2
R23C55
BC23

```

```
BC23
R23C55

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-1B |
| Contest | 1 |
| Index | B |
| Rating | 1600 |
| Points | - |
| Codeforces 标签 | `implementation`、`math` |
| 镜像标签 | `implementation`、`math`、`*1600` |
| Codeforces 通过次数 | 25952 |
| 镜像尝试 / 通过 | 45 / 13 |
| 时限 | 10000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/1/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/1/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P1B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

