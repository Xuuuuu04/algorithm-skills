# CF-41E 3-cycles

## 题面快照

## Description

During a recent research Berland scientists found out that there were n cities in Ancient Berland, joined by two-way paths. Any two cities are joined by no more than one path. No path joins a city with itself. According to a well-known tradition, the road network was built so that it would be impossible to choose three cities from each of which one can get to any other one directly. That is, there was no cycle exactly as long as 3. Unfortunately, the road map has not been preserved till nowadays. Now the scientists are interested how much developed a country Ancient Berland was. Help them - find, what maximal number of roads could be in the country. You also have to restore any of the possible road maps.

The first line contains an integer n (1 ≤ n ≤ 100) — the number of cities in Berland.

On the first line must be printed number m — the maximal number of roads in Berland. Then print m lines containing two numbers each — the numbers of cities that the given road joins. The cities are numbered with integers from 1 to n. If there are several variants of solving the problem, print any of them.

## Input

The first line contains an integer n (1 ≤ n ≤ 100) — the number of cities in Berland.

## Output

On the first line must be printed number m — the maximal number of roads in Berland. Then print m lines containing two numbers each — the numbers of cities that the given road joins. The cities are numbered with integers from 1 to n. If there are several variants of solving the problem, print any of them.

## Samples

```
3

```

```
2
1 2
2 3

```

```
4

```

```
4
1 2
2 3
3 4
4 1

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-41E |
| Contest | 41 |
| Index | E |
| Rating | 1900 |
| Points | - |
| Codeforces 标签 | `constructive algorithms`、`graphs`、`greedy` |
| 镜像标签 | `constructive algorithms`、`graphs`、`greedy`、`*1900` |
| Codeforces 通过次数 | 2207 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/41/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/41/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P41E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

