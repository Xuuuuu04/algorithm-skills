# CF-45I TCMCF+++

## 题面快照

## Description

Vasya has gotten interested in programming contests in TCMCF+++ rules. On the contest n problems were suggested and every problem had a cost — a certain integral number of points (perhaps, negative or even equal to zero). According to TCMCF+++ rules, only accepted problems can earn points and the overall number of points of a contestant was equal to the product of the costs of all the problems he/she had completed. If a person didn't solve anything, then he/she didn't even appear in final standings and wasn't considered as participant. Vasya understood that to get the maximal number of points it is not always useful to solve all the problems. Unfortunately, he understood it only after the contest was finished. Now he asks you to help him: find out what problems he had to solve to earn the maximal number of points.

## Input

Input

The first line contains an integer n (1 ≤ n ≤ 100) — the number of the suggested problems. The next line contains n space-separated integers ci ( - 100 ≤ ci ≤ 100) — the cost of the i-th task. The tasks' costs may coinсide.

## Output

Output

Print space-separated the costs of the problems that needed to be solved to get the maximal possible number of points. Do not forget, please, that it was necessary to solve at least one problem. If there are several solutions to that problem, print any of them.

## Samples

### Sample 1

Input
```
5
1 2 -3 3 3
```

Output
```
3 1 2 3
```

### Sample 2

Input
```
13
100 100 100 100 100 100 100 100 100 100 100 100 100
```

Output
```
100 100 100 100 100 100 100 100 100 100 100 100 100
```

### Sample 3

Input
```
4
-2 -2 -2 -2
```

Output
```
-2 -2 -2 -2
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-45I |
| Contest | 45 |
| Index | I |
| Rating | 1400 |
| Points | - |
| Codeforces 标签 | `greedy` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 2768 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/45/I)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/45/problem/I)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/45/I)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

