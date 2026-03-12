# CF-47E Cannon

## 题面快照

## Description

Bertown is under siege! The attackers have blocked all the ways out and their cannon is bombarding the city. Fortunately, Berland intelligence managed to intercept the enemies' shooting plan. Let's introduce the Cartesian system of coordinates, the origin of which coincides with the cannon's position, the Ox axis is directed rightwards in the city's direction, the Oy axis is directed upwards (to the sky). The cannon will make n more shots. The cannon balls' initial speeds are the same in all the shots and are equal to V, so that every shot is characterized by only one number alphai which represents the angle at which the cannon fires. Due to the cannon's technical peculiarities this angle does not exceed 45 angles (π / 4). We disregard the cannon sizes and consider the firing made from the point (0, 0).

The balls fly according to the known physical laws of a body thrown towards the horizon at an angle:
vx(t) = V·cos(alpha)vy(t) = V·sin(alpha) – g·tx(t) = V·cos(alpha)·ty(t) = V·sin(alpha)·t – g·t2 / 2
Think of the acceleration of gravity g as equal to 9.8.

Bertown defends m walls. The i-th wall is represented as a vertical segment (xi, 0) - (xi, yi). When a ball hits a wall, it gets stuck in it and doesn't fly on. If a ball doesn't hit any wall it falls on the ground (y = 0) and stops. If the ball exactly hits the point (xi, yi), it is considered stuck.

Your task is to find for each ball the coordinates of the point where it will be located in the end.

The first line contains integers n and V (1 ≤ n ≤ 104, 1 ≤ V ≤ 1000) which represent the number of shots and the initial speed of every ball. The second line contains n space-separated real numbers alphai (0 < alphai < π / 4) which represent the angles in radians at which the cannon will fire. The third line contains integer m (1 ≤ m ≤ 105) which represents the number of walls. Then follow m lines, each containing two real numbers xi and yi (1 ≤ xi ≤ 1000, 0 ≤ yi ≤ 1000) which represent the wall’s coordinates. All the real numbers have no more than 4 decimal digits. The walls may partially overlap or even coincide.

Print n lines containing two real numbers each — calculate for every ball the coordinates of its landing point. Your answer should have the relative or absolute error less than 10 - 4.

## Input

The first line contains integers n and V (1 ≤ n ≤ 104, 1 ≤ V ≤ 1000) which represent the number of shots and the initial speed of every ball. The second line contains n space-separated real numbers alphai (0 < alphai < π / 4) which represent the angles in radians at which the cannon will fire. The third line contains integer m (1 ≤ m ≤ 105) which represents the number of walls. Then follow m lines, each containing two real numbers xi and yi (1 ≤ xi ≤ 1000, 0 ≤ yi ≤ 1000) which represent the wall’s coordinates. All the real numbers have no more than 4 decimal digits. The walls may partially overlap or even coincide.

## Output

Print n lines containing two real numbers each — calculate for every ball the coordinates of its landing point. Your answer should have the relative or absolute error less than 10 - 4.

## Samples

```
2 10
0.7853
0.3
3
5.0 5.0
4.0 2.4
6.0 1.9

```

```
5.000000000 2.549499369
4.000000000 0.378324889

```

```
2 10
0.7853
0.3
2
4.0 2.4
6.0 1.9

```

```
10.204081436 0.000000000
4.000000000 0.378324889

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-47E |
| Contest | 47 |
| Index | E |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `data structures`、`geometry`、`sortings` |
| 镜像标签 | `data structures`、`geometry`、`sortings`、`*2200` |
| Codeforces 通过次数 | 435 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/47/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/47/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P47E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

