# CF-48F Snow sellers

## 题面快照

## Description

The New Year celebrations in Berland last n days. Only this year the winter is snowless, that’s why the winter celebrations’ organizers should buy artificial snow. There are m snow selling companies in Berland. Every day the i-th company produces wi cubic meters of snow. Next day the snow thaws and the company has to produce wi cubic meters of snow again. During the celebration new year discounts are on, that’s why the snow cost decreases every day. It is known that on the first day the total cost of all the snow produced by the i-th company is equal to ci bourles. Every day this total cost decreases by ai bourles, i.e. on the second day it is equal to ci - ai,and on the third day — to ci - 2ai, and so on. It is known that for one company the cost of the snow produced by it does not get negative or equal to zero. You have to organize the snow purchase so as to buy every day exactly W snow cubic meters. At that it is not necessary to buy from any company all the snow produced by it. If you buy ni cubic meters of snow (0 ≤ ni ≤ wi, the number ni is not necessarily integer!) from the i-th company at one of the days when the cost of its snow is equal to si, then its price will total to  bourles. During one day one can buy the snow from several companies. In different days one can buy the snow from different companies. It is required to make the purchases so as to spend as little money as possible. It is guaranteed that the snow produced by the companies will be enough.

The first line contains integers n, m and W (1 ≤ n ≤ 100, 1 ≤ m ≤ 500000, 1 ≤ W ≤ 109) which represent the number of days, the number of companies and the amount of snow that needs to be purchased on every one of the n days. The second line contains m integers wi. The third line contains m integers ci. The fourth line contains m integers ai. All the numbers are strictly positive and do not exceed 109. For all the i the inequation ci - (n - 1)ai > 0 holds true.

Print a single number — the answer to the given problem. Print the answer in the format with the decimal point (even if the answer is integer, it must contain the decimal point), without "e" and without leading zeroes. The answer should differ with the right one by no more than 10 - 9.

## Input

The first line contains integers n, m and W (1 ≤ n ≤ 100, 1 ≤ m ≤ 500000, 1 ≤ W ≤ 109) which represent the number of days, the number of companies and the amount of snow that needs to be purchased on every one of the n days. The second line contains m integers wi. The third line contains m integers ci. The fourth line contains m integers ai. All the numbers are strictly positive and do not exceed 109. For all the i the inequation ci - (n - 1)ai > 0 holds true.

## Output

Print a single number — the answer to the given problem. Print the answer in the format with the decimal point (even if the answer is integer, it must contain the decimal point), without "e" and without leading zeroes. The answer should differ with the right one by no more than 10 - 9.

## Samples

```
2 3 10
4 4 4
5 5 8
1 2 5

```

```
22.000000000000000

```

```
100 2 1000000000
999999998 999999999
1000000000 1000000000
1 1

```

```
99999995149.999995249999991

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-48F |
| Contest | 48 |
| Index | F |
| Rating | 2800 |
| Points | - |
| Codeforces 标签 | `greedy`、`sortings` |
| 镜像标签 | `greedy`、`sortings`、`*2800` |
| Codeforces 通过次数 | 189 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 10000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/48/F)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/48/problem/F)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P48F)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

