# CF-32E Hide-and-Seek

## 题面快照

## Description

Victor and Peter are playing hide-and-seek. Peter has hidden, and Victor is to find him. In the room where they are playing, there is only one non-transparent wall and one double-sided mirror. Victor and Peter are points with coordinates (xv, yv) and (xp, yp) respectively. The wall is a segment joining points with coordinates (xw, 1, yw, 1) and (xw, 2, yw, 2), the mirror — a segment joining points (xm, 1, ym, 1) and (xm, 2, ym, 2).

If an obstacle has a common point with a line of vision, it's considered, that the boys can't see each other with this line of vision. If the mirror has a common point with the line of vision, it's considered, that the boys can see each other in the mirror, i.e. reflection takes place. The reflection process is governed by laws of physics — the angle of incidence is equal to the angle of reflection. The incident ray is in the same half-plane as the reflected ray, relative to the mirror. I.e. to see each other Victor and Peter should be to the same side of the line, containing the mirror (see example 1). If the line of vision is parallel to the mirror, reflection doesn't take place, and the mirror isn't regarded as an obstacle (see example 4).

Victor got interested if he can see Peter, while standing at the same spot. Help him solve this problem.

The first line contains two numbers xv and yv — coordinates of Victor.

The second line contains two numbers xp and yp — coordinates of Peter.

The third line contains 4 numbers xw, 1, yw, 1, xw, 2, yw, 2 — coordinates of the wall.

The forth line contains 4 numbers xm, 1, ym, 1, xm, 2, ym, 2 — coordinates of the mirror.

All the coordinates are integer numbers, and don't exceed 104 in absolute value. It's guaranteed, that the segments don't have common points, Victor and Peter are not on any of the segments, coordinates of Victor and Peter aren't the same, the segments don't degenerate into points.

Output YES, if Victor can see Peter without leaving the initial spot. Otherwise output NO.

## Input

The first line contains two numbers xv and yv — coordinates of Victor.

The second line contains two numbers xp and yp — coordinates of Peter.

The third line contains 4 numbers xw, 1, yw, 1, xw, 2, yw, 2 — coordinates of the wall.

The forth line contains 4 numbers xm, 1, ym, 1, xm, 2, ym, 2 — coordinates of the mirror.

All the coordinates are integer numbers, and don't exceed 104 in absolute value. It's guaranteed, that the segments don't have common points, Victor and Peter are not on any of the segments, coordinates of Victor and Peter aren't the same, the segments don't degenerate into points.

## Output

Output YES, if Victor can see Peter without leaving the initial spot. Otherwise output NO.

## Samples

```
-1 3
1 3
0 2 0 4
0 0 0 1

```

```
NO

```

```
0 0
1 1
0 1 1 0
-100 -100 -101 -101

```

```
NO

```

```
0 0
1 1
0 1 1 0
-1 1 1 3

```

```
YES

```

```
0 0
10 0
100 100 101 101
1 0 3 0

```

```
YES

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-32E |
| Contest | 32 |
| Index | E |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `geometry`、`implementation` |
| 镜像标签 | `geometry`、`implementation`、`*2400` |
| Codeforces 通过次数 | 417 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/32/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/32/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P32E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

