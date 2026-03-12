# CF-73E Morrowindows

## 题面快照

## Description

Vasya plays The Elder Trolls III: Morrowindows. He has a huge list of items in the inventory, however, there is no limits on the size of things. Vasya does not know the total amount of items but he is sure that are not more than x and not less than 2 items in his inventory. A new patch for the game appeared to view inventory in n different modes. Displaying in mode i is a partition of all inventory items on pages, each of which (except for maybe the last one) shows exactly ai items. In addition, each mode shows how many pages bi is in a complete list. Great! Perhaps this information will be enough for Vasya to find the required number. Moreover, it is very interesting, what is the fewest number of modes in which Vasya can see inventory to determine the number of items in it?

Vasya cannot use the information that was received while looking on inventory in some mode for selection of next actions. I. e. Vasya chooses some set of modes first, and then sees all the results and determines the size.

Knowing the number of ai, x and assuming that Vasya is very smart, check whether he can uniquely determine the number of items in his inventory, and how many modes he will need to do that if he knows numbers ai, x and he is able to know number bi after viewing items in mode i.

The first line contains two integers n and x (0 ≤ n ≤ 105, 2 ≤ x ≤ 109). The second line contains integers ai (1 ≤ ai ≤ 109). Some numbers among all ai may be equal.

Output the fewest amount of modes required to uniquely determine amount of items in the inventory. If there is no solution output  - 1.

## Input

The first line contains two integers n and x (0 ≤ n ≤ 105, 2 ≤ x ≤ 109). The second line contains integers ai (1 ≤ ai ≤ 109). Some numbers among all ai may be equal.

## Output

Output the fewest amount of modes required to uniquely determine amount of items in the inventory. If there is no solution output  - 1.

## Samples

```
2 4
2 3

```

```
2

```

```
1 4
2

```

```
-1

```

## Note

In the second example Vasya is not able to determine items count uniquely because 3 items, as well as 4 items, can be displayed on two pages.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-73E |
| Contest | 73 |
| Index | E |
| Rating | 2400 |
| Points | - |
| Codeforces 标签 | `math`、`number theory` |
| 镜像标签 | `math`、`number theory`、`*2400` |
| Codeforces 通过次数 | 401 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/73/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/73/problem/E)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P73E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

