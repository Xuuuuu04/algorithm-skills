# CF-39E What Has Dirichlet Got to Do with That?

## 题面快照

## Description

You all know the Dirichlet principle, the point of which is that if n boxes have no less than n + 1 items, that leads to the existence of a box in which there are at least two items.

Having heard of that principle, but having not mastered the technique of logical thinking, 8 year olds Stas and Masha invented a game. There are a different boxes and b different items, and each turn a player can either add a new box or a new item. The player, after whose turn the number of ways of putting b items into a boxes becomes no less then a certain given number n, loses. All the boxes and items are considered to be different. Boxes may remain empty.

Who loses if both players play optimally and Stas's turn is first?

The only input line has three integers a, b, n (1 ≤ a ≤ 10000, 1 ≤ b ≤ 30, 2 ≤ n ≤ 109) — the initial number of the boxes, the number of the items and the number which constrains the number of ways, respectively. Guaranteed that the initial number of ways is strictly less than n.

Output "Stas" if Masha wins. Output "Masha" if Stas wins. In case of a draw, output "Missing".

## Input

The only input line has three integers a, b, n (1 ≤ a ≤ 10000, 1 ≤ b ≤ 30, 2 ≤ n ≤ 109) — the initial number of the boxes, the number of the items and the number which constrains the number of ways, respectively. Guaranteed that the initial number of ways is strictly less than n.

## Output

Output "Stas" if Masha wins. Output "Masha" if Stas wins. In case of a draw, output "Missing".

## Samples

```
2 2 10

```

```
Masha

```

```
5 5 16808

```

```
Masha

```

```
3 1 4

```

```
Stas

```

```
1 4 10

```

```
Missing

```

## Note

In the second example the initial number of ways is equal to 3125.

-  If Stas increases the number of boxes, he will lose, as Masha may increase the number of boxes once more during her turn. After that any Stas's move will lead to defeat.

-  But if Stas increases the number of items, then any Masha's move will be losing.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-39E |
| Contest | 39 |
| Index | E |
| Rating | 2000 |
| Points | - |
| Codeforces 标签 | `dp`、`games` |
| 镜像标签 | `dp`、`games`、`*2000` |
| Codeforces 通过次数 | 1026 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 64MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/39/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/39/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P39E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

