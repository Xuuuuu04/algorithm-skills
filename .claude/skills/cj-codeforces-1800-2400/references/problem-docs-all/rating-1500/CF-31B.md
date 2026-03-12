# CF-31B Sysadmin Bob

## 题面快照

## Description

Email address in Berland is a string of the form A@B, where A and B are arbitrary strings consisting of small Latin letters.

Bob is a system administrator in «Bersoft» company. He keeps a list of email addresses of the company's staff. This list is as a large string, where all addresses are written in arbitrary order, separated by commas. The same address can be written more than once.

Suddenly, because of unknown reasons, all commas in Bob's list disappeared. Now Bob has a string, where all addresses are written one after another without any separators, and there is impossible to determine, where the boundaries between addresses are. Unfortunately, on the same day his chief asked him to bring the initial list of addresses. Now Bob wants to disjoin addresses in some valid way. Help him to do that.

The first line contains the list of addresses without separators. The length of this string is between 1 and 200, inclusive. The string consists only from small Latin letters and characters «@».

If there is no list of the valid (according to the Berland rules) email addresses such that after removing all commas it coincides with the given string, output No solution. In the other case, output the list. The same address can be written in this list more than once. If there are several solutions, output any of them.

## Input

The first line contains the list of addresses without separators. The length of this string is between 1 and 200, inclusive. The string consists only from small Latin letters and characters «@».

## Output

If there is no list of the valid (according to the Berland rules) email addresses such that after removing all commas it coincides with the given string, output No solution. In the other case, output the list. The same address can be written in this list more than once. If there are several solutions, output any of them.

## Samples

```
a@aa@a

```

```
a@a,a@a

```

```
a@a@a

```

```
No solution

```

```
@aa@a

```

```
No solution

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-31B |
| Contest | 31 |
| Index | B |
| Rating | 1500 |
| Points | 1000.0 |
| Codeforces 标签 | `greedy`、`implementation`、`strings` |
| 镜像标签 | `greedy`、`implementation`、`strings`、`*1500` |
| Codeforces 通过次数 | 4706 |
| 镜像尝试 / 通过 | 2 / 1 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/31/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/31/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P31B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

