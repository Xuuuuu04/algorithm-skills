# CF-38E Let's Go Rolling!

## 题面快照

## Description

On a number axis directed from the left rightwards, n marbles with coordinates x1, x2, ..., xn are situated. Let's assume that the sizes of the marbles are infinitely small, that is in this task each of them is assumed to be a material point. You can stick pins in some of them and the cost of sticking in the marble number i is equal to ci, number ci may be negative. After you choose and stick the pins you need, the marbles will start to roll left according to the rule: if a marble has a pin stuck in it, then the marble doesn't move, otherwise the marble rolls all the way up to the next marble which has a pin stuck in it and stops moving there. If there is no pinned marble on the left to the given unpinned one, it is concluded that the marble rolls to the left to infinity and you will pay an infinitely large fine for it. If no marble rolled infinitely to the left, then the fine will consist of two summands:

-  the sum of the costs of stuck pins;

-  the sum of the lengths of the paths of each of the marbles, that is the sum of absolute values of differences between their initial and final positions.

Your task is to choose and pin some marbles in the way that will make the fine for you to pay as little as possible.

The first input line contains an integer n (1 ≤ n ≤ 3000) which is the number of marbles. The next n lines contain the descriptions of the marbles in pairs of integers xi, ci ( - 109 ≤ xi, ci ≤ 109). The numbers are space-separated. Each description is given on a separate line. No two marbles have identical initial positions.

Output the single number — the least fine you will have to pay.

## Input

The first input line contains an integer n (1 ≤ n ≤ 3000) which is the number of marbles. The next n lines contain the descriptions of the marbles in pairs of integers xi, ci ( - 109 ≤ xi, ci ≤ 109). The numbers are space-separated. Each description is given on a separate line. No two marbles have identical initial positions.

## Output

Output the single number — the least fine you will have to pay.

## Samples

```
3
2 3
3 4
1 2

```

```
5

```

```
4
1 7
3 1
5 10
6 1

```

```
11

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-38E |
| Contest | 38 |
| Index | E |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `dp`、`sortings` |
| 镜像标签 | `dp`、`sortings`、`*1800` |
| Codeforces 通过次数 | 2968 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/38/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/38/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P38E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

