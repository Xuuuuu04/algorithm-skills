# CF-67B Restoration of the Permutation

## 题面快照

## Description

Let A = {a1, a2, ..., an} be any permutation of the first n natural numbers {1, 2, ..., n}. You are given a positive integer k and another sequence B = {b1, b2, ..., bn}, where bi is the number of elements aj in A to the left of the element at = i such that aj ≥ (i + k).

For example, if n = 5, a possible A is {5, 1, 4, 2, 3}. For k = 2, B is given by {1, 2, 1, 0, 0}. But if k = 3, then B = {1, 1, 0, 0, 0}.

For two sequences X = {x1, x2, ..., xn} and Y = {y1, y2, ..., yn}, let i-th elements be the first elements such that xi ≠ yi. If xi < yi, then X is lexicographically smaller than Y, while if xi > yi, then X is lexicographically greater than Y.

Given n, k and B, you need to determine the lexicographically smallest A.

The first line contains two space separated integers n and k (1 ≤ n ≤ 1000, 1 ≤ k ≤ n). On the second line are n integers specifying the values of B = {b1, b2, ..., bn}.

Print on a single line n integers of A = {a1, a2, ..., an} such that A is lexicographically minimal. It is guaranteed that the solution exists.

## Input

The first line contains two space separated integers n and k (1 ≤ n ≤ 1000, 1 ≤ k ≤ n). On the second line are n integers specifying the values of B = {b1, b2, ..., bn}.

## Output

Print on a single line n integers of A = {a1, a2, ..., an} such that A is lexicographically minimal. It is guaranteed that the solution exists.

## Samples

```
5 2
1 2 1 0 0

```

```
4 1 5 2 3

```

```
4 2
1 0 0 0

```

```
2 3 1 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-67B |
| Contest | 67 |
| Index | B |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `greedy` |
| 镜像标签 | `greedy`、`*1800` |
| Codeforces 通过次数 | 929 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/67/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/67/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P67B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

