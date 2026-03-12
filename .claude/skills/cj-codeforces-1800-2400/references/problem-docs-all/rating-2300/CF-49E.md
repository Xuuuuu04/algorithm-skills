# CF-49E Common ancestor

## 题面快照

## Description

The DNA sequence for every living creature in Berland can be represented as a non-empty line consisting of lowercase Latin letters. Berland scientists found out that all the creatures evolve by stages. During one stage exactly one symbol of the DNA line is replaced by exactly two other ones. At that overall there are n permissible substitutions. The substitution ai->bici means that any one symbol ai can be replaced with two symbols bici. Every substitution could happen an unlimited number of times.

They say that two creatures with DNA sequences s1 and s2 can have a common ancestor if there exists such a DNA sequence s3 that throughout evolution it can result in s1 and s2, perhaps after a different number of stages. Your task is to find out by the given s1 and s2 whether the creatures possessing such DNA sequences can have a common ancestor. If the answer is positive, you have to find the length of the shortest sequence of the common ancestor’s DNA.

The first line contains a non-empty DNA sequence s1, the second line contains a non-empty DNA sequence s2. The lengths of these lines do not exceed 50, the lines contain only lowercase Latin letters. The third line contains an integer n (0 ≤ n ≤ 50) — the number of permissible substitutions. Then follow n lines each of which describes a substitution in the format ai->bici. The characters ai, bi, and ci are lowercase Latin letters. Lines s1 and s2 can coincide, the list of substitutions can contain similar substitutions.

If s1 and s2 cannot have a common ancestor, print -1. Otherwise print the length of the shortest sequence s3, from which s1 and s2 could have evolved.

## Input

The first line contains a non-empty DNA sequence s1, the second line contains a non-empty DNA sequence s2. The lengths of these lines do not exceed 50, the lines contain only lowercase Latin letters. The third line contains an integer n (0 ≤ n ≤ 50) — the number of permissible substitutions. Then follow n lines each of which describes a substitution in the format ai->bici. The characters ai, bi, and ci are lowercase Latin letters. Lines s1 and s2 can coincide, the list of substitutions can contain similar substitutions.

## Output

If s1 and s2 cannot have a common ancestor, print -1. Otherwise print the length of the shortest sequence s3, from which s1 and s2 could have evolved.

## Samples

```
ababa
aba
2
c->ba
c->cc

```

```
2

```

```
ababa
aba
7
c->ba
c->cc
e->ab
z->ea
b->ba
d->dd
d->ab

```

```
1

```

```
ababa
aba
1
c->ba

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-49E |
| Contest | 49 |
| Index | E |
| Rating | 2300 |
| Points | 2500.0 |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*2300` |
| Codeforces 通过次数 | 789 |
| 镜像尝试 / 通过 | 1 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/49/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/49/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P49E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

