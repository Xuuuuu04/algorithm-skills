# CF-54D Writing a Song

## 题面快照

## Description

One of the Hedgehog and his friend's favorite entertainments is to take some sentence or a song and replace half of the words (sometimes even all of them) with each other's names.

The friend's birthday is approaching and the Hedgehog decided to make a special present to his friend: a very long song, where his name will be repeated many times. But try as he might, he can't write a decent song!

The problem is that the Hedgehog has already decided how long the resulting sentence should be (i.e. how many letters it should contain) and in which positions in the sentence the friend's name should occur, and it must not occur in any other position in the sentence. Besides, the Hedgehog decided to limit himself to using only the first K letters of an English alphabet in this sentence (so it will be not even a sentence, but one long word).

The resulting problem is indeed quite complicated, that's why the Hedgehog asks you to help him and write a program that will make the desired word by the given name P, the length N of the required word, the given positions of the occurrences of the name P in the desired word and the alphabet's size K. Note that the occurrences of the name can overlap with each other.

The first line contains numbers N and K which are the length of the required string and the alphabet size accordingly. The limitations are: 1 ≤ N ≤ 100, 2 ≤ K ≤ 26.

The second line contains the name P which is a non-empty string whose length does not exceed N characters. The string consists only of the first K lowercase symbols of an English alphabet.

The third line contains the string of length N - length(P) + 1, consisting only of numbers zero and one. A number one in the i-th position means that an occurrence of the name P should start from i-th position of the desired word, while a zero means that there is no occurrence starting here.

Print the desired word S. If there are several answers, print any of them.

If there is no solution, then print "No solution".

## Input

The first line contains numbers N and K which are the length of the required string and the alphabet size accordingly. The limitations are: 1 ≤ N ≤ 100, 2 ≤ K ≤ 26.

The second line contains the name P which is a non-empty string whose length does not exceed N characters. The string consists only of the first K lowercase symbols of an English alphabet.

The third line contains the string of length N - length(P) + 1, consisting only of numbers zero and one. A number one in the i-th position means that an occurrence of the name P should start from i-th position of the desired word, while a zero means that there is no occurrence starting here.

## Output

Print the desired word S. If there are several answers, print any of them.

If there is no solution, then print "No solution".

## Samples

```
5 2
aba
101

```

```
ababa

```

```
5 2
a
10001

```

```
abbba

```

```
6 2
abba
101

```

```
No solution

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-54D |
| Contest | 54 |
| Index | D |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `brute force`、`dp`、`strings` |
| 镜像标签 | `brute force`、`dp`、`strings`、`*2100` |
| Codeforces 通过次数 | 694 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/54/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/54/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P54D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

