# CF-90B African Crossword

## 题面快照

## Description

An African crossword is a rectangular table n × m in size. Each cell of the table contains exactly one letter. This table (it is also referred to as grid) contains some encrypted word that needs to be decoded.

To solve the crossword you should cross out all repeated letters in rows and columns. In other words, a letter should only be crossed out if and only if the corresponding column or row contains at least one more letter that is exactly the same. Besides, all such letters are crossed out simultaneously.

When all repeated letters have been crossed out, we should write the remaining letters in a string. The letters that occupy a higher position follow before the letters that occupy a lower position. If the letters are located in one row, then the letter to the left goes first. The resulting word is the answer to the problem.

You are suggested to solve an African crossword and print the word encrypted there.

The first line contains two integers n and m (1 ≤ n, m ≤ 100). Next n lines contain m lowercase Latin letters each. That is the crossword grid.

Print the encrypted word on a single line. It is guaranteed that the answer consists of at least one letter.

## Input

The first line contains two integers n and m (1 ≤ n, m ≤ 100). Next n lines contain m lowercase Latin letters each. That is the crossword grid.

## Output

Print the encrypted word on a single line. It is guaranteed that the answer consists of at least one letter.

## Samples

```
3 3
cba
bcd
cbc

```

```
abcd

```

```
5 5
fcofd
ooedo
afaoa
rdcdf
eofsf

```

```
codeforces

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-90B |
| Contest | 90 |
| Index | B |
| Rating | 1100 |
| Points | 1000.0 |
| Codeforces 标签 | `implementation`、`strings` |
| 镜像标签 | `implementation`、`strings`、`*1100` |
| Codeforces 通过次数 | 5683 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/90/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/90/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P90B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

