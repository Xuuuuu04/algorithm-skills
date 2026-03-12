# CF-50C Happy Farm 5

## 题面快照

## Description

The Happy Farm 5 creators decided to invent the mechanism of cow grazing. The cows in the game are very slow and they move very slowly, it can even be considered that they stand still. However, carnivores should always be chased off them.

For that a young player Vasya decided to make the shepherd run round the cows along one and the same closed path. It is very important that the cows stayed strictly inside the area limited by the path, as otherwise some cows will sooner or later be eaten. To be absolutely sure in the cows' safety, Vasya wants the path completion time to be minimum.

The new game is launched for different devices, including mobile phones. That's why the developers decided to quit using the arithmetics with the floating decimal point and use only the arithmetics of integers. The cows and the shepherd in the game are represented as points on the plane with integer coordinates. The playing time is modeled by the turns. During every turn the shepherd can either stay where he stands or step in one of eight directions: horizontally, vertically, or diagonally. As the coordinates should always remain integer, then the length of a horizontal and vertical step is equal to 1, and the length of a diagonal step is equal to . The cows do not move. You have to minimize the number of moves the shepherd needs to run round the whole herd.

The first line contains an integer N which represents the number of cows in the herd (1 ≤ N ≤ 105). Each of the next N lines contains two integers Xi and Yi which represent the coordinates of one cow of (|Xi|, |Yi| ≤ 106). Several cows can stand on one point.

Print the single number — the minimum number of moves in the sought path.

## Input

The first line contains an integer N which represents the number of cows in the herd (1 ≤ N ≤ 105). Each of the next N lines contains two integers Xi and Yi which represent the coordinates of one cow of (|Xi|, |Yi| ≤ 106). Several cows can stand on one point.

## Output

Print the single number — the minimum number of moves in the sought path.

## Samples

```
4
1 1
5 1
5 3
1 3

```

```
16

```

## Note

Picture for the example test: The coordinate grid is painted grey, the coordinates axes are painted black, the cows are painted red and the sought route is painted green.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-50C |
| Contest | 50 |
| Index | C |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `geometry` |
| 镜像标签 | `geometry`、`*2000` |
| Codeforces 通过次数 | 860 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/50/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/50/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P50C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

