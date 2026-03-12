# CF-95D Horse Races

## 题面快照

## Description

Petya likes horse racing very much. Horses numbered from l to r take part in the races. Petya wants to evaluate the probability of victory; for some reason, to do that he needs to know the amount of nearly lucky horses' numbers. A nearly lucky number is an integer number that has at least two lucky digits the distance between which does not exceed k. Petya learned from some of his mates from Lviv that lucky digits are digits 4 and 7. The distance between the digits is the absolute difference between their positions in the number of a horse. For example, if k = 2, then numbers 412395497, 404, 4070400000070004007 are nearly lucky and numbers 4, 4123954997, 4007000040070004007 are not.

Petya prepared t intervals [li, ri] and invented number k, common for all of them. Your task is to find how many nearly happy numbers there are in each of these segments. Since the answers can be quite large, output them modulo 1000000007 (109 + 7).

The first line contains two integers t and k (1 ≤ t, k ≤ 1000) — the number of segments and the distance between the numbers correspondingly. Next t lines contain pairs of integers li and ri (1 ≤ l ≤ r ≤ 101000). All numbers are given without the leading zeroes. Numbers in each line are separated by exactly one space character.

Output t lines. In each line print one integer — the answer for the corresponding segment modulo 1000000007 (109 + 7).

## Input

The first line contains two integers t and k (1 ≤ t, k ≤ 1000) — the number of segments and the distance between the numbers correspondingly. Next t lines contain pairs of integers li and ri (1 ≤ l ≤ r ≤ 101000). All numbers are given without the leading zeroes. Numbers in each line are separated by exactly one space character.

## Output

Output t lines. In each line print one integer — the answer for the corresponding segment modulo 1000000007 (109 + 7).

## Samples

```
1 2
1 100

```

```
4

```

```
1 2
70 77

```

```
2

```

```
2 1
1 20
80 100

```

```
0
0

```

## Note

In the first sample, the four nearly lucky numbers are 44, 47, 74, 77.

In the second sample, only 74 and 77 are in the given segment.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-95D |
| Contest | 95 |
| Index | D |
| Rating | 2500 |
| Points | 2000.0 |
| Codeforces 标签 | `dp`、`math` |
| 镜像标签 | `dp`、`math`、`*2500` |
| Codeforces 通过次数 | 491 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/95/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/95/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P95D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

