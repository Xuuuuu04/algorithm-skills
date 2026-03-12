# CF-42A Guilty --- to the kitchen!

## 题面快照

## Description

It's a very unfortunate day for Volodya today. He got bad mark in algebra and was therefore forced to do some work in the kitchen, namely to cook borscht (traditional Russian soup). This should also improve his algebra skills.

According to the borscht recipe it consists of n ingredients that have to be mixed in proportion  litres (thus, there should be a1 ·x, ..., an ·x litres of corresponding ingredients mixed for some non-negative x). In the kitchen Volodya found out that he has b1, ..., bn litres of these ingredients at his disposal correspondingly. In order to correct his algebra mistakes he ought to cook as much soup as possible in a V litres volume pan (which means the amount of soup cooked can be between 0 and V litres). What is the volume of borscht Volodya will cook ultimately?

The first line of the input contains two space-separated integers n and V (1 ≤ n ≤ 20, 1 ≤ V ≤ 10000). The next line contains n space-separated integers ai (1 ≤ ai ≤ 100). Finally, the last line contains n space-separated integers bi (0 ≤ bi ≤ 100).

Your program should output just one real number — the volume of soup that Volodya will cook. Your answer must have a relative or absolute error less than 10 - 4.

## Input

The first line of the input contains two space-separated integers n and V (1 ≤ n ≤ 20, 1 ≤ V ≤ 10000). The next line contains n space-separated integers ai (1 ≤ ai ≤ 100). Finally, the last line contains n space-separated integers bi (0 ≤ bi ≤ 100).

## Output

Your program should output just one real number — the volume of soup that Volodya will cook. Your answer must have a relative or absolute error less than 10 - 4.

## Samples

```
1 100
1
40

```

```
40.0

```

```
2 100
1 1
25 30

```

```
50.0

```

```
2 100
1 1
60 60

```

```
100.0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-42A |
| Contest | 42 |
| Index | A |
| Rating | 1400 |
| Points | 500.0 |
| Codeforces 标签 | `greedy`、`implementation` |
| 镜像标签 | `greedy`、`implementation`、`*1400` |
| Codeforces 通过次数 | 3141 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/42/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/42/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P42A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

