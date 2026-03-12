# CF-10E Greedy Change

## 题面快照

## Description

Billy investigates the question of applying greedy algorithm to different spheres of life. At the moment he is studying the application of greedy algorithm to the problem about change. There is an amount of n coins of different face values, and the coins of each value are not limited in number. The task is to collect the sum x with the minimum amount of coins. Greedy algorithm with each its step takes the coin of the highest face value, not exceeding x. Obviously, if among the coins' face values exists the face value 1, any sum x can be collected with the help of greedy algorithm. However, greedy algorithm does not always give the optimal representation of the sum, i.e. the representation with the minimum amount of coins. For example, if there are face values {1, 3, 4} and it is asked to collect the sum 6, greedy algorithm will represent the sum as 4 + 1 + 1, while the optimal representation is 3 + 3, containing one coin less. By the given set of face values find out if there exist such a sum x that greedy algorithm will collect in a non-optimal way. If such a sum exists, find out the smallest of these sums.

The first line contains an integer n (1 ≤ n ≤ 400) — the amount of the coins' face values. The second line contains n integers ai (1 ≤ ai ≤ 109), describing the face values. It is guaranteed that a1 > a2 > ... > an and an = 1.

If greedy algorithm collects any sum in an optimal way, output -1. Otherwise output the smallest sum that greedy algorithm collects in a non-optimal way.

## Input

The first line contains an integer n (1 ≤ n ≤ 400) — the amount of the coins' face values. The second line contains n integers ai (1 ≤ ai ≤ 109), describing the face values. It is guaranteed that a1 > a2 > ... > an and an = 1.

## Output

If greedy algorithm collects any sum in an optimal way, output -1. Otherwise output the smallest sum that greedy algorithm collects in a non-optimal way.

## Samples

```
5
25 10 5 2 1

```

```
-1

```

```
3
4 3 1

```

```
6

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-10E |
| Contest | 10 |
| Index | E |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | `constructive algorithms` |
| 镜像标签 | `constructive algorithms`、`*2600` |
| Codeforces 通过次数 | 904 |
| 镜像尝试 / 通过 | 2 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/10/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/10/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P10E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

