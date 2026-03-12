# CF-55E Very simple problem

## 题面快照

## Description

You are given a convex polygon. Count, please, the number of triangles that contain a given point in the plane and their vertices are the vertices of the polygon. It is guaranteed, that the point doesn't lie on the sides and the diagonals of the polygon.

The first line contains integer n — the number of vertices of the polygon (3 ≤ n ≤ 100000). The polygon description is following: n lines containing coordinates of the vertices in clockwise order (integer x and y not greater than 109 by absolute value). It is guaranteed that the given polygon is nondegenerate and convex (no three points lie on the same line).

The next line contains integer t (1 ≤ t ≤ 20) — the number of points which you should count the answer for. It is followed by t lines with coordinates of the points (integer x and y not greater than 109 by absolute value).

The output should contain t integer numbers, each on a separate line, where i-th number is the answer for the i-th point.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

## Input

The first line contains integer n — the number of vertices of the polygon (3 ≤ n ≤ 100000). The polygon description is following: n lines containing coordinates of the vertices in clockwise order (integer x and y not greater than 109 by absolute value). It is guaranteed that the given polygon is nondegenerate and convex (no three points lie on the same line).

The next line contains integer t (1 ≤ t ≤ 20) — the number of points which you should count the answer for. It is followed by t lines with coordinates of the points (integer x and y not greater than 109 by absolute value).

## Output

The output should contain t integer numbers, each on a separate line, where i-th number is the answer for the i-th point.

Please, do not use %lld specificator to read or write 64-bit integers in C++. It is preffered to use cin (also you may use %I64d).

## Samples

```
4
5 0
0 0
0 5
5 5
1
1 3

```

```
2

```

```
3
0 0
0 5
5 0
2
1 1
10 10

```

```
1
0

```

```
5
7 6
6 3
4 1
1 2
2 4
4
3 3
2 3
5 5
4 2

```

```
5
3
3
4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-55E |
| Contest | 55 |
| Index | E |
| Rating | 2500 |
| Points | 2500.0 |
| Codeforces 标签 | `geometry`、`two pointers` |
| 镜像标签 | `geometry`、`two pointers`、`*2500` |
| Codeforces 通过次数 | 801 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/55/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/55/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P55E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

