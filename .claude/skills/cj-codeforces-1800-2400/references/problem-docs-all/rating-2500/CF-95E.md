# CF-95E Lucky Country

## 题面快照

## Description

Petya loves lucky numbers. Everybody knows that positive integers are lucky if their decimal representation doesn't contain digits other than 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

One night Petya was sleeping. He was dreaming of being the president of some island country. The country is represented by islands connected by two-way roads. Between some islands there is no road way, even through other islands, that's why the country is divided into several regions. More formally, each island belongs to exactly one region, there is a path between any two islands located in the same region; there is no path between any two islands from different regions. A region is lucky if the amount of islands in it is a lucky number.

As a real president, Petya first decided to build a presidential palace. Being a lucky numbers' fan, Petya wants to position his palace in one of the lucky regions. However, it is possible that initially the country has no such regions. In this case Petya can build additional roads between different regions, thus joining them. Find the minimum number of roads needed to build to create a lucky region.

The first line contains two integers n and m (1 ≤ n, m ≤ 105). They are the number of islands and the number of roads correspondingly. Next m lines contain road descriptions. Each road is defined by the numbers of islands that it connects: that is, by two integers u and v (1 ≤ u, v ≤ n). Some roads can connect an island with itself; there can be more than one road between a pair of islands. Numbers in each line are separated by exactly one space character.

If there's no solution, output the only number "-1" (without the quotes). Otherwise, output the minimum number of roads r that need to be built to get a lucky region.

## Input

The first line contains two integers n and m (1 ≤ n, m ≤ 105). They are the number of islands and the number of roads correspondingly. Next m lines contain road descriptions. Each road is defined by the numbers of islands that it connects: that is, by two integers u and v (1 ≤ u, v ≤ n). Some roads can connect an island with itself; there can be more than one road between a pair of islands. Numbers in each line are separated by exactly one space character.

## Output

If there's no solution, output the only number "-1" (without the quotes). Otherwise, output the minimum number of roads r that need to be built to get a lucky region.

## Samples

```
4 3
1 2
2 3
1 3

```

```
1

```

```
5 4
1 2
3 4
4 5
3 5

```

```
-1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-95E |
| Contest | 95 |
| Index | E |
| Rating | 2500 |
| Points | 2500.0 |
| Codeforces 标签 | `dp`、`dsu`、`graphs` |
| 镜像标签 | `dp`、`dsu`、`graphs`、`*2500` |
| Codeforces 通过次数 | 1827 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/95/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/95/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P95E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

