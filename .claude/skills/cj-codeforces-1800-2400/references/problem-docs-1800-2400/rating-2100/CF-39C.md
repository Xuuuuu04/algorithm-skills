# CF-39C Moon Craters

## 题面快照

## Description

There are lots of theories concerning the origin of moon craters. Most scientists stick to the meteorite theory, which says that the craters were formed as a result of celestial bodies colliding with the Moon. The other version is that the craters were parts of volcanoes.

An extraterrestrial intelligence research specialist professor Okulov (the namesake of the Okulov, the author of famous textbooks on programming) put forward an alternate hypothesis. Guess what kind of a hypothesis it was –– sure, the one including extraterrestrial mind involvement. Now the professor is looking for proofs of his hypothesis.

Professor has data from the moon robot that moves linearly in one direction along the Moon surface. The moon craters are circular in form with integer-valued radii. The moon robot records only the craters whose centers lay on his path and sends to the Earth the information on the distance from the centers of the craters to the initial point of its path and on the radii of the craters.

According to the theory of professor Okulov two craters made by an extraterrestrial intelligence for the aims yet unknown either are fully enclosed one in the other or do not intersect at all. Internal or external tangency is acceptable. However the experimental data from the moon robot do not confirm this theory! Nevertheless, professor Okulov is hopeful. He perfectly understands that to create any logical theory one has to ignore some data that are wrong due to faulty measuring (or skillful disguise by the extraterrestrial intelligence that will be sooner or later found by professor Okulov!) That’s why Okulov wants to choose among the available crater descriptions the largest set that would satisfy his theory.

The first line has an integer n (1 ≤ n ≤ 2000) — the number of discovered craters. The next n lines contain crater descriptions in the "ciri" format, where ci is the coordinate of the center of the crater on the moon robot’s path, ri is the radius of the crater. All the numbers ci and ri are positive integers not exceeding 109. No two craters coincide.

In the first line output the number of craters in the required largest set. In the next line output space-separated numbers of craters that this set consists of. The craters are numbered from 1 to n in the order in which they were given in the input data. The numbers may be output in any order. If the result is not unique, output any.

## Input

The first line has an integer n (1 ≤ n ≤ 2000) — the number of discovered craters. The next n lines contain crater descriptions in the "ciri" format, where ci is the coordinate of the center of the crater on the moon robot’s path, ri is the radius of the crater. All the numbers ci and ri are positive integers not exceeding 109. No two craters coincide.

## Output

In the first line output the number of craters in the required largest set. In the next line output space-separated numbers of craters that this set consists of. The craters are numbered from 1 to n in the order in which they were given in the input data. The numbers may be output in any order. If the result is not unique, output any.

## Samples

```
4
1 1
2 2
4 1
5 1

```

```
3
1 2 4

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-39C |
| Contest | 39 |
| Index | C |
| Rating | 2100 |
| Points | - |
| Codeforces 标签 | `dp`、`sortings` |
| 镜像标签 | `dp`、`sortings`、`*2100` |
| Codeforces 通过次数 | 695 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/39/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/39/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P39C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

