# CF-79C Beaver

## 题面快照

## Description

After Fox Ciel got off a bus, she found that the bus she was on was a wrong bus and she lost her way in a strange town. However, she fortunately met her friend Beaver Taro and asked which way to go to her castle. Taro's response to her was a string s, and she tried to remember the string s correctly.

However, Ciel feels n strings b1, b2, ... , bn are really boring, and unfortunately she dislikes to remember a string that contains a boring substring. To make the thing worse, what she can remember is only the contiguous substring of s.

Determine the longest contiguous substring of s that does not contain any boring string, so that she can remember the longest part of Taro's response.

In the first line there is a string s. The length of s will be between 1 and 105, inclusive.

In the second line there is a single integer n (1 ≤ n ≤ 10). Next n lines, there is a string bi (1 ≤ i ≤ n). Each length of bi will be between 1 and 10, inclusive.

Each character of the given strings will be either a English alphabet (both lowercase and uppercase) or a underscore ('_') or a digit. Assume that these strings are case-sensitive.

Output in the first line two space-separated integers len and pos: the length of the longest contiguous substring of s that does not contain any bi, and the first position of the substring (0-indexed). The position pos must be between 0 and |s| - len inclusive, where |s| is the length of string s.

If there are several solutions, output any.

## Input

In the first line there is a string s. The length of s will be between 1 and 105, inclusive.

In the second line there is a single integer n (1 ≤ n ≤ 10). Next n lines, there is a string bi (1 ≤ i ≤ n). Each length of bi will be between 1 and 10, inclusive.

Each character of the given strings will be either a English alphabet (both lowercase and uppercase) or a underscore ('_') or a digit. Assume that these strings are case-sensitive.

## Output

Output in the first line two space-separated integers len and pos: the length of the longest contiguous substring of s that does not contain any bi, and the first position of the substring (0-indexed). The position pos must be between 0 and |s| - len inclusive, where |s| is the length of string s.

If there are several solutions, output any.

## Samples

```
Go_straight_along_this_street
5
str
long
tree
biginteger
ellipse

```

```
12 4

```

```
IhaveNoIdea
9
I
h
a
v
e
N
o
I
d

```

```
0 0

```

```
unagioisii
2
ioi
unagi

```

```
5 5

```

## Note

In the first sample, the solution is traight_alon.

In the second sample, the solution is an empty string, so the output can be «0 0», «0 1», «0 2», and so on.

In the third sample, the solution is either nagio or oisii.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-79C |
| Contest | 79 |
| Index | C |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `data structures`、`dp`、`greedy`、`hashing`、`strings`、`two pointers` |
| 镜像标签 | `data structures`、`dp`、`greedy`、`hashing`、`strings`、`two pointers`、`*1800` |
| Codeforces 通过次数 | 2051 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/79/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/79/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P79C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

