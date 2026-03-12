# CF-2B The least round way

## 题面快照

## Description

There is a square matrix n × n, consisting of non-negative integer numbers. You should find such a way on it that

-  starts in the upper left cell of the matrix;

-  each following cell is to the right or down from the current cell;

-  the way ends in the bottom right cell.

Moreover, if we multiply together all the numbers along the way, the result should be the least "round". In other words, it should end in the least possible number of zeros.

The first line contains an integer number n (2 ≤ n ≤ 1000), n is the size of the matrix. Then follow n lines containing the matrix elements (non-negative integer numbers not exceeding 109).

In the first line print the least number of trailing zeros. In the second line print the correspondent way itself.

## Input

The first line contains an integer number n (2 ≤ n ≤ 1000), n is the size of the matrix. Then follow n lines containing the matrix elements (non-negative integer numbers not exceeding 109).

## Output

In the first line print the least number of trailing zeros. In the second line print the correspondent way itself.

## Samples

```
3
1 2 3
4 5 6
7 8 9

```

```
0
DDRR

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-2B |
| Contest | 2 |
| Index | B |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dp`、`math` |
| 镜像标签 | `dp`、`math`、`*2000` |
| Codeforces 通过次数 | 12750 |
| 镜像尝试 / 通过 | 13 / 5 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/2/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/2/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P2B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

