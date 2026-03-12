# CF-42D Strange town

## 题面快照

## Description

Volodya has recently visited a very odd town. There are N tourist attractions in the town and every two of them are connected by a bidirectional road. Each road has some travel price (natural number) assigned to it and all prices are distinct. But the most striking thing about this town is that each city sightseeing tour has the same total price! That is, if we choose any city sightseeing tour — a cycle which visits every attraction exactly once — the sum of the costs of the tour roads is independent of the tour. Volodya is curious if you can find such price system with all road prices not greater than 1000.

Input contains just one natural number (3 ≤ N ≤ 20) — the number of town attractions.

Output should contain N rows containing N positive integer numbers each — the adjacency matrix of the prices graph (thus, j-th number in i-th row should be equal to the price of the road between the j-th and the i-th attraction). Diagonal numbers should be equal to zero. All numbers should not be greater than 1000. All prices should be positive and pairwise distinct. If there are several solutions, output any of them.

## Input

Input contains just one natural number (3 ≤ N ≤ 20) — the number of town attractions.

## Output

Output should contain N rows containing N positive integer numbers each — the adjacency matrix of the prices graph (thus, j-th number in i-th row should be equal to the price of the road between the j-th and the i-th attraction). Diagonal numbers should be equal to zero. All numbers should not be greater than 1000. All prices should be positive and pairwise distinct. If there are several solutions, output any of them.

## Samples

```
3

```

```
0 3 4
3 0 5
4 5 0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-42D |
| Contest | 42 |
| Index | D |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`math` |
| 镜像标签 | `constructive algorithms`、`math`、`*2300` |
| Codeforces 通过次数 | 477 |
| 镜像尝试 / 通过 | 4 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/42/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/42/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P42D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

