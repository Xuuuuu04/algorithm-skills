# CF-81B Sequence Formatting

## 题面快照

## Description

Polycarp is very careful. He even types numeric sequences carefully, unlike his classmates. If he sees a sequence without a space after the comma, with two spaces in a row, or when something else does not look neat, he rushes to correct it. For example, number sequence written like "1,2 ,3,..., 10" will be corrected to "1, 2, 3, ..., 10".

In this task you are given a string s, which is composed by a concatination of terms, each of which may be:

-  a positive integer of an arbitrary length (leading zeroes are not allowed),

-  a "comma" symbol (","),

-  a "space" symbol (""),

-  "three dots" ("...", that is, exactly three points written one after another, also known as suspension points).

Polycarp wants to add and remove spaces in the string s to ensure the following:

-  each comma is followed by exactly one space (if the comma is the last character in the string, this rule does not apply to it),

-  each "three dots" term is preceded by exactly one space (if the dots are at the beginning of the string, this rule does not apply to the term),

-  if two consecutive numbers were separated by spaces only (one or more), then exactly one of them should be left,

-  there should not be other spaces.

Automate Polycarp's work and write a program that will process the given string s.

The input data contains a single string s. Its length is from 1 to 255 characters. The string s does not begin and end with a space. Its content matches the description given above.

Print the string s after it is processed. Your program's output should be exactly the same as the expected answer. It is permissible to end output line with a line-break character, and without it.

## Input

The input data contains a single string s. Its length is from 1 to 255 characters. The string s does not begin and end with a space. Its content matches the description given above.

## Output

Print the string s after it is processed. Your program's output should be exactly the same as the expected answer. It is permissible to end output line with a line-break character, and without it.

## Samples

```
1,2 ,3,...,     10

```

```
1, 2, 3, ..., 10

```

```
1,,,4...5......6

```

```
1, , , 4 ...5 ... ...6

```

```
...,1,2,3,...

```

```
..., 1, 2, 3, ...

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-81B |
| Contest | 81 |
| Index | B |
| Rating | 1700 |
| Points | 1000.0 |
| Codeforces 标签 | `implementation`、`strings` |
| 镜像标签 | `implementation`、`strings`、`*1700` |
| Codeforces 通过次数 | 2114 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/81/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/81/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P81B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

