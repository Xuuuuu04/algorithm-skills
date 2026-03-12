# CF-28C Bath Queue

## 题面快照

## Description

There are n students living in the campus. Every morning all students wake up at the same time and go to wash. There are m rooms with wash basins. The i-th of these rooms contains ai wash basins. Every student independently select one the rooms with equal probability and goes to it. After all students selected their rooms, students in each room divide into queues by the number of wash basins so that the size of the largest queue is the least possible. Calculate the expected value of the size of the largest queue among all rooms.

The first line contains two positive integers n and m (1 ≤ n, m ≤ 50) — the amount of students and the amount of rooms. The second line contains m integers a1, a2, ... , am (1 ≤ ai ≤ 50). ai means the amount of wash basins in the i-th room.

Output single number: the expected value of the size of the largest queue. Your answer must have an absolute or relative error less than 10 - 9.

## Input

The first line contains two positive integers n and m (1 ≤ n, m ≤ 50) — the amount of students and the amount of rooms. The second line contains m integers a1, a2, ... , am (1 ≤ ai ≤ 50). ai means the amount of wash basins in the i-th room.

## Output

Output single number: the expected value of the size of the largest queue. Your answer must have an absolute or relative error less than 10 - 9.

## Samples

```
1 1
2

```

```
1.00000000000000000000

```

```
2 2
1 1

```

```
1.50000000000000000000

```

```
2 3
1 1 1

```

```
1.33333333333333350000

```

```
7 5
1 1 2 3 1

```

```
2.50216960000000070000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-28C |
| Contest | 28 |
| Index | C |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `combinatorics`、`dp`、`probabilities` |
| 镜像标签 | `combinatorics`、`dp`、`probabilities`、`*2200` |
| Codeforces 通过次数 | 1253 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/28/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/28/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P28C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

