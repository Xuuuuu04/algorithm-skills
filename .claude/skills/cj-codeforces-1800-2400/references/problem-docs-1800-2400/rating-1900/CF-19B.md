# CF-19B Checkout Assistant

## 题面快照

## Description

Bob came to a cash & carry store, put n items into his trolley, and went to the checkout counter to pay. Each item is described by its price ci and time ti in seconds that a checkout assistant spends on this item. While the checkout assistant is occupied with some item, Bob can steal some other items from his trolley. To steal one item Bob needs exactly 1 second. What is the minimum amount of money that Bob will have to pay to the checkout assistant? Remember, please, that it is Bob, who determines the order of items for the checkout assistant.

The first input line contains number n (1 ≤ n ≤ 2000). In each of the following n lines each item is described by a pair of numbers ti, ci (0 ≤ ti ≤ 2000, 1 ≤ ci ≤ 109). If ti is 0, Bob won't be able to steal anything, while the checkout assistant is occupied with item i.

Output one number — answer to the problem: what is the minimum amount of money that Bob will have to pay.

## Input

The first input line contains number n (1 ≤ n ≤ 2000). In each of the following n lines each item is described by a pair of numbers ti, ci (0 ≤ ti ≤ 2000, 1 ≤ ci ≤ 109). If ti is 0, Bob won't be able to steal anything, while the checkout assistant is occupied with item i.

## Output

Output one number — answer to the problem: what is the minimum amount of money that Bob will have to pay.

## Samples

```
4
2 10
0 20
1 5
1 3

```

```
8

```

```
3
0 1
0 10
0 100

```

```
111

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-19B |
| Contest | 19 |
| Index | B |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `dp` |
| 镜像标签 | `dp`、`*1900` |
| Codeforces 通过次数 | 5681 |
| 镜像尝试 / 通过 | 4 / 1 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/19/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/19/problem/B)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P19B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

