# CF-70C Lucky Tickets

## 题面快照

## Description

In Walrusland public transport tickets are characterized by two integers: by the number of the series and by the number of the ticket in the series. Let the series number be represented by a and the ticket number — by b, then a ticket is described by the ordered pair of numbers (a, b).

The walruses believe that a ticket is lucky if a * b = rev(a) * rev(b). The function rev(x) reverses a number written in the decimal system, at that the leading zeroes disappear. For example, rev(12343) = 34321, rev(1200) = 21.

The Public Transport Management Committee wants to release x series, each containing y tickets, so that atleastw lucky tickets were released and the total number of released tickets (x * y) were minimum. The series are numbered from 1 to x inclusive. The tickets in each series are numbered from 1 to y inclusive. The Transport Committee cannot release more than maxx series and more than maxy tickets in one series.

The first line contains three integers maxx, maxy, w (1 ≤ maxx, maxy ≤ 105, 1 ≤ w ≤ 107).

Print on a single line two space-separated numbers, the x and the y. If there are several possible variants, print any of them. If such x and y do not exist, print a single number  - 1.

## Input

The first line contains three integers maxx, maxy, w (1 ≤ maxx, maxy ≤ 105, 1 ≤ w ≤ 107).

## Output

Print on a single line two space-separated numbers, the x and the y. If there are several possible variants, print any of them. If such x and y do not exist, print a single number  - 1.

## Samples

```
2 2 1

```

```
1 1

```

```
132 10 35

```

```
7 5

```

```
5 18 1000

```

```
-1

```

```
48 132 235

```

```
22 111

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-70C |
| Contest | 70 |
| Index | C |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `binary search`、`data structures`、`sortings`、`two pointers` |
| 镜像标签 | `binary search`、`data structures`、`sortings`、`two pointers`、`*2200` |
| Codeforces 通过次数 | 625 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/70/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/70/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P70C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

