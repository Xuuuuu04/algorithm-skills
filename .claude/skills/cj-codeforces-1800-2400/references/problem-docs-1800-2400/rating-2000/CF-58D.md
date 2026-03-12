# CF-58D Calendar

## 题面快照

## Description

BerOilGasDiamondBank has branches in n cities, at that n is an even number. The bank management wants to publish a calendar with the names of all those cities written in two columns: the calendar should consist of exactly n / 2 lines of strictly equal length, each of which contains exactly two names and exactly one separator character between them. The name of every city should be used in the calendar exactly once. For historical reasons the symbol d is used as the separator of words in the calendar.

The BerOilGasDiamondBank management wants to show that all its branches are equally important to it, that's why the order of their appearance in the calendar should be following: if we "glue"(concatinate) all the n / 2 calendar lines (from top to bottom) to make a single line, then the lexicographically minimal line is obtained. No separator character will be used to separate calendar lines. For example, if the lines are "bertown!berville", "newberville!bera", then the resulting line is "bertown!bervillenewberville!bera". In some sense one has to find the lexicographically minimal calendar, where the comparison of calendars happens line by line.

Help BerOilGasDiamondBank and construct the required calendar.

The first line contains an integer n (1 ≤ n ≤ 104, n is even) which is the number of branches. Then follow n lines which are the names of the cities. All the names consist of lowercase Latin letters; their lengths are no less than 1 and no more than 10 symbols. The next line contains a single symbol d (d has an ASCII-code from 33 to 126 inclusively, excluding lowercase Latin letters) which is the separator between words in the calendar lines. It is guaranteed that the calendar is possible to be constructed and all the names are different.

Print n / 2 lines of similar length which are the required calendar. Every line should contain exactly two words and exactly one separator between them. If there are several solutions, print the lexicographically minimal one. The lexicographical comparison of lines is realized by the "<" operator in the modern programming languages.

## Input

The first line contains an integer n (1 ≤ n ≤ 104, n is even) which is the number of branches. Then follow n lines which are the names of the cities. All the names consist of lowercase Latin letters; their lengths are no less than 1 and no more than 10 symbols. The next line contains a single symbol d (d has an ASCII-code from 33 to 126 inclusively, excluding lowercase Latin letters) which is the separator between words in the calendar lines. It is guaranteed that the calendar is possible to be constructed and all the names are different.

## Output

Print n / 2 lines of similar length which are the required calendar. Every line should contain exactly two words and exactly one separator between them. If there are several solutions, print the lexicographically minimal one. The lexicographical comparison of lines is realized by the "<" operator in the modern programming languages.

## Samples

```
4
b
aa
hg
c
.

```

```
aa.b
c.hg

```

```
2
aa
a
!

```

```
a!aa

```

```
2
aa
a
|

```

```
aa|a

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-58D |
| Contest | 58 |
| Index | D |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `greedy`、`strings` |
| 镜像标签 | `greedy`、`strings`、`*2000` |
| Codeforces 通过次数 | 825 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/58/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/58/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P58D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

