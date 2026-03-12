# CF-10A Power Consumption Calculation

## 题面快照

## Description

Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P1 watt per minute. T1 minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P2 watt per minute. Finally, after T2 minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P3 watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into n time periods [l1, r1], [l2, r2], ..., [ln, rn]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l1, rn].

## Input

Input

The first line contains 6 integer numbers n, P1, P2, P3, T1, T2 (1 ≤ n ≤ 100, 0 ≤ P1, P2, P3 ≤ 100, 1 ≤ T1, T2 ≤ 60). The following n lines contain description of Tom's work. Each i-th of these lines contains two space-separated integers li and ri (0 ≤ li < ri ≤ 1440, ri < li + 1 for i < n), which stand for the start and the end of the i-th period of work.

## Output

Output

Output the answer to the problem.

## Samples

### Sample 1

Input
```
1 3 2 1 5 10
0 10
```

Output
```
30
```

### Sample 2

Input
```
2 8 4 2 5 10
20 30
50 100
```

Output
```
570
```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-10A |
| Contest | 10 |
| Index | A |
| Rating | 900 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 8245 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 1 second |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/10/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/10/problem/A)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/10/A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

