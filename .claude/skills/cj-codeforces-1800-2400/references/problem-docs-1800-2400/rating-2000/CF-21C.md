# CF-21C Stripe 2

## 题面快照

## Description

Once Bob took a paper stripe of n squares (the height of the stripe is 1 square). In each square he wrote an integer number, possibly negative. He became interested in how many ways exist to cut this stripe into three pieces so that the sum of numbers from each piece is equal to the sum of numbers from any other piece, and each piece contains positive integer amount of squares. Would you help Bob solve this problem?

The first input line contains integer n (1 ≤ n ≤ 105) — amount of squares in the stripe. The second line contains n space-separated numbers — they are the numbers written in the squares of the stripe. These numbers are integer and do not exceed 10000 in absolute value.

Output the amount of ways to cut the stripe into three non-empty pieces so that the sum of numbers from each piece is equal to the sum of numbers from any other piece. Don't forget that it's allowed to cut the stripe along the squares' borders only.

## Input

The first input line contains integer n (1 ≤ n ≤ 105) — amount of squares in the stripe. The second line contains n space-separated numbers — they are the numbers written in the squares of the stripe. These numbers are integer and do not exceed 10000 in absolute value.

## Output

Output the amount of ways to cut the stripe into three non-empty pieces so that the sum of numbers from each piece is equal to the sum of numbers from any other piece. Don't forget that it's allowed to cut the stripe along the squares' borders only.

## Samples

```
4
1 2 3 3

```

```
1

```

```
5
1 2 3 4 5

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-21C |
| Contest | 21 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `binary search`、`dp`、`sortings` |
| 镜像标签 | `binary search`、`dp`、`sortings`、`*2000` |
| Codeforces 通过次数 | 2490 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/21/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/21/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P21C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

