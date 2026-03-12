# CF-67A Partial Teacher

## 题面快照

## Description

A teacher decides to give toffees to his students. He asks n students to stand in a queue. Since the teacher is very partial, he follows the following rule to distribute toffees.

He looks at the first two students and gives more toffees to the student having higher marks than the other one. If they have the same marks they get the same number of toffees. The same procedure is followed for each pair of adjacent students starting from the first one to the last one.

It is given that each student receives at least one toffee. You have to find the number of toffees given to each student by the teacher such that the total number of toffees is minimum.

The first line of input contains the number of students n (2 ≤ n ≤ 1000). The second line gives (n - 1) characters consisting of "L", "R" and "=". For each pair of adjacent students "L" means that the left student has higher marks, "R" means that the right student has higher marks and "=" means that both have equal marks.

Output consists of n integers separated by a space representing the number of toffees each student receives in the queue starting from the first one to the last one.

## Input

The first line of input contains the number of students n (2 ≤ n ≤ 1000). The second line gives (n - 1) characters consisting of "L", "R" and "=". For each pair of adjacent students "L" means that the left student has higher marks, "R" means that the right student has higher marks and "=" means that both have equal marks.

## Output

Output consists of n integers separated by a space representing the number of toffees each student receives in the queue starting from the first one to the last one.

## Samples

```
5
LRLR

```

```
2 1 2 1 2

```

```
5
=RRR

```

```
1 1 2 3 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-67A |
| Contest | 67 |
| Index | A |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `dp`、`graphs`、`greedy`、`implementation` |
| 镜像标签 | `dp`、`graphs`、`greedy`、`implementation`、`*1800` |
| Codeforces 通过次数 | 2396 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/67/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/67/problem/A)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P67A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

