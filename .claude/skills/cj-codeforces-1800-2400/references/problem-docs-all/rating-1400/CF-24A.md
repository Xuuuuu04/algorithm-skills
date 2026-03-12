# CF-24A Ring road

## 题面快照

## Description

Nowadays the one-way traffic is introduced all over the world in order to improve driving safety and reduce traffic jams. The government of Berland decided to keep up with new trends. Formerly all n cities of Berland were connected by n two-way roads in the ring, i. e. each city was connected directly to exactly two other cities, and from each city it was possible to get to any other city. Government of Berland introduced one-way traffic on all n roads, but it soon became clear that it's impossible to get from some of the cities to some others. Now for each road is known in which direction the traffic is directed at it, and the cost of redirecting the traffic. What is the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other?

The first line contains integer n (3 ≤ n ≤ 100) — amount of cities (and roads) in Berland. Next n lines contain description of roads. Each road is described by three integers ai, bi, ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 100) — road is directed from city ai to city bi, redirecting the traffic costs ci.

Output single integer — the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other.

## Input

The first line contains integer n (3 ≤ n ≤ 100) — amount of cities (and roads) in Berland. Next n lines contain description of roads. Each road is described by three integers ai, bi, ci (1 ≤ ai, bi ≤ n, ai ≠ bi, 1 ≤ ci ≤ 100) — road is directed from city ai to city bi, redirecting the traffic costs ci.

## Output

Output single integer — the smallest amount of money the government should spend on the redirecting of roads so that from every city you can get to any other.

## Samples

```
3
1 3 1
1 2 1
3 2 1

```

```
1

```

```
3
1 3 1
1 2 5
3 2 1

```

```
2

```

```
6
1 5 4
5 3 8
2 4 15
1 6 16
2 3 23
4 6 42

```

```
39

```

```
4
1 2 9
2 3 8
3 4 7
4 1 5

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-24A |
| Contest | 24 |
| Index | A |
| Rating | 1400 |
| Points | - |
| Codeforces 标签 | `graphs` |
| 镜像标签 | `graphs`、`*1400` |
| Codeforces 通过次数 | 6696 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/24/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/24/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P24A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

