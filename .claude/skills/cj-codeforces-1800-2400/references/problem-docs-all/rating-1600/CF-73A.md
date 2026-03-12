# CF-73A The Elder Trolls IV: Oblivon

## 题面快照

## Description

Vasya plays The Elder Trolls IV: Oblivon. Oh, those creators of computer games! What they do not come up with! Absolutely unique monsters have been added to the The Elder Trolls IV: Oblivon. One of these monsters is Unkillable Slug. Why it is "Unkillable"? Firstly, because it can be killed with cutting weapon only, so lovers of two-handed amber hammers should find suitable knife themselves. Secondly, it is necessary to make so many cutting strokes to Unkillable Slug. Extremely many. Too many!

Vasya has already promoted his character to 80-th level and in order to gain level 81 he was asked to kill Unkillable Slug. The monster has a very interesting shape. It looks like a rectangular parallelepiped with size x × y × z, consisting of undestructable cells 1 × 1 × 1. At one stroke Vasya can cut the Slug along an imaginary grid, i.e. cut with a plane parallel to one of the parallelepiped side. Monster dies when amount of parts it is divided reaches some critical value.

All parts of monster do not fall after each cut, they remains exactly on its places. I. e. Vasya can cut several parts with one cut.

Vasya wants to know what the maximum number of pieces he can cut the Unkillable Slug into striking him at most k times.

Vasya's character uses absolutely thin sword with infinite length.

The first line of input contains four integer numbers x, y, z, k (1 ≤ x, y, z ≤ 106, 0 ≤ k ≤ 109).

Output the only number — the answer for the problem.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

## Input

The first line of input contains four integer numbers x, y, z, k (1 ≤ x, y, z ≤ 106, 0 ≤ k ≤ 109).

## Output

Output the only number — the answer for the problem.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cout (also you may use %I64d).

## Samples

```
2 2 2 3

```

```
8

```

```
2 2 2 1

```

```
2

```

## Note

In the first sample Vasya make 3 pairwise perpendicular cuts. He cuts monster on two parts with the first cut, then he divides each part on two with the second cut, and finally he divides each of the 4 parts on two.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-73A |
| Contest | 73 |
| Index | A |
| Rating | 1600 |
| Points | 500.0 |
| Codeforces 标签 | `greedy`、`math` |
| 镜像标签 | `greedy`、`math`、`*1600` |
| Codeforces 通过次数 | 1620 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/73/A)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/73/problem/A)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P73A)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

