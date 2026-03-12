# CF-58C Trees

## 题面快照

## Description

On Bertown's main street n trees are growing, the tree number i has the height of ai meters (1 ≤ i ≤ n). By the arrival of the President of Berland these trees were decided to be changed so that their heights formed a beautiful sequence. This means that the heights of trees on ends (the 1st one and the n-th one) should be equal to each other, the heights of the 2-nd and the (n - 1)-th tree must also be equal to each other, at that the height of the 2-nd tree should be larger than the height of the first tree by 1, and so on. In other words, the heights of the trees, standing at equal distance from the edge (of one end of the sequence) must be equal to each other, and with the increasing of the distance from the edge by 1 the tree height must also increase by 1. For example, the sequences "2 3 4 5 5 4 3 2" and "1 2 3 2 1" are beautiful, and '1 3 3 1" and "1 2 3 1" are not.

Changing the height of a tree is a very expensive operation, using advanced technologies invented by Berland scientists. In one operation you can choose any tree and change its height to any number, either increase or decrease. Note that even after the change the height should remain a positive integer, i. e, it can't be less than or equal to zero. Identify the smallest number of changes of the trees' height needed for the sequence of their heights to become beautiful.

The first line contains integer n (1 ≤ n ≤ 105) which is the number of trees. The second line contains integers ai (1 ≤ ai ≤ 105) which are the heights of the trees.

Print a single number which is the minimal number of trees whose heights will have to be changed for the sequence to become beautiful.

## Input

The first line contains integer n (1 ≤ n ≤ 105) which is the number of trees. The second line contains integers ai (1 ≤ ai ≤ 105) which are the heights of the trees.

## Output

Print a single number which is the minimal number of trees whose heights will have to be changed for the sequence to become beautiful.

## Samples

```
3
2 2 2

```

```
1

```

```
4
1 2 2 1

```

```
0

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-58C |
| Contest | 58 |
| Index | C |
| Rating | 1800 |
| Points | - |
| Codeforces 标签 | `brute force` |
| 镜像标签 | `brute force`、`*1800` |
| Codeforces 通过次数 | 2248 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/58/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/58/problem/C)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P58C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

