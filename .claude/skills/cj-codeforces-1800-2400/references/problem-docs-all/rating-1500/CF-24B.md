# CF-24B F1 Champions

## 题面快照

## Description

Formula One championship consists of series of races called Grand Prix. After every race drivers receive points according to their final position. Only the top 10 drivers receive points in the following order 25, 18, 15, 12, 10, 8, 6, 4, 2, 1. At the conclusion of the championship the driver with most points is the champion. If there is a tie, champion is the one with most wins (i.e. first places). If a tie still exists, it is chosen the one with most second places, and so on, until there are no more place to use for compare.

Last year another scoring system was proposed but rejected. In it the champion is the one with most wins. If there is tie, champion is the one with most points. If a tie still exists it is proceeded the same way as in the original scoring system, that is comparing number of second, third, forth, and so on, places.

You are given the result of all races during the season and you are to determine the champion according to both scoring systems. It is guaranteed, that both systems will produce unique champion.

## Input

Input

The first line contain integer t (1 ≤ t ≤ 20), where t is the number of races. After that all races are described one by one. Every race description start with an integer n (1 ≤ n ≤ 50) on a line of itself, where n is the number of clasified drivers in the given race. After that n lines follow with the classification for the race, each containing the name of a driver. The names of drivers are given in order from the first to the last place. The name of the driver consists of lowercase and uppercase English letters and has length at most 50 characters. Comparing of names should be case-sensetive.

## Output

Output

Your output should contain exactly two line. On the first line is the name of the champion according to the original rule, and on the second line the name of the champion according to the alternative rule.

## Samples

### Sample 1

Input
```
3
3
Hamilton
Vettel
Webber
2
Webber
Vettel
2
Hamilton
Vettel
```

Output
```
Vettel
Hamilton
```

### Sample 2

Input
```
2
7
Prost
Surtees
Nakajima
Schumacher
Button
DeLaRosa
Buemi
8
Alonso
Prost
NinoFarina
JimClark
DeLaRosa
Nakajima
Patrese
Surtees
```

Output
```
Prost
Prost
```

## Note

Note

It is not guaranteed that the same drivers participate in all races. For the championship consider every driver that has participated in at least one race. The total number of drivers during the whole season is not more then 50.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Codeforces 官方镜像 |
| 编号 | CF-24B |
| Contest | 24 |
| Index | B |
| Rating | 1500 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | 无 |
| Codeforces 通过次数 | 2001 |
| 镜像尝试 / 通过 | - / - |
| 时限 | 2 seconds |
| 内存限制 | 256 megabytes |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/24/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/24/problem/B)
- Codeforces 官方镜像：[mirror](https://mirror.codeforces.com/problemset/problem/24/B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

