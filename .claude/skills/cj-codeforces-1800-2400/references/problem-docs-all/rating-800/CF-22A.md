# CF-22A Second Order Statistics

## 题面快照

## Description

Once Bob needed to find the second order statistics of a sequence of integer numbers. Lets choose each number from the sequence exactly once and sort them. The value on the second position is the second order statistics of the given sequence. In other words it is the smallest element strictly greater than the minimum. Help Bob solve this problem.

The first input line contains integer n (1 ≤ n ≤ 100) — amount of numbers in the sequence. The second line contains n space-separated integer numbers — elements of the sequence. These numbers don't exceed 100 in absolute value.

If the given sequence has the second order statistics, output this order statistics, otherwise output NO.

## Input

The first input line contains integer n (1 ≤ n ≤ 100) — amount of numbers in the sequence. The second line contains n space-separated integer numbers — elements of the sequence. These numbers don't exceed 100 in absolute value.

## Output

If the given sequence has the second order statistics, output this order statistics, otherwise output NO.

## Samples

```
4
1 2 2 -4

```

```
1

```

```
5
1 2 3 1 1

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-22A |
| Contest | 22 |
| Index | A |
| Rating | 800 |
| Points | - |
| Codeforces 标签 | `brute force` |
| 镜像标签 | `brute force`、`*800` |
| Codeforces 通过次数 | 26545 |
| 镜像尝试 / 通过 | 6 / 5 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/22/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/22/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P22A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

