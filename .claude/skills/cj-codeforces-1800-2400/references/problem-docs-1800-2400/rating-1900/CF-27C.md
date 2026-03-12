# CF-27C Unordered Subsequence

## 题面快照

## Description

The sequence is called ordered if it is non-decreasing or non-increasing. For example, sequnces [3, 1, 1, 0] and [1, 2, 3, 100] are ordered, but the sequence [1, 3, 3, 1] is not. You are given a sequence of numbers. You are to find it's shortest subsequence which is not ordered.

A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

The first line of the input contains one integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers — the given sequence. All numbers in this sequence do not exceed 106 by absolute value.

If the given sequence does not contain any unordered subsequences, output 0. Otherwise, output the length k of the shortest such subsequence. Then output k integers from the range [1..n] — indexes of the elements of this subsequence. If there are several solutions, output any of them.

## Input

The first line of the input contains one integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers — the given sequence. All numbers in this sequence do not exceed 106 by absolute value.

## Output

If the given sequence does not contain any unordered subsequences, output 0. Otherwise, output the length k of the shortest such subsequence. Then output k integers from the range [1..n] — indexes of the elements of this subsequence. If there are several solutions, output any of them.

## Samples

```
5
67 499 600 42 23

```

```
3
1 3 5

```

```
3
1 2 3

```

```
0

```

```
3
2 3 1

```

```
3
1 2 3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-27C |
| Contest | 27 |
| Index | C |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`greedy` |
| 镜像标签 | `constructive algorithms`、`greedy`、`*1900` |
| Codeforces 通过次数 | 3032 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/27/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/27/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P27C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

