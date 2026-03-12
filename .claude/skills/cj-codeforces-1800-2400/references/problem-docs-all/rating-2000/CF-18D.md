# CF-18D Seller Bob

## 题面快照

## Description

Last year Bob earned by selling memory sticks. During each of n days of his work one of the two following events took place:

-  A customer came to Bob and asked to sell him a 2x MB memory stick. If Bob had such a stick, he sold it and got 2x berllars.

-  Bob won some programming competition and got a 2x MB memory stick as a prize. Bob could choose whether to present this memory stick to one of his friends, or keep it.

Bob never kept more than one memory stick, as he feared to mix up their capacities, and deceive a customer unintentionally. It is also known that for each memory stick capacity there was at most one customer, who wanted to buy that memory stick. Now, knowing all the customers' demands and all the prizes won at programming competitions during the last n days, Bob wants to know, how much money he could have earned, if he had acted optimally.

The first input line contains number n (1 ≤ n ≤ 5000) — amount of Bob's working days. The following n lines contain the description of the days. Line sell x stands for a day when a customer came to Bob to buy a 2x MB memory stick (0 ≤ x ≤ 2000). It's guaranteed that for each x there is not more than one line sell x. Line win x stands for a day when Bob won a 2x MB memory stick (0 ≤ x ≤ 2000).

Output the maximum possible earnings for Bob in berllars, that he would have had if he had known all the events beforehand. Don't forget, please, that Bob can't keep more than one memory stick at a time.

## Input

The first input line contains number n (1 ≤ n ≤ 5000) — amount of Bob's working days. The following n lines contain the description of the days. Line sell x stands for a day when a customer came to Bob to buy a 2x MB memory stick (0 ≤ x ≤ 2000). It's guaranteed that for each x there is not more than one line sell x. Line win x stands for a day when Bob won a 2x MB memory stick (0 ≤ x ≤ 2000).

## Output

Output the maximum possible earnings for Bob in berllars, that he would have had if he had known all the events beforehand. Don't forget, please, that Bob can't keep more than one memory stick at a time.

## Samples

```
7
win 10
win 5
win 3
sell 5
sell 3
win 10
sell 10

```

```
1056

```

```
3
win 5
sell 6
sell 4

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-18D |
| Contest | 18 |
| Index | D |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `brute force`、`dp`、`greedy` |
| 镜像标签 | `brute force`、`dp`、`greedy`、`*2000` |
| Codeforces 通过次数 | 1273 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 128MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/18/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/18/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P18D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

