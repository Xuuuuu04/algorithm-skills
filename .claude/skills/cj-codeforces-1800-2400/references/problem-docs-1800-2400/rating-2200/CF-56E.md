# CF-56E Domino Principle

## 题面快照

## Description

Vasya is interested in arranging dominoes. He is fed up with common dominoes and he uses the dominoes of different heights. He put n dominoes on the table along one axis, going from left to right. Every domino stands perpendicular to that axis so that the axis passes through the center of its base. The i-th domino has the coordinate xi and the height hi. Now Vasya wants to learn for every domino, how many dominoes will fall if he pushes it to the right. Help him do that.

Consider that a domino falls if it is touched strictly above the base. In other words, the fall of the domino with the initial coordinate x and height h leads to the fall of all dominoes on the segment [x + 1, x + h - 1].

The first line contains integer n (1 ≤ n ≤ 105) which is the number of dominoes. Then follow n lines containing two integers xi and hi ( - 108 ≤ xi ≤ 108, 2 ≤ hi ≤ 108) each, which are the coordinate and height of every domino. No two dominoes stand on one point.

Print n space-separated numbers zi — the number of dominoes that will fall if Vasya pushes the i-th domino to the right (including the domino itself).

## Input

The first line contains integer n (1 ≤ n ≤ 105) which is the number of dominoes. Then follow n lines containing two integers xi and hi ( - 108 ≤ xi ≤ 108, 2 ≤ hi ≤ 108) each, which are the coordinate and height of every domino. No two dominoes stand on one point.

## Output

Print n space-separated numbers zi — the number of dominoes that will fall if Vasya pushes the i-th domino to the right (including the domino itself).

## Samples

```
4
16 5
20 5
10 10
18 2

```

```
3 1 4 1

```

```
4
0 10
1 5
9 10
15 10

```

```
4 1 2 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-56E |
| Contest | 56 |
| Index | E |
| Rating | 2200 |
| Points | - |
| Codeforces 标签 | `binary search`、`data structures`、`sortings` |
| 镜像标签 | `binary search`、`data structures`、`sortings`、`*2200` |
| Codeforces 通过次数 | 2809 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/56/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/56/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P56E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

