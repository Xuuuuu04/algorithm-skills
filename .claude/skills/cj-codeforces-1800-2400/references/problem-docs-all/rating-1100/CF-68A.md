# CF-68A Irrational problem

## 题面快照

## Description

Little Petya was given this problem for homework:

You are given function  (here  represents the operation of taking the remainder). His task is to count the number of integers x in range [a;b] with property f(x) = x.

It is a pity that Petya forgot the order in which the remainders should be taken and wrote down only 4 numbers. Each of 24 possible orders of taking the remainder has equal probability of being chosen. For example, if Petya has numbers 1, 2, 3, 4 then he can take remainders in that order or first take remainder modulo 4, then modulo 2, 3, 1. There also are 22 other permutations of these numbers that represent orders in which remainder can be taken. In this problem 4 numbers wrote down by Petya will be pairwise distinct.

Now it is impossible for Petya to complete the task given by teacher but just for fun he decided to find the number of integers  with property that probability that f(x) = x is not less than 31.4159265352718281828459045%. In other words, Petya will pick up the number x if there exist at least 7 permutations of numbers p1, p2, p3, p4, for which f(x) = x.

First line of the input will contain 6 integers, separated by spaces: p1, p2, p3, p4, a, b (1 ≤ p1, p2, p3, p4 ≤ 1000, 0 ≤ a ≤ b ≤ 31415).

It is guaranteed that numbers p1, p2, p3, p4 will be pairwise distinct.

Output the number of integers in the given range that have the given property.

## Input

First line of the input will contain 6 integers, separated by spaces: p1, p2, p3, p4, a, b (1 ≤ p1, p2, p3, p4 ≤ 1000, 0 ≤ a ≤ b ≤ 31415).

It is guaranteed that numbers p1, p2, p3, p4 will be pairwise distinct.

## Output

Output the number of integers in the given range that have the given property.

## Samples

```
2 7 1 8 2 8

```

```
0

```

```
20 30 40 50 0 100

```

```
20

```

```
31 41 59 26 17 43

```

```
9

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-68A |
| Contest | 68 |
| Index | A |
| Rating | 1100 |
| Points | 500.0 |
| Codeforces 标签 | `implementation`、`number theory` |
| 镜像标签 | `implementation`、`number theory`、`*1100` |
| Codeforces 通过次数 | 5308 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/68/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/68/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P68A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

