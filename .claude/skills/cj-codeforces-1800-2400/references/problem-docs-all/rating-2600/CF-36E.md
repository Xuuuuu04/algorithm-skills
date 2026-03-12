# CF-36E Two Paths

## 题面快照

## Description

Once archaeologists found m mysterious papers, each of which had a pair of integers written on them. Ancient people were known to like writing down the indexes of the roads they walked along, as «ab» or «ba», where a, b are the indexes of two different cities joint by the road . It is also known that the mysterious papers are pages of two travel journals (those days a new journal was written for every new journey).

During one journey the traveler could walk along one and the same road several times in one or several directions but in that case he wrote a new entry for each time in his journal. Besides, the archaeologists think that the direction the traveler took on a road had no effect upon the entry: the entry that looks like «ab» could refer to the road from a to b as well as to the road from b to a.

The archaeologists want to put the pages in the right order and reconstruct the two travel paths but unfortunately, they are bad at programming. That’s where you come in. Go help them!

The first input line contains integer m (1 ≤ m ≤ 10000). Each of the following m lines describes one paper. Each description consists of two integers a, b (1 ≤ a, b ≤ 10000, a ≠ b).

In the first line output the number L1. That is the length of the first path, i.e. the amount of papers in its description. In the following line output L1 space-separated numbers — the indexes of the papers that describe the first path. In the third and fourth lines output similarly the length of the second path L2 and the path itself. Both paths must contain at least one road, i.e. condition L1 > 0 and L2 > 0 must be met. The papers are numbered from 1 to m according to the order of their appearance in the input file. The numbers should be output in the order in which the traveler passed the corresponding roads. If the answer is not unique, output any.

If it’s impossible to find such two paths, output «-1».

Don’t forget that each paper should be used exactly once, i.e L1 + L2 = m.

## Input

The first input line contains integer m (1 ≤ m ≤ 10000). Each of the following m lines describes one paper. Each description consists of two integers a, b (1 ≤ a, b ≤ 10000, a ≠ b).

## Output

In the first line output the number L1. That is the length of the first path, i.e. the amount of papers in its description. In the following line output L1 space-separated numbers — the indexes of the papers that describe the first path. In the third and fourth lines output similarly the length of the second path L2 and the path itself. Both paths must contain at least one road, i.e. condition L1 > 0 and L2 > 0 must be met. The papers are numbered from 1 to m according to the order of their appearance in the input file. The numbers should be output in the order in which the traveler passed the corresponding roads. If the answer is not unique, output any.

If it’s impossible to find such two paths, output «-1».

Don’t forget that each paper should be used exactly once, i.e L1 + L2 = m.

## Samples

```
2
4 5
4 3

```

```
1
2
1
1

```

```
1
1 2

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-36E |
| Contest | 36 |
| Index | E |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `constructive algorithms`、`dsu`、`graphs`、`implementation` |
| 镜像标签 | `constructive algorithms`、`dsu`、`graphs`、`implementation`、`*2600` |
| Codeforces 通过次数 | 593 |
| 镜像尝试 / 通过 | 3 / 1 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/36/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/36/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P36E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

