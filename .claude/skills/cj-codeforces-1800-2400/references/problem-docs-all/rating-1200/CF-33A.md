# CF-33A What is for dinner?

## 题面快照

## Description

In one little known, but very beautiful country called Waterland, lives a lovely shark Valerie. Like all the sharks, she has several rows of teeth, and feeds on crucians. One of Valerie's distinguishing features is that while eating one crucian she uses only one row of her teeth, the rest of the teeth are "relaxing".

For a long time our heroine had been searching the sea for crucians, but a great misfortune happened. Her teeth started to ache, and she had to see the local dentist, lobster Ashot. As a professional, Ashot quickly relieved Valerie from her toothache. Moreover, he managed to determine the cause of Valerie's developing caries (for what he was later nicknamed Cap).

It turned that Valerie eats too many crucians. To help Valerie avoid further reoccurrence of toothache, Ashot found for each Valerie's tooth its residual viability. Residual viability of a tooth is a value equal to the amount of crucians that Valerie can eat with this tooth. Every time Valerie eats a crucian, viability of all the teeth used for it will decrease by one. When the viability of at least one tooth becomes negative, the shark will have to see the dentist again.

Unhappy, Valerie came back home, where a portion of crucians was waiting for her. For sure, the shark couldn't say no to her favourite meal, but she had no desire to go back to the dentist. That's why she decided to eat the maximum amount of crucians from the portion but so that the viability of no tooth becomes negative.

As Valerie is not good at mathematics, she asked you to help her to find out the total amount of crucians that she can consume for dinner.

We should remind you that while eating one crucian Valerie uses exactly one row of teeth and the viability of each tooth from this row decreases by one.

The first line contains three integers n, m, k (1 ≤ m ≤ n ≤ 1000, 0 ≤ k ≤ 106) — total amount of Valerie's teeth, amount of tooth rows and amount of crucians in Valerie's portion for dinner. Then follow n lines, each containing two integers: r (1 ≤ r ≤ m) — index of the row, where belongs the corresponding tooth, and c (0 ≤ c ≤ 106) — its residual viability.

It's guaranteed that each tooth row has positive amount of teeth.

In the first line output the maximum amount of crucians that Valerie can consume for dinner.

## Input

The first line contains three integers n, m, k (1 ≤ m ≤ n ≤ 1000, 0 ≤ k ≤ 106) — total amount of Valerie's teeth, amount of tooth rows and amount of crucians in Valerie's portion for dinner. Then follow n lines, each containing two integers: r (1 ≤ r ≤ m) — index of the row, where belongs the corresponding tooth, and c (0 ≤ c ≤ 106) — its residual viability.

It's guaranteed that each tooth row has positive amount of teeth.

## Output

In the first line output the maximum amount of crucians that Valerie can consume for dinner.

## Samples

```
4 3 18
2 3
1 2
3 6
2 3

```

```
11

```

```
2 2 13
1 13
2 12

```

```
13

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-33A |
| Contest | 33 |
| Index | A |
| Rating | 1200 |
| Points | 500.0 |
| Codeforces 标签 | `greedy`、`implementation` |
| 镜像标签 | `greedy`、`implementation`、`*1200` |
| Codeforces 通过次数 | 4772 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/33/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/33/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P33A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

