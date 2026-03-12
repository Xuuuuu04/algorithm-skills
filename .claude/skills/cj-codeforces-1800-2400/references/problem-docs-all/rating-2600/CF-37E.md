# CF-37E Trial for Chief

## 题面快照

## Description

Having unraveled the Berland Dictionary, the scientists managed to read the notes of the chroniclers of that time. For example, they learned how the chief of the ancient Berland tribe was chosen.

As soon as enough pretenders was picked, the following test took place among them: the chief of the tribe took a slab divided by horizontal and vertical stripes into identical squares (the slab consisted of N lines and M columns) and painted every square black or white. Then every pretender was given a slab of the same size but painted entirely white. Within a day a pretender could paint any side-linked set of the squares of the slab some color. The set is called linked if for any two squares belonging to the set there is a path belonging the set on which any two neighboring squares share a side. The aim of each pretender is to paint his slab in the exactly the same way as the chief’s slab is painted. The one who paints a slab like that first becomes the new chief.

Scientists found the slab painted by the ancient Berland tribe chief. Help them to determine the minimal amount of days needed to find a new chief if he had to paint his slab in the given way.

The first line contains two integers N and M (1 ≤ N, M ≤ 50) — the number of lines and columns on the slab. The next N lines contain M symbols each — the final coloration of the slab. W stands for the square that should be painted white and B — for the square that should be painted black.

In the single line output the minimal number of repaintings of side-linked areas needed to get the required coloration of the slab.

## Input

The first line contains two integers N and M (1 ≤ N, M ≤ 50) — the number of lines and columns on the slab. The next N lines contain M symbols each — the final coloration of the slab. W stands for the square that should be painted white and B — for the square that should be painted black.

## Output

In the single line output the minimal number of repaintings of side-linked areas needed to get the required coloration of the slab.

## Samples

```
3 3
WBW
BWB
WBW

```

```
2

```

```
2 3
BBB
BWB

```

```
1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-37E |
| Contest | 37 |
| Index | E |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `graphs`、`greedy`、`shortest paths` |
| 镜像标签 | `graphs`、`greedy`、`shortest paths`、`*2600` |
| Codeforces 通过次数 | 672 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/37/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/37/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P37E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

