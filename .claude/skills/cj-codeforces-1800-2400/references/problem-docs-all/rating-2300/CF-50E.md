# CF-50E Square Equation Roots

## 题面快照

## Description

A schoolboy Petya studies square equations. The equations that are included in the school curriculum, usually look simple:
x2 + 2bx + c = 0 where b, c are natural numbers.
Petya noticed that some equations have two real roots, some of them have only one root and some equations don't have real roots at all. Moreover it turned out that several different square equations can have a common root.

Petya is interested in how many different real roots have all the equations of the type described above for all the possible pairs of numbers b and c such that 1 ≤ b ≤ n, 1 ≤ c ≤ m. Help Petya find that number.

The single line contains two integers n and m. (1 ≤ n, m ≤ 5000000).

Print a single number which is the number of real roots of the described set of equations.

## Input

The single line contains two integers n and m. (1 ≤ n, m ≤ 5000000).

## Output

Print a single number which is the number of real roots of the described set of equations.

## Samples

```
3 3

```

```
12

```

```
1 2

```

```
1

```

## Note

In the second test from the statement the following equations are analysed:

b = 1, c = 1: x2 + 2x + 1 = 0; The root is x = - 1

b = 1, c = 2: x2 + 2x + 2 = 0; No roots

Overall there's one root

In the second test the following equations are analysed:

b = 1, c = 1: x2 + 2x + 1 = 0; The root is x = - 1

b = 1, c = 2: x2 + 2x + 2 = 0; No roots

b = 1, c = 3: x2 + 2x + 3 = 0; No roots

b = 2, c = 1: x2 + 4x + 1 = 0; The roots are

b = 2, c = 2: x2 + 4x + 2 = 0; The roots are

b = 2, c = 3: x2 + 4x + 3 = 0; The roots are x1 = - 3, x2 = - 1

b = 3, c = 1: x2 + 6x + 1 = 0; The roots are

b = 3, c = 2: x2 + 6x + 2 = 0; The roots are

b = 3, c = 3: x2 + 6x + 3 = 0; The roots are  Overall there are 13 roots and as the root  - 1 is repeated twice, that means there are 12 different roots.

-  登录后递交

-

-  讨论 (0)

-  题解 (0)

-  文件

-  统计

-

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-50E |
| Contest | 50 |
| Index | E |
| Rating | 2300 |
| Points | 2500.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*2300` |
| Codeforces 通过次数 | 423 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/50/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/50/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P50E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

