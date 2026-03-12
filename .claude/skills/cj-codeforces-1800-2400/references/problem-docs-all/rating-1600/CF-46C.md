# CF-46C Hamsters and Tigers

## 题面快照

## Description

Today there is going to be an unusual performance at the circus — hamsters and tigers will perform together! All of them stand in circle along the arena edge and now the trainer faces a difficult task: he wants to swap the animals' positions so that all the hamsters stood together and all the tigers also stood together. The trainer swaps the animals in pairs not to create a mess. He orders two animals to step out of the circle and swap places. As hamsters feel highly uncomfortable when tigers are nearby as well as tigers get nervous when there's so much potential prey around (consisting not only of hamsters but also of yummier spectators), the trainer wants to spend as little time as possible moving the animals, i.e. he wants to achieve it with the minimal number of swaps. Your task is to help him.

The first line contains number n (2 ≤ n ≤ 1000) which indicates the total number of animals in the arena. The second line contains the description of the animals' positions. The line consists of n symbols "H" and "T". The "H"s correspond to hamsters and the "T"s correspond to tigers. It is guaranteed that at least one hamster and one tiger are present on the arena. The animals are given in the order in which they are located circle-wise, in addition, the last animal stands near the first one.

Print the single number which is the minimal number of swaps that let the trainer to achieve his goal.

## Input

The first line contains number n (2 ≤ n ≤ 1000) which indicates the total number of animals in the arena. The second line contains the description of the animals' positions. The line consists of n symbols "H" and "T". The "H"s correspond to hamsters and the "T"s correspond to tigers. It is guaranteed that at least one hamster and one tiger are present on the arena. The animals are given in the order in which they are located circle-wise, in addition, the last animal stands near the first one.

## Output

Print the single number which is the minimal number of swaps that let the trainer to achieve his goal.

## Samples

```
3
HTH

```

```
0

```

```
9
HTHTHTHHT

```

```
2

```

## Note

In the first example we shouldn't move anybody because the animals of each species already stand apart from the other species. In the second example you may swap, for example, the tiger in position 2 with the hamster in position 5 and then — the tiger in position 9 with the hamster in position 7.

## 元信息

| 字段 | 内容 |
|---|---|
| 来源 | Codeforces / Hydro 镜像 |
| 编号 | CF-46C |
| Contest | 46 |
| Index | C |
| Rating | 1600 |
| Points | - |
| Codeforces 标签 | `two pointers` |
| 镜像标签 | `two pointers`、`*1600` |
| Codeforces 通过次数 | 2852 |
| 镜像尝试 / 通过 | 0 / 0 |
| 时限 | 2000ms |
| 内存限制 | 256MiB |

## 远端入口

- Codeforces 题面：[problem](https://codeforces.com/problemset/problem/46/C)
- Codeforces 提交列表：[status](https://codeforces.com/problemset/status/46/problem/C)
- Hydro 镜像：[mirror](https://hydro.ac/p/codeforces-P46C)

## 本地补充位

这里继续补写解题思路、仓颉实现、边界样例和错题复盘。

