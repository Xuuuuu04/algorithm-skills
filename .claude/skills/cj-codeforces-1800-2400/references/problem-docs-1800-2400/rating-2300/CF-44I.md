# CF-44I Toys

## 题面快照

## Description

Little Masha loves arranging her toys into piles on the floor. And she also hates it when somebody touches her toys. One day Masha arranged all her n toys into several piles and then her elder brother Sasha came and gathered all the piles into one. Having seen it, Masha got very upset and started crying. Sasha still can't calm Masha down and mom is going to come home soon and punish Sasha for having made Masha crying. That's why he decides to restore the piles' arrangement. However, he doesn't remember at all the way the toys used to lie. Of course, Masha remembers it, but she can't talk yet and can only help Sasha by shouting happily when he arranges the toys in the way they used to lie. That means that Sasha will have to arrange the toys in every possible way until Masha recognizes the needed arrangement. The relative position of the piles and toys in every pile is irrelevant, that's why the two ways of arranging the toys are considered different if can be found two such toys that when arranged in the first way lie in one and the same pile and do not if arranged in the second way. Sasha is looking for the fastest way of trying all the ways because mom will come soon. With every action Sasha can take a toy from any pile and move it to any other pile (as a result a new pile may appear or the old one may disappear). Sasha wants to find the sequence of actions as a result of which all the pile arrangement variants will be tried exactly one time each. Help Sasha. As we remember, initially all the toys are located in one pile.

The first line contains an integer n (1 ≤ n ≤ 10) — the number of toys.

In the first line print the number of different variants of arrangement of toys into piles. Then print all the ways of arranging toys into piles in the order in which Sasha should try them (i.e. every next way must result from the previous one through the operation described in the statement). Every way should be printed in the following format. In every pile the toys should be arranged in ascending order of the numbers. Then the piles should be sorted in ascending order of the numbers of the first toys there. Output every way on a single line. Cf. the example to specify the output data format. If the solution is not unique, output any of them.

## Input

The first line contains an integer n (1 ≤ n ≤ 10) — the number of toys.

## Output

In the first line print the number of different variants of arrangement of toys into piles. Then print all the ways of arranging toys into piles in the order in which Sasha should try them (i.e. every next way must result from the previous one through the operation described in the statement). Every way should be printed in the following format. In every pile the toys should be arranged in ascending order of the numbers. Then the piles should be sorted in ascending order of the numbers of the first toys there. Output every way on a single line. Cf. the example to specify the output data format. If the solution is not unique, output any of them.

## Samples

```
3

```

```
5
{1,2,3}
{1,2},{3}
{1},{2,3}
{1},{2},{3}
{1,3},{2}

```

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / HydroOJ 镜像 |
| 编号 | CF-44I |
| Contest | 44 |
| Index | I |
| Rating | 2300 |
| Points | - |
| Codeforces 标签 | `brute force`、`combinatorics` |
| 镜像标签 | `brute force`、`combinatorics`、`*2300` |
| Codeforces 通过次数 | 228 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 5000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/44/I)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/44/problem/I)
- Hydro 镜像：[hydro](https://hydro.ac/p/codeforces-P44I)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

