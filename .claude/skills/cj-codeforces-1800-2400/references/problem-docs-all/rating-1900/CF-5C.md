# CF-5C Longest Regular Bracket Sequence

## 题面快照

## Description

This is yet another problem dealing with regular bracket sequences.

We should remind you that a bracket sequence is called regular, if by inserting «+» and «1» into it we can get a correct mathematical expression. For example, sequences «(())()», «()» and «(()(()))» are regular, while «)(», «(()» and «(()))(» are not.

You are given a string of «(» and «)» characters. You are to find its longest substring that is a regular bracket sequence. You are to find the number of such substrings as well.

The first line of the input file contains a non-empty string, consisting of «(» and «)» characters. Its length does not exceed 106.

Print the length of the longest substring that is a regular bracket sequence, and the number of such substrings. If there are no such substrings, write the only line containing "0 1".

## Input

The first line of the input file contains a non-empty string, consisting of «(» and «)» characters. Its length does not exceed 106.

## Output

Print the length of the longest substring that is a regular bracket sequence, and the number of such substrings. If there are no such substrings, write the only line containing "0 1".

## Samples

```
)((())))(()())

```

```
6 2

```

```
))(

```

```
0 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-5C |
| Contest | 5 |
| Index | C |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`data structures`、`dp`、`greedy`、`sortings`、`strings` |
| 镜像标签 | `constructive algorithms`、`data structures`、`dp`、`greedy`、`sortings`、`strings`、`*1900` |
| Codeforces 通过次数 | 17383 |
| 镜像尝试 / 通过 | 5 / 2 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/5/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/5/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P5C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

