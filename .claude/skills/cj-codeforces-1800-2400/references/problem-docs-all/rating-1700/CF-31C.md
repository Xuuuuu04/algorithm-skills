# CF-31C Schedule

## 题面快照

## Description

At the beginning of the new semester there is new schedule in the Berland State University. According to this schedule, n groups have lessons at the room 31. For each group the starting time of the lesson and the finishing time of the lesson are known. It has turned out that it is impossible to hold all lessons, because for some groups periods of their lessons intersect. If at some moment of time one groups finishes it's lesson, and the other group starts the lesson, their lessons don't intersect.

The dean wants to cancel the lesson in one group so that no two time periods of lessons of the remaining groups intersect. You are to find all ways to do that.

The first line contains integer n (1 ≤ n ≤ 5000) — amount of groups, which have lessons in the room 31. Then n lines follow, each of them contains two integers liri (1 ≤ li < ri ≤ 106) — starting and finishing times of lesson of the i-th group. It is possible that initially no two lessons intersect (see sample 1).

Output integer k — amount of ways to cancel the lesson in exactly one group so that no two time periods of lessons of the remaining groups intersect. In the second line output k numbers — indexes of groups, where it is possible to cancel the lesson. Groups are numbered starting from 1 in the order that they were given in the input. Output the numbers in increasing order.

## Input

The first line contains integer n (1 ≤ n ≤ 5000) — amount of groups, which have lessons in the room 31. Then n lines follow, each of them contains two integers liri (1 ≤ li < ri ≤ 106) — starting and finishing times of lesson of the i-th group. It is possible that initially no two lessons intersect (see sample 1).

## Output

Output integer k — amount of ways to cancel the lesson in exactly one group so that no two time periods of lessons of the remaining groups intersect. In the second line output k numbers — indexes of groups, where it is possible to cancel the lesson. Groups are numbered starting from 1 in the order that they were given in the input. Output the numbers in increasing order.

## Samples

```
3
3 10
20 30
1 3

```

```
3
1 2 3

```

```
4
3 10
20 30
1 3
1 39

```

```
1
4

```

```
3
1 5
2 6
3 7

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-31C |
| Contest | 31 |
| Index | C |
| Rating | 1700 |
| Points | 1500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1700` |
| Codeforces 通过次数 | 1992 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/31/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/31/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P31C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

