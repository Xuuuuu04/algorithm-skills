# CF-43D Journey

## 题面快照

## Description

The territory of Berland is represented by a rectangular field n × m in size. The king of Berland lives in the capital, located on the upper left square (1, 1). The lower right square has coordinates (n, m). One day the king decided to travel through the whole country and return back to the capital, having visited every square (except the capital) exactly one time. The king must visit the capital exactly two times, at the very beginning and at the very end of his journey. The king can only move to the side-neighboring squares. However, the royal advise said that the King possibly will not be able to do it. But there is a way out — one can build the system of one way teleporters between some squares so that the king could fulfill his plan. No more than one teleporter can be installed on one square, every teleporter can be used any number of times, however every time it is used, it transports to the same given for any single teleporter square. When the king reaches a square with an installed teleporter he chooses himself whether he is or is not going to use the teleport. What minimum number of teleporters should be installed for the king to complete the journey? You should also compose the journey path route for the king.

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 100, 2 ≤ n·m) — the field size. The upper left square has coordinates (1, 1), and the lower right square has coordinates of (n, m).

On the first line output integer k — the minimum number of teleporters. Then output k lines each containing 4 integers x1y1x2y2 (1 ≤ x1, x2 ≤ n, 1 ≤ y1, y2 ≤ m) — the coordinates of the square where the teleporter is installed (x1, y1), and the coordinates of the square where the teleporter leads (x2, y2).

Then print nm + 1 lines containing 2 numbers each — the coordinates of the squares in the order in which they are visited by the king. The travel path must start and end at (1, 1). The king can move to side-neighboring squares and to the squares where a teleporter leads. Besides, he also should visit the capital exactly two times and he should visit other squares exactly one time.

## Input

The first line contains two space-separated integers n and m (1 ≤ n, m ≤ 100, 2 ≤ n·m) — the field size. The upper left square has coordinates (1, 1), and the lower right square has coordinates of (n, m).

## Output

On the first line output integer k — the minimum number of teleporters. Then output k lines each containing 4 integers x1y1x2y2 (1 ≤ x1, x2 ≤ n, 1 ≤ y1, y2 ≤ m) — the coordinates of the square where the teleporter is installed (x1, y1), and the coordinates of the square where the teleporter leads (x2, y2).

Then print nm + 1 lines containing 2 numbers each — the coordinates of the squares in the order in which they are visited by the king. The travel path must start and end at (1, 1). The king can move to side-neighboring squares and to the squares where a teleporter leads. Besides, he also should visit the capital exactly two times and he should visit other squares exactly one time.

## Samples

```
2 2

```

```
0
1 1
1 2
2 2
2 1
1 1

```

```
3 3

```

```
1
3 3 1 1
1 1
1 2
1 3
2 3
2 2
2 1
3 1
3 2
3 3
1 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-43D |
| Contest | 43 |
| Index | D |
| Rating | 2000 |
| Points | 2000.0 |
| Codeforces 标签 | `brute force`、`constructive algorithms`、`implementation` |
| 镜像标签 | `brute force`、`constructive algorithms`、`implementation`、`*2000` |
| Codeforces 通过次数 | 1209 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/43/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/43/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P43D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

