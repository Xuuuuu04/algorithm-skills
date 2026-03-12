# CF-41C Email address

## 题面快照

## Description

Sometimes one has to spell email addresses over the phone. Then one usually pronounces a dot as dot, an at sign as at. As a result, we get something like vasyaatgmaildotcom. Your task is to transform it into a proper email address (vasya@gmail.com).

It is known that a proper email address contains only such symbols as .@ and lower-case Latin letters, doesn't start with and doesn't end with a dot. Also, a proper email address doesn't start with and doesn't end with an at sign. Moreover, an email address contains exactly one such symbol as @, yet may contain any number (possible, zero) of dots.

You have to carry out a series of replacements so that the length of the result was as short as possible and it was a proper email address. If the lengths are equal, you should print the lexicographically minimal result.

Overall, two variants of replacement are possible: dot can be replaced by a dot, at can be replaced by an at.

The first line contains the email address description. It is guaranteed that that is a proper email address with all the dots replaced by dot an the at signs replaced by at. The line is not empty and its length does not exceed 100 symbols.

Print the shortest email address, from which the given line could be made by the described above replacements. If there are several solutions to that problem, print the lexicographically minimal one (the lexicographical comparison of the lines are implemented with an operator < in modern programming languages).

In the ASCII table the symbols go in this order: . @ ab...z

## Input

The first line contains the email address description. It is guaranteed that that is a proper email address with all the dots replaced by dot an the at signs replaced by at. The line is not empty and its length does not exceed 100 symbols.

## Output

Print the shortest email address, from which the given line could be made by the described above replacements. If there are several solutions to that problem, print the lexicographically minimal one (the lexicographical comparison of the lines are implemented with an operator < in modern programming languages).

In the ASCII table the symbols go in this order: . @ ab...z

## Samples

```
vasyaatgmaildotcom

```

```
vasya@gmail.com

```

```
dotdotdotatdotdotat

```

```
dot..@..at

```

```
aatt

```

```
a@t

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-41C |
| Contest | 41 |
| Index | C |
| Rating | 1300 |
| Points | 1500.0 |
| Codeforces 标签 | `expression parsing`、`implementation` |
| 镜像标签 | `expression parsing`、`implementation`、`*1300` |
| Codeforces 通过次数 | 4162 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/41/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/41/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P41C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

