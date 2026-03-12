# CF-45H Road Problem

## 题面快照

## Description

The Berland capital (as you very well know) contains n junctions, some pairs of which are connected by two-way roads. Unfortunately, the number of traffic jams in the capital has increased dramatically, that's why it was decided to build several new roads. Every road should connect two junctions.

The city administration noticed that in the cities of all the developed countries between any two roads one can drive along at least two paths so that the paths don't share any roads (but they may share the same junction). The administration decided to add the minimal number of roads so that this rules was fulfilled in the Berland capital as well. In the city road network should exist no more than one road between every pair of junctions before or after the reform.

The first input line contains a pair of integers n, m (2 ≤ n ≤ 900, 1 ≤ m ≤ 100000), where n is the number of junctions and m is the number of roads. Each of the following m lines contains a description of a road that is given by the numbers of the connected junctions ai, bi (1 ≤ ai, bi ≤ n, ai ≠ bi). The junctions are numbered from 1 to n. It is possible to reach any junction of the city from any other one moving along roads.

On the first line print t — the number of added roads. Then on t lines print the descriptions of the added roads in the format of the input data. You can use any order of printing the roads themselves as well as the junctions linked by every road. If there are several solutions to that problem, print any of them.

If the capital doesn't need the reform, print the single number 0.

If there's no solution, print the single number -1.

## Input

The first input line contains a pair of integers n, m (2 ≤ n ≤ 900, 1 ≤ m ≤ 100000), where n is the number of junctions and m is the number of roads. Each of the following m lines contains a description of a road that is given by the numbers of the connected junctions ai, bi (1 ≤ ai, bi ≤ n, ai ≠ bi). The junctions are numbered from 1 to n. It is possible to reach any junction of the city from any other one moving along roads.

## Output

On the first line print t — the number of added roads. Then on t lines print the descriptions of the added roads in the format of the input data. You can use any order of printing the roads themselves as well as the junctions linked by every road. If there are several solutions to that problem, print any of them.

If the capital doesn't need the reform, print the single number 0.

If there's no solution, print the single number -1.

## Samples

```
4 3
1 2
2 3
3 4

```

```
1
1 4

```

```
4 4
1 2
2 3
2 4
3 4

```

```
1
1 3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-45H |
| Contest | 45 |
| Index | H |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `graphs` |
| 镜像标签 | `graphs`、`*2100` |
| Codeforces 通过次数 | 225 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/45/H)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/45/problem/H)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P45H)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

