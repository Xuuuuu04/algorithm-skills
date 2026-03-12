# CF-38D Vasya the Architect

## 题面快照

## Description

Once Vasya played bricks. All the bricks in the set had regular cubical shape. Vasya vas a talented architect, however the tower he built kept falling apart.

Let us consider the building process. Vasya takes a brick and puts it on top of the already built tower so that the sides of the brick are parallel to the sides of the bricks he has already used. Let's introduce a Cartesian coordinate system on the horizontal plane, where Vasya puts the first brick. Then the projection of brick number i on the plane is a square with sides parallel to the axes of coordinates with opposite corners in points (xi, 1, yi, 1) and (xi, 2, yi, 2). The bricks are cast from homogeneous plastic and the weight of a brick a × a × a is a3 grams.

It is guaranteed that Vasya puts any brick except the first one on the previous one, that is the area of intersection of the upper side of the previous brick and the lower side of the next brick is always positive.

We (Vasya included) live in a normal world where the laws of physical statics work. And that is why, perhaps, if we put yet another brick, the tower will collapse under its own weight. Vasya puts the cubes consecutively one on top of the other until at least one cube loses the balance and falls down. If it happens, Vasya gets upset and stops the construction. Print the number of bricks in the maximal stable tower, that is the maximal number m satisfying the condition that all the towers consisting of bricks 1, 2, ..., k for every integer k from 1 to m remain stable.

The first input file contains an integer n (1 ≤ n ≤ 100) which is the number of bricks. Each of the next n lines contains four numbers xi, 1, yi, 1, xi, 2, yi, 2 (xi, 1 ≠ xi, 2, |xi, 1 - xi, 2| = |yi, 1 - yi, 2|) which are the coordinates of the opposite angles of the base of the brick number i. The coordinates are integers and their absolute value does not exceed 50.

The cubes are given in the order Vasya puts them. It is guaranteed that the area of intersection of the upper side of the brick number i - 1 and the lower side of the brick number i is strictly strictly greater than zero for all i ≥ 2.

Print the number of bricks in the maximal stable tower.

## Input

The first input file contains an integer n (1 ≤ n ≤ 100) which is the number of bricks. Each of the next n lines contains four numbers xi, 1, yi, 1, xi, 2, yi, 2 (xi, 1 ≠ xi, 2, |xi, 1 - xi, 2| = |yi, 1 - yi, 2|) which are the coordinates of the opposite angles of the base of the brick number i. The coordinates are integers and their absolute value does not exceed 50.

The cubes are given in the order Vasya puts them. It is guaranteed that the area of intersection of the upper side of the brick number i - 1 and the lower side of the brick number i is strictly strictly greater than zero for all i ≥ 2.

## Output

Print the number of bricks in the maximal stable tower.

## Samples

```
2
0 0 3 3
1 0 4 3

```

```
2

```

```
2
0 0 3 3
2 0 5 3

```

```
1

```

```
3
0 0 3 3
1 0 4 3
2 0 5 3

```

```
3

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-38D |
| Contest | 38 |
| Index | D |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `implementation` |
| 镜像标签 | `implementation`、`*1900` |
| Codeforces 通过次数 | 1000 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/38/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/38/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P38D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

