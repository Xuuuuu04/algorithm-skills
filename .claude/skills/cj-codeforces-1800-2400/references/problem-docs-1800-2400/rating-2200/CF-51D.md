# CF-51D Geometrical problem

## 题面快照

## Description

Polycarp loves geometric progressions — he collects them. However, as such progressions occur very rarely, he also loves the sequences of numbers where it is enough to delete a single element to get a geometric progression.

In this task we shall define geometric progressions as finite sequences of numbers a1, a2, ..., ak, where ai = c·bi - 1 for some real numbers c and b. For example, the sequences [2, -4, 8], [0, 0, 0, 0], [199] are geometric progressions and [0, 1, 2, 3] is not.

Recently Polycarp has found a sequence and he can't classify it. Help him to do it. Determine whether it is a geometric progression. If it is not, check if it can become a geometric progression if an element is deleted from it.

The first line contains an integer n (1 ≤ n ≤ 105) — the number of elements in the given sequence. The second line contains the given sequence. The numbers are space-separated. All the elements of the given sequence are integers and their absolute value does not exceed 104.

Print 0, if the given sequence is a geometric progression. Otherwise, check if it is possible to make the sequence a geometric progression by deleting a single element. If it is possible, print 1. If it is impossible, print 2.

## Input

The first line contains an integer n (1 ≤ n ≤ 105) — the number of elements in the given sequence. The second line contains the given sequence. The numbers are space-separated. All the elements of the given sequence are integers and their absolute value does not exceed 104.

## Output

Print 0, if the given sequence is a geometric progression. Otherwise, check if it is possible to make the sequence a geometric progression by deleting a single element. If it is possible, print 1. If it is impossible, print 2.

## Samples

```
4
3 6 12 24

```

```
0

```

```
4
-8 -16 24 -32

```

```
1

```

```
4
0 1 2 3

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-51D |
| Contest | 51 |
| Index | D |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*2200` |
| Codeforces 通过次数 | 553 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/51/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/51/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P51D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

