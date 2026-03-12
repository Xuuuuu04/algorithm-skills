# CF-91A Newspaper Headline

## 题面快照

## Description

A newspaper is published in Walrusland. Its heading is s1, it consists of lowercase Latin letters. Fangy the little walrus wants to buy several such newspapers, cut out their headings, glue them one to another in order to get one big string. After that walrus erase several letters from this string in order to get a new word s2. It is considered that when Fangy erases some letter, there's no whitespace formed instead of the letter. That is, the string remains unbroken and it still only consists of lowercase Latin letters.

For example, the heading is "abc". If we take two such headings and glue them one to the other one, we get "abcabc". If we erase the letters on positions 1 and 5, we get a word "bcac".

Which least number of newspaper headings s1 will Fangy need to glue them, erase several letters and get word s2?

The input data contain two lines. The first line contain the heading s1, the second line contains the word s2. The lines only consist of lowercase Latin letters (1 ≤ |s1| ≤ 104, 1 ≤ |s2| ≤ 106).

If it is impossible to get the word s2 in the above-described manner, print "-1" (without the quotes). Otherwise, print the least number of newspaper headings s1, which Fangy will need to receive the word s2.

## Input

The input data contain two lines. The first line contain the heading s1, the second line contains the word s2. The lines only consist of lowercase Latin letters (1 ≤ |s1| ≤ 104, 1 ≤ |s2| ≤ 106).

## Output

If it is impossible to get the word s2 in the above-described manner, print "-1" (without the quotes). Otherwise, print the least number of newspaper headings s1, which Fangy will need to receive the word s2.

## Samples

```
abc
xyz

```

```
-1

```

```
abcd
dabc

```

```
2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-91A |
| Contest | 91 |
| Index | A |
| Rating | 1500 |
| Points | 500.0 |
| Codeforces 标签 | `greedy`、`strings` |
| 镜像标签 | `greedy`、`strings`、`*1500` |
| Codeforces 通过次数 | 3918 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/91/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/91/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P91A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

