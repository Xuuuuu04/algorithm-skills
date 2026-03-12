# CF-95A Hockey

## 题面快照

## Description

Petya loves hockey very much. One day, as he was watching a hockey match, he fell asleep. Petya dreamt of being appointed to change a hockey team's name. Thus, Petya was given the original team name w and the collection of forbidden substrings s1, s2, ..., sn. All those strings consist of uppercase and lowercase Latin letters. String w has the length of |w|, its characters are numbered from 1 to |w|.

First Petya should find all the occurrences of forbidden substrings in the w string. During the search of substrings the case of letter shouldn't be taken into consideration. That is, strings "aBC" and "ABc" are considered equal.

After that Petya should perform the replacement of all letters covered by the occurrences. More formally: a letter in the position i should be replaced by any other one if for position i in string w there exist pair of indices l, r (1 ≤ l ≤ i ≤ r ≤ |w|) such that substring w[l ... r] is contained in the collection s1, s2, ..., sn, when using case insensitive comparison. During the replacement the letter's case should remain the same. Petya is not allowed to replace the letters that aren't covered by any forbidden substring.

Letter letter (uppercase or lowercase) is considered lucky for the hockey players. That's why Petya should perform the changes so that the letter occurred in the resulting string as many times as possible. Help Petya to find such resulting string. If there are several such strings, find the one that comes first lexicographically.

Note that the process of replacements is not repeated, it occurs only once. That is, if after Petya's replacements the string started to contain new occurrences of bad substrings, Petya pays no attention to them.

The first line contains the only integer n (1 ≤ n ≤ 100) — the number of forbidden substrings in the collection. Next n lines contain these substrings. The next line contains string w. All those n + 1 lines are non-empty strings consisting of uppercase and lowercase Latin letters whose length does not exceed 100. The last line contains a lowercase letter letter.

Output the only line — Petya's resulting string with the maximum number of letters letter. If there are several answers then output the one that comes first lexicographically.

The lexicographical comparison is performed by the standard < operator in modern programming languages. The line a is lexicographically smaller than the line b, if a is a prefix of b, or there exists such an i (1 ≤ i ≤ |a|), that ai < bi, and for any j (1 ≤ j < i) aj = bj. |a| stands for the length of string a.

## Input

The first line contains the only integer n (1 ≤ n ≤ 100) — the number of forbidden substrings in the collection. Next n lines contain these substrings. The next line contains string w. All those n + 1 lines are non-empty strings consisting of uppercase and lowercase Latin letters whose length does not exceed 100. The last line contains a lowercase letter letter.

## Output

Output the only line — Petya's resulting string with the maximum number of letters letter. If there are several answers then output the one that comes first lexicographically.

The lexicographical comparison is performed by the standard < operator in modern programming languages. The line a is lexicographically smaller than the line b, if a is a prefix of b, or there exists such an i (1 ≤ i ≤ |a|), that ai < bi, and for any j (1 ≤ j < i) aj = bj. |a| stands for the length of string a.

## Samples

```
3
bers
ucky
elu
PetrLoveLuckyNumbers
t

```

```
PetrLovtTttttNumtttt

```

```
4
hello
party
abefglghjdhfgj
IVan
petrsmatchwin
a

```

```
petrsmatchwin

```

```
2
aCa
cba
abAcaba
c

```

```
abCacba

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-95A |
| Contest | 95 |
| Index | A |
| Rating | 1600 |
| Points | 500.0 |
| Codeforces 标签 | `implementation`、`strings` |
| 镜像标签 | `implementation`、`strings`、`*1600` |
| Codeforces 通过次数 | 1836 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/95/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/95/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P95A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

