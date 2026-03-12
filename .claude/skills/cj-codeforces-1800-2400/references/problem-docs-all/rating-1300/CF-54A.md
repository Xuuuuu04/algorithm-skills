# CF-54A Presents

## 题面快照

## Description

The Hedgehog likes to give presents to his friend, but no less he likes to receive them.

Having received another present today, the Hedgehog suddenly understood that he has no place to put it as there was no room left on the special shelf in the cupboard. He will have to choose another shelf, but which one should he choose, how large should it be?

In order to get to know this, the Hedgehog asks you to write him a program that will count the estimated number of presents that he will receive during the following N days. Besides, he is guided by the principle:

-  on each holiday day the Hedgehog will necessarily receive a present,

-  he receives presents at least every K days (i.e., if he received a present on the i-th day, he will receive the next present no later than on the i + K-th day).

For the given N and K, as well as the list of holidays among the following N days count the minimal number of presents that could be given to the Hedgehog. The number of today's day is zero, and you should regard today's present as already given (i.e., you shouldn't count it in the answer).

The first line contains integers N and K (1 ≤ N ≤ 365, 1 ≤ K ≤ N).

The second line contains a number C which represents the number of holidays (0 ≤ C ≤ N). Then in the same line follow C numbers ranging from 1 to N which are the numbers of holiday days. The numbers are given in the increasing order, without repeating numbers among them.

Print a single number — the minimal number of presents the Hedgehog will receive over the following N days.

## Input

The first line contains integers N and K (1 ≤ N ≤ 365, 1 ≤ K ≤ N).

The second line contains a number C which represents the number of holidays (0 ≤ C ≤ N). Then in the same line follow C numbers ranging from 1 to N which are the numbers of holiday days. The numbers are given in the increasing order, without repeating numbers among them.

## Output

Print a single number — the minimal number of presents the Hedgehog will receive over the following N days.

## Samples

```
5 2
1 3

```

```
3

```

```
10 1
3 6 7 8

```

```
10

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-54A |
| Contest | 54 |
| Index | A |
| Rating | 1300 |
| Points | 500.0 |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1300` |
| Codeforces 通过次数 | 2506 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/54/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/54/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P54A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

