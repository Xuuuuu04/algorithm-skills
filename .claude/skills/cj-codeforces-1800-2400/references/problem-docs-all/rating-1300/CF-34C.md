# CF-34C Page Numbers

## 题面快照

## Description

«Bersoft» company is working on a new version of its most popular text editor — Bord 2010. Bord, like many other text editors, should be able to print out multipage documents. A user keys a sequence of the document page numbers that he wants to print out (separates them with a comma, without spaces).

Your task is to write a part of the program, responsible for «standardization» of this sequence. Your program gets the sequence, keyed by the user, as input. The program should output this sequence in format l1-r1,l2-r2,...,lk-rk, where ri + 1 < li + 1 for all i from 1 to k - 1, and li ≤ ri. The new sequence should contain all the page numbers, keyed by the user, and nothing else. If some page number appears in the input sequence several times, its appearances, starting from the second one, should be ignored. If for some element i from the new sequence li = ri, this element should be output as li, and not as «li - li».

For example, sequence 1,2,3,1,1,2,6,6,2 should be output as 1-3,6.

The only line contains the sequence, keyed by the user. The sequence contains at least one and at most 100 positive integer numbers. It's guaranteed, that this sequence consists of positive integer numbers, not exceeding 1000, separated with a comma, doesn't contain any other characters, apart from digits and commas, can't end with a comma, and the numbers don't contain leading zeroes. Also it doesn't start with a comma or contain more than one comma in a row.

Output the sequence in the required format.

## Input

The only line contains the sequence, keyed by the user. The sequence contains at least one and at most 100 positive integer numbers. It's guaranteed, that this sequence consists of positive integer numbers, not exceeding 1000, separated with a comma, doesn't contain any other characters, apart from digits and commas, can't end with a comma, and the numbers don't contain leading zeroes. Also it doesn't start with a comma or contain more than one comma in a row.

## Output

Output the sequence in the required format.

## Samples

```
1,2,3,1,1,2,6,6,2

```

```
1-3,6

```

```
3,2,1

```

```
1-3

```

```
30,20,10

```

```
10,20,30

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-34C |
| Contest | 34 |
| Index | C |
| Rating | 1300 |
| Points | 1500.0 |
| Codeforces 标签 | `expression parsing`、`implementation`、`sortings`、`strings` |
| 镜像标签 | `expression parsing`、`implementation`、`sortings`、`strings`、`*1300` |
| Codeforces 通过次数 | 4723 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/34/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/34/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P34C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

