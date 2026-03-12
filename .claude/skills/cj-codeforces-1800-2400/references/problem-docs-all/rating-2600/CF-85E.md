# CF-85E Guard Towers

## 题面快照

## Description

In a far away kingdom lives a very greedy king. To defend his land, he built n guard towers. Apart from the towers the kingdom has two armies, each headed by a tyrannical and narcissistic general. The generals can't stand each other, specifically, they will never let soldiers of two armies be present in one tower.

During defence operations to manage a guard tower a general has to send part of his army to that tower. Each general asks some fee from the king for managing towers. As they live in a really far away kingdom, each general evaluates his fee in the following weird manner: he finds two remotest (the most distant) towers, where the soldiers of his army are situated and asks for the fee equal to the distance. Each tower is represented by a point on the plane with coordinates (x, y), and the distance between two points with coordinates (x1, y1) and (x2, y2) is determined in this kingdom as |x1 - x2| + |y1 - y2|.

The greedy king was not exactly satisfied with such a requirement from the generals, that's why he only agreed to pay one fee for two generals, equal to the maximum of two demanded fees. However, the king is still green with greed, and among all the ways to arrange towers between armies, he wants to find the cheapest one. Each tower should be occupied by soldiers of exactly one army.

He hired you for that. You should find the minimum amount of money that will be enough to pay the fees. And as the king is also very scrupulous, you should also count the number of arrangements that will cost the same amount of money. As their number can be quite large, it is enough for the king to know it as a remainder from dividing by 109 + 7.

Two arrangements are distinct if the sets of towers occupied by soldiers of the first general are distinct.

The first line contains an integer n (2 ≤ n ≤ 5000), n is the number of guard towers. Then follow n lines, each of which contains two integers x, y — the coordinates of the i-th tower (0 ≤ x, y ≤ 5000). No two towers are present at one point.

Pretest 6 is one of the maximal tests for this problem.

Print on the first line the smallest possible amount of money that will be enough to pay fees to the generals.

Print on the second line the number of arrangements that can be carried out using the smallest possible fee. This number should be calculated modulo 1000000007 (109 + 7).

## Input

The first line contains an integer n (2 ≤ n ≤ 5000), n is the number of guard towers. Then follow n lines, each of which contains two integers x, y — the coordinates of the i-th tower (0 ≤ x, y ≤ 5000). No two towers are present at one point.

Pretest 6 is one of the maximal tests for this problem.

## Output

Print on the first line the smallest possible amount of money that will be enough to pay fees to the generals.

Print on the second line the number of arrangements that can be carried out using the smallest possible fee. This number should be calculated modulo 1000000007 (109 + 7).

## Samples

```
2
0 0
1 1

```

```
0
2

```

```
4
0 0
0 1
1 0
1 1

```

```
1
4

```

```
3
0 0
1000 1000
5000 5000

```

```
2000
2

```

## Note

In the first example there are only two towers, the distance between which is equal to 2. If we give both towers to one general, then we well have to pay 2 units of money. If each general receives a tower to manage, to fee will be equal to 0. That is the smallest possible fee. As you can easily see, we can obtain it in two ways.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-85E |
| Contest | 85 |
| Index | E |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `binary search`、`dsu`、`geometry`、`graphs`、`sortings` |
| 镜像标签 | `binary search`、`dsu`、`geometry`、`graphs`、`sortings`、`*2600` |
| Codeforces 通过次数 | 1072 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 1000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/85/E)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/85/problem/E)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P85E)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

