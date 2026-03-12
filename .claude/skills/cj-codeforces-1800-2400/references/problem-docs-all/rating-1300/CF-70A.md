# CF-70A Cookies

## 题面快照

## Description

Fangy collects cookies. Once he decided to take a box and put cookies into it in some way. If we take a square k × k in size, divided into blocks 1 × 1 in size and paint there the main diagonal together with cells, which lie above it, then the painted area will be equal to the area occupied by one cookie k in size. Fangy also has a box with a square base 2n × 2n, divided into blocks 1 × 1 in size. In a box the cookies should not overlap, and they should not be turned over or rotated. See cookies of sizes 2 and 4 respectively on the figure:

To stack the cookies the little walrus uses the following algorithm. He takes out of the repository the largest cookie which can fit in some place in the box and puts it there. Everything could be perfect but alas, in the repository the little walrus has infinitely many cookies of size 2 and larger, and there are no cookies of size 1, therefore, empty cells will remain in the box. Fangy wants to know how many empty cells will be left in the end.

The first line contains a single integer n (0 ≤ n ≤ 1000).

Print the single number, equal to the number of empty cells in the box. The answer should be printed modulo 106 + 3.

## Input

The first line contains a single integer n (0 ≤ n ≤ 1000).

## Output

Print the single number, equal to the number of empty cells in the box. The answer should be printed modulo 106 + 3.

## Samples

```
3

```

```
9

```

## Note

If the box possesses the base of 23 × 23 (as in the example), then the cookies will be put there in the following manner:

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-70A |
| Contest | 70 |
| Index | A |
| Rating | 1300 |
| Points | 500.0 |
| Codeforces 标签 | `math` |
| 镜像标签 | `math`、`*1300` |
| Codeforces 通过次数 | 3521 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/70/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/70/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P70A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

