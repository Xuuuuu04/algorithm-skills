# CF-22B Bargaining Table

## 题面快照

## Description

Bob wants to put a new bargaining table in his office. To do so he measured the office room thoroughly and drew its plan: Bob's office room is a rectangular room n × m meters. Each square meter of the room is either occupied by some furniture, or free. A bargaining table is rectangular, and should be placed so, that its sides are parallel to the office walls. Bob doesn't want to change or rearrange anything, that's why all the squares that will be occupied by the table should be initially free. Bob wants the new table to sit as many people as possible, thus its perimeter should be maximal. Help Bob find out the maximum possible perimeter of a bargaining table for his office.

The first line contains 2 space-separated numbers n and m (1 ≤ n, m ≤ 25) — the office room dimensions. Then there follow n lines with m characters 0 or 1 each. 0 stands for a free square meter of the office room. 1 stands for an occupied square meter. It's guaranteed that at least one square meter in the room is free.

Output one number — the maximum possible perimeter of a bargaining table for Bob's office room.

## Input

The first line contains 2 space-separated numbers n and m (1 ≤ n, m ≤ 25) — the office room dimensions. Then there follow n lines with m characters 0 or 1 each. 0 stands for a free square meter of the office room. 1 stands for an occupied square meter. It's guaranteed that at least one square meter in the room is free.

## Output

Output one number — the maximum possible perimeter of a bargaining table for Bob's office room.

## Samples

```
3 3
000
010
000

```

```
8

```

```
5 4
1100
0000
0000
0000
0000

```

```
16

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-22B |
| Contest | 22 |
| Index | B |
| Rating | 1500 |
| Points | - |
| Codeforces 标签 | `brute force`、`dp` |
| 镜像标签 | `brute force`、`dp`、`*1500` |
| Codeforces 通过次数 | 4728 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/22/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/22/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P22B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

