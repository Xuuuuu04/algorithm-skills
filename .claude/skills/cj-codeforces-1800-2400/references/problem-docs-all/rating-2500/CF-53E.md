# CF-53E Dead Ends

## 题面快照

## Description

Life in Bertown has become hard. The city has too many roads and the government spends too much to maintain them. There are n junctions and m two way roads, at which one can get from each junction to any other one. The mayor wants to close some roads so that the number of roads left totaled to n - 1 roads and it were still possible to get from each junction to any other one. Besides, the mayor is concerned with the number of dead ends which are the junctions from which only one road goes. There shouldn't be too many or too few junctions. Having discussed the problem, the mayor and his assistants decided that after the roads are closed, the road map should contain exactly k dead ends. Your task is to count the number of different ways of closing the roads at which the following conditions are met:

-  There are exactly n - 1 roads left.

-  It is possible to get from each junction to any other one.

-  There are exactly k dead ends on the resulting map.

Two ways are considered different if there is a road that is closed in the first way, and is open in the second one.

The first line contains three integers n, m and k (3 ≤ n ≤ 10, n - 1 ≤ m ≤ n·(n - 1) / 2, 2 ≤ k ≤ n - 1) which represent the number of junctions, roads and dead ends correspondingly. Then follow m lines each containing two different integers v1 and v2 (1 ≤ v1, v2 ≤ n, v1 ≠ v2) which represent the number of junctions connected by another road. There can be no more than one road between every pair of junctions. The junctions are numbered with integers from 1 to n. It is guaranteed that it is possible to get from each junction to any other one along the original roads.

Print a single number — the required number of ways.

## Input

The first line contains three integers n, m and k (3 ≤ n ≤ 10, n - 1 ≤ m ≤ n·(n - 1) / 2, 2 ≤ k ≤ n - 1) which represent the number of junctions, roads and dead ends correspondingly. Then follow m lines each containing two different integers v1 and v2 (1 ≤ v1, v2 ≤ n, v1 ≠ v2) which represent the number of junctions connected by another road. There can be no more than one road between every pair of junctions. The junctions are numbered with integers from 1 to n. It is guaranteed that it is possible to get from each junction to any other one along the original roads.

## Output

Print a single number — the required number of ways.

## Samples

```
3 3 2
1 2
2 3
1 3

```

```
3

```

```
4 6 2
1 2
2 3
3 4
4 1
1 3
2 4

```

```
12

```

```
4 6 3
1 2
2 3
3 4
4 1
1 3
2 4

```

```
4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-53E |
| Contest | 53 |
| Index | E |
| Rating | 2500 |
| Points | 2500.0 |
| Codeforces 标签 | `bitmasks`、`dp` |
| 镜像标签 | `bitmasks`、`dp`、`*2500` |
| Codeforces 通过次数 | 1243 |
| 镜像尝试 / 通过 | 2 / 2 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/53/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/53/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P53E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

