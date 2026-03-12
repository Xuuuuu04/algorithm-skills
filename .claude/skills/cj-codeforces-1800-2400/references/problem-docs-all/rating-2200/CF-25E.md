# CF-25E Test

## 题面快照

## Description

Sometimes it is hard to prepare tests for programming problems. Now Bob is preparing tests to new problem about strings — input data to his problem is one string. Bob has 3 wrong solutions to this problem. The first gives the wrong answer if the input data contains the substring s1, the second enters an infinite loop if the input data contains the substring s2, and the third requires too much memory if the input data contains the substring s3. Bob wants these solutions to fail single test. What is the minimal length of test, which couldn't be passed by all three Bob's solutions?

There are exactly 3 lines in the input data. The i-th line contains string si. All the strings are non-empty, consists of lowercase Latin letters, the length of each string doesn't exceed 105.

Output one number — what is minimal length of the string, containing s1, s2 and s3 as substrings.

## Input

There are exactly 3 lines in the input data. The i-th line contains string si. All the strings are non-empty, consists of lowercase Latin letters, the length of each string doesn't exceed 105.

## Output

Output one number — what is minimal length of the string, containing s1, s2 and s3 as substrings.

## Samples

```
ab
bc
cd

```

```
4

```

```
abacaba
abaaba
x

```

```
11

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-25E |
| Contest | 25 |
| Index | E |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `hashing`、`strings` |
| 镜像标签 | `hashing`、`strings`、`*2200` |
| Codeforces 通过次数 | 3087 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/25/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/25/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P25E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

