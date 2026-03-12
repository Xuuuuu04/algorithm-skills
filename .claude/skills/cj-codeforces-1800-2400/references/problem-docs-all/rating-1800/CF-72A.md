# CF-72A Goshtasp, Vishtasp and Eidi

## 题面快照

## Description

Goshtasp was known to be a good programmer in his school. One day Vishtasp, Goshtasp's friend, asked him to solve this task:

Given a positive integer n, you should determine whether n is rich.

The positive integer x is rich, if there exists some set of distinct numbers a1, a2, ..., am such that . In addition: every ai should be either a prime number, or equal to 1.

Vishtasp said that he would share his Eidi 50 / 50 with Goshtasp, if he could solve the task. Eidi is money given to children for Noruz by their parents and/or relatives.

Goshtasp needs to solve this problem to get money, you need to solve it to get score!

Input contains a single positive integer n (1 ≤ n ≤ 10000).

If the number is not rich print 0. Otherwise print the numbers a1, ..., am. If several solutions exist print the lexicographically latest solution. Answers are compared as sequences of numbers, not as strings.

For comparing two sequences a1, ..., am and b1, ..., bn we first find the first index i such that ai ≠ bi, if ai < bi then a is lexicographically earlier and if bi < ai then b is lexicographically earlier. If m ≠ n we add zeroes at the end of the smaller sequence (only for the moment of comparison) and then perform the comparison.

You do not need to minimize the number of elements in sequence (i.e. m). You just need to print the lexicographically latest solution.

See samples to find out how to print the sequence.

## Input

Input contains a single positive integer n (1 ≤ n ≤ 10000).

## Output

If the number is not rich print 0. Otherwise print the numbers a1, ..., am. If several solutions exist print the lexicographically latest solution. Answers are compared as sequences of numbers, not as strings.

For comparing two sequences a1, ..., am and b1, ..., bn we first find the first index i such that ai ≠ bi, if ai < bi then a is lexicographically earlier and if bi < ai then b is lexicographically earlier. If m ≠ n we add zeroes at the end of the smaller sequence (only for the moment of comparison) and then perform the comparison.

You do not need to minimize the number of elements in sequence (i.e. m). You just need to print the lexicographically latest solution.

See samples to find out how to print the sequence.

## Samples

```
11

```

```
11=11

```

```
545

```

```
541+3+1=545

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-72A |
| Contest | 72 |
| Index | A |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `*special`、`greedy`、`math` |
| 镜像标签 | `*special problem`、`greedy`、`math`、`*1800` |
| Codeforces 通过次数 | 193 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/72/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/72/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P72A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

