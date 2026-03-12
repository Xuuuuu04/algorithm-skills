# CF-73C LionAge II

## 题面快照

## Description

Vasya plays the LionAge II. He was bored of playing with a stupid computer, so he installed this popular MMORPG, to fight with his friends. Vasya came up with the name of his character — non-empty string s, consisting of a lowercase Latin letters. However, in order not to put up a front of friends, Vasya has decided to change no more than k letters of the character name so that the new name sounded as good as possible. Euphony of the line is defined as follows: for each pair of adjacent letters x and y (x immediately precedes y) the bonus c(x, y) is added to the result. Your task is to determine what the greatest Euphony can be obtained by changing at most k letters in the name of the Vasya's character.

The first line contains character's name s and an integer number k (0 ≤ k ≤ 100). The length of the nonempty string s does not exceed 100. The second line contains an integer number n (0 ≤ n ≤ 676) — amount of pairs of letters, giving bonus to the euphony. The next n lines contain description of these pairs «xyc», which means that sequence xy gives bonus c (x, y — lowercase Latin letters,  - 1000 ≤ c ≤ 1000). It is guaranteed that no pair xy mentioned twice in the input data.

Output the only number — maximum possible euphony оf the new character's name.

## Input

The first line contains character's name s and an integer number k (0 ≤ k ≤ 100). The length of the nonempty string s does not exceed 100. The second line contains an integer number n (0 ≤ n ≤ 676) — amount of pairs of letters, giving bonus to the euphony. The next n lines contain description of these pairs «xyc», which means that sequence xy gives bonus c (x, y — lowercase Latin letters,  - 1000 ≤ c ≤ 1000). It is guaranteed that no pair xy mentioned twice in the input data.

## Output

Output the only number — maximum possible euphony оf the new character's name.

## Samples

```
winner 4
4
s e 7
o s 8
l o 13
o o 8

```

```
36

```

```
abcdef 1
5
a b -10
b c 5
c d 5
d e 5
e f 5

```

```
20

```

## Note

In the first example the most euphony name will be looser. It is easy to calculate that its euphony is 36.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-73C |
| Contest | 73 |
| Index | C |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*1800` |
| Codeforces 通过次数 | 2473 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/73/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/73/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P73C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

