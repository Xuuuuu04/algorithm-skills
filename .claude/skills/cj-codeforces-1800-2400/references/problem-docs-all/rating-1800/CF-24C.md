# CF-24C Sequence of points

## 题面快照

## Description

You are given the following points with integer coordinates on the plane: M0, A0, A1, ..., An - 1, where n is odd number. Now we define the following infinite sequence of points Mi: Mi is symmetric to Mi - 1 according  (for every natural number i). Here point B is symmetric to A according M, if M is the center of the line segment AB. Given index j find the point Mj.

On the first line you will be given an integer n (1 ≤ n ≤ 105), which will be odd, and j (1 ≤ j ≤ 1018), where j is the index of the desired point. The next line contains two space separated integers, the coordinates of M0. After that n lines follow, where the i-th line contain the space separated integer coordinates of the point Ai - 1. The absolute values of all input coordinates will not be greater then 1000.

On a single line output the coordinates of Mj, space separated.

## Input

On the first line you will be given an integer n (1 ≤ n ≤ 105), which will be odd, and j (1 ≤ j ≤ 1018), where j is the index of the desired point. The next line contains two space separated integers, the coordinates of M0. After that n lines follow, where the i-th line contain the space separated integer coordinates of the point Ai - 1. The absolute values of all input coordinates will not be greater then 1000.

## Output

On a single line output the coordinates of Mj, space separated.

## Samples

```
3 4
0 0
1 1
2 3
-5 3

```

```
14 0

```

```
3 1
5 5
1000 1000
-1000 1000
3 100

```

```
1995 1995

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-24C |
| Contest | 24 |
| Index | C |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `geometry`、`implementation`、`math` |
| 镜像标签 | `geometry`、`implementation`、`math`、`*1800` |
| Codeforces 通过次数 | 1408 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/24/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/24/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P24C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

