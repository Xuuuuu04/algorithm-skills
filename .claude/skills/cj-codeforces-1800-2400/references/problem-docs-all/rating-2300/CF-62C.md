# CF-62C Inquisition

## 题面快照

## Description

In Medieval times existed the tradition of burning witches at steaks together with their pets, black cats. By the end of the 15-th century the population of black cats ceased to exist. The difficulty of the situation led to creating the EIC - the Emergency Inquisitory Commission.

The resolution #666 says that a white cat is considered black when and only when the perimeter of its black spots exceeds the acceptable norm. But what does the acceptable norm equal to? Every inquisitor will choose it himself depending on the situation. And your task is to find the perimeter of black spots on the cat's fur.

The very same resolution says that the cat's fur is a white square with the length of 105. During the measurement of spots it is customary to put the lower left corner of the fur into the origin of axes (0;0) and the upper right one — to the point with coordinates (105;105). The cats' spots are nondegenerate triangles. The spots can intersect and overlap with each other, but it is guaranteed that each pair of the triangular spots' sides have no more than one common point.

We'll regard the perimeter in this problem as the total length of the boarders where a cat's fur changes color.

The first input line contains a single integer n (0 ≤ n ≤ 100). It is the number of spots on the cat's fur. The i-th of the last n lines contains 6 integers: x1i, y1i, x2i, y2i, x3i, y3i. They are the coordinates of the i-th triangular spot (0 < xji, yji < 105).

Print a single number, the answer to the problem, perimeter of the union of triangles. Your answer should differ from the correct one in no more than 10 - 6.

## Input

The first input line contains a single integer n (0 ≤ n ≤ 100). It is the number of spots on the cat's fur. The i-th of the last n lines contains 6 integers: x1i, y1i, x2i, y2i, x3i, y3i. They are the coordinates of the i-th triangular spot (0 < xji, yji < 105).

## Output

Print a single number, the answer to the problem, perimeter of the union of triangles. Your answer should differ from the correct one in no more than 10 - 6.

## Samples

```
1
1 1 2 1 1 2

```

```
3.4142135624

```

```
3
3 3 10 3 3 10
1 1 9 4 5 6
2 2 11 7 6 11

```

```
37.7044021497

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-62C |
| Contest | 62 |
| Index | C |
| Rating | 2300 |
| Points | 1500.0 |
| Codeforces 标签 | `geometry`、`implementation`、`sortings` |
| 镜像标签 | `geometry`、`implementation`、`sortings`、`*2300` |
| Codeforces 通过次数 | 326 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 3000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/62/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/62/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P62C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

