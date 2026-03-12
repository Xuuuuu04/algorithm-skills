# CF-71C Round Table Knights

## 题面快照

## Description

There are n knights sitting at the Round Table at an equal distance from each other. Each of them is either in a good or in a bad mood.

Merlin, the wizard predicted to King Arthur that the next month will turn out to be particularly fortunate if the regular polygon can be found. On all vertices of the polygon knights in a good mood should be located. Otherwise, the next month will bring misfortunes.

A convex polygon is regular if all its sides have same length and all his angles are equal. In this problem we consider only regular polygons with at least 3 vertices, i. e. only nondegenerated.

On a picture below some examples of such polygons are present. Green points mean knights in a good mood. Red points mean ones in a bad mood.

King Arthur knows the knights' moods. Help him find out if the next month will be fortunate or not.

The first line contains number n, which is the number of knights at the round table (3 ≤ n ≤ 105). The second line contains space-separated moods of all the n knights in the order of passing them around the table. "1" means that the knight is in a good mood an "0" means that he is in a bad mood.

Print "YES" without the quotes if the following month will turn out to be lucky. Otherwise, print "NO".

## Input

The first line contains number n, which is the number of knights at the round table (3 ≤ n ≤ 105). The second line contains space-separated moods of all the n knights in the order of passing them around the table. "1" means that the knight is in a good mood an "0" means that he is in a bad mood.

## Output

Print "YES" without the quotes if the following month will turn out to be lucky. Otherwise, print "NO".

## Samples

```
3
1 1 1

```

```
YES

```

```
6
1 0 1 1 1 0

```

```
YES

```

```
6
1 0 0 1 0 1

```

```
NO

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-71C |
| Contest | 71 |
| Index | C |
| Rating | 1600 |
| Points | 1500.0 |
| Codeforces 标签 | `dp`、`math`、`number theory` |
| 镜像标签 | `dp`、`math`、`number theory`、`*1600` |
| Codeforces 通过次数 | 7271 |
| 镜像尝试 / 通过 | 1 / 1 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/71/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/71/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P71C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

