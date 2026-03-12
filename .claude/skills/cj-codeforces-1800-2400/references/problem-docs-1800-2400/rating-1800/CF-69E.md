# CF-69E Subsegments

## 题面快照

## Description

Programmer Sasha has recently begun to study data structures. His coach Stas told him to solve the problem of finding a minimum on the segment of the array in , which Sasha coped with. For Sasha not to think that he had learned all, Stas gave him a new task. For each segment of the fixed length Sasha must find the maximum element of those that occur on the given segment exactly once. Help Sasha solve this problem.

The first line contains two positive integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ n) — the number of array elements and the length of the segment.

Then follow n lines: the i-th one contains a single number ai ( - 109 ≤ ai ≤ 109).

Print n–k + 1 numbers, one per line: on the i-th line print of the maximum number of those numbers from the subarray aiai + 1 … ai + k - 1 that occur in this subarray exactly 1 time. If there are no such numbers in this subarray, print "Nothing".

## Input

The first line contains two positive integers n and k (1 ≤ n ≤ 105, 1 ≤ k ≤ n) — the number of array elements and the length of the segment.

Then follow n lines: the i-th one contains a single number ai ( - 109 ≤ ai ≤ 109).

## Output

Print n–k + 1 numbers, one per line: on the i-th line print of the maximum number of those numbers from the subarray aiai + 1 … ai + k - 1 that occur in this subarray exactly 1 time. If there are no such numbers in this subarray, print "Nothing".

## Samples

```
5 3
1
2
2
3
3

```

```
1
3
2

```

```
6 4
3
3
3
4
4
2

```

```
4
Nothing
3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-69E |
| Contest | 69 |
| Index | E |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `data structures`、`implementation` |
| 镜像标签 | `data structures`、`implementation`、`*1800` |
| Codeforces 通过次数 | 5029 |
| 镜像尝试 / 通过 | 2 / 2 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/69/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/69/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P69E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

