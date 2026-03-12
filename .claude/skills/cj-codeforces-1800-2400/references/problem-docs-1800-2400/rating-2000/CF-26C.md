# CF-26C Parquet

## 题面快照

## Description

Once Bob decided to lay a parquet floor in his living room. The living room is of size n × m metres. Bob had planks of three types: a planks 1 × 2 meters, b planks 2 × 1 meters, and c planks 2 × 2 meters. Help Bob find out, if it is possible to parquet the living room with such a set of planks, and if it is possible, find one of the possible ways to do so. Bob doesn't have to use all the planks.

The first input line contains 5 space-separated integer numbers n, m, a, b, c (1 ≤ n, m ≤ 100, 0 ≤ a, b, c ≤ 104), n and m — the living room dimensions, a, b and c — amount of planks 1 × 2, 2 × 1 и 2 × 2 respectively. It's not allowed to turn the planks.

If it is not possible to parquet the room with such a set of planks, output IMPOSSIBLE. Otherwise output one of the possible ways to parquet the room — output n lines with m lower-case Latin letters each. Two squares with common sides should contain the same letters, if they belong to one and the same plank, and different letters otherwise. Different planks can be marked with one and the same letter (see examples). If the answer is not unique, output any.

## Input

The first input line contains 5 space-separated integer numbers n, m, a, b, c (1 ≤ n, m ≤ 100, 0 ≤ a, b, c ≤ 104), n and m — the living room dimensions, a, b and c — amount of planks 1 × 2, 2 × 1 и 2 × 2 respectively. It's not allowed to turn the planks.

## Output

If it is not possible to parquet the room with such a set of planks, output IMPOSSIBLE. Otherwise output one of the possible ways to parquet the room — output n lines with m lower-case Latin letters each. Two squares with common sides should contain the same letters, if they belong to one and the same plank, and different letters otherwise. Different planks can be marked with one and the same letter (see examples). If the answer is not unique, output any.

## Samples

```
2 6 2 2 1

```

```
aabcca
aabdda

```

```
1 1 100 100 100

```

```
IMPOSSIBLE

```

```
4 4 10 10 10

```

```
aabb
aabb
bbaa
bbaa

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-26C |
| Contest | 26 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `combinatorics`、`constructive algorithms`、`greedy`、`implementation` |
| 镜像标签 | `combinatorics`、`constructive algorithms`、`greedy`、`implementation`、`*2000` |
| Codeforces 通过次数 | 1003 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/26/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/26/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P26C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

