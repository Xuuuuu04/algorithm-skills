# CF-91D Grocer's Problem

## 题面快照

## Description

Yesterday was a fair in a supermarket's grocery section. There were n jars with spices on the fair. Before the event the jars were numbered from 1 to n from the left to the right. After the event the jars were moved and the grocer had to sort them by the increasing of the numbers.

The grocer has a special machine at his disposal. The machine can take any 5 or less jars and rearrange them in the way the grocer wants. Note that the jars do not have to stand consecutively. For example, from the permutation 2, 6, 5, 4, 3, 1 one can get permutation 1, 2, 3, 4, 5, 6, if pick the jars on the positions 1, 2, 3, 5 and 6.

Which minimum number of such operations is needed to arrange all the jars in the order of their numbers' increasing?

The first line contains an integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers ai (1 ≤ ai ≤ n) — the i-th number represents the number of a jar that occupies the i-th position. It is guaranteed that all the numbers are distinct.

Print on the first line the least number of operations needed to rearrange all the jars in the order of the numbers' increasing. Then print the description of all actions in the following format.

On the first line of the description of one action indicate the number of jars that need to be taken (k), on the second line indicate from which positions the jars need to be taken (b1, b2, ..., bk), on the third line indicate the jar's new order (c1, c2, ..., ck). After the operation is fulfilled the jar from position bi will occupy the position ci. The set (c1, c2, ..., ck) should be the rearrangement of the set (b1, b2, ..., bk).

If there are multiple solutions, output any.

## Input

The first line contains an integer n (1 ≤ n ≤ 105). The second line contains n space-separated integers ai (1 ≤ ai ≤ n) — the i-th number represents the number of a jar that occupies the i-th position. It is guaranteed that all the numbers are distinct.

## Output

Print on the first line the least number of operations needed to rearrange all the jars in the order of the numbers' increasing. Then print the description of all actions in the following format.

On the first line of the description of one action indicate the number of jars that need to be taken (k), on the second line indicate from which positions the jars need to be taken (b1, b2, ..., bk), on the third line indicate the jar's new order (c1, c2, ..., ck). After the operation is fulfilled the jar from position bi will occupy the position ci. The set (c1, c2, ..., ck) should be the rearrangement of the set (b1, b2, ..., bk).

If there are multiple solutions, output any.

## Samples

```
6
3 5 6 1 2 4

```

```
2
4
1 3 6 4
3 6 4 1
2
2 5
5 2

```

```
14
9 13 11 3 10 7 12 14 1 5 4 6 8 2

```

```
3
4
2 13 8 14
13 8 14 2
5
6 7 12 5 10
7 12 6 10 5
5
3 11 4 1 9
11 4 3 9 1

```

## Note

Let's consider the first sample. The jars can be sorted within two actions.

During the first action we take the jars from positions 1, 3, 6 and 4 and put them so that the jar that used to occupy the position 1 will occupy the position 3 after the operation is completed. The jar from position 3 will end up in position 6, the jar from position 6 will end up in position 4 and the jar from position 4 will end up in position 1.

After the first action the order will look like that: 1, 5, 3, 4, 2, 6.

During the second operation the jars in positions 2 and 5 will change places.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-91D |
| Contest | 91 |
| Index | D |
| Rating | 2600 |
| Points | 2500.0 |
| Codeforces 标签 | `constructive algorithms`、`graphs`、`greedy` |
| 镜像标签 | `constructive algorithms`、`graphs`、`greedy`、`*2600` |
| Codeforces 通过次数 | 295 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/91/D)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/91/problem/D)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P91D)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

