# CF-23D Tetragon

## 题面快照

## Description

You're given the centers of three equal sides of a strictly convex tetragon. Your task is to restore the initial tetragon.

The first input line contains one number T — amount of tests (1 ≤ T ≤ 5·104). Each of the following T lines contains numbers x1, y1, x2, y2, x3, y3 — coordinates of different points that are the centers of three equal sides (non-negative integer numbers, not exceeding 10).

For each test output two lines. If the required tetragon exists, output in the first line YES, in the second line — four pairs of numbers — coordinates of the polygon's vertices in clockwise or counter-clockwise order. Don't forget, please, that the tetragon should be strictly convex, i.e. no 3 of its points lie on one line. Output numbers with 9 characters after a decimal point.

If the required tetragon doen't exist, output NO in the first line, and leave the second line empty.

## Input

The first input line contains one number T — amount of tests (1 ≤ T ≤ 5·104). Each of the following T lines contains numbers x1, y1, x2, y2, x3, y3 — coordinates of different points that are the centers of three equal sides (non-negative integer numbers, not exceeding 10).

## Output

For each test output two lines. If the required tetragon exists, output in the first line YES, in the second line — four pairs of numbers — coordinates of the polygon's vertices in clockwise or counter-clockwise order. Don't forget, please, that the tetragon should be strictly convex, i.e. no 3 of its points lie on one line. Output numbers with 9 characters after a decimal point.

If the required tetragon doen't exist, output NO in the first line, and leave the second line empty.

## Samples

```
3
1 1 2 2 3 3
0 1 1 0 2 2
9 3 7 9 9 8

```

```
NO

YES
3.5 1.5 0.5 2.5 -0.5 -0.5 2.5 0.5
NO

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-23D |
| Contest | 23 |
| Index | D |
| Rating | 2600 |
| Points | - |
| Codeforces 标签 | `geometry`、`math` |
| 镜像标签 | `geometry`、`math`、`*2600` |
| Codeforces 通过次数 | 377 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/23/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/23/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P23D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

