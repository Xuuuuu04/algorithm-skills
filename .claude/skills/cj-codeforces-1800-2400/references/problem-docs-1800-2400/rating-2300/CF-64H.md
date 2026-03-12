# CF-64H Table Bowling

## 题面快照

## Description

Table bowling tournament participant completed the competition according to the given final standings table. The table is given as a sequence of lines, each line has a format "name score". Your task is to prepare another table consisting of lines in the form "place name". Sort participant by score (desc.) and by the name lexicographically in the case of a tie. Places are numerated from 1. If more than one participant has some score, all of them share the places and you should output something like "12-14 john".

Please, look into the samples for clarification.

The first line contains n (1 ≤ n ≤ 100) — the number of rows in the table. Following n lines contain the given table. Each line has the form "name score", where "name" is a sequence of lowercase Latin letters, and "score" — is an integer number between 0 and 1000, inclusive. All the names are distinct. The length of each name is between 1 and 10 characters, inclusive. There is single space between the name and the score in each line.

Print the required table. Look at the sample outputs for clarifications.

## Input

The first line contains n (1 ≤ n ≤ 100) — the number of rows in the table. Following n lines contain the given table. Each line has the form "name score", where "name" is a sequence of lowercase Latin letters, and "score" — is an integer number between 0 and 1000, inclusive. All the names are distinct. The length of each name is between 1 and 10 characters, inclusive. There is single space between the name and the score in each line.

## Output

Print the required table. Look at the sample outputs for clarifications.

## Samples

```
5
vasya 10
ted 11
petya 10
katya 33
mike 44

```

```
1 mike
2 katya
3 ted
4-5 petya
4-5 vasya

```

```
3
a 1
b 13
c 1

```

```
1 b
2-3 a
2-3 c

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-64H |
| Contest | 64 |
| Index | H |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `*special`、`sortings` |
| 镜像标签 | `*special problem`、`sortings`、`*2300` |
| Codeforces 通过次数 | 122 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/64/H)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/64/problem/H)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P64H)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

