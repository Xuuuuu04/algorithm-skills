# CF-10C Digital Root

## 题面快照

## Description

Not long ago Billy came across such a problem, where there were given three natural numbers A, B and C from the range [1, N], and it was asked to check whether the equation AB = C is correct. Recently Billy studied the concept of a digital root of a number. We should remind you that a digital root d(x) of the number x is the sum s(x) of all the digits of this number, if s(x) ≤ 9, otherwise it is d(s(x)). For example, a digital root of the number 6543 is calculated as follows: d(6543) = d(6 + 5 + 4 + 3) = d(18) = 9. Billy has counted that the digital root of a product of numbers is equal to the digital root of the product of the factors' digital roots, i.e. d(xy) = d(d(x)d(y)). And the following solution to the problem came to his mind: to calculate the digital roots and check if this condition is met. However, Billy has doubts that this condition is sufficient. That's why he asks you to find out the amount of test examples for the given problem such that the algorithm proposed by Billy makes mistakes.

The first line contains the only number N (1 ≤ N ≤ 106).

Output one number — the amount of required A, B and C from the range [1, N].

## Input

The first line contains the only number N (1 ≤ N ≤ 106).

## Output

Output one number — the amount of required A, B and C from the range [1, N].

## Samples

```
4

```

```
2

```

```
5

```

```
6

```

## Note

For the first sample the required triples are (3, 4, 3) and (4, 3, 3).

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-10C |
| Contest | 10 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `number theory` |
| 镜像标签 | `number theory`、`*2000` |
| Codeforces 通过次数 | 1669 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/10/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/10/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P10C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

