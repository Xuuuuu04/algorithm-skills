# CF-63D Dividing Island

## 题面快照

## Description

A revolution took place on the Buka Island. New government replaced the old one. The new government includes n parties and each of them is entitled to some part of the island according to their contribution to the revolution. However, they can't divide the island.

The island can be conventionally represented as two rectangles a × b and c × d unit squares in size correspondingly. The rectangles are located close to each other. At that, one of the sides with the length of a and one of the sides with the length of c lie on one line. You can see this in more details on the picture.

The i-th party is entitled to a part of the island equal to xi unit squares. Every such part should fully cover several squares of the island (it is not allowed to cover the squares partially) and be a connected figure. A "connected figure" presupposes that from any square of this party one can move to any other square of the same party moving through edge-adjacent squares also belonging to that party.

Your task is to divide the island between parties.

The first line contains 5 space-separated integers — a, b, c, d and n (1 ≤ a, b, c, d ≤ 50, b ≠ d, 1 ≤ n ≤ 26). The second line contains n space-separated numbers. The i-th of them is equal to number xi (1 ≤ xi ≤ a × b + c × d). It is guaranteed that .

If dividing the island between parties in the required manner is impossible, print "NO" (without the quotes). Otherwise, print "YES" (also without the quotes) and, starting from the next line, print max(b, d) lines each containing a + c characters. To mark what square should belong to what party, use lowercase Latin letters. For the party that is first in order in the input data, use "a", for the second one use "b" and so on. Use "." for the squares that belong to the sea. The first symbol of the second line of the output data should correspond to the square that belongs to the rectangle a × b. The last symbol of the second line should correspond to the square that belongs to the rectangle c × d.

If there are several solutions output any.

## Input

The first line contains 5 space-separated integers — a, b, c, d and n (1 ≤ a, b, c, d ≤ 50, b ≠ d, 1 ≤ n ≤ 26). The second line contains n space-separated numbers. The i-th of them is equal to number xi (1 ≤ xi ≤ a × b + c × d). It is guaranteed that .

## Output

If dividing the island between parties in the required manner is impossible, print "NO" (without the quotes). Otherwise, print "YES" (also without the quotes) and, starting from the next line, print max(b, d) lines each containing a + c characters. To mark what square should belong to what party, use lowercase Latin letters. For the party that is first in order in the input data, use "a", for the second one use "b" and so on. Use "." for the squares that belong to the sea. The first symbol of the second line of the output data should correspond to the square that belongs to the rectangle a × b. The last symbol of the second line should correspond to the square that belongs to the rectangle c × d.

If there are several solutions output any.

## Samples

```
3 4 2 2 3
5 8 3

```

```
YES
aaabb
aabbb
cbb..
ccb..

```

```
3 2 1 4 4
1 2 3 4

```

```
YES
abbd
cccd
...d
...d

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-63D |
| Contest | 63 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `constructive algorithms` |
| 镜像标签 | `constructive algorithms`、`*1900` |
| Codeforces 通过次数 | 1432 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/63/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/63/problem/D)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P63D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

