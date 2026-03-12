# CF-58E Expression

## 题面快照

## Description

One day Vasya was solving arithmetical problems. He wrote down an expression a + b = c in his notebook. When the teacher checked Vasya's work it turned out that Vasya had solved the problem incorrectly. Now Vasya tries to find excuses. He says that he simply forgot to write down several digits in numbers a, b and c, but he can't remember what numbers they actually were. Help Vasya, find such numbers x, y and z, with which the following conditions are met:

- x + y = z,

-  from the expression x + y = z several digits can be erased in such a way that the result will be a + b = c,

-  the expression x + y = z should have the minimal length.

The first and only input line contains the expression a + b = c (1 ≤ a, b, c ≤ 106, a, b and c don't contain leading zeroes) which is the expression Vasya wrote down.

Print the correct expression x + y = z (x, y and z are non-negative numbers without leading zeroes). The expression a + b = c must be met in x + y = z as a subsequence. The printed solution should have the minimal possible number of characters. If there are several such solutions, you can print any of them.

## Input

The first and only input line contains the expression a + b = c (1 ≤ a, b, c ≤ 106, a, b and c don't contain leading zeroes) which is the expression Vasya wrote down.

## Output

Print the correct expression x + y = z (x, y and z are non-negative numbers without leading zeroes). The expression a + b = c must be met in x + y = z as a subsequence. The printed solution should have the minimal possible number of characters. If there are several such solutions, you can print any of them.

## Samples

```
2+4=5

```

```
21+4=25

```

```
1+1=3

```

```
1+31=32

```

```
1+1=2

```

```
1+1=2

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-58E |
| Contest | 58 |
| Index | E |
| Rating | 2400 |
| Points | 2500.0 |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*2400` |
| Codeforces 通过次数 | 454 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/58/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/58/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P58E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

