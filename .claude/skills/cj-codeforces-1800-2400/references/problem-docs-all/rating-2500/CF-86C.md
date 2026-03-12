# CF-86C Genetic engineering

## 题面快照

## Description

"Multidimensional spaces are completely out of style these days, unlike genetics problems" — thought physicist Woll and changed his subject of study to bioinformatics. Analysing results of sequencing he faced the following problem concerning DNA sequences. We will further think of a DNA sequence as an arbitrary string of uppercase letters "A", "C", "G" and "T" (of course, this is a simplified interpretation).

Let w be a long DNA sequence and s1, s2, ..., sm — collection of short DNA sequences. Let us say that the collection filtersw iff w can be covered with the sequences from the collection. Certainly, substrings corresponding to the different positions of the string may intersect or even cover each other. More formally: denote by |w| the length of w, let symbols of w be numbered from 1 to |w|. Then for each position i in w there exist pair of indices l, r (1 ≤ l ≤ i ≤ r ≤ |w|) such that the substring w[l ... r] equals one of the elements s1, s2, ..., sm of the collection.

Woll wants to calculate the number of DNA sequences of a given length filtered by a given collection, but he doesn't know how to deal with it. Help him! Your task is to find the number of different DNA sequences of length n filtered by the collection {si}.

Answer may appear very large, so output it modulo 1000000009.

First line contains two integer numbers n and m (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10) — the length of the string and the number of sequences in the collection correspondently.

Next m lines contain the collection sequences si, one per line. Each si is a nonempty string of length not greater than 10. All the strings consist of uppercase letters "A", "C", "G", "T". The collection may contain identical strings.

Output should contain a single integer — the number of strings filtered by the collection modulo 1000000009 (109 + 9).

## Input

First line contains two integer numbers n and m (1 ≤ n ≤ 1000, 1 ≤ m ≤ 10) — the length of the string and the number of sequences in the collection correspondently.

Next m lines contain the collection sequences si, one per line. Each si is a nonempty string of length not greater than 10. All the strings consist of uppercase letters "A", "C", "G", "T". The collection may contain identical strings.

## Output

Output should contain a single integer — the number of strings filtered by the collection modulo 1000000009 (109 + 9).

## Samples

```
2 1
A

```

```
1

```

```
6 2
CAT
TACT

```

```
2

```

## Note

In the first sample, a string has to be filtered by "A". Clearly, there is only one such string: "AA".

In the second sample, there exist exactly two different strings satisfying the condition (see the pictures below).

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-86C |
| Contest | 86 |
| Index | C |
| Rating | 2500 |
| Points | 2000.0 |
| Codeforces 标签 | `dp`、`string suffix structures`、`trees` |
| 镜像标签 | `dp`、`string suffix structures`、`trees`、`*2500` |
| Codeforces 通过次数 | 850 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/86/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/86/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P86C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

