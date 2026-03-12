# CF-54E Vacuum Сleaner

## 题面快照

## Description

One winter evening the Hedgehog was relaxing at home in his cozy armchair and clicking through the TV channels. Stumbled on an issue of «TopShop», the Hedgehog was about to change the channel when all of a sudden he was stopped by an advertisement of a new wondrous invention.

Actually, a vacuum cleaner was advertised there. It was called Marvellous Vacuum and it doesn't even need a human to operate it while it cleans! The vacuum cleaner can move around the flat on its own: it moves in some direction and if it hits an obstacle there, it automatically chooses a new direction. Sooner or later this vacuum cleaner will travel through all the room and clean it all. Having remembered how much time the Hedgehog spends every time on cleaning (surely, no less than a half of the day), he got eager to buy this wonder.

However, the Hedgehog quickly understood that the cleaner has at least one weak point: it won't clean well in the room's corners because it often won't able to reach the corner due to its shape. To estimate how serious is this drawback in practice, the Hedgehog asked you to write for him the corresponding program.

You will be given the cleaner's shape in the top view. We will consider only the cases when the vacuum cleaner is represented as a convex polygon. The room is some infinitely large rectangle. We consider one corner of this room and want to find such a rotation of the vacuum cleaner so that it, being pushed into this corner, will leave the minimum possible area in the corner uncovered.

The first line contains an integer N which represents the number of vertices of the vacuum cleaner's polygon (3 ≤ N ≤ 4·104). Then follow N lines each containing two numbers — the coordinates of a vertex of the polygon. All the coordinates are integer and their absolute values do not exceed 106.

It is guaranteed that the given polygon is nondegenerate and convex (no three points lie on the same line). The polygon vertices are given in a clockwise or counter-clockwise direction.

Print the minimum possible uncovered area. The answer will be accepted if it is within 10 - 6 of absolute or relative error from the correct answer.

## Input

The first line contains an integer N which represents the number of vertices of the vacuum cleaner's polygon (3 ≤ N ≤ 4·104). Then follow N lines each containing two numbers — the coordinates of a vertex of the polygon. All the coordinates are integer and their absolute values do not exceed 106.

It is guaranteed that the given polygon is nondegenerate and convex (no three points lie on the same line). The polygon vertices are given in a clockwise or counter-clockwise direction.

## Output

Print the minimum possible uncovered area. The answer will be accepted if it is within 10 - 6 of absolute or relative error from the correct answer.

## Samples

```
4
0 0
1 0
1 1
0 1

```

```
0.00000000000000000000

```

```
8
1 2
2 1
2 -1
1 -2
-1 -2
-2 -1
-2 1
-1 2

```

```
0.50000000000000000000

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-54E |
| Contest | 54 |
| Index | E |
| Rating | 2700 |
| Points | 2500.0 |
| Codeforces 标签 | `geometry` |
| 镜像标签 | `geometry`、`*2700` |
| Codeforces 通过次数 | 213 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/54/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/54/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P54E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

