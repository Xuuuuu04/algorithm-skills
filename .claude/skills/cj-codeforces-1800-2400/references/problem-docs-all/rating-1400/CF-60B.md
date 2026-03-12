# CF-60B Serial Time!

## 题面快照

## Description

The Cereal Guy's friend Serial Guy likes to watch soap operas. An episode is about to start, and he hasn't washed his plate yet. But he decided to at least put in under the tap to be filled with water. The plate can be represented by a parallelepiped k × n × m, that is, it has k layers (the first layer is the upper one), each of which is a rectangle n × m with empty squares ('.') and obstacles ('#'). The water can only be present in the empty squares. The tap is positioned above the square (x, y) of the first layer, it is guaranteed that this square is empty. Every minute a cubical unit of water falls into the plate. Find out in how many minutes the Serial Guy should unglue himself from the soap opera and turn the water off for it not to overfill the plate. That is, you should find the moment of time when the plate is absolutely full and is going to be overfilled in the next moment.

Note: the water fills all the area within reach (see sample 4). Water flows in each of the 6 directions, through faces of 1 × 1 × 1 cubes.

The first line contains three numbers k, n, m (1 ≤ k, n, m ≤ 10) which are the sizes of the plate. Then follow k rectangles consisting of n lines each containing m characters '.' or '#', which represents the "layers" of the plate in the order from the top to the bottom. The rectangles are separated by empty lines (see the samples). The last line contains x and y (1 ≤ x ≤ n, 1 ≤ y ≤ m) which are the tap's coordinates. x is the number of the line and y is the number of the column. Lines of each layer are numbered from left to right by the integers from 1 to n, columns of each layer are numbered from top to bottom by the integers from 1 to m.

The answer should contain a single number, showing in how many minutes the plate will be filled.

## Input

The first line contains three numbers k, n, m (1 ≤ k, n, m ≤ 10) which are the sizes of the plate. Then follow k rectangles consisting of n lines each containing m characters '.' or '#', which represents the "layers" of the plate in the order from the top to the bottom. The rectangles are separated by empty lines (see the samples). The last line contains x and y (1 ≤ x ≤ n, 1 ≤ y ≤ m) which are the tap's coordinates. x is the number of the line and y is the number of the column. Lines of each layer are numbered from left to right by the integers from 1 to n, columns of each layer are numbered from top to bottom by the integers from 1 to m.

## Output

The answer should contain a single number, showing in how many minutes the plate will be filled.

## Samples

```
1 1 1

.

1 1

```

```
1

```

```
2 1 1

.

#

1 1

```

```
1

```

```
2 2 2

.#
##

..
..

1 1

```

```
5

```

```
3 2 2

#.
##

#.
.#

..
..

1 2

```

```
7

```

```
3 3 3

.#.
###
##.

.##
###
##.

...
...
...

1 1

```

```
13

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-60B |
| Contest | 60 |
| Index | B |
| Rating | 1400 |
| Points | 1000.0 |
| Codeforces 标签 | `dfs and similar`、`dsu` |
| 镜像标签 | `dfs and similar`、`dsu`、`*1400` |
| Codeforces 通过次数 | 5228 |
| 镜像尝试 / 通过 | 1 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/60/B)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/60/problem/B)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P60B)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

