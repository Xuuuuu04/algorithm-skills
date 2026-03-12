# CF-45E Director

## 题面快照

## Description

Vasya is a born Berland film director, he is currently working on a new blockbuster, "The Unexpected". Vasya knows from his own experience how important it is to choose the main characters' names and surnames wisely. He made up a list of n names and n surnames that he wants to use. Vasya haven't decided yet how to call characters, so he is free to match any name to any surname. Now he has to make the list of all the main characters in the following format: "Name1Surname1, Name2Surname2, ..., NamenSurnamen", i.e. all the name-surname pairs should be separated by exactly one comma and exactly one space, and the name should be separated from the surname by exactly one space. First of all Vasya wants to maximize the number of the pairs, in which the name and the surname start from one letter. If there are several such variants, Vasya wants to get the lexicographically minimal one. Help him.

An answer will be verified a line in the format as is shown above, including the needed commas and spaces. It's the lexicographical minimality of such a line that needs to be ensured. The output line shouldn't end with a space or with a comma.

The first input line contains number n (1 ≤ n ≤ 100) — the number of names and surnames. Then follow n lines — the list of names. Then follow n lines — the list of surnames. No two from those 2n strings match. Every name and surname is a non-empty string consisting of no more than 10 Latin letters. It is guaranteed that the first letter is uppercase and the rest are lowercase.

The output data consist of a single line — the needed list. Note that one should follow closely the output data format!

## Input

The first input line contains number n (1 ≤ n ≤ 100) — the number of names and surnames. Then follow n lines — the list of names. Then follow n lines — the list of surnames. No two from those 2n strings match. Every name and surname is a non-empty string consisting of no more than 10 Latin letters. It is guaranteed that the first letter is uppercase and the rest are lowercase.

## Output

The output data consist of a single line — the needed list. Note that one should follow closely the output data format!

## Samples

```
4
Ann
Anna
Sabrina
John
Petrov
Ivanova
Stoltz
Abacaba

```

```
Ann Abacaba, Anna Ivanova, John Petrov, Sabrina Stoltz

```

```
4
Aa
Ab
Ac
Ba
Ad
Ae
Bb
Bc

```

```
Aa Ad, Ab Ae, Ac Bb, Ba Bc

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-45E |
| Contest | 45 |
| Index | E |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`greedy` |
| 镜像标签 | `constructive algorithms`、`greedy`、`*2000` |
| Codeforces 通过次数 | 636 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/45/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/45/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P45E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

